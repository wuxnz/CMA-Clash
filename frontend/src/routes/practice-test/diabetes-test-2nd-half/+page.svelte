<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import RandomizedPracticeTest from '$lib/study/RandomizedPracticeTest.svelte';
	import { TEST_2ND_HALF_CARDS, TEST_2ND_HALF_CATEGORIES } from '$lib/study/diabetes-test-2nd-half';
</script>

<RandomizedPracticeTest
	title="Diabetes Test 2nd Half"
	cards={TEST_2ND_HALF_CARDS}
	categories={TEST_2ND_HALF_CATEGORIES}
	backHref="/study/diabetes-test-2nd-half"
	backLabel="Study guide"
/>
