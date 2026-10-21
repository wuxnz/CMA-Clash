/** One desktop grid: header + rows share these tracks (subgrid per row). */
export const quizTableDesktopShell =
	'min-w-0 md:grid md:grid-cols-[minmax(0,1.4fr)_6.5rem_3.5rem_7rem_auto] md:gap-x-3';

export const quizTableHeaderRow =
	'hidden md:col-span-full md:grid md:grid-cols-subgrid md:gap-x-3 md:items-end text-xs text-ink-muted pb-2 border-b border-white/[0.07]';

export const quizTableDataRow =
	'grid grid-cols-[1fr_auto] gap-x-3 gap-y-1 items-center py-3 border-b border-white/[0.07] min-w-0 md:col-span-full md:grid md:grid-cols-subgrid md:gap-x-3';

export const quizColCert = 'hidden md:flex items-center gap-2 text-xs text-ink-muted min-w-0';

export const quizColCertDot = 'inline-block w-1.5 h-1.5 shrink-0';

export const quizColQs = 'hidden md:block text-xs text-ink-muted tabular-nums text-right';

export const quizColDifficulty = 'hidden md:block text-xs text-ink-muted truncate min-w-0';

export const quizColActions = 'flex items-center justify-end gap-1 min-w-0';

/** Header-only cells (row is already desktop-only). */
export const quizHeaderColCert = 'flex items-center gap-2 min-w-0';

export const quizHeaderColQs = 'tabular-nums text-right';

export const quizHeaderColDifficulty = 'truncate min-w-0';
