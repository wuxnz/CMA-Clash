<!--
SPDX-FileCopyrightText: 2026 CMA Clash contributors

SPDX-License-Identifier: MPL-2.0
-->

<script lang="ts">
	import RandomizedPracticeTest from '$lib/study/RandomizedPracticeTest.svelte';
	import { PHLEB_TEST_CARDS, PHLEB_TEST_CATEGORIES } from '$lib/study/phlebotomy-test-study';
</script>

<RandomizedPracticeTest
	title="Phlebotomy Test Study Guide"
	cards={PHLEB_TEST_CARDS}
	categories={PHLEB_TEST_CATEGORIES}
	backHref="/study/phlebotomy-test-study"
	backLabel="Study guide"
/>