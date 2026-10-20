// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { get } from 'svelte/store';
import { isSiteAdmin, signedIn } from '$lib/stores';

export async function refreshSiteAdminFlag(): Promise<void> {
	if (!get(signedIn)) {
		isSiteAdmin.set(false);
		return;
	}
	try {
		const res = await fetch('/api/v1/users/me', { credentials: 'include' });
		if (!res.ok) {
			isSiteAdmin.set(false);
			return;
		}
		const data = await res.json();
		isSiteAdmin.set(Boolean(data.is_site_admin));
	} catch {
		isSiteAdmin.set(false);
	}
}
