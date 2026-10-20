<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { onMount } from 'svelte';
	import Editor from '$lib/editor.svelte';
	import { getLocalization } from '$lib/i18n';
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import type { Question } from '$lib/quiz_types';
	import { page } from '$app/state';
	import Button from '$lib/ui/Button.svelte';
	import { focusTrap } from '$lib/ui/focusTrap';

	navbarVisible.visible = false;

	const { t } = getLocalization();

	interface Data {
		public: boolean;
		title: string;
		description: string;
		questions: Question[];
	}

	let responseData = {
		open: false
	};

	let data: Data = $state();
	let quiz_id = $state(null);
	onMount(() => {
		const from_localstorage = localStorage.getItem('create_game');
		if (from_localstorage === null) {
			let title = page.url.searchParams.get('title');
			title ??= '';
			data = {
				description: '',
				public: false,
				title,
				questions: [
					/*					{
						type: QuizQuestionType.ABCD,
						question: '',
						time: '20',
						answers: [{ right: false, answer: '' }]
					}*/
				]
			};
		} else {
			data = JSON.parse(from_localstorage);
		}
	});
</script>

<svelte:head>
	<title>CMA Clash: Create</title>
</svelte:head>

{#if data !== undefined}
	<Editor bind:data bind:quiz_id />
{/if}

{#if responseData.open}
	<div class="dialog-backdrop" role="presentation">
		<div
			use:focusTrap
			class="dialog-panel dialog-panel-in p-5"
			role="dialog"
			aria-modal="true"
			aria-labelledby="create-success-title"
			tabindex="-1"
		>
			<h2 id="create-success-title" class="text-lg font-semibold text-ink tracking-tight">
				{$t('create_page.success.title')}
			</h2>
			<p class="text-sm text-ink-muted mt-2">{$t('create_page.success.body')}</p>
			<div class="mt-6">
				<Button class="w-full" onclick={() => (window.location.href = '/dashboard')}>
					{$t('words.close')}
				</Button>
			</div>
		</div>
	</div>
{/if}
