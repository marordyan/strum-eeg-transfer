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
md_quality: rough
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
of the error reaches 0.73 in the best subject and falls to 0.32 in the worst; the corresponding
mean phase error is as low as 0.5 radians, described in the author summary as about 20 degrees in
the best cases. The comparator is a purely temporal Fourier model fitted at the same site, which
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
  the best subject (0.32 in the worst), and states that the temporal-only model "gives somewhat
  higher error angles at the times and frequencies of best predictions" while admitting good
  predictions over a much narrower frequency range. The comparison is presented as
  time-by-frequency panels in Figure 3A rather than as paired scalars, so the margin cannot be
  quoted as a single number from the source.
- **Only the best-predicted site is reported.** The target site is chosen during model
  construction as the one with high magnitude in the future-model term, then evaluated on held-out
  data. The authors state this is done to match the reporting convention of the prior phase-
  prediction literature they compare against.
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
- Between-subject variation is large (PLV-error 0.73 to 0.32) and unexplained beyond a
  correlation with signal power. With three ECoG subjects, the intracranial arm is effectively
  three case studies.
- The comparison against the purely temporal baseline is reported as figure panels, not as a
  table of paired values, so the size of the advantage cannot be extracted from the text. This is
  a reporting limitation, not an absent measurement: the paper reports it, but at a granularity
  the card cannot quote.
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
