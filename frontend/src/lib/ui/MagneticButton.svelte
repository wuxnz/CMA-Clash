<script lang="ts">
	import { resolve } from '$app/paths';
	import type { Pathname } from '$app/types';
	import { onMount } from 'svelte';
	import { prefersReducedMotion } from './motion';

	interface Props {
		href?: string;
		type?: 'button' | 'submit';
		class?: string;
		disabled?: boolean;
		static?: boolean;
		children?: import('svelte').Snippet;
		onclick?: (_e: MouseEvent) => void;
	}

	let {
		href,
		type = 'button',
		class: className = '',
		disabled = false,
		static: isStatic = false,
		children,
		onclick
	}: Props = $props();

	const reduced = prefersReducedMotion();
	let x = $state(0);
	let y = $state(0);
	let canMagnet = $state(false);

	onMount(() => {
		canMagnet =
			!isStatic &&
			!reduced &&
			window.matchMedia('(hover: hover) and (pointer: fine)').matches;
	});

	function onMove(e: PointerEvent) {
		if (!canMagnet || disabled) return;
		const t = e.currentTarget as HTMLElement;
		const r = t.getBoundingClientRect();
		x = (e.clientX - r.left - r.width / 2) * 0.12;
		y = (e.clientY - r.top - r.height / 2) * 0.15;
	}

	function reset() {
		x = 0;
		y = 0;
	}

	const baseClass =
		'inline-flex items-center justify-center transition-transform duration-150 ease-out press-scale disabled:opacity-50';
</script>

{#if href}
	<a
		href={resolve(href as Pathname)}
		class="{baseClass} {className}"
		style={canMagnet ? `transform: translate(${x}px, ${y}px);` : undefined}
		onpointermove={onMove}
		onpointerleave={reset}
	>
		{@render children?.()}
	</a>
{:else}
	<button
		{type}
		{disabled}
		class="{baseClass} {className}"
		style={canMagnet ? `transform: translate(${x}px, ${y}px);` : undefined}
		onpointermove={onMove}
		onpointerleave={reset}
		{onclick}
	>
		{@render children?.()}
	</button>
{/if}
