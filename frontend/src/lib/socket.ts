// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { io } from 'socket.io-client';
import { env } from '$env/dynamic/public';

const socketUrl = env.PUBLIC_SOCKET_URL?.replace(/\/$/, '') || undefined;

export const socket = io(socketUrl, {
	withCredentials: true,
	transports: ['websocket', 'polling']
});
