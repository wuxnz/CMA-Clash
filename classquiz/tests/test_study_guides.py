# SPDX-FileCopyrightText: 2026 CMA Clash contributors
#
# SPDX-License-Identifier: MPL-2.0

"""Quality and coverage checks for the seeded study guides."""

from __future__ import annotations

from urllib.parse import urlparse

from classquiz.seed.catalog import CERTIFICATIONS
from classquiz.seed.sources import OFFICIAL_SOURCE_DOMAINS
from classquiz.seed.study_guides import STUDY_BY_TOPIC

MIN_BLOCKS_PER_TOPIC = 4
MIN_SUMMARY_CHARS = 80
MAX_SUMMARY_CHARS = 1200
MIN_BULLETS = 2
MAX_BULLET_CHARS = 240

ALL_TOPIC_SLUGS = [slug for cert in CERTIFICATIONS for slug, _name, _order in cert["topics"]]


def _host(url: str) -> str:
    host = (urlparse(url).hostname or "").lower()
    return host[4:] if host.startswith("www.") else host


def _is_official(url: str) -> bool:
    host = _host(url)
    return any(host == domain or host.endswith(f".{domain}") for domain in OFFICIAL_SOURCE_DOMAINS)


def test_every_catalog_topic_has_a_study_guide():
    missing = [slug for slug in ALL_TOPIC_SLUGS if slug not in STUDY_BY_TOPIC]
    assert not missing, f"topics without study content: {missing}"


def test_no_orphaned_study_guides():
    orphaned = [slug for slug in STUDY_BY_TOPIC if slug not in ALL_TOPIC_SLUGS]
    assert not orphaned, f"study guides for unknown topics: {orphaned}"


def test_each_topic_has_enough_sections():
    for slug, blocks in STUDY_BY_TOPIC.items():
        assert len(blocks) >= MIN_BLOCKS_PER_TOPIC, f"{slug} has only {len(blocks)} sections"


def test_block_shape():
    for slug, blocks in STUDY_BY_TOPIC.items():
        for block in blocks:
            assert set(block) <= {"title", "summary", "url", "source", "bullets"}, slug
            assert block["title"].strip(), slug
            assert block["summary"].strip(), slug
            assert block["source"].strip(), slug
            assert block["url"].startswith("https://"), (slug, block["url"])


def test_summaries_are_substantive():
    for slug, blocks in STUDY_BY_TOPIC.items():
        for block in blocks:
            summary = block["summary"]
            assert MIN_SUMMARY_CHARS <= len(summary) <= MAX_SUMMARY_CHARS, (
                slug,
                block["title"],
                len(summary),
            )


def test_titles_are_unique_per_topic():
    for slug, blocks in STUDY_BY_TOPIC.items():
        titles = [block["title"] for block in blocks]
        assert len(titles) == len(set(titles)), f"{slug} has duplicate section titles"


def test_urls_point_at_official_sources():
    for slug, blocks in STUDY_BY_TOPIC.items():
        for block in blocks:
            assert _is_official(block["url"]), (slug, block["url"])


def test_bullets_are_present_and_readable():
    for slug, blocks in STUDY_BY_TOPIC.items():
        with_bullets = [block for block in blocks if block.get("bullets")]
        assert len(with_bullets) >= MIN_BLOCKS_PER_TOPIC, f"{slug} has too few sections with key points"
        for block in with_bullets:
            bullets = block["bullets"]
            assert len(bullets) >= 2, (slug, block["title"])
            for bullet in bullets:
                assert bullet.strip(), (slug, block["title"])
                assert len(bullet) <= MAX_BULLET_CHARS, (slug, block["title"], len(bullet))


def test_source_label_matches_the_linked_host():
    label_hints = {
        "cdc.gov": "CDC",
        "osha.gov": "OSHA",
        "fda.gov": "FDA",
        "accessdata.fda.gov": "FDA",
        "hhs.gov": "HHS",
        "ecfr.gov": "eCFR",
        "medlineplus.gov": "MedlinePlus",
        "nhanow.com": "NHA",
        "clsi.org": "CLSI",
        "who.int": "WHO",
        "iris.who.int": "WHO",
        "cpr.heart.org": "American Heart Association",
        "redcross.org": "American Red Cross",
        "ahrq.gov": "AHRQ",
    }
    for slug, blocks in STUDY_BY_TOPIC.items():
        for block in blocks:
            host = _host(block["url"])
            for domain, hint in label_hints.items():
                if host == domain or host.endswith(f".{domain}"):
                    assert hint.lower() in block["source"].lower(), (slug, block["source"], host)
                    break


def test_study_guides_use_distinct_sources_per_topic():
    """A guide should not point at a single source for every section."""
    for slug, blocks in STUDY_BY_TOPIC.items():
        urls = {block["url"] for block in blocks}
        assert len(urls) >= 2, f"{slug} only links {len(urls)} distinct sources"


def test_study_guide_library_uses_a_broad_set_of_official_sources():
    hosts = {_host(block["url"]) for blocks in STUDY_BY_TOPIC.values() for block in blocks}
    assert len(hosts) >= 20, f"study guides only use {len(hosts)} official hosts"
    assert all(_is_official(f"https://{host}/") for host in hosts)
