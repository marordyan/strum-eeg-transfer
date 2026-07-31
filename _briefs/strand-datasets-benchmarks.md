# Strand C, Datasets, benchmarks, and evaluation protocols (Phase 1 brief)

**Goal:** populate `research/collection/datasets-benchmarks/` with at least 18 cards covering
the data layer: what electroencephalography (EEG) and physiology datasets exist, what each one
actually contains, how models are evaluated on them, and where the STRUM dataset sits among
them.

This strand carries the load for the epic's headline question, which is how the project can use
STRUM or other datasets to close an identified gap. Phase 4 maps gaps to datasets; that mapping
is only as good as the specifications collected here.

## Scope

Cover 5 categories.

### 1. Large EEG pretraining corpora

- Temple University Hospital EEG Corpus, Sleep-EDF, and other multi-thousand-hour sources used
  to pretrain the models in the `eeg-models` strand.
- Recording context: clinical versus laboratory, montage, sampling rate, population.
- License and access terms, since these determine whether the project could pretrain or
  continue pretraining rather than only fine-tune.

### 2. Small downstream benchmarks

- BCI Competition sets, motor imagery, event-related potential paradigms, and the workload and
  attention datasets that transfer papers report on.
- Participant counts, trials per participant, and class balance.
- Which of these the pretrained checkpoints have already been evaluated on, so the project can
  tell an established result from a novel one.

### 3. Dyadic, team, and hyperscanning recordings

- Public datasets with two or more simultaneously recorded participants.
- Synchronization method and its precision, which constrains any inter-brain analysis.
- Task structure, and whether labels are per-participant, per-dyad, or per-trial.

This category is where the project's setting either has public comparators or does not. If the
category comes back thin after a genuine search, that absence is itself a finding, and the
strand must record what was searched rather than quietly returning fewer entries.

### 4. Multimodal physiology datasets

- Datasets carrying synchronized EEG with electrocardiography, electrooculography,
  respiration, or electrodermal activity.
- Which peripheral channels are usable as signal versus recorded only for artifact rejection.
- Standard formats: Brain Imaging Data Structure for EEG (EEG-BIDS), European Data Format,
  and what tooling reads them.

### 5. STRUM and evaluation protocol conventions

- The STRUM data descriptor or documentation, carded as `type: dataset` from the primary source
  the user provides. Record participant count, channel montage, peripheral channels present,
  stimulus conditions and their markers, session structure, and total hours.
- Split conventions in the surrounding literature: subject-wise versus record-wise versus
  random splits, and documented cases of leakage.
- Metric conventions and how small-sample confidence intervals are reported, or not.

## Per-entry deliverable

Create folder `research/collection/datasets-benchmarks/<slug>/` containing:

- `card.md` with `strand: datasets-benchmarks`, and `type: dataset` for datasets, `type: paper`
  for protocol and critique papers, `type: standard` for format specifications.
- `source.md` always. For datasets with no paper, snapshot the canonical documentation or
  landing page. Set `pdf_status: not-applicable` in that case.
- `source.pdf` only when `meta.json.redistribution_ok` is true.
- `meta.json` with the access uniform resource locator, `retrieved_at`, license, and
  `redistribution_ok`. Record the data license, not only the paper license, in `notes`.
- BibTeX appended to `research/collection/datasets-benchmarks/datasets-benchmarks.bib`, with
  the citation key rewritten to equal the entry slug exactly. `opencite` generates keys such as
  `Xu2019ADT`; replace them, since the validator and the direction papers both key on the slug.
- One categorized line in `research/collection/datasets-benchmarks/INDEX.md`.

Every dataset card must record, in "Notable details", a fixed set of fields so Phase 3 can build
a comparison table without re-reading sources: participants, simultaneous participants per
recording, channels, sampling rate, peripheral channels, total hours, task, label type, license,
access route. Write `unknown` where the source does not say. Do not infer.

## Seed material

### Required entry: the STRUM dataset

Mullen T, Kothe C, Makeig S. STRUM: A New Dataset for Neuroergonomics Research. 2018 IEEE
International Conference on Systems, Man, and Cybernetics (SMC), pages 77 to 82.
Digital object identifier `10.1109/SMC.2018.00023`.

Card this as `type: dataset`, slug `strum-2018`, with the full fixed field set. Retrieval notes:
IEEE SMC proceedings are paywalled, so expect `redistribution_ok: false` and a markdown
extraction only, unless an author copy exists. Check the Swartz Center for Computational
Neuroscience and Intheon publication pages for an author accepted manuscript before settling for
extraction alone.

Record the citation count and check it against the claim below. At retrieval time Semantic
Scholar and OpenAlex both reported 2 citations. If that holds, it is a substantive finding rather
than trivia: it means there is almost no published modeling work on STRUM to compare against,
which changes what the project can claim as a baseline and belongs in the Phase 4 gap analysis.
Search explicitly for work citing this paper with `opencite cite "10.1109/SMC.2018.00023"
--direction backward` and card whatever it returns.

### Secondary seeds, inferred rather than given

These follow from the STRUM authorship and are worth checking, but they are the collector's
leads rather than confirmed dependencies. Verify relevance before carding; drop any that turn out
not to bear on STRUM.

- Kothe C and colleagues. The Lab Streaming Layer for Synchronized Multimodal Recording. bioRxiv,
  digital object identifier `10.1101/2024.02.13.580071`. Bears on category 3, since
  synchronization method and its precision constrain any inter-participant analysis, and STRUM
  was plausibly recorded with this toolchain. Confirm from the STRUM paper's methods rather than
  assuming it.
- Other datasets and recording infrastructure from the same authors, found by
  `opencite cite --direction both` from the two entries above.

### Remaining anchors

The user's broader seed list of papers and authors has not yet arrived, so categories 1 through 4
still rely on derived anchors: the pretraining corpora named by the `eeg-models` strand's
checkpoints, and the dataset registries PhysioNet, OpenNeuro, and the EEG-BIDS example
collection, mined for entries in categories 3 and 4.

Imported entries must set `imported_from: <relative path>` in `card.md`.

## Search strategy

Sources: arXiv, OpenAlex, Crossref, PubMed, plus direct registry browsing for PhysioNet and
OpenNeuro, which are not well covered by citation search. Record registry finds with the
registry landing page as `source_url`.

Window: no lower bound. Datasets remain current long after publication, and an older corpus can
still be the one a 2025 checkpoint was pretrained on.

Representative queries:

- `opencite search "EEG dataset data descriptor multimodal physiological" --max 25`
- `opencite search "hyperscanning dataset two participants simultaneous EEG" --max 25`
- `opencite search "EEG BIDS dataset open access workload" --max 20`
- `opencite search "cross-subject evaluation protocol EEG leakage benchmark" --max 20`
- `opencite lookup "<STRUM reference>"`
- `opencite cite "<pretraining corpus DOI>" --direction both`

Inclusion: the work releases data, specifies a data format, defines a benchmark protocol, or
critiques evaluation practice on these datasets.

Exclusion: private clinical datasets with no access route; datasets under 8 participants with no
peripheral channels and no dyadic structure, unless a checkpoint in the `eeg-models` strand
reports on them.

## Skills to use

- `opencite:opencite` for lookup, retrieval, conversion, and BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 18 entries across all 5 categories
- [ ] At least 3 entries per category
- [ ] The STRUM dataset is carded from its primary source, digital object identifier
      `10.1109/SMC.2018.00023`
- [ ] A backward citation search from the STRUM digital object identifier has been run, and
      `INDEX.md` records what it returned, including the case where it returns nothing usable
- [ ] Every `type: dataset` card records the full fixed field set, with `unknown` where the
      source is silent
- [ ] At least 4 datasets carrying synchronized EEG and at least one peripheral modality
- [ ] Category 3 either reaches 3 entries or `INDEX.md` records the queries run and what they
      returned
- [ ] Every entry folder has `card.md`, `source.md`, and `meta.json`
- [ ] Every entry has BibTeX in `datasets-benchmarks.bib`
- [ ] No more than 40 percent of entries marked `relevance: high`
- [ ] `python tools/validate_corpus.py` exits 0
- [ ] No prose synthesis and no dataset ranking; that is Phases 3 and 4

## Out of scope

- Model architectures and pretraining objectives. That is the `eeg-models` strand.
- Fusion methods. That is the `multimodal-biosignals` strand.
- Cognitive interpretation of the tasks a dataset uses. That is the `team-neuroergonomics`
  strand, which cards the construct while this strand cards the recording.
- Data engineering tooling beyond format readers.
- Recommending which dataset the project should use. Phase 4 decides that from this evidence.
