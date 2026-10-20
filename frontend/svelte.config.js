// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

import adapterNode from '@sveltejs/adapter-node';
import adapterVercel from '@sveltejs/adapter-vercel';
import preprocess from 'svelte-preprocess';
import { mdsvex } from 'mdsvex';

const adapter =
	process.env.VERCEL === '1'
		? adapterVercel()
		: adapterNode({
				out: 'build',
				precompress: true
			});

/** @type {import('@sveltejs/kit').Config} */
const config = {
	// Consult https://github.com/sveltejs/svelte-preprocess
	// for more information about preprocessors
	preprocess: [
		preprocess({
			postcss: true
		}),
		mdsvex()
	],
	extensions: ['.svelte', '.svx'],

	kit: {
		adapter
		// +++ SOON OBSOLETE +++
		/*
		vite: {
			optimizeDeps: {
				include: ['swiper']
			},
			build: {
				sourcemap: true
			}
		}
		*/
		// --- SOON OBSOLETE ---
	}
};

export default config;
