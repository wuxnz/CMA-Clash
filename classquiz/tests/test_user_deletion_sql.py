# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

from classquiz.services.user_deletion import _BATTLE_RESULTS_BY_PLAYER_SQL


def test_battle_results_sql_avoids_jsonb_question_mark_operator():
    sql = str(_BATTLE_RESULTS_BY_PLAYER_SQL)
    assert "jsonb_exists" in sql
    assert " ? " not in sql
