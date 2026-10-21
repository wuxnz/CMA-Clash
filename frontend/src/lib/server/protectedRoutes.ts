// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

const PROTECTED_PREFIXES = [
	'/dashboard',
	'/create',
	'/edit',
	'/import',
	'/account/settings',
	'/account/controllers',
	'/site-admin',
	'/moderation',
	'/admin',
	'/quiztivity/edit',
	'/quiztivity/create',
	'/results'
] as const;

/** Routes that need a live session (token refresh) before SSR layout/load runs. */
export function routeNeedsSessionRefresh(pathname: string): boolean {
	return PROTECTED_PREFIXES.some(
		(prefix) => pathname === prefix || pathname.startsWith(`${prefix}/`)
	);
}
