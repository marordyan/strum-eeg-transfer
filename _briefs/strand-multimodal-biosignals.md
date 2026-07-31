# Strand B, Peripheral biosignals and multimodal fusion (Phase 1 brief)

**Goal:** populate `research/collection/multimodal-biosignals/` with at least 25 paper-cards
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

Supplied by the user. These are required entries, not suggestions.

- Li J, Chen N, Zhu H, Li G, Xu Z, Chen D. Incongruity-aware multimodal physiology signals fusion
  for emotion recognition. Information Fusion, 2023. Digital object identifier
  `10.1016/j.inffus.2023.102220`. Slug `li-2023-incongruity-fusion`. Categories 2 and 3. The
  incongruity framing is the useful part: it treats disagreement between modalities as information
  rather than noise, which is the mechanism by which peripheral signals could add value beyond a
  redundant copy of what the EEG already carries. Record how incongruity is operationalized and
  whether the ablation isolates it.
- Salam A, Alam F, Shah D, Rahman SU, Ali S, Tahir M. Improving cognitive stress classification via
  multimodal EEG and ECG fusion: gender differences in physiological response. Scientific Reports.
  Digital object identifier `10.1038/s41598-026-38356-3`. Slug `salam-eeg-ecg-stress`. Category 3,
  and the closest published analogue to this project's third comparison. Record the EEG-only arm,
  the combined arm, the split protocol, and the participant count. The gender-difference result
  also raises a subgroup-confound question worth carrying to Phase 4.
- Liu H, Lou T, Zhang Y, Wu Y, Xiao Y, and colleagues. EEG-Based Multimodal Emotion Recognition: A
  Machine Learning Perspective. Slug `liu-eeg-multimodal-emotion-review`. Identifier not yet
  resolved; resolve by exact title in Phase 2 and record it in `meta.json`. Do not guess an
  identifier. As a review it is a source of further entries for categories 2 and 3; mine its
  reference list rather than treating it as evidence on its own.
- Ha U, Lee Y, Kim H, Roh T, Bae J, Kim C. A Wearable EEG-HEG-HRV Multimodal System With
  Simultaneous Monitoring of transcranial Electrical Stimulation for Mental Health Management. Slug
  `ha-wearable-eeg-heg-hrv`. Identifier not yet resolved; resolve in Phase 2. Categories 1 and 5,
  and the only hardware-side entry in the seed set. It carries heart rate variability and
  hemoencephalography rather than the ECG and respiration this project has, so card what transfers
  at the level of acquisition and synchronization constraints, and mark it `relevance: low` if the
  modality set does not overlap enough to inform the STRUM design.

- Wang H, Jiang C, Liu G, Yuan J, Yu M, Ma X, Liu C, Xiao J, Zhang G. A Machine Learning Approach
  for Real-Time Detection of Inadequate Sedation Using Non-EEG Physiological Signals.
  Bioengineering, 2025. Digital object identifier `10.3390/bioengineering12101049`. Slug
  `wang-2025-sedation-non-eeg`. Published by a fully open-access publisher, so expect
  `pdf_license: CC-BY-4.0` and an archivable PDF.

  Categories 3 and 5, and it earns its place for a specific reason: it decodes a state from
  peripheral physiology with no EEG at all. Category 3 asks for EEG-only, physiology-only, and
  combined arms, and the physiology-only arm is the one the literature most often omits. This entry
  supplies it directly. Record which signals and which engineered features carry the decoding, the
  performance against chance, and whether evaluation held out participants.

  Note the scope tension: the out-of-scope section below excludes clinical endpoints, and sedation
  adequacy is one. The exclusion is amended for this case, because a clinical setting is where
  physiology-only decoding is most often reported and the endpoint is incidental to what the card
  contributes. Card the decoding evidence, not the clinical claim.

- Ahmad MI, Keller I, Robb DA, Lohan KS. A framework to estimate cognitive load using physiological
  data. Personal and Ubiquitous Computing, 2020. Digital object identifier
  `10.1007/s00779-020-01455-7`. Slug `ahmad-2020-cognitive-load-framework`. Categories 3 and 5.
  Cognitive load is the construct closest to what this project could plausibly decode beyond a
  stimulus label, so record how load was manipulated, how it was labelled, which physiological
  channels were used, and whether the framework was validated across participants. The
  `candidate-datasets` strand covers label validity; this strand covers the estimation
  method. Card it here, and cross-reference it there rather than carding it twice.
- Haque Y, Zawad RS, Rony CSA, Al Banna H, Ghosh T, Kaiser MS, Mahmud M. State-of-the-Art of Stress
  Prediction from Heart Rate Variability Using Artificial Intelligence. Slug
  `haque-hrv-stress-review`. Identifier not yet resolved; resolve by exact title in Phase 2 and
  record it in `meta.json`. Do not guess an identifier. Category 5, and the strand's reference point
  for what engineered heart rate variability features achieve before any learned encoder is
  introduced. As a review, mine its reference list for primary entries rather than treating its
  aggregate numbers as evidence.

- Wibirama S, Alfarozi SAI, Suhari AR, Fristiana AH, Nurlatifa H, Santosa PI. Classification of
  Cognitive Load Using Deep Learning Based on Eye Movement Indices. Slug
  `wibirama-cognitive-load-eye-movement`. Identifier not yet resolved; resolve by exact title in
  Phase 2 and record it in `meta.json`. Do not guess an identifier.

  Categories 4 and 5, and it sits on the strand's most useful fault line. Eye movement indices are
  what electrooculography measures, and the same ocular activity that this literature decodes as
  signal is what EEG pipelines routinely remove as artifact. If cognitive load is decodable from eye
  movement alone, then ocular artifact removal is discarding task-relevant information, and any gain
  this project sees from adding an electrooculography channel may be ocular rather than cortical.
  Record which indices carry the classification, whether they were derived from eye tracking or from
  electrooculography, and the performance against chance.

- Zeng X, Zhang X, Dong H, Bian G, de Albuquerque VHC, Wu W. Emotion effects on spatiotemporal
  brain-heart interactions with convergent cross mapping. Slug `zeng-brain-heart-ccm`. Identifier not
  yet resolved; resolve by exact title in Phase 2 and record it in `meta.json`. Do not guess an
  identifier.

  Categories 3 and 4, and it asks a sharper question than the fusion papers do. Convergent cross
  mapping tests directed coupling between two dynamical systems, so this is not fusion for
  classification but an attempt to establish whether cardiac and cortical activity drive each other.
  That bears directly on the project's third comparison: if the cardiac signal is largely downstream
  of the same central state the EEG already reflects, then adding it should buy little, and a measured
  gain would need another explanation. If the coupling is genuinely bidirectional or lagged, the
  peripheral channel may carry information the EEG does not.

  Record the direction and strength of coupling reported, the time scales involved, and whether the
  analysis controlled for shared task structure driving both signals.

- Schiecke K, Pester B, Feucht M, Leistritz L, Witte H. Convergent Cross Mapping: Basic concept,
  influence of estimation parameters and practical application. Slug `schiecke-ccm-methods`. Identifier
  not yet resolved; resolve by exact title in Phase 2 and record it in `meta.json`. Do not guess an
  identifier.

  A methods entry, category 5, and it is what makes the coupling results in this strand judgeable. If
  convergent cross mapping outcomes are sensitive to embedding dimension, lag, or library size, then a
  reported coupling direction is a function of analysis choices as much as of physiology. Record which
  parameters matter, how much, and what the paper recommends. Phase 3 needs this to weigh
  `zeng-brain-heart-ccm` rather than take its direction claim at face value.

  Related and already resolved, from the same group: Schiecke K and colleagues. Brain-heart
  interactions considering complex physiological data: processing schemes for time-variant,
  frequency-dependent, topographical and statistical examination of directed interactions by convergent
  cross mapping. Physiological Measurement, 2019. Digital object identifier
  `10.1088/1361-6579/ab5050`. Slug `schiecke-2019-brain-heart-ccm`. This applies the method to
  brain-heart interaction directly and is closer to the project's question than a generic methods
  treatment, so card it as well rather than treating the two as duplicates.

Convergent cross mapping now appears in three seed entries. Treat it as a recurring method in the
corpus rather than an incidental one: the applications belong to categories 3 and 4, the methods and
parameter-sensitivity work to category 5, and Phase 3 should be able to state whether the coupling
findings across these papers agree once analysis choices are accounted for.

Also anchor on the model families in category 1 and on affect-recognition and workload-estimation
datasets that ship synchronized EEG and peripheral channels, since those are where ablation arms
are most often reported. Expand with `opencite cite --direction both` from each resolved seed.

### Lead surfaced while resolving the seeds

- Lee and colleagues. A Comprehensive Review of Biosignal Foundation Models, 2025. Digital object
  identifier `10.36227/techrxiv.176369849.97173246/v1`. Bears on category 1 and is a likely source
  of further entries. Note it is a preprint on a server that does not peer review, so weigh it as
  a map of the field rather than as evidence.

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

## Collection practice

Read `_briefs/collection-practice.md` before starting. It carries the working tool invocations, the
BibTeX verification requirement, the search trap that silently reports zero matches on converted
sources, and the rules for missing facts, self-contradicting sources, and strand-level fields. Every
item in it cost real time or nearly corrupted a card during the Phase 2 pilot.

## Skills to use

- `opencite:opencite` for retrieval, conversion, and BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 25 entries across all 5 categories
- [ ] At least 4 entries per category
- [ ] At least 8 entries in category 3 that report a genuine EEG-only versus combined comparison
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
- Cardiology, sleep medicine, and critical-care prediction as clinical endpoints, with two
  exceptions: the paper is the primary reference for a peripheral foundation model, or the clinical
  setting is the only one in which a physiology-only decoding arm is reported, as with the sedation
  entry in Seed material. In the second case, card the decoding evidence and leave the clinical
  claim alone.
- Camera-based or contactless physiology estimation.
- Comparing or ranking entries against each other. Collection only.
