<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { getLocalization } from '$lib/i18n';
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { onMount } from 'svelte';
	import { page } from '$app/state';
	import Spinner from '$lib/Spinner.svelte';
	import Button from '$lib/ui/Button.svelte';
	import Footer from '$lib/footer.svelte';
	import { resolve } from '$app/paths';

	navbarVisible.visible = true;

	const { t } = getLocalization();
	let url_input = $state('');
	let file_input: FileList | undefined = $state();
	let kahoot_regex = /^https:\/\/create\.kahoot\.it\/details\/.*\/?([a-zA-Z-\d]{36})\/?$/;
	let url_valid = $derived(kahoot_regex.test(url_input));
	let is_loading = $state(false);
	let error = $state('');

	const submit = async (e: Event) => {
		e.preventDefault();
		if (!url_valid) return;
		is_loading = true;
		error = '';
		const regex_res = kahoot_regex.exec(url_input);
		const res = await fetch(`/api/v1/quiz/import/${regex_res?.[1]}`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' }
		});
		if (res.status === 200) {
			window.location.href = '/dashboard';
			return;
		}
		if (res.status === 400) error = "This quiz isn't supported yet.";
		else if (res.status === 403) error = 'Quiz is probably private.';
		else error = `Kahoot replied with ${res.status}`;
		is_loading = false;
	};

	const file_submit = async (e: Event) => {
		e.preventDefault();
		if (!file_input?.[0]) return;
		is_loading = true;
		error = '';
		const formdata = new FormData();
		formdata.append('file', file_input[0]);
		let res: Response;
		if (file_input[0].name.includes('.xlsx')) {
			res = await fetch('/api/v1/quiz/excel-import', { method: 'POST', body: formdata });
		} else if (file_input[0].name.includes('.cqa')) {
			res = await fetch('/api/v1/eximport/', { method: 'POST', body: formdata });
		} else {
			error = 'Use a .cqa or .xlsx file.';
			is_loading = false;
			return;
		}
		if (res.status === 200) {
			window.location.href = '/dashboard';
			return;
		}
		error = 'Import failed.';
		is_loading = false;
	};

	onMount(() => {
		url_input = page.url.searchParams.get('url') ?? '';
	});
</script>

<svelte:head>
	<title>CMA Clash — Import</title>
</svelte:head>

<div class="min-h-screen flex flex-col overflow-x-hidden">
	<div class="w-full max-w-3xl mx-auto px-4 pt-8 pb-16 min-w-0 flex-1">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Import</h1>
		{#if error}
			<p class="text-sm text-danger mt-3">{error}</p>
		{/if}

		<div class="mt-8 grid grid-cols-1 md:grid-cols-2 gap-10">
			<form onsubmit={submit} class="min-w-0">
				<h2 class="text-sm font-semibold text-ink">Kahoot URL</h2>
				<p class="text-sm text-ink-muted mt-1">{$t('import_page.url_should_look_like_this')}</p>
				<label class="sr-only" for="url">Kahoot URL</label>
				<input
					id="url"
					bind:value={url_input}
					name="url"
					type="url"
					class="ledger-input mt-3 min-h-11"
					placeholder="https://create.kahoot.it/details/…"
				/>
				<p class="text-sm text-ink-muted mt-2">{$t('import_page.side_import_kahoot')}</p>
				<Button class="w-full sm:w-auto mt-4" type="submit" disabled={!url_valid || is_loading}>
					{#if is_loading}
						<Spinner class="h-4 w-4" my_20={false} />
					{/if}
					{$t('words.submit')}
				</Button>
			</form>

			<form onsubmit={file_submit} class="min-w-0 md:border-l md:border-white/[0.07] md:pl-10">
				<h2 class="text-sm font-semibold text-ink">File</h2>
				<p class="text-sm text-ink-muted mt-1">{$t('import_page.upload_file_ending')}</p>
				<label class="sr-only" for="file">Quiz file</label>
				<input
					id="file"
					bind:files={file_input}
					name="file"
					type="file"
					accept=".cqa,.xlsx"
					class="ledger-input mt-3 min-h-11 file:mr-3 file:border-0 file:bg-transparent file:text-ink"
				/>
				<p class="text-sm text-ink-muted mt-2">
					{$t('import_page.this_side_cma_clash')}
					{$t('import_page.this_side_cma_clash_excel')}
				</p>
				<a
					class="text-sm text-ink link-hover inline-flex min-h-11 items-center"
					download
					href="https://blog.web.garage.realux.mawoka.eu/classquiz/ClassQuizImportTemplate.xlsx"
					>{$t('import_page.download_template_here')}</a
				>
				<Button class="w-full sm:w-auto mt-4" type="submit" disabled={!file_input || is_loading}>
					{#if is_loading}
						<Spinner class="h-4 w-4" my_20={false} />
					{/if}
					{$t('words.submit')}
				</Button>
			</form>
		</div>

		<p class="text-sm text-ink-muted mt-10">
			{$t('import_page.need_help')}
			<a href={resolve('/docs/import-from-kahoot')} class="text-ink link-hover"
				>{$t('import_page.visit_docs')}</a
			>
		</p>
	</div>
	<Footer />
</div>
