// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

export interface FitTextOptions {
	/** Smallest font size in px the text may shrink to. */
	min?: number;
	/** Largest font size in px the text may grow to. */
	max?: number;
}

/**
 * Sets the element's font size to the largest value between `min` and `max` at which its text fits
 * the space its siblings leave in the parent. The parent needs a definite height, or the fit has no
 * bound. Refits when the parent or the element changes size, and when the action's options change.
 */
export function fitText(node: HTMLElement, options: FitTextOptions = {}) {
	let min = options.min ?? 12;
	let max = options.max ?? 48;
	let frame = 0;

	function available(): { width: number; height: number } | null {
		const parent = node.parentElement;
		if (!parent) return null;
		const style = getComputedStyle(parent);
		const padX = parseFloat(style.paddingLeft) + parseFloat(style.paddingRight);
		const padY = parseFloat(style.paddingTop) + parseFloat(style.paddingBottom);
		const siblings = Array.from(parent.children).filter((child) => child !== node);
		const gap = parseFloat(style.rowGap) || 0;
		let height = parent.clientHeight - padY - gap * siblings.length;
		for (const sibling of siblings) height -= (sibling as HTMLElement).offsetHeight;
		return { width: parent.clientWidth - padX, height };
	}

	function fit() {
		frame = 0;
		const box = available();
		if (!box || box.width <= 0 || box.height <= 0) return;
		let lo = min;
		let hi = max;
		let best = min;
		while (lo <= hi) {
			const mid = Math.floor((lo + hi) / 2);
			node.style.fontSize = `${mid}px`;
			if (node.offsetHeight <= box.height && node.scrollWidth <= box.width) {
				best = mid;
				lo = mid + 1;
			} else {
				hi = mid - 1;
			}
		}
		node.style.fontSize = `${best}px`;
	}

	function schedule() {
		if (!frame) frame = requestAnimationFrame(fit);
	}

	const observer = new ResizeObserver(schedule);
	if (node.parentElement) observer.observe(node.parentElement);
	observer.observe(node);
	schedule();

	return {
		update(next: FitTextOptions) {
			min = next.min ?? 12;
			max = next.max ?? 48;
			schedule();
		},
		destroy() {
			cancelAnimationFrame(frame);
			observer.disconnect();
		}
	};
}
