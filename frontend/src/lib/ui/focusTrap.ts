const SELECTOR =
	'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])';

export function focusTrap(node: HTMLElement) {
	const previous = document.activeElement as HTMLElement | null;

	function list(): HTMLElement[] {
		return Array.from(node.querySelectorAll<HTMLElement>(SELECTOR)).filter(
			(el) => !el.hasAttribute('disabled') && el.getAttribute('aria-hidden') !== 'true'
		);
	}

	function onKey(event: KeyboardEvent) {
		if (event.key !== 'Tab') return;
		const items = list();
		if (items.length === 0) return;
		const first = items[0];
		const last = items[items.length - 1];
		if (event.shiftKey && document.activeElement === first) {
			event.preventDefault();
			last.focus();
		} else if (!event.shiftKey && document.activeElement === last) {
			event.preventDefault();
			first.focus();
		}
	}

	requestAnimationFrame(() => {
		const items = list();
		(items[0] ?? node).focus();
	});

	node.addEventListener('keydown', onKey);
	return {
		destroy() {
			node.removeEventListener('keydown', onKey);
			previous?.focus?.();
		}
	};
}
