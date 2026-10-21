<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import AnswerTiles from '$lib/play/arena/AnswerTiles.svelte';
	import HostProgress from '$lib/play/admin/host-progress.svelte';

	const answers = [
		{ answer: 'Systolic pressure', color: '#e21b3c' },
		{ answer: 'Diastolic pressure', color: '#d89e00' },
		{ answer: 'Mean arterial pressure', color: '#7b3ff2' },
		{ answer: 'Pulse pressure', color: '#00b5e2' }
	];

	let mode = $state<'player' | 'host'>('player');
</script>

<div class="bg-paper min-h-dvh">
	<div class="flex gap-2 justify-center py-2 border-b border-white/10">
		<button type="button" class="btn btn-secondary text-sm" onclick={() => (mode = 'player')}>
			Player
		</button>
		<button type="button" class="btn btn-secondary text-sm" onclick={() => (mode = 'host')}>
			Host kahoot
		</button>
	</div>
	{#if mode === 'player'}
		<div data-testid="player-answer-screen">
			<AnswerTiles
				question="Which value is measured during ventricular contraction?"
				{answers}
				remainingSeconds={13}
				totalSeconds={30}
				interactive={true}
			/>
		</div>
	{:else}
		<div data-testid="host-answer-screen">
			<AnswerTiles
				question="Which value is measured during ventricular contraction?"
				{answers}
				remainingSeconds={13}
				totalSeconds={30}
				answeredCount={4}
			/>
		</div>
		<div data-testid="host-normal-screen" class="hidden">
			<HostProgress gamePin="123456" remainingSeconds={13} totalSeconds={30} answerCount={4} />
		</div>
	{/if}
</div>
