// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

export function sleep(ms: number): Promise<void> {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function fetchWithRetry(
	url: string,
	init: RequestInit = {},
	options: { attempts?: number; baseDelayMs?: number; timeoutMs?: number } = {}
): Promise<Response | null> {
	const attempts = options.attempts ?? 3;
	const baseDelayMs = options.baseDelayMs ?? 1500;
	const timeoutMs = options.timeoutMs ?? 20_000;

	for (let i = 0; i < attempts; i++) {
		try {
			const res = await fetch(url, {
				...init,
				signal: AbortSignal.timeout(timeoutMs)
			});
			if (res.ok) {
				return res;
			}
			if (res.status >= 500 && i < attempts - 1) {
				await sleep(baseDelayMs * (i + 1));
				continue;
			}
			return res;
		} catch {
			if (i < attempts - 1) {
				await sleep(baseDelayMs * (i + 1));
			}
		}
	}
	return null;
}
