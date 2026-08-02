---
slug: brain4fms
type: standard
strand: datasets-benchmarks
year: 2026
authors: [Shen, Yang, Li, Hong, Pan, Yuan, Li, Yang]
venue: arXiv preprint 2602.11558
doi: null
url: https://arxiv.org/abs/2602.11558
license: null
modalities: [scalp-eeg, intracranial-eeg, clinical-eeg, sleep-eeg, motor-imagery, emotion-eeg]
tags: [benchmark-suite, evaluation-protocol, leave-subjects-out, group-wise-cross-validation, auroc, cohens-kappa, channel-permutation, full-fine-tuning, checkpoint-to-benchmark-mapping, eeg-and-ieeg]
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

Fifteen brain foundation models spanning both scalp EEG and intracranial EEG are fine-tuned end to
end under one cross-subject leave-subjects-out protocol on 22 tasks from 18 datasets, and the suite
adds a channel-permutation perturbation designed to test whether a model has internalized
dataset-specific spatial structure rather than transferable topology.

## Summary

Brain4FMs organizes brain foundation models under a self-supervised-learning taxonomy
(contrastive, generative, other) and pairs that with a curated set of public downstream datasets,
then releases an evaluation platform with plug-and-play interfaces integrating 15 models and 18
datasets. Its distinguishing scope choice is that it covers intracranial EEG alongside scalp EEG,
so it can ask whether pretraining modality predicts downstream modality performance; it reports
that it does — Brant, pretrained on iEEG, is strong on the iEEG cohorts MAYO and FNUSA but
"degrades markedly on CHBMIT", while BrainWave, pretrained jointly on EEG and iEEG, "remains robust
across settings". The suite organizes its analysis around five questions covering pretraining data
composition, self-supervised strategy, spatial structure, frequency representation, and codebook
discretization. Its headline evaluative finding is deflationary: "Performance varies significantly
across tasks, with no single BFMs consistently outperforming others", though it also concludes that
"large-scale pretraining yields more transferable representations than task-specific supervised
training in most clinical diagnosis settings".

## Relevance to the review

Two things here bear on this project directly. The first is the channel-permutation probe. The suite
permutes channels in the training and validation splits while leaving the test split unchanged,
"so any performance change is attributable to disrupted channel topology", explicitly in order to
test "whether BFMs internalize dataset-specific spatial structure during training". That is a
shortcut-learning diagnostic built into a benchmark rather than published as a critique, and it
is the mechanism-level complement to the identity and dataset-identity confounds reported in
`lin-2026-identity-trap` and `zare-2026-stress-testing`. The suite sorts models into spatially
strong (BrainWave, BrainOmni, CBraMod, EEGPT, MBrain, REVE) and spatially weak groups for this test.

The second is the supervised comparison. Unlike the sibling suites, Brain4FMs includes purpose-built
supervised baselines per task family — SPaRCNet for epilepsy, DeprNet for depression, CCNSE for
sleep staging, MSCARNet for communication and affective computing — rather than only generic EEG
CNNs. It finds SPaRCNet outperforming three foundation models (SppEEGNet, NeuroLM, BFM) on epilepsy
in both AUROC and accuracy, and DeprNet remaining "a strong baseline" on MDD-64 though surpassed by
REVE, BrainOmni and BrainWave. For this project's comparison 1 versus comparison 2, that is the
right shape of evidence: a supervised model tuned for the task, not a generic one.

The suite also names the two task families where cross-subject generalization fails — "Communication
and affective computing remain challenging for cross-subject generalization due to strong
non-stationarity and large cross-subject/inter-session variability". A spoken-versus-written
language contrast in a small dyadic corpus sits in that region.

## Notable details

- **Split rule.** "We adopt a cross-subject leave-subjects-out protocol with train/valid/test splits
  of approximately 3:1:1, ensuring no data leakage." Evaluation is by group-wise cross-validation;
  the grouping variable is the subject. The suite states this "enforces generalization to unseen
  subjects".
- **Metrics.** Accuracy, AUROC, F1, F2, and Cohen's κ, reported with standard deviations across
  cross-validation folds. AUROC is the metric the analysis sections lead with.
- **Fine-tuning budget.** Full fine-tuning of the backbone with a task-specific classifier head:
  "Models are finetuned for up to 50 epochs with early stopping (patience = 5) based on validation
  performance", Adam or AdamW, except that for a small number of models the authors' original
  optimizers were retained "to avoid unintended performance degradation caused by altering model
  specific training designs". No linear-probing protocol is defined.
- **Checkpoints covered (15), with parameter count, pretraining modality and feature domain from the
  suite's own Table 1:** contrastive — SppEEGNet 138K EEG time; BIOT 3.19M EEG time+frequency;
  BENDR 3.97M EEG time+frequency; MBrain 8.34M EEG/iEEG time+frequency+space. Generative — Brant
  196.10M iEEG time+frequency+space; BFM 708.96M EEG time; BrainBERT 43.18M iEEG time+frequency;
  CBraMod 4.88M EEG time+frequency+space; NeuroGPT 79.62M EEG time+frequency; LaBraM 5.80M EEG
  time+frequency+space; BrainWave 102.13M EEG+iEEG time+frequency+space; REVE 69.19M EEG time+space;
  BrainOmni 32.71M EEG time+frequency+space. Other — EEGPT-1 51.04M EEG time+space; NeuroLM 169.60M
  EEG time+frequency.
- **Datasets covered:** 22 downstream classification tasks drawn from 18 public datasets, "as some
  datasets contain multiple subtasks". The suite's Table 2 lists all 18 with signal type, task,
  subject count and number of categories: CHBMIT (EEG, epilepsy, 23 sub., 2), MAYO (iEEG, DRE, 25,
  2), FNUSA (iEEG, DRE, 14, 2), Dep-BDI (EEG, depression, 122, 2), MDD-64 (EEG, MDD, 30H + 43MDD,
  2), SD-28 (EEG, SD, 28, 2), UCSD (EEG, PD, 31H + 15PD, 2), ADFD (EEG, AD, 88, 2), ADHDAdult (EEG,
  ADHD, 42H + 37ADHD, 2), ADHDChild (EEG, ADHD, 60H + 61ADHD, 2), ISRUC (EEG, sleep stage, 100, 5),
  SleepEDFx (EEG, sleep stage, 44, 5), DEAP (EEG, emotion, 32, 4), SEED-IV (EEG, emotion, 15, 4),
  EEGMat (EEG, mental workload, 36, 2), EEGMMIDB (EEG, MI & ME, 109, 4), BCI-2a (EEG, MI, 9, 4),
  Chisco (EEG, concept classification, 5 sub., 39 categories). A second table in Appendix C gives
  per-task recording parameters, e.g. "BCI-2a [11]|22|3s|250|130 min|4" and "Chisco-R
  [116]|125|3.3s|500|58.6 h|39", whose columns are channels, window, sampling rate, duration and
  number of classes. *Correction, made during review: an earlier version of this card listed only
  nine of the eighteen datasets as "named in the extraction with their subject counts" — all
  eighteen are in Table 2 — and read the last column of the Appendix C table as subjects, giving
  "BCI-2a ... 4 subject groups" and "Chisco-R and Chisco-I ... 39 subjects each". That column is the
  class count. Chisco has 5 subjects and 39 categories; BCI-2a has 9 subjects and 4 classes.* Task
  families are epilepsy, sleep staging, disease diagnosis, communication, and affective computing.
- **Supervised reference points:** SPaRCNet (epilepsy), DeprNet (depression), CCNSE (sleep staging),
  MSCARNet (communication and affective computing).
- **Representative reported values** (AUROC ± sd, iEEG epilepsy): on MAYO, BENDR 0.93 ± 0.03,
  MBrain 0.92 ± 0.04, BIOT 0.90 ± 0.07; on FNUSA, MBrain 0.91 ± 0.08. On CHB-MIT, MBrain drops to
  0.71 ± 0.03 AUROC — the modality-dependence result.
- Preprocessing fixed by the suite: "bandpass and notch filtering, downsampling, event-aligned
  window segmentation, channel selection, and perchannel z-score normalization".

## Open questions / limitations

- **Conflict with the sibling suites, recorded not resolved.** Brain4FMs uses an approximately 3:1:1
  leave-subjects-out split with group-wise cross-validation and full fine-tuning only.
  `omnieeg-bench` uses 8:1:1 subject-level with linear probing as primary. `adabrain-bench` states
  no ratio and uses full fine-tuning as primary. `neuralbench` chooses among four strategies per
  task. Because Brain4FMs runs group-wise cross-validation while OmniEEG-Bench runs three fixed
  seeded splits and AdaBrain-Bench appears to run single splits, the three suites also differ in how
  much of the reported variation is estimated at all, not only in where the boundary falls. Which
  protocol should govern is a Phase 3 question.
- The "ensuring no data leakage" claim is asserted for the subject grouping and not tested. Nothing
  in the paper addresses whether any of the 15 checkpoints was pretrained on any of the 18
  evaluation datasets — a form of leakage that a subject-level split cannot prevent, and that
  `neuralbench` reports finding in its own model set.
- The paper's abstract says the platform "integrates 15 representative BFMs and 18 public datasets";
  the results section says "22 downstream classification tasks from 18 public datasets". These are
  reconcilable, but a reader quoting "18" should say whether they mean datasets or tasks.
- Metrics are split by task type, not omitted: "For binary tasks, we report ... AUROC, Accuracy, F1,
  and F2 ... For multi-class tasks, we report Accuracy, AUROC (one-vs-rest; OvR), macro-F1 (MF1),
  and Cohen's 𝜅". Appendix D's per-dataset tables follow that division — Tables 8 to 22 (binary)
  carry AUROC/Acc/F1/F2, Tables 23 to 29 (multi-class: BCI-2a, EEGMMIDB-I, EEGMMIDB-R, DEAP,
  SEED-IV, Chisco-I, Chisco-R) carry AUROC/Acc/MF1/Kappa. *Correction, made during review: an
  earlier version of this card said "Cohen's κ is listed among the reported metrics but does not
  appear in the result tables recovered from the extraction ... Full results are deferred to
  Appendix D." Appendix D is in the extraction in full, Tables 8 through 29, and Kappa is reported
  in seven of those tables.*
- The channel-permutation experiment perturbs train and validation while holding test fixed, which
  measures sensitivity to a training-time corruption rather than to a test-time one. It therefore
  answers "does the model depend on a specific channel ordering during learning" and not "does the
  model's representation encode absolute channel index", which is the stronger claim the framing
  invites. The suite's own sensitivity analysis over the quantile threshold q ∈ {0.05, 0.10, 0.20}
  reports that relative trends are stable but absolute values vary.
- "BFM" is used both as the abbreviation for the class of brain foundation models and as the name of
  one specific 708.96M-parameter model, so quoting "BFM" without context is ambiguous in this
  source. *Correction, made during review: an earlier version of this card added that BFM, MBrain,
  Brant and BrainBERT "are named without a bibliographic expansion in the recovered text". All four
  resolve in the reference list, which the extraction carries: [9] Darvishi Bayazi et al., [13] Cai
  et al. "Mbrain: A multi-channel self-supervised learning framework for brain signals", [112] Zhang
  et al. "Brant: Foundation model for intracranial neural signal", [90] Wang et al. "BrainBERT:
  Self-supervised representation learning".*
- No dyadic or multi-person task; no peripheral physiology.

## Citations

Primary: `brain4fms`

- `adabrain-bench` — Wu et al. 2025. Overlapping checkpoints: BIOT, LaBraM, CBraMod, EEGPT.
- `omnieeg-bench` — Lu et al. 2026. Overlapping checkpoints: BENDR, BIOT, LaBraM, CBraMod,
  BrainOmni, NeuroLM, REVE.
- `neuralbench` — Banville et al. 2026. Overlapping checkpoints: BENDR, BIOT, LaBraM, CBraMod, REVE.
- `reve-2025` (strand `eeg-models`) — one of the evaluated checkpoints, and one the suite classes as
  spatially strong.
- `zare-2026-stress-testing` (strand `eeg-models`) — the negative-control study whose dataset-identity
  probe is the critique-side analogue of this suite's channel-permutation probe.
