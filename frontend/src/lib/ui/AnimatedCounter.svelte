<script lang="ts">
	import { untrack } from 'svelte';
	import { prefersReducedMotion } from './motion';
	import { loadGsap } from '$lib/motion/gsap';

	interface Props {
		value: number;
		duration?: number;
		suffix?: string;
		class?: string;
	}

	let { value, duration = 1.2, suffix = '', class: className = '' }: Props = $props();

	let display = $state(0);
	const reduced = prefersReducedMotion();

	$effect(() => {
		const target = value;
		if (reduced) {
			display = target;
			return;
		}
		const from = untrack(() => display);
		let killed = false;
		loadGsap().then((gsap) => {
			if (killed) return;
			const obj = { n: from };
			gsap.killTweensOf(obj);
			gsap.to(obj, {
				n: target,
				duration,
				ease: 'power2.out',
				onUpdate: () => {
					display = Math.round(obj.n);
				}
			});
		});
		return () => {
			killed = true;
		};
	});
</script>

<span class="tabular-nums {className}">{display.toLocaleString()}{suffix}</span>
