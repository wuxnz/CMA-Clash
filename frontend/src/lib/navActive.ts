// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

/** Whether a main-nav href matches the current path (exact for `/`, prefix for sections). */
export function isNavLinkActive(pathname: string, href: string): boolean {
	if (href === '/') {
		return pathname === '/';
	}
	if (href.startsWith('http') || href.startsWith('/api')) {
		return false;
	}
	const base = href.replace(/\/$/, '');
	if (pathname === base) {
		return true;
	}
	return pathname.startsWith(`${base}/`);
}
