# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

import asyncio
import os

import pytest

pytestmark = pytest.mark.order("last")

from classquiz.kahoot_importer.search import search


@pytest.mark.skipif(
    os.environ.get("RUN_KAHOOT_TESTS", "").lower() not in ("1", "true", "yes"),
    reason="Set RUN_KAHOOT_TESTS=1 to run live Kahoot search tests",
)
def test_search():
    async def _run():
        res = await search(query="Python", limit=100)
        assert len(res.entities) == 100
        await search(query="Test Quiz", limit=100)
        await search(query="Biologie", limit=100)
        await search(query="Chemie", limit=100)
        await search(query="Deutsch", limit=100)
        await search(query="Mathe", limit=100)
        await search(query="Englisch", limit=100)
        await search(query="Barbie", limit=100)
        await search(query="Internet", limit=100)
        await search(query="Windows", limit=100)
        await search(query="Python", limit=100)

    asyncio.run(_run())
