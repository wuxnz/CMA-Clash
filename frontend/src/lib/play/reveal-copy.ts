// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import type { Question } from '$lib/quiz_types';

export function correctAnswerFromQuestion(question: Question | undefined): string | null {
	if (!question?.answers || !Array.isArray(question.answers)) {
		return null;
	}
	const labels = question.answers
		.filter((a) => Boolean(a?.right))
		.map((a) => String(a?.answer ?? '').trim())
		.filter(Boolean);
	return labels.length > 0 ? labels.join('; ') : null;
}
