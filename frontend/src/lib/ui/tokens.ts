/** Arena answer tiles — Kahoot-style shape + saturated color. */
export const LEDGER_ANSWER_COLORS = ['#FF3B5C', '#7B5CFF', '#F59E0B', '#22D3EE'] as const;

export const LEDGER_ANSWER_SHAPES = ['triangle', 'diamond', 'circle', 'square'] as const;

export type AnswerShape = (typeof LEDGER_ANSWER_SHAPES)[number];

export const ARENA = {
	night: '#0B0F1A',
	panel: '#151B2B',
	volt: '#C8FF2E',
	violet: '#7B5CFF',
	signal: '#FF3B5C',
	cyan: '#22D3EE'
} as const;
