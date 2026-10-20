<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { goto } from '$app/navigation';
	import type { PageData } from './$types';

	interface Props {
		data: PageData;
	}

	let { data }: Props = $props();
	let input_data = $state({
		player_name: data.username,
		name: ''
	});

	let isValid = $derived(input_data.name.length !== 0 && input_data.player_name.length !== 0);
	let isSubmitting = false;

	const submit = async (e: Event) => {
		e.preventDefault();
		if (!isValid) {
			return;
		}
		const res = await fetch('/api/v1/box-controller/web/setup', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(input_data)
		});
		if (res.ok) {
			const json = await res.json();
			goto(`/account/controllers/add/wait?id=${json.id}&code=${json.code}`);
		}
	};
</script>

<div class="flex items-center justify-center h-full px-4">
	<div>
		<div
			class="w-full max-w-sm mx-auto overflow-hidden bg-surface rounded-lg shadow-md"
		>
			<div class="px-6 py-4">
				<h2 class="text-3xl font-bold text-center text-ink">
					CMA Clash
				</h2>

				<h3 class="mt-1 text-xl font-medium text-center text-ink-muted">
					Add a controller
				</h3>

				<form onsubmit={submit}>
					<div class="w-full mt-4">
						<div class="bg-surface p-4 rounded-lg">
							<div class="relative bg-inherit w-full">
								<input
									id="player_name"
									name="player_name"
									type="text"
									class="w-full peer bg-transparent h-10 rounded-lg text-ink placeholder-transparent ring-2 px-2 ring-ink/30 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
									class:ring-red-700={input_data.player_name.length === 0}
									class:ring-green-600={input_data.player_name.length !== 0}
									bind:value={input_data.player_name}
								/>
								<label
									for="player_name"
									class="absolute cursor-text left-0 -top-3 text-sm text-ink bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-ink-muted peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
								>
									Player name
								</label>
							</div>
						</div>
						<div class="bg-surface p-4 rounded-lg">
							<div class="relative bg-inherit w-full">
								<input
									id="name"
									name="name"
									type="text"
									class="w-full peer bg-transparent h-10 rounded-lg text-ink placeholder-transparent ring-2 px-2 ring-ink/30 focus:ring-sky-600 focus:outline-hidden focus:border-rose-600"
									placeholder="Name"
									class:ring-red-700={input_data.name.length === 0}
									class:ring-green-600={input_data.name.length !== 0}
									bind:value={input_data.name}
								/>
								<label
									for="name"
									class="absolute cursor-text left-0 -top-3 text-sm text-ink bg-inherit mx-1 px-1 peer-placeholder-shown:text-base peer-placeholder-shown:text-ink-muted peer-placeholder-shown:top-2 peer-focus:-top-3 peer-focus:text-sky-600 peer-focus:text-sm transition-all"
								>
									Name
								</label>
							</div>
						</div>

						<div class="flex items-center justify-center mt-4">
							<button
								class="px-4 py-2 leading-5 text-white transition-colors duration-200 transform bg-elevated rounded-sm hover:bg-primary-hover focus:outline-hidden"
								disabled={!isValid || isSubmitting}
								class:cursor-not-allowed={!isValid || isSubmitting}
								class:opacity-50={!isValid || isSubmitting}
								type="submit"
							>
								{#if isSubmitting}
									<svg class="h-4 w-4 animate-spin" viewBox="3 3 18 18">
										<path
											class="fill-blue-800"
											d="M12 5C8.13401 5 5 8.13401 5 12C5 15.866 8.13401 19 12 19C15.866 19 19 15.866 19 12C19 8.13401 15.866 5 12 5ZM3 12C3 7.02944 7.02944 3 12 3C16.9706 3 21 7.02944 21 12C21 16.9706 16.9706 21 12 21C7.02944 21 3 16.9706 3 12Z"
										/>
										<path
											class="fill-blue-100"
											d="M16.9497 7.05015C14.2161 4.31648 9.78392 4.31648 7.05025 7.05015C6.65973 7.44067 6.02656 7.44067 5.63604 7.05015C5.24551 6.65962 5.24551 6.02646 5.63604 5.63593C9.15076 2.12121 14.8492 2.12121 18.364 5.63593C18.7545 6.02646 18.7545 6.65962 18.364 7.05015C17.9734 7.44067 17.3403 7.44067 16.9497 7.05015Z"
										/>
									</svg>
								{:else}
									Add
								{/if}
							</button>
						</div>
					</div>
				</form>
			</div>

			<div
				class="flex items-center justify-center py-4 text-center bg-paper-muted"
			>
				<span class="text-sm text-ink-muted"
					>Don't know what this is?
				</span>

				<a
					href="/controller"
					class="mx-2 text-sm font-bold text-primary hover:underline"
					>Read more here.</a
				>
			</div>
		</div>
	</div>
</div>
