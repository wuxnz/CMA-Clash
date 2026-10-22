<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { theme } from '$lib/theme.svelte';

	interface Props {
		class?: string;
		label?: string;
	}

	let { class: className = '', label = 'Toggle colour theme' }: Props = $props();
</script>

<button
	type="button"
	class="theme-toggle {className}"
	aria-label={label}
	aria-pressed={theme.mode === 'light'}
	title={theme.mode === 'dark' ? 'Switch to light theme' : 'Switch to dark theme'}
	onclick={() => theme.toggle()}
>
	<span class="theme-toggle__track" aria-hidden="true">
		<span class="theme-toggle__thumb" data-mode={theme.mode}>
			{#if theme.mode === 'dark'}
				<svg
					viewBox="0 0 24 24"
					width="13"
					height="13"
					fill="none"
					stroke="currentColor"
					stroke-width="1.9"
					stroke-linecap="round"
					stroke-linejoin="round"
				>
					<path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79Z" />
				</svg>
			{:else}
				<svg
					viewBox="0 0 24 24"
					width="13"
					height="13"
					fill="none"
					stroke="currentColor"
					stroke-width="1.9"
					stroke-linecap="round"
					stroke-linejoin="round"
				>
					<circle cx="12" cy="12" r="4" />
					<path
						d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"
					/>
				</svg>
			{/if}
		</span>
	</span>
</button>

<style>
	.theme-toggle {
		display: inline-flex;
		align-items: center;
		padding: 0;
		background: transparent;
		border: 0;
		line-height: 0;
	}

	.theme-toggle__track {
		position: relative;
		display: inline-block;
		width: 3.25rem;
		height: 1.75rem;
		border-radius: 999px;
		background: color-mix(in oklch, var(--color-ink) 12%, transparent);
		box-shadow: inset 0 0 0 1px var(--color-line);
		transition: background 320ms cubic-bezier(0.4, 0, 0.2, 1);
	}

	.theme-toggle__thumb {
		position: absolute;
		top: 50%;
		left: 0.1875rem;
		display: grid;
		place-items: center;
		width: 1.375rem;
		height: 1.375rem;
		border-radius: 999px;
		background: var(--color-primary);
		color: #fff;
		transform: translateY(-50%);
		transition:
			transform 380ms cubic-bezier(0.34, 1.56, 0.64, 1),
			background 320ms ease;
		box-shadow: 0 2px 10px color-mix(in oklch, var(--color-primary) 45%, transparent);
	}

	.theme-toggle__thumb[data-mode='light'] {
		transform: translate(1.5rem, -50%);
	}

	@media (prefers-reduced-motion: reduce) {
		.theme-toggle__thumb {
			transition: none;
		}
	}
</style>
