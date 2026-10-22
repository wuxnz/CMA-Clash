// SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
//
// SPDX-License-Identifier: MPL-2.0

const { defineConfig, globalIgnores } = require('eslint/config');

const tsParser = require('@typescript-eslint/parser');
const typescriptEslint = require('@typescript-eslint/eslint-plugin');
const globals = require('globals');
const js = require('@eslint/js');
const svelte = require('eslint-plugin-svelte');

module.exports = defineConfig([
	js.configs.recommended,
	svelte.configs.recommended,
	globalIgnores([
		'**/*.cjs',
		'src/app.html',
		// Generated output must never be linted: `build/` is the adapter bundle and
		// `.svelte-kit/` holds SvelteKit's generated types/manifests.
		'build/**',
		'.svelte-kit/**',
		'node_modules/**',
		'playwright-report/**',
		'test-results/**',
		// Ambient declaration files only describe types; they have no runtime code.
		'**/*.d.ts'
	]),
	{
		languageOptions: {
			sourceType: 'module',
			// 2022+ is required for top-level await (scripts/*.mjs) and numeric separators.
			ecmaVersion: 2022,

			globals: {
				...globals.browser,
				...globals.node,
				// Type-only namespaces and script-provided globals that have no runtime
				// counterpart in the `globals` package.
				NodeJS: 'readonly',
				grecaptcha: 'readonly'
			}
		}
	},
	{
		files: ['**/*.{ts,js}'],
		languageOptions: {
			parser: tsParser
		},

		plugins: {
			'@typescript-eslint': typescriptEslint
		},

		rules: {
			// TypeScript already reports unresolved identifiers; `no-undef` does not
			// understand type positions and flags every DOM/Node type alias.
			'no-undef': 'off',

			'no-unused-vars': [
				'error',
				{
					argsIgnorePattern: '^_.*'
				}
			],

			'@typescript-eslint/no-unused-vars': [
				'error',
				{
					argsIgnorePattern: '^_.*'
				}
			]
		}
	},
	{
		files: ['**/*.svelte'],
		languageOptions: {
			parserOptions: {
				parser: tsParser,
				extraFileExtensions: ['.svelte']
			}
		}
	},
	{
		files: ['**/*.svelte', '**/*.ts', '**/*.js'],

		rules: {
			'a11y-click-events-have-key-events': 'off',
			'no-unused-vars': [
				'error',
				{
					argsIgnorePattern: '^_.*'
				}
			],
			'@typescript-eslint/no-unused-vars': [
				'error',
				{
					argsIgnorePattern: '^_.*'
				}
			],
			'svelte/no-at-html-tags': 'warn',
			'svelte/require-each-key': 'warn'
		},

		plugins: {
			'@typescript-eslint': typescriptEslint
		}
	}
]);
