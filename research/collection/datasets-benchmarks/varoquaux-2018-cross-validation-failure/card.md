---
slug: varoquaux-2018-cross-validation-failure
type: paper
strand: datasets-benchmarks
year: 2018
authors: [Varoquaux]
venue: NeuroImage 180:68-77 (Comments and Controversies)
doi: 10.1016/j.neuroimage.2017.06.061
url: https://arxiv.org/abs/1706.07581
license: null
modalities: [fmri, meg, vbm]
tags: [cross-validation, error-bars, small-sample, confidence-intervals, leave-one-out, repeated-splits, permutation-testing, vibration-effects, publication-bias, protocol-critique]
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

At the sample sizes neuroimaging actually uses — median 89 across 642 surveyed studies — a
cross-validated classification accuracy carries a confidence interval of roughly ±10 percentage
points, and the standard error across folds understates that interval by a factor of about 0.73 for
leave-one-out and 0.26 for repeated random splits.

## Summary

The paper is a Comments and Controversies piece arguing that cross-validation, correctly performed,
still cannot deliver a trustworthy accuracy estimate at neuroimaging sample sizes, and that the
usual uncertainty statistic makes this invisible. It assembles four lines of evidence: re-analysis
of within-subject functional magnetic resonance imaging, across-subject functional magnetic
resonance imaging, and magnetoencephalography cohorts of roughly 200–240 samples under a nested
design where the cross-validated estimate is compared against a held-out validation set; the public
versus private leaderboard discrepancy of a Kaggle schizophrenia-prediction challenge with 144
subjects; simulations of balanced binary classification at n from 30 to 1000; and a demonstration on
Haxby et al.'s data with labels deliberately inverted so that true accuracy is chance, where roughly
50 near-identical analysis pipelines reach 71 percent at 4 sessions. It summarizes the result in a
table of ballpark confidence bounds whose body did not survive extraction (see Open questions); the
only row the prose states outright is n = 100 — "A typical sample size in neuroimaging, 100
observations, leads to ±10% errors in prediction accuracy" — and the caption, itself cut off at a
page break in this extraction, says the bounds "may be significantly larger in adverse situations
such as with correlated observations or very unstable classi-". The recommended replacements are
permutation testing, group-level inference, comparison across many datasets, larger and pooled
samples, preregistration, and blind analysis.

## Relevance to the review

This is the entry that tells the project what a difference has to be before it means anything. Every
transfer number in this corpus — REVE's +10.7 points from pretraining on PhysioNet-MI,
AdaBrain-Bench's 88.89 versus 73.89 on EEGMAT with 36 participants and 1,080 samples, this project's
own eventual spoken-versus-written accuracy on a small dyadic corpus — sits at a sample size where
the paper's own numbers put the confidence bound at roughly ±10 points or worse. That does not make
those results wrong; it makes the ones with margins under 10 points uninterpretable as single
measurements, which is the distinction Phase 4 has to draw.

Two specifics carry over directly. First, the fold-based standard error is the statistic that would
naturally be reported and is the one the paper shows is worst: for repeated random splits with 20
percent held out and 50 repetitions, the standard-error-implied interval at n = 100 is ±2.0 percent
against an empirical ±8.1 percent. So the scheme with the tighter true error bars has the more
badly biased uncertainty estimate, because "repeated random splits create more correlations across
fold". Second, the vibration-effects demonstration is the mechanism by which a project that tries
several preprocessing and model choices arrives at a number that will not replicate: on data
guaranteed to be at chance, the best of ~50 reasonable pipelines reached 71 percent.

The paper also contains the one sentence that bridges its neuroimaging analysis to this project's
design directly: with several sessions per subject, "care must be taken to avoid having" different
sessions of the same subject in train and test, "to prevent subject-identification to be driving
prediction".

## Notable details

- **Central claim.** "Sample sizes of many neuroimaging studies inherently lead to large error bars,
  eg ±10% for 100 samples", and "the standard error across folds strongly underestimates them".
- **Headline table (Table 1) — body not recoverable from this extraction; treat as unverified.**
  Only the caption survives, and truncated: "Table 1: **Confidence bounds to be expected for a
  binary classification** , summarizing experiments and simulations in Figure 1. Actual confidence
  bounds may be significantly larger in adverse situations such as with correlated observations or
  very unstable classi-". *Correction, made during review: an earlier version of this card gave the
  table as "Sample size 30 / 100 / 300 / 1000 gives confidence bounds ±15% / ±10% / ±6% / ±3%". Of
  those four, only the n = 100 row is stated anywhere in `source.md` — "A typical sample size in
  neuroimaging, 100 observations, leads to ±10% errors in prediction accuracy" (Conclusion) and "eg
  ±10% for 100 samples" (abstract). The other three are marked unverified here rather than deleted;
  the nearest supported values are the Figure 1b/1c figures carded below, which at n = 30 read
  −20%/+18% (simulation, leave-one-out) and −15%/+12% (binomial), at n = 300 −6%/+6%, and at
  n = 1000 −3%/+3%.*
- **Real-data results** (leave-one-out; 50 repeated splits with 20% test): within-subject functional
  magnetic resonance imaging, ~212 samples, −21%/+18% and −24%/+13%; across-subject functional
  magnetic resonance imaging, ~241 samples, −10%/+10% and −10%/+8%; magnetoencephalography, ~199
  samples, −16%/+14% and −13%/+10%.
- **The simulated feature count is stated two ways and neither is preferred here.** Appendix C.1
  says "each described by a Gaussian of identity covariance in 100 dimensions"; the Figure A3 caption
  says the 2D illustration is "unlike the actual experiments, which are performed on 300 features".
  Both readings are recorded; the bullet below carries the Appendix C.1 figure because it is the
  method description.
- **Simulation results** (100-dimensional Gaussian per Appendix C.1, separation tuned to 75% accuracy, linear support
  vector machine, compared against 10,000 held-out samples over 1000 repeats): n = 30 gives
  −20%/+18% for leave-one-out and −19%/+15% for repeated splits; n = 100, −10%/+10% and −10%/+8%;
  n = 200, −7%/+7% and −7%/+5%; n = 300, −6%/+6% and −5%/+4%; n = 1000, −3%/+3% and −3%/+2%.
- **The standard-error bias, quantified.** Leave-one-out: standard-error-implied versus empirical
  bounds of ±13.8% versus ±18.9% at n = 30, ±7.4% versus ±10.3% at 100, ±4.1% versus ±5.9% at 300,
  ±2.2% versus ±2.9% at 1000. Fifty repeated splits with 20% test: ±3.4% versus ±15.3% at 30, ±2.0%
  versus ±8.1% at 100, ±1.1% versus ±4.1% at 300, ±0.6% versus ±2.1% at 1000. The paper's main text
  states the underestimation "by a factor of 0.7 in the best case"; the appendix gives 0.73 for
  leave-one-out and 0.26 for repeated splits.
- **Schemes compared.** Only two are benchmarked: leave-one-out (described as "leave one run out or
  leave one subject out in data with multiple runs or subjects") and 50 repeated random splits with
  20% held out. Repeated splits are preferred — they yield "slightly smaller error bars than leave
  one out" — but the same footnote says this "will not fix the problem of large error bars". k-fold
  is discussed only through the Bengio and Grandvalet result that there is no unbiased estimator of
  the variance of k-fold cross-validation. The reusable holdout "cannot circumvent intrinsic
  limitations of small samples".
- **The binomial is a floor, not a description.** With 100 tosses the binomial bounds lie ±7% from
  the true accuracy, and this "is a best-case scenario for errors on the accuracy measure:
  observations are i.i.d. and there is no additional variability from training a decoder", whereas
  real data "is strife with correlation across samples and confounding effects".
- **Vibration effects.** On Haxby et al.'s first subject with labels inverted in one of two sessions
  so that chance is the true answer, roughly 50 pipelines (support vector machine or logistic
  regression × feature selection at 100/200/500/1000/2000 voxels × smoothing at 2/4/6 mm) score
  44–52% using all 12 sessions, "going up to 57% for 6 sessions and 71% for 4 sessions". Such gains
  "are meaningless as they will not carry over to predicting on new data".
- **Literature sample sizes.** A stacked histogram over four review sources plus 100 PubMed hits,
  "the total histogram comprises 642 studies", with "a median number of samples of 89".
- **Publication bias.** "The literature acts as a filter as only studies that report significant
  effects are published", which "tends to inflate the reported effect size"; the meta-observation is
  that "the typical prediction accuracy reported in studies with" small sample size "is larger that
  reported in studies with many samples", with uncontrolled heterogeneity in large cohorts offered
  as a competing explanation.
- **Cross-validation is retained, not rejected.** "Cross-validation is not a silver bullet" but it is
  the best tool available, because it is the only non-parametric way to test generalization; Bayesian
  model selection, the Bayesian and Akaike information criteria and minimum description length are
  rejected as "strongly parametric".
- **Recommendations.** Report the ballpark bounds from the table rather than the fold standard error;
  use permutation testing (noting that "around a 30% of" MVPA publications use permutations "but
  that only 15% of the fMRI" decoding studies do); do group-level inference on subject-level
  predictions; compare methods across several datasets, which the author calls "the only sound way of
  doing methods development" at these sample sizes; use larger and pooled samples and
  preregistration; and use blind analysis where an independent test set is unaffordable.

## Open questions / limitations

- **Scope: mostly balanced binary classification, and no EEG.** The real-data results concern
  balanced two-class accuracy in within-subject functional magnetic resonance imaging,
  across-subject functional magnetic resonance imaging and magnetoencephalography. Multiclass and
  other expected accuracies are handled in Appendix A.2, and *quantitatively*: Table A1 gives 5–95%
  binomial confidence bounds for expected accuracies of 10%, 25%, 50%, 75% and 90% at 30, 100 and
  300 samples — for example 10.0% expected accuracy gives 3.3%–20.0% at 30 samples and 7.3%–13.0% at
  300, and 25.0% gives 13.3%–40.0% and 21.0%–29.0%. *Correction, made during review: an earlier
  version of this bullet said "Multiclass is addressed qualitatively in an appendix" and listed
  voxel-based morphometry among the paper's own quantitative results. Appendix A.2 is quantitative,
  and voxel-based morphometry appears only in Appendix B's description of the earlier study,
  "Varoquaux et al. (2017) applied such experiments on a variety of neuroimaging decoding datasets,
  within and across subjects, in fMRI, VBM (Voxel Based Morphometry) and MEG"; no VBM number is
  reported in this paper.* Continuous-outcome
  prediction is not analysed at all — the word "continuous" does not appear, and the paper's own
  diagnosis attributes the problem to discreteness, that it "is inherent to the discriminant nature
  of the test, measuring only a success or failure per observations". No number here should be
  attributed to a regression target or to EEG specifically.
- **The headline summary is optimistic relative to the paper's own real data.** At n = 30 the
  binomial lower bound is −15%/+12%, while the simulations give −20%/+18% and the appendix's
  empirical leave-one-out bound is ±18.9%. At ~212 samples the within-subject functional magnetic resonance
  imaging cohort shows −21%/+18%, worse than the stated ±10% at n = 100 would suggest. The paper
  does not flag that its summary is anchored on the simulation and binomial rather than on its
  worst real cohort.
- **Two statements about repeated splits versus leave-one-out that are not reconciled.** A footnote
  says repeated splits give "slightly smaller error bars than leave one out"; the perfect-predictor
  control appendix says "leave-one-out and random splits with 20% of the data give the same errors".
  The two are reconcilable given the different settings, but the paper does not reconcile them.
- **The main-text factor understates the appendix.** "A factor of 0.7 in the best case" versus 0.73
  and 0.26; a reader who quotes only the main text understates the repeated-splits problem by nearly
  threefold.
- The x-axis of the analysis deliberately mixes units: the paper is upfront that samples means "less
  than 100 observations given to the classifier, trials or subjects depending on the settings". For
  EEG, where one participant contributes thousands of epochs, which n the table refers to is exactly
  the question `kamrud-2021-data-partitioning` and `brookshire-2024-data-leakage` show is decisive,
  and this paper does not settle it.
- "Session" and "run" are used interchangeably and neither is defined.
- The version carded is the arXiv preprint dated 26 June 2017, not the published NeuroImage version
  of record; page and section numbering will differ, and any change made in revision is not captured.

## Citations

Primary: `varoquaux-2018-cross-validation-failure`

- `combrisson-2015-chance-level` — the companion result on the other half of the same problem: that
  the theoretical chance level is not the empirical chance level at small n.
- `kamrud-2021-data-partitioning` — reports EEG error rates with 95% intervals so narrow that this
  paper's analysis suggests they cannot be right.
- `moabb` — implements the across-datasets comparison this paper calls "the only sound way of doing
  methods development".
- Bengio and Grandvalet (2004) — no unbiased estimator of the variance of k-fold cross-validation.
- Saeb et al. (2017) — the subject-identification leakage the paper warns about for multi-session
  designs.
