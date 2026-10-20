/** Lazy-loaded GSAP + ScrollTrigger (client only). */

let gsapPromise: Promise<typeof import('gsap').gsap> | null = null;

export function loadGsap(): Promise<typeof import('gsap').gsap> {
	if (typeof window === 'undefined') {
		return Promise.reject(new Error('gsap is client-only'));
	}
	if (!gsapPromise) {
		gsapPromise = import('gsap').then(async (mod) => {
			const { ScrollTrigger } = await import('gsap/ScrollTrigger');
			mod.gsap.registerPlugin(ScrollTrigger);
			return mod.gsap;
		});
	}
	return gsapPromise;
}

export async function loadFlip() {
	const gsap = await loadGsap();
	const { Flip } = await import('gsap/Flip');
	gsap.registerPlugin(Flip);
	return { gsap, Flip };
}
