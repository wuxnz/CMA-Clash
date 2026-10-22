<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { goto } from '$app/navigation';
	import { resolve } from '$app/paths';
	import type { Pathname } from '$app/types';
	import type { PageData } from './$types';
	import Button from '$lib/ui/Button.svelte';
	import Spinner from '$lib/Spinner.svelte';
	import Footer from '$lib/footer.svelte';
	import { navbarVisible } from '$lib/stores.svelte';

	navbarVisible.visible = true;

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
	let input_data = $state({
		player_name: data.username,
		name: ''
	});

	let isValid = $derived(input_data.name.length !== 0 && input_data.player_name.length !== 0);
	let isSubmitting = $state(false);

	const submit = async (e: Event) => {
		e.preventDefault();
		if (!isValid) {
			return;
		}
		isSubmitting = true;
		const res = await fetch('/api/v1/box-controller/web/setup', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(input_data)
		});
		if (res.ok) {
			const json = await res.json();
			goto(resolve(`/account/controllers/add/wait?id=${json.id}&code=${json.code}` as Pathname));
		}
		isSubmitting = false;
	};
</script>

<svelte:head>
	<title>CMA Clash: Add controller</title>
</svelte:head>

<div class="flex items-center justify-center min-h-[80vh] px-4">
	<div
		class="w-full max-w-sm mx-auto overflow-hidden bg-surface rounded-2xl border border-white/10 shadow-[var(--shadow-card)]"
	>
		<div class="px-6 py-6">
			<h1 class="text-xl font-semibold text-ink tracking-tight text-center">Add a controller</h1>
			<form onsubmit={submit} class="mt-6 space-y-4">
				<div>
					<label class="text-sm font-medium text-ink" for="player_name">Player name</label>
					<input
						id="player_name"
						name="player_name"
						type="text"
						class="ledger-input mt-1 min-h-11"
						bind:value={input_data.player_name}
					/>
				</div>
				<div>
					<label class="text-sm font-medium text-ink" for="name">Name</label>
					<input
						id="name"
						name="name"
						type="text"
						class="ledger-input mt-1 min-h-11"
						placeholder="Name"
						bind:value={input_data.name}
					/>
				</div>
				<Button class="w-full" disabled={!isValid || isSubmitting} type="submit">
					{#if isSubmitting}
						<Spinner class="h-4 w-4" my_20={false} />
					{:else}
						Add
					{/if}
				</Button>
			</form>
		</div>
		<div class="flex items-center justify-center py-4 text-center bg-paper-muted px-4">
			<span class="text-sm text-ink-muted">Don't know what this is?</span>
			<a href={resolve('/controller')} class="mx-2 text-sm text-ink link-hover">Read more</a>
		</div>
	</div>
</div>
<Footer />
