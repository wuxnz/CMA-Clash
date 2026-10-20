<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { ThumbsUp, ThumbsDown } from '@lucide/svelte';

	interface Props {
		quiz: {
			id: string;
			likes?: number;
			dislikes?: number;
		};
	}

	let { quiz = $bindable() }: Props = $props();

	const rate = async (positive: boolean) => {
		const res = await fetch(`/api/v1/community/rate/${quiz.id}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({ type: positive ? 'LIKE' : 'DISLIKE' })
		});
		if (res.status === 409) {
			alert('You already rated this quiz.');
			return;
		}
		if (!res.ok) return;
		if (positive) quiz.likes = (quiz.likes ?? 0) + 1;
		else quiz.dislikes = (quiz.dislikes ?? 0) + 1;
	};
</script>

<div class="inline-flex items-center gap-1">
	<button
		type="button"
		class="btn btn-ghost btn-sm w-auto min-w-11 px-2 text-ink-muted"
		aria-label="Like"
		onclick={() => rate(true)}
	>
		<ThumbsUp class="w-4 h-4" aria-hidden="true" />
		{#if (quiz.likes ?? 0) > 0}
			<span class="tabular-nums">{quiz.likes}</span>
		{/if}
	</button>
	<button
		type="button"
		class="btn btn-ghost btn-sm w-auto min-w-11 px-2 text-ink-muted"
		aria-label="Dislike"
		onclick={() => rate(false)}
	>
		<ThumbsDown class="w-4 h-4" aria-hidden="true" />
		{#if (quiz.dislikes ?? 0) > 0}
			<span class="tabular-nums">{quiz.dislikes}</span>
		{/if}
	</button>
</div>
