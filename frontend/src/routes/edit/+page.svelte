<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Spinner from '$lib/Spinner.svelte';
	import Editor from '$lib/editor.svelte';
	import { getLocalization } from '$lib/i18n';
	import { navbarVisible} from '$lib/stores.svelte.ts';
	import { QuizQuestionType } from '$lib/quiz_types';
	import Button from '$lib/ui/Button.svelte';
	import { focusTrap } from '$lib/ui/focusTrap';

	navbarVisible.visible= false;

	const { t } = getLocalization();

	let responseData = {
		open: false,
		data: ''
	};

	interface Data {
		public: boolean;
		title: string;
		description: string;
		questions: Question[];
	}

	interface Question {
		question: string;
		time: string;
		answers: Answer[];
	}

	interface Answer {
		right: boolean;
		answer: string;
	}

	let { data } = $props();
	let { quiz_id } = $state(data);
	let quiz_data: Data = $state();

	const get_quiz = async (): Promise<void> => {
		const response = await fetch(`/api/v1/quiz/get/${quiz_id}`);
		if (response.status === 404) {
			throw new Error('Quiz not found');
		} else if (response.status === 200) {
			let temp_data = await response.json();
			for (let i = 0; i < temp_data.questions.length; i++) {
				let question = temp_data.questions[i];
				if (question.type === undefined) {
					temp_data.questions[i].type = QuizQuestionType.ABCD;
				} else {
					temp_data.questions[i].type = QuizQuestionType[question.type];
				}
			}
			quiz_data = temp_data;
			return;
		}
	};
</script>

<svelte:head>
	<title>CMA Clash: Edit</title>
</svelte:head>
{#await get_quiz()}
	<Spinner />
{:then _}
	{#if quiz_data !== undefined}
		<Editor bind:data={quiz_data} submit_button_text={$t('words.save')} bind:quiz_id />
	{/if}
{:catch err}
	<div class="min-h-[50vh] flex items-center justify-center px-4">
		<p class="text-lg font-semibold text-ink">{err.message}</p>
	</div>
{/await}

{#if responseData.open}
	<div class="dialog-backdrop" role="presentation">
		<div
			use:focusTrap
			class="dialog-panel dialog-panel-in p-5"
			role="dialog"
			aria-modal="true"
			aria-labelledby="edit-success-title"
			tabindex="-1"
		>
			<h2 id="edit-success-title" class="text-lg font-semibold text-ink tracking-tight">
				{$t('edit_page.success_update_title')}
			</h2>
			<p class="text-sm text-ink-muted mt-2">{$t('edit_page.success_update_body')}</p>
			<div class="mt-6">
				<Button class="w-full" onclick={() => (window.location.href = '/dashboard')}>
					{$t('words.close')}
				</Button>
			</div>
		</div>
	</div>
{/if}
