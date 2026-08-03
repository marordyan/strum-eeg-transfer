---
slug: neuralbench
type: standard
strand: datasets-benchmarks
year: 2026
authors: [Banville, d'Ascoli, Dahan, Rapin, Careil, Benchetrit, Lévy, Panchavati, Ratouchniak, Zhang, Cascardi, Begany, Brooks, King]
venue: arXiv preprint 2605.08495
doi: null
url: https://arxiv.org/abs/2605.08495
license: null
modalities: [scalp-eeg, intracranial-eeg, meg, fmri, naturalistic-stimulus-eeg, clinical-eeg, erp]
tags: [benchmark-suite, evaluation-protocol, per-task-split-strategy, cross-subject-split, random-split, pretraining-data-overlap, balanced-accuracy, normalized-score, end-to-end-fine-tuning, checkpoint-to-benchmark-mapping]
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

The suite that declines to fix one split rule — it selects among four strategies per task, including
random splits where examples are scarce — and, uniquely among the four suites carded here, flags on
the leaderboard itself which models were pretrained on the dataset they are being evaluated on.

## Summary

NeuralBench is a framework for benchmarking artificial-intelligence models of brain activity,
released with NeuralBench-EEG v1.0: 36 tasks, 94 datasets, 9,478 subjects and 13,603 hours, run
against 14 architectures (8 task-specific networks trained from scratch and 6 pretrained foundation
models) plus handcrafted-feature, dummy and chance baselines. Two variants exist:
NeuralBench-EEG-Core v1.0, one dataset per task, and NeuralBench-EEG-Full v1.0, up to 24 datasets
per task, which allows within-task variability to be studied. Its two stated findings are that
"current foundation models only marginally outperform task-specific models" and that a large set of
tasks, especially cognitive decoding, remain hard for every model. The results bear this out in a
specific way: the top three by average per-task rank are foundation models (REVE, LaBraM, LUNA), but
CTNet at 150K parameters ranks close behind REVE at 69.2M. The framework is configuration-driven —
tasks are specified in YAML files naming the data source, the split strategy, preprocessing,
target processing, trainer settings and metrics — and no data is shipped with the package; datasets
are reached through the NeuralSet and NeuralFetch interfaces.

## Relevance to the review

This is the suite that most directly addresses the two questions this project has to answer before
it can trust any published transfer number.

First, pretraining-data overlap. NeuralBench states plainly that "as there is a limited set of
publicly available EEG datasets, some of these models saw (part of) the downstream datasets during
pretraining", marks those cells with hashed bars so that "the reported performance could be
overinflated since test subjects or examples may have been seen by the model", and keeps them in
the leaderboard rather than discarding them, "as we did not notice a clear trend suggesting
pretraining 'leakage' improves downstream performance on the same data". No other suite carded here
even raises the issue. For Phase 4, this is the concrete basis for asking, of any published
checkpoint-on-benchmark result, whether the benchmark was in the pretraining corpus.

Second, the split strategy is per task and is *reported* per task: each results panel is labelled
with whether it used a cross-subject, within-subject, or random split, alongside the total number of
examples. That makes NeuralBench the only source in this strand where a reader can see, for a given
task, which protocol produced the number — which is exactly what `brookshire-2024-data-leakage`
shows most of the translational EEG literature does not report.

Third, the task inventory contains the closest analogues to STRUM's stimulus contrast. Cognitive
decoding tasks — speech, sentence, video, word and image decoding — are all run under
*within-subject* splits in the Core release (the panels are labelled "within-subject"), while the
clinical and BCI tasks are cross-subject. So the tasks nearest this project's label type are the
ones the suite does not evaluate cross-subject, and the paper reports foundation models standing
out precisely there. That combination should be carried into Phase 4 rather than the headline rank.

## Notable details

- **Split rule.** Four strategies, chosen per task: "(1) predefined splits when provided by the
  authors, (2) 'leave-concept-out' for cognitive decoding tasks, (3) cross-subject splits, with
  optional stratification for clinical tasks, or (4) random splits when very few examples are
  available." Each model is trained or fine-tuned three times on each task, "using a single
  train/valid/test partition but three different random seeds for the initialization of the
  (non-pretrained) model weights" — so the three runs vary initialization, not the split.
- **Metrics.** One representative metric per task type: balanced accuracy for binary and multiclass
  classification, macro F1 for multilabel, Pearson correlation for regression, top-5 accuracy for
  retrieval. Additionally a normalized score `s̃ = (s − s_dummy)/(s_perfect − s_dummy)`, where 0 is
  dummy-level and 1 is the metric's theoretical ceiling. Global rankings are per-task ranks averaged
  over tasks; in the Full variant, ranks are first averaged across datasets of the same task.
- **Fine-tuning budget.** End-to-end fine-tuning under one shared recipe for all models, "to focus
  the comparison on model architecture and pretraining methodology": a linear projection head over
  average-pooled output tokens, AdamW. The authors flag this as a limitation, since "alternative
  strategies, such as linear probing, parameter-efficient finetuning ... may further improve
  performance and differentiate models from one another".
- **Checkpoints covered (6 foundation models):** BENDR, LaBraM, BIOT, CBraMod, LUNA, REVE.
  **Task-specific architectures (8):** ShallowFBCSPNet, Deep4Net, EEGNet, BDTCN, ATCNet,
  EEGConformer, SimpleConvTimeAgg, CTNet. Plus handcrafted-feature pipelines built on symmetric
  positive definite matrix representations fed to logistic or ridge regression, a chance baseline
  (an untrained randomly initialized model) and a dummy baseline (majority class or training-set
  mean).
- **Ranking result.** Highest-ranked are REVE, LaBraM and LUNA; CTNet, SimpleConvTimeAgg and
  Deep4Net rank well "despite significantly lower parameter counts (e.g. 150K parameters for CTNet
  vs. 69.2M for REVE)". BENDR and BIOT "did not perform as well overall despite their pretraining",
  which the authors attribute partly to the channel-adapter linear layer needed to match the channel
  set seen during pretraining, and for BIOT to the use of a linear rather than MLP head.
- **Task difficulty.** Near saturation: SSVEP classification, pathology, seizure detection, sleep
  staging, age regression, sex classification. Hardest: cognitive decoding (speech, sentence, video,
  word, image), mental imagery, sleep arousal, psychopathology decoding.
- **Preprocessing** includes notch filters at 50 and 60 Hz plus harmonics, channel-wise robust
  scaling at the recording level, and clamping at 20. The authors note that they have not
  systematically evaluated preprocessing effects.
- **Scale of the run.** NeuralBench-EEG-Full v1.0 requires 4,947 experiments (14 models plus chance,
  dummy and handcrafted baselines × 97 task-datasets × 3 seeds), about 11 TB of disk and roughly
  1,751 GPU-hours; median training time per experiment 2.7 minutes, mean 21.7, longest 18.2 hours.
- Datasets are reached through MOABB for the motor-imagery and P300 tasks, which is where the Full
  variant's multiple comparison points come from.
- Preliminary MEG and fMRI extensions exist, with the paper reporting "promising transfer from EEG
  to MEG".

## Open questions / limitations

- **Conflict with the sibling suites, recorded not resolved.** NeuralBench selects a split strategy
  per task and permits random splits "when very few examples are available". `omnieeg-bench` fixes
  8:1:1 at the subject level for every task and makes linear probing primary. `brain4fms` uses
  approximately 3:1:1 leave-subjects-out with group-wise cross-validation. `adabrain-bench` states
  no ratio. NeuralBench's flexibility is the sharpest disagreement in the set, because a random
  split over segments is exactly the protocol `brookshire-2024-data-leakage` shows inflates accuracy
  by tens of points; NeuralBench mitigates this by labelling every panel with its split type, but
  the labelled random-split numbers still enter the same average-rank computation as the
  cross-subject ones. Which protocol should govern, and whether a mixed-protocol average rank means
  anything, is a Phase 3 question.
- The authors state their own splitting limitation: a single partition per task "limits the
  assessment of performance variability (as compared to a cross-validated approach)", and they
  invite the community to add stochastic partitioning. With three seeds varying only weight
  initialization, the reported standard errors do not capture split-to-split variance at all.
- The pretraining-overlap flag is honest but its justification is weak: the conclusion that overlap
  does not help rests on "we did not notice a clear trend", not on a test. The overlapping cells are
  neither excluded nor separately analysed.
- The `SklearnSplit` configuration shown as the worked YAML example uses `valid_split_ratio: 0.2`
  and `test_split_ratio: 0.2` with `stratify_by: description` and no grouping key, on a
  sub-300-example single-subject dataset (MNE's sample data). That is a random split over epochs
  from one recording — appropriate for a smoke test, as the paper says, but it is also the
  configuration a new user will copy.
- The abstract says the benchmark "is evaluated on 94 datasets" and includes "14 deep learning
  architectures"; the body reconciles 14 as 8 task-specific plus 6 foundation models, and the
  compute section counts "97 task-datasets" against the 94 datasets. The counts are reconcilable but
  not stated as such.
- No dyadic or multi-person task, and no peripheral physiology channel is used as signal.

## Citations

Primary: `neuralbench`

- `adabrain-bench`, `omnieeg-bench`, `brain4fms` — the three sibling suites, each with a different
  split rule; overlapping checkpoints noted on those cards.
- `moabb` — the framework NeuralBench draws on for its motor-imagery and P300 comparison points.
- `brookshire-2024-data-leakage` — the leakage demonstration that makes NeuralBench's random-split
  option and its per-panel split labelling consequential.
- `reve-2025`, `labram-2024` (strand `eeg-models`) — the two highest-ranked checkpoints in this suite.
- `openneuro` — one of the standardized data sources NeuralSet reaches.
