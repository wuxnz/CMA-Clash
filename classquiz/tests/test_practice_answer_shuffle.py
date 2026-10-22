# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Practice mode shuffles ABCD answers client-side (see question.svelte)."""

import pytest

pytestmark = pytest.mark.order("last")


def test_practice_question_component_shuffles_answers():
    path = "frontend/src/lib/practice/question.svelte"
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    assert "shuffleArray(question.answers)" in src
