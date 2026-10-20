<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	interface Props {
		open: boolean;
	}

	let { open = $bindable() }: Props = $props();

	const closeThing = () => {
		open = false;
		localStorage.setItem('newsletter', 'closed');
	};
</script>

<form method="post" action="#" class="bg-transparent">
	<div class="absolute top-1 right-1">
		<button type="button" aria-label="Close newsletter signup" onclick={closeThing}>
			<svg
				class="w-6 h-6"
				fill="none"
				stroke="currentColor"
				viewBox="0 0 24 24"
				xmlns="http://www.w3.org/2000/svg"
			>
				<path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
				/>
			</svg>
		</button>
	</div>
	<div>
		<h3 class="text-lg font-semibold">CMA Clash Newsletter</h3>
		<input type="hidden" name="nonce" />
		<p>
			<label class="block text-sm font-medium text-gray-800 dark:text-gray-200" for="newsletter-email"
				>E-mail</label
			>
			<input
				id="newsletter-email"
				type="email"
				name="email"
				required
				autocomplete="email"
				class="m-0.5 w-full border-b-2 border-gray-600 rounded-lg p-0.5 outline-hidden focus:outline-gray-400 bg-transparent"
			/>
		</p>
		<p>
			<label class="block text-sm font-medium text-gray-800 dark:text-gray-200" for="newsletter-name"
				>Name (optional)</label
			>
			<input
				id="newsletter-name"
				type="text"
				name="name"
				autocomplete="name"
				class="m-0.5 w-full border-b-2 border-gray-600 rounded-lg p-0.5 outline-hidden focus:outline-gray-400 bg-transparent"
			/>
		</p>

		<p class="hidden">
			<input
				id="fec55"
				type="checkbox"
				name="l"
				checked
				value="fec5595e-9af1-497a-b7eb-1edd7ad2e21c"
			/>
			<label for="fec55">CMA Clash News</label>
		</p>
		<div class="bg-gradient-to-r from-[#009444] via-[#39b54a] to-[#8dc63f] w-fit rounded-lg">
			<button type="submit" class="m-0.5 bg-white/7 rounded-lg py-0.5 px-1 text-black"
				>Subscribe!
			</button>
		</div>
	</div>
</form>
