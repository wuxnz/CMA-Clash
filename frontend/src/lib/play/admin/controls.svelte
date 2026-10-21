<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { QuizQuestionType } from '$lib/quiz_types';
	import { getLocalization } from '$lib/i18n';
	import { SocketGameControls } from '$lib/play/admin/socket_game_controls.ts';
	import type { GameState } from '$lib/play/admin/game_state.ts';

	interface Props {
		bg_color: string;
		socket_game_controls: SocketGameControls;
		game_token: string;
		game_state: GameState;
	}

	let { bg_color, socket_game_controls, game_token, game_state = $bindable() }: Props = $props();

	const { t } = getLocalization();

	const show_solutions = () => {
		socket_game_controls.show_solutions();
		game_state.timer_res = '0';
	};
</script>

<div
	class="fixed inset-x-0 bottom-0 z-30 border-t border-white/10 bg-surface/95 backdrop-blur-md px-3 py-3 safe-bottom"
	style="background: {bg_color ? `${bg_color}ee` : undefined}"
>
	<div class="max-w-xl mx-auto flex flex-wrap gap-2 justify-end">
		{#if game_state.selected_question + 1 === game_state.quiz_data.questions.length && ((game_state.timer_res === '0' && game_state.question_results !== null) || game_state.quiz_data?.questions?.[game_state.selected_question]?.type === QuizQuestionType.SLIDE)}
			{#if JSON.stringify(game_state.final_results) === JSON.stringify([null])}
				<button
					type="button"
					onclick={() => socket_game_controls.get_final_results()}
					class="admin-button flex-1 min-w-[10rem]"
				>
					{$t('admin_page.get_final_results')}
				</button>
			{/if}
		{:else if game_state.timer_res === '0' || game_state.selected_question === -1}
			{#if (game_state.selected_question + 1 !== game_state.quiz_data.questions.length && game_state.question_results !== null) || game_state.selected_question === -1}
				<button
					type="button"
					onclick={() => {
						socket_game_controls.set_question_number(game_state.selected_question + 1);
					}}
					class="admin-button flex-1 min-w-[10rem]"
				>
					{$t('admin_page.next_question', {
						question: game_state.selected_question + 2
					})}
				</button>
			{/if}
			{#if game_state.question_results === null && game_state.selected_question !== -1}
				{#if game_state.quiz_data.questions[game_state.selected_question].type === QuizQuestionType.SLIDE}
					<button
						type="button"
						onclick={() => {
							socket_game_controls.set_question_number(game_state.selected_question + 1);
						}}
						class="admin-button flex-1 min-w-[10rem]"
					>
						{$t('admin_page.next_question', {
							question: game_state.selected_question + 2
						})}
					</button>
				{:else if game_state.quiz_data.questions[game_state.selected_question]?.hide_results === true}
					<button
						type="button"
						onclick={() => {
							socket_game_controls.get_question_results(
								game_token,
								game_state.shown_question_now
							);
							setTimeout(() => {
								socket_game_controls.set_question_number(game_state.selected_question + 1);
							}, 200);
						}}
						class="admin-button flex-1 min-w-[10rem]"
					>
						{$t('admin_page.next_question', {
							question: game_state.selected_question + 2
						})}
					</button>
				{:else}
					<button
						type="button"
						onclick={() =>
							socket_game_controls.get_question_results(
								game_token,
								game_state.shown_question_now
							)}
						class="admin-button flex-1 min-w-[10rem]"
					>
						{$t('admin_page.show_results')}
					</button>
				{/if}
			{/if}
		{:else if game_state.selected_question !== -1}
			{#if game_state.quiz_data.questions[game_state.selected_question].type === QuizQuestionType.SLIDE}
				<button
					type="button"
					onclick={() => {
						socket_game_controls.set_question_number(game_state.selected_question + 1);
					}}
					class="admin-button flex-1 min-w-[10rem]"
				>
					{$t('admin_page.next_question', {
						question: game_state.selected_question + 2
					})}
				</button>
			{:else}
				<button type="button" onclick={show_solutions} class="admin-button flex-1 min-w-[10rem]">
					{$t('admin_page.stop_time_and_solutions')}
				</button>
			{/if}
		{/if}
	</div>
</div>

<style>
	.safe-bottom {
		padding-bottom: max(0.75rem, env(safe-area-inset-bottom));
	}
</style>
