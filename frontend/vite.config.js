// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig, loadEnv } from 'vite';

/** Backend used by the dev proxy when nothing else is configured. */
const DEFAULT_API_TARGET = 'https://cmaclash-api.onrender.com';

/**
 * @type {import("vite").UserConfig}
 */
export default defineConfig(({ mode }) => {
	// `loadEnv` with an empty prefix reads the whole .env file, not only VITE_* keys.
	const env = loadEnv(mode, process.cwd(), '');
	const apiTarget = (
		env.API_PROXY_TARGET ||
		env.BACKEND_URL ||
		env.API_URL ||
		DEFAULT_API_TARGET
	).replace(/\/+$/, '');

	return {
		plugins: [
			sveltekit(),
			{
				name: 'configure-response-headers',
				configureServer: (server) => {
					server.middlewares.use((_req, res, next) => {
						/*        res.setHeader("Cross-Origin-Embedder-Policy", "require-corp");
        res.setHeader("Cross-Origin-Opener-Policy", "same-origin");
        res.setHeader("Access-Control-Allow-Origin", "https://cmaclash.com");*/
					next();
				});
			}
			}
		],
		server: {
			port: 3000,
			proxy: {
				'/api': { target: apiTarget, changeOrigin: true },
				'/socket.io': { target: apiTarget, ws: true, changeOrigin: true },
				'/openapi.json': { target: apiTarget, changeOrigin: true },
				'/rapidoc': { target: apiTarget, changeOrigin: true }
			}
		},
		preview: {
			port: 3000
		},
		optimizeDeps: {
			include: ['swiper', 'tippy.js']
		},
		build: {
			sourcemap: true
		}

		/* Trying

    ssr: {
      noExternal: ['@ckeditor/*'],
    }

    end trying*/
	};
});
