# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

import inspect

from classquiz.services import user_deletion as ud


def test_battle_cleanup_does_not_use_jsonb_exists_bulk_sql():
    """Bulk jsonb_exists DELETE was removed: keys are usernames and bad JSON types abort transactions."""
    source = inspect.getsource(ud._delete_battle_results_for_user)
    assert "database.execute" not in source
    assert "DELETE FROM battle_results WHERE" not in source
