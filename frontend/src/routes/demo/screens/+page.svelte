<!-- UI preview for documentation screenshots (static composition). -->
<script lang="ts">
	import { navbarVisible } from '$lib/stores.svelte';
	import LivePlayHeader from '$lib/ui/LivePlayHeader.svelte';
	import Card from '$lib/ui/Card.svelte';
	import TimerBar from '$lib/ui/TimerBar.svelte';
	import TopicTag from '$lib/ui/TopicTag.svelte';
	import AnswerShapeIcon from '$lib/ui/AnswerShapeIcon.svelte';
	import { LEDGER_ANSWER_COLORS, LEDGER_ANSWER_SHAPES } from '$lib/ui/tokens';
	import LedgerTable from '$lib/ui/LedgerTable.svelte';
	import Podium from '$lib/ui/Podium.svelte';
	import PinDisplay from '$lib/ui/PinDisplay.svelte';
	import CountdownRing from '$lib/ui/CountdownRing.svelte';
	import PlayerChip from '$lib/ui/PlayerChip.svelte';
	import ExplanationDrawer from '$lib/ui/ExplanationDrawer.svelte';

	navbarVisible.visible = false;

	const answers = ['Left ventricle', 'Right atrium', 'Left atrium', 'Right ventricle'];
</script>

<div class="bg-paper min-h-screen p-8 space-y-16 max-w-4xl mx-auto">
	<section id="host-lobby">
		<h2 class="font-display text-xl mb-4">Host lobby</h2>
		<PinDisplay pin="482913" />
		<div class="flex gap-2 mt-4">
			<PlayerChip name="You" />
			<PlayerChip name="M. Chen" />
		</div>
		<div class="mt-6 flex justify-center opacity-90 pointer-events-none">
			<CountdownRing seconds={5} label="Starting soon" />
		</div>
	</section>

	<section id="live-question">
		<h2 class="font-display text-xl mb-4">Live question</h2>
		<LivePlayHeader pin="482913" rank={3} totalPlayers={28} rankDelta={1} />
		<Card class="mt-4">
			<TopicTag label="CCMA · Anatomy & Physiology · Q4/10" />
			<p class="font-display mt-3 mb-4">
				Which chamber of the heart receives oxygenated blood from the pulmonary veins?
			</p>
			<TimerBar remainingSeconds={11} totalSeconds={30} showRing={true} />
			<div class="grid grid-cols-2 gap-3 mt-6">
				{#each LEDGER_ANSWER_COLORS as color, i}
					<div
						class="rounded-xl p-6 flex flex-col items-center gap-2 text-white"
						style="background:{color}"
					>
						<AnswerShapeIcon shape={LEDGER_ANSWER_SHAPES[i]} class="w-8 h-8" />
						<span class="font-mono text-sm text-center">{answers[i]}</span>
					</div>
				{/each}
			</div>
		</Card>
	</section>

	<section id="results">
		<h2 class="font-display text-xl mb-4">Per-question results</h2>
		<LedgerTable
			flip={true}
			rows={[
				{ rank: 1, name: 'A. Okafor', score: '9,420' },
				{ rank: 3, name: 'You', score: '8,870', isYou: true, delta: 1 }
			]}
		/>
		<div class="mt-4">
			<ExplanationDrawer
				explanation="The left atrium receives oxygenated blood from the pulmonary veins before it passes to the left ventricle."
			/>
		</div>
	</section>

	<section id="podium">
		<h2 class="font-display text-xl mb-4">Podium</h2>
		<Podium
			entries={[
				{ name: 'A. Okafor', score: '9,420' },
				{ name: 'M. Chen', score: '9,105' },
				{ name: 'You', score: '8,870' }
			]}
		/>
	</section>
</div>
