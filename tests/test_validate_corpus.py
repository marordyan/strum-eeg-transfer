"""Tests for tools/validate_corpus.py.

Each test builds a small fixture corpus under tmp_path and perturbs exactly
one thing away from a known-valid baseline entry.
"""

from __future__ import annotations

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
    skip_files: tuple[str, ...] = (),
    with_pdf: bool = False,
    pdf_bytes: bytes = b"%PDF-1.4 test content\n",
) -> Path:
    """Write one valid entry folder, then apply targeted perturbations."""
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

    meta = dict(META_TEMPLATE)
    if meta_overrides:
        meta.update(meta_overrides)
    if "meta.json" not in skip_files:
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

    violations, warnings, entry_count = vc.run_validation(tmp_path)
    assert violations == []
    assert warnings == []
    assert entry_count == 0

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


def test_relevance_high_share_warning(tmp_path: Path) -> None:
    slugs = [f"paper-{i}" for i in range(6)]
    for i, slug in enumerate(slugs):
        relevance = "high" if i < 5 else "low"
        write_entry(tmp_path, "strand-a", slug, card_overrides={"relevance": relevance})
    write_strand_index(tmp_path, "strand-a", slugs)
    write_strand_bib(tmp_path, "strand-a", slugs)

    violations, warnings, entry_count = vc.run_validation(tmp_path)

    assert violations == []
    assert entry_count == 6
    assert any("relevance=high share" in w for w in warnings)
