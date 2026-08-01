---
slug: adabrain-bench
type: standard
strand: datasets-benchmarks
year: 2025
authors: [Wu, Ren, Wang, Zhu, Song, Liu, Zheng, Bai, Ouyang, Song]
venue: arXiv preprint 2507.09882 (v2, 5 Aug 2025)
doi: null
url: https://arxiv.org/abs/2507.09882
license: null
modalities: [scalp-eeg, clinical-eeg, motor-imagery, emotion-eeg, sleep-eeg, visual-decoding]
tags: [benchmark-suite, evaluation-protocol, cross-subject-split, multi-subject-split, few-shot, transfer-score, balanced-accuracy, full-fine-tuning, linear-probe, checkpoint-to-benchmark-mapping]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

A benchmark that fixes the adaptation pipeline rather than the leaderboard: 13 EEG datasets across
7 task families are run through one preprocessing and fine-tuning recipe under three named transfer
settings (cross-subject, multi-subject, few-shot), so that the four public checkpoints it evaluates
can be compared on something other than each paper's own choice of split.

## Summary

AdaBrain-Bench evaluates four publicly released EEG foundation models — BIOT, EEGPT, LaBraM,
CBraMod — against four supervised baselines (EEGNet, LDMA, ST-Tran, Conformer) on 13 public
datasets spanning emotion recognition, workload classification, vigilance estimation, motor imagery,
visual decoding, clinical anomaly detection, and sleep staging. Its stated motivation is that
"even for identical tasks, the data splitting strategies and data preprocessing pipelines are
inconsistent across studies, causing significant performance fluctuations". Three evaluation
settings are defined: cross-subject transfer (test subjects "explicitly excluded from training"),
multi-subject adaptation (same subject cohort, different recording sessions or trials), and few-shot
transfer (a sampled proportion of the training data per class per subject). Full fine-tuning is the
primary adaptation strategy, with linear probing reported as a secondary. Under cross-subject
transfer, LaBraM and CBraMod reach macro-average scores of 64.61 and 62.66 against 58.12 for the
best supervised baseline (Conformer); under multi-subject adaptation the same two lead at 62.87 and
61.06, while BIOT (51.96) and EEGPT (51.67) fall *below* EEGNet (52.64) and Conformer (53.66). The
paper also defines a transfer score combining the relative gain of a pretrained model over its own
trained-from-scratch counterpart with the relative closure of the gap to an assumed upper bound.

## Relevance to the review

This is the closest published analogue to the evaluation this project will have to design, and it
is the reference point for deciding whether a STRUM protocol is comparable or bespoke. Three of its
specifics bear directly on the plan. First, its cross-subject definition is subject-disjoint by
construction, which is the minimum bar the `lin-2026-identity-trap` card argues is necessary but
not sufficient. Second, it reports the pretraining ablation this project's comparison 1 versus
comparison 2 needs: models trained from scratch on the same downstream data, with LaBraM and
CBraMod gaining "over 10% and 7% in average" from pretraining, and the gain "more pronounced on
datasets with limited scale of training data, including BCI-IV-2A and EEGMAT". Third, and most
directly, it measures the number of training subjects needed: cross-subject accuracy improves
steeply up to roughly 40 training subjects and "tends to plateau at approximately 40 subjects on
both HMC and SHHS", with a single-subject training set costing CBraMod 23.09 points on SHHS
relative to 40 subjects. That figure is a concrete constraint on what a small dyadic corpus can
support.

The EEGMAT result is also worth carrying forward because it is the benchmark closest to STRUM's
regime: 36 participants, 19 channels, 1,080 samples, binary workload label. CBraMod reaches 88.89
balanced accuracy and LaBraM 85.83 there, against 73.89 for the best supervised model — the
largest foundation-model margin in the cross-subject table.

## Notable details

- **Split rule.** Cross-subject: subjects in the test set are "explicitly excluded from training".
  Multi-subject: same subject cohort, held-out recording sessions or trials. Few-shot: a proportion
  of samples per category per subject forms the support set, remainder is the query set, results
  averaged over three runs. **The paper does not state the train/validation/test ratios.** It says
  only that datasets are "publicly available at the GitHub repository along with instructions for
  data splitting and preprocessing to reproduce the reported results", so the numeric split is in
  code rather than in the paper.
- **Metrics.** Balanced accuracy (average recall across classes) is primary throughout. Secondary
  metric depends on the dataset: weighted F1 for multiclass, AUROC for balanced binary (EEGMAT,
  SHU), AUC-PR for imbalanced binary (TUAB, Siena), Pearson correlation and R² for regression
  (SEED-VIG), 2-way and top-5 accuracy for retrieval (Things-EEG). Plus the transfer score, defined
  as `TS = λ·(P_prt − P_scr)/P_scr + (1−λ)·(P_prt − P_scr)/(P_oracle − P_scr)` with λ = 0.5 and
  P_oracle = 1 in the cross-subject setting.
- **Fine-tuning budget.** 50 training epochs, batch size 64, AdamW with weight decay 0.05, learning
  rate grid-searched over `[1e-3, 5e-4, 1e-4, 5e-4, 1e-5]` per adaptation-strategy/setting
  combination. (That list as printed contains `5e-4` twice; see limitations.) No early stopping is
  mentioned.
- **Checkpoints covered, with what each was pretrained on** (the paper's own Table 7): BIOT, 3.2M
  parameters, 59,304 h, 18 fixed channels, pretrained on PREST, SHHS, CHB-MIT, IIIC Seizure, TUAB
  and TUEV; EEGPT, 25M, 198 h in the table, 58 channels, pretrained on PhysioNet-MI, HGD, TSU, SEED
  and M3CV; LaBraM, 5.8M, 2,535 h, 136 channels, pretrained on BCI-IV-1, Emobrain, SPIS, Grasp and
  Lift, Inria P300, SEED series, Siena, TUEP, TUSZ and others; CBraMod, 4.0M, 9,246 h in the table,
  flexible channel count, pretrained on TUAB, TUAR, TUEP, TUEV, TUSE and TUSL.
- **Benchmark datasets and their recording parameters, as tabulated by the benchmark** (Table 6;
  these are the benchmark's post-preprocessing counts, not necessarily the corpora's own):
  SEED 1,000 Hz / 62 ch / 1 s / 15 subjects / 144,852 samples; SEED-IV 1,000 Hz / 62 ch / 1 s / 15 /
  151,845; EEGMAT 500 Hz / 19 ch / 4 s / 36 / 1,080; SEED-VIG 200 Hz / 17 ch / 8 s / 21 / 20,355;
  BCI-IV-2A 250 Hz / 22 ch / 4 s / 9 / 5,184; SHU 250 Hz / 32 ch / 4 s / 25 / 11,988; Things-EEG
  1,000 Hz / 63 ch / 1 s / 10 / 821,600; TUEV 256 Hz / 23 ch / 5 s / 370 / 112,237; TUAB
  250/256/512 Hz / 23 ch / 10 s / 2,383 / 409,083; Siena 512 Hz / 29 ch / 10 s / 14 / 51,307; HMC
  256 Hz / 4 ch / 30 s / 151 / 137,243; SHHS 125 Hz / 1 ch / 30 s / 329 / 324,854; Sleep-EDF 100 Hz
  / 2 ch / 30 s / 78 / 414,961.
- **Preprocessing fixed by the suite**: 0.1–75 Hz band-pass; notch at the power-line frequency
  identified per site by FFT; resampling to whatever the evaluated model expects; z-score
  normalization using global statistics across all trials, except 95th-percentile normalization for
  SHU and a rescale to roughly [−1, 1] for Things-EEG. Models with incompatible channel
  requirements (BIOT, EEGPT) are given a 1×1 channel-wise convolution to adapt.
- **Transfer scores** (cross-subject / few-shot average): BIOT 0.0264 / −0.0573; EEGPT 0.0764 /
  0.0789; LaBraM 0.2373 / 0.1773; CBraMod 0.1391 / 0.2761. BIOT's few-shot transfer score is
  negative at ratio 0.3 (−0.3489), i.e. pretraining hurt relative to from-scratch there.
- **Linear probing is much weaker than full fine-tuning, except for the largest model.** CBraMod on
  BCI-IV-2A drops from 47.71 to 32.32 under linear probing; EEGPT *rises* from 25.81 to 47.89 on the
  same dataset and from 70.21 to 73.82 on HMC, which the authors attribute to overfitting of its
  larger parameter count under full fine-tuning.
- Code is released under an MIT licence; the datasets themselves are not redistributed.

## Open questions / limitations

- **Split ratios are not in the paper.** The suite's central claim is "uniform data splitting", but
  the numeric partition lives only in the repository. A reader cannot check comparability against
  another suite from the paper alone, which is a reproducibility gap in a document whose purpose is
  reproducibility.
- **The suite conflicts with its sibling suites on both split ratio and primary adaptation
  strategy.** `omnieeg-bench` fixes an 8:1:1 subject-level split and makes *linear probing* the
  primary protocol; `brain4fms` uses an approximately 3:1:1 leave-subjects-out split with group-wise
  cross-validation and full fine-tuning; `neuralbench` selects among four splitting strategies per
  task, including random splits for small datasets. AdaBrain-Bench states no ratio and makes full
  fine-tuning primary. Under OmniEEG-Bench's linear-probing protocol the model ordering differs from
  its own full-fine-tuning ordering, so this is not a cosmetic disagreement. Recorded here, not
  resolved: which protocol is right is a Phase 3 question.
- **Internal inconsistencies.** (i) EEGPT's pretraining data is 198 h in Table 7 and "246 hours" in
  the body. (ii) CBraMod is 9,246 h in Table 7 and "approximately 27,000 hours" in the body.
  (iii) LaBraM is 2,535 h / 136 channels in Table 7 and "about 2,500 hours ... supporting 137 EEG
  channels" in the body. (iv) The few-shot sampling ratios are `[0.02, 0.05, 0.3, 0.5]` in Methods
  but `[0.02, 0.05, 0.1, 0.3, 0.5]` in the Figure 2 caption and in the Results text. (v) The
  learning-rate grid lists `5e-4` twice and omits an obvious fifth value. Following the standing
  rule, the table values are carded above for the pretraining sizes and the results text for the
  few-shot ratios, with the conflict recorded here.
- The arXiv abstract for v2 and the abstract printed in the v2 PDF are not identical (the landing
  page says "generic neural representations" and "comprehensive, practical and extensible
  benchmarks"; the PDF says "robust neural representations" and "standard and comprehensive
  benchmarks"). Nothing substantive turns on it, but a quotation from one will not match the other.
- No confidence intervals or significance tests are reported on the main leaderboard tables; the
  few-shot results are averaged over three runs and the rest appear to be single runs. With
  EEGMAT at 1,080 samples and BCI-IV-2A at 5,184, the differences between adjacent models are not
  obviously larger than run-to-run variance, and the paper does not let a reader check.
- SHHS is described as having 6,441 subjects in the body but the benchmark uses 329 selected healthy
  subjects, and the Table 6 row records 329. A reader comparing this SHHS number to another suite's
  SHHS number is not comparing the same cohort.
- No dyadic or multi-person task is included, and the smallest dataset (EEGMAT, 1,080 samples) is
  still larger than what a small two-person corpus would yield per condition.

## Citations

Primary: `adabrain-bench`

- `omnieeg-bench` — Lu et al. 2026. The competing suite whose primary protocol is linear probing on
  an 8:1:1 subject-level split; overlaps on LaBraM, CBraMod, BIOT.
- `brain4fms` — Shen et al. 2026. Third suite, approximately 3:1:1 leave-subjects-out with group-wise
  cross-validation.
- `neuralbench` — Banville et al. 2026. Fourth suite; selects a splitting strategy per task.
- `labram-2024` (strand `eeg-models`) — the strongest checkpoint in this suite's cross-subject table.
- `tuab`, `tuev`, `bci-competition-iv-2a`, `sleep-edf-expanded` — four of the 13 datasets, carded
  separately in this strand.
