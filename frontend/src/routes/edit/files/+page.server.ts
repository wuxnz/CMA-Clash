// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { redirect } from '@sveltejs/kit';
import type { PageServerLoad } from './$types';
import type { PrivateImageData } from '$lib/quiz_types';
import { ssrBackendFetchWithRequest } from '$lib/server-api';

export const load: PageServerLoad = async ({ parent, request }) => {
	const { email } = await parent();
	if (!email) {
		redirect(302, '/account/login?returnTo=/edit/files');
	}
	const [res, res2] = await Promise.all([
		ssrBackendFetchWithRequest(request, '/api/v1/storage/list'),
		ssrBackendFetchWithRequest(request, '/api/v1/storage/limit')
	]);
	let images: PrivateImageData[] = [];
	if (res?.ok) {
		images = await res.json();
	}
	const storage_usage: { limit: number; limit_reached: boolean; used: number } = res2?.ok
		? await res2.json()
		: { limit: 0, limit_reached: false, used: 0 };
	return {
		images,
		storage_usage
	};
};
