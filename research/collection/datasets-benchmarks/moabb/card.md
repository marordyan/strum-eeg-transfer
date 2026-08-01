---
slug: moabb
type: standard
strand: datasets-benchmarks
year: 2018
authors: [Jayaram, Barachant]
venue: Journal of Neural Engineering 15(6):066011
doi: 10.1088/1741-2552/aadea0
url: https://doi.org/10.1088/1741-2552/aadea0
license: CC BY 3.0 (per Crossref licence record for the version of record)
modalities: [scalp-eeg, motor-imagery]
tags: [benchmark-suite, evaluation-protocol, within-session-cross-validation, roc-auc, meta-analysis, stouffer-method, effect-size, reproducibility, paradigm-evaluation-separation, no-pretrained-models]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-available
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

The protocol object model the later foundation-model suites inherited: separate the *paradigm*
(continuous data to trials) from the *evaluation* (trials to train/test split and metric), then
compare pipelines across twelve datasets with a per-dataset non-parametric test combined by
Stouffer's method rather than by pooling subjects.

## Summary

MOABB — Mother of All BCI Benchmarks — is a Python framework that aggregates publicly available EEG
datasets into a common format, wraps decoding pipelines behind the scikit-learn interface, and runs
an automated cross-dataset statistical comparison. The paper demonstrates it on binary motor
imagery across 12 open-access datasets covering 275 subjects (the abstract rounds this to "over 250")
and six classical pipelines: CSP + LDA, DLCSPauto + shrinkage LDA, Tikhonov-regularized CSP + LDA,
filter-bank CSP + optimized SVM, Riemannian tangent space + optimized SVM, and channel log-variance
+ optimized SVM. Its conceptual contribution is the decomposition of an experiment into
dataset × context × pipeline, where context is further split into a paradigm object (imagery type,
trial length and overlap, band-pass, pre- and post-event windows) and an evaluation object (train/test
splitting and the reported metric), "and these must be fixed identically for a given analysis". Its
empirical result is deflationary and is the reason the framework exists: "different datasets can
result in very different results for identical processing pipelines ... many previously validated
methods do not hold up when applied across different datasets". Tikhonov-weighted CSP's published
advantage "was not validated in this analysis", and filter-bank CSP's significance "goes in both
directions depending on the dataset".

## Relevance to the review

MOABB matters to this project for two reasons that have nothing to do with its leaderboard.

The first is the statistical machinery, which is the only cross-dataset inference procedure in this
strand. Rather than pooling subjects across datasets — which it rejects because "differences in
trial amount, sampling rate, and even location and hardware mean that we cannot expect subjects
across datasets to be naively comparable" — it runs a one-tailed paired test within each dataset,
combines the resulting p-values by Stouffer's method weighted by the square root of the subject
count, applies a Bonferroni correction across the pipeline comparisons, and computes a standardized
mean difference as the meta-effect size. The four foundation-model suites carded in this strand
report average ranks and standard deviations across seeds and do none of this. If Phase 4 needs to
say whether an observed difference between a pretrained checkpoint and a supervised baseline is
real, this is the procedure in the corpus that would let it.

The second is the explicit refusal to over-claim from a favourable split. MOABB reports within-session
5-fold cross-validation only, and says so: it "represents the best-case scenario for any pipeline,
with minimal non-stationarity", and because of that "regularization is at its least useful — which
means that it would be inappropriate to dismiss regularization in the case of CSP out of hand".
That is a model for how this project should qualify any STRUM number it produces under a favourable
protocol.

MOABB is also load-bearing infrastructure for two other entries here: `neuralbench` draws its
motor-imagery and P300 comparison datasets through MOABB, and REVE's pretraining corpus includes 384
hours from MOABB (see `reve-2025` in strand `eeg-models`).

## Notable details

- **Split rule.** Within-session 5-fold cross-validation, with "the splits were kept identical for
  all pipelines in a given subject". Where a dataset has multiple sessions, "the scores from each
  session were averaged when multiple sessions were present" to yield one score per subject. No
  cross-session and no cross-subject evaluation is implemented in this paper: cross-session is named
  once as future work, "a task that is currently infeasible" given how few multi-session datasets
  there were; transfer learning is gestured at by citation only.
- **Metric.** ROC-AUC. "In comparison with the more interpretable classification accuracy, the
  ROC-AUC is less sensitive to imbalanced classes, which is important in this case where the
  datasets vary heavily." The paper notes that multiclass problems cannot use it, which is why the
  metric is a property of the evaluation object rather than a global constant.
- **Statistics.** Per pipeline pair, within each dataset: a one-tailed permutation-based paired
  t-test for datasets with fewer than 20 subjects, otherwise a Wilcoxon signed-rank test. p-values
  combined across datasets by Stouffer's method weighted by √(number of subjects). Bonferroni
  correction across the N_pipelines − 1 comparisons per subject. Effect size by standardized mean
  difference within datasets, combined with the same weighting. 95% intervals shown per dataset in
  the forest plots. Sample meta-effect p-values against CSP + LDA: channel log-variance + optSVM
  3.58e-21, tangent space + optSVM 8.57e-13, DLCSPauto 4.85e-02, TRCSP 3.02e-02, FBCSP 2.59e-03.
- **Fine-tuning budget.** Not applicable — all six pipelines are classical and trained per subject
  per session. "All hyperparameters were set via cross-validation"; whether that inner loop is
  nested inside the outer 5 folds is not stated, which is itself an evaluation-protocol gap.
- **Checkpoints covered: none.** This predates the EEG foundation-model literature; the words
  "pretrained", "foundation model" and "deep learning" do not appear in the paper. The only
  "pre-trained" occurrence describes human subjects, not models. It is carded here as the standard
  the later suites depart from, and as the framework two of them depend on.
- **Datasets and their parameters** (name / imagery / channels / trials / sessions / subjects /
  epoch window): Cho 2017 R-L hand 64 / 200 / 1 / 49 / 0–3 s; PhysioNet R-L hand 64 / 40–60 / 1 /
  109 / 1–3 s; Shin 2017 R-L hand 25 / 60 / 3 / 29 / 0–10 s; BNCI2014-001 R-L hand 22 / 144 / 2 / 9
  / 2–6 s; BNCI2014-002 R hand-feet 15 / 160 / 1 / 14 / 3–8 s; BNCI2014-004 R-L hand 3 / 120–160 /
  5 / 9 / 3–7.5 s; BNCI2015-001 R hand-feet 13 / 200 / 2–3 / 13 / 3–8 s; BNCI2015-004 R hand-feet 30
  / 70–80 / 2 / 10 / 3–10 s; AlexandreMotorImagery R hand-feet 16 / 40 / 1 / 9 / 0–3 s; Yi 2014 R-L
  hand 60 / 160 / 1 / 10 / 3–7 s; Zhou 2016 R-L hand 14 / 100 / 3 / 4 / 1–6 s; Grosse-Wentrup 2009
  R-L hand 128 / 300 / 1 / 10 / 3–10 s. Total 275 subjects. All data subsampled to 128 Hz;
  band-passes tested were a single 8–35 Hz and a filter bank of 4 Hz increments over the same range.
- **Reproducibility argument.** The paper attributes the field's problem to two causes: over-reliance
  on a handful of competition datasets ("over a thousand journal and conference submissions have
  been written on the BCI Competition III and IV datasets ... with less than 50 subjects total"),
  and code scarcity, which forces each lab to reimplement competitors and therefore to "compare
  either against other work from the same lab, or old, easily implementable standards".
- **On sample size**: "what this analysis shows most clearly is that the sample size problem in BCIs
  is bigger than we might have expected", and "for studies with very few subjects ... the confidence
  intervals make even very strong standardized effects quite untrustworthy".
- Licence: BSD, at github.com/NeuroTechX/moabb. Built on MNE-Python for preprocessing and
  scikit-learn for the machine-learning interface.

## Open questions / limitations

- **Conflict with the foundation-model suites, recorded not resolved.** MOABB implements only
  within-session cross-validation and states that this is a best case. `omnieeg-bench` fixes an
  8:1:1 subject-level split, `brain4fms` an approximately 3:1:1 leave-subjects-out split,
  `adabrain-bench` an unstated ratio with subject-disjoint test sets, and `neuralbench` a per-task
  choice among four strategies. MOABB is the only one whose primary protocol is not subject-disjoint
  at all — deliberately, and with the limitation named — so a MOABB number and a cross-subject
  number from any other suite are not comparable quantities even on the same dataset.
- Contradiction between the stated test-selection rule and the figure captions. Section III
  specifies a permutation-based paired t-test for datasets with fewer than 20 subjects and Wilcoxon
  otherwise, but the Figure 2 and Figure 3 captions attribute all per-dataset p-values to "the
  one-tailed Wilcoxon signed-rank test", including datasets with 4, 9, 10, 13 and 14 subjects. Which
  test actually produced the reported p-values for the small datasets is unresolved in the paper.
- Subject count is "over 250 subjects" in the abstract and conclusion; Table I's own total row reads
  275. The prose never states 275.
- Dataset naming is inconsistent between the table and the figures: Table I's "Yi et al. 2014" is
  "Weibo 2014" in every figure, and Table I's "BNCI2014-001" is "001-2014" in the figures.
- Scope is one paradigm — two-class imagined motor imagery. The framework claims generality to ERP,
  multiclass, fNIRS and transfer settings, but none is demonstrated here, so the protocol's
  behaviour on an event-related stimulus contrast like this project's is untested in this source.
- Whether the hyperparameter search is nested inside the reported 5-fold cross-validation is not
  stated. If it is not, the reported ROC-AUCs are optimistically biased by selection on the test
  folds — the failure Varoquaux describes as vibration effects.

## Citations

Primary: `moabb`

- `neuralbench` — Banville et al. 2026, which reaches its motor-imagery and P300 comparison datasets
  through MOABB.
- `bci-competition-iv-2a` — one of the competition datasets this paper argues the field over-relies
  on; BNCI2014-001 in MOABB's table is the same recording.
- `physionet-mi` — the largest single dataset in MOABB's table at 109 subjects.
- `varoquaux-2018-cross-validation-failure` — the companion argument about error-bar magnitude that
  MOABB's confidence-interval observation echoes.
- `mne-python` — the preprocessing layer MOABB is built on.
