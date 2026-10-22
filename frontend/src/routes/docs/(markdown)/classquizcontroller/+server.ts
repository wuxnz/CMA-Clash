// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { redirect } from '@sveltejs/kit';

/**
 * The quiz-controller documentation used to live under the upstream project name.
 * Keep the old path working so existing links don't 404.
 */
export const GET = () => {
	redirect(308, '/docs/quiz-controller');
};
