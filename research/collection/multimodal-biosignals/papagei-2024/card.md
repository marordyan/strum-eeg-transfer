---
slug: papagei-2024
type: paper
strand: multimodal-biosignals
year: 2024
authors: [Pillai, Spathis, Kawsar, Malekzadeh]
venue: ICLR 2025 (arXiv preprint 2410.20542)
doi: 10.48550/arXiv.2410.20542
url: https://arxiv.org/abs/2410.20542
license: CC BY-NC-ND 4.0 (arXiv posting)
modalities: [ppg]
tags: [foundation-model, photoplethysmography, morphology-supervision, resnet-encoder, released-weights, out-of-domain-generalization, skin-tone-bias, feature-extractor, parameter-efficiency, 125hz-input-contract]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

The first open foundation model for photoplethysmography: a ResNet-style encoder pretrained on
20 million unlabelled segments (57,641 hours) with a morphology-based supervision signal instead
of instance-contrastive learning, released as weights and explicitly positioned as an encoder for
multimodal models.

## Summary

PaPaGei addresses three limitations the authors identify in PPG machine learning — single-device
datasets, insufficient evaluation of out-of-domain generalisation, and no publicly available
models. It is pretrained on three public sources: VitalDB (intraoperative finger PPG at 500 Hz,
5,866 participants, 6,248,100 segments, 17,355 hours), the MIMIC-III waveform matched subset (ICU
finger-tip PPG at 125 Hz) and the MESA sleep sub-study (polysomnography finger-tip PPG at 256 Hz),
totalling 13,517 participants, 20,751,206 segments and 57,641 hours. Preprocessing band-passes at
0.5–12 Hz, segments, removes segments more than 25% flat, z-score normalises and resamples
everything to 125 Hz, the lowest rate among the pretraining sources. The encoder is an 18-block
ResNet-style CNN starting at filter size 32 and doubling every four blocks, with a single
fully-connected projection to a 512-dimensional embedding; a PaPaGei-S variant adds an expert
block of three parallel two-layer fully-connected networks producing a 128-dimensional embedding.
The representation-learning objective uses domain knowledge of PPG signal morphology across
individuals rather than standard contrastive augmentation. Evaluation covers 20 tasks from 10
datasets — cardiovascular health, sleep disorders, pregnancy monitoring and wellbeing — including
held-out out-of-domain datasets, and reports improvements of 6.3% on classification and 2.9% on
regression metrics in at least 14 tasks, while outperforming models 70 times larger. The paper
also benchmarks robustness across Fitzpatrick skin tones.

## Relevance to the review

This strand needs a concrete answer to "what does a released peripheral-signal foundation model
actually give you", and PaPaGei is the cleanest available instance for the optical channel. Four
things matter for the project's third comparison.

The input contract is narrow and fixed: single-channel PPG resampled to 125 Hz, band-passed
0.5–12 Hz, z-scored, with flat-segment rejection. Any peripheral encoder bolted onto an EEG
pipeline inherits a resampling and filtering stage of its own, at a rate unrelated to the EEG
rate, which is the concrete form the brief's "modality-specific sampling rates" problem takes.

The paper explicitly frames the model as "both a feature extractor and an encoder for multimodal
models", which is the configuration this project would use — frozen peripheral encoder, head on
top — rather than end-to-end training. That framing is a claim the paper does not itself test:
no multimodal experiment appears in the evaluation.

The parameter-efficiency result cuts against the assumption that a bigger peripheral encoder is
better. Outperforming models 70 times larger on the same tasks suggests the useful capacity for a
single-channel peripheral signal is small, which bears on whether a learned peripheral encoder is
worth the complexity relative to the engineered features in category 5.

The skin-tone benchmark is the only fairness evaluation in this strand and is directly relevant to
a dyadic study with a heterogeneous participant pool: PPG amplitude depends on optical absorption,
so a peripheral channel that works unevenly across participants introduces a subgroup confound of
exactly the kind `salam-eeg-ecg-stress` runs into with sex.

STRUM as described carries ECG rather than PPG, so this entry is context for the model family
rather than a direct dependency; hence `relevance: medium`.

## Notable details

- **Pretraining corpus**: 13,517 participants, 20,751,206 segments, 57,641 hours across VitalDB
  (5,866 participants, 6,248,100 segments, 17,355 hours), MIMIC-III waveform matched subset, and
  the MESA sleep sub-study.
- **Native sampling rates of the sources**: VitalDB 500 Hz, MIMIC-III 125 Hz, MESA 256 Hz;
  everything resampled down to 125 Hz.
- **Input contract**: single-channel PPG; Chebyshev-style band-pass with cut-offs at 0.5 Hz and
  12 Hz; flat-segment rejection when more than 25% of a segment is flat; z-score normalisation;
  resample to 125 Hz. Segment lengths of 60 s are used, following prior wearable-PPG work.
- **Architecture**: 18 convolutional blocks, initial filter size 32 doubling every 4 blocks,
  single fully-connected projection to 512 dimensions. PaPaGei-S adds an expert block of three
  parallel two-layer FCNNs giving a 128-dimensional embedding. PaPaGei-P uses augmentations
  including cropping (p = 0.50), negation (0.20) and flipping.
- **Objective**: representation learning that "leverages domain knowledge of PPG signal morphology
  across individuals", presented as an alternative to traditional contrastive learning.
- **Reported gains**: 6.3% on classification metrics and 2.9% on regression metrics in at least 14
  of 20 tasks, against state-of-the-art time-series foundation models (Chronos, Moment) and
  self-supervised baselines (SimCLR, BYOL, TF-C) plus PPG-specific comparators (REGLE, EAM).
- **Evaluation set**: 20 tasks across 10 datasets, with some datasets held out entirely
  (out-of-domain) and held-out test sets retained for the pretraining datasets. Tasks include ICU
  admission and operation type (VitalDB), mortality (MIMIC-III), smoking status and two
  apnoea-hypopnoea indices (MESA), pregnancy stage and gestational age (nuMom2B), systolic and
  diastolic blood pressure on a skin-tone-stratified dataset (VV, 231 subjects), blood pressure,
  average heart rate and hypertension (PPG-BP, 219 subjects), and sleep-disordered breathing
  (SDB, 146 subjects).
- **Bias benchmark**: results stratified over the six-level Fitzpatrick skin tone scale for blood
  pressure estimation, offered as "a benchmark for bias evaluation in future models".
- **Release**: the paper is positioned as the first *open* PPG foundation model; weights and code
  are released. The licence attached to the released weights is not stated in the extracted text,
  which is the same gap the `eeg-models` strand records for its checkpoints.

## Open questions / limitations

- Every pretraining source is clinical or laboratory finger-tip PPG (surgery, ICU,
  polysomnography). Wrist-worn consumer PPG under motion — the setting the paper motivates itself
  by — is not in the pretraining corpus, and the paper's own introduction notes that PPG is
  "susceptible to noise and motion artifacts".
- The multimodal-encoder claim is asserted, not demonstrated. There is no experiment in which
  PaPaGei embeddings are combined with another modality, so the strand cannot say what it
  contributes on top of an EEG embedding.
- Resampling everything to 125 Hz to match the lowest-rate source discards information present in
  the 500 Hz and 256 Hz recordings. No ablation reports the cost.
- The 6.3% and 2.9% figures are averaged improvements over "at least 14 tasks", which leaves up to
  six tasks where the model does not improve; the extraction does not preserve which.
- No skin-tone result is quoted on this card: the detailed skin-tone figure (Figure 26) converts to
  character soup in the markdown extraction and the numbers were not recoverable without reading
  the PDF figure directly.
- Licence for the released weights is unrecorded, which matters for whether this project could use
  them.
- The evaluation is dominated by slow physiological and clinical endpoints (blood pressure, apnoea
  index, gestational age, mortality). Nothing tests a stimulus-locked, sub-minute cognitive
  contrast, which is the regime this project needs.

## Citations

Primary: `papagei-2024`

- `mckeen-2025-ecg-fm` — the equivalent open foundation model for the cardiac electrical channel,
  with a comparable release-and-benchmark posture.
- `lee-2025-biosignal-fm-review` — the survey that situates PaPaGei among biosignal foundation
  models generally.
- `haque-hrv-stress-review` — the engineered-feature baseline a learned peripheral encoder has to
  beat.
- `ha-wearable-eeg-heg-hrv` — the acquisition-side constraints on optical sensing in a head-worn
  device.
- Abbaspourazad et al. (2023) — the large-scale wearable PPG and ECG self-supervised work whose
  segment length and EfficientNet-style encoder choice PaPaGei references.
