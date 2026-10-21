// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

export function formatApiErrorDetail(detail: unknown, fallback = 'Request failed.'): string {
	if (typeof detail === 'string' && detail.trim()) {
		return detail;
	}
	if (Array.isArray(detail)) {
		const parts = detail
			.map((entry) => {
				if (typeof entry === 'string') return entry;
				if (entry && typeof entry === 'object' && 'msg' in entry) {
					return String((entry as { msg: unknown }).msg);
				}
				return '';
			})
			.filter(Boolean);
		if (parts.length) {
			return parts.join(' ');
		}
	}
	if (detail && typeof detail === 'object' && 'message' in detail) {
		const message = (detail as { message: unknown }).message;
		if (typeof message === 'string' && message.trim()) {
			return message;
		}
	}
	return fallback;
}
