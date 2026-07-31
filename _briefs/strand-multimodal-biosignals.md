# Strand B, Peripheral biosignals and multimodal fusion (Phase 1 brief)

**Goal:** populate `research/collection/multimodal-biosignals/` with at least 18 paper-cards
covering models for non-electroencephalography (non-EEG) biosignals and architectures that fuse
them with EEG, with priority on evidence that isolates what the peripheral channel contributes.

This strand supplies the evidence base for the project's third comparison: a fine-tuned EEG
model plus peripheral physiology features. The question it must answer is whether peripheral
signals add decodable information beyond EEG, or whether reported gains are explained by
artifact leakage, task confounds, or the peripheral channel proxying for the same construct the
EEG already carries.

## Scope

Cover 5 categories.

### 1. Single-modality foundation models for peripheral signals

- Electrocardiography (ECG) models and their pretraining corpora.
- Photoplethysmography (PPG) and wearable models (for example PaPaGei and successors).
- Respiration, electrodermal activity (EDA), and electrooculography (EOG) models, including
  cases where no foundation model exists and only feature-engineering pipelines do.
- What is released: weights, license, input contract, sampling rate assumptions.

### 2. Fusion architectures

- Early fusion on raw or windowed signals, intermediate fusion on embeddings, late fusion on
  per-modality predictions, and cross-attention designs.
- Handling of modality-specific sampling rates and of missing or corrupted channels.
- Whether the fusion model is trained end to end or bolts a head onto frozen encoders, which is
  the configuration this project would actually use.

### 3. Ablations that isolate the peripheral contribution

- Studies reporting EEG-only, physiology-only, and combined performance on the same split.
- Modality dropout and permutation tests.
- Effect sizes: how large the combined-minus-EEG-only gain is, and whether it survives
  subject-wise evaluation.

Category 3 is the strand's center of gravity. An entry that reports only combined performance,
with no EEG-only arm, cannot answer the project's question and should be marked
`relevance: low` unless it contributes to another category.

### 4. Artifact versus signal

- Ocular and cardiac artifact in EEG: how it is removed, and what removal costs.
- Evidence that EOG or ECG channels carry task information rather than nuisance, and evidence
  for the reverse, where apparent physiological decoding was traced to artifact or to a motion
  confound.
- Interaction with the epoching choices this project will make, since stimulus-locked epochs
  can align with blink and swallow patterns produced by the stimulus itself.

### 5. Classical physiology feature baselines

- Heart rate variability, respiratory sinus arrhythmia, pupil and blink metrics, and EDA phasic
  or tonic decomposition as engineered features.
- Reference implementations (for example NeuroKit2, HeartPy, BioSPPy) and their validation.
- Cases where engineered features matched or beat learned representations, which sets the bar
  for whether a learned peripheral encoder is worth the complexity.

## Per-entry deliverable

Create folder `research/collection/multimodal-biosignals/<slug>/` containing:

- `card.md` with `strand: multimodal-biosignals` and `type` one of paper, tool, or platform.
- `source.md` always; `source.pdf` only when `meta.json.redistribution_ok` is true, `pdf_status` is `archived`,
  and `pdf_license` is in the redistributable set listed in the card schema addendum.
- `meta.json` with digital object identifier (DOI) or uniform resource locator (URL),
  `retrieved_at`, license, `pdf_sha256` when archived, and `redistribution_ok`.
- BibTeX appended to `research/collection/multimodal-biosignals/multimodal-biosignals.bib`,
  with the citation key rewritten to equal the entry slug exactly. `opencite` generates keys
  such as `Xu2019ADT`; replace them, since the validator and the direction papers both key on
  the slug.
- One categorized line in `research/collection/multimodal-biosignals/INDEX.md`.

Populate `modalities` with the exact signals used, spelled consistently as `eeg`, `ecg`, `ppg`,
`eog`, `eda`, `resp`, so Phase 3 can build a modality-by-task matrix mechanically.

In "Notable details", always record for category 3 entries: the EEG-only number, the combined
number, the split protocol, and the number of participants. Absent any of those, say so
explicitly rather than omitting the line.

## Seed material

Provisional, pending the user's seed list of papers and authors.

Until it arrives, anchor on the model families in category 1 and on affect-recognition and
workload-estimation datasets that ship synchronized EEG and peripheral channels, since those
are where ablation arms are most often reported. Expand with
`opencite cite --direction both` from each anchor.

Imported entries must set `imported_from: <relative path>` in `card.md`.

## Search strategy

Sources: arXiv, OpenAlex, Crossref, PubMed. Semantic Scholar rate-limits without a key.

Window: 2022 onward, with earlier work admitted for category 5 baselines and for artifact
methodology that later work still cites as current practice.

Representative queries:

- `opencite canonical "ECG foundation model" --max 15`
- `opencite canonical "PPG wearable foundation model" --max 15`
- `opencite search "EEG peripheral physiology multimodal fusion workload" --max 25`
- `opencite search "multimodal physiological signals ablation unimodal comparison" --max 25`
- `opencite search "ocular artifact EEG task related information confound" --max 20`
- `opencite search "heart rate variability features versus deep learning affect" --max 20`
- `opencite cite "<seed DOI>" --direction both`

Inclusion: the work models a non-EEG biosignal at scale, fuses one with EEG, isolates a
peripheral contribution by ablation, or establishes an engineered-feature baseline.

Exclusion: consumer wearable stress or recovery products with no published evaluation; medical
diagnosis from ECG alone with no representation-learning or transfer angle.

## Skills to use

- `opencite:opencite` for retrieval, conversion, and BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 18 entries across all 5 categories
- [ ] At least 3 entries per category
- [ ] At least 5 entries in category 3 that report a genuine EEG-only versus combined comparison
- [ ] At least 2 entries in category 4 arguing that a reported physiological effect was artifact
      or confound
- [ ] Every entry folder has `card.md`, `source.md`, and `meta.json`
- [ ] Every entry has BibTeX in `multimodal-biosignals.bib`
- [ ] `INDEX.md` fully populated with categorized one-liners
- [ ] No more than 40 percent of entries marked `relevance: high`
- [ ] `modalities` uses the controlled spellings listed above
- [ ] `uv run python tools/validate_corpus.py` exits 0
- [ ] No prose synthesis; that is Phase 3

## Out of scope

- EEG-only pretraining and architecture work. That is the `eeg-models` strand.
- Dataset characterization beyond naming which signals a dataset carries. That is the
  `datasets-benchmarks` strand.
- Cardiology, sleep medicine, and critical-care prediction as clinical endpoints, except where
  the paper is the primary reference for a peripheral foundation model.
- Camera-based or contactless physiology estimation.
- Comparing or ranking entries against each other. Collection only.
