---
slug: salam-eeg-ecg-stress
type: paper
strand: multimodal-biosignals
year: 2026
authors: [Salam, Alam, Shah, Rahman, Ali, Tahir]
venue: Scientific Reports 16:7304
doi: 10.1038/s41598-026-38356-3
url: https://doi.org/10.1038/s41598-026-38356-3
license: CC BY-NC-ND 4.0
modalities: [eeg, ecg]
tags: [feature-level-fusion, unimodal-ablation, theta-alpha-ratio, hrv, lf-hf, mist, subject-grouped-split, svm, sex-differences, cognitive-stress]
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

Three engineered features — one from EEG (theta/alpha ratio) and two from ECG (heart rate and
LF/HF) — beat either modality alone by a wide margin when concatenated, but the paper's own
tables show the whole gain rides on a single classifier, and the split protocol it describes is
internally inconsistent.

## Summary

A secondary analysis of the public dataset "ECG & EEG features for mental workload and multilevel
stress classification in different sexes", collected from 66 healthy university students (21 male,
45 female) at Prince of Songkla University while they performed an adapted Montreal Imaging Stress
Task (rest with eyes open, then four arithmetic conditions AC1–AC4). One EEG feature (theta/alpha
ratio, TAR) and two ECG features (heart rate, LF/HF) were extracted, screened with Shapiro-Wilk
and Kruskal-Wallis tests, reduced with principal component analysis, and fed to six classifiers
(decision tree, k-nearest neighbours, linear discriminant, naive Bayes, random forest, support
vector machine) in unimodal and concatenated-feature configurations. On the five-way rest-versus-
AC1–AC4 problem the support-vector machine averages 80.0% with EEG alone, 66.65% with ECG alone,
and 92.6% fused. On the three-way rest / low / high problem the same classifier gives 75.2%
(EEG), 71.3% (ECG) and 85.7% (fused). A sex-stratified analysis finds the female subgroup easier
to classify and reports a significant condition-by-sex interaction.

## Relevance to the review

This is the closest published analogue to the project's third comparison: same two modalities,
same "does peripheral physiology add anything over EEG" question, and a fusion arm reported
against both unimodal arms on what the paper presents as one split. The size of the reported gain
— +12.6 points over EEG alone on the five-class problem, +10.5 on the three-class — is the number
Phase 3 would have to beat or explain, and it is far larger than the near-zero gains in
`hogervorst-2014-workload-comparison` and `azad-2025-construction-noise`, which is itself the
interesting fact.

Two features of the design bear directly on how much of that gain would survive in STRUM. First,
the peripheral contribution here is entirely autonomic-arousal information (HR, LF/HF) against a
stressor that manipulates arousal by design; a spoken-versus-written stimulus contrast has no
comparable arousal manipulation, so the mechanism that makes ECG informative in this paper may not
be present. Second, the feature set is three scalars per window, not a learned encoder, so the
paper is evidence about engineered peripheral features (category 5) as much as about fusion.

The sex result matters as a confound warning rather than as a finding: females were 45 of 66
participants and were classified more accurately, so subgroup composition and accuracy are
entangled in exactly the way that would let a demographic imbalance masquerade as a physiological
effect.

## Notable details

- **EEG-only number**: 80.0% mean accuracy (SVM, rest vs AC1–AC4, combined sexes, Table 12);
  75.2% on rest / low / high (Table 13).
- **Peripheral-only number**: ECG alone 66.65% (Table 12) and 71.3% (Table 13). Note the ECG arm's
  Matthews correlation coefficient is 0.0 in Table 13 despite 71.3% accuracy, i.e. that arm is at
  or near the majority-class baseline on the three-class problem.
- **Combined number**: 92.6% (Table 12), 85.7% (Table 13).
- **Split protocol**: the paper states data "were grouped by subject ID and ensured that all data
  points corresponding to a single subject were assigned exclusively to either the training or the
  testing set", an 80/20 split, and "stratified 10-fold cross-validation". Those three statements
  are not mutually consistent as written — a fixed 80/20 subject-wise split and a stratified
  10-fold cross-validation are different protocols, and stratification is by class, not by
  subject. What was actually run cannot be determined from the text.
- **Participants**: 66 (21 male, 45 female), secondary analysis of a public dataset; no new
  recording.
- **Features**: EEG theta/alpha ratio only — no other band, no spatial feature, no per-channel
  information. ECG contributes heart rate and LF/HF only. Kruskal-Wallis effect sizes: TAR
  H = 49.946, p < .001, epsilon-squared 0.154; LF/HF H = 30.598, p < .001, 0.094; HR H = 9.683,
  p = .046, 0.030.
- The gain is classifier-specific. In Table 7 the linear discriminant classifier reaches 84.3%
  combined-sex accuracy and the random forest only 65.7%; the SVM's 92.6% is an outlier among the
  six models rather than a property of the feature set.
- Sex-stratified: linear discriminant reaches 90% for males and 90.9% for females (Tables 5, 6),
  while the SVM reaches 75% and 80.6%. So the best classifier differs between the pooled and the
  stratified analyses.

## Open questions / limitations

- **Self-contradiction on the headline number.** The abstract says the SVM attained "94.7% accuracy
  in the combined-gender classification of cognitive stress" and separately "a peak average
  accuracy of 92.6%"; the conclusion says 94.7% was reached "in the rest versus cognitive stress
  classification". In Table 8, 94.7% is the SVM's accuracy for rest-versus-low-stress only, one
  cell of a three-condition row whose average is 85.7%. This card takes the table values (80.0 /
  66.65 / 92.6 and 75.2 / 71.3 / 85.7) per the tables-over-prose rule.
- **Self-contradiction on the sex-specific number.** The abstract attributes 90.9% to "sex-specific
  classifications" generally; the body attributes 90% to males and 90.9% to females, and Table 7's
  linear-discriminant row shows 86.6% and 87.4%. The 90 / 90.9 figures come from Tables 5 and 6,
  the per-condition tables, not from the averaged Table 7.
- The split ambiguity above is the most consequential gap. If any part of the evaluation used
  record-wise rather than subject-wise folds, the fused number is not comparable to a subject-wise
  result, and the +12.6-point gain could partly reflect that.
- No chance level or class-balance figure is given for the five-class problem, so the 92.6% cannot
  be converted into an effect size. The classes are one rest condition against four arithmetic
  conditions, which is unlikely to be balanced.
- The peripheral features are computed from ECG-derived HRV over windows the paper does not
  specify in the extracted text, so the temporal resolution of the fused decision is unstated.
  This matters for STRUM, where stimulus-locked epochs are short relative to HRV estimation
  windows.
- The dataset is a feature table, not raw signal, so nothing can be said about artifact handling,
  and the possibility that the EEG theta/alpha ratio is itself contaminated by muscle or ocular
  activity during arithmetic is not addressed.
- Sex is confounded with sample size (45 female vs 21 male). The paper interprets higher female
  accuracy as a physiological difference; a class-size explanation is not excluded.

## Citations

Primary: `salam-eeg-ecg-stress`

- `hogervorst-2014-workload-comparison` — the same comparison run on a within-subject temporal
  split, reaching the opposite conclusion about whether fusion helps.
- `kumar-2026-attention-eeg-ecg-stress` — the same modality pair and construct with a deep
  attention-fusion model, reporting a similar-sized gain.
- `azad-2025-construction-noise` — EEG versus EEG-plus-peripheral under subject-independent
  cross-validation, where the gain is 0.2 points.
- `haque-hrv-stress-review` — the engineered-HRV baseline literature that LF/HF and HR come from.
- Ahmed et al., "ECG & EEG features for mental workload and multilevel stress classification of
  different sexes" — the underlying public dataset (reference 56 in the paper); dataset
  characterization belongs to the `datasets-benchmarks` strand.
