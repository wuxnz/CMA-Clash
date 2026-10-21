<!-- Arena live-flow screenshots (one phase at a time via ?phase=). -->
<script lang="ts">
	import { page } from '$app/state';
	import { navbarVisible } from '$lib/stores.svelte';
	import QuestionIntro from '$lib/play/arena/QuestionIntro.svelte';
	import AnswerTiles from '$lib/play/arena/AnswerTiles.svelte';
	import RevealPhase from '$lib/play/arena/RevealPhase.svelte';
	import RankingsBoard from '$lib/play/arena/RankingsBoard.svelte';
	import FinalResults from '$lib/play/admin/final_results.svelte';
	import GrayButton from '$lib/components/buttons/gray.svelte';
	import { LEDGER_ANSWER_COLORS } from '$lib/ui/tokens';
	import MasteryHeatmap from '$lib/ui/MasteryHeatmap.svelte';
	import RetentionBar from '$lib/ui/RetentionBar.svelte';

	navbarVisible.visible = false;

	const q = 'Which chamber of the heart receives oxygenated blood from the pulmonary veins?';
	const answers = [
		{ answer: 'Left ventricle', color: LEDGER_ANSWER_COLORS[0] },
		{ answer: 'Right atrium', color: LEDGER_ANSWER_COLORS[1] },
		{ answer: 'Left atrium', color: LEDGER_ANSWER_COLORS[2], right: true },
		{ answer: 'Right ventricle', color: LEDGER_ANSWER_COLORS[3] }
	];
	const dist = [
		{ answer: 'Left ventricle', count: 8 },
		{ answer: 'Right atrium', count: 4 },
		{ answer: 'Left atrium', count: 14, right: true },
		{ answer: 'Right ventricle', count: 2 }
	];
	const ranks = [
		{ rank: 1, name: 'A. Okafor', score: 9420 },
		{ rank: 2, name: 'M. Chen', score: 9105, delta: 1 },
		{ rank: 3, name: 'You', score: 8870, isYou: true, delta: -1 }
	];

	const phase = $derived(page.url.searchParams.get('phase') ?? 'all');
	const show = (id: string) => phase === 'all' || phase === id;

	const podiumScores = {
		'A. Okafor': 9420,
		'M. Chen': 9105,
		'Jordan Lee': 8870,
		'Sam Rivera': 8200,
		'Priya N.': 7905,
		'Chris M.': 7650,
		'Emma T.': 7100,
		'Noah K.': 6800
	};
</script>

<div class="bg-paper">
	{#if show('host-intro')}
		<section id="host-intro" class="h-dvh overflow-hidden">
			<QuestionIntro question={q} topic="CCMA · Anatomy · Q4/10" seconds={4} />
		</section>
	{/if}
	{#if show('host-answer')}
		<section id="host-answer" class="h-dvh overflow-hidden">
			<AnswerTiles
				question={q}
				{answers}
				remainingSeconds={11}
				totalSeconds={30}
				answeredCount={18}
			/>
		</section>
	{/if}
	{#if show('host-reveal')}
		<section id="host-reveal" class="h-dvh overflow-hidden">
			<RevealPhase question={q} distribution={dist} />
		</section>
	{/if}
	{#if show('host-rankings')}
		<section id="host-rankings" class="h-dvh overflow-hidden">
			<RankingsBoard rows={ranks} />
		</section>
	{/if}
	{#if show('host-podium')}
		<section id="host-podium" class="h-dvh max-h-dvh overflow-hidden">
			<FinalResults data={podiumScores} show_final_results={true} hostLayout>
				{#snippet actions()}
					<GrayButton>Export results</GrayButton>
					<GrayButton>Save results</GrayButton>
				{/snippet}
			</FinalResults>
		</section>
	{/if}
	{#if show('player-join')}
		<section id="player-join" class="h-dvh overflow-hidden flex flex-col items-center justify-center">
			<p class="font-display text-gold text-sm tracking-[0.35em] mb-4">Arena</p>
			<h1 class="font-display text-7xl text-ink">Join</h1>
			<p class="font-display text-5xl text-gold tabular-nums tracking-widest mt-6">482913</p>
			<input class="ledger-input text-center max-w-xs mt-6 font-display text-2xl" value="You" readonly />
			<button type="button" class="ledger-btn-primary w-auto px-10 mt-4">Enter</button>
		</section>
	{/if}
	{#if show('player-answer')}
		<section id="player-answer" class="h-dvh overflow-hidden">
			<AnswerTiles
				question={q}
				{answers}
				remainingSeconds={11}
				totalSeconds={30}
				interactive={true}
			/>
		</section>
	{/if}
	{#if show('player-correct')}
		<section id="player-correct" class="h-dvh overflow-hidden">
			<RevealPhase
				question={q}
				distribution={dist}
				isPlayer={true}
				correct={true}
				points={240}
				streak={3}
			/>
		</section>
	{/if}
	{#if show('player-incorrect')}
		<section id="player-incorrect" class="h-dvh overflow-hidden">
			<RevealPhase
				question={q}
				distribution={dist}
				isPlayer={true}
				correct={false}
				points={0}
				streak={0}
			/>
		</section>
	{/if}
	{#if show('practice')}
		<section id="practice" class="h-dvh overflow-hidden">
			<div class="h-full flex flex-col">
				<div class="px-4 pt-6 text-center">
					<h1 class="text-2xl font-semibold text-ink">Practice</h1>
				</div>
				<div class="flex-1 min-h-0">
					<AnswerTiles
						question={q}
						{answers}
						remainingSeconds={18}
						totalSeconds={30}
						interactive={true}
					/>
				</div>
			</div>
		</section>
	{/if}
	{#if show('dashboard')}
		<section id="dashboard" class="min-h-dvh px-4 py-8 max-w-4xl mx-auto">
			<div class="flex flex-wrap items-center justify-between gap-3 mb-6">
				<div>
					<h1 class="text-2xl font-semibold text-ink">Dashboard</h1>
				</div>
				<a href="/battle" class="ledger-btn-primary w-auto px-6">Battle queue</a>
			</div>
			<RetentionBar streakDays={7} dailyGoalPercent={62} leagueName="Volt III" />
			<div class="my-6">
				<MasteryHeatmap
					stats={[
						{
							topic_name: 'Anatomy',
							topic_slug: 'anatomy',
							accuracy_percent: 88,
							questions_answered: 40,
							questions_correct: 35,
							xp_earned: 900
						},
						{
							topic_name: 'Clinical',
							topic_slug: 'clinical',
							accuracy_percent: 71,
							questions_answered: 28,
							questions_correct: 20,
							xp_earned: 620
						},
						{
							topic_name: 'Legal',
							topic_slug: 'legal',
							accuracy_percent: 54,
							questions_answered: 12,
							questions_correct: 6,
							xp_earned: 210
						},
						{
							topic_name: 'Admin',
							topic_slug: 'admin',
							accuracy_percent: 40,
							questions_answered: 10,
							questions_correct: 4,
							xp_earned: 80
						}
					]}
				/>
			</div>
			<p class="font-display text-xl text-ink mb-3">Recent matches</p>
			<ul class="space-y-2">
				<li class="rounded-xl bg-surface px-4 py-3 flex justify-between">
					<span>CCMA Anatomy Clash</span>
					<span class="font-display text-gold">+240 XP</span>
				</li>
				<li class="rounded-xl bg-surface px-4 py-3 flex justify-between">
					<span>1v1 vs M. Chen</span>
					<span class="font-display text-signal">▼ 2</span>
				</li>
			</ul>
		</section>
	{/if}
</div>
