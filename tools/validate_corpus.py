#!/usr/bin/env python3
"""Validate the lit-review corpus under research/collection/.

Checks each paper-card entry (research/collection/<strand>/<slug>/) for
structural consistency: required files, frontmatter schema, the
redistribution-license invariant, and cross-references into the strand's
INDEX.md and .bib file. See:

  research/collection/_schema/paper-card.md

Standard-library only; no external dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED_ENTRY_FILES = ("card.md", "source.md", "meta.json")

REQUIRED_FRONTMATTER_KEYS = (
    "slug",
    "type",
    "strand",
    "year",
    "authors",
    "venue",
    "relevance",
    "added",
    "pdf_status",
    "md_path",
    "md_quality",
)

TYPE_VALUES = {"paper", "dataset", "tool", "platform", "standard"}
RELEVANCE_VALUES = {"high", "medium", "low"}
PDF_STATUS_VALUES = {"archived", "not-redistributable", "not-available", "not-applicable"}
MD_QUALITY_VALUES = {"clean", "rough", "partial", "abstract-only"}

REQUIRED_META_KEYS = (
    "doi",
    "source_url",
    "retrieved_at",
    "pdf_sha256",
    "pdf_license",
    "redistribution_ok",
    "notes",
)

YEAR_RE = re.compile(r"^\d{4}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BIB_KEY_RE = re.compile(r"@\w+\{\s*([^,\s]+)\s*,")
INDEX_LINK_RE = re.compile(r"\]\(\./([^)]+)\)")

HIGH_RELEVANCE_CEILING = 0.40
HIGH_RELEVANCE_MIN_ENTRIES = 5


def _scalar_or_none(raw: str) -> str | None:
    """Coerce a raw scalar YAML value to a Python str or None."""
    value = raw.strip()
    if value == "" or value.lower() in ("null", "~"):
        return None
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
        value = value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict[str, object] | None, list[str]]:
    """Parse the '---' delimited YAML frontmatter block at the top of card.md.

    Supports scalar `key: value` lines and inline list values of the form
    `key: [a, b, c]`. This is not a general YAML parser; any line that
    cannot be understood is reported as a parse error instead of raising.

    Returns (fields, parse_errors). `fields` is None when there is no
    well-formed frontmatter block to parse at all.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, ["card.md does not start with a '---' frontmatter delimiter"]

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, ["card.md frontmatter block has no closing '---' delimiter"]

    fields: dict[str, object] = {}
    errors: list[str] = []
    for raw_line in lines[1:end_idx]:
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"unparseable frontmatter line: {raw_line!r}")
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if not key:
            errors.append(f"unparseable frontmatter line: {raw_line!r}")
            continue
        if not value.startswith("[") and " #" in value:
            value = value.split(" #", 1)[0].strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            fields[key] = [] if inner == "" else [_scalar_or_none(v) for v in inner.split(",")]
        else:
            fields[key] = _scalar_or_none(value)
    return fields, errors


def _check_enum(
    fields: dict[str, object], key: str, allowed: set[str], violations: list[str]
) -> None:
    value = fields.get(key)
    if value is None:
        return
    # A list value (e.g. `type: [paper]`) is malformed for an enum field, and
    # would raise on the membership test below since lists are unhashable.
    if not isinstance(value, str):
        violations.append(f"{key} value {value!r} must be a scalar, not a list")
        return
    if value not in allowed:
        violations.append(f"{key} value '{value}' is not one of {sorted(allowed)}")


def validate_entry(entry_dir: Path, root: Path) -> list[str]:
    """Validate one entry folder. Returns a list of violation strings.

    Each string already includes the entry's path relative to `root`.
    """
    raw_violations: list[str] = []
    rel = entry_dir.relative_to(root)
    strand_name = entry_dir.parent.name
    slug_name = entry_dir.name

    for filename in REQUIRED_ENTRY_FILES:
        if not (entry_dir / filename).is_file():
            raw_violations.append(f"missing required file {filename}")

    frontmatter: dict[str, object] | None = None
    card_path = entry_dir / "card.md"
    if card_path.is_file():
        frontmatter, parse_errors = parse_frontmatter(card_path.read_text(encoding="utf-8"))
        raw_violations.extend(parse_errors)

    if frontmatter is not None:
        for key in REQUIRED_FRONTMATTER_KEYS:
            if frontmatter.get(key) is None:
                raw_violations.append(f"frontmatter missing required key '{key}'")

        slug_value = frontmatter.get("slug")
        if slug_value is not None and slug_value != slug_name:
            raw_violations.append(
                f"frontmatter slug '{slug_value}' does not match folder name '{slug_name}'"
            )

        strand_value = frontmatter.get("strand")
        if strand_value is not None and strand_value != strand_name:
            raw_violations.append(
                f"frontmatter strand '{strand_value}' does not match parent folder '{strand_name}'"
            )

        _check_enum(frontmatter, "type", TYPE_VALUES, raw_violations)
        _check_enum(frontmatter, "relevance", RELEVANCE_VALUES, raw_violations)
        _check_enum(frontmatter, "pdf_status", PDF_STATUS_VALUES, raw_violations)
        _check_enum(frontmatter, "md_quality", MD_QUALITY_VALUES, raw_violations)

        year = frontmatter.get("year")
        if year is not None and not YEAR_RE.match(str(year)):
            raw_violations.append(f"year '{year}' is not a 4-digit year")

        added = frontmatter.get("added")
        if added is not None and not DATE_RE.match(str(added)):
            raw_violations.append(f"added '{added}' is not a YYYY-MM-DD date")

    meta: object = None
    meta_path = entry_dir / "meta.json"
    if meta_path.is_file():
        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raw_violations.append(f"meta.json is not valid JSON: {exc}")
        if meta is not None and not isinstance(meta, dict):
            raw_violations.append("meta.json top-level value must be an object")
            meta = None

    redistribution_ok: bool | None = None
    if isinstance(meta, dict):
        for key in REQUIRED_META_KEYS:
            if key not in meta:
                raw_violations.append(f"meta.json missing required key '{key}'")
        if "redistribution_ok" in meta:
            value = meta["redistribution_ok"]
            if isinstance(value, bool):
                redistribution_ok = value
            else:
                raw_violations.append("meta.json redistribution_ok must be a boolean")

    pdf_path = entry_dir / "source.pdf"
    pdf_exists = pdf_path.is_file()

    # License invariant: the single source of truth for whether source.pdf
    # is allowed to exist in the repo.
    if redistribution_ok is False and pdf_exists:
        raw_violations.append("redistribution_ok is false but source.pdf exists")

    if frontmatter is not None:
        pdf_status = frontmatter.get("pdf_status")
        if pdf_status == "archived":
            if not pdf_exists:
                raw_violations.append("pdf_status is 'archived' but source.pdf is missing")
            sha256 = meta.get("pdf_sha256") if isinstance(meta, dict) else None
            if not sha256:
                raw_violations.append(
                    "pdf_status is 'archived' but meta.json pdf_sha256 is null/missing"
                )
            elif pdf_exists:
                actual = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
                if actual != sha256:
                    raw_violations.append(
                        f"pdf_sha256 mismatch: meta.json has '{sha256}', actual is '{actual}'"
                    )
        else:
            if frontmatter.get("pdf_path") is not None:
                raw_violations.append(
                    "pdf_status is not 'archived' but card.md pdf_path is not null"
                )

    return [f"{rel}: {message}" for message in raw_violations]


def validate_strand(strand_dir: Path, root: Path) -> tuple[list[str], int, int]:
    """Validate one strand folder.

    Returns (violations, entry_count, high_relevance_count).
    """
    violations: list[str] = []
    strand_name = strand_dir.name
    rel_strand = strand_dir.relative_to(root)

    entry_dirs = sorted(
        p for p in strand_dir.iterdir() if p.is_dir() and not p.name.startswith("_")
    )

    high_count = 0
    entry_slugs: list[str] = []
    for entry_dir in entry_dirs:
        entry_slugs.append(entry_dir.name)
        violations.extend(validate_entry(entry_dir, root))

        card_path = entry_dir / "card.md"
        if card_path.is_file():
            frontmatter, _ = parse_frontmatter(card_path.read_text(encoding="utf-8"))
            if frontmatter is not None and frontmatter.get("relevance") == "high":
                high_count += 1

    # BibTeX keys must match entry slugs verbatim (exact, case-sensitive):
    # opencite emits keys like "Xu2019ADT", and Phase 2 agents are expected
    # to rewrite them to the slug before committing. A fuzzy match would
    # accept opencite's default keys and defeat the point of the check.
    bib_path = strand_dir / f"{strand_name}.bib"
    bib_text = bib_path.read_text(encoding="utf-8") if bib_path.is_file() else ""
    bib_keys = [match.group(1) for match in BIB_KEY_RE.finditer(bib_text)]

    seen_keys: set[str] = set()
    duplicate_keys: set[str] = set()
    for key in bib_keys:
        if key in seen_keys:
            duplicate_keys.add(key)
        seen_keys.add(key)
    for key in sorted(duplicate_keys):
        violations.append(f"{rel_strand}/{strand_name}.bib: duplicate BibTeX key '{key}'")

    bib_key_set = set(bib_keys)
    for slug in entry_slugs:
        if slug not in bib_key_set:
            violations.append(
                f"{rel_strand}/{slug}: no BibTeX entry with key '{slug}' in {strand_name}.bib"
            )

    index_path = strand_dir / "INDEX.md"
    if entry_slugs and not index_path.is_file():
        violations.append(f"{rel_strand}: missing INDEX.md")
    elif index_path.is_file():
        index_text = index_path.read_text(encoding="utf-8")
        linked_first_segments: set[str] = set()
        for link in INDEX_LINK_RE.findall(index_text):
            target = (strand_dir / link).resolve()
            if not target.exists():
                violations.append(
                    f"{rel_strand}/INDEX.md: link './{link}' does not resolve to an existing path"
                )
            linked_first_segments.add(link.split("/", 1)[0])
        for slug in entry_slugs:
            if slug not in linked_first_segments:
                violations.append(f"{rel_strand}: entry '{slug}' is not linked from INDEX.md")

    return violations, len(entry_slugs), high_count


def iter_strands(collection_root: Path) -> list[Path]:
    if not collection_root.is_dir():
        return []
    return sorted(p for p in collection_root.iterdir() if p.is_dir() and not p.name.startswith("_"))


def run_validation(root: Path) -> tuple[list[str], list[str], int]:
    """Validate the whole corpus under root/research/collection/.

    Returns (violations, warnings, total_entry_count).
    """
    collection_root = root / "research" / "collection"
    violations: list[str] = []
    warnings: list[str] = []
    total_entries = 0

    for strand_dir in iter_strands(collection_root):
        strand_violations, entry_count, high_count = validate_strand(strand_dir, root)
        violations.extend(strand_violations)
        total_entries += entry_count

        if entry_count >= HIGH_RELEVANCE_MIN_ENTRIES:
            share = high_count / entry_count
            if share > HIGH_RELEVANCE_CEILING:
                warnings.append(
                    f"WARNING {strand_dir.name}: relevance=high share is {share * 100:.1f}%, "
                    f"above the 40% ceiling"
                )

    return violations, warnings, total_entries


def discover_root() -> Path:
    """Infer the repo root from this script's location (tools/.. )."""
    return Path(__file__).resolve().parent.parent


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the lit-review corpus.")
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Repository root to validate (default: inferred from script location).",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve() if args.root is not None else discover_root()

    violations, warnings, entry_count = run_validation(root)

    for violation in violations:
        print(f"VIOLATION {violation}")
    for warning in warnings:
        print(warning)
    print(f"Checked {entry_count} entries; {len(violations)} violation(s).")

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
