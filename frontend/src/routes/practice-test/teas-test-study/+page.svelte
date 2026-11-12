<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import RandomizedPracticeTest from '$lib/study/RandomizedPracticeTest.svelte';
	import { TEAS_TEST_CARDS, TEAS_TEST_CATEGORIES } from '$lib/study/teas-test-study';
</script>

<RandomizedPracticeTest
	title="TEAS Test Study Guide"
	cards={TEAS_TEST_CARDS}
	categories={TEAS_TEST_CATEGORIES}
	backHref="/study/teas-test-study"
	backLabel="Study guide"
/>
