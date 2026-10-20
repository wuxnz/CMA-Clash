import { certificationShortLabel, type Certification } from '$lib/cma/client';

export const CERT_FILTERS = [
	{ slug: '', label: 'All' },
	{ slug: 'ccma', label: 'NHA CCMA' },
	{ slug: 'ekg', label: 'EKG' },
	{ slug: 'phlebotomy', label: 'Phlebotomy' },
	{ slug: 'cpr-bls', label: 'CPR / BLS' },
	{ slug: 'clinical-skills', label: 'Clinical' }
] as const;

export const DIFFICULTY_FILTERS = [
	{ value: '', label: 'All levels' },
	{ value: 'beginner', label: 'Beginner' },
	{ value: 'intermediate', label: 'Intermediate' },
	{ value: 'advanced', label: 'Advanced' }
] as const;

export function certDotClass(label?: string | null): string {
	const s = (label ?? '').toLowerCase();
	if (s.includes('ekg')) return 'bg-cyan';
	if (s.includes('phleb')) return 'bg-gold';
	if (s.includes('bls') || s.includes('cpr')) return 'bg-signal';
	if (s.includes('skill') || s.includes('clinical')) return 'bg-ink-muted';
	return 'bg-violet';
}

export function certLabelFor(
	item: { certification_id?: string | null; title?: string | null },
	certs: Certification[] = []
): string | undefined {
	const match = certs.find((c) => c.id === item.certification_id);
	if (match) return certificationShortLabel(match.slug, match.name);
	const title = String(item.title ?? '');
	const s = title.toLowerCase();
	if (s.includes('ekg')) return 'EKG';
	if (s.includes('phleb')) return 'Phlebotomy';
	if (s.includes('bls') || s.includes('cpr')) return 'BLS';
	if (s.includes('clinical') || s.includes('skill')) return 'Skills';
	if (/ccma/i.test(title)) return 'CCMA';
	return undefined;
}

export function stripHighlight(html: string | undefined | null): string {
	if (!html) return '';
	return html.replace(/<[^>]+>/g, '');
}

export function prettyDifficulty(value?: string | null): string | undefined {
	if (!value) return undefined;
	return value.charAt(0).toUpperCase() + value.slice(1);
}

export function certSlugFor(
	item: { certification_id?: string | null; title?: string | null; certLabel?: string | null },
	certs: Certification[] = []
): string {
	const match = certs.find((c) => c.id === item.certification_id);
	if (match) return match.slug;
	const label = (item.certLabel ?? '').toLowerCase();
	if (label.includes('ekg')) return 'ekg';
	if (label.includes('phleb')) return 'phlebotomy';
	if (label.includes('bls') || label.includes('cpr')) return 'cpr-bls';
	if (label.includes('skill') || label.includes('clinical')) return 'clinical-skills';
	if (label.includes('ccma')) return 'ccma';
	return '';
}
