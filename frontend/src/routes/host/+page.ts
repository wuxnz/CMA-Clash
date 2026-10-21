// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import type { PageLoad } from './$types';

export const load = (() => ({
	quizzes: [],
	ssrQuizLoadFailed: false
})) satisfies PageLoad;
