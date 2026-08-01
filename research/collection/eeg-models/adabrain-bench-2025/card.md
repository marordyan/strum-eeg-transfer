---
slug: adabrain-bench-2025
type: standard
strand: eeg-models
year: 2025
authors: [Wu, Ren, Wang, Zhu, Song, Liu, Zheng, Bai, Ouyang, Song]
venue: arXiv preprint 2507.09882
doi: null
url: https://arxiv.org/abs/2507.09882
license: null
modalities: [scalp-eeg, clinical-eeg, sleep-eeg, motor-imagery, emotion-eeg, visual-decoding-eeg]
tags: [benchmark, third-party-evaluation, cross-subject, multi-subject, few-shot, linear-probe-vs-finetune, transfer-score, normalization-ablation, pretraining-ablation, mit-licensed-pipeline]
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

A third-party benchmark that runs four released EEG checkpoints and four supervised baselines
through one adaptation pipeline on 13 datasets, and finds that the pretrained models win on
average — by 6.5 macro-average points cross-subject — while losing outright on every
clinical-monitoring task, and that one of them scores below chance on 4-class motor imagery under
full fine-tuning.

## Summary

AdaBrain-Bench standardizes the evaluation of publicly released EEG foundation models. It fixes
13 datasets across 7 BCI application areas, a single adaptation pipeline, and three transfer
regimes: *cross-subject* (fine-tune on one cohort, test on a disjoint cohort), *multi-subject*
(train and test on the same cohort but different sessions or trials), and *few-shot* (fine-tune
on a sampled fraction r of the training data, r from 0.02 to 0.5). Four released checkpoints —
BIOT, EEGPT, LaBraM, CBraMod — are compared against four supervised architectures — EEGNet, LDMA,
ST-Transformer, Conformer — all trained under the same protocol. Beyond the headline tables it
runs four ablations that matter more than the ranking: pretraining versus training the same
foundation architecture from scratch; linear probing versus full fine-tuning; the number of
training subjects; and the choice of normalization. It defines a *transfer score* as the relative
improvement of a pretrained model over its own trained-from-scratch counterpart.

## Relevance to the review

This is the strand's most decision-relevant entry for choosing a checkpoint, because it is the
only source that runs several of them under one pipeline with supervised baselines included, and
because three of its four ablations map directly onto choices this project must make.

The pretraining ablation is the direct evidence for comparison 1 versus comparison 2: "LaBraM and
CBraMod with pretraining outperform the non-pretrained counterpart by over 10% and 7% in average",
with gains "more pronounced on datasets with limited scale of training data, including BCI-IV-2A
and EEGMAT, compared to datasets with large amount of data, including SHHS, HMC, and TUAB". STRUM
is a small dataset, so this is the regime the project sits in.

The subject-count ablation puts a number on the project's cohort-size question: cross-subject
accuracy climbs steeply with the number of training subjects and "tends to plateau at
approximately 40 subjects", with a single-subject training set on SHHS giving CBraMod 40.70
percent balanced accuracy and a stated 23.09-point gain at 40 subjects.

The normalization ablation is a practical warning. The best normalization differs by model and by
dataset — CBraMod gains 12 points on EEGMAT from z-score over unit rescale (88.89 against 76.94)
while LaBraM is unaffected (85.83 either way) — so a checkpoint's reported number is partly a
property of a preprocessing choice that the project would have to re-tune.

Finally, the paper records each checkpoint's supported channel count, which is the input-contract
fact that determines whether STRUM's montage can be fed to it at all.

## Notable details

- **Pretraining corpus and total hours**: not applicable to this benchmark, which pretrains
  nothing. It reports, for the four evaluated checkpoints: BIOT pretrained on six clinical
  seizure and sleep datasets supporting 18 predefined channels; EEGPT on 246 hours from five
  datasets; LaBraM on about 2,500 hours from around 20 datasets, supporting 137 channels;
  CBraMod on approximately 27,000 hours from TUEG. These figures are the benchmark's
  characterization of other people's models and should be checked against those models' own cards
  before being quoted (see limitations).
- **Parameter count**: not applicable to the benchmark. It lists EEGPT at 25 million parameters
  and refers to LaBraM at 5.8M and CBraMod at 4M when arguing that EEGPT's model scale is
  disproportionate to its pretraining data ("model scaling should be proportional to available
  training data").
- **Input contract**: the benchmark's own contribution here is the supported-channel inventory —
  BIOT 18 fixed channels, EEGPT 58, LaBraM 137, CBraMod arbitrary via input-conditioned channel
  embedding. Its 13 datasets span 1 to 63 channels, 100 Hz to 1,000 Hz native sampling, and 1 s
  to 30 s windows. The BIOT bottleneck is stated explicitly: "its support for fixed 18 channels in
  its pretrained version... is incompatible with downstream tasks such as SEED and SEED-IV (62
  channels), potentially diminishing the spatial cues of downstream EEG signals".
- **Most informative transfer number, with baseline**: cross-subject macro-average across all 13
  datasets — LaBraM 64.61 and CBraMod 62.66 against the best supervised model, Conformer, at
  58.12 and EEGNet at 56.32. That is a 6.5-point margin for the best pretrained model over the
  best supervised one, measured under one pipeline. The same table shows BIOT at 58.42 and EEGPT
  at 55.00, i.e. two of the four checkpoints are level with or below the best supervised
  baseline.
- **Where the pretrained models lose**: "for clinical monitoring tasks, including TUAB, Siena,
  HMC, and Sleep-EDF, foundation models perform comparable or even worse than traditional
  models". On Sleep-EDF the best foundation model reaches 69.47 balanced accuracy against 69.55
  for the best traditional one; on Siena, EEGNet's 72.29 beats every foundation model (best BIOT
  at 71.67); on HMC, Conformer's 73.84 beats every foundation model. The authors attribute this to
  those datasets being large enough that supervised learning suffices.
- **A below-chance result**: EEGPT under full fine-tuning reaches 25.81 balanced accuracy on
  BCI-IV-2A, a 4-class task where chance is 25 percent. Under linear probing the same checkpoint
  reaches 47.89. The authors attribute the collapse to overfitting given EEGPT's parameter count,
  and thereafter report linear-probing results for EEGPT and full fine-tuning for the others — a
  per-model protocol change that is stated but complicates the multi-subject table.
- **Linear probing is generally worse**: "Compared to fine-tuning, linear evaluation consistently
  yields lower performance across most datasets, including those with limited samples (e.g.,
  EEGMAT)". CBraMod on BCI-IV-2A falls from 47.71 to 32.32. EEGPT is the exception, in both
  directions listed above.
- **Multi-subject versus cross-subject**: cross-subject is consistently worse. On SEED, the drop
  is 15 points for LaBraM, 19 for CBraMod, 7 for EEGPT. The authors propose the multi-subject
  setting as "a natural upper bound to quantify the performance drop when attempting to generalize
  across subjects". In the multi-subject table, BIOT (51.96) and EEGPT (51.67) fall below EEGNet
  (52.64) and Conformer (53.66) on macro-average.
- **Transfer score** (relative improvement over the same architecture trained from scratch),
  averaged across few-shot ratios: CBraMod 0.2761, LaBraM 0.1773, EEGPT 0.0789, BIOT −0.0573.
  BIOT's average is negative, driven by −0.3489 at r = 0.3. Cross-subject transfer scores are
  BIOT 0.0264, EEGPT 0.0764, LaBraM 0.2373, CBraMod 0.1391.
- **Few-shot**: CBraMod beats its non-pretrained version by 10 and 12 points at r = 0.05 and 0.1
  on SEED but by only 3 points at full data, and by 14.09 points on BCI-IV-2A at 33 percent of
  the training data. EEGPT underperforms across few-shot ratios on SEED-IV (27.93 at r = 0.5
  against BIOT's 37.36).
- **Release**: benchmark pipeline and data-splitting instructions on GitHub under an **MIT
  License**, stated explicitly in the Code Availability section. This is the only entry in the
  strand so far where a licence for released artefacts is stated at all.
- Datasets: SEED, SEED-IV (emotion), EEGMAT (workload), SEED-VIG (vigilance, regression),
  BCI-IV-2A, SHU (motor imagery), Things-EEG (visual retrieval), TUEV, TUAB, Siena (clinical
  anomaly), HMC, SHHS, Sleep-EDF (sleep staging).

## Open questions / limitations

- **The pretraining-hour figures it attributes to other models should not be quoted from here
  without checking the source.** It credits CBraMod with "approximately 27,000 hours", which is
  the size of the raw TUEG corpus rather than of the retained pretraining set that CBraMod's own
  paper reports. The card for `cbramod-2025` records what that paper itself says. This affects
  the benchmark's argument that EEGPT's pretraining data is small relative to its parameter
  count, which is made by comparing these three figures.
- The protocol is not uniform across models: after observing EEGPT's collapse under full
  fine-tuning, the authors report linear probing for EEGPT and full fine-tuning for the other
  three in the multi-subject table. This is disclosed, but it means the multi-subject
  macro-averages compare different adaptation strategies.
- Only four checkpoints are evaluated, chosen for being open source. REVE, BrainWave, Brant,
  NeuroGPT and EEGFormer are absent, so "brain foundation models" in the conclusions means these
  four.
- The pretraining ablation, the subject-count ablation and the linear-probe comparison are all
  presented as figures (Figures 2a, 3a, 3b) rather than tables. The percentages quoted on this
  card ("over 10% and 7% in average", "10.75% and 18.19% lower", "40.70%... 23.09% increase") are
  the authors' prose summaries of those figures, not values read off them, and per-dataset numbers
  for those ablations cannot be recovered from the paper.
- Improvements are reported in percent throughout without stating whether relative or absolute.
  Where both endpoints are given (SHHS: 40.70 percent with one subject, "23.09% increase" with 40)
  the convention appears to be absolute points, but it is never defined.
- Transfer score is defined as relative improvement over a from-scratch counterpart, which means
  a model with a weak from-scratch baseline scores well for reasons unrelated to representation
  quality. The metric is not validated against anything.
- No statistical testing is reported anywhere: no confidence intervals, no repeated runs, no
  significance tests. Several of the conclusions rest on macro-average differences of a few
  points across 13 heterogeneous datasets and metrics.
- Typographical error worth knowing when searching the source: the normalization table labels the
  EEGMAT dataset "EDMAT".
- Carded as `type: standard` rather than `paper` because what it contributes is an evaluation
  protocol and a released pipeline; the arXiv document is the description of that standard.

## Citations

Primary: `adabrain-bench-2025`

- `labram-2024` — the best-performing checkpoint in both the cross-subject and multi-subject
  macro-averages, and one of the two whose pretraining ablation shows a double-digit gain.
- `cbramod-2025` — the checkpoint with the highest transfer score, credited by the benchmark to
  its input-conditioned channel embedding adapting to arbitrary channel configurations.
- `biot-2023` — the checkpoint whose fixed 18-channel input contract the benchmark identifies as
  its bottleneck, and whose average few-shot transfer score is negative.
- `eegpt-2024` — the checkpoint that falls below chance on BCI-IV-2A under full fine-tuning and
  recovers under linear probing.
- Lawhern et al., EEGNet (2018) and Song et al., EEG Conformer — the supervised baselines that
  beat every foundation model on the clinical-monitoring tasks.
