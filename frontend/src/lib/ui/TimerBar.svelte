<script lang="ts">
	interface Props {
		remainingSeconds: number;
		totalSeconds: number;
	}

	let { remainingSeconds, totalSeconds }: Props = $props();

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
