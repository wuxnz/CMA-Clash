// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

// the old prefix: import.meta.env.VITE_
export const google_auth_enabled = import.meta.env.VITE_GOOGLE_AUTH_ENABLED;
export const github_auth_enabled = import.meta.env.VITE_GITHUB_AUTH_ENABLED;
export const captcha_enabled = import.meta.env.VITE_CAPTCHA_ENABLED;
export const custom_oauth_name = import.meta.env.VITE_CUSTOM_OAUTH_NAME;
/** When true, hide registration (VITE_REGISTRATION_DISABLED=true or 1). */
export const registration_disabled =
	import.meta.env.VITE_REGISTRATION_DISABLED === 'true' ||
	import.meta.env.VITE_REGISTRATION_DISABLED === '1';
export const hcaptcha_site_key = import.meta.env.VITE_HCAPTCHA;
export const sentry_dsn = import.meta.env.VITE_SENTRY;
export const recaptcha_key = import.meta.env.VITE_RECAPTCHA;
export const plausible_data_url = import.meta.env.VITE_PLAUSIBLE_DATA_URL;
