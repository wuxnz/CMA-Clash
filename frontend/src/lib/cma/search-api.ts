// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { fetchWithRetry } from '$lib/api/http';
import { kitOrBackendFetch } from '$lib/server-api';

/** FastAPI mounts search at `/api/v1/search` (no trailing slash). */
export const SEARCH_API_PATH = '/api/v1/search';

export type SearchHit = {
	id: string;
	title: string;
	description: string;
	user: string;
	imported_from_kahoot?: boolean | null;
	_formatted?: SearchHit;
};

export type SearchResponse = {
	hits: SearchHit[];
	query: string;
	limit: number;
	offset: number;
	processingTimeMs: number;
};

export async function postSearch(
	fetchFn: typeof fetch,
	body: Record<string, unknown>
): Promise<SearchResponse | null> {
	const res = await kitOrBackendFetch(fetchFn, SEARCH_API_PATH, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify(body)
	});
	if (!res?.ok) {
		return null;
	}
	return (await res.json()) as SearchResponse;
}

/** Browser retry for cold starts / transient proxy errors. */
export async function postSearchClient(
	body: Record<string, unknown>
): Promise<SearchResponse | null> {
	const res = await fetchWithRetry(SEARCH_API_PATH, {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		credentials: 'include',
		body: JSON.stringify(body)
	});
	if (!res?.ok) {
		return null;
	}
	return (await res.json()) as SearchResponse;
}
