import type { Action } from 'svelte/action';
import { loadGsap } from './gsap';

export type ScrollRevealOptions = {
	delay?: number;
	y?: number;
	stagger?: number;
	childSelector?: string;
};

const ENTER_DURATION = 0.3;
const ENTER_EASE = 'power2.out';
const STAGGER = 0.1;
const Y = 12;
const BLUR = 4;

export const scrollReveal: Action<HTMLElement, ScrollRevealOptions | undefined> = (
	node,
	opts = {}
) => {
	if (typeof window === 'undefined') return {};

	const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
	let destroyed = false;

	loadGsap().then(async (gsap) => {
		if (destroyed) return;
		const { ScrollTrigger } = await import('gsap/ScrollTrigger');
		const y = opts.y ?? Y;
		const targets = opts.childSelector
			? node.querySelectorAll(opts.childSelector)
			: [node];

		if (reduced) {
			gsap.set(targets, { opacity: 0 });
			ScrollTrigger.batch(targets, {
				start: 'top 88%',
				onEnter: (batch) => {
					gsap.to(batch, {
						opacity: 1,
						duration: ENTER_DURATION,
						ease: ENTER_EASE,
						stagger: opts.stagger ?? STAGGER,
						delay: opts.delay ?? 0,
						overwrite: true
					});
				},
				once: true
			});
			return;
		}

		gsap.set(targets, { opacity: 0, y, filter: `blur(${BLUR}px)` });
		ScrollTrigger.batch(targets, {
			start: 'top 88%',
			onEnter: (batch) => {
				gsap.to(batch, {
					opacity: 1,
					y: 0,
					filter: 'blur(0px)',
					duration: ENTER_DURATION,
					ease: ENTER_EASE,
					stagger: opts.stagger ?? STAGGER,
					delay: opts.delay ?? 0,
					overwrite: true
				});
			},
			once: true
		});
	});

	return {
		destroy() {
			destroyed = true;
		}
	};
};
