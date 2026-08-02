---
slug: zare-2026-stress-testing
type: paper
strand: eeg-models
year: 2026
authors: [Zare]
venue: arXiv preprint 2607.24519
doi: null
url: https://arxiv.org/abs/2607.24519
license: null
modalities: [scalp-eeg, resting-state-eeg, clinical-eeg, 10-20-montage, bipolar-montage, 2-channel-eeg, 19-channel, 21-channel]
tags: [negative-results, negative-controls, random-initialisation, label-permutation, dataset-identity, linear-probe, leave-one-subject-out, cross-population-transfer, classical-features, benchmark]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

A randomly-initialised encoder outperforms pretrained REVE on Korean dementia classification
(0.659 versus 0.570 AUROC), and a linear probe separates any tested pair of datasets from frozen
REVE embeddings at AUROC 1.000 while the same pipeline decodes the actual diagnosis at 0.528 —
so the leading variance directions encode which dataset a recording came from, not the clinical label.

## Summary

Zare benchmarks six pretrained EEG models (LaBraM, EEGMamba, CBraMod, REVE, BENDR, BIOT) on five
clinical tasks across four datasets under frozen linear probing with leave-one-subject-out,
subject-grouped, or explicitly identified recording-level splits, then applies a battery of targeted
negative controls to selected REVE findings: random initialisation, random features, label
permutation, scrambled-label fine-tuning, and projection-method sensitivity. The results are mixed
by design and by outcome. On an external Korean dementia cohort (CAUEEG, 3-way) frozen REVE reaches
0.568 AUROC against 0.769 for classical handcrafted features, and the ordering survives on the
cohort's own patient-disjoint held-out split (0.565 versus 0.768). Dataset identity is decodable from
frozen REVE embeddings at or near ceiling even after projection to 50 principal components, whereas
3-way diagnosis under the same pipeline reaches 0.528. On Alzheimer's disease, subject-level
aggregation and a stronger classical comparator remove a nominal epoch-level advantage (classical
0.878 versus REVE 0.867). The clearest controlled positive is cross-subject ictal detection on
CHB-MIT (n = 23), where pretrained REVE reaches 0.793 AUROC against 0.701 for a randomly-initialised
encoder of the same architecture and 0.505 for random features, with label permutation at 0.500. All
experiments ran on an Apple M3 with 16 GB and no cloud GPU.

## Relevance to the review

The value of this card to the project is the control battery, not the leaderboard. Three controls are
directly portable to a STRUM experiment and each answers a question a single accuracy number cannot.
Random initialisation tests the pretrained weights against the architecture — the same comparison
`reve-2025` makes internally, here run by a third party and reaching the opposite conclusion on a
different cohort. Label permutation bounds probe capacity, i.e. it detects when a pipeline can fit
anything. Scrambled-label fine-tuning tests whether label correctness contributes to adaptation at
all. For a project whose central question is whether pretraining beats a small supervised model on a
small dataset, these are the checks that separate a real gain from a pipeline artefact, and the paper
supplies them as a concrete recipe rather than a principle.

The dataset-identity probe is the second transferable idea, and it bears on STRUM's design directly.
If a linear probe recovers dataset membership from frozen embeddings at ceiling while the clinical
label sits near chance, then any evaluation that pools recordings from more than one source risks
scoring on provenance. STRUM is a single dataset, which limits the exposure — but the same logic
applies within it to any variable that tracks recording session or site.

The paper also confirms, from an independent direction, the pattern `lin-2026-identity-trap` reports:
frozen foundation-model representations on small clinical cohorts are often not better than classical
features, and where a gain appears it is fragile to the choice of evaluation unit.

## Notable details

- **Pretraining corpus and total hours**: not applicable to this paper's own contribution — it
  pretrains nothing. It tabulates the six audited models' corpora: LaBraM-Base 2,500 h; EEGMamba
  16,724 h; CBraMod 9,200 h; REVE-Base 60,000 h; BENDR TUH at 256 Hz (hours not given); BIOT six
  datasets (TUH, SHHS, CHB-MIT, plus three further biosignal datasets).
- **Parameter count**: reported per model — LaBraM-Base 5.8M, EEGMamba 3.3M, CBraMod 4.9M backbone
  (8.1M with task heads), REVE-Base 69.4M (512-d, 22 layers), BENDR 157M, BIOT 3.2M. The paper's own
  reading: "Parameter count alone does not order the models: BENDR is [the largest and not the
  best]", and on sleep the ordering "does not track parameter count".
- **Input contract**: one harmonized pipeline with documented per-model exceptions — resample to
  200 Hz, FIR band-pass 0.5–70 Hz, common average reference, epoch into 4.0-second non-overlapping
  windows, artifact rejection, per-channel z-score within each accepted epoch, clip at +/-8 standard
  deviations. Exceptions matter and the author flags them as limitations rather than results: BENDR
  is resampled *back* to 256 Hz after the shared 70 Hz band limit and needs 21-channel inputs
  truncated and 19-channel inputs zero-padded with a dead channel (its Conv1d encoder was pretrained
  on 20 channels at 256 Hz with 96x temporal downsampling); LaBraM's 128-channel position embeddings
  are linearly interpolated to each dataset's channel count; EEGMamba's fixed channel-count-specific
  patch embeddings restrict it to the 21-channel and 2-channel tasks and exclude it from the
  19-channel and 18-channel cohorts. REVE needs no interpolation because it consumes 3D coordinates,
  but its embedding dimension scales with channel count since it does not spatially pool.
- **Most informative transfer number, with baseline**: on CAUEEG 3-way Korean dementia
  classification, frozen REVE reaches 0.568 AUROC against 0.769 for classical handcrafted features —
  a ~20 point deficit — and the ordering holds on the authors' patient-disjoint held-out split
  (0.565 versus 0.768). **Correction, made during a Phase 5 traceability spot-check.** An earlier version of this
  bullet said "under every tested condition classical features beat frozen REVE by at least 12.7
  points". That is false as a universal and the string "12.7" does not occur in the source at all.
  The robustness sweep it paraphrases is scoped to CAUEEG alone, and elsewhere in the same paper REVE
  beats classical: ds004504 three-way 0.795 against 0.754, TUAB by +9.8, CHB-MIT 79.3 against 70.0,
  and ds004504 AD-versus-HC 82.8 against 80.6. The correct statement is that the classical advantage
  is large and robust **on CAUEEG**, where the sweep over probe family and epoch length never reverses
  it, and that the direction is cohort-dependent across the paper as a whole. Separately, and more damaging to the pretraining claim specifically, a
  **randomly-initialised encoder of the same architecture outperforms pretrained REVE on the same
  task, 0.659 versus 0.570**.
- **The one controlled positive**: CHB-MIT cross-subject ictal detection, full 23-patient cohort,
  held-out patients: pretrained REVE 0.793 AUROC, random-initialised encoder 0.701 (+9.2 points for
  pretraining), random features of the raw signal 0.505, label permutation 0.500. Stable to a +/-30 s
  guard band (0.798) and to drawing negatives from separate seizure-free recordings (0.787). The
  author attributes the cleanliness to positives and negatives sharing recording sessions, which
  reduces session-level confounding.
- **Dataset identity dominates the leading variance directions**: a linear probe separates ds004504
  from CAUEEG frozen REVE embeddings at AUROC 1.000, including after projection to the top 50
  principal components; all tested within-Western dataset pairs also separate at ceiling; a
  band-limited replication (0.5–40 Hz, per-epoch z-scored) still reaches 0.9998. The same PCA-50
  pipeline decodes Korean 3-way diagnosis at 0.528.
- **Sleep and differential diagnosis**: no foundation model beats classical features on the
  2-channel binary Sleep-EDF task (classical 68.6%). AD-vs-FTD remains difficult under all evaluated
  frozen probes. The paper corroborates AdaBrain-Bench on two points: foundation models performed
  comparably to or worse than traditional models on clinical-monitoring tasks (best FM 69.47% versus
  69.55% for the best traditional model on Sleep-EDF), and linear probing consistently underperformed
  fine-tuning.
- **A methodological trap worth reproducing**: CAUEEG ships 21 channels; the author uses the
  19-channel 10-20 montage after excluding EKG and Photic, noting that "retaining those two channels
  raises apparent CAUEEG AUROC, because a linear probe can exploit cardiac and stimulation-marker
  variance that is not cortical signal." This is a direct warning for any pipeline that keeps
  auxiliary channels in the input.
- Projection-method sensitivity is reported honestly as *not* a test of pretraining: Gaussian random
  projection and PCA of the same pretrained embeddings perform similarly on Alzheimer's (GRP-200
  0.875 versus PCA-200 0.860), which the author notes bears on the projection choice only, since both
  operate on pretrained features.

## Open questions / limitations

- The author's own stated limits, which are unusually candid: the benchmark is heterogeneous across
  tasks, cohorts, montages, corpus exposure, and split structures, so cross-task patterns are
  descriptive rather than causal claims about scale or channel density.
- CAUEEG primary cross-validation is recording-level because public patient identifiers are
  unavailable; the patient-disjoint split is a sensitivity bound only, and repeat recordings within
  training "remain unquantified". The recording-level cross-validation gaps are therefore upper
  bounds.
- The dataset-identity probes confound site with hardware, preprocessing, population, diagnosis
  composition, and dataset history. They establish decodable dataset membership and nothing more —
  the author is explicit that recording site is not isolated.
- BENDR and LaBraM results are contaminated by sampling-rate, bandwidth, channel-padding, and
  position-mapping mismatches against their pretraining pipelines, and the author states they
  "should not be interpreted as clean tests of pretraining objective". Only REVE received the
  targeted control battery.
- BIOT's pretraining includes CHB-MIT and TUH, so its results on those datasets are in-domain, and
  TUAB is in-domain for several models. Corpus-exposure confounds are acknowledged but not removed.
- Statistical comparisons are limited by small numbers of independent subjects or folds, overlapping
  cross-validation training sets, and multiple exploratory analyses; the author explicitly prefers
  effect estimates and controls over confirmatory significance testing, so no claim here carries a
  corrected p-value.
- CHB-MIT uses bipolar derivations with approximate positional coordinates — which matters
  specifically for REVE, whose whole mechanism is coordinate-based — and per-epoch normalization
  removes absolute amplitude. An amplitude-aware classical comparator remains unevaluated, so the one
  clean positive result rests on a montage whose coordinates are approximated.
- Internal inconsistency in the source: Section 3.1 opens "Seven pretrained EEG foundation models
  ... were evaluated" while Table 1, the abstract, and the conclusion all say six, and Table 1 lists
  six rows. This card follows the abstract, Table 1, and the conclusion.
- No dyadic or two-person data, and no task with a within-subject stimulus-condition label of the
  kind STRUM plans, so the paper's cell-by-cell conclusions do not map onto STRUM's label structure
  as directly as `lin-2026-identity-trap`'s 2x2 does.

## Citations

Primary: `zare-2026-stress-testing`

- `reve-2025` — El Ouahidi et al., NeurIPS 2025. The model the control battery targets; the paper
  contradicts REVE's own pretraining ablation on the Korean cohort (random init beats pretrained) and
  confirms it on CHB-MIT (+9.2 points over random init).
- `labram-2024` — Jiang et al., ICLR 2024. Benchmarked here at 5.8M parameters; its learned position
  embeddings had to be linearly interpolated, which the author flags as invalidating it as a clean
  test.
- Wang et al., CBraMod — benchmarked at 4.9M backbone parameters, pretrained on ~9,200 hours of TUH.
- Kostas et al., BENDR — the wav2vec-2.0-derived contrastive predecessor, at 157M the largest model
  in the panel and not the best, which is the paper's evidence that parameter count does not order
  performance.
- AdaBrain-Bench — the prior standardized benchmark whose scope this paper positions against (four
  models, full fine-tuning primary, no non-Western cohort, no negative controls) and which
  corroborates two of its findings.
