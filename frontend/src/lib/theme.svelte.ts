/*
 * Site-wide colour theme.
 *
 * The design direction is a solid near-black canvas with a medical blue
 * accent; the light theme is a warm paper white with the same accent.
 * The class is applied to <html> so Tailwind's `dark:` / `light:` variants
 * and the token set in app.css stay in sync.
 */
import { browser } from '$app/environment';

export type ThemeMode = 'dark' | 'light';

const STORAGE_KEY = 'cma-clash:theme';

function readStoredMode(): ThemeMode {
	if (!browser) return 'dark';
	try {
		const stored = localStorage.getItem(STORAGE_KEY);
		if (stored === 'light' || stored === 'dark') return stored;
	} catch {
		/* storage blocked — fall through to the system preference */
	}
	return 'dark';
}

function systemMode(): ThemeMode {
	if (!browser) return 'dark';
	return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
}

class ThemeController {
	#mode = $state<ThemeMode>('dark');

	constructor() {
		if (browser) {
			this.#mode = readStoredMode();
			this.#apply(this.#mode, false);
		}
	}

	get mode(): ThemeMode {
		return this.#mode;
	}

	get isDark(): boolean {
		return this.#mode === 'dark';
	}

	set(mode: ThemeMode) {
		this.#mode = mode;
		if (browser) {
			try {
				localStorage.setItem(STORAGE_KEY, mode);
			} catch {
				/* storage blocked — the theme still applies for this session */
			}
			this.#apply(mode, true);
		}
	}

	toggle() {
		this.set(this.#mode === 'dark' ? 'light' : 'dark');
	}

	/** Follow the OS preference; used by the "system" affordance. */
	useSystem() {
		this.set(systemMode());
	}

	#apply(mode: ThemeMode, announce: boolean) {
		const root = document.documentElement;
		root.classList.toggle('light', mode === 'light');
		root.classList.toggle('dark', mode === 'dark');
		root.style.colorScheme = mode;
		const meta = document.querySelector('meta[name="theme-color"]');
		if (meta) {
			meta.setAttribute('content', mode === 'light' ? '#f6f5f2' : '#070707');
		}
		if (announce) {
			document.dispatchEvent(new CustomEvent('cma-theme-change', { detail: mode }));
		}
	}
}

export const theme = new ThemeController();
