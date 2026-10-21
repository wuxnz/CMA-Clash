<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';
	import TimerBar from '$lib/ui/TimerBar.svelte';
	import { getLocalization } from '$lib/i18n';

	interface Props {
		gamePin?: string;
		remainingSeconds: number;
		totalSeconds: number;
		answerCount: number;
	}

	let { gamePin, remainingSeconds, totalSeconds, answerCount }: Props = $props();
	const { t } = getLocalization();
</script>

<div class="min-h-dvh bg-paper flex flex-col">
	<LivePlayHeader pin={gamePin} />
	<div class="flex-1 flex flex-col items-center justify-center px-6 gap-8">
		<p class="text-sm text-ink-muted text-center max-w-md">
			Players see the question on their devices. This screen tracks time and responses.
		</p>
		<TimerBar {remainingSeconds} {totalSeconds} showRing={true} />
		<p class="text-center text-lg text-ink font-mono tabular-nums">
			{$t('admin_page.answers_submitted', { answer_count: answerCount })}
		</p>
	</div>
</div>
