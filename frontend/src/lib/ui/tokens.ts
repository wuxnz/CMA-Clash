/** Ledger design tokens — answer tiles (Kahoot-style order: triangle, diamond, circle, square). */
export const LEDGER_ANSWER_COLORS = ['#D9485F', '#3867D6', '#E0A200', '#1E9E6A'] as const;

export const LEDGER_ANSWER_SHAPES = ['triangle', 'diamond', 'circle', 'square'] as const;

export type AnswerShape = (typeof LEDGER_ANSWER_SHAPES)[number];
