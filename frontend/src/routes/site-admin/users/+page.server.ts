// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { ssrBackendFetchWithRequest } from '$lib/server-api';

export const load: PageServerLoad = async ({ parent, request }) => {
	const { email } = await parent();
	if (!email) {
		redirect(302, '/account/login?returnTo=/site-admin/users');
	}
	const res = await ssrBackendFetchWithRequest(request, '/api/v1/admin/me');
	if (!res) {
		redirect(302, '/account/login?returnTo=/site-admin/users');
	}
	if (res.status === 401) {
		redirect(302, '/account/login?returnTo=/site-admin/users');
	}
	if (res.status === 403 || !res.ok) {
		redirect(302, '/dashboard');
	}
	return {};
};
