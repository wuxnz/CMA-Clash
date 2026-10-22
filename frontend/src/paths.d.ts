// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { Pathname } from '$app/types';

declare module '$app/paths' {
	/**
	 * `resolve()` is typed for a single route id, so it cannot be called with a
	 * union of paths - which is exactly what a link list holds. This overload
	 * accepts any app path and is used as a fallback by the kit's own overload.
	 */
	export function resolve(path: Pathname): string;
}
