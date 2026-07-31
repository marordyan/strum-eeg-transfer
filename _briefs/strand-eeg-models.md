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
- `source.pdf` only when `meta.json.redistribution_ok` is true.
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

Provisional. The user is supplying a seed list of papers and authors; when it arrives, the
named entries below are replaced or extended and this section loses its provisional marking.

Until then, anchor on the model families named in categories 2 and 3, and expand outward with
`opencite cite --direction both` from each anchor once its DOI is resolved. Prefer the citation
graph over keyword search for category 4 and 5 entries, since null results rarely surface in
citation-ranked keyword queries.

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

## Skills to use

- `opencite:opencite` for DOI lookup, PDF retrieval, PDF to markdown conversion, BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 18 entries across all 5 categories
- [ ] At least 3 entries per category, and at least 3 in category 5 specifically
- [ ] At least 6 distinct model families represented
- [ ] Every entry folder has `card.md`, `source.md`, and `meta.json`
- [ ] Every entry has BibTeX in `eeg-models.bib`
- [ ] `INDEX.md` fully populated with categorized one-liners
- [ ] No more than 40 percent of entries marked `relevance: high`
- [ ] Every category 4 card records a transfer number and the baseline it was measured against
- [ ] `python tools/validate_corpus.py` exits 0
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
