---
slug: lin-2026-identity-trap
type: paper
strand: eeg-models
year: 2026
authors: [Lin, Wu, Jung]
venue: arXiv preprint 2606.06647
doi: null
url: https://arxiv.org/abs/2606.06647
license: null
modalities: [scalp-eeg, resting-state-eeg, clinical-eeg, 10-20-montage, 19-channel, 30-channel]
tags: [negative-results, subject-identity-confound, shortcut-learning, linear-probe, frozen-representations, leace-erasure, aperiodic-1f, fooof, subject-disjoint-cv, variance-decomposition]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

Subject-disjoint cross-validation is necessary but not sufficient: across 12 model-by-dataset pairs
the frozen embeddings of LaBraM, CBraMod, and REVE are dominated by subject identity at 13 to 89
times a random-Gaussian null, and where the label varies within subject, *erasing* that identity axis
makes label decoding better rather than worse.

## Summary

The paper names and diagnoses the "Identity Trap": on small-N clinical resting-state EEG, high
balanced accuracy under subject-disjoint cross-validation is ambiguous between a genuine
cross-subject marker, stable subject traits that happen to co-vary with the label in that cohort,
and an inseparable entanglement of the two. The authors propose FMScope, a frozen-representation
pre-flight protocol of five diagnostics — variance decomposition, closed-form subject-axis erasure
(LEACE), aperiodic 1/f ablation via FOOOF, layer-wise label probing, and within-subject direction
consistency — and apply it to three open-weight transformer foundation models across four public
resting-state datasets arranged in an a priori 2x2 layout: whether the label varies within subject,
crossed with whether a consensus cross-subject EEG marker exists in the literature. Three findings
follow. The subject-variance dominance is universal (12 of 12 frozen pairs, rising in all 12 under
fine-tuning by +10 to +63 percentage points) but lies on a removable linear axis, and erasing it
improves label decoding by +6 to +12 points in the primary within-subject cells. The aperiodic 1/f
background is one identifiable carrier of subject identity for LaBraM and CBraMod (removing it drops
the subject probe by 9 to 19 points) but not for REVE. And fine-tuning amplifies label variance only
in cells where the literature already establishes a cross-subject marker (Mann-Whitney U, one-sided
p = 0.0022, n = 12).

## Relevance to the review

This is the card that constrains how this project must design its STRUM evaluation, and it does so
for exactly the three checkpoints the strand cares about. Two mechanisms transfer directly.

First, the fine-tuning paradox. Across 12 pairs, full fine-tuning beats a frozen linear probe in
only 2; ten fall within a single percentage point of the corresponding probe. If STRUM's spoken
versus written contrast behaves like these cells, the expensive comparison this project plans —
fine-tune a pretrained checkpoint — may return nothing a frozen probe would not have given, and the
paper supplies a cheap pre-flight that would say so before the compute is spent.

Second, and more sharply, the 2x2 axis that predicts *whether pretraining helps at all* is whether
the label varies within subject. STRUM's planned label is stimulus condition — spoken versus written
language — which is a within-subject contrast: the same participant experiences both. That places
STRUM in the paper's within-subject row, which is the favourable row, and the paper's guidance for
that row is concrete: erase the subject axis before decoding, because identity dominance is
suppressing the label signal rather than carrying it. It also means the trait-cell failure mode
(where no consensus marker exists and the layer-wise label probe descends monotonically to chance)
is not the failure mode STRUM is most exposed to.

Third, the paper is a worked example of a baseline this project needs. On EEGMAT — the
within-subject, consensus-marker cell — a classical handcrafted-feature logistic regression at 0.847
balanced accuracy beats every foundation-model tier, the best of which is 0.755. A small
supervised-from-scratch comparison is not a formality here; it won.

## Notable details

- **Pretraining corpus and total hours**: not applicable to this paper's own contribution — it
  pretrains nothing. It restates the three audited models' corpora: LaBraM ~2,500 hours of mixed
  EEG; CBraMod a cleaned ~9,000-hour subset of TUEG (whose total is ~15,000 subjects, ~27,000
  hours); REVE ~60,000 hours from 92 datasets covering 25,000 subjects.
- **Parameter count**: the paper does not report parameter counts for the three models. It reports
  embedding dimension instead: d = 200 (LaBraM), 200 (CBraMod), 512 (REVE).
- **Input contract**: standardized across all four cells so the models are compared under one
  contract — each backbone receives a 5-second by C-channel epoch at 200 Hz. Preprocessing is
  per-channel mean subtraction, 1–45 Hz zero-phase Butterworth band-pass, 5-second non-overlapping
  epochs. Datasets are 19-channel 10-20 montage except Stress-DASS at 30 channels. Pooling is left
  to each backbone's release default and not re-pooled: LaBraM mean-pools patch tokens after
  stripping a prepended CLS token; CBraMod applies 2D adaptive average pooling over the (channel,
  patch) grid; REVE returns its attention-pooling secondary-task token. All three receive raw
  microvolt-scale input and apply their own release-default internal rescaling. The input contract
  was held fixed rather than swept.
- **Most informative transfer number, with baseline**: on EEGMAT (within-subject x consensus
  marker), classical handcrafted-feature logistic regression reaches 0.847 +/- 0.050 balanced
  accuracy under subject-disjoint 5-fold CV, versus the best foundation-model result of 0.755
  (LaBraM linear probe 0.755 +/- 0.070, REVE linear probe 0.755 +/- 0.021) and versus EEGNet trained
  from scratch at 0.671 +/- 0.042. The classical baseline beats every pretrained tier by ~9 points.
  ADFTD is the one cell where pretraining wins: LaBraM linear probe 0.814 +/- 0.023 against EEGNet
  0.793 +/- 0.016, a +2.1 point margin.
- **The fine-tuning paradox**: "Fine-tuning rarely beats the frozen linear probe: 10 of 12 pairs
  fall within +/-1pp of the corresponding LP." On the two no-consensus cells (SleepDep, Stress) all
  four tiers — classical, non-FM deep, FM linear probe, FM fine-tuned — fall inside a 0.43–0.57
  band, i.e. at or near chance for binary tasks.
- **A 45-point reproduction gap**: a prior evaluation reported 0.9047 balanced accuracy on the
  Komarov stress dataset using a fixed 80/10/10 split in which the same subjects appear in different
  folds (best of four seeds; the worst seed reached 0.67). Under subject-disjoint CV the present
  authors observe 0.43–0.50 across three foundation models and five classical baselines. "The gap is
  ~45pp."
- **Erasure improves decoding**: closed-form LEACE erasure drives a linear subject probe to chance
  in all 12 pairs. Where the label varies within subject, erasing identity *improves* label decoding
  by +6 to +12 points in the primary cells and +4 to +27 points across four external
  consensus-marker cohorts (one-sided sign test p < 10^-3).
- **Carrier is model-specific**: removing the FOOOF aperiodic 1/f component drops the linear subject
  probe by 9 to 19 points uniformly across all four cells for LaBraM and CBraMod. REVE's subject
  probe is already saturated at >= 0.93 balanced accuracy and shifts by <= 1.2 points, and REVE
  retains a nonlinearly-decodable subject residual after linear erasure. The authors report this
  two-versus-one split descriptively, not mechanistically.
- **Evaluation protocol**: subject-stratified group 5-fold CV grouped by subject; recording-level
  aggregation by averaging per-window posteriors and thresholding at 0.5 (threshold fixed by design,
  not tuned); balanced accuracy averaged over three fine-tuning seeds {42, 123, 2024} and eight
  linear-probe seeds. Each model fine-tuned under its own published repository configuration, applied
  uniformly, with no per-dataset hyperparameter sweep.
- Datasets: EEGMAT (36 subjects x 72 recordings, within-subject paired, consensus marker); ADFTD (65
  subjects, one recording each, subject-trait, consensus marker); SleepDep (36 x 72, within-subject
  paired, no consensus marker); Stress-DASS (17 subjects x 70 recordings, subject-trait, no
  consensus marker).

## Open questions / limitations

- The authors' own stated limits: the three-model panel differs along five design axes at once
  (spectral processing in the pretraining pipeline, reconstruction loss, corpus diversity, positional
  encoding, and REVE's attention-pooling secondary task), so no cross-model contrast can be
  attributed to any single axis without a controlled architecture-level ablation.
- Single-session ADFTD cannot separate disease state from stable subject traits by data alone, and
  the authors note the limit is intrinsic rather than fixable with more recordings, because diagnosis
  is a fixed subject attribute. For such labels they argue the discriminative features must be
  validated against external physiological evidence.
- All analyses assume subject-disjoint CV, recording-level labels, and a >= 19-channel 10-20
  montage. Cells with finer label resolution or trial-level splitting "may produce different
  readings" — which matters for STRUM if its labels are epoch-level rather than recording-level.
- No Riemannian or Euclidean pre-alignment was applied before fine-tuning. The authors flag this as a
  natural follow-up that "may attenuate the subject-axis amplification", so the reported identity
  dominance is measured without the standard engineering mitigation.
- Only one dataset per cell, so the 2x2 result is a sampling layout rather than a replicated design.
  The authors list replication with a second dataset per cell as future work.
- Statistical power is limited: n = 12 pairs for the cell-conditional test, and the sign test for
  erasure gains pools primary cells with four external cohorts.
- Extraction discrepancy worth flagging for anyone re-reading the source: the prose at Section 4.1
  says "On EEGMAT the classical RF beats every FM tier", while the row in Table 2 is labelled
  "Classical LR" and Section 3.6 describes a logistic-regression comparator. The value 0.847 is
  consistent across both; only the model name is inconsistent. This card follows Table 2 and
  Section 3.6 and calls it logistic regression.
- The paper offers no evidence at all about dyadic or two-person recording setups, and its four
  cohorts are all resting-state or rest-plus-task single-subject clinical data.

## Citations

Primary: `lin-2026-identity-trap`

- `labram-2024` — Jiang et al., ICLR 2024. One of the three audited backbones; its subject probe
  drops 9 to 19 points when the aperiodic 1/f component is removed.
- `reve-2025` — El Ouahidi et al., NeurIPS 2025. The third audited backbone; the only one with no
  measurable aperiodic dependence and a nonlinearly-decodable subject residual after linear erasure.
- Wang et al., CBraMod — the second audited backbone, pretrained on a cleaned ~9,000-hour TUEG
  subset; also the source of the 0.9047 stress-dataset headline the paper fails to reproduce.
- Brookshire et al. (2024) — the prior critique establishing that trial-level cross-validation
  inflates clinical EEG accuracy via subject leakage; this paper starts where that one stops.
- Finn et al. (2015) and Mantwill et al. (2022) — resting-state fMRI fingerprinting, cited as
  cross-modality evidence that subject-identifying structure and behaviour-predictive structure
  occupy different systems.
