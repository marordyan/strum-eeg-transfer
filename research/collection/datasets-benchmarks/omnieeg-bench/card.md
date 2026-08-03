---
slug: omnieeg-bench
type: standard
strand: datasets-benchmarks
year: 2026
authors: [Lu, Li, Shen, Lou, Xin, Chen, Wang, Chen, Fan, Huang, Xu, Hou, Wei, Liu]
venue: arXiv preprint 2606.00815
doi: 10.48550/arXiv.2606.00815
url: https://arxiv.org/abs/2606.00815
license: null
modalities: [scalp-eeg, clinical-eeg, sleep-eeg, naturalistic-stimulus-eeg, motor-imagery, resting-state-eeg]
tags: [benchmark-suite, evaluation-protocol, linear-probing, subject-level-split, 8-1-1-split, balanced-accuracy, channel-masking, few-shot, task-card, checkpoint-to-benchmark-mapping]
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

Ten EEG foundation models are ranked on 54 datasets under a *frozen-backbone linear probe* on an
8:1:1 subject-level split, and the ranking that protocol produces is not the ranking full
fine-tuning produces on the same data — which is the finding, more than the leaderboard itself.

## Summary

OmniEEG-Bench organizes EEG foundation-model evaluation into six task families — signal
reliability, biometrics and disease, consciousness and state, cognition and emotion, naturalistic
stimulus decoding, and motor and interaction — and standardizes each with a task-card specification
covering preprocessing, inputs and outputs, and metrics. It unifies 54 EEG datasets behind a single
HDF5 schema and benchmarks ten checkpoints: BENDR, BIOT, LaBraM, CBraMod, BrainOmni, FEMBA,
Neuro-GPT, NeuroLM, EEGMamba and REVE. Four evaluation protocols are implemented: cross-subject
transfer, multi-subject trial-level adaptation, zero-/few-shot adaptation, and channel-masking
robustness. Linear probing on a frozen backbone is the primary evaluation; full fine-tuning is run
additionally on every dataset "to characterize the performance ceiling of each architecture". Under
the primary cross-subject linear-probing protocol BrainOmni takes the best average rank, followed
by CBraMod and REVE; under full fine-tuning "the model rankings change substantially", with
CBraMod, LaBraM and FEMBA at average ranks 4.51, 4.88 and 5.42. The paper's headline claim is a
scaling relationship: the number of pretraining datasets and model size are both significantly
associated with better average ranks (median Spearman ρ = −0.27, Wilcoxon p = 1.1×10⁻⁷ for
pretraining-dataset count).

## Relevance to the review

The single most useful number here for this project is the linear-probing versus fine-tuning
comparison against a supervised baseline, because it is exactly the boundary between the project's
comparison 1 and comparison 2. Under full fine-tuning, seven of ten foundation models beat
EEGConformer (average rank 7.25) and nine beat EEGNet (8.24). Under linear probing, only five beat
EEGConformer and five fall behind it, which the authors state as "frozen pretrained representations
remain substantially limited for direct transfer". A project planning to use a frozen embedding
plus peripheral-physiology features — this project's third comparison — is planning to operate in
the regime where the pretrained advantage is, on this suite's evidence, roughly a coin flip against
a small supervised model.

Second, the suite includes naturalistic stimulus decoding as a task family and reports it as "one of
the most challenging task categories for current EEG foundation models", naming
natural-versus-reversed speech classification (Broderick-reverse) and speech attention detection
(Broderick-Cocktail-party) among the hardest tasks. STRUM's spoken-versus-written contrast sits in
that family, so this is the nearest published evidence about how far a checkpoint gets on a language
stimulus contrast.

## Notable details

- **Split rule.** Cross-subject: "splits are made at the subject level: subjects are partitioned
  into train/validation/test groups with a ratio of 8:1:1". Multi-subject: samples from each subject
  are split 8:1:1 over trials and pooled across subjects. Few-shot: labelled examples at ratio
  k ∈ {0.02, 0.05, 0.1, 0.3} per class drawn from the training split, with k = 0 as zero-shot.
  Channel masking: cross-subject split, with a random subset of channels zero-masked at corruption
  ratio p ∈ {20%, 40%, 60%, 80%}. Where a task has no meaningful held-out-subject formulation
  (longitudinal test-retest), the multi-subject protocol is used as a fallback and still enters the
  main leaderboard.
- **Metric.** Balanced accuracy, reported as mean and standard deviation across runs; three runs for
  cross-subject transfer and multi-subject adaptation, five for few-shot and channel masking. Each
  run uses "a pre-generated, fixed data split derived from a different random seed". Models are
  ranked by average rank across datasets rather than by pooled accuracy.
- **Fine-tuning budget.** Primary protocol is linear probing: the backbone is frozen and only a
  lightweight linear head `g(·)` mapping the representation to task logits is trained. Sampling is
  capped at "up to 40 samples per subject per class for linear probing", justified by a
  variance-stabilization analysis, "from which all subsequent splits derive". Full fine-tuning is
  additionally run on all datasets in each task category under the cross-subject setting.
- **Checkpoints covered:** BENDR, BIOT, LaBraM, CBraMod, BrainOmni, FEMBA, Neuro-GPT, NeuroLM,
  EEGMamba, REVE. Task-specific comparison points: EEGConformer and EEGNet.
- **Preprocessing fixed by the suite**: downsampling, band-pass and notch filtering, common average
  referencing, and window segmentation. All preprocessed data are stored in a standardized HDF5
  schema whose root level holds subject-level attributes such as montage and sampling rate, with
  trial groups organizing recording sessions and segment groups holding the preprocessed matrices
  and synchronized labels.
- **Hardest tasks named**: Parkinson's detection (PD31), arousal classification (DEAP-arousal),
  speech attention detection (Broderick-Cocktail-party), natural-versus-reversed speech
  (Broderick-reverse), image concept identification (ThingsEEG2), and error-related potential
  detection (Monitoring-Errp).
- **Robustness**: at corruption ratios of 0.6 and 0.8 "most models collapse to near-chance
  performance". BIOT is stable at 0.2 and 0.4.
- **Factor analysis**: publication year has the strongest association with better per-dataset rank
  (ρ = −0.40), then log parameter count (−0.21) and pretraining-dataset count (−0.27); training
  hours (−0.08) and number of training subjects (−0.10) show weaker associations, i.e. more hours
  and more subjects in pretraining do not by themselves predict downstream generalization.
- Zero-shot is implemented as nearest-neighbour label transfer in embedding space, matching each
  test sample to its most similar *validation* sample "to avoid information leakage" rather than to
  a training sample.

## Open questions / limitations

- **Conflict with the sibling suites, recorded not resolved.** OmniEEG-Bench fixes an 8:1:1
  subject-level split and makes linear probing primary. `adabrain-bench` states no split ratio in
  the paper at all and makes full fine-tuning primary. `brain4fms` uses approximately 3:1:1
  leave-subjects-out with group-wise cross-validation and full fine-tuning. `neuralbench` picks one
  of four splitting strategies per task, including random splits where examples are few. This suite
  is the one that demonstrates the disagreement matters: its own linear-probe and full-fine-tune
  rankings of the same ten models on the same 54 datasets "change substantially". Which protocol
  should govern is a Phase 3 question.
- The cap of 40 samples per subject per class is a design choice that bounds how much of a large
  dataset any model sees, and it interacts with the 8:1:1 subject split in a way the paper does not
  analyse: two datasets with the same subject count but very different trials-per-subject are
  reduced to comparable training-set sizes, which may flatten real differences in data efficiency.
- The primary leaderboard mixes protocols. Longitudinal test-retest is scored under the
  multi-subject fallback but included in the same average-rank computation as the cross-subject
  tasks, so the headline ranking is not uniformly a cross-subject ranking.
- Three runs differing only in split seed is a small basis for the standard deviations reported, and
  the paper draws model orderings from average ranks without a per-comparison significance test. The
  factor analysis does use a Wilcoxon signed-rank test on per-dataset Spearman correlations, so the
  scaling claim is tested where the leaderboard claims are not.
- The suite does not state whether any of the ten checkpoints was pretrained on any of the 54
  evaluation datasets. `neuralbench` explicitly flags such overlap for its own model set and finds
  it common; the same risk applies here and is unaddressed.
- Correction, made during review. An earlier version of this card stated that the abstract carried
  the typo "nconsistent task protocols" and that supplementary tables 5 to 7 were outside the
  retrieved document. Both were wrong: the extraction reads "inconsistent", and Supplementary Tables
  2, 5, 6 and 7 are all present, including the `#Params` column for all ten checkpoints. The
  per-dataset accuracies and the parameter counts behind the log-parameter correlation are therefore
  verifiable from this source.

## Citations

Primary: `omnieeg-bench`

- `adabrain-bench` — Wu et al. 2025. The suite whose primary protocol is full fine-tuning; overlaps
  on LaBraM, CBraMod, BIOT.
- `brain4fms` — Shen et al. 2026. Overlaps on BENDR, BIOT, LaBraM, CBraMod, BrainOmni, NeuroLM, REVE.
- `neuralbench` — Banville et al. 2026. Overlaps on BENDR, BIOT, LaBraM, CBraMod, REVE.
- `reve-2025` (strand `eeg-models`) — third-ranked under this suite's primary linear-probing
  protocol.
- `lin-2026-identity-trap` (strand `eeg-models`) — argues that a subject-level split of the kind
  this suite fixes is necessary but not sufficient, because frozen embeddings remain dominated by
  subject identity.
