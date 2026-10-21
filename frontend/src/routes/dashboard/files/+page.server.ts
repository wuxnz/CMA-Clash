// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import { ssrBackendFetchWithRequest } from '$lib/server-api';

export const load: PageServerLoad = async ({ parent, request }) => {
	const { email } = await parent();
	if (!email) {
		redirect(302, '/account/login?returnTo=/dashboard/files');
	}
	const res = await ssrBackendFetchWithRequest(request, '/api/v1/storage/list');
	if (!res?.ok) {
		return { files: [] };
	}
	return { files: await res.json() };
};
