// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

/** Canonical production origin for link previews and SEO. */
export const SITE_URL = 'https://cmaclash.vercel.app';

export const SITE_NAME = 'CMA Clash';

/** Default meta description from index_page copy (en locale). */
export const DEFAULT_DESCRIPTION =
	'CMA Clash is gamified CMA exam prep with live quizzes, multiplayer battles, streaks, and leaderboards.';

export const DEFAULT_TAGLINE = 'Gamified CMA exam prep.';

/** Absolute URL for Open Graph / Twitter preview image (1200×630). */
export const OG_IMAGE_URL = `${SITE_URL}/og-image.png`;

export function canonicalUrl(pathname: string): string {
	return new URL(pathname, SITE_URL).href;
}
