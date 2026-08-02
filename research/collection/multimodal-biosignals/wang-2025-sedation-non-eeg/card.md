---
slug: wang-2025-sedation-non-eeg
type: paper
strand: multimodal-biosignals
year: 2025
authors: [Wang, Jiang, Liu, Yuan, Yu, Ma, Liu, Xiao, Zhang]
venue: Bioengineering 12(10):1049
doi: 10.3390/bioengineering12101049
url: https://doi.org/10.3390/bioengineering12101049
license: CC BY 4.0
modalities: [ecg, ppg]
tags: [physiology-only, no-eeg-arm, engineered-features, hrv, lgbm, shap, vitaldb, patient-wise-split, temporal-window-sweep, recursive-feature-elimination, bispectral-index]
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

Predicts an EEG-derived label from peripheral physiology alone — 27 demographic, vital-sign and
HRV features at a 2 s window reach AUROC 0.825 for detecting a bispectral index above 60 — which
makes it the strand's cleanest instance of a physiology-only decoding arm with a patient-wise
split.

## Summary

A retrospective TRIPOD-reporting study on the public VitalDB database, which holds high-resolution
intraoperative waveforms and clinical records from 6,388 surgical patients at a single tertiary
centre. After exclusions — craniocerebral neurosurgery, transplantation and cardiopulmonary bypass;
age outside 18–65; ASA class above III; body mass index at or below 18 or at or above 30; surgery
shorter than two hours; non-general anaesthesia; and missing synchronised bispectral index, ECG and
photoplethysmography waveforms — 5,366 patients were removed, leaving 1,022. Inadequate sedation is
defined as bispectral index above 60. Features spanning demographics, conventional vital signs and
heart-rate-variability metrics were computed over four temporal windows (2, 6, 10 and 20 s), with
the input dimensionality rising from 27 at 2 s to 464 at 20 s, and fed to four classifiers (Light Gradient Boosting Machine, logistic regression, random
forest, naive Bayes). LGBM is best at every window: AUROC 0.825 (95% CI 0.823–0.826) and accuracy
0.741 (0.740–0.742) at 2 s, improving by roughly 0.012 in both at 20 s. Recursive feature
elimination with cross-validation reduces 27 features to 12 with comparable accuracy. SHAP
identifies mean blood pressure, end-tidal CO2, systolic blood pressure, heart rate, body mass
index, HRV_CVNN, sex and ASA status as the most influential predictors.

## Relevance to the review

Category 3 asks for EEG-only, physiology-only and combined arms on the same split, and the
physiology-only arm is the one the multimodal literature almost never reports — every fusion paper
in this strand except this one and `kuttala-2023-hierarchical-fusion` builds its peripheral arm
only as a foil. This entry supplies it directly, and does so in the most informative possible
configuration: the *label itself* is derived from EEG (the bispectral index is an EEG-derived
depth-of-anaesthesia index), so the experiment is literally "how much of an EEG-derived state can
peripheral physiology recover without the EEG". The answer is AUROC 0.825 against a 0.5 chance
line, from 27 engineered scalars.

Read as decoding evidence rather than as a clinical claim, which is what the brief instructs, three
things transfer.

The split is patient-wise and explicitly motivated as such: "To avoid potential data leakage,
train/test splitting was performed at the patient ID level". That is the protocol most of this
strand's positive fusion results do not clearly have.

The temporal-window sweep is directly relevant to a project deciding how long an epoch to give a
peripheral branch. Going from 2 s to 20 s buys about 0.012 AUROC — small, and not free twice over:
a 20 s window cannot resolve a stimulus-locked contrast, and the 20 s model is also a 464-dimension
model against the 2 s model's 27, so part of that 0.012 is extra parameters rather than extra time.
The peripheral channel's information here is slow and barely improved by looking longer.

The SHAP ranking says which features carry the decoding, and the answer is mostly *not* HRV: mean
blood pressure, end-tidal CO2 and systolic blood pressure lead, with heart rate fourth and a single
HRV index (CVNN) sixth. Two of the top three are not available in a non-clinical setting at all.
A project with ECG and respiration but no arterial line or capnograph would be working with the
weaker half of this feature set.

## Notable details

- **Physiology-only number**: LGBM AUROC 0.825 (95% CI 0.823–0.826), accuracy 0.741 (0.740–0.742)
  at a 2 s window; AUROC roughly 0.837 at 20 s (per the ROC-figure caption values 0.837, 0.737,
  0.809, 0.739 across the four models at that window). Chance AUROC is 0.5.

  The paired accuracy at 20 s is **not verifiable**. An earlier version of this card gave 0.753,
  which appears nowhere in the source and is contradicted by this card's own quoted caption list.
  The re-extracted figure text recovers 0.835, 0.837, 0.837, 0.825, 0.804, 0.805, 0.809, 0.794,
  0.741, 0.739, 0.738, 0.737, 0.730, 0.725 and 0.716; 0.753 is not among them. It was most likely
  misread off a plotted bar. The value is left unstated rather than replaced with a guess, since
  reading it needs the figure itself and not the extraction.
- **EEG-only number**: **not reported, by design.** The paper's whole point is to avoid EEG; the
  EEG-derived bispectral index is the label, not an input. There is no EEG arm and no combined arm.
- **Combined number**: not reported, same reason.
- **Split protocol**: patient-ID-level train/test split, 80% of patients to training and 20% to
  test, with 10-fold cross-validation used for hyperparameter tuning inside the training set.
- **Participants**: 1,022 after exclusions. The denominator is stated twice and inconsistently.
  Section 2.1: "486 intraoperative monitoring parameters, 73 perioperative clinical variables, and
  34 time-series laboratory parameters collected from 6388 surgical patients at a single tertiary
  medical center. Among these, 5543 patients had BIS monitoring records available and were
  considered for inclusion". Figure 2's cascade instead opens "6388 patients monitored using BIS in
  the VitalDB database", and only the 6,388 figure reconciles with the arithmetic — the seven
  exclusions sum to 5,366 and 6,388 − 5,366 = 1,022, exactly the stated cohort, whereas
  5,543 − 5,366 = 177. Both readings are recorded; the card follows neither as settled, though the
  arithmetic favours the figure. Exclusion cascade (Figure 2): 2,223 outside 18–65; 125 with ASA
  above III; 400 with BMI at or below 18 or at or above 30; 1,769 with surgery under two hours;
  283 craniocerebral neurosurgery, transplantation or cardiopulmonary bypass; 9 non-general
  anaesthesia; 557 lacking synchronised BIS, ECG and PPG.
- **Signals**: ECG and photoplethysmography waveforms, plus tabulated vital signs and demographics.
  Respiration enters only as end-tidal CO2, a capnograph-derived vital sign, not as a respiratory
  waveform.
- **Feature count**: 27 is the input dimensionality at the 2 s window only. The Methods state
  "The input dimensionality increased with window length: 27 features for 2 s, 142 for 6 s, 234 for
  10 s, and 464 for 20 s." Corrected in the Phase 4 audit: an earlier version of this card said 27
  features were "computed over four temporal windows", which reads as one feature set evaluated at
  four resolutions. It is not — the 20 s model has 17 times as many inputs as the 2 s model, so the
  0.012 AUROC gained by going from 2 s to 20 s is bought with a much larger feature space, not with
  a longer view of the same features. The abstract's flat "27 features" is what the earlier reading
  followed. Recursive feature elimination with cross-validation reduces the set to 12 with
  comparable accuracy (the MINsubset reaches AUC 0.825 and accuracy 0.738 "despite a 55.6% reduction
  in dimensionality"; the OPTsubset reaches AUC 0.827, accuracy 0.743).
- **Top SHAP features**: mean blood pressure, end-tidal CO2, systolic blood pressure, heart rate,
  body mass index, HRV_CVNN, sex, ASA physical status.
- **Sex effect**: female patients were more likely to be classified as inadequately sedated. The
  paper reads this as possible physiological difference in anaesthetic sensitivity — the same
  subgroup-confound shape as `salam-eeg-ecg-stress`'s sex result, in a different direction.
- **Windows evaluated**: 2, 6, 10 and 20 s, with LGBM best at all four.
- The paper is candid that BIS above 60 is an operational surrogate: "Given the retrospective
  nature of the dataset, which did not include postoperative interviews to confirm awareness, BIS
  thresholds were adopted as the operational definition."

## Open questions / limitations

- **The label is EEG-derived and proprietary.** BIS is a closed-source composite of EEG features.
  Predicting it from peripheral signals is not the same as predicting awareness, and the paper says
  so. For this strand the useful reading is narrower still: it shows peripheral physiology tracks
  *something an EEG-derived index also tracks*, which is precisely the redundancy scenario
  `zeng-brain-heart-ccm` predicts and which would make a peripheral channel add little on top of
  EEG.
- Two of the three top predictors — mean and systolic blood pressure — and the second-ranked
  end-tidal CO2 come from invasive or clinical monitoring unavailable outside an operating theatre.
  The decoding does not transfer to a wearable or laboratory setting at this level of performance.
- Anaesthetic agents directly manipulate both the EEG and the cardiovascular system. The
  association between peripheral features and BIS may be substantially mediated by drug
  concentration rather than by any central-peripheral coupling, and the paper does not adjust for
  intraoperative drug dosing in the accessible text.
- Accuracy 0.741 with AUROC 0.825 implies a substantially imbalanced problem; the class balance
  of BIS > 60 in the cohort is not stated in the extracted text.
- The confidence intervals are implausibly tight (0.823–0.826 for AUROC), which is what happens
  when intervals are computed over segments rather than over patients. With a patient-wise split
  and 1,022 patients, patient-level bootstrap intervals would be far wider.
- Single centre, single database, no external validation cohort.
- The exclusion cascade removes 84% of the available patients, including everyone under 18 or
  over 65 and everyone outside a narrow BMI band, so the cohort is not representative even of
  VitalDB.

## Citations

Primary: `wang-2025-sedation-non-eeg`

- `haque-hrv-stress-review` — the engineered-HRV literature this feature set draws on.
- `makowski-2021-neurokit2` — a reference implementation for the HRV metrics used here.
- `kuttala-2023-hierarchical-fusion` — the other peripheral-only entry, with learned rather than
  engineered features.
- `zeng-brain-heart-ccm` — the coupling result that would explain why an EEG-derived index is
  partly recoverable from peripheral signals.
- `salam-eeg-ecg-stress` — the same sex-difference finding in a non-clinical stress setting.
