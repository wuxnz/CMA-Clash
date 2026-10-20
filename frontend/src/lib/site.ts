// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

/** Canonical production origin for link previews and SEO. */
export const SITE_URL = 'https://cmaclash.vercel.app';

export const SITE_NAME = 'CMA Clash';

/** Default meta description from index_page copy (en locale). */
export const DEFAULT_DESCRIPTION =
	'CCMA, EKG, phlebotomy, and CPR exam prep with live quizzes (PIN lobbies), battles, practice sets, and leaderboards.';

export const DEFAULT_TAGLINE = 'CCMA and allied health exam prep.';

/** Absolute URL for Open Graph / Twitter preview image (1200×630). */
export const OG_IMAGE_URL = `${SITE_URL}/og-image.png`;

export function canonicalUrl(pathname: string): string {
	return new URL(pathname, SITE_URL).href;
}
