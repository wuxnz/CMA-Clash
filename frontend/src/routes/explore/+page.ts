// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { PageLoad } from './$types';
import { kitOrBackendFetch } from '$lib/server-api';

const emptyResults = { hits: [] as unknown[] };

export const load = (async ({ fetch }) => {
	try {
		const response = await kitOrBackendFetch(fetch, '/api/v1/search/', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				q: '*',
				sort: ['created_at:desc']
			})
		});
		if (!response?.ok) {
			return { results: emptyResults, exploreSsrFailed: true };
		}
		return { results: await response.json(), exploreSsrFailed: false };
	} catch {
		return { results: emptyResults, exploreSsrFailed: true };
	}
}) satisfies PageLoad;
