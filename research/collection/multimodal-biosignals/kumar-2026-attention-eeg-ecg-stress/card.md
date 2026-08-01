---
slug: kumar-2026-attention-eeg-ecg-stress
type: paper
strand: multimodal-biosignals
year: 2026
authors: [Kumar, Bala Krishnan, Yadav, Saini, Chakrabarti, Balodi, Shwetha]
venue: Scientific Reports 16:15188
doi: 10.1038/s41598-026-44499-0
url: https://doi.org/10.1038/s41598-026-44499-0
license: CC BY 4.0
modalities: [eeg, ecg]
tags: [attention-fusion, transfer-learning, scalogram, wesad, case, cross-dataset, ablation, early-fusion, late-fusion, dataset-provenance-error]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

Reports the full ablation this strand asks for — EEG-only 82.3%, ECG-only 85.6%, early fusion
89.2%, late fusion 91.4%, attention fusion 95.7% — but attributes EEG recordings to WESAD and CASE,
two public datasets that do not contain EEG, so the provenance of the EEG arm cannot be verified
from the paper.

## Summary

The paper proposes a three-backbone transfer-learning framework for stress detection from EEG and
ECG. EEG is band-pass filtered 0.5–45 Hz with a zero-phase Butterworth filter, common-average
re-referenced, ICA-cleaned, decomposed into theta/alpha/beta bands, converted to Morlet continuous
wavelet-transform scalograms and stacked into a 128 x 128 x 3 image; that image is passed in
parallel through VGG16 (14.7 M parameters), EfficientNetB0 (5.3 M) and ResNeXt50 (25 M), whose
outputs are concatenated into a 1536-dimensional vector and compressed to 512 dimensions. ECG
contributes heart-rate-variability features together with raw signal. An attention layer weights
the two streams. Reported data are WESAD (stated as 15 participants) and CASE (stated as 20),
described in the abstract as "35 subjects" in neutral, tense and positive states. The three-class
accuracy is 95.7%, against 82.3–84.1% for EEG-only backbones and 79.8–85.6% for ECG-only. Ablations
remove each backbone and the attention layer; cross-dataset transfer gives 88.3% (WESAD to CASE)
and 86.7% (CASE to WESAD) against 94.1% combined-to-combined. The full model has 42.7 M parameters
and 18.5 ms inference latency per sample.

## Relevance to the review

On its face this is exactly the ablation the project's third comparison needs: one table with
EEG-only, ECG-only, two naive fusion baselines and the proposed fusion, all on the same data, plus
an attention-removal ablation isolating the fusion mechanism (0.905 without attention versus 0.957
with). The claimed peripheral contribution is large, +11.6 points over the best EEG-only backbone
and +13.4 over the weakest.

The reason this entry is marked `relevance: low` despite that is a data-provenance problem serious
enough to make the EEG arm uninterpretable. The paper states that WESAD "consists of synchronised,
high-resolution EEG and ECG recordings for 14 channels" at 700 Hz, and that CASE "offers an EEG
with a maximum of 32 EEG electrodes". Neither public dataset distributes EEG: WESAD's chest
RespiBAN carries ECG, EDA, EMG, respiration, temperature and acceleration (700 Hz is its sampling
rate, not an EEG rate), and CASE carries ECG, blood volume pulse, EMG, galvanic skin response,
respiration and skin temperature alongside continuous affect annotation, with no EEG in either
release. Whatever the EEG stream in this paper is, it
is not documented by the datasets named. Since the EEG-only arm is the denominator of the claimed
peripheral gain, the gain cannot be trusted either.

The entry is still worth keeping for two reasons. It is a clean instance of the architecture family
this project might use — frozen pretrained image backbones over a time-frequency representation,
with a learned attention weighting over modality streams and a head on top — with parameter counts
and latency reported. And it is a cautionary example for Phase 3 of how a well-formed ablation
table can sit on top of an unverifiable dataset claim, which is a failure mode a synthesis reading
only the tables would not catch.

## Notable details

- **EEG-only number**: 0.823 (VGG16), 0.841 (EfficientNetB0), 0.836 (ResNeXt50) accuracy, with
  F1 0.809 / 0.828 / 0.821. The paper summarises this as EEG alone "could not exceed an average
  maximum accuracy of 84.1%".
- **Peripheral-only number**: ECG 0.798 with HRV features, 0.856 with raw signal plus CNN.
- **Combined number**: proposed multimodal 0.957 accuracy, F1 0.953, precision 0.956, recall 0.951.
  Early fusion 0.892, late (average) fusion 0.914, attention removed 0.905.
- **Split protocol**: the test set is "the remaining 10%, obtained from three individuals whose
  data were entirely excluded from both training and validation phases to prevent data leakage",
  i.e. a subject-wise held-out test set of three participants. Stratification of the training and
  validation split is by dataset and gender.
- **Participants**: 35 stated in the abstract; the body gives WESAD as 15 and CASE as 20, which
  sums to 35. (CASE as published has 30 participants, so the 20 is unexplained.)
- **Backbone ablation**: removing ResNeXt50 costs least (0.934), removing VGG16 next (0.931),
  removing EfficientNetB0 most (0.928); removing the attention layer costs most of all (0.905).
- **Cross-dataset**: WESAD to CASE 88.3%, CASE to WESAD 86.7%, combined-to-combined 94.1%. The
  authors read the small drop as evidence of transferable representations.
- **Cost**: proposed 42.7 M parameters, 3.2 min per training epoch, 18.5 ms inference per sample,
  against EEG-only VGG16 at 14.7 M / 1.8 min / 12.3 ms and ECG-only raw CNN at 8.3 M / 1.2 min /
  8.7 ms. The paper frames the trade as "a 5–10% increase in accuracy from multimodal fusion
  against a 2–3x increase in computational cost".
- Epochs are 10 s non-overlapping and are "treated as an independent sample"; ICA is applied to
  remove eye movement, muscle and cardiac interference from the EEG stream. Note that removing
  cardiac interference from EEG while using ECG as the second modality is a design choice worth
  flagging, since it is the one preprocessing step that would suppress the shared component.

## Open questions / limitations

- **The dataset claim is the central problem.** WESAD and CASE, as publicly released, contain no
  EEG. The paper gives no alternative source, no acquisition description of its own, and no data
  availability statement reconciling the discrepancy in the extracted text. Everything downstream
  of the EEG stream is therefore unverifiable.
- Participant arithmetic: the abstract's "35 subjects" matches 15 + 20 from the body, but CASE is
  a 30-participant dataset. Either a subset was used and not described, or the count is wrong.
- A three-subject test set is too small to support a 95.7% point estimate. No confidence interval,
  no repeated-split variance and no per-subject breakdown are reported.
- No chance level or class balance is given for the three-state problem, so the margin over a
  trivial baseline is unstated.
- The comparison arms are not equal-effort. The EEG-only arms are single backbones; the fused model
  is an ensemble of three backbones plus attention. Part of the 95.7% is ensembling, not fusion,
  and the backbone-ablation table (0.928–0.934 with two backbones) suggests the ensemble
  contributes 2–3 points on its own.
- The paper's own discussion invokes "the neurovisceral model" to explain the gain, but nothing in
  the analysis distinguishes a genuine central-peripheral complementarity from the ECG arm simply
  carrying the task-condition signal better than the EEG arm does — the ECG-only model (0.856)
  already beats every EEG-only model.
- Writing quality is uneven in a way that matters for reliability: the methods describe ICA twice,
  in steps 2/4 of the EEG pipeline, with different wording, and one sentence refers to "the
  undetectable model".

## Citations

Primary: `kumar-2026-attention-eeg-ecg-stress`

- `salam-eeg-ecg-stress` — the same modality pair and construct with engineered features rather
  than transfer learning, and a comparable claimed gain.
- `ding-2025-cross-attention-fusion` — cross-attention fusion of EEG with peripheral signals,
  without a unimodal arm.
- `li-2023-incongruity-fusion` — the cross-modal transformer approach to the same fusion problem.
- `azad-2025-construction-noise` — a fusion study whose subject-independent protocol and near-null
  gain make a useful contrast to this paper's three-subject test set.
- Schmidt et al., "Introducing WESAD, a multimodal dataset for wearable stress and affect
  detection" — the dataset whose modality list this paper misstates; dataset characterization
  belongs to the `datasets-benchmarks` strand.
