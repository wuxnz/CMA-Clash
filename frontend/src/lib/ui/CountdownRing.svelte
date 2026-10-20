<script lang="ts">
	import { onMount } from 'svelte';
	import { prefersReducedMotion } from './motion';
	import { loadGsap } from '$lib/motion/gsap';

	interface Props {
		seconds?: number;
		onComplete?: () => void;
		label?: string;
	}

	let { seconds = 5, onComplete, label = 'Starting' }: Props = $props();

	let display = $state(seconds);
	let reduced = prefersReducedMotion();
	const circumference = 2 * Math.PI * 54;

	let progress = $derived(seconds > 0 ? Math.max(0, Math.min(1, display / seconds)) : 0);

	onMount(() => {
		if (reduced) {
			onComplete?.();
			return;
		}
		let killed = false;
		loadGsap().then((gsap) => {
			const obj = { t: seconds };
			gsap.to(obj, {
				t: 0,
				duration: seconds,
				ease: 'power2.inOut',
				onUpdate: () => {
					display = obj.t;
				},
				onComplete: () => {
					if (!killed) onComplete?.();
				}
			});
		});
		return () => {
			killed = true;
		};
	});
</script>

<div class="flex flex-col items-center gap-3" role="status" aria-live="polite">
	<p class="text-sm font-medium text-ink-muted uppercase tracking-wider">{label}</p>
	<div class="relative w-32 h-32">
		<svg class="w-full h-full -rotate-90" viewBox="0 0 120 120" aria-hidden="true">
			<circle cx="60" cy="60" r="54" fill="none" stroke="currentColor" stroke-width="8" class="text-paper-muted/80" />
			<circle
				cx="60"
				cy="60"
				r="54"
				fill="none"
				stroke="currentColor"
				stroke-width="8"
				stroke-linecap="round"
				class="text-primary"
				stroke-dasharray={circumference}
				stroke-dashoffset={circumference * (1 - progress)}
				style="transition: stroke-dashoffset 0.15s linear"
			/>
		</svg>
		<span
			class="absolute inset-0 flex items-center justify-center font-display text-4xl font-bold text-ink tabular-nums"
		>
			{Math.max(0, Math.ceil(display))}
		</span>
	</div>
</div>
