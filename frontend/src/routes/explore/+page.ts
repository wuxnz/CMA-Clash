// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { PageLoad } from './$types';
import { postSearch, type SearchResponse } from '$lib/cma/search-api';

const emptyResults: SearchResponse = {
	hits: [],
	query: '*',
	limit: 20,
	offset: 0,
	processingTimeMs: 0
};

export const load = (async ({ fetch }) => {
	try {
		const results = await postSearch(fetch, { q: '*', sort: ['created_at:desc'] });
		if (!results) {
			return { results: emptyResults, exploreSsrFailed: true };
		}
		return { results, exploreSsrFailed: false };
	} catch {
		return { results: emptyResults, exploreSsrFailed: true };
	}
}) satisfies PageLoad;
