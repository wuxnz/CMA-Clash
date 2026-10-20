// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

/** Canonical production origin for link previews and SEO. */
export const SITE_URL = 'https://cmaclash.vercel.app';

export const SITE_NAME = 'ClassQuiz';

/** Default meta description from index_page copy (en locale). */
export const DEFAULT_DESCRIPTION =
	'ClassQuiz is a quiz app to learn interactively for students, which is open source and free to use';

export const DEFAULT_TAGLINE = 'The open-source quiz-platform!';

/** Absolute URL for Open Graph / Twitter preview image (1200×630). */
export const OG_IMAGE_URL = `${SITE_URL}/og-image.png`;

export function canonicalUrl(pathname: string): string {
	return new URL(pathname, SITE_URL).href;
}
