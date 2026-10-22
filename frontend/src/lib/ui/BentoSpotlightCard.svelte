<script lang="ts">
	import { prefersReducedMotion } from './motion';

	interface Props {
		class?: string;
		href?: string;
		tilt?: boolean;
		'data-bento'?: boolean;
		'data-platform'?: boolean;
		children?: import('svelte').Snippet;
	}

	let {
		class: className = '',
		href,
		tilt = true,
		'data-bento': dataBento,
		'data-platform': dataPlatform,
		children
	}: Props = $props();
	const reduced = prefersReducedMotion();

	let el: HTMLElement;
	let spotX = $state(50);
	let spotY = $state(50);
	let rotateX = $state(0);
	let rotateY = $state(0);

	function onMove(e: PointerEvent) {
		if (reduced || !el || !window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
		const r = el.getBoundingClientRect();
		spotX = ((e.clientX - r.left) / r.width) * 100;
		spotY = ((e.clientY - r.top) / r.height) * 100;
		if (tilt) {
			rotateY = ((e.clientX - r.left) / r.width - 0.5) * 8;
			rotateX = ((e.clientY - r.top) / r.height - 0.5) * -8;
		}
	}

	function onLeave() {
		spotX = 50;
		spotY = 50;
		rotateX = 0;
		rotateY = 0;
	}
</script>

<svelte:element
	this={href ? 'a' : 'div'}
	{href}
	bind:this={el}
	data-bento={dataBento ? '' : undefined}
	data-platform={dataPlatform ? '' : undefined}
	class="group relative rounded-2xl glass-panel p-6 md:p-8 overflow-hidden {className}"
	style:transition-property="box-shadow, transform"
	style:transition-duration="300ms"
	style:transition-timing-function="ease-out"
	style="--spot-x: {spotX}%; --spot-y: {spotY}%; transform: perspective(800px) rotateX({rotateX}deg) rotateY({rotateY}deg);"
	onpointermove={onMove}
	onpointerleave={onLeave}
>
	<div
		class="pointer-events-none absolute inset-0 opacity-0 rounded-2xl max-[hover:none]:hidden [@media(hover:hover)]:group-hover:opacity-100"
		style:transition="opacity 300ms ease-out"
		style="background: radial-gradient(600px circle at var(--spot-x) var(--spot-y), color-mix(in srgb, var(--color-primary) 22%, transparent), transparent 45%);"
		aria-hidden="true"
	></div>
	<div
		class="pointer-events-none absolute inset-0 rounded-2xl opacity-0 max-[hover:none]:hidden [@media(hover:hover)]:group-hover:opacity-100"
		style:transition="opacity 300ms ease-out"
		style="padding: 1px; background: radial-gradient(400px circle at var(--spot-x) var(--spot-y), var(--color-primary), transparent 40%); mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0); mask-composite: exclude;"
		aria-hidden="true"
	></div>
	<div class="relative z-10 h-full flex flex-col">{@render children?.()}</div>
</svelte:element>
