#!/usr/bin/env python3
"""Validate the lit-review corpus under research/collection/.

Checks each paper-card entry (research/collection/<strand>/<slug>/) for
structural consistency: required files, frontmatter schema, the
redistribution-license invariant, and cross-references into the strand's
INDEX.md and .bib file. See:

  research/collection/_schema/paper-card.md

Requires PyYAML (declared in the `dev` dependency group; `uv run` installs
dev groups by default, so this stays available in CI without extra steps).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

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

# research/collection/_schema/paper-card.md, "pdf_license vocabulary".
PDF_LICENSE_VALUES = {
    "CC-BY",
    "CC-BY-2.0",
    "CC-BY-3.0",
    "CC-BY-4.0",
    "CC-BY-NC",
    # Added after the four-strand run: without these, a Nature Scientific Data
    # article under CC-BY-NC-ND had to be recorded with a leading token of
    # "preprint-cc-arxiv", which asserts an arXiv posting that does not exist.
    # A vocabulary that forces a false statement is worse than a longer one.
    "CC-BY-NC-ND",
    "CC-BY-SA",
    "CC-BY-NC-SA",
    "CC0",
    "preprint-cc-arxiv",
    "preprint-cc-biorxiv",
    "preprint-cc-osf",
    "author-accepted-manuscript",
    "publisher-paywall",
    "not-applicable",
    "unknown",
}

# Subset of PDF_LICENSE_VALUES that the schema's mapping table marks as
# actually redistributable. Everything else in the vocabulary - including
# "not-applicable" ("no paper exists") and "unknown" - must not sit next to
# a committed source.pdf, even though only "publisher-paywall" and
# "unknown" are excluded from the separate redistribution_ok=false rule
# above.
REDISTRIBUTABLE_LICENSES = {
    "CC-BY",
    "CC-BY-2.0",
    "CC-BY-3.0",
    "CC-BY-4.0",
    "CC-BY-NC",
    # NoDerivatives permits verbatim redistribution, so a PDF may be archived;
    # the markdown extraction rests on research-note fair use instead, which
    # the schema addendum requires be stated in notes.
    "CC-BY-NC-ND",
    "CC-BY-SA",
    "CC-BY-NC-SA",
    "CC0",
    "preprint-cc-arxiv",
    "preprint-cc-biorxiv",
    "preprint-cc-osf",
    "author-accepted-manuscript",
}

# Strand directories currently recognized under research/collection/. New
# strands are legitimate but should be added here deliberately, rather than
# a typo'd or misplaced directory silently going uncounted.
EXPECTED_STRANDS = {
    "eeg-models",
    "multimodal-biosignals",
    "datasets-benchmarks",
    "candidate-datasets",
}

YEAR_RE = re.compile(r"^\d{4}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
BIB_KEY_RE = re.compile(r"@\w+\{\s*([^,\s]+)\s*,")
INDEX_LINK_RE = re.compile(r"\]\(\./([^)]+)\)")
PDF_LICENSE_LEADING_RE = re.compile(r"[(;]")
DOI_URL_PREFIX_RE = re.compile(r"^https?://(dx\.)?doi\.org/")
ARXIV_ABS_RE = re.compile(r"arxiv\.org/abs/([0-9]+\.[0-9]+)")

HIGH_RELEVANCE_CEILING = 0.40
HIGH_RELEVANCE_MIN_ENTRIES = 5

# Sentinel distinguishing "meta.json was never successfully parsed into a
# dict" (missing file, unreadable, invalid JSON, or a non-object top-level
# value such as `null` or a list) from "parsed to a dict". Using None for
# this would collide with `json.loads("null")`, which also returns None -
# that collision is exactly what let a literal-`null` meta.json bypass every
# downstream check (Finding 1).
_UNSET = object()


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate keys in a mapping.

    PyYAML's default is last-key-wins, which would silently accept
    `relevance: high` followed by `relevance: medium`. Raising here turns
    that into a yaml.YAMLError, which parse_frontmatter reports as a
    violation like any other malformed YAML.

    A YAML key can be unhashable (e.g. `? [a, b]`), in which case it can't
    be tested for set membership. The membership test and the bookkeeping
    add are both guarded with `try/except TypeError` so an unhashable key
    just skips duplicate-tracking for itself; `super().construct_mapping`
    is then left to raise PyYAML's own ConstructorError ("found unhashable
    key"), which is still a yaml.YAMLError and so still reported as a
    violation naming the file, rather than escaping as a bare TypeError
    that aborts the whole run.
    """

    def construct_mapping(self, node, deep=False):
        seen: set[object] = set()
        for key_node, _value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                is_duplicate = key in seen
            except TypeError:
                is_duplicate = False
            if is_duplicate:
                raise yaml.constructor.ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key {key!r}",
                    key_node.start_mark,
                )
            try:
                seen.add(key)
            except TypeError:
                pass
        return super().construct_mapping(node, deep=deep)


def _read_text_safe(path: Path) -> tuple[str | None, str | None]:
    """Read a file as UTF-8 text.

    Returns (text, None) on success or (None, error_message) on failure, so
    one bad file (non-UTF-8 bytes, permissions, etc.) is reported as a
    violation naming the file rather than aborting the whole run with a
    traceback.
    """
    try:
        return path.read_text(encoding="utf-8"), None
    except UnicodeDecodeError as exc:
        return None, f"could not be read as UTF-8: {exc}"
    except OSError as exc:
        return None, f"could not be read: {exc}"


def _read_bytes_safe(path: Path) -> tuple[bytes | None, str | None]:
    """Read a file as raw bytes.

    Returns (data, None) on success or (None, error_message) on failure, so
    an unreadable file (e.g. permissions) is reported as a violation naming
    the file rather than aborting the whole run with a traceback.
    """
    try:
        return path.read_bytes(), None
    except OSError as exc:
        return None, f"could not be read: {exc}"


def parse_frontmatter(text: str) -> tuple[dict[str, object] | None, list[str]]:
    """Parse the '---' delimited YAML frontmatter block at the top of card.md.

    Two hand checks exist only to produce the specific error messages
    below: line 1 must be '---', and there must be a later line that is
    exactly '---' with no leading whitespace to close the block (not merely
    a line that strips down to '---' - that would also match an indented
    '---' inside a block scalar, which YAML does not treat as a document
    boundary).

    The actual parse does not hand-slice the block: the FULL card text is
    given to `yaml.load_all(text, Loader=_UniqueKeyLoader)`, and only the
    first document is taken via `next(...)`. YAML's own document-boundary
    rule then decides where the frontmatter ends, so a '---' line indented
    inside a block scalar cannot truncate it early. The generator is lazy,
    so the markdown body after the closing delimiter is never parsed and
    its colons and bullets cannot raise. Uses `_UniqueKeyLoader` so a
    duplicate key is a violation rather than silently last-wins.

    Returns (fields, parse_errors). `fields` is None when there is no
    well-formed frontmatter block to parse at all: missing delimiters,
    malformed YAML, or a block that doesn't parse to a mapping. Never
    raises: a yaml.YAMLError (malformed YAML, duplicate/unhashable keys)
    or a RecursionError (deeply nested flow YAML can exceed the parser's
    recursion limit) becomes an error string instead.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, ["card.md does not start with a '---' frontmatter delimiter"]

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i] == "---":
            end_idx = i
            break
    if end_idx is None:
        return None, ["card.md frontmatter block has no closing '---' delimiter"]

    try:
        loaded = next(yaml.load_all(text, Loader=_UniqueKeyLoader))
    except (yaml.YAMLError, RecursionError) as exc:
        return None, [f"card.md frontmatter is not valid YAML: {exc}"]

    if loaded is None:
        return {}, []
    if not isinstance(loaded, dict):
        return None, ["card.md frontmatter block must be a YAML mapping"]

    return loaded, []


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


def _validate_frontmatter_fields(
    frontmatter: dict[str, object], strand_name: str, slug_name: str
) -> list[str]:
    """Check required keys, slug/strand consistency, enums, and year/date formats."""
    violations: list[str] = []

    for key in REQUIRED_FRONTMATTER_KEYS:
        value = frontmatter.get(key)
        missing = (
            value is None
            or (isinstance(value, str) and value.strip() == "")
            or (isinstance(value, list) and len(value) == 0)
            or (isinstance(value, dict) and len(value) == 0)
        )
        if missing:
            violations.append(f"frontmatter missing required key '{key}'")

    slug_value = frontmatter.get("slug")
    if slug_value is not None and slug_value != slug_name:
        violations.append(
            f"frontmatter slug '{slug_value}' does not match folder name '{slug_name}'"
        )

    strand_value = frontmatter.get("strand")
    if strand_value is not None and strand_value != strand_name:
        violations.append(
            f"frontmatter strand '{strand_value}' does not match parent folder '{strand_name}'"
        )

    _check_enum(frontmatter, "type", TYPE_VALUES, violations)
    _check_enum(frontmatter, "relevance", RELEVANCE_VALUES, violations)
    _check_enum(frontmatter, "pdf_status", PDF_STATUS_VALUES, violations)
    _check_enum(frontmatter, "md_quality", MD_QUALITY_VALUES, violations)

    # PyYAML parses `year: 2023` as int and `added: 2024-01-01` as
    # datetime.date; str() first keeps these regexes working for both the
    # old hand-rolled-parser strings and the new native types.
    year = frontmatter.get("year")
    if year is not None and not YEAR_RE.match(str(year)):
        violations.append(f"year '{year}' is not a 4-digit year")

    added = frontmatter.get("added")
    if added is not None and not DATE_RE.match(str(added)):
        violations.append(f"added '{added}' is not a YYYY-MM-DD date")

    return violations


def _validate_meta_and_pdf(entry_dir: Path, frontmatter: dict[str, object] | None) -> list[str]:
    """Parse meta.json and enforce the redistribution-license and
    archival-storage invariants against source.pdf."""
    violations: list[str] = []

    pdf_path = entry_dir / "source.pdf"
    pdf_exists = pdf_path.is_file()

    # A committed source.pdf must actually be a PDF. Several publishers
    # (IOP, PMC, MDPI, eLife) answer automated fetches with an HTML challenge
    # or interstitial page under HTTP 200, so a naive download writes HTML to
    # a file named source.pdf. The sha256 would match its own garbage and
    # every other check would pass.
    if pdf_exists:
        head, read_error = _read_bytes_safe(pdf_path)
        if read_error is not None:
            violations.append(f"source.pdf {read_error}")
        elif not head.startswith(b"%PDF"):
            violations.append(
                "source.pdf is not a PDF (no %PDF header); a publisher challenge or "
                "interstitial page was probably saved under HTTP 200"
            )

    meta: object = _UNSET
    meta_path = entry_dir / "meta.json"
    if meta_path.is_file():
        meta_text, read_error = _read_text_safe(meta_path)
        if read_error is not None:
            violations.append(f"meta.json {read_error}")
        else:
            try:
                parsed = json.loads(meta_text)
            except json.JSONDecodeError as exc:
                violations.append(f"meta.json is not valid JSON: {exc}")
            else:
                # Checked directly against `parsed`, not `is not None` -
                # json.loads("null") also returns None, and that collision
                # with the "not yet parsed" sentinel is exactly what let a
                # literal-null meta.json bypass this check (Finding 1).
                if not isinstance(parsed, dict):
                    violations.append("meta.json top-level value must be an object")
                else:
                    meta = parsed

    redistribution_ok: bool | None = None
    if isinstance(meta, dict):
        for key in REQUIRED_META_KEYS:
            if key not in meta:
                violations.append(f"meta.json missing required key '{key}'")

        if "redistribution_ok" in meta:
            value = meta["redistribution_ok"]
            if isinstance(value, bool):
                redistribution_ok = value
            else:
                violations.append("meta.json redistribution_ok must be a boolean")

        if "pdf_license" in meta:
            raw_license = meta["pdf_license"]
            if not isinstance(raw_license, str):
                violations.append("meta.json pdf_license must be a string")
            else:
                # The schema permits a trailing parenthetical or semicolon
                # qualifier (e.g. "publisher-paywall (NeuroImage); ...");
                # only the leading token is checked against the vocabulary.
                leading = PDF_LICENSE_LEADING_RE.split(raw_license, maxsplit=1)[0].strip()
                if leading not in PDF_LICENSE_VALUES:
                    violations.append(
                        f"meta.json pdf_license '{raw_license}' has leading token "
                        f"'{leading}' not in {sorted(PDF_LICENSE_VALUES)}"
                    )
                else:
                    # publisher-paywall is the only vocabulary member with
                    # that prefix, so it is exactly `==`, not a real prefix
                    # family; membership makes that explicit instead of
                    # reading like unfinished prefix-matching logic.
                    if leading in {"publisher-paywall", "unknown"}:
                        if redistribution_ok is not False:
                            violations.append(
                                f"meta.json pdf_license '{raw_license}' implies "
                                f"redistribution_ok must be false, but redistribution_ok "
                                f"is {redistribution_ok!r}"
                            )
                    # Separate from the redistribution_ok cross-check above:
                    # a committed source.pdf requires a license that is
                    # actually redistributable, not merely "not one of the
                    # two excluded values". Closes the hole where
                    # "not-applicable" ("no paper exists") or a qualified
                    # variant like "not-applicable (really publisher-
                    # paywall)" sat next to a committed PDF uncaught.
                    if pdf_exists and leading not in REDISTRIBUTABLE_LICENSES:
                        violations.append(
                            f"meta.json pdf_license '{raw_license}' has leading token "
                            f"'{leading}', which is not in the redistributable set "
                            f"{sorted(REDISTRIBUTABLE_LICENSES)}; a committed source.pdf "
                            "requires a redistributable license"
                        )

    # License invariant: the single source of truth for whether source.pdf
    # is allowed to exist in the repo.
    if redistribution_ok is False and pdf_exists:
        violations.append("redistribution_ok is false but source.pdf exists")

    if frontmatter is not None:
        pdf_status = frontmatter.get("pdf_status")
        if pdf_status == "archived":
            if not pdf_exists:
                violations.append("pdf_status is 'archived' but source.pdf is missing")
            sha256 = meta.get("pdf_sha256") if isinstance(meta, dict) else None
            if not sha256:
                # Suppressed when meta is _UNSET: meta.json could not be
                # parsed at all in that case, and a violation naming that
                # real cause (missing file, unreadable, invalid JSON, or a
                # non-object top-level value) was already appended above.
                # Without this guard the report named two causes for one
                # problem.
                if meta is not _UNSET:
                    violations.append(
                        "pdf_status is 'archived' but meta.json pdf_sha256 is null/missing"
                    )
            elif pdf_exists:
                pdf_bytes, read_error = _read_bytes_safe(pdf_path)
                if read_error is not None:
                    violations.append(f"source.pdf {read_error}")
                else:
                    actual = hashlib.sha256(pdf_bytes).hexdigest()
                    if actual != sha256:
                        violations.append(
                            f"pdf_sha256 mismatch: meta.json has '{sha256}', actual is '{actual}'"
                        )
        else:
            if frontmatter.get("pdf_path") is not None:
                violations.append("pdf_status is not 'archived' but card.md pdf_path is not null")
            # Symmetric storage rule: only an 'archived' entry may commit a
            # PDF. Without this, `pdf_status: not-redistributable` next to a
            # committed source.pdf and `redistribution_ok: true` passed
            # silently.
            if pdf_exists:
                violations.append(
                    f"pdf_status is '{pdf_status}' but source.pdf exists in the entry "
                    "folder (only 'archived' entries may commit a PDF)"
                )

    return violations


def validate_entry(entry_dir: Path, root: Path) -> tuple[list[str], dict[str, object] | None]:
    """Validate one entry folder.

    Returns (violations, frontmatter). Each violation string already
    includes the entry's path relative to `root`. `frontmatter` is the
    parsed card.md frontmatter (or None if it could not be parsed),
    returned so validate_strand's relevance tally does not need to re-read
    and re-parse card.md a second time.
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
        card_text, read_error = _read_text_safe(card_path)
        if read_error is not None:
            raw_violations.append(f"card.md {read_error}")
        else:
            frontmatter, parse_errors = parse_frontmatter(card_text)
            raw_violations.extend(parse_errors)

    if frontmatter is not None:
        raw_violations.extend(_validate_frontmatter_fields(frontmatter, strand_name, slug_name))

    raw_violations.extend(_validate_meta_and_pdf(entry_dir, frontmatter))

    return [f"{rel}: {message}" for message in raw_violations], frontmatter


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
        entry_violations, frontmatter = validate_entry(entry_dir, root)
        violations.extend(entry_violations)
        if frontmatter is not None and frontmatter.get("relevance") == "high":
            high_count += 1

    # BibTeX keys must match entry slugs verbatim (exact, case-sensitive):
    # opencite emits keys like "Xu2019ADT", and Phase 2 agents are expected
    # to rewrite them to the slug before committing. A fuzzy match would
    # accept opencite's default keys and defeat the point of the check.
    bib_path = strand_dir / f"{strand_name}.bib"
    bib_text = ""
    if bib_path.is_file():
        text, read_error = _read_text_safe(bib_path)
        if read_error is not None:
            violations.append(f"{rel_strand}/{strand_name}.bib: {read_error}")
        else:
            bib_text = text
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
        index_text, read_error = _read_text_safe(index_path)
        if read_error is not None:
            violations.append(f"{rel_strand}/INDEX.md: {read_error}")
        else:
            linked_first_segments: set[str] = set()
            for link in INDEX_LINK_RE.findall(index_text):
                target = (strand_dir / link).resolve()
                if not target.exists():
                    violations.append(
                        f"{rel_strand}/INDEX.md: link './{link}' does not resolve to an "
                        "existing path"
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


def _entry_identifier(entry_dir: Path) -> str | None:
    """Return a normalized identifier for an entry, or None if it has none.

    Prefers meta.json's doi, falling back to an arXiv id parsed out of
    source_url, so that a DOI-registered arXiv paper and a bare abs link to
    the same preprint collapse to one key.
    """
    meta_path = entry_dir / "meta.json"
    if not meta_path.is_file():
        return None
    text, read_error = _read_text_safe(meta_path)
    if read_error is not None:
        return None
    try:
        meta = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(meta, dict):
        return None

    doi = meta.get("doi")
    if isinstance(doi, str) and doi.strip():
        key = DOI_URL_PREFIX_RE.sub("", doi.strip().lower())
        return key.replace("10.48550/arxiv.", "arxiv:")

    url = meta.get("source_url")
    if isinstance(url, str):
        match = ARXIV_ABS_RE.search(url)
        if match:
            return f"arxiv:{match.group(1)}"
    return None


def _cross_strand_duplicate_warnings(collection_root: Path, root: Path) -> list[str]:
    """Warn when one identifier is carded in more than one strand.

    The per-strand duplicate-key check cannot see across strands, so the same
    paper carded twice passes clean and becomes two bibliography entries for
    one identifier at synthesis time. Dual-carding is legitimate when each
    card answers its own strand's question, so this warns rather than fails;
    the point is that it be deliberate and visible.
    """
    by_identifier: dict[str, list[str]] = {}
    for strand_dir in iter_strands(collection_root):
        for entry_dir in sorted(p for p in strand_dir.iterdir() if p.is_dir()):
            if entry_dir.name.startswith("_"):
                continue
            identifier = _entry_identifier(entry_dir)
            if identifier is None:
                continue
            by_identifier.setdefault(identifier, []).append(
                str(entry_dir.relative_to(root / "research" / "collection"))
            )

    warnings: list[str] = []
    for identifier, locations in sorted(by_identifier.items()):
        if len(locations) > 1:
            warnings.append(
                f"WARNING identifier '{identifier}' is carded in {len(locations)} strands: "
                f"{', '.join(locations)}"
            )
    return warnings


def run_validation(root: Path) -> tuple[list[str], list[str], int, dict[str, int]]:
    """Validate the whole corpus under root/research/collection/.

    Returns (violations, warnings, total_entry_count, per_strand_entry_counts).
    """
    collection_root = root / "research" / "collection"
    violations: list[str] = []
    warnings: list[str] = []
    total_entries = 0
    strand_counts: dict[str, int] = {}

    for strand_dir in iter_strands(collection_root):
        strand_name = strand_dir.name

        if strand_name not in EXPECTED_STRANDS:
            warnings.append(
                f"WARNING unexpected strand directory '{strand_name}' "
                f"(not one of {sorted(EXPECTED_STRANDS)})"
            )

        strand_card_path = strand_dir / "card.md"
        if strand_card_path.is_file():
            violations.append(
                f"{strand_card_path.relative_to(root)}: card.md found at strand depth; "
                "an entry folder level appears to have been skipped"
            )

        strand_violations, entry_count, high_count = validate_strand(strand_dir, root)
        violations.extend(strand_violations)
        total_entries += entry_count
        strand_counts[strand_name] = entry_count

        if entry_count >= HIGH_RELEVANCE_MIN_ENTRIES:
            share = high_count / entry_count
            if share > HIGH_RELEVANCE_CEILING:
                warnings.append(
                    f"WARNING {strand_name}: relevance=high share is {share * 100:.1f}%, "
                    f"above the 40% ceiling"
                )

    warnings.extend(_cross_strand_duplicate_warnings(collection_root, root))

    return violations, warnings, total_entries, strand_counts


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

    violations, warnings, entry_count, strand_counts = run_validation(root)

    for violation in violations:
        print(f"VIOLATION {violation}")
    for warning in warnings:
        print(warning)
    for strand_name in sorted(strand_counts):
        print(f"  {strand_name}: {strand_counts[strand_name]} entries")
    print(f"Checked {entry_count} entries; {len(violations)} violation(s).")

    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
