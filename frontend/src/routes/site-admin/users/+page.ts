// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { redirect } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
	const res = await fetch('/api/v1/admin/me', { credentials: 'include' });
	if (res.status === 401) {
		throw redirect(302, '/account/login?returnTo=/site-admin/users');
	}
	if (res.status === 403 || !res.ok) {
		throw redirect(302, '/dashboard');
	}
	return {};
};
