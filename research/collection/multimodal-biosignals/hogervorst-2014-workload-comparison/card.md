---
slug: hogervorst-2014-workload-comparison
type: paper
strand: multimodal-biosignals
year: 2014
authors: [Hogervorst, Brouwer, van Erp]
venue: Frontiers in Neuroscience 8:322
doi: 10.3389/fnins.2014.00322
url: https://doi.org/10.3389/fnins.2014.00322
license: CC BY
modalities: [eeg, ecg, eda, resp, eog]
tags: [negative-result, n-back, mental-workload, sensor-group-comparison, feature-fusion, decision-fusion, within-subject-temporal-split, pupil-size, elastic-net, svm]
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

With body movement and visual input held constant across workload levels, EEG classified n-back
load at about 86% while peripheral physiology and eye measures reached 70–75%, and combining
sensor groups produced no statistically significant improvement over the best single sensor — a
negative result on fusion from a study designed specifically to test it.

## Summary

Fourteen participants performed a 0/1/2-back task while EEG, skin conductance, respiration, ECG,
pupil size and eye blinks were recorded. The design deliberately held the two usual confounds
constant: the amount of body movement and the visual input were the same across workload levels,
so a variable that tracks load cannot be doing so through motion or through the quantity of
information on screen. Variables were divided into three "sensor groups" reflecting different
hypothesised mechanisms — EEG for cognitive processes, peripheral physiology for arousal and
energy demand, eye-related measures for a mixture. Individually tuned classification models (SVM
and elastic net, plus a decision-level model combining single-feature model outputs) were trained
on the first part of each participant's data and tested on the last part, simulating online use
and avoiding accuracy inflation from time-dependence. All three sensor groups classified high
versus low workload above chance at p < 0.01. EEG reached around 86%; peripheral physiology and
eye-related variables reached 70–75%. The best single variable was the event-related potential at
Pz at 88%. Combining sensor groups did not significantly improve on the best single sensor.

## Relevance to the review

This is the strand's cleanest direct test of the project's third comparison, and it comes out
negative. The authors state the hypothesis this project would start from — "combination of these
groups is expected to lead to better classification accuracy than either group alone, especially
for the combination of EEG and peripheral physiology" — and then report that it did not happen.
Their literature review notes two prior studies (Coffey et al. 2012 on EEG plus fNIRS, Chanel et
al. 2006 on EEG plus skin conductance, heart rate, blood pressure, respiration and temperature)
that also found no strong fusion advantage, so the null is not isolated.

Two design choices make the null more informative than a typical negative result. First, the
movement and visual-input controls remove the confounds that would otherwise let peripheral
channels pick up task-correlated nuisance — which is the same worry the `zare`-style negative
literature raises for EEG. Second, the train-on-early, test-on-late split is closer to a
deployment protocol than random cross-validation is, so the null is not an artifact of an easy
split; if anything a harder split should make complementary information more valuable, not less.

The one arm that does approach EEG is eye-related: pupil size alone reaches 75%, and EEG plus eye
measures reaches "a little over 90%" against 86% for EEG at Pz alone, a difference the authors
report as not significant. That places the eye channel, not the cardiac or electrodermal channel,
as the plausible source of any peripheral gain — the same conclusion `wibirama-cognitive-load-eye-movement`
reaches from the other direction, and the reason the ocular-artifact question in category 4 is
load-bearing for this project.

## Notable details

- **EEG-only number**: around 86% for high versus low workload (2-back vs 0-back, 120 s segments);
  the single best variable was the ERP at Pz at 88% with elastic net. All EEG variables except
  theta power at Fz classified well above chance at p < 0.01.
- **Peripheral-only and eye-only numbers**: 70–75% at the sensor-group level. The only non-EEG
  variables exceeding the 0.01 chance level were respiration frequency (69%) and pupil size (75%).
  Combining the peripheral physiological sensors (skin conductance electrodes, respiration belt,
  ECG electrodes) gave a "modest, non-significant improvement to around 75%" over the best single
  physiological sensor, respiration at around 70%.
- **Per-sensor accuracies (2-vs-0-back, 120 s), from the Results prose**: EEG 0.86 (both
  classifiers); eye 0.75 (SVM); respiration 0.70; skin conductance 0.63 (elastic net); **ECG 0.61**
  (elastic net), the last two "just reaching a level that is significantly higher than chance
  (p < 0.05)". The ECG figure is the one this strand most needs and an earlier version of this card
  omitted it: on this task the cardiac channel alone is 25 points below EEG and 5 points above the
  weakest sensor.
- **What counts as a real difference here**: "Using the assumption of a binomial distribution,
  significance (p < 0.05) is reached for differences of around 10%." Adding a sensor group to EEG
  bought "3-5%" with elastic net. The null is therefore a null against a coarse yardstick — the
  study can exclude a 10-point fusion gain, not a 3-point one.
- **Harder conditions do not rescue fusion**: at 30 s segments performance drops 8% (SVM) and 5%
  (elastic net) and "the pattern of results is highly similar", which the authors read as evidence
  that the absent fusion benefit "is not due to a ceiling effect". For 2-vs-1-back performance is
  10% (SVM) and 6% (elastic net) lower; for 1-vs-0-back, 22% and 18% lower, with EEG models "just
  below 0.70". In both small-difference conditions the physiology model is not significantly
  different from chance, and the eye model drops to chance for 1-vs-0-back.
- **Adding the time of measurement as a feature** raises the physiology model by 9% (significant)
  and the eye model by 5% (not significant), while doing nothing for EEG — a direct measurement of
  how much of the peripheral signal is drift rather than state.
- **Combined number**: "a little over 90%" for EEG plus eye-related variables on 2-minute
  segments, against 86% for EEG from Pz alone, described by the authors as "a similar and not
  significantly different performance". Combining EEG with another sensor group did not
  significantly improve performance.
- **Split protocol**: within-subject, individually tuned models; the first part of each
  participant's data is the training set and the last part the test set, explicitly to avoid
  inflation from time dependencies. This is *not* subject-wise — every model is personal — so the
  numbers say nothing about cross-subject transfer.
- **Participants**: 14 analysed, "aged between 23 and 40 years (mean age 27.9), 8 female and
  6 male". A footnote records that "A total of 35 participants took part in the original experiment
  … However, we here only considered participants with complete data sets", with partial analyses
  reported to show the same patterns. The 30 s analysis uses 12 of the 14.
- **Instruments**: EEG from g.tec Au electrodes at Fz, FCz, Pz, C3, C4, F3 and F4, mastoid-
  referenced, 256 Hz. ECG, skin conductance and respiration on a MindWare BioNex. The eye measures
  — pupil size and blinks — come from a **Tobii T60 eye-tracker monitor**, not from
  electrooculography electrodes; the card tags the channel `eog` per the strand's controlled
  vocabulary, as `ahmad-2020-cognitive-load-framework` does, but the measurement is video eye
  tracking. This matters wherever the card's eye-channel result is carried into an EOG argument.
- The authors offer two explanations for their own null in the discussion: that they used
  decision-level as well as feature-level fusion and still saw no reliable advantage, and that
  giving more weight to lower-performing variables hurts. Both cut against the idea that a better
  fusion architecture would have rescued the result.
- The paper is explicit that eye-related measures "have probably partly been found to covary with
  workload due to the often occurring confound of the amount of visual information", and that for
  pupil dilation "the reason for its association with workload is unclear" — an unusual admission
  that one of its own sensor groups may be measuring the stimulus rather than the state.
- Companion group-level analysis of the same data is Brouwer et al. (2014).

## Open questions / limitations

- Fourteen participants with individually tuned models is a small basis for a null, and the paper
  states the resolution limit itself: differences below about 10 percentage points are not
  detectable under its binomial test. The observed 3-5% fusion increment sits inside that band, so
  the result is "no gain larger than the study can see", not "no gain".
- The evaluation is entirely within-subject. Whether fusion helps *across* subjects — the regime
  where EEG is weakest and where a peripheral channel might plausibly be more stable — is not
  tested, and this is the most important untested case for the project.
- Feature engineering is classical (band powers, an ERP amplitude, HRV bands, respiration rate,
  pupil size, blink counts). A learned peripheral encoder might extract more; the paper predates
  that literature and cannot speak to it.
- Because the design holds visual input constant, it also removes a source of variance that a
  realistic task would have. The null therefore applies to a deliberately clean setting; it is
  arguably a lower bound on the confound risk and an upper bound on the honesty of the peripheral
  arms.
- The workload contrast is 2-back versus 0-back within one task. Nothing establishes that the same
  ordering (EEG best, eyes second, peripheral third) holds for a different construct, and this
  project's construct is a stimulus-modality contrast, not load.
- **Extraction limitation, restated after the Phase 4 audit.** Figures 1-4 are images and their
  plotted values did not convert; per-sensor-group bar heights for each of the four comparisons
  cannot be read off `source.md`. But the Results prose restates the values that matter, and this
  card now quotes them (ECG 0.61, skin conductance 0.63, respiration 0.70, eye 0.75, EEG 0.86, the
  3-5% fusion increment, the ~10% significance threshold, and the drops for 30 s and for smaller
  workload differences). An earlier version said "every number on this card comes from the prose in
  the Conclusion and Discussion, so per-condition values are unavailable" — the Results section
  states them too, and the condition-level summaries are prose rather than figure-only.

## Citations

Primary: `hogervorst-2014-workload-comparison`

- `salam-eeg-ecg-stress` — same EEG-plus-ECG question, large positive fusion gain; the contrast
  with this null is one of the strand's sharpest disagreements.
- `azad-2025-construction-noise` — a modern deep-learning replication of the same null shape
  (fused 0.796 vs EEG 0.794) under subject-independent folds.
- `angkan-2024-invehicle-cognitive-load` — the same sensor set with a positive but modest gain
  under leave-one-subject-out.
- `wibirama-cognitive-load-eye-movement` — the eye-only arm taken seriously as a decoder rather
  than as a comparator.
- Chanel et al. (2006), "Emotion assessment: arousal evaluation using EEG's and peripheral
  physiological signals" — cited here as an earlier study that also found no strong advantage of
  fusing EEG and peripheral physiology.
