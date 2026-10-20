<script lang="ts">
	import { CERT_FILTERS, DIFFICULTY_FILTERS } from './labels';

	interface Props {
		cert: string;
		difficulty: string;
		sort?: string;
		showSort?: boolean;
	}

	let { cert = $bindable(), difficulty = $bindable(), sort = $bindable('relevance'), showSort = true }: Props =
		$props();
</script>

<div class="flex flex-col gap-3 min-w-0">
	<div class="chip-row -mx-4 px-4 sm:mx-0 sm:px-0" role="tablist" aria-label="Certification">
		{#each CERT_FILTERS as item}
			<button
				type="button"
				role="tab"
				aria-selected={cert === item.slug}
				class="chip {cert === item.slug ? 'chip-active' : ''}"
				onclick={() => (cert = item.slug)}
			>
				{item.label}
			</button>
		{/each}
	</div>
	<div class="flex flex-wrap items-center gap-3 min-w-0">
		<div class="chip-row min-w-0 flex-1" role="tablist" aria-label="Difficulty">
			{#each DIFFICULTY_FILTERS as item}
				<button
					type="button"
					role="tab"
					aria-selected={difficulty === item.value}
					class="chip {difficulty === item.value ? 'chip-active' : ''}"
					onclick={() => (difficulty = item.value)}
				>
					{item.label}
				</button>
			{/each}
		</div>
		{#if showSort}
			<label class="sr-only" for="browse-sort">Sort</label>
			<select id="browse-sort" class="ledger-input w-auto min-h-11 text-sm" bind:value={sort}>
				<option value="relevance">Relevance</option>
				<option value="newest">Newest</option>
				<option value="plays">Most played</option>
			</select>
		{/if}
	</div>
</div>
