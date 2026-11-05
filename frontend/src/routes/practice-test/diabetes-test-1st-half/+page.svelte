<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import RandomizedPracticeTest from '$lib/study/RandomizedPracticeTest.svelte';
	import { TEST_1ST_HALF_CARDS, TEST_1ST_HALF_CATEGORIES } from '$lib/study/diabetes-test-1st-half';
</script>

<RandomizedPracticeTest
	title="Diabetes Test 1st Half"
	cards={TEST_1ST_HALF_CARDS}
	categories={TEST_1ST_HALF_CATEGORIES}
	backHref="/study/diabetes-test-1st-half"
	backLabel="Study guide"
/>
