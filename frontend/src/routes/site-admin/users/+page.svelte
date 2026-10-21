<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import Footer from '$lib/footer.svelte';
	import Button from '$lib/ui/Button.svelte';
	import Spinner from '$lib/Spinner.svelte';
	import { navbarVisible } from '$lib/stores.svelte.ts';
	import { focusTrap } from '$lib/ui/focusTrap';
	import { onMount } from 'svelte';
	import { formatApiErrorDetail } from '$lib/apiErrorDetail';

	const DELETE_TIMEOUT_MS = 30_000;

	navbarVisible.visible = true;

	type AdminUserRow = {
		id: string;
		username: string;
		email: string;
		verified: boolean;
		created_at: string;
		quiz_count: number;
	};

	let query = $state('');
	let page = $state(1);
	let loading = $state(false);
	let rows = $state<AdminUserRow[]>([]);
	let total = $state(0);
	let pageSize = $state(50);
	let banner = $state<{ kind: 'success' | 'error'; text: string } | null>(null);

	let deleteTarget = $state<AdminUserRow | null>(null);
	let deleteConfirm = $state('');
	let deleteBusy = $state(false);

	async function loadUsers() {
		loading = true;
		banner = null;
		try {
			const params = new URLSearchParams({
				q: query.trim(),
				page: String(page),
				page_size: String(pageSize)
			});
			const res = await fetch(`/api/v1/admin/users?${params}`, { credentials: 'include' });
			if (res.status === 403) {
				window.location.assign('/dashboard');
				return;
			}
			if (!res.ok) {
				banner = { kind: 'error', text: 'Could not load users.' };
				return;
			}
			const data = await res.json();
			rows = data.items ?? [];
			total = data.total ?? 0;
			pageSize = data.page_size ?? 50;
		} finally {
			loading = false;
		}
	}

	function onSearchSubmit(e: Event) {
		e.preventDefault();
		page = 1;
		loadUsers();
	}

	function openDelete(row: AdminUserRow) {
		deleteTarget = row;
		deleteConfirm = '';
	}

	function closeDelete() {
		deleteTarget = null;
		deleteConfirm = '';
	}

	async function confirmDelete() {
		if (!deleteTarget || deleteConfirm !== deleteTarget.username) {
			return;
		}
		deleteBusy = true;
		banner = null;
		const controller = new AbortController();
		const timeoutId = setTimeout(() => controller.abort(), DELETE_TIMEOUT_MS);
		try {
			const res = await fetch(
				`/api/v1/admin/user/id?user_id=${encodeURIComponent(deleteTarget.id)}`,
				{ method: 'DELETE', credentials: 'include', signal: controller.signal }
			);
			if (!res.ok) {
				const body = await res.json().catch(() => ({}));
				banner = {
					kind: 'error',
					text: formatApiErrorDetail(body.detail, 'Delete failed.')
				};
				return;
			}
			banner = { kind: 'success', text: `Deleted user ${deleteTarget.username}.` };
			closeDelete();
			await loadUsers();
		} catch (err) {
			if (err instanceof DOMException && err.name === 'AbortError') {
				banner = {
					kind: 'error',
					text: 'Delete timed out. The server may still be working; refresh and check the list.'
				};
			} else {
				banner = { kind: 'error', text: 'Delete failed.' };
			}
		} finally {
			clearTimeout(timeoutId);
			deleteBusy = false;
		}
	}

	const pageCount = $derived(Math.max(1, Math.ceil(total / pageSize)));
	const canDelete = $derived(
		deleteTarget !== null && deleteConfirm === deleteTarget?.username && !deleteBusy
	);

	onMount(() => {
		loadUsers();
	});
</script>

<svelte:head>
	<title>CMA Clash: Site admin users</title>
</svelte:head>

<div class="min-h-screen flex flex-col">
	<div class="w-full max-w-6xl mx-auto px-4 pt-8 pb-16 min-w-0">
		<h1 class="text-xl sm:text-2xl font-semibold text-ink tracking-tight">Site admin</h1>
		<p class="text-sm text-ink-muted mt-1">Search accounts and delete users when needed.</p>

		{#if banner}
			<p
				class="mt-4 text-sm rounded-lg px-3 py-2 border {banner.kind === 'success'
					? 'border-primary/40 text-ink bg-primary/10'
					: 'border-danger/40 text-danger bg-danger/10'}"
				role="status"
			>
				{banner.text}
			</p>
		{/if}

		<form class="mt-6 flex flex-col sm:flex-row gap-2" onsubmit={onSearchSubmit}>
			<label class="sr-only" for="user-search">Search users</label>
			<input
				id="user-search"
				class="ledger-input min-h-11 flex-1"
				placeholder="Email or username"
				bind:value={query}
				autocomplete="off"
			/>
			<Button type="submit" class="w-auto sm:w-32" disabled={loading}>Search</Button>
		</form>

		<div class="mt-6 overflow-x-auto rounded-xl border border-white/10">
			<table class="w-full text-sm text-left">
				<caption class="sr-only">User search results</caption>
				<thead class="bg-paper-muted text-ink-muted">
					<tr>
						<th class="px-3 py-2 font-medium">Username</th>
						<th class="px-3 py-2 font-medium">Email</th>
						<th class="px-3 py-2 font-medium">Verified</th>
						<th class="px-3 py-2 font-medium">Quizzes</th>
						<th class="px-3 py-2 font-medium">Joined</th>
						<th class="px-3 py-2 font-medium"><span class="sr-only">Actions</span></th>
					</tr>
				</thead>
				<tbody>
					{#if loading && rows.length === 0}
						<tr>
							<td colspan="6" class="px-3 py-8 text-center text-ink-muted">
								<Spinner class="h-5 w-5 mx-auto" my_20={false} />
							</td>
						</tr>
					{:else if rows.length === 0}
						<tr>
							<td colspan="6" class="px-3 py-8 text-center text-ink-muted">No users found.</td>
						</tr>
					{:else}
						{#each rows as row (row.id)}
							<tr class="border-t border-white/5">
								<td class="px-3 py-2 font-medium text-ink">{row.username}</td>
								<td class="px-3 py-2 text-ink-muted">{row.email}</td>
								<td class="px-3 py-2">{row.verified ? 'Yes' : 'No'}</td>
								<td class="px-3 py-2 tabular-nums">{row.quiz_count}</td>
								<td class="px-3 py-2 text-ink-muted whitespace-nowrap">
									{new Date(row.created_at).toLocaleDateString()}
								</td>
								<td class="px-3 py-2 text-right">
									<button
										type="button"
										class="text-danger text-sm hover:underline min-h-11 px-2"
										onclick={() => openDelete(row)}
									>
										Delete
									</button>
								</td>
							</tr>
						{/each}
					{/if}
				</tbody>
			</table>
		</div>

		{#if total > pageSize}
			<div class="mt-4 flex items-center justify-between gap-3 text-sm text-ink-muted">
				<p>Page {page} of {pageCount} ({total} users)</p>
				<div class="flex gap-2">
					<Button
						type="button"
						variant="secondary"
						class="w-auto"
						disabled={page <= 1 || loading}
						onclick={() => {
							page -= 1;
							loadUsers();
						}}
					>
						Previous
					</Button>
					<Button
						type="button"
						variant="secondary"
						class="w-auto"
						disabled={page >= pageCount || loading}
						onclick={() => {
							page += 1;
							loadUsers();
						}}
					>
						Next
					</Button>
				</div>
			</div>
		{/if}
	</div>
	<Footer />
</div>

{#if deleteTarget}
	<div
		class="dialog-backdrop"
		role="presentation"
		onclick={(e) => {
			if (e.target === e.currentTarget) closeDelete();
		}}
	>
		<div
			use:focusTrap
			class="dialog-panel dialog-panel-in p-5 max-w-md w-full"
			role="dialog"
			aria-modal="true"
			aria-labelledby="delete-user-title"
			tabindex="-1"
		>
			<h2 id="delete-user-title" class="text-lg font-semibold text-ink tracking-tight">
				Delete {deleteTarget.username}?
			</h2>
			<p class="text-sm text-ink-muted mt-2 leading-relaxed">
				This removes the account, quizzes, and related data. Type the username to confirm.
			</p>
			<label class="block mt-4 text-sm font-medium text-ink" for="delete-confirm">
				Username
			</label>
			<input
				id="delete-confirm"
				class="ledger-input mt-1 min-h-11"
				bind:value={deleteConfirm}
				autocomplete="off"
			/>
			<div class="mt-6 flex gap-2 justify-end">
				<Button type="button" variant="secondary" class="w-auto" onclick={closeDelete}>Cancel</Button>
				<Button
					type="button"
					class="w-auto"
					disabled={!canDelete}
					onclick={confirmDelete}
				>
					{#if deleteBusy}
						<Spinner class="h-4 w-4" my_20={false} />
					{:else}
						Delete user
					{/if}
				</Button>
			</div>
		</div>
	</div>
{/if}
