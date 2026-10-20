import { browser } from '$app/environment';
import type { Certification, QuizBrowseItem } from '$lib/cma/client';
import { serverApiUrl } from '$lib/server-api';
import { certLabelFor, certSlugFor, prettyDifficulty, stripHighlight } from './labels';
import type { QuizRowItem } from './QuizRow.svelte';

function apiUrl(path: string): string {
	return browser ? path : serverApiUrl(path);
}

export type MeiliHit = {
	id: string;
	title?: string;
	description?: string;
	user?: string | null;
	created_at?: number;
	imported_from_kahoot?: boolean;
	_formatted?: {
		title?: string;
		description?: string;
		user?: string;
	};
};

export type SearchResponse = {
	hits: MeiliHit[];
	query: string;
	limit: number;
	offset: number;
	processingTimeMs?: number;
};

export type BrowseRow = QuizRowItem & {
	created_at?: number;
	certification_id?: string | null;
};

const PAGE_SIZE = 20;

export function searchPageSize(): number {
	return PAGE_SIZE;
}

async function apiFetch(path: string, init?: RequestInit): Promise<Response> {
	return globalThis.fetch(apiUrl(path), init);
}

export async function searchMeili(
	_fetchFn: typeof fetch,
	opts: { q: string; offset?: number; limit?: number; sort?: string[] }
): Promise<SearchResponse> {
	const q = opts.q.trim().length ? opts.q : '*';
	try {
		const res = await apiFetch('/api/v1/search/', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({
				q,
				offset: opts.offset ?? 0,
				limit: opts.limit ?? PAGE_SIZE,
				attributesToHighlight: ['*'],
				sort: opts.sort
			})
		});
		if (!res.ok) {
			return { hits: [], query: q, limit: opts.limit ?? PAGE_SIZE, offset: opts.offset ?? 0 };
		}
		const raw = (await res.text()).replaceAll('<em>', '<mark>').replaceAll('</em>', '</mark>');
		const data = JSON.parse(raw) as SearchResponse;
		return {
			hits: Array.isArray(data.hits) ? data.hits : [],
			query: data.query ?? q,
			limit: data.limit ?? opts.limit ?? PAGE_SIZE,
			offset: data.offset ?? opts.offset ?? 0,
			processingTimeMs: data.processingTimeMs
		};
	} catch {
		return { hits: [], query: q, limit: opts.limit ?? PAGE_SIZE, offset: opts.offset ?? 0 };
	}
}

export async function fetchClashQuizzes(
	fetchFn: typeof fetch,
	params: {
		certification_slug?: string;
		difficulty?: string;
		page?: number;
		page_size?: number;
	} = {}
): Promise<QuizBrowseItem[]> {
	const search = new URLSearchParams();
	if (params.certification_slug) search.set('certification_slug', params.certification_slug);
	if (params.difficulty) search.set('difficulty', params.difficulty);
	if (params.page) search.set('page', String(params.page));
	search.set('page_size', String(params.page_size ?? PAGE_SIZE));
	try {
			const res = await apiFetch(`/api/v1/clash/quizzes?${search}`);
		if (!res.ok) return [];
		const data = await res.json();
		return Array.isArray(data) ? data : [];
	} catch {
		return [];
	}
}

export async function fetchCerts(fetchFn: typeof fetch): Promise<Certification[]> {
	try {
			const res = await apiFetch('/api/v1/clash/certifications');
		if (!res.ok) return [];
		const data = await res.json();
		return Array.isArray(data) ? data : [];
	} catch {
		return [];
	}
}

export function clashMap(items: QuizBrowseItem[]): Map<string, QuizBrowseItem> {
	return new Map(items.map((item) => [String(item.id), item]));
}

export function clashByTitle(items: QuizBrowseItem[]): Map<string, QuizBrowseItem> {
	return new Map(items.map((item) => [item.title.toLowerCase(), item]));
}

export function findClash(
	hit: MeiliHit,
	byId: Map<string, QuizBrowseItem>,
	byTitle: Map<string, QuizBrowseItem>
): QuizBrowseItem | undefined {
	const title = stripHighlight(hit._formatted?.title ?? hit.title).toLowerCase();
	return byId.get(String(hit.id)) ?? (title ? byTitle.get(title) : undefined);
}

export async function fetchClashCatalog(
	fetchFn: typeof fetch,
	maxPages = 6
): Promise<QuizBrowseItem[]> {
	const all: QuizBrowseItem[] = [];
	for (let page = 1; page <= maxPages; page++) {
		const batch = await fetchClashQuizzes(fetchFn, { page, page_size: 100 });
		all.push(...batch);
		if (batch.length < 100) break;
	}
	return all;
}

export function rowsFromMeili(
	hits: MeiliHit[],
	clashItems: QuizBrowseItem[],
	certs: Certification[],
	cert: string,
	difficulty: string,
	sort: string
): BrowseRow[] {
	const byId = clashMap(clashItems);
	const byTitle = clashByTitle(clashItems);
	return sortRows(
		filterRows(
			hits.map((hit) => mergeHit(hit, findClash(hit, byId, byTitle), certs)),
			cert,
			difficulty,
			certs
		),
		sort
	);
}

export function rowsFromClash(
	items: QuizBrowseItem[],
	certs: Certification[],
	users: Map<string, string>,
	sort: string
): BrowseRow[] {
	return sortRows(
		items.map((item) => rowFromClash(item, certs, users)),
		sort === 'relevance' ? 'newest' : sort
	);
}

export function mergeHit(
	hit: MeiliHit,
	clash: QuizBrowseItem | undefined,
	certs: Certification[]
): BrowseRow {
	const title = stripHighlight(hit._formatted?.title ?? hit.title);
	return {
		id: String(hit.id),
		title,
		user: stripHighlight(hit._formatted?.user ?? hit.user ?? undefined) || null,
		created_at: hit.created_at,
		difficulty: prettyDifficulty(clash?.difficulty),
		question_count: clash?.question_count,
		plays: clash?.plays,
		certification_id: clash?.certification_id ? String(clash.certification_id) : null,
		certLabel: certLabelFor(
			{ certification_id: clash?.certification_id ? String(clash.certification_id) : null, title },
			certs
		)
	};
}

export function rowFromClash(
	item: QuizBrowseItem,
	certs: Certification[],
	users: Map<string, string>
): BrowseRow {
	const title = item.title;
	return {
		id: String(item.id),
		title,
		user: users.get(String(item.id)) ?? users.get(title.toLowerCase()) ?? null,
		difficulty: prettyDifficulty(item.difficulty),
		question_count: item.question_count,
		plays: item.plays,
		certification_id: item.certification_id ? String(item.certification_id) : null,
		certLabel: certLabelFor(
			{ certification_id: item.certification_id ? String(item.certification_id) : null, title },
			certs
		)
	};
}

export function userMapFromHits(hits: MeiliHit[]): Map<string, string> {
	const map = new Map<string, string>();
	for (const hit of hits) {
		const name = stripHighlight(hit._formatted?.user ?? hit.user ?? undefined);
		if (!name) continue;
		map.set(String(hit.id), name);
		const title = stripHighlight(hit._formatted?.title ?? hit.title).toLowerCase();
		if (title) map.set(title, name);
	}
	return map;
}

export function filterRows(
	rows: BrowseRow[],
	cert: string,
	difficulty: string,
	certs: Certification[]
): BrowseRow[] {
	const wantDiff = difficulty.toLowerCase();
	return rows.filter((row) => {
		if (cert && certSlugFor(row, certs) !== cert) return false;
		if (wantDiff && (row.difficulty ?? '').toLowerCase() !== wantDiff) return false;
		return true;
	});
}

export function sortRows(rows: BrowseRow[], sort: string): BrowseRow[] {
	if (sort === 'newest') {
		return [...rows].sort((a, b) => (b.created_at ?? 0) - (a.created_at ?? 0));
	}
	if (sort === 'plays') {
		return [...rows].sort((a, b) => (b.plays ?? 0) - (a.plays ?? 0));
	}
	return rows;
}

export function meiliSort(sort: string): string[] | undefined {
	return sort === 'newest' ? ['created_at:desc'] : undefined;
}
