// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

import { spawn } from 'node:child_process';

const backendUrl = process.argv[2] ?? 'https://cmaclash-api.onrender.com';
const port = process.argv[3] ?? '3000';
const isWindows = process.platform === 'win32';
const packageManager = isWindows ? 'pnpm.cmd' : 'pnpm';
const env = {
	...process.env,
	BACKEND_URL: backendUrl,
	PUBLIC_SOCKET_URL: backendUrl,
	NODE_ENV: 'production'
};

function run(command, args, options = {}) {
	return new Promise((resolve, reject) => {
		const child = spawn(command, args, {
			stdio: 'inherit',
			env,
			shell: isWindows,
			...options
		});
		child.once('error', reject);
		child.once('exit', (code, signal) => {
			if (code === 0) resolve();
			else reject(new Error(`${command} exited with ${signal ?? code}`));
		});
	});
}

await run(process.execPath, ['scripts/write-vercel-config.mjs']);
await run(packageManager, ['exec', 'vite', 'build']);

const preview = spawn(
	packageManager,
	['exec', 'vite', 'preview', '--host', '127.0.0.1', '--port', port],
	{ stdio: 'inherit', env, shell: isWindows }
);

for (const signal of ['SIGINT', 'SIGTERM']) {
	process.on(signal, () => preview.kill(signal));
}

preview.once('error', (error) => {
	console.error(error);
	process.exitCode = 1;
});
preview.once('exit', (code, signal) => {
	process.exitCode = code ?? (signal ? 1 : 0);
});
