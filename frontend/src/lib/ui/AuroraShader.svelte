<script lang="ts">
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	import { prefersReducedMotion } from './motion';

	interface Props {
		class?: string;
		paused?: boolean;
	}

	let { class: className = '', paused = false }: Props = $props();

	let canvas: HTMLCanvasElement;
	let reduced = prefersReducedMotion();
	let visible = $state(true);

	const vert = `
	attribute vec2 position;
	void main() { gl_Position = vec4(position, 0.0, 1.0); }
`;

	const frag = `
	precision highp float;
	uniform float uTime;
	uniform vec2 uRes;
	void main() {
		vec2 uv = gl_FragCoord.xy / uRes;
		vec2 p = uv * 2.0 - 1.0;
		p.x *= uRes.x / uRes.y;
		float t = uTime * 0.15;
		float wave = sin(p.x * 2.0 + t) * 0.12 + sin(p.y * 3.0 - t * 1.2) * 0.1;
		float glow = smoothstep(0.85, -0.2, p.y + wave);
		vec3 deep = vec3(0.02, 0.03, 0.07);
		vec3 blue = vec3(0.04, 0.35, 0.75);
		vec3 accent = vec3(0.05, 0.55, 0.92);
		vec3 col = mix(deep, blue, glow * 0.7);
		col = mix(col, accent, pow(glow, 2.0) * 0.35);
		gl_FragColor = vec4(col, 1.0);
	}
`;

	onMount(() => {
		if (!browser || reduced) return;

		const onVis = () => {
			visible = document.visibilityState === 'visible';
		};
		document.addEventListener('visibilitychange', onVis);

		const gl = canvas.getContext('webgl', { alpha: false, antialias: false });
		if (!gl) return;

		const compile = (type: number, src: string) => {
			const s = gl.createShader(type)!;
			gl.shaderSource(s, src);
			gl.compileShader(s);
			return s;
		};
		const prog = gl.createProgram()!;
		gl.attachShader(prog, compile(gl.VERTEX_SHADER, vert));
		gl.attachShader(prog, compile(gl.FRAGMENT_SHADER, frag));
		gl.linkProgram(prog);
		gl.useProgram(prog);

		const buf = gl.createBuffer()!;
		gl.bindBuffer(gl.ARRAY_BUFFER, buf);
		gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 1, -1, -1, 1, 1, 1]), gl.STATIC_DRAW);
		const loc = gl.getAttribLocation(prog, 'position');
		gl.enableVertexAttribArray(loc);
		gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);

		const uTime = gl.getUniformLocation(prog, 'uTime');
		const uRes = gl.getUniformLocation(prog, 'uRes');

		let raf = 0;
		const start = performance.now();
		const resize = () => {
			const dpr = Math.min(window.devicePixelRatio || 1, 2);
			canvas.width = canvas.clientWidth * dpr;
			canvas.height = canvas.clientHeight * dpr;
			gl.viewport(0, 0, canvas.width, canvas.height);
		};
		resize();
		const ro = new ResizeObserver(resize);
		ro.observe(canvas);

		const draw = () => {
			if (!paused && visible) {
				const t = (performance.now() - start) / 1000;
				gl.uniform1f(uTime, t);
				gl.uniform2f(uRes, canvas.width, canvas.height);
				gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
			}
			raf = requestAnimationFrame(draw);
		};
		draw();

		return () => {
			cancelAnimationFrame(raf);
			ro.disconnect();
			document.removeEventListener('visibilitychange', onVis);
		};
	});
</script>

{#if reduced}
	<div
		class="absolute inset-0 bg-gradient-to-b from-[#05070D] via-[#0A1628] to-[#05070D] {className}"
		aria-hidden="true"
	></div>
{:else}
	<canvas
		bind:this={canvas}
		class="absolute inset-0 w-full h-full {className}"
		aria-hidden="true"
	></canvas>
{/if}
