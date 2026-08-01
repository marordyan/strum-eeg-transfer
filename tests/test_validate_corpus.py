"""Tests for tools/validate_corpus.py.

Each test builds a small fixture corpus under tmp_path and perturbs exactly
one thing away from a known-valid baseline entry.
"""

from __future__ import annotations

import datetime
import hashlib
import json
from pathlib import Path

import validate_corpus as vc

CARD_TEMPLATE = """---
slug: {slug}
type: paper
strand: {strand}
year: 2023
authors: [Smith, Jones]
venue: Some Venue
doi: null
url: null
license: null
modalities: [eeg]
tags: [eeg, transfer]
relevance: medium
imported_from: null
added: 2024-01-01
pdf_status: not-applicable
pdf_path: null
md_path: source.md
md_quality: clean
---

# {slug}

Body text.
"""

META_TEMPLATE = {
    "doi": None,
    "source_url": "https://example.com/paper",
    "retrieved_at": "2024-01-01",
    "pdf_sha256": None,
    "pdf_license": "not-applicable",
    "redistribution_ok": True,
    "notes": "test fixture",
}


def write_entry(
    root: Path,
    strand: str,
    slug: str,
    *,
    card_overrides: dict[str, str] | None = None,
    meta_overrides: dict[str, object] | None = None,
    meta_missing_keys: tuple[str, ...] = (),
    meta_raw: str | None = None,
    skip_files: tuple[str, ...] = (),
    with_pdf: bool = False,
    pdf_bytes: bytes = b"%PDF-1.4 test content\n",
) -> Path:
    """Write one valid entry folder, then apply targeted perturbations.

    `meta_raw`, when given, is written verbatim as meta.json's content
    instead of the JSON-encoded META_TEMPLATE (for testing malformed/
    non-object meta.json bodies). `meta_missing_keys` drops keys from the
    template dict before encoding (for testing missing required keys).
    """
    entry_dir = root / "research" / "collection" / strand / slug
    entry_dir.mkdir(parents=True, exist_ok=True)

    card_text = CARD_TEMPLATE.format(slug=slug, strand=strand)
    if card_overrides:
        lines = card_text.splitlines()
        for i, line in enumerate(lines):
            if ":" in line:
                key = line.split(":", 1)[0].strip()
                if key in card_overrides:
                    lines[i] = f"{key}: {card_overrides[key]}"
        card_text = "\n".join(lines) + "\n"

    if "card.md" not in skip_files:
        (entry_dir / "card.md").write_text(card_text, encoding="utf-8")
    if "source.md" not in skip_files:
        (entry_dir / "source.md").write_text(f"# {slug}\n\nSource text.\n", encoding="utf-8")

    if "meta.json" not in skip_files:
        if meta_raw is not None:
            (entry_dir / "meta.json").write_text(meta_raw, encoding="utf-8")
        else:
            meta = dict(META_TEMPLATE)
            if meta_overrides:
                meta.update(meta_overrides)
            for key in meta_missing_keys:
                meta.pop(key, None)
            (entry_dir / "meta.json").write_text(json.dumps(meta), encoding="utf-8")

    if with_pdf:
        (entry_dir / "source.pdf").write_bytes(pdf_bytes)

    return entry_dir


def write_strand_index(root: Path, strand: str, slugs: list[str]) -> None:
    strand_dir = root / "research" / "collection" / strand
    strand_dir.mkdir(parents=True, exist_ok=True)
    lines = [f"# {strand} Collection Index", "", "## Entries"]
    for slug in slugs:
        lines.append(f"- [{slug}](./{slug}/card.md): test entry")
    (strand_dir / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_strand_bib(root: Path, strand: str, keys: list[str]) -> None:
    """Write a strand .bib whose entry keys are exactly `keys` (verbatim)."""
    strand_dir = root / "research" / "collection" / strand
    strand_dir.mkdir(parents=True, exist_ok=True)
    entries = []
    for key in keys:
        entries.append(f"@article{{{key},\n  title = {{Test paper {key}}},\n}}")
    (strand_dir / f"{strand}.bib").write_text("\n\n".join(entries) + "\n", encoding="utf-8")


def test_valid_entry_no_violations(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _entry_count, high_count = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert violations == []
    assert high_count == 0


def test_missing_source_md(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", skip_files=("source.md",))
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("missing required file source.md" in v for v in violations)


def test_slug_mismatch(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", card_overrides={"slug": "paper-two"})
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("does not match folder name" in v for v in violations)


def test_relevance_out_of_vocabulary(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", card_overrides={"relevance": "extreme"})
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("relevance value 'extreme'" in v for v in violations)


def test_enum_field_with_list_value_is_reported_not_raised(tmp_path: Path) -> None:
    """A list where a scalar enum belongs must be reported, not crash the run.

    Lists are unhashable, so a naive membership test against the allowed set
    would raise TypeError and abort validation of the whole corpus.
    """
    write_entry(tmp_path, "strand-a", "paper-one", card_overrides={"type": "[paper]"})
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("must be a scalar, not a list" in v for v in violations)


def test_redistribution_violation(tmp_path: Path) -> None:
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        meta_overrides={"redistribution_ok": False},
        with_pdf=True,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("redistribution_ok is false but source.pdf exists" in v for v in violations)


def test_entry_missing_from_index(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    write_entry(tmp_path, "strand-a", "paper-two")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])  # paper-two omitted
    write_strand_bib(tmp_path, "strand-a", ["paper-one", "paper-two"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("paper-two" in v and "not linked from INDEX.md" in v for v in violations)


def test_entry_missing_bibtex_key(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", [])  # no matching key for paper-one

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("paper-one" in v and "no BibTeX entry with key 'paper-one'" in v for v in violations)


def test_entry_bibtex_key_must_match_slug_verbatim(tmp_path: Path) -> None:
    """A near-match (e.g. opencite's default 'Xu2019ADT'-style key) must not
    satisfy the check: the key has to equal the slug exactly, not fuzzily."""
    write_entry(tmp_path, "strand-a", "paper-one")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["Paperone2024"])  # close, but not exact

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("paper-one" in v and "no BibTeX entry with key 'paper-one'" in v for v in violations)


def test_duplicate_bibtex_key_is_a_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    write_entry(tmp_path, "strand-a", "paper-two")
    write_strand_index(tmp_path, "strand-a", ["paper-one", "paper-two"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one", "paper-two", "paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("duplicate BibTeX key 'paper-one'" in v for v in violations)


def test_empty_corpus_is_valid(tmp_path: Path) -> None:
    (tmp_path / "research" / "collection").mkdir(parents=True)

    violations, warnings, entry_count, strand_counts = vc.run_validation(tmp_path)
    assert violations == []
    assert warnings == []
    assert entry_count == 0
    assert strand_counts == {}

    exit_code = vc.main(["--root", str(tmp_path)])
    assert exit_code == 0


def test_empty_corpus_missing_collection_dir_is_valid(tmp_path: Path) -> None:
    exit_code = vc.main(["--root", str(tmp_path)])
    assert exit_code == 0


def test_main_exits_1_on_violations(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", skip_files=("source.md",))
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    exit_code = vc.main(["--root", str(tmp_path)])
    assert exit_code == 1


def test_archived_pdf_sha256_mismatch(tmp_path: Path) -> None:
    entry_dir = write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_overrides={"pdf_sha256": "0" * 64, "pdf_license": "CC-BY-4.0"},
        with_pdf=True,
    )
    assert entry_dir.name == "paper-one"
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("pdf_sha256 mismatch" in v for v in violations)


def test_source_pdf_must_have_a_pdf_header(tmp_path: Path) -> None:
    """An HTML challenge page saved as source.pdf must be caught.

    Several publishers answer automated fetches with an interstitial page
    under HTTP 200, so a naive download writes HTML into a file named
    source.pdf. Its sha256 then matches its own garbage and every other
    check passes.
    """
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        with_pdf=True,
        pdf_bytes=b"<!DOCTYPE html>\n<html><body>Checking your browser</body></html>\n",
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("source.pdf is not a PDF" in v for v in violations)


def test_real_pdf_header_raises_no_header_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", with_pdf=True, pdf_bytes=b"%PDF-1.7\nbody\n")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert not any("is not a PDF" in v for v in violations)


def test_same_identifier_in_two_strands_warns(tmp_path: Path) -> None:
    """Dual-carding is legitimate, but it has to be visible.

    The per-strand duplicate-key check cannot see across strands, so without
    this the same paper carded twice becomes two bibliography entries for one
    identifier at synthesis time, with nothing having flagged it.
    """
    for strand in ("strand-a", "strand-b"):
        write_entry(tmp_path, strand, "paper-one", meta_overrides={"doi": "10.1234/shared"})
        write_strand_index(tmp_path, strand, ["paper-one"])
        write_strand_bib(tmp_path, strand, ["paper-one"])

    violations, warnings, _, _ = vc.run_validation(tmp_path)

    assert violations == []
    assert any(
        "10.1234/shared" in w and "strand-a/paper-one" in w and "strand-b/paper-one" in w
        for w in warnings
    )


def test_arxiv_doi_and_abs_url_collapse_to_one_identifier(tmp_path: Path) -> None:
    """A DOI-registered arXiv paper and a bare abs link to the same preprint
    are one work, so the duplicate check must pair them."""
    write_entry(
        tmp_path, "strand-a", "paper-one", meta_overrides={"doi": "10.48550/arXiv.2510.21585"}
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    write_entry(
        tmp_path,
        "strand-b",
        "paper-two",
        meta_overrides={"doi": None, "source_url": "https://arxiv.org/abs/2510.21585"},
    )
    write_strand_index(tmp_path, "strand-b", ["paper-two"])
    write_strand_bib(tmp_path, "strand-b", ["paper-two"])

    _, warnings, _, _ = vc.run_validation(tmp_path)

    assert any("arxiv:2510.21585" in w for w in warnings)


def test_distinct_identifiers_do_not_warn(tmp_path: Path) -> None:
    for strand, doi in (("strand-a", "10.1234/one"), ("strand-b", "10.1234/two")):
        write_entry(tmp_path, strand, "paper-one", meta_overrides={"doi": doi})
        write_strand_index(tmp_path, strand, ["paper-one"])
        write_strand_bib(tmp_path, strand, ["paper-one"])

    _, warnings, _, _ = vc.run_validation(tmp_path)

    assert not any("carded in" in w for w in warnings)


def test_relevance_high_share_warning(tmp_path: Path) -> None:
    slugs = [f"paper-{i}" for i in range(6)]
    for i, slug in enumerate(slugs):
        relevance = "high" if i < 5 else "low"
        write_entry(tmp_path, "strand-a", slug, card_overrides={"relevance": relevance})
    write_strand_index(tmp_path, "strand-a", slugs)
    write_strand_bib(tmp_path, "strand-a", slugs)

    violations, warnings, entry_count, _strand_counts = vc.run_validation(tmp_path)

    assert violations == []
    assert entry_count == 6
    assert any("relevance=high share" in w for w in warnings)


# -- Finding 1: meta.json literal null bypassing the "must be an object" check --


def test_meta_json_null_is_a_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", meta_raw="null")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("meta.json top-level value must be an object" in v for v in violations)


def test_meta_json_null_with_committed_pdf_also_violates_license_invariant(
    tmp_path: Path,
) -> None:
    """This is the exact bypass the reviewer demonstrated: a null meta.json
    (with the entry's `pdf_status` left at its non-archived template
    default) alongside a committed source.pdf used to produce zero
    violations, because `meta is not None` was False for a parsed `null`
    and the symmetric storage rule didn't exist yet. Both the "must be an
    object" check and the storage rule now catch it independently."""
    write_entry(tmp_path, "strand-a", "paper-one", meta_raw="null", with_pdf=True)
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("meta.json top-level value must be an object" in v for v in violations)
    assert any("pdf_status is 'not-applicable' but source.pdf exists" in v for v in violations)


def test_meta_json_array_is_a_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", meta_raw="[]")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("meta.json top-level value must be an object" in v for v in violations)


def test_meta_json_invalid_json_is_a_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", meta_raw="{not valid json")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("meta.json is not valid JSON" in v for v in violations)


def test_meta_json_missing_required_key_is_a_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", meta_missing_keys=("doi",))
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("meta.json missing required key 'doi'" in v for v in violations)


def test_non_boolean_redistribution_ok_is_a_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", meta_overrides={"redistribution_ok": "yes"})
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("redistribution_ok must be a boolean" in v for v in violations)


# -- Finding 2: the license invariant now validates pdf_license itself --


def test_paywall_license_with_redistribution_ok_true_is_a_violation(tmp_path: Path) -> None:
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        meta_overrides={"pdf_license": "publisher-paywall", "redistribution_ok": True},
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("implies redistribution_ok must be false" in v for v in violations)


def test_paywall_license_with_qualifier_and_redistribution_ok_false_is_accepted(
    tmp_path: Path,
) -> None:
    """Guards against over-strict matching: the schema explicitly permits a
    trailing parenthetical/semicolon qualifier on pdf_license, and only the
    leading token should be checked against the vocabulary / cross-check."""
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        meta_overrides={
            "pdf_license": "publisher-paywall (NeuroImage); university repository copy archived",
            "redistribution_ok": False,
        },
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert violations == []


def test_out_of_vocabulary_pdf_license_is_a_violation(tmp_path: Path) -> None:
    write_entry(
        tmp_path, "strand-a", "paper-one", meta_overrides={"pdf_license": "made-up-license"}
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("has leading token 'made-up-license' not in" in v for v in violations)


def test_not_redistributable_with_committed_pdf_is_a_violation(tmp_path: Path) -> None:
    """Closes the case the reviewer demonstrated: pdf_status:
    not-redistributable sitting next to a committed PDF, even with
    redistribution_ok: true in meta.json, must be flagged."""
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "not-redistributable"},
        with_pdf=True,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("pdf_status is 'not-redistributable' but source.pdf exists" in v for v in violations)


def test_archived_happy_path_has_no_violations(tmp_path: Path) -> None:
    """There was previously no positive test for the archived path at all."""
    pdf_bytes = b"%PDF-1.4 archived happy path\n"
    sha256 = hashlib.sha256(pdf_bytes).hexdigest()
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_overrides={"pdf_sha256": sha256, "pdf_license": "CC-BY-4.0"},
        with_pdf=True,
        pdf_bytes=pdf_bytes,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert violations == []


# -- Parser behavior under PyYAML --


def test_nested_mapping_keys_are_not_promoted_to_top_level(tmp_path: Path) -> None:
    """Finding 3: the hand-rolled parser ignored indentation and promoted
    any `key: value` line to the top level, regardless of nesting. A real
    YAML parser must instead leave a nested key (here, pdf_status under an
    `archival:` mapping) absent from the top-level fields dict."""
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Some Venue\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "archival:\n"
        "  pdf_status: archived\n"
        "  pdf_path: source.pdf\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "---\n"
    )

    fields, errors = vc.parse_frontmatter(text)

    assert errors == []
    assert fields is not None
    assert fields.get("pdf_status") is None
    assert fields["archival"]["pdf_status"] == "archived"


def test_venue_hash_without_preceding_whitespace_is_literal(tmp_path: Path) -> None:
    """Finding 4, verified against real PyYAML behavior rather than assumed:
    a '#' preceded by whitespace *does* start a YAML comment (confirmed:
    `venue: Workshop #3 on EEG` parses to just `Workshop`), but a '#' with
    no preceding whitespace is literal and round-trips intact."""
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Workshop#3 on EEG\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "pdf_status: not-applicable\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "---\n"
    )

    fields, errors = vc.parse_frontmatter(text)

    assert errors == []
    assert fields is not None
    assert fields["venue"] == "Workshop#3 on EEG"


def test_empty_authors_list_is_a_missing_required_key_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one", card_overrides={"authors": "[]"})
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("frontmatter missing required key 'authors'" in v for v in violations)


def test_duplicate_relevance_key_is_a_violation(tmp_path: Path) -> None:
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Some Venue\n"
        "relevance: high\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "pdf_status: not-applicable\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "---\n"
    )

    fields, errors = vc.parse_frontmatter(text)

    assert fields is None
    assert any("duplicate" in e for e in errors)


def test_malformed_yaml_is_a_violation_not_a_raise(tmp_path: Path) -> None:
    text = "---\n\tbadly: indented\n---\n"

    fields, errors = vc.parse_frontmatter(text)

    assert fields is None
    assert len(errors) == 1


def test_year_int_and_added_date_still_validate(tmp_path: Path) -> None:
    text = CARD_TEMPLATE.format(slug="paper-one", strand="strand-a")

    fields, errors = vc.parse_frontmatter(text)

    assert errors == []
    assert fields is not None
    assert isinstance(fields["year"], int)
    assert isinstance(fields["added"], datetime.date)

    write_entry(tmp_path, "strand-a", "paper-one")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert not any(
        "is not a 4-digit year" in v or "is not a YYYY-MM-DD date" in v for v in violations
    )


# -- Robustness and structure --


def test_latin1_card_is_a_violation_not_a_raise(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    entry_dir = tmp_path / "research" / "collection" / "strand-a" / "paper-one"
    (entry_dir / "card.md").write_bytes("café résumé".encode("latin-1"))
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("card.md" in v and "could not be read as UTF-8" in v for v in violations)


def test_card_at_strand_depth_is_a_violation(tmp_path: Path) -> None:
    strand_dir = tmp_path / "research" / "collection" / "eeg-models"
    strand_dir.mkdir(parents=True)
    (strand_dir / "card.md").write_text(
        CARD_TEMPLATE.format(slug="paper-one", strand="eeg-models"), encoding="utf-8"
    )

    violations, _warnings, _entry_count, _strand_counts = vc.run_validation(tmp_path)

    assert any("card.md found at strand depth" in v for v in violations)


def test_unexpected_strand_directory_is_a_warning_not_a_violation(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, warnings, _entry_count, strand_counts = vc.run_validation(tmp_path)

    assert violations == []
    assert any("unexpected strand directory 'strand-a'" in w for w in warnings)
    assert strand_counts == {"strand-a": 1}


def test_expected_strand_validates_normally_without_warning(tmp_path: Path) -> None:
    write_entry(tmp_path, "eeg-models", "paper-one")
    write_strand_index(tmp_path, "eeg-models", ["paper-one"])
    write_strand_bib(tmp_path, "eeg-models", ["paper-one"])

    violations, warnings, entry_count, strand_counts = vc.run_validation(tmp_path)

    assert violations == []
    assert not any("unexpected strand directory" in w for w in warnings)
    assert entry_count == 1
    assert strand_counts == {"eeg-models": 1}


# -- Second-round fixes: _UniqueKeyLoader unhashable-key TypeError, the
# unguarded source.pdf read, hand-split frontmatter truncation, the
# residual license hole, dead prefix logic, and dict emptiness / a
# misleading cascade --


def test_unhashable_yaml_key_is_reported_not_raised(tmp_path: Path) -> None:
    """Fix 1: `construct_mapping` did `if key in seen` before delegating to
    PyYAML, so an unhashable key (e.g. `? [a, b]`) raised a bare TypeError
    that escaped parse_frontmatter uncaught, aborting the entire run. With
    the membership test guarded, super().construct_mapping is left to
    raise PyYAML's own catchable ConstructorError instead."""
    entry_dir = write_entry(tmp_path, "strand-a", "paper-one")
    (entry_dir / "card.md").write_text(
        "---\n? [a, b]\n: v\n---\n\n# paper-one\n\nBody text.\n", encoding="utf-8"
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("paper-one" in v and "not valid YAML" in v for v in violations)


def test_deeply_nested_flow_yaml_is_reported_not_raised(tmp_path: Path) -> None:
    """Fix 1: deeply nested flow YAML can exceed PyYAML's recursion limit
    (RecursionError), a failure mode inherited from PyYAML rather than
    introduced here. parse_frontmatter must still catch it and report a
    violation rather than let it propagate."""
    nested = "k: " + "[" * 20000
    text = f"---\n{nested}\n---\n"

    fields, errors = vc.parse_frontmatter(text)

    assert fields is None
    assert len(errors) == 1
    assert "not valid YAML" in errors[0]


def test_unreadable_archived_pdf_is_reported_not_raised(tmp_path: Path) -> None:
    """Fix 2: hashlib.sha256(pdf_path.read_bytes()) in the archived-PDF
    branch was not routed through a safe reader. A source.pdf with mode 000
    used to abort the run with PermissionError."""
    pdf_bytes = b"%PDF-1.4 unreadable test\n"
    entry_dir = write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_overrides={
            "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
            "pdf_license": "CC-BY-4.0",
        },
        with_pdf=True,
        pdf_bytes=pdf_bytes,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    pdf_path = entry_dir / "source.pdf"
    pdf_path.chmod(0o000)
    try:
        violations, _, _ = vc.validate_strand(
            tmp_path / "research" / "collection" / "strand-a", tmp_path
        )
    finally:
        pdf_path.chmod(0o644)

    assert any("source.pdf" in v and "could not be read" in v for v in violations)


def test_block_scalar_with_indented_delimiter_no_longer_runs_clean(tmp_path: Path) -> None:
    """Fix 3: the old hand-split extraction stopped at the first line whose
    strip() was '---', which truncated the frontmatter block when a '---'
    appeared indented inside a block scalar (here, `notes: |`). That
    silently dropped `pdf_path: source.pdf` before the
    pdf_status-versus-pdf_path check could see it, producing a clean run
    with zero violations. Parsing via yaml.load_all on the full text lets
    YAML's own document-boundary rule find the real end of frontmatter, so
    pdf_path survives and the violation fires."""
    entry_dir = write_entry(tmp_path, "strand-a", "paper-one")
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Some Venue\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "pdf_status: not-redistributable\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "notes: |\n"
        "  Retrieval notes\n"
        "  ---\n"
        "  continued\n"
        "pdf_path: source.pdf\n"
        "---\n"
        "\n# paper-one\n\nBody text.\n"
    )
    (entry_dir / "card.md").write_text(text, encoding="utf-8")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any(
        "pdf_status is not 'archived' but card.md pdf_path is not null" in v for v in violations
    )


def test_notes_block_scalar_with_indented_delimiter_keeps_later_keys(tmp_path: Path) -> None:
    """Fix 3 positive case: a '---' indented inside a block scalar must not
    be mistaken for the closing delimiter, and every key after it must
    still parse."""
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Some Venue\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "pdf_status: not-applicable\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "notes: |\n"
        "  Retrieval notes\n"
        "  ---\n"
        "  continued\n"
        "pdf_path: null\n"
        "---\n"
        "\n# paper-one\n\nBody text.\n"
    )

    fields, errors = vc.parse_frontmatter(text)

    assert errors == []
    assert fields is not None
    assert fields["notes"] == "Retrieval notes\n---\ncontinued\n"
    assert fields["pdf_path"] is None
    assert fields["md_quality"] == "clean"


def test_archived_not_applicable_license_with_committed_pdf_is_a_violation(
    tmp_path: Path,
) -> None:
    """Fix 4: pdf_license: not-applicable ('no paper exists' per the
    schema) sitting next to a committed, correctly-hashed source.pdf must
    be caught. The old rule only excluded publisher-paywall/unknown, so
    everything else - including not-applicable - was implicitly treated as
    redistributable."""
    pdf_bytes = b"%PDF-1.4 not-applicable license test\n"
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_overrides={
            "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
            "pdf_license": "not-applicable",
        },
        with_pdf=True,
        pdf_bytes=pdf_bytes,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("requires a redistributable license" in v for v in violations)


def test_archived_not_applicable_qualifier_license_with_committed_pdf_is_a_violation(
    tmp_path: Path,
) -> None:
    """Fix 4: the qualifier form must not dodge the redistributable check
    either - only the leading token before '(' or ';' is checked, and here
    that leading token is still 'not-applicable'."""
    pdf_bytes = b"%PDF-1.4 qualifier license test\n"
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_overrides={
            "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
            "pdf_license": "not-applicable (really publisher-paywall)",
        },
        with_pdf=True,
        pdf_bytes=pdf_bytes,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("requires a redistributable license" in v for v in violations)


def test_archived_cc_by_license_with_committed_pdf_is_clean(tmp_path: Path) -> None:
    """Fix 4 positive case: a license that IS in REDISTRIBUTABLE_LICENSES,
    next to a committed PDF with a matching sha256, must not trip the new
    check."""
    pdf_bytes = b"%PDF-1.4 redistributable license test\n"
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_overrides={
            "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
            "pdf_license": "CC-BY-4.0",
        },
        with_pdf=True,
        pdf_bytes=pdf_bytes,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert violations == []


def test_critical_2_repro_archived_paywall_license_is_a_violation(tmp_path: Path) -> None:
    """The original critical-2 repro, end to end: pdf_status archived,
    pdf_license publisher-paywall, redistribution_ok true, a committed PDF
    with a matching sha256. Every storage/hash invariant is internally
    consistent; only the license-implies-redistribution_ok cross-check
    should fire."""
    pdf_bytes = b"%PDF-1.4 critical-2 repro\n"
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_overrides={
            "pdf_sha256": hashlib.sha256(pdf_bytes).hexdigest(),
            "pdf_license": "publisher-paywall",
            "redistribution_ok": True,
        },
        with_pdf=True,
        pdf_bytes=pdf_bytes,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("implies redistribution_ok must be false" in v for v in violations)


def test_empty_authors_dict_is_a_missing_required_key_violation(tmp_path: Path) -> None:
    """Fix 6: the required-key emptiness test covered str and list, but not
    dict, so `authors: {}` passed."""
    write_entry(tmp_path, "strand-a", "paper-one", card_overrides={"authors": "{}"})
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("frontmatter missing required key 'authors'" in v for v in violations)


def test_archived_with_unparseable_meta_json_does_not_also_emit_pdf_sha256_message(
    tmp_path: Path,
) -> None:
    """Fix 6: for an archived entry whose meta.json could not be parsed at
    all, the run used to emit the real diagnosis plus a spurious
    "pdf_status is 'archived' but meta.json pdf_sha256 is null/missing".
    The second message must be suppressed when meta is the _UNSET
    sentinel, so the report names one cause rather than two."""
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "archived", "pdf_path": "source.pdf"},
        meta_raw="{not valid json",
        with_pdf=True,
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("meta.json is not valid JSON" in v for v in violations)
    assert not any("pdf_sha256 is null/missing" in v for v in violations)


def test_duplicate_key_at_nesting_depth_two_is_rejected(tmp_path: Path) -> None:
    """Locks currently-working behavior: _UniqueKeyLoader.construct_mapping
    is invoked by PyYAML for every nested mapping node, not just the top
    level, so a duplicate two levels down is already caught."""
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Some Venue\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "pdf_status: not-applicable\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "archival:\n"
        "  tier: cold\n"
        "  tier: hot\n"
        "---\n"
    )

    fields, errors = vc.parse_frontmatter(text)

    assert fields is None
    assert any("duplicate" in e for e in errors)


def test_duplicate_key_at_nesting_depth_three_is_rejected(tmp_path: Path) -> None:
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Some Venue\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "pdf_status: not-applicable\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "archival:\n"
        "  storage:\n"
        "    tier: cold\n"
        "    tier: hot\n"
        "---\n"
    )

    fields, errors = vc.parse_frontmatter(text)

    assert fields is None
    assert any("duplicate" in e for e in errors)


def test_duplicate_key_inside_list_of_mappings_is_rejected(tmp_path: Path) -> None:
    text = (
        "---\n"
        "slug: paper-one\n"
        "type: paper\n"
        "strand: strand-a\n"
        "year: 2023\n"
        "authors: [Smith]\n"
        "venue: Some Venue\n"
        "relevance: medium\n"
        "added: 2024-01-01\n"
        "pdf_status: not-applicable\n"
        "md_path: source.md\n"
        "md_quality: clean\n"
        "reviewers:\n"
        "  - name: A\n"
        "    name: B\n"
        "---\n"
    )

    fields, errors = vc.parse_frontmatter(text)

    assert fields is None
    assert any("duplicate" in e for e in errors)


def test_latin1_meta_json_is_a_violation_not_a_raise(tmp_path: Path) -> None:
    """`_read_text_safe` failures were only tested for card.md; meta.json
    goes through the same helper and must be covered too."""
    write_entry(tmp_path, "strand-a", "paper-one")
    entry_dir = tmp_path / "research" / "collection" / "strand-a" / "paper-one"
    (entry_dir / "meta.json").write_bytes("café résumé".encode("latin-1"))
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any("meta.json" in v and "could not be read as UTF-8" in v for v in violations)


def test_latin1_index_md_is_a_violation_not_a_raise(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])
    strand_dir = tmp_path / "research" / "collection" / "strand-a"
    (strand_dir / "INDEX.md").write_bytes("café résumé".encode("latin-1"))

    violations, _, _ = vc.validate_strand(strand_dir, tmp_path)

    assert any("INDEX.md" in v and "could not be read as UTF-8" in v for v in violations)


def test_latin1_strand_bib_is_a_violation_not_a_raise(tmp_path: Path) -> None:
    write_entry(tmp_path, "strand-a", "paper-one")
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    strand_dir = tmp_path / "research" / "collection" / "strand-a"
    (strand_dir / "strand-a.bib").write_bytes("café résumé".encode("latin-1"))

    violations, _, _ = vc.validate_strand(strand_dir, tmp_path)

    assert any("strand-a.bib" in v and "could not be read as UTF-8" in v for v in violations)


def test_non_archived_pdf_status_with_non_null_pdf_path_is_a_violation(tmp_path: Path) -> None:
    """No test previously covered this directly (Fix 3's block-scalar test
    exercises the same message, but only as a side effect of the
    truncation bug)."""
    write_entry(
        tmp_path,
        "strand-a",
        "paper-one",
        card_overrides={"pdf_status": "not-redistributable", "pdf_path": "source.pdf"},
    )
    write_strand_index(tmp_path, "strand-a", ["paper-one"])
    write_strand_bib(tmp_path, "strand-a", ["paper-one"])

    violations, _, _ = vc.validate_strand(
        tmp_path / "research" / "collection" / "strand-a", tmp_path
    )

    assert any(
        "pdf_status is not 'archived' but card.md pdf_path is not null" in v for v in violations
    )
