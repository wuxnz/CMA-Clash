/** Suppress CSS transitions during theme class swap (better-ui spec). */
export function swapThemeClass(useDark: boolean) {
	const root = document.documentElement;
	root.classList.add('theme-switching');
	if (useDark) {
		root.classList.add('dark');
		localStorage.setItem('theme', 'dark');
	} else {
		root.classList.remove('dark');
		localStorage.setItem('theme', 'light');
	}
	// force style flush
	void root.offsetHeight;
	requestAnimationFrame(() => {
		root.classList.remove('theme-switching');
	});
}
