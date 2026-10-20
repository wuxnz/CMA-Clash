// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { error } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { kitOrBackendFetch } from '$lib/server-api';

export const load: PageServerLoad = async ({ params, parent, fetch }) => {
	const { quiz_id } = params;
	const res = await kitOrBackendFetch(fetch, `/api/v1/quiz/get/public/${quiz_id}`);
	const { email } = await parent();
	if (!res) {
		error(503, 'Could not reach the quiz service. Please try again in a moment.');
	}
	if (res.status === 404 || res.status === 400 || res.status === 422) {
		error(404);
	}
	if (!res.ok) {
		error(503, 'Quiz data is temporarily unavailable. Please try again.');
	}
	const quiz = await res.json();
	return {
		quiz,
		logged_in: Boolean(email)
	};
};
