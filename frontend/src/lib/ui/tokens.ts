/** Answer tiles — distinct, colorblind-safe (triangle, diamond, circle, square). */
export const LEDGER_ANSWER_COLORS = ['#F87171', '#60A5FA', '#FBBF24', '#34D399'] as const;

export const LEDGER_ANSWER_SHAPES = ['triangle', 'diamond', 'circle', 'square'] as const;

export type AnswerShape = (typeof LEDGER_ANSWER_SHAPES)[number];
