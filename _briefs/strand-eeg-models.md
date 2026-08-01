# Strand A, EEG representation learning and foundation models (Phase 1 brief)

**Goal:** populate `research/collection/eeg-models/` with at least 18 paper-cards covering
pretrained electroencephalography (EEG) models, what they were pretrained on, what is actually
released, and what evidence exists that they transfer to small downstream datasets.

This strand supplies the evidence base for the project's first two comparisons: a small
supervised-from-scratch model trained directly on STRUM, and an off-the-shelf pretrained model
fine-tuned on STRUM. The question this strand must be able to answer is narrow and empirical:
under what conditions does EEG pretraining help, and how often does it fail to beat a small
supervised baseline.

## Scope

Cover 5 categories. Breadth first across model families, depth on transfer evidence.

### 1. Pretraining objectives

- Masked signal or masked patch reconstruction, contrastive objectives, next-token prediction
  on discretized signal, and hybrid objectives.
- Tokenization and discretization choices: vector-quantized codebooks, patch embeddings, raw
  sample windows.
- What the objective assumes about channel montage, sampling rate, and recording length, since
  those assumptions determine whether STRUM data can be fed to the model at all.
- Theoretical or mechanistic motivation for applying sequence models to neural time series, kept
  strictly separate from evidence that they work. At most 2 entries, marked `relevance: medium` or
  lower. A card here explains why an architecture might suit neural data; it never establishes that
  a checkpoint transfers.

### 2. Architectures

- Transformer variants for EEG (LaBraM, EEGPT, Brant, EEGFormer, BIOT, NeuroGPT).
- Convolutional and recurrent predecessors that pretraining is measured against (BENDR,
  EEGNet, ShallowConvNet, DeepConvNet).
- Channel-agnostic and montage-flexible designs, and how they handle a channel set the model
  never saw during pretraining.

### 3. Released checkpoints and reproducibility

- Which models publish weights, under what license, at what parameter count.
- Input contract per checkpoint: expected sampling rate, window length, channel count and
  ordering, referencing and filtering assumptions, normalization.
- Known reproduction attempts, third-party reimplementations, and reported discrepancies with
  the original numbers.

### 4. Transfer and fine-tuning evidence

- Linear probe versus partial fine-tune versus full fine-tune comparisons.
- Behavior on small downstream datasets, few-subject regimes, and out-of-distribution montages
  or tasks.
- Cross-subject and cross-session generalization, and whether evaluation used subject-wise
  splits or leaked subjects across folds.

### 5. Negative and null results

- Studies where a small supervised model matched or beat a pretrained one.
- Critiques of EEG benchmark construction, label leakage, and inflated transfer claims.
- Scaling studies that report diminishing or absent returns from more pretraining data.

Category 5 is not optional. A corpus that contains only success stories cannot support a gap
analysis, and Phase 4 depends on knowing where pretraining does not pay.

## Per-entry deliverable

Create folder `research/collection/eeg-models/<slug>/` containing:

- `card.md` from `research/collection/_schema/paper-card.md`, with `strand: eeg-models` and
  `type` one of paper, tool, or platform.
- `source.md` always. Markdown extraction of the paper, or the canonical README for a released
  checkpoint or codebase.
- `source.pdf` only when `meta.json.redistribution_ok` is true, `pdf_status` is `archived`,
  and `pdf_license` is in the redistributable set listed in the card schema addendum.
- `meta.json` with digital object identifier (DOI) or uniform resource locator (URL),
  `retrieved_at`, license, `pdf_sha256` when a PDF is archived, and `redistribution_ok`.
- BibTeX appended to `research/collection/eeg-models/eeg-models.bib`, with the citation key
  rewritten to equal the entry slug exactly. `opencite` generates keys such as `Xu2019ADT`;
  replace them, since the validator and the direction papers both key on the slug.
- One categorized line in `research/collection/eeg-models/INDEX.md`.

Populate `modalities` with the electrode montage scale and signal types the work uses, and
`tags` with the pretraining objective, architecture family, and downstream task.

In "Notable details", always record: pretraining corpus and its total hours, parameter count,
input contract, and the single most informative transfer number with its baseline. A card
without a baseline number is not useful to Phase 3.

## Seed material

Supplied by the user. These are required entries, not suggestions.

- El Ouahidi Y, Lys J, Thölke P, Farrugia N, Pasdeloup B, Gripon V, Jerbi K, Lioi G. REVE: A
  Foundation Model for EEG, Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects.
  arXiv `2510.21585`, 2025. Slug `reve-2025`. The highest-value entry in the strand for category 2,
  because adapting to any setup is precisely the montage-flexibility question that determines
  whether STRUM data can be fed to a checkpoint at all. Record the exact mechanism by which it
  handles an unseen channel set, not merely the claim that it does.
- Yuan Z, Shen F, Li M, Yu Y, Wu F, Tan C, Yang Y. BrainWave: A Brain Signal Foundation Model for
  Clinical Applications. Slug `brainwave`. Identifier not yet resolved: `opencite` keyword search
  did not return it. Resolve it in Phase 2 by searching the arXiv listing directly or by exact
  title on OpenAlex, and record the identifier in `meta.json`. Do not guess an identifier.

- Muller L, Churchland PS, Sejnowski TJ. Transformers and cortical waves: encoders for pulling in
  context across time. Trends in Neurosciences, 2024. Digital object identifier
  `10.1016/j.tins.2024.08.006`. PubMed Central identifier `PMC11936488`. Slug
  `muller-2024-transformers-cortical-waves`.

  Category 1, under the theoretical-motivation line, and the only theory entry in the seed set. It
  argues an analogy between transformer attention over a sequence and cortical traveling waves
  carrying context over time. Card it as motivation and nothing more. It reports no transfer result,
  so it cannot support any claim about whether a pretrained model works on STRUM, and a direction
  paper that cites it as though it did would be making an argument the source does not make. State
  that limit explicitly in the card's "Open questions / limitations" section.

  Retrieval note, corrected during collection. An earlier version of this brief said that a standard
  author manuscript deposit takes `author-accepted-manuscript` and may be archived. The collecting
  agent checked and found the PubMed Central record is an NIHMS deposit carrying no license statement
  at all, with Europe PMC reporting `isOpenAccess: N` and `license: null`. That is structurally the
  same as the arXiv default: a grant running to the host, not to third parties. It was recorded
  `unknown`, markdown only, which is correct. Read the license off the record; deposit in a
  repository is not itself a license.

- Alexander DM, Ball T, Schulze-Bonhage A, van Leeuwen C. Large-scale cortical travelling waves
  predict localized future cortical signals. PLOS Computational Biology, 2019. Digital object
  identifier `10.1371/journal.pcbi.1007316`. PubMed Central identifier `PMC6894364`. Slug
  `alexander-2019-cortical-waves`. Published by PLOS under Creative Commons Attribution, so the PDF is
  archivable and `pdf_license: CC-BY-4.0` applies.

  The second and final entry on the theoretical-motivation line, which this fills. Note honestly on
  the card what it is: an empirical result about the spatiotemporal structure of cortical signals, not
  a theory paper and not transfer evidence. It is carded under a motivation line by a deliberate
  scoping decision to keep this thread small, so the card must state that its evidential weight here
  is limited to establishing that cortical signals carry predictable spatiotemporal structure. It
  cannot support any claim about whether a pretrained model captures that structure.

  The line is now at its cap. A further signal-structure paper cannot be added without reopening the
  scoping decision, which is a Phase 3 conversation and not a collection-time judgment.

Also anchor on the model families named in categories 2 and 3, then expand outward with
`opencite cite --direction both` from each resolved seed. Prefer the citation graph over keyword
search for categories 4 and 5, since null results rarely surface in citation-ranked keyword
queries.

### Leads surfaced while resolving the seeds

Found incidentally during seed lookup and recorded so they are not lost. Verify each before
carding. The first two are unusually valuable for category 5 and should be chased first.

- Lin and colleagues. The Identity Trap in EEG Foundation Models: A Diagnostic Audit. OpenAlex
  `W7164090340`.
- Zare. Stress-Testing EEG Foundation Models for Clinical Decoding: Dataset Identity and Targeted
  Negative Controls. OpenAlex `W7171748390`.

  Both appear to argue that these models can score well by recognizing which dataset a recording
  came from rather than by decoding the task. If that holds it bears directly on how this project
  must design its evaluation, and it belongs in Phase 4 whichever way the evidence falls.

- Wang and colleagues. CBraMod: A Criss-Cross Brain Foundation Model for EEG Decoding. Digital
  object identifier `10.48550/arxiv.2412.07236`.
- Guetschel and colleagues. Review of deep representation learning techniques for brain-computer
  interfaces. Digital object identifier `10.1088/1741-2552/ad8962`.

Imported entries must set `imported_from: <relative path>` in `card.md`.

## Search strategy

Sources: arXiv, OpenAlex, Crossref, PubMed. Semantic Scholar rate-limits without a key; set
`SEMANTIC_SCHOLAR_API_KEY` to restore it, otherwise expect that source to return nothing.

Window: 2022 onward. Admit earlier work when a later entry depends on it, for example BENDR
(2021) and EEGNet (2018) as the baselines transfer papers report against.

Note that `opencite search` ranks by citation count by default, which biases toward older work.
Pair every keyword query with `--sort` variation and with a `canonical` query, and treat the
citation graph as the primary discovery route.

Representative queries:

- `opencite canonical "EEG foundation model" --max 15`
- `opencite search "EEG self-supervised pretraining transfer" --max 25`
- `opencite search "masked EEG modeling large-scale pretraining" --max 25`
- `opencite search "EEG pretraining does not improve small dataset" --max 25`
- `opencite search "EEG deep learning subject-wise cross-validation leakage" --max 20`
- `opencite cite "<seed DOI>" --direction both`

Inclusion: the work either pretrains an EEG model on a corpus larger than its evaluation set,
or evaluates such a model on a downstream task, or critiques that practice.

Exclusion: single-dataset supervised models with no pretraining and no role as a transfer
baseline; brain-computer interface (BCI) application papers that use a pretrained model as a
black box without reporting a baseline comparison.

## Collection practice

Read `_briefs/collection-practice.md` before starting. It carries the working tool invocations, the
BibTeX verification requirement, the search trap that silently reports zero matches on converted
sources, and the rules for missing facts, self-contradicting sources, and strand-level fields. Every
item in it cost real time or nearly corrupted a card during the Phase 2 pilot.

## Skills to use

- `opencite:opencite` for DOI lookup, PDF retrieval, PDF to markdown conversion, BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 18 entries across all 5 categories
- [ ] At least 3 entries per category, and at least 3 in category 5 specifically
- [ ] Every checkpoint named on a `Checkpoints covered` line in a `datasets-benchmarks`
      benchmark-suite card has an entry in this strand. `uv run python tools/validate_corpus.py`
      warns for any that does not; the warning is the criterion, not a suggestion
- [ ] At least 6 distinct model families represented. This is a floor, not the test. It is a
      self-contained count, and a strand can satisfy it while omitting the model that wins a
      suite's primary protocol, which is exactly what happened on the first pass: BrainOmni,
      EEGConformer, FEMBA and LUNA were all named repeatedly in benchmark cards and carded by
      nobody. The coverage criterion above is what actually prevents that
- [ ] Every entry folder has `card.md`, `source.md`, and `meta.json`
- [ ] Every entry has BibTeX in `eeg-models.bib`
- [ ] `INDEX.md` fully populated with categorized one-liners
- [ ] No more than 40 percent of entries marked `relevance: high`
- [ ] Every category 4 card records a transfer number and the baseline it was measured against
- [ ] `uv run python tools/validate_corpus.py` exits 0
- [ ] No prose synthesis; that is Phase 3

## Out of scope

- Clinical seizure detection and sleep staging as applications, except where a checkpoint's
  only published transfer evidence is on those tasks.
- Magnetoencephalography, functional near-infrared spectroscopy (fNIRS), and functional
  magnetic resonance imaging models, except where a single paper covers EEG alongside them.
- Peripheral physiology models and fusion architectures. Those belong to the
  `multimodal-biosignals` strand.
- Dataset characterization beyond one line naming the pretraining corpus. Datasets are the
  `datasets-benchmarks` strand.
- Comparing or ranking entries against each other. Collection only.
