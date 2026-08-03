---
slug: alexander-2019-cortical-waves
type: paper
strand: eeg-models
year: 2019
authors: [Alexander, Ball, Schulze-Bonhage, van Leeuwen]
venue: PLOS Computational Biology 15(11):e1007316
doi: 10.1371/journal.pcbi.1007316
url: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007316
license: CC BY 4.0
modalities: [meg, ecog, whole-head-gradiometer-151-sensor, subdural-grid, no-scalp-eeg]
tags: [theoretical-motivation, traveling-waves, phase-prediction, pca, morlet-wavelet, spatiotemporal-structure, self-initiated-motor-task, no-transfer-evidence]
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

Future phase at a single recording site is predicted better from the large-scale traveling-wave
pattern across the whole sensor array than from that site's own past — establishing that cortical
signals carry predictable spatiotemporal structure that a purely local model discards.

## Summary

Alexander and colleagues predict the future phase of band-limited cortical activity at one
selected recording site, using only Fourier analysis and principal component analysis of the
phase pattern across the entire array. The model relates the past whole-array phase pattern to
the future whole-array pattern, and reads the prediction for the target site off the latter; past
data from the target site itself is not required. The dominant eigenvectors are smooth,
low-spatial-frequency propagating waves with wavenumber approximately unity across the array,
and the first eigenvector alone is enough for nearly maximal accuracy. Evaluated on MEG from 20
subjects and ECoG from 3 subjects during self-initiated hand movements, the phase-locking value
of the error reaches 0.73 in the best subject and falls to 0.32 in the worst when all test trials
are used, and 0.94 to 0.51 (subject-wise mean 0.72) when trials are selected by power, which is
the condition the paper tabulates as its headline result; the abstract's summary figure is a mean
phase error "as low as 0.5 radians". The comparator is a purely temporal Fourier model fitted at the same site, which
yields larger error angles at the times and frequencies of best prediction and, more strikingly,
a much narrower band of frequencies at which any good prediction is available.

## Relevance to the review

This is the second and final entry on the strand's theoretical-motivation line, and it is carded
there by a scoping decision rather than because it is a theory paper. It is an empirical
prediction study. What it establishes for this project is narrow and worth stating precisely:
cortical signals carry spatiotemporal structure that is predictable across space, so a model that
takes the whole electrode array as a joint object has access to information that a per-channel
model does not. That is the assumption underneath every spatio-temporal EEG architecture in this
strand, and this paper is the closest thing the corpus has to a direct measurement of it.

The measured margin over the local baseline is what makes it usable, and it is also what bounds
it. The paper does not show that any learned model captures the structure, only that a
two-step linear decomposition can exploit it for one-cycle-ahead phase prediction. It cannot
support a claim that a pretrained checkpoint has learned wave structure, that such structure
survives in scalp EEG, or that it helps a classification task. The line is now at its cap of two,
so a further signal-structure paper cannot be added without reopening the scoping decision, which
is a Phase 3 conversation.

## Notable details

- **Pretraining corpus and total hours**: not applicable. No model is pretrained; the analysis is
  fitted per subject on that subject's own recording, with model construction and prediction
  assessed on disjoint data.
- **Parameter count**: not applicable in the usual sense. The model is a PCA basis over
  complex-valued phase patterns; the reported dimensionality is that the first three (ECoG) or
  four (MEG) eigenvectors are low-spatial-frequency waves, and that one eigenvector suffices for
  near-maximal accuracy.
- **Input contract**: MEG recorded on a 151-sensor whole-head CTF gradiometer at 312.5 Hz; ECoG
  from a 112-contact subdural platinum array with 7.1 mm spacing (ECOG1) and two 8x8 grids with
  10 mm spacing (ECOG2, ECOG3), digitized at 256 Hz (ECOG1) and 1024 Hz (ECOG2, ECOG3),
  band-pass filtered 0.032–97 Hz and re-referenced to average reference. Phase estimated with
  one-cycle (ECoG) or two-cycle (MEG) Morlet wavelets over 120 logarithmically spaced centre
  frequencies from 2.0 to 16.0 Hz; predictions made for samples from −500 ms to +500 ms around
  the movement or button press. Prediction horizon is one cycle (ECoG) or two cycles (MEG) at the
  frequency of interest.
- **Most informative transfer number, with baseline**: there is no transfer number, because
  nothing is transferred. The informative comparison is the ablation of spatial information:
  the large-scale spatio-temporal Fourier model versus a purely temporal Fourier model fitted at
  the same target site. The paper reports the spatio-temporal model reaching PLV-error 0.73 in
  the best subject (0.32 in the worst) over all trials, and states that the temporal-only model
  "gives somewhat higher error angles at the times and frequencies of best predictions" while
  admitting good predictions over a much narrower frequency range ("the range of temporal
  frequencies at which good predictions can be found is rather narrow for the purely temporal
  model, compared to spatio-temporal model"). The time-by-frequency panels of Figure 3 do not give
  the margin as paired scalars, but the paper does test it — see the statistics bullet below.
- **A third comparator exists: the local event-related model.** The card previously described the
  study as a two-model comparison. It is a three-model comparison. Verbatim: "we also compared the
  large-scale model (one eigenvector, varimax rotation, top quartile past MLP) to the event-related
  model (condition 'both', top quartile past MLP) and the temporal Fourier model (top quartile past
  MLP). The former two models did not differ in mean performance (see S1 Table), but the temporal
  Fourier model performed less well." The event-related model needs knowledge of the subject's
  task events, which the large-scale model does not, and it degrades under task ambiguity and on
  cognitive paradigms. The paper's own conclusion: "large-scale spatio-temporal models out-perform
  purely temporal models in the prediction of future phase and that the performance is similar to
  eventrelated models in the present setting."
- **Only the best-predicted site is reported.** The target site is chosen during model
  construction as the one with high magnitude in the future-model term, then evaluated on held-out
  data. The authors state this is done to match the reporting convention of the prior phase-
  prediction literature they compare against — a convention that includes selecting trials by
  power as well as sites by accuracy: "The previous literature has reported the case of the best
  predicted sensor, and selected trials according to power in the relevant band, which for the
  sake of comparison we adopt".
- **Table 1, the paper's headline accuracy table** (subject-wise PLV-error at the best time and
  frequency, for varimax rotation, two eigenvectors, top 25 percent of trials by past mean log
  power): best MEG6 at 0.94, best ECoG ECOG1 at 0.83, worst MEG17 at 0.51, subject-wise mean 0.72
  over n = 23 subjects. Verbatim: "When only the highest 25% of trials, by past MLP, were included,
  the performance of the model improved to PLVerror=0.94 for the best subject, with mean
  improvement over subjects of 0.17 (see Table 1)."
- **Error angles, and which condition each belongs to (corrected during the Phase 4 audit).** An
  earlier version of this card said the "mean phase error is as low as 0.5 radians, described in
  the author summary as about 20 degrees in the best cases", presenting the two as the same
  quantity. They are not, and 0.5 rad is about 28.6 degrees. The abstract says "mean phase
  prediction errors were as low as 0.5 radians at local sites". The ~20 degree figure belongs to
  the power-selected condition only: "This best PLVerror corresponds to a mean error angle of
  ~20 ̊, compared to the best case in EEG of ~40 ̊ previously reported [16]. For ECoG, power
  selected trials allow a mean error angle of ~30 ̊ in the best subject, compared to previously
  reported best results of ~60 ̊". The 40 and 60 degree figures are the comparators' numbers, not
  this paper's.
- **Variance explained**: across subjects, the low-spatial-frequency bases explain 20 to 53
  percent of the variance in phase — lower, the authors note, than when a single time sample of
  phase is entered into the PCA.
- **Power dependence**: PLV-error correlates moderately with mean log power (r = 0.3 to 0.6 for
  some frequencies in most subjects), and restricting to the highest-power quartile of trials
  improves prediction. Prediction accuracy was not strongly dependent on position in the task
  time-course.
- **Best band is subject-dependent**: best PLV-error occurred in delta, theta, alpha or beta
  depending on the subject; the example MEG subject predicted well in delta and alpha-beta but
  not theta, and the example ECoG subject showed the opposite pattern.

## Open questions / limitations

- **The dataset contains no EEG.** It is MEG and ECoG only. This strand and this project are
  about scalp EEG, and the paper's own framing of why non-local information helps rests on array
  geometry that a 32- or 64-channel scalp montage does not reproduce. Nothing here establishes
  that the same structure is recoverable after volume conduction and scalp blurring.
- The reported accuracy is for the single best-predicted site per subject, selected during model
  construction. Held-out data is used for evaluation, so this is not test-set leakage, but the
  numbers describe a favourable site rather than a typical one, and the paper gives no
  distribution over sites.
- Between-subject variation is large (PLV-error 0.73 to 0.32 over all trials; 0.94 to 0.51 in
  Table 1's power-selected condition) and unexplained beyond a correlation with signal power. With
  three ECoG subjects, the intracranial arm is effectively three case studies.
- **The size of the advantage over the temporal baseline, corrected during the Phase 4 audit.** An
  earlier version of this card said the comparison "is reported as figure panels, not as a table of
  paired values, so the size of the advantage cannot be extracted from the text", and called this
  "a reporting limitation, not an absent measurement". The second half was right and the first half
  was wrong: the paper runs a mixed linear model over all trials and reports it under "Summary
  statistics", stating that "The regression coefficients and standard errors are reported in S1
  Table" and that the temporal Fourier model "performed less well" than the large-scale and
  event-related models, which did not differ from each other. What is unavailable to this card is
  S1 Table itself, which is supplementary and not part of `source.md`; the effect size therefore
  cannot be quoted here, but it exists and is tabulated in the paper's supplement. The same section
  gives the eigenvector-configuration statistics: the all-low-plus-one and frequency-doubled
  configurations were worse than the first eigenvector alone (p < 0.001 in both cases), one/two/all
  low-spatial-frequency configurations did not differ, and rotated PCA beat both unrotated PCA and
  the leave-out-target-site condition (p < 0.001).
- The three ECoG subjects are epilepsy patients with focal cortical dysplasia, recorded during
  pre-neurosurgical monitoring. The paper does not discuss how pathological tissue might affect
  the wave structure it measures.
- The task is a self-initiated hand movement in both modalities, and the analysis window is
  ±500 ms around movement onset. No claim is made, or supportable, about resting or naturalistic
  recording.

## Citations

Primary: `alexander-2019-cortical-waves`

- `muller-2024-transformers-cortical-waves` — the other entry on this strand's
  theoretical-motivation line; argues the computational interpretation of the structure that this
  paper measures.
- Zhang et al. and the auto-regression / Fourier phase-prediction line (references [15], [16] of
  the source) — the local, within-time-series baselines whose reporting convention this paper
  adopts and whose accuracy it exceeds.
- Alexander et al., traveling-wave analyses of the same MEG dataset (references [3], [13], [23])
  — the authors' prior work supplying the multi-grid wave-fitting estimates the spatial-frequency
  results are checked against.
- Schmidt, Dynamic mode decomposition (reference [52]) — the fluid-dynamics method the approach
  is explicitly related to, differing in that this model relates past to future patterns rather
  than estimating system difference equations.
