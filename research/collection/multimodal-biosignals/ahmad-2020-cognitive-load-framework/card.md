---
slug: ahmad-2020-cognitive-load-framework
type: paper
strand: multimodal-biosignals
year: 2020
authors: [Ahmad, Keller, Robb, Lohan]
venue: Personal and Ubiquitous Computing 27(6)
doi: 10.1007/s00779-020-01455-7
url: https://doi.org/10.1007/s00779-020-01455-7
license: CC BY 4.0
modalities: [ecg, eog]
tags: [cognitive-load, engineered-features, pupil-diameter, blink-rate, random-forest, naive-bayes, feature-elimination, stratified-kfold, no-eeg-arm, three-level-load, large-cohort]
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

Three-level cognitive load classified at 91.66% from eye and heart measures alone on 40
participants, with mean pupil diameter change in both eyes as the dominant feature and blink rate
a moderate contributor — but the evaluation is a stratified 5-fold split over samples, not over
participants.

## Summary

The paper proposes a framework for non-intrusive cognitive-load detection from physiological data
of the eyes and the heart, and evaluates it on a reading task designed to induce low, medium and
high load. Stimuli were built from the British National Corpus: 20 ten-letter nouns with
frequencies in a controlled range, and 20 sentences filtered from a movie-review dataset after
removing items with apostrophes, quotes, numbers and very short words. The framework applies a
feature-refinement step and then a range of supervised classifiers — naive Bayes, logistic
regression, support vector machine, k-nearest neighbours and others — to predict the three load
levels. Random forest reaches 91.66% and naive Bayes 85.83%. Feature importance identifies mean
pupil diameter change for the right and left eyes as the most prominent features, with blink rate
a moderately important contributor. Forty-one participants were recruited; eye-tracking data could
not be captured for one, so 40 are analysed. Evaluation uses stratified k-fold to create five
splits of the dataset, followed by a classification report for F1 scores.

## Relevance to the review

The brief places this entry in categories 3 and 5 and directs the card to record how load was
manipulated, how it was labelled, which channels were used and whether the framework was validated
across participants. Taking those in turn produces a mixed picture that is worth stating precisely.

The construct and the cohort are the strengths. Cognitive load induced by a language task is the
closest thing in this strand to what a spoken-versus-written manipulation would produce, and 40
participants is large for this literature — the paper's own argument for its contribution is that
prior accuracy results rest on "small user groups (on average, 8–10 with lows of 3 and 4), which
are known to have low statistical power".

The channel set is the limitation for category 3. There is no EEG. The measures are ocular (pupil
diameter, blink rate) and cardiac (heart rate and HRV), so the paper has a physiology-only arm and
nothing to compare it against. It cannot answer whether peripheral physiology adds to EEG; it can
only say what peripheral physiology achieves alone, which is why the card places its primary weight
on category 5.

The validation is the problem. "Stratified KFold to create five different splits in our dataset"
stratifies by class, not by participant. The dataset is one observation per participant per phase
— the ANOVA is reported as F(2,119), and all seven classifier accuracies are exact multiples of
1/120 (91.66 = 110/120, 85.83 = 103/120, 85.00 = 102/120, 82.50 = 99/120, 77.50 = 93/120,
69.16 = 83/120, 45.83 = 55/120) — so 40 participants contribute three rows each. A stratified split
over those rows therefore places a participant's low-load row in training and their high-load row
in test. Pupil diameter and blink rate are strongly idiosyncratic, so a classifier can learn
participant identity and read the load level off it. The 91.66% should therefore be read as a
within-subject-leakage-inclusive number, and the brief's question — whether the framework was
validated across participants — is answered: it was not.

Correction, Phase 4 audit. An earlier version of this paragraph said "40 participants each
contributing many samples" and described the leaked units as "windows". The source describes no
windowing: each phase yields one aggregate feature vector per participant (mean pupil diameter
change, blink rate, heart rate, HRV over the phase segment). The leakage conclusion is unchanged;
its mechanism is not per-window correlation but per-participant identity across three rows.

That reading is reinforced by the finding itself. The dominant features are *changes* in pupil
diameter, which is the right normalisation for a within-subject comparison and the wrong one for a
cross-subject one.

## Notable details

- **Physiology-only number**: random forest 91.66%, naive Bayes 85.83%, for three-way low/medium/
  high cognitive load. Full Table 4 (mean accuracy, %): AB 69.16, NB 85.83, DT 85.00, SVM 82.50,
  LR 77.50, RF 91.66, KNN 45.83.
- **Per-classifier F1 scores (Table 5)**, low / medium / high cognitive load: AB 0.62 / 0.71 / 0.75;
  NB 0.87 / 0.81 / 0.90; DT 0.84 / 0.80 / 0.84; SVM 0.83 / 0.77 / 0.88; LR 0.80 / 0.64 / 0.85;
  RF 0.91 / 0.85 / 0.95; KNN 0.48 / 0.51 / 0.37. Corrected in the Phase 4 audit: an earlier version
  of this card said "the results tables lose their column alignment in the extraction, so
  per-classifier F1 scores are not quoted on this card". Both tables are intact in the current
  `source.md`, which renders Table 5 as `|Low|AB|0.62| ||NB|0.87| ||DT|0.84| ||SVM|0.83| ||LR|0.80|
  ||RF|0.91| ||KNN|0.48|` and the corresponding medium and high blocks. The extraction was
  regenerated with pymupdf4llm (see `meta.json.notes`); the card's claim of loss described the
  superseded markitdown conversion.
- **Sample count and chance level**: the source does not state either in words, but the design fixes
  both. Each participant contributes one observation per phase and the phases *are* the three load
  levels ("Our stimuli had three phases: (1) the rest phase, (2) the trial phase, and (3) the task
  phase. These were used to generate three levels of CL, Low, Medium and High respectively"), the
  ANOVA is reported as "F 2 , 119" throughout, and every reported accuracy is an exact multiple of
  1/120. That gives 120 observations, 40 per class, and a chance level of 33.3%. An earlier version
  of this card said the accessible text did not establish the class balance; it establishes it
  by construction rather than by statement.
- **EEG-only number**: **not reported.** No EEG was recorded. This is a property of the study, not
  an access gap.
- **Combined number**: not applicable; there is no second arm.
- **Split protocol**: stratified 5-fold over the dataset. **Not subject-wise.** The paper does not
  report a leave-one-participant-out or otherwise participant-disjoint evaluation.
- **Participants**: 41 recruited, 40 analysed (eye-tracking capture failed for one).
- **Channels**: eye (pupil diameter, blink rate) via eye-tracking glasses, and heart. The card
  tags these as `eog` and `ecg` per the controlled vocabulary; the actual instruments are an
  eye tracker and a heart-rate sensor, not electrooculography electrodes and a clinical ECG.
- **Dominant features**: mean pupil diameter change, right and left eye, with blink rate a
  moderate contributor. The paper's framework explicitly runs feature elimination to identify the
  indicative features in a given context rather than committing to a fixed set.
- **Load manipulation**: a reading task using 20 controlled-frequency ten-letter nouns and 20
  sentences selected from a movie-review corpus after filtering.
- **Cohort argument**: the paper positions itself against a literature of 3–10 participant studies
  and against prior work that "uses SVM and suffers from overfitting".
- **Year**: published online 2020; the print issue is Personal and Ubiquitous Computing 27(6),
  2027–2041, 2023. The brief and this card use 2020.
- **Cross-strand**: the brief assigns label-validity questions about this work to the
  `candidate-datasets` strand and the estimation method to this one. No file was written into a
  sibling strand.

## Open questions / limitations

- The stratified-5-fold evaluation almost certainly leaks participant identity across folds. Until
  a participant-disjoint number exists, 91.66% cannot be compared with the subject-wise figures
  elsewhere in this strand (for example `angkan-2024-invehicle-cognitive-load`'s 41.59% EEG-only
  LOSO ternary), and comparing them directly would be a category error.
- No EEG arm, so the entry cannot contribute to the project's third comparison.
- Neither the class balance nor the chance level is stated in words; both follow from the design
  (see the sample-count bullet above), so the margin over chance is 91.66% against 33.3% — but that
  margin is a within-subject-leakage-inclusive one.
- One hundred and twenty observations across seven classifiers and a five-fold split is a very small
  evaluation. A single reclassified observation moves accuracy by 0.83 points.
- Pupil diameter is confounded with screen luminance and with the amount of text on screen. The
  three load levels use different stimuli (single words versus sentences), so the visual display
  differs between conditions — the exact confound `hogervorst-2014-workload-comparison` controlled
  for and this paper does not.
- The paper's own text flags that pupil diameter "is sensitive to changes in light and also varies
  with age", and that heart rate and HRV "are insensitive to the instantaneous load", without
  reporting how either was handled.
- Ocular measures dominating a load classifier is the same finding as
  `wibirama-cognitive-load-eye-movement` and points the same way for this project: an added ocular
  channel may decode a stimulus-modality contrast through reading behaviour rather than through
  cognition.
- The per-level F1 scores show a pattern the mean accuracy hides: five of the seven classifiers
  (NB, DT, SVM, LR, RF) score lowest on the medium level, which is the trial phase — a
  familiarisation block rather than a calibrated point on a load scale. The three "load levels" are
  three procedural stages of the session, which also makes them perfectly confounded with time on
  task.

## Citations

Primary: `ahmad-2020-cognitive-load-framework`

- `wibirama-cognitive-load-eye-movement` — the same construct from eye movement alone with deep
  time-series models, at 0.8780.
- `hogervorst-2014-workload-comparison` — the workload comparison that controls the visual-input
  confound this study leaves open, and finds pupil size at 75%.
- `angkan-2024-invehicle-cognitive-load` — cognitive load with EEG plus gaze under leave-one-
  subject-out, giving the subject-wise reference point this entry lacks.
- `haque-hrv-stress-review` — the HRV-feature literature the cardiac half of this framework draws
  on.
- `makowski-2021-neurokit2` — reference implementation for the cardiac and ocular feature
  extraction such a framework needs.
