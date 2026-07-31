# Strand C, Pretraining corpora, benchmarks, and evaluation protocols (Phase 1 brief)

**Goal:** populate `research/collection/datasets-benchmarks/` with at least 18 cards covering how the
field trains and measures: what corpora the checkpoints were pretrained on, which benchmarks and
protocols they are evaluated under, and whether those evaluations are sound.

This strand answers "how is transfer measured, and can the measurement be trusted". Strand D answers
the separate question of what data this project could actually fine-tune on. The split matters
because an evaluation protocol can invalidate a result on a dataset that is otherwise perfect for the
study, and Phase 4 needs both halves to say anything useful.

## Scope

Cover 5 categories.

### 1. Large EEG pretraining corpora

- Temple University Hospital EEG Corpus, Sleep-EDF, and other multi-thousand-hour sources used to
  pretrain the models in strand A.
- Recording context: clinical versus laboratory, montage, sampling rate, population.
- License and access terms, since these decide whether the project could continue pretraining rather
  than only fine-tune.

### 2. Downstream benchmarks the checkpoints report on

- BCI Competition sets, motor imagery, event-related potential paradigms, and the workload and
  attention datasets that transfer papers use.
- Participant counts, trials per participant, and class balance.
- Which checkpoints have already been evaluated on which benchmark, so the project can tell an
  established result from a novel one. This mapping is the category's main deliverable.

### 3. Benchmark suites and standardized protocols

- Multi-model, multi-dataset evaluation suites built specifically for brain foundation models.
- What each suite fixes: datasets included, splits, fine-tuning budget, metrics, and which
  checkpoints it covers.
- Where suites disagree with each other. Disagreement between two suites about how to split or score
  is more informative than either suite's leaderboard, and Phase 3 needs it named rather than
  averaged away.

### 4. Evaluation protocol conventions and their critiques

- Subject-wise versus record-wise versus random splits, and documented cases of leakage.
- Whether reported gains survive a corrected protocol, where anyone has checked.
- Metric conventions, and whether small-sample confidence intervals are reported at all.
- Shortcut learning in this specific setting: evidence that a model separated recording sessions,
  dataset identity, or acquisition hardware rather than the labelled construct.

Category 4 is the strand's center of gravity. A transfer number produced under a leaky split is not
weak evidence, it is no evidence, and Phase 4 cannot weigh the literature without knowing which
numbers were produced that way.

### 5. Formats and tooling standards

- Brain Imaging Data Structure for EEG, European Data Format, and what reads them.
- Conventions for storing events, annotations, and stimulus markers, since the project's labels come
  from stimulus markers.
- Reference implementations, carded as `type: tool` where a tool is the primary source.

## Per-entry deliverable

Create folder `research/collection/datasets-benchmarks/<slug>/` containing:

- `card.md` with `strand: datasets-benchmarks`, and `type: dataset` for corpora and benchmark
  datasets, `type: paper` for protocol and critique papers, `type: standard` for format
  specifications, `type: tool` for implementations.
- `source.md` always. For a corpus or tool with no paper, snapshot the canonical documentation or
  landing page and set `pdf_status: not-applicable`.
- `source.pdf` only when `meta.json.redistribution_ok` is true, `pdf_status` is `archived`, and
  `pdf_license` is in the redistributable set listed in the card schema addendum.
- `meta.json` with the access uniform resource locator, `retrieved_at`, license, and
  `redistribution_ok`. Record the data license separately from the paper license in `notes`.
- BibTeX appended to `research/collection/datasets-benchmarks/datasets-benchmarks.bib`, with the
  citation key rewritten to equal the entry slug exactly. `opencite` generates keys such as
  `Xu2019ADT`; replace them, since the validator and the direction papers both key on the slug.
- One categorized line in `research/collection/datasets-benchmarks/INDEX.md`.

Every `type: dataset` card must record, in "Notable details": participants, channels, sampling rate,
total hours, task, label type, license, access route, and which checkpoints were pretrained on or
evaluated against it. Write `unknown` where the source is silent. Do not infer.

Every protocol or benchmark-suite card must record the split rule, the metric, the fine-tuning budget
where one is specified, and the checkpoints covered.

Imported entries must set `imported_from: <relative path>` in `card.md`.

## Seed material

### Benchmark seed, supplied by the user

- Wu J, Ren Z, Wang J, Zhu P, Song Y, Liu M, Zheng Q, Bai L, Ouyang W, Song C. AdaBrain-Bench:
  Benchmarking Brain Foundation Models for Brain-Computer Interface Applications. Slug
  `adabrain-bench`. Identifier not yet resolved: `opencite` keyword search did not return it, so
  resolve it in Phase 2 from the arXiv listing or by exact title on OpenAlex and record the identifier
  in `meta.json`. Do not guess an identifier.

  Card as `type: standard` if it defines a protocol, or `type: paper` if it is an evaluation study;
  decide from the source rather than from the title. A category 3 entry above all: record which split
  protocol it prescribes, which datasets it includes, and which checkpoints it evaluates, so Phase 4
  can tell whether this project's planned evaluation is comparable to an established protocol or is
  bespoke.

### Benchmark leads surfaced while resolving the seeds

Recorded so they are not lost; verify each before carding. If two or more prescribe conflicting split
protocols, that disagreement belongs in the Phase 3 synthesis rather than being resolved by picking
one.

- Lu and colleagues. OmniEEG-Bench: A Standardized Evaluation Benchmark for EEG Foundation Models.
  arXiv `2606.00815`.
- Shen and colleagues. Brain4FMs: A Benchmark of Foundation Models for Electrical Brain Signal.
  OpenAlex `W7128864510`.
- Banville and colleagues. NeuralBench: A Unifying Framework to Benchmark NeuroAI Models. OpenAlex
  `W7161091175`.

### Shortcut-learning leads, shared with strand A

These bear on category 4 and are also recorded in the `eeg-models` brief for category 5. Card
whichever strand the source fits better and cross-reference the other; do not card twice.

- Lin and colleagues. The Identity Trap in EEG Foundation Models: A Diagnostic Audit. OpenAlex
  `W7164090340`.
- Zare. Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted
  Negative Controls. OpenAlex `W7171748390`.

### Remaining anchors

Categories 1, 2, and 5 rely on derived anchors: the pretraining corpora named by strand A's
checkpoints, followed by the benchmark datasets those checkpoints report on, followed by the format
specifications those datasets use.

## Search strategy

Sources: arXiv, OpenAlex, Crossref, PubMed, plus direct browsing for corpus landing pages, which
citation search covers poorly. Record such finds with the landing page as `source_url`.

Window: no lower bound. An older corpus can still be the one a 2025 checkpoint was pretrained on.

Representative queries:

- `opencite search "EEG foundation model benchmark standardized evaluation" --max 25`
- `opencite search "cross-subject evaluation protocol EEG leakage benchmark" --max 25`
- `opencite search "EEG deep learning shortcut learning dataset identity confound" --max 20`
- `opencite search "Temple University Hospital EEG corpus" --max 15`
- `opencite search "EEG BIDS specification events annotations" --max 15`
- `opencite cite "<pretraining corpus DOI>" --direction both`

Inclusion: the work releases a corpus used for pretraining, defines a benchmark or protocol,
specifies a data format, or critiques evaluation practice.

Exclusion: candidate datasets this project might fine-tune on, which belong to strand D unless a
strand A checkpoint pretrained on or benchmarked against them; private corpora with no access route.

## Skills to use

- `opencite:opencite` for lookup, retrieval, conversion, and BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 18 entries across all 5 categories
- [ ] At least 3 entries per category
- [ ] At least 4 entries in category 4, of which at least 2 critique a protocol or demonstrate
      leakage or shortcut learning rather than merely describing convention
- [ ] The checkpoint-to-benchmark mapping in category 2 is recorded on the cards, not left implicit
- [ ] Every `type: dataset` card records the full fixed field set, with `unknown` where the source is
      silent
- [ ] Every benchmark-suite card records its split rule, metric, and covered checkpoints
- [ ] Every entry folder has `card.md`, `source.md`, and `meta.json`
- [ ] Every entry has BibTeX in `datasets-benchmarks.bib`, keyed to the slug
- [ ] `INDEX.md` fully populated with categorized one-liners
- [ ] No more than 40 percent of entries marked `relevance: high`
- [ ] `uv run python tools/validate_corpus.py` exits 0
- [ ] No prose synthesis and no protocol recommendation; those are Phases 3 and 4

## Out of scope

- Model architectures and pretraining objectives. That is strand A, `eeg-models`. This strand cards
  the corpus; strand A cards the model trained on it.
- Fusion methods and peripheral signal modeling. That is strand B, `multimodal-biosignals`.
- Candidate datasets for this project to fine-tune on, dyadic and multi-person recordings, EEG plus
  peripheral physiology datasets, and label validity. Those moved to strand D,
  `candidate-datasets`. A dataset that is both a strand A benchmark and a strand D candidate gets a
  card in each, written to that strand's question.
- Data engineering tooling beyond format readers.
- Recommending an evaluation protocol for this project. Phase 4 decides that from this evidence.
