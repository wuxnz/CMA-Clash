<script lang="ts">
	import {
		quizColCert,
		quizColCertDot,
		quizColDifficulty,
		quizColQs,
		quizTableGrid,
		quizTableHeaderShell
	} from './quizTableLayout';
</script>

<div class="{quizTableGrid} {quizTableHeaderShell}">
	<span class="min-w-0">Title</span>
	<span class={quizColCert}>
		<span class="{quizColCertDot}" aria-hidden="true"></span>
		<span>Cert</span>
	</span>
	<span class={quizColQs}>Qs</span>
	<span class={quizColDifficulty}>Difficulty</span>
	<span class="text-right min-w-0" aria-hidden="true"> </span>
</div>
