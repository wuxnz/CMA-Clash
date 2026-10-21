// SPDX-FileCopyrightText: 2026 CMA Clash contributors
//
// SPDX-License-Identifier: MPL-2.0

function ordinalPlace(n: number): string {
	if (n === 1) return '1st';
	if (n === 2) return '2nd';
	if (n === 3) return '3rd';
	return `${n}th`;
}

export type PlayerStandingsFields = {
	overall_rank?: number | null;
	points_behind_above?: number | null;
	player_above?: string | null;
	points_ahead_of_next?: number | null;
	speed_rank?: number | null;
	base_score?: number | null;
	speed_bonus?: number | null;
	right?: boolean | string | number | null;
};

export function placeLine(row: PlayerStandingsFields | undefined | null): string | null {
	const rank = row?.overall_rank;
	if (rank == null || !Number.isFinite(Number(rank))) return null;
	return `You're in ${ordinalPlace(Number(rank))} place`;
}

export function behindOrLeadLine(row: PlayerStandingsFields | undefined | null): string | null {
	const rank = row?.overall_rank;
	if (rank == null) return null;
	const r = Number(rank);
	if (r === 1) {
		const ahead = row?.points_ahead_of_next;
		if (ahead != null && Number(ahead) > 0) {
			return `${Number(ahead)} points ahead of 2nd place`;
		}
		return null;
	}
	const behind = row?.points_behind_above;
	const above = row?.player_above;
	if (behind != null && above) {
		return `${Number(behind)} points behind ${above}`;
	}
	return null;
}

function isCorrect(row: PlayerStandingsFields | undefined | null): boolean {
	const r = row?.right;
	return r === true || r === 'true' || r === 1;
}

export function speedRankLine(row: PlayerStandingsFields | undefined | null): string | null {
	if (!isCorrect(row)) {
		return null;
	}
	const sr = row?.speed_rank;
	if (sr == null || !Number.isFinite(Number(sr))) return null;
	return `You answered ${ordinalPlace(Number(sr))} fastest`;
}
