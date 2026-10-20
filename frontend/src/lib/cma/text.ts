/** Normalize quiz copy that was over-escaped for templates (e.g. literal `\$`). */
export function normalizeQuizText(text: string | undefined | null): string {
	if (!text) return '';
	return text.replace(/\\\$/g, '$');
}
