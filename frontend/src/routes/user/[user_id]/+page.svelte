<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import type { PageData } from './$types';
	import { getLocalization } from '$lib/i18n';
	import { signedIn } from '$lib/stores';
	import StartGamePopup from '$lib/dashboard/start_game.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';
	import QuizBrowseList from '$lib/quiz/QuizBrowseList.svelte';
	import { certLabelFor } from '$lib/quiz/labels';
	import Button from '$lib/ui/Button.svelte';

	navbarVisible.visible = true;
	const { t } = getLocalization();
	let start_game = $state<string | null>(null);

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();

	const rows = $derived(
		(data.quizzes ?? []).map((quiz: Record<string, unknown>) => ({
			...quiz,
			id: String(quiz.id),
			title: String(quiz.title ?? ''),
			certLabel: certLabelFor({ title: String(quiz.title ?? '') })
		}))
	);
</script>

<svelte:head>
	<title>CMA Clash — {data.user.username ? `@${data.user.username}` : 'User'}</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
		{#if !data.user.username}
			<h1 class="text-xl font-semibold text-ink">{$t('public_user_page.user_not_found')}</h1>
		{:else}
			<div class="flex items-center gap-4 min-w-0">
				<img
					src={`/api/v1/users/avatar/${data.user.id}`}
					alt=""
					class="w-14 h-14 rounded-lg bg-elevated object-cover shrink-0"
				/>
				<div class="min-w-0">
					<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight truncate">
						@{data.user.username}
					</h1>
					<p class="text-sm text-ink-muted mt-1">
						{$t('public_user_page.joined_on', {
							date: new Date(data.user.created_at).toLocaleDateString()
						})}
					</p>
				</div>
			</div>

			<section class="mt-10">
				<h2 class="text-sm font-semibold text-ink mb-2">Quizzes</h2>
				{#if rows.length === 0}
					<p class="text-sm text-ink-muted">{$t('public_user_page.no_original_quizzes')}</p>
				{:else if $signedIn}
					<QuizBrowseList items={rows} onHost={(id) => (start_game = id)} />
				{:else}
					<QuizBrowseList items={rows} />
					<p class="text-sm text-ink-muted mt-4">
						<Button href="/account/login" variant="ghost" class="w-auto">Sign in</Button>
						to host.
					</p>
				{/if}
			</section>
		{/if}
	</div>
	<Footer />
</div>

{#if start_game !== null}
	<StartGamePopup bind:quiz_id={start_game} />
{/if}
