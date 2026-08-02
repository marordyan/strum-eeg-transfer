---
slug: angkan-2024-invehicle-cognitive-load
type: paper
strand: multimodal-biosignals
year: 2024
authors: [Angkan, Behinaein, Mahmud, Bhatti, Rodenburg, Hungler, Etemad]
venue: IEEE Transactions on Intelligent Transportation Systems 25(6)
doi: 10.1109/TITS.2023.3345846
url: https://arxiv.org/abs/2304.04273
license: CC BY-NC-SA 4.0 (arXiv posting of the accepted version)
modalities: [eeg, ecg, eda, eog]
tags: [cl-drive, driving-simulator, cognitive-load, leave-one-subject-out, modality-grid, hand-crafted-features, raw-signal, vgg, resnet, xgboost, subjective-labels]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

The only entry in this strand that reports a full modality grid — EEG alone, EEG with each of
three peripheral channels, and every combination — under both record-wise and leave-one-subject-out
evaluation, and the pattern is monotone: each added channel helps a little, all three together
help most, and the whole four-modality gain over EEG alone is about 6 points under LOSO.

## Summary

The paper introduces CL-Drive, a driver cognitive-load dataset of 21 subjects recorded in an
immersive vehicle simulator across nine driving scenarios of increasing complexity, three minutes
each, with each driver self-reporting cognitive load on a PAAS scale every ten seconds. Recorded
signals are EEG, ECG, electrodermal activity and eye tracking (gaze). The authors then benchmark
thirteen models — nine classical machine-learning models (AdaBoost, decision tree, naive Bayes,
k-nearest neighbours, linear discriminant analysis, random forest, SVM, XGBoost, multilayer
perceptron) and four deep models (VGG-style and ResNet-style networks, each on hand-crafted
features and on raw signals) — across eight modality subsets, two label granularities (binary and
ternary) and two evaluation criteria (10-fold and leave-one-subject-out). This yields four full
accuracy/F1 tables. Peak accuracy is 83.67% (XGBoost, all four modalities, 10-fold binary) and
74.08% (XGBoost, all four, 10-fold ternary). Under LOSO the four-modality means fall to 67.04%
(binary) and 47.80% (ternary).

## Relevance to the review

This is the strand's reference grid for "how much does each peripheral channel add on top of EEG",
because the modality axis and the evaluation axis are crossed rather than confounded. Three things
transfer directly to the project's third comparison.

First, the gain is real but small and roughly additive: averaged over all thirteen models, LOSO
binary accuracy goes 61.20% (EEG) → 63.95% (EEG+ECG) → 64.04% (EEG+EDA) → 64.25% (EEG+gaze) →
67.04% (all four). No single peripheral channel dominates, and no pairing is worth more than about
3 points on its own. That is a very different picture from `salam-eeg-ecg-stress`'s +12.6 points
and much closer to the near-null in `azad-2025-construction-noise`.

Second, the split protocol costs more than the modalities buy. Moving from 10-fold to LOSO on the
same four-modality input drops binary accuracy from 74.78% to 67.04% and ternary from 60.90% to
47.80% — a larger swing than the entire EEG-to-all-four gain. Any project reporting a fusion gain
under record-wise folds is reporting a number smaller than its own split-protocol artifact.

Third, the ranking of model families inverts between splits. Under 10-fold the best models are
gradient boosting on hand-crafted features; under LOSO ternary the best are the deep networks on
*raw* signals (ResNet-raw EEG alone reaches 58.13%, above every classical model's four-modality
score). A project choosing an architecture on record-wise folds would pick the wrong one for
cross-subject deployment.

## Notable details

- **EEG-only number**: LOSO binary mean across models 61.20% (F1 52.14); LOSO ternary mean 41.59%
  (F1 34.28). 10-fold binary mean 67.72%; 10-fold ternary mean 51.78%. Best single model on EEG
  alone: random forest 77.41% (10-fold binary, with XGBoost second at 77.38%), XGBoost 64.49%
  (10-fold ternary), VGG-features 70.70% (LOSO binary), ResNet-raw 58.13% (LOSO ternary).
- **Combined number** (EEG + ECG + EDA + gaze): LOSO binary mean 67.04% (F1 62.02); LOSO ternary
  mean 47.80% (F1 43.02). 10-fold binary mean 74.78%; 10-fold ternary mean 60.90%. Best single
  model on all four modalities: XGBoost 83.67% (10-fold binary) and 74.08% (10-fold ternary);
  VGG-features 75.52% (LOSO binary, with XGBoost at 71.48%); VGG-raw 63.56% (LOSO ternary, with
  ResNet-raw at 61.55%).
- **Correction, Phase 4 audit — which model is best is not XGBoost everywhere.** An earlier version
  of this card gave "XGBoost 77.38% (10-fold binary)" as the best EEG-alone result and "XGBoost …
  71.48% (LOSO binary)" as the best four-modality result. Table VIII's EEG column has random forest
  at 77.41%, above XGBoost's 77.38%; Table IX's four-modality column has VGG (feat.) at 75.52%,
  well above XGBoost's 71.48%. The paper's own Section V says so directly: "In Table IX, for the
  binary LOSO evaluation scheme, we observe that the highest accuracy of 76.17% is obtained by the
  VGG-style network trained with features. This accuracy is obtained using 3 modalities, namely
  EEG, ECG and EDA." The correction reinforces the card's third argument rather than weakening it:
  gradient boosting wins under 10-fold and deep networks win under LOSO.
- **Peripheral-only number**: *not reported.* Every one of the eight modality subsets includes
  EEG, so there is no physiology-only arm. This is the paper's one structural gap for category 3.
- **Split protocol**: both 10-fold cross-validation and leave-one-subject-out, reported in full
  and separately, for both label granularities.
- **Participants**: 21.
- **Labels**: subjective PAAS cognitive-load self-report every 10 s, binarised and trinarised.
  Ground truth is therefore self-report, not a task-difficulty proxy — which is a strength for
  construct validity and a weakness for label noise.
- **Task**: nine scenarios of increasing complexity, 3 minutes each, including night driving and
  highway conditions; scenario 0 is an orientation block.
- Per-modality feature sets are tabulated (Table V): EEG 40 features (PSD absolute, mean, maximum,
  minimum and median power; spectral entropy; Hjorth mobility and complexity; Lempel-Ziv
  complexity; Higuchi fractal dimension; and raw-signal mean, minimum, maximum, median, variance
  and standard deviation), ECG 53, EDA 30, gaze 32. An earlier version of this card listed only the
  first three EEG families and so under-described the set.
- **Segmentation**: each 3-minute scenario is cut into 18 non-overlapping 10 s segments, aligned to
  the 10 s self-report interval. Segments with missing EEG (Bluetooth dropouts of about 30 s) were
  excluded rather than imputed.
- Two of the peripheral channels in the grid are the ones this project has (ECG, and gaze as an
  eye-movement proxy for EOG); EDA is not in the STRUM set as far as this strand knows.

## Open questions / limitations

- No physiology-only arm, so the paper cannot say whether the peripheral channels carry the
  cognitive-load signal independently or only sharpen an EEG-led decision.
- Twenty-one subjects under LOSO means each held-out fold is a single subject and the reported
  means hide a wide per-subject spread that the tables do not show (no standard deviations are
  given in the modality tables).
- Ternary LOSO accuracy of 47.80% against three classes is a modest margin over a 33.3% chance
  level. The paper does report the label distribution — "Figure 7 presents the distribution of the
  recorded output scores for all the participants", and it states that the 10 s reporting interval
  was chosen because "we aimed to balance the frequency of labels" — but the distribution is a
  figure and no per-class counts survive in the extraction, so the effective margin cannot be
  computed here. This is a reported-but-not-readable gap, not an omission by the paper; an earlier
  version of this card recorded it as "not stated".
- Gaze is recorded with an eye tracker, not electrooculography. Whether the gain it contributes
  would survive substituting EOG electrodes — which is what this project would have — is untested,
  and the two are not interchangeable: an eye tracker gives position, EOG gives a potential
  difference that mixes gaze angle with blink and with the corneo-retinal offset.
- The paper reports accuracy and F1 only. There is no permutation test, no chance-corrected
  metric, and no modality-dropout experiment at inference time, so robustness to a missing channel
  — the scenario a deployed system actually faces — is not evaluated.
- Cognitive load in a driving simulator is manipulated by scenario complexity, which changes the
  visual scene. That is precisely the confound `hogervorst-2014-workload-comparison` controlled
  for and this paper does not: the gaze channel's contribution could reflect the scene rather than
  the load.
- The archived text is the arXiv version; numbers were not diffed against the IEEE version of
  record.

## Citations

Primary: `angkan-2024-invehicle-cognitive-load`

- `hogervorst-2014-workload-comparison` — the same sensor set on an n-back task, with the fusion
  gain not reaching significance.
- `azad-2025-construction-noise` — EEG plus EDA under subject-independent folds, gain ~0.2 points.
- `salam-eeg-ecg-stress` — EEG plus ECG with a much larger reported gain and a less clearly
  specified split.
- `rotaru-2024-auditory-attention-bias` — why a gaze-correlated channel can inflate EEG decoding
  without carrying task information.
- `makowski-2021-neurokit2` — the kind of reference implementation from which this paper's
  hand-crafted peripheral features are drawn.
