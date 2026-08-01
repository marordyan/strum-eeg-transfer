---
slug: haque-hrv-stress-review
type: paper
strand: multimodal-biosignals
year: 2023
authors: [Haque, Zawad, Rony, Al Banna, Ghosh, Kaiser, Mahmud]
venue: Cognitive Computation 16(2)
doi: 10.1007/s12559-023-10200-0
url: https://doi.org/10.1007/s12559-023-10200-0
license: CC BY 4.0
modalities: [ecg, ppg, eda]
tags: [review, heart-rate-variability, stress-prediction, engineered-features, shallow-ml, deep-learning, sensing-technologies, wearables, rmssd, sdnn, lf-hf, multi-modal-preprocessing]
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

Systematically reviews 43 studies predicting stress from heart-rate variability with artificial
intelligence, tabulating for each the sensors, the preprocessing, the features and the model — the
strand's reference point for what engineered HRV features achieve before any learned encoder is
introduced.

## Summary

The review's premise is that miniaturised sensors and low-cost wearables have made continuous
physiological monitoring routine, and that heart-rate variability — the time interval between
consecutive heartbeats — has become the standard indicative measure for estimating stress,
depression and anxiety. It analyses 43 studies applying artificial-intelligence algorithms to this
problem, summarising each in tables and evaluating the completeness of their findings and reported
results. Coverage is organised into sensing technologies, preprocessing methods applied to
multimodal data, and prediction models, followed by a critical examination of how machine-learning
models have been used to predict stress from HRV, an analysis of which features enable better
performance, and a closing list of challenges with possible mitigations. The summary tables record,
per study, the model family, the preprocessing, the sensors and the features: for example one entry
uses SVM and k-nearest neighbours on a Kinect 3D sensor plus ECG with RMSSD, AVNN, SDANN, SDNN,
NN50, PNN50, LF, HF and LF/HF; another uses k-NN, SVM, decision tree and naive Bayes on GSR, blood
volume pulse, skin temperature, three-axis acceleration and heart rate with time-domain,
frequency-domain and distribution features; others use Fitbit activity counts or a Polar H10
wristband with SD1, SD2, RMSSD, SDNN and mean heart rate.

## Relevance to the review

The brief makes this the strand's reference point for the engineered-feature bar, and the tables
are what deliver on that. Three things they establish.

The feature vocabulary is small and stable. Across 43 studies the same dozen indices recur: RMSSD,
SDNN, SDANN, AVNN, NN50, PNN50, SD1, SD2, LF, HF, LF/HF and mean heart rate. That is the complete
engineered-cardiac feature space this project would be choosing between, and it is small enough to
compute exhaustively — which is what makes the classical arm cheap and makes omitting it hard to
justify.

The sensing is heterogeneous in a way that matters for feature validity. Studies in the tables draw
intervals from clinical ECG, from wrist PPG, from a Polar chest strap, from ballistocardiography
with an EMFi sensor, and in one case from Fitbit activity summaries and phone-usage counts. HRV
computed from a PPG pulse interval is not the same quantity as HRV computed from an ECG R-R
interval, and a review that pools them is pooling different measurements under one name. A project
using ECG should read the ECG-sourced rows only.

The multimodal preprocessing section is the part closest to this project's needs, because HRV is
almost never used alone in these studies — GSR, blood volume pulse, skin temperature and
acceleration recur alongside it — and the review's stated focus on "pre-processing methods applied
on multi-modal data" is the step where sampling-rate reconciliation between channels happens.

The review is secondary evidence and its aggregate accuracy figures should not be treated as
findings, per the brief. Its value here is the taxonomy and the per-study tables, not its
conclusions.

## Notable details

- **Scope**: 43 studies, each summarised for model, preprocessing, sensors and features.
- **Feature families recurring in the tables**: time domain (RMSSD, SDNN, SDANN, AVNN, NN50,
  PNN50, mean NN), frequency domain (LF, HF, VLF, total power, LF/HF), nonlinear/Poincaré (SD1,
  SD2), plus distribution statistics of the interval series.
- **Sensor heterogeneity in the tables**: clinical ECG (including 12-lead), wrist PPG and blood
  volume pulse, GSR, skin temperature, three-axis accelerometry, Polar H10 chest strap,
  ballistocardiography via EMFi sensor, and Fitbit activity and phone-usage counts.
- **Preprocessing methods tabulated**: Savitzky-Golay filtering, Butterworth filters, adaptive
  noise cancellation, FIR and IIR filters, empirical mode decomposition, artifact interpolation
  and removal, normalisation and transformation, principal component analysis.
- **Model families**: shallow machine learning (SVM, k-NN, naive Bayes, logistic regression,
  decision tree, random forest, multilayer perceptron) and deep learning (CNN, LSTM), with the
  review noting rule-based and fuzzy approaches are rare but attractive for interpretability.
- **Structure**: sensing technologies, then multimodal preprocessing, then prediction models, then
  a features analysis, then challenges and mitigations.
- **Per-study accuracy figures are not quoted on this card.** The review's value is in its large
  landscape summary tables, and those are exactly what the two-column extraction destroys: the
  tables collapse into unusable pipe fragments (see `meta.json.notes`). Quoting a number from the
  extraction would risk attaching a value to the wrong study.
- 98 citations at retrieval; Cognitive Computation 16(2), 455–481.

## Open questions / limitations

- No per-study number is recorded here, which limits what this entry can contribute beyond the
  taxonomy. A downstream reader wanting the engineered-feature bar as a *number* has to open the
  PDF's tables.
- Pooling ECG-derived and PPG-derived HRV under one label is a validity problem the review does not
  appear to flag in the accessible text. Pulse-interval variability includes pulse-transit-time
  variation that R-R interval variability does not.
- "Stress" across 43 studies spans acute laboratory stressors, driving, occupational monitoring and
  clinical anxiety. Aggregate statements about which features work best are averaging over
  constructs that need not share a physiological signature.
- Reviews of this kind rarely report split protocols per study, and this one's tables record model,
  preprocessing, sensors and features but not, in the visible rows, whether evaluation was
  subject-wise. Given how strongly HRV indices are trait-like, that omission is consequential.
- Publication bias is not addressed in the accessible text: a table of 43 reported accuracies is a
  table of published accuracies.
- The review predates the peripheral-foundation-model literature (`papagei-2024`,
  `mckeen-2025-ecg-fm`) and therefore cannot say whether learned representations beat these
  engineered features. That head-to-head comparison is missing from this strand entirely.

## Citations

Primary: `haque-hrv-stress-review`

- `makowski-2021-neurokit2` — the reference implementation for essentially every HRV index this
  review tabulates.
- `mckeen-2025-ecg-fm` — the learned-representation alternative for the same signal.
- `wang-2025-sedation-non-eeg` — a recent engineered-HRV-plus-vitals decoder with a patient-wise
  split, showing what the feature family achieves in practice.
- `salam-eeg-ecg-stress` — uses two of the indices reviewed here (heart rate, LF/HF) as the entire
  peripheral arm of an EEG fusion.
- Quigley et al. (2024), "Publication guidelines for human heart rate and heart rate variability
  studies in psychophysiology", Psychophysiology 61, doi 10.1111/psyp.14604 — the reporting
  standard against which the studies in this review could be audited. Not carded in this strand.
