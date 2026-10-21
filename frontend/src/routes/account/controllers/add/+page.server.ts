// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { ssrBackendFetchWithRequest } from '$lib/server-api';

export const load: PageServerLoad = async ({ parent, request }) => {
	const { email } = await parent();
	if (!email) {
		redirect(302, '/account/login?returnTo=/account/controllers/add');
	}
	const resp = await ssrBackendFetchWithRequest(request, '/api/v1/users/me');
	if (!resp?.ok) {
		return { username: null };
	}
	const json = await resp.json();
	return { username: json.username ?? null };
};
