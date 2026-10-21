<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import TimerBar from '$lib/ui/TimerBar.svelte';
	import { getLocalization } from '$lib/i18n';

	interface Props {
		remainingSeconds: number;
		totalSeconds: number;
		answerCount: number;
	}

	let { remainingSeconds, totalSeconds, answerCount }: Props = $props();
	const { t } = getLocalization();
</script>

<div class="flex flex-col px-4 py-6 gap-6 max-w-md mx-auto w-full">
	<p class="text-sm text-ink-muted text-center">
		Players see the question on their devices. This screen tracks time and responses.
	</p>
	<TimerBar {remainingSeconds} {totalSeconds} showRing={false} />
	<p class="text-center text-xl text-ink font-mono tabular-nums">
		{$t('admin_page.answers_submitted', { answer_count: answerCount })}
	</p>
</div>
