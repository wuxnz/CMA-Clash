/** Shared grid + column classes for browse/dashboard quiz tables. */
export const quizTableGrid =
	'grid grid-cols-[1fr_auto] md:grid-cols-[minmax(0,1.4fr)_6.5rem_3.5rem_7rem_auto] gap-x-3';

export const quizTableHeaderShell =
	'hidden md:grid text-xs text-ink-muted pb-2 border-b border-white/[0.07]';

export const quizTableRowShell = 'items-center gap-y-1 py-3 border-b border-white/[0.07] min-w-0';

export const quizColCert = 'hidden md:flex items-center gap-2 text-xs text-ink-muted min-w-0';

export const quizColCertDot = 'inline-block w-1.5 h-1.5 shrink-0';

export const quizColQs = 'hidden md:block text-xs text-ink-muted tabular-nums text-right';

export const quizColDifficulty = 'hidden md:block text-xs text-ink-muted truncate min-w-0';

export const quizColActions = 'flex items-center justify-end gap-1 min-w-0';
