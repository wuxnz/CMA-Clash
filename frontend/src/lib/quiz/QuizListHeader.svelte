<script lang="ts">
	import {
		quizHeaderColCert,
		quizHeaderColDifficulty,
		quizHeaderColQs,
		quizColCertDot,
		quizTableHeaderRow
	} from './quizTableLayout';
</script>

<div class={quizTableHeaderRow} role="row" data-quiz-header>
	<span data-quiz-col="title" data-quiz-row="header" class="min-w-0">Title</span>
	<span data-quiz-col="cert" data-quiz-row="header" class={quizHeaderColCert}>
		<span class={quizColCertDot} aria-hidden="true"></span>
		<span>Cert</span>
	</span>
	<span data-quiz-col="qs" data-quiz-row="header" class={quizHeaderColQs}>Qs</span>
	<span data-quiz-col="difficulty" data-quiz-row="header" class={quizHeaderColDifficulty}
		>Difficulty</span
	>
	<span data-quiz-col="actions" data-quiz-row="header" class="min-w-0" aria-hidden="true"></span>
</div>
