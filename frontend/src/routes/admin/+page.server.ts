// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

export async function load({ url }) {
	const token = url.searchParams.get('token');
	const pin = url.searchParams.get('pin');
	let auto_connect = url.searchParams.get('connect') !== null;
	if (token === null || pin === null) {
		auto_connect = false;
	}
	return {
		game_pin: pin === null ? '' : pin,
		game_token: token === null ? '' : token,
		auto_connect
	};
}
