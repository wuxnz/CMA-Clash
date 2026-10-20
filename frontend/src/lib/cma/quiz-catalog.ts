// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { fetchWithRetry } from '$lib/api/http';
import { kitOrBackendFetch } from '$lib/server-api';
import type { QuizBrowseItem } from '$lib/cma/client';

async function fetchCatalog(
	fetchFn: typeof fetch,
	query: string
): Promise<QuizBrowseItem[]> {
	const res = await kitOrBackendFetch(fetchFn, `/api/v1/clash/quizzes?${query}`);
	if (!res?.ok) {
		return [];
	}
	return (await res.json()) as QuizBrowseItem[];
}

/** Load public clash quizzes (SSR-safe). */
export async function loadPublicQuizCatalog(fetchFn: typeof fetch): Promise<QuizBrowseItem[]> {
	const ccma = await fetchCatalog(fetchFn, 'page_size=50&certification_slug=ccma');
	if (ccma.length > 0) {
		return ccma;
	}
	return fetchCatalog(fetchFn, 'page_size=50');
}

/** Browser-only retry for cold starts after SSR miss. */
export async function loadPublicQuizCatalogClient(): Promise<QuizBrowseItem[]> {
	const tryQuery = async (query: string) => {
		const res = await fetchWithRetry(`/api/v1/clash/quizzes?${query}`, {
			credentials: 'include'
		});
		if (!res?.ok) {
			return [] as QuizBrowseItem[];
		}
		return (await res.json()) as QuizBrowseItem[];
	};
	const ccma = await tryQuery('page_size=50&certification_slug=ccma');
	if (ccma.length > 0) {
		return ccma;
	}
	return tryQuery('page_size=50');
}
