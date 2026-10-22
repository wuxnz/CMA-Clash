/*
 * Editorial motion primitives.
 *
 * Scroll-triggered reveals, masked headline splits and count-ups. Everything
 * degrades to a static, fully readable layout when the visitor prefers
 * reduced motion.
 */
import type { Action } from 'svelte/action';
import { loadGsap } from './gsap';

export const reducedMotion = (): boolean =>
	typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export type RevealOptions = {
	/** Stagger between children. */
	stagger?: number;
	delay?: number;
	y?: number;
	x?: number;
	scale?: number;
	blur?: number;
	duration?: number;
	childSelector?: string;
	/** Scroll position that triggers the reveal. */
	start?: string;
	once?: boolean;
};

/**
 * Runs `run` the first time `node` scrolls into view.
 *
 * Deliberately avoids IntersectionObserver: it is unreliable in embedded /
 * headless contexts and it does not fire for content that is already on
 * screen at load time. A rect check on mount plus a throttled scroll/resize
 * listener is deterministic everywhere.
 */
function whenVisible(node: Element, run: () => void): () => void {
	let done = false;
	let ticking = false;

	const check = () => {
		ticking = false;
		if (done) return;
		// Actions can run before the element is inserted into the document.
		// Wait a tick and try again rather than measuring a zero rect.
		if (!node.isConnected) {
			setTimeout(check, 60);
			return;
		}
		const rect = node.getBoundingClientRect();
		if (rect.top < window.innerHeight * 0.92 && rect.bottom > 0) {
			done = true;
			run();
		}
	};

	const onScroll = () => {
		if (done || ticking) return;
		ticking = true;
		requestAnimationFrame(check);
	};

	// Content already on screen reveals straight away.
	check();
	window.addEventListener('scroll', onScroll, { passive: true });
	window.addEventListener('resize', onScroll, { passive: true });

	return () => {
		window.removeEventListener('scroll', onScroll);
		window.removeEventListener('resize', onScroll);
	};
}

/**
 * Safety net: a reveal must never leave content permanently invisible.
 * If the tween has not run (backgrounded tab, throttled rAF, blocked
 * animation) the final state is applied directly after a grace period.
 */
function ensureReadable(
	gsap: typeof import('gsap').gsap,
	elements: Element[],
	afterMs: number,
	extra: Record<string, unknown> = {}
): void {
	const grace = Math.max(1200, afterMs + 800);
	setTimeout(() => {
		for (const el of elements) {
			const opacity = Number(gsap.getProperty(el, 'opacity'));
			if (!Number.isFinite(opacity) || opacity < 0.99) {
				gsap.set(el, { opacity: 1, y: 0, x: 0, scale: 1, filter: 'blur(0px)', ...extra });
			}
		}
	}, grace);
}

/** Fade / slide / blur reveal bound to scroll position. */
export const reveal: Action<HTMLElement, RevealOptions | undefined> = (node, opts = {}) => {
	if (typeof window === 'undefined') return {};
	if (reducedMotion()) return {};

	let destroyed = false;
	let cleanup: (() => void) | undefined;
	const {
		stagger = 0.08,
		delay = 0,
		y = 28,
		x = 0,
		scale = 1,
		blur = 6,
		duration = 0.85,
		childSelector
	} = opts;

	loadGsap().then(async (gsap) => {
		if (destroyed) return;
		const targets = childSelector ? node.querySelectorAll(childSelector) : [node];
		if (!targets.length) return;

		gsap.set(targets, {
			opacity: 0,
			y,
			x,
			scale,
			filter: blur ? `blur(${blur}px)` : 'none'
		});

		const animate = (batch: Element[]) => {
			gsap.to(batch, {
				opacity: 1,
				y: 0,
				x: 0,
				scale: 1,
				filter: 'blur(0px)',
				duration,
				ease: 'power3.out',
				stagger,
				delay,
				overwrite: true
			});
			ensureReadable(gsap, batch, delay + duration + 400);
		};

		const stop = whenVisible(node, () => animate(Array.from(targets)));
		cleanup = stop;
	});

	return {
		destroy() {
			destroyed = true;
			cleanup?.();
		}
	};
};

export type MaskLinesOptions = {
	delay?: number;
	stagger?: number;
	duration?: number;
	/** Split by word instead of line. */
	words?: boolean;
};

/**
 * Splits the content of a node into masked lines and animates them upward
 * out of an overflow-hidden clip on scroll. Inline markup (e.g. `<em>`) is
 * preserved so emphasis survives the split.
 */
export const maskLines: Action<HTMLElement, MaskLinesOptions | undefined> = (node, opts = {}) => {
	if (typeof window === 'undefined') return {};
	if (reducedMotion()) return {};

	let destroyed = false;
	let cleanup: (() => void) | undefined;
	const { delay = 0, stagger = 0.09, duration = 1.0, words = false } = opts;

	loadGsap().then(async (gsap) => {
		if (destroyed) return;

		const children = Array.from(node.childNodes);
		node.innerHTML = '';
		const inners: HTMLElement[] = [];

		const makeLine = (className: string, content: Node | string) => {
			const outer = document.createElement('span');
			outer.className = className;
			const inner = document.createElement('span');
			inner.className = 'ml-split-inner';
			if (typeof content === 'string') inner.textContent = content;
			else inner.appendChild(content);
			outer.appendChild(inner);
			node.appendChild(outer);
			inners.push(inner);
		};

		const hasNewline = children.some(
			(child) => child.nodeType === Node.TEXT_NODE && (child.textContent ?? '').includes('\n')
		);

		if (!hasNewline) {
			// A single masked line keeps inline markup (e.g. `<em>`) on the
			// same typographic line as the surrounding words.
			const inner = document.createElement('span');
			inner.className = 'ml-split-inner';
			for (const child of children) {
				if (child.nodeType === Node.TEXT_NODE) {
					inner.appendChild(document.createTextNode(child.textContent ?? ''));
				} else {
					inner.appendChild(child);
				}
			}
			const outer = document.createElement('span');
			outer.className = words ? 'ml-split-word' : 'ml-split-line';
			outer.appendChild(inner);
			node.appendChild(outer);
			inners.push(inner);
		} else {
			for (const child of children) {
				if (child.nodeType === Node.TEXT_NODE) {
					const text = child.textContent ?? '';
					if (words) {
						for (const word of text.split(/(\s+)/)) {
							if (word.trim() === '') {
								node.appendChild(document.createTextNode(' '));
								continue;
							}
							makeLine('ml-split-word', word);
						}
					} else {
						for (const line of text.split('\n')) {
							if (line.trim() === '') continue;
							makeLine('ml-split-line', line);
						}
					}
				} else if (child.nodeType === Node.ELEMENT_NODE) {
					makeLine(words ? 'ml-split-word' : 'ml-split-line', child);
				}
			}
		}

		if (!inners.length) return;
		gsap.set(inners, { yPercent: 112, opacity: 0 });

		const animate = () => {
			gsap.to(inners, {
				yPercent: 0,
				opacity: 1,
				duration,
				ease: 'power4.out',
				stagger,
				delay
			});
			ensureReadable(gsap, inners, delay + duration + 400, { yPercent: 0 });
		};

		cleanup = whenVisible(node, animate);
	});

	return {
		destroy() {
			destroyed = true;
			cleanup?.();
		}
	};
};

/** Counts a number up when the node scrolls into view. */
export const countUp: Action<
	HTMLElement,
	{ to: number; duration?: number; decimals?: number; suffix?: string } | undefined
> = (node, opts) => {
	if (typeof window === 'undefined') return {};
	const { to, duration = 1.6, decimals = 0, suffix = '' } = opts ?? { to: 0 };
	if (reducedMotion()) {
		node.textContent = to.toFixed(decimals) + suffix;
		return {};
	}

	let destroyed = false;
	let cleanup: (() => void) | undefined;

	loadGsap().then(async (gsap) => {
		if (destroyed) return;
		const state = { v: 0 };

		cleanup = whenVisible(node, () => {
			gsap.to(state, {
				v: to,
				duration,
				ease: 'power2.out',
				onUpdate: () => {
					node.textContent =
						state.v.toLocaleString('en-US', {
							minimumFractionDigits: decimals,
							maximumFractionDigits: decimals
						}) + suffix;
				}
			});
		});
	});

	return {
		destroy() {
			destroyed = true;
			cleanup?.();
		}
	};
};
