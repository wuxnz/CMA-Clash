<!--
SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import { github_auth_enabled, google_auth_enabled, custom_oauth_name } from '$lib/config';
</script>

{#if google_auth_enabled || github_auth_enabled || custom_oauth_name}
	<div class="mt-6 flex flex-col gap-2">
		{#if google_auth_enabled}
			<a href="/api/v1/users/oauth/google/login" class="btn btn-secondary w-full">
				Continue with Google
			</a>
		{/if}
		{#if github_auth_enabled}
			<a href="/api/v1/users/oauth/github/login" class="btn btn-secondary w-full">
				Continue with GitHub
			</a>
		{/if}
		{#if custom_oauth_name}
			<a href="/api/v1/users/oauth/custom/login" class="btn btn-secondary w-full">
				Continue with {custom_oauth_name}
			</a>
		{/if}
	</div>
{/if}
