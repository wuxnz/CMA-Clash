<script lang="ts">
	import { prefersReducedMotion } from './motion';

	interface Props {
		remainingSeconds: number;
		totalSeconds: number;
		/** Compact ring (CSS-only — safe for live play). */
		showRing?: boolean;
	}

	let { remainingSeconds, totalSeconds, showRing = false }: Props = $props();

	const reduced = prefersReducedMotion();
	const ringR = 18;
	const ringC = 2 * Math.PI * ringR;

	let progress = $derived(
		totalSeconds > 0 ? Math.max(0, Math.min(1, remainingSeconds / totalSeconds)) : 0
	);

	function formatTime(sec: number): string {
		const s = Math.max(0, Math.floor(sec));
		const m = Math.floor(s / 60);
		const r = s % 60;
		return `${String(m).padStart(2, '0')}:${String(r).padStart(2, '0')}`;
	}
</script>

<div class="flex items-center gap-3 w-full">
	{#if showRing}
		<div class="relative w-11 h-11 shrink-0" aria-hidden="true">
			<svg class="w-full h-full -rotate-90" viewBox="0 0 44 44">
				<circle
					cx="22"
					cy="22"
					r={ringR}
					fill="none"
					stroke="currentColor"
					stroke-width="3"
					class="text-paper-muted/80"
				/>
				<circle
					cx="22"
					cy="22"
					r={ringR}
					fill="none"
					stroke="currentColor"
					stroke-width="3"
					stroke-linecap="round"
					class="text-primary"
					stroke-dasharray={ringC}
					stroke-dashoffset={ringC * (1 - progress)}
					style="transition: {reduced ? 'none' : 'stroke-dashoffset 1s linear'}"
				/>
			</svg>
			<span
				class="absolute inset-0 flex items-center justify-center font-mono text-[10px] tabular-nums text-ink"
			>
				{Math.max(0, Math.ceil(remainingSeconds))}
			</span>
		</div>
	{/if}
	<div
		class="flex-1 h-2.5 rounded-full bg-paper-muted overflow-hidden border border-ink/10"
		role="progressbar"
		aria-valuenow={remainingSeconds}
		aria-valuemin={0}
		aria-valuemax={totalSeconds}
		aria-label="Time remaining"
	>
		<div
			class="h-full rounded-full bg-primary transition-[width] duration-1000 ease-linear motion-reduce:transition-none"
			style="width: {progress * 100}%"
		></div>
	</div>
	<span class="font-mono text-sm tabular-nums text-ink shrink-0 min-w-[3.25rem] text-right">
		{formatTime(remainingSeconds)}
	</span>
</div>
