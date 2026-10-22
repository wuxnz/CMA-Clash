<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import type { PageData } from './$types';
	import PlayerOverview from './player_overview.svelte';
	import QuestionOverview from './question_overview.svelte';
	import GeneralOverview from './general_overview.svelte';
	import { fade } from 'svelte/transition';
	import { getLocalization } from '$lib/i18n';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';

	navbarVisible.visible = true;

	const { t } = getLocalization();

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	enum SelectedTab {
		// eslint-disable-next-line no-unused-vars
		Overview,
		// eslint-disable-next-line no-unused-vars
		Players,
		// eslint-disable-next-line no-unused-vars
		Questions
	}

	let selected_tab: SelectedTab = $state(SelectedTab.Overview);
</script>

<svelte:head>
	<title>CMA Clash: Result</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
	<div class="chip-row mb-6" role="tablist">
		<button
			type="button"
			role="tab"
			aria-selected={selected_tab === SelectedTab.Overview}
			onclick={() => {
				selected_tab = SelectedTab.Overview;
			}}
			class="chip {selected_tab === SelectedTab.Overview ? 'chip-active' : ''}"
		>
			{$t('words.overview')}
		</button>
		<button
			type="button"
			role="tab"
			aria-selected={selected_tab === SelectedTab.Players}
			onclick={() => {
				selected_tab = SelectedTab.Players;
			}}
			class="chip {selected_tab === SelectedTab.Players ? 'chip-active' : ''}"
		>
			{$t('words.player', { count: 2 })}
		</button>
		<button
			type="button"
			role="tab"
			aria-selected={selected_tab === SelectedTab.Questions}
			onclick={() => {
				selected_tab = SelectedTab.Questions;
			}}
			class="chip {selected_tab === SelectedTab.Questions ? 'chip-active' : ''}"
		>
			{$t('words.question', { count: 2 })}
		</button>
	</div>
	{#if selected_tab === SelectedTab.Overview}
		<div in:fade|global={{ duration: 150 }}>
			<GeneralOverview
				scores={data.results.player_scores}
				title={data.results.title}
				timestamp={data.results.timestamp}
			/>
		</div>
	{:else if selected_tab === SelectedTab.Questions}
		<div in:fade|global={{ duration: 150 }}>
			<QuestionOverview questions={data.results.questions} answers={data.results.answers} />
		</div>
	{:else if selected_tab === SelectedTab.Players}
		<div in:fade|global={{ duration: 150 }}>
			<PlayerOverview
				custom_field={data.results.custom_field_data}
				scores={data.results.player_scores}
				answers={data.results.answers}
			/>
		</div>
	{/if}
	</div>
	<Footer />
</div>
