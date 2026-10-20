import type { Action } from 'svelte/action';
import { loadGsap } from './gsap';

export type ParallaxOptions = { speed?: number };

/** Subtle Y parallax tied to scroll (skipped when reduced motion). */
export const scrollParallax: Action<HTMLElement, ParallaxOptions | undefined> = (node, opts = {}) => {
	if (typeof window === 'undefined') return {};
	if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return {};

	let destroyed = false;
	const speed = opts.speed ?? 0.35;

	loadGsap().then(async (gsap) => {
		if (destroyed) return;
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		gsap.to(node, {
			y: () => speed * 80,
			ease: 'none',
			scrollTrigger: {
				trigger: node,
				start: 'top bottom',
				end: 'bottom top',
				scrub: true
			}
		});
	});

	return {
		destroy() {
			destroyed = true;
		}
	};
};
