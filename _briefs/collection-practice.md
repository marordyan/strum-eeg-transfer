# Collection practice (read before starting any strand)

Rules and tool invocations that apply to every strand, separated out so there is one place to fix
them rather than four. Everything here was learned from the Phase 2 pilot on `eeg-models`, where six
entries were collected specifically to find these problems before four agents hit them at once. Each
item below cost real time or nearly corrupted a card.

Your strand brief governs what to collect. This document governs how.

## Tool invocations that actually work

### Converting a PDF to markdown

**Superseded. Use pymupdf4llm; see "Converting PDFs" below for the invocation and the measurements.**
Kept only because the failure recorded here is real and someone will otherwise rediscover it: bare
`uvx opencite convert` fails on a missing dependency, and `uvx --from 'opencite[pdf]'` then fails on
markitdown's own extra, so the only form of the markitdown route that runs at all is

```bash
uvx --from 'opencite[pdf]' --with 'markitdown[pdf]' opencite convert <pdf> -o <out.md>
```

Do not use it for new entries. It mangles two-column layouts badly enough that the whole corpus was
re-extracted.

### Resolving a bare OpenAlex work identifier

`opencite lookup` handles digital object identifiers, not OpenAlex work identifiers.
`uvx opencite lookup "W7164090340"` returns "Paper not found". Use the REST interface:

```bash
curl -s "https://api.openalex.org/works/W7164090340"
```

Several leads in the briefs are given as OpenAlex identifiers, so this is not an edge case.

### Resolving a paper that keyword search cannot find

Keyword search misses recent preprints that exact-title search finds. Before concluding an identifier
is unresolvable, try the exact title in quotes. In the pilot, BrainWave failed repeated keyword
queries and resolved immediately on exact title. Only after exact title, an arXiv listing search, and
an OpenAlex title query all fail should an entry take the `not-available` path.

Never construct an identifier that looks plausible. A card honestly recording a failed resolution is
correct and useful; a card carrying a well-formed wrong identifier is corpus poison, because
everything downstream treats it as verified.

## Endpoints and invocations, corrected by four strands

Corrections found after the pilot, during the four-strand run. Each cost an agent time.

- **`opencite cite --direction` takes `citing`, `references`, or `both`.** Not `backward`. An earlier
  brief said `backward` and the invocation simply fails. `both` also emitted
  `Citation query failed: 'NoneType' object is not iterable` while still returning merged results, so
  run the two directions separately when the answer matters.
- **`export.arxiv.org` is unreachable from this environment** and returns empty results *silently*,
  which is the same failure shape as the grep trap below. `curl https://arxiv.org/abs/<id>` and
  `https://arxiv.org/search/?searchtype=all&query=<exact title>` both work. The web search interface is
  the third fallback when `opencite` and OpenAlex both return nothing, and it is what finally resolved
  two entries.
- **`opencite search` is unreliable enough that it should not be the primary route.** Semantic Scholar
  rate-limits nearly every call, OSF returns HTTP 400 on any query containing a colon, and one query
  ran past 120 seconds. `opencite lookup` on a known identifier is fine. For discovery, call the
  OpenAlex and Crossref REST interfaces directly; they were faster and more complete in every strand.
  PubMed `esearch` beat everything for psychophysiology and human-factors venues.
- **Publishers that block automated fetches, with the endpoints that work.** IOP returns a captcha
  page, PMC an interstitial, MDPI 403, eLife 406, ACM 403, and IEEE a JavaScript challenge, all under
  a status that looks like success. IEEE is the trap of the group, because the open-access PDF URL
  that Unpaywall and Semantic Scholar both advertise
  (`ieeexplore.ieee.org/ielx7/.../<id>.pdf`) is one of the challenge pages; the working alternate is
  `https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=<arnumber>&ref=` with a browser
  user-agent.

  Working alternates for the rest: `europepmc.org/articles/<PMCID>?pdf=render`,
  `res.mdpi.com/d_attachment/...`,
  `cdn.elifesciences.org/articles/<id>/elife-<id>-v2.pdf`, and the Europe PMC `fullTextXML` endpoint.
  A naive `curl -o source.pdf` against a blocked endpoint writes HTML into a file named `.pdf`; the
  validator now rejects any `source.pdf` without a `%PDF` header, so this fails loudly rather than
  entering the corpus.
- **Europe PMC free-text search prefers Publisher Corrections to the article itself.** Searching by
  title, or even by the PMCID quoted inside a correction notice, can return the two-page correction.
  Only a `DOI:"..."` query resolves reliably. This is silent wrong-record retrieval and easy to miss.

## Discovery when the citation graph is empty

The pilot brief said to traverse `opencite cite --direction both` from existing entries. For recent
preprints this returns nothing: OpenAlex often has `referenced_works: []` and zero citations for a
2025 or 2026 arXiv posting, so the graph is empty exactly where the newest work is.

What worked instead, and produced most of the hardest entries in two strands: read the reference
sections of the sources already archived in the corpus. A pretrained-model paper's related-work
section is a curated list of the checkpoints and critiques the strand needs, and it is already on
disk in `source.md`.

## Do not use grep on converted markdown

This nearly poisoned a card in the pilot. Markitdown output can contain bytes that make BSD grep on
macOS treat the file as binary, and `grep -c` then prints nothing and exits 1, which is
indistinguishable from a genuine zero. It was verified at the time on `labram-2024/source.md`, then
a markitdown conversion: `grep -c "Hz"` reported no matches while Python counted 24 occurrences of
the same string in the same file.

That example no longer reproduces, and the reason is worth knowing rather than hiding. Every
extraction was later regenerated with pymupdf4llm, which emits plain UTF-8, so the same command now
returns a count on the committed file. The hazard is a property of the converter's output, not of the
corpus, so it returns the moment anyone converts with a tool that emits stray control bytes. Treat
the rule as standing and the example as historical.

The failure mode is what makes this dangerous. An agent that trusts the silent zero writes "the paper
does not report its sampling rate" on the card, and that reads as diligence rather than as an error.

Search converted sources with `rg`, or with Python:

```bash
python3 -c "print(open('<path>', encoding='utf-8', errors='replace').read().count('<needle>'))"
```

Two related traps found later in the same run:

- **Short uppercase acronyms need case-sensitive, word-boundary matching.** A case-insensitive search
  for `STRUM` returns 38 hits on `instrument` and `instrumentation` and zero real ones. The reader
  concludes the term appears throughout when it never appears at all.
- **Normalize the minus sign before searching.** Several extractions render minus as U+2212 rather
  than ASCII hyphen, so a search for `-0.5` misses `−0.5`. Four verification checks came back as
  misses on that alone.
- **Collapse whitespace as well as stripping emphasis, and never assert a negative without it.**
  pymupdf4llm renders emphasised decimals as `12 _._ 7`. Stripping `_` and `*` leaves `12 . 7`, so a
  search for `12.7` still misses. The correct normalisation for any literal search is
  `re.sub(r'\s+', '', re.sub(r'[_*`]', '', text))` on both the haystack and the needle. This is the
  most expensive single defect the review produced: a Phase 5 spot-check concluded from an
  unnormalised search that "the string 12.7 does not occur in the source at all", retracted a
  faithfully-sourced number from a card and from the direction paper, and published the retraction
  as a headline finding. The number was at `source.md:341` the whole time. A positive search that
  fails costs a lookup; a negative claim built on a failed search deletes true content and states a
  falsehood about a source, which is the one defect class a citation guarantee cannot catch.

## Converting PDFs: use pymupdf4llm, not markitdown

Measured on this corpus, not assumed. On one benchmark paper, `pymupdf4llm` preserved 72 markdown
table rows where markitdown preserved none, and cut de-spacing artifacts from 1413 runs to 7.
Markitdown also joins words across a two-column layout, producing text like `ZilingLu1†` that cannot
be quoted or reliably searched. Across 50 re-extracted entries, 39 improved from `md_quality: rough`
to `clean`, and seven gained real content markitdown had silently dropped, one by 61 percent.

```bash
uvx --from pymupdf4llm python -c "
import pymupdf4llm, pathlib, sys
pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1]), encoding='utf-8')
" <pdf> <entry>/source.md
```

One trap it introduces: decimal points inside emphasized table cells are escaped as `13_._8`. A
verification pass that does not strip `_` and `*` before matching will report large numbers of
spurious misses. In one run this produced 49 false alarms out of 84 apparent misses.

## When the tables are images, render the page

Some papers have no text layer behind their tables at all. EEG Conformer's Tables I to IV return
nothing from `pymupdf.get_text()` between their captions: the numbers exist only as pixels. No
converter recovers them, so this is not a conversion-fidelity problem and no `md_quality` value
describes it well; use `partial` and name the loss in `notes`.

The numbers are still readable. Render the page and look at it:

```bash
uvx --from pymupdf python -c "
import pymupdf, sys
d = pymupdf.open(sys.argv[1])
d[int(sys.argv[2])-1].get_pixmap(dpi=200).save(sys.argv[3])
" <pdf> <page number> /tmp/page.png
```

Then read the PNG. This is the only route to an image-only table, and on the pilot's most-cited
supervised baseline it was the difference between a card with accuracy numbers and a card without
any. Note that the `Read` tool cannot open a PDF directly in this environment, which needs
`pdftoppm` from poppler; the pymupdf route above needs no install.

## A third case: the source declined to do the thing

Collection practice already distinguishes "the source does not report it" from "the source reports it
and we could not see it". A third case turns up in the model strand and is a finding rather than a
gap: the source deliberately did not do it.

EEG Conformer has no pretraining corpus and no pretraining hours, not because the paper omits them
but because it argues against pretraining in this setting: "pre-training is not used in EEG
Conformer, due to the limited data for calibration". Recording that as `not reported` would file a
stated design choice as an absence. Card it as the choice it is, quote the reasoning, and give the
quantity as zero where a number is required.

## Reading a paper you may not republish

A licence that forbids redistribution stops the PDF being committed. It does not stop it being read.
Cache it as `source.local.pdf`, which is gitignored, and regenerate `source.md` from it. The
validator requires a real `%PDF` header and forbids it coexisting with a committed `source.pdf`.

This matters most where results live in figures: without a cached copy, a leaderboard that exists
only as an image is simply unavailable to synthesis. Note the limit, though. A locally cached PDF is
not reproducible for anyone who clones the corpus, so any claim resting on it must also be supported
by the committed `source.md`.

## Second-hand text is a provenance category, and must be labelled

One entry's only available method description came from search-engine snippets of a publisher
abstract page, the paper being unreadable everywhere. The first snippet attributed a named
architecture to the paper that a follow-up search showed belongs to a different article.

If a card rests on text you did not read in the source, say so in the card and in `source.md`, name
where the text came from, and do not let a snippet supply a specific claim such as a method name, an
architecture, or a number. `md_quality: abstract-only` overstates such an entry, because there was no
retrievable abstract either; state the truth in `notes` rather than letting the enum imply better
sourcing than exists.

## BibTeX from opencite is not trustworthy

Rewriting the citation key to the slug, which the schema addendum requires, is necessary but nowhere
near sufficient. Three of six pilot entries came back with substantively wrong metadata:

- a conference paper was given `booktitle = {Balkan Conference in Informatics}`, an unrelated venue,
  from a Semantic Scholar venue-match error
- an author was silently dropped from the author list
- conference papers came back as `@article` with the conference name stuffed into `journal`

These fields flow into the direction paper's reference list, where a wrong venue or a truncated author
list is a citation error in a published document.

So for every entry: verify the entry type, venue, year, and full author list against the PDF's own
title block or against Crossref before appending to the strand bib. Treat opencite's venue and author
fields as leads. Fix the entry type (`@inproceedings` for conference papers) rather than leaving what
opencite emitted.

## Reading the source well enough to fill the card

The per-entry cost is dominated by this, not by retrieval. The facts each brief requires are scattered:
in the pilot, one paper's parameter counts were in an appendix table and its patch size in another,
neither mentioned in the body. Budget four to six targeted reads per paper after conversion. This
cannot be shortened without guessing, and guessing here is what the whole review is built to avoid.

Where a converted source is mangled, cross-check numbers against the PDF's own tables rather than
trusting the extraction.

## Two distinct kinds of missing fact

Your brief requires certain facts on every card, for example a transfer number with its baseline. When
one is absent, which of these two cases applies changes what a reader should do about it, so record
them differently:

- **The source does not report it.** Write `not reported`. This is evidence about the literature and
  belongs in the synthesis.
- **The source reports it but you could not see it**, typically a paywalled paper whose abstract gives
  the comparator and the direction but not the magnitude. Write
  `reported but not accessible: <what is known>`, and in `meta.json.notes` record what retrieval was
  attempted. This is a gap in our access, not in the literature, and it is worth re-attempting later.

Conflating the two would tell Phase 4 that the field has not measured something when in fact we simply
have not read it.

## Use domain terms precisely, even when the source does not

Caught during review of the pilot's first card. The card said a pretrained model tolerates an unseen
"montage", following the source's own abstract. But montage means the derivation scheme, referential
or bipolar or average-reference, while what the mechanism actually supports is an arbitrary electrode
*layout*, a set of positions. The distinction was load-bearing: a bipolar derivation is a difference
between two electrodes, and the model in question has no representation for one, so its authors
substituted the midpoint of the pair in preprocessing. The imprecise word concealed an approximation
that matters for whether the method transfers.

Papers, including good ones, use these terms loosely in abstracts and tighten them in methods
sections. When they diverge, card the methods-section meaning, and say on the card that the abstract
is looser so a later reader does not think the card misread the paper.

Terms worth keeping distinct in this corpus: montage versus electrode layout versus channel count;
epoch versus trial versus window; session versus run versus recording; subject-wise versus
record-wise splits. If a source blurs one of these in a way that changes what a claim supports, that
is a finding for "Open questions / limitations", not a wording preference.

## When a source contradicts itself

This happened twice in six pilot entries. One paper's prose named a different classifier than its own
table; another gave a different model count in its abstract, its table, and its conclusion.

Standing rule: prefer the tables and the abstract over body prose, card the value you take, and record
the discrepancy in the card's "Open questions / limitations" section. Do not silently pick one. A
source that contradicts itself is a fact about that source, and Phase 3 needs it.

## Fields that need strand-level judgment

### `relevance`

The 40 percent ceiling on `relevance: high` is a property of the finished strand, but you assign the
field one entry at a time and cannot see the distribution mid-collection. Assign provisionally as you
go, then rebalance at strand close, before running the validator for the last time. The validator
warns rather than fails on this, so nothing blocks, and an unrebalanced strand quietly loses the
field's discriminative power.

### `imported_from`

Set this only when an entry was carried over from an existing document rather than found during
collection: a prior literature review, a grant document, another strand's corpus. A paper named as a
seed or a lead in your brief is not imported, it is found. When nothing was carried over, `null` is
correct. None of the pilot's six entries qualified.

## `type` values

Use the full schema vocabulary, `paper`, `dataset`, `tool`, `platform`, `standard`, choosing from what
the source actually is. Where a brief lists a narrower set, the brief is describing what that strand
usually collects, not restricting the enum. A released checkpoint with only a repository is a `tool`;
a benchmark that defines a protocol is a `standard`.

## Expect most entries to be markdown-only

The pilot corrected an assumption built into the briefs. Because arXiv's default license grants no
redistribution right to third parties, and because most arXiv postings use it, `pdf_status: archived`
is the exception rather than the rule. One of six pilot entries qualified.

Two consequences. Extraction quality matters more than archival, so `md_quality` and the `notes`
describing what is unusable carry real weight. And paywalled entries are cheaper per entry than open
ones, not more expensive, since an abstract-only card is quick to write. Cheaper does not mean better:
such a card supports much less, and the acceptance criteria still apply.
