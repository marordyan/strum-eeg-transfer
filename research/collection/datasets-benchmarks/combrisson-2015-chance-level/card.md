---
slug: combrisson-2015-chance-level
type: paper
strand: datasets-benchmarks
year: 2015
authors: [Combrisson, Jerbi]
venue: Journal of Neuroscience Methods 250:126-136
doi: 10.1016/j.jneumeth.2015.01.010
url: https://doi.org/10.1016/j.jneumeth.2015.01.010
license: null
modalities: [meg, intracranial-eeg, simulated-gaussian-signals]
tags: [chance-level, small-sample, statistical-significance, permutation-test, binomial-test, cross-validation, protocol-critique, metric-conventions, decoding-accuracy, abstract-only]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: abstract-only
---

## TL;DR

Classifying pure Gaussian noise with a small sample can yield "decoding accuracies of up to 70% or
higher in two-class decoding", so the theoretical chance level — 50% for two classes, 25% for four —
is not the threshold a decoding result should be compared against.

## Summary

The paper addresses a convention rather than a split: how a reported decoding accuracy is judged
significant. Its observation is that theoretical chance levels "hold for an infinite number of data
samples but not for small data sets", a limitation "widely recognized in the machine learning field"
but "sometimes still overlooked or ignored in the emerging field of brain signal classification",
which is "often faced with the difficulty of low sample size". The demonstration is a simulation:
applying signal classification to Gaussian random signals reaches accuracies of 70% or more in
two-class decoding with small sample sets. The paper then quantifies how severe this is as a
function of sample size, class number, cross-validation parameters (k-fold, leave-one-out, and the
number of repetitions) and classifier type (linear discriminant analysis, naive Bayes, support
vector machine), and presents two remedies that produce a p-value for a decoding accuracy while
taking sample size into account: an analytical solution using the binomial formula, and an empirical
one using permutation tests. It closes by applying both to real recordings, assessing noise-level
classifications in magnetoencephalography and intracranial electroencephalography baseline data.

## Relevance to the review

This is the metric-convention half of the strand's category 4 question, and it is the one this
project will hit first. A spoken-versus-written classifier on a small dyadic corpus will produce a
two-class accuracy, and the natural reflex is to compare it to 50%. This paper is the standard
citation for why that comparison is invalid at small n and for what to do instead: report a p-value
from the binomial formula or from a permutation test, both computed with the actual sample size.

It pairs with `varoquaux-2018-cross-validation-failure` on the two halves of the same failure.
Varoquaux quantifies the width of the interval around a reported accuracy; Combrisson and Jerbi
quantify how far the *null* moves away from its theoretical value. A project that fixes only one of
the two still cannot say whether a number is real. Together they set the reporting standard the
benchmark suites in category 3 do not meet: none of `adabrain-bench`, `omnieeg-bench`, `brain4fms`
or `neuralbench` reports a per-comparison significance test on its leaderboard, and only `moabb`
implements permutation or rank-based testing at all.

The paper's specific finding that the number of cross-validation repetitions affects the empirical
chance level also bears on how this project should configure its own evaluation, since repetition
count is usually treated as a free computational parameter rather than as something that changes the
null.

## Notable details

- **The demonstration.** "We demonstrate how applying signal classification to Gaussian random
  signals can yield decoding accuracies of up to 70% or higher in two-class decoding with small
  sample sets."
- **Parameters manipulated in the simulations.** Sample size; class number; cross-validation
  parameters, specifically "k-fold, leave-one-out and repetition number"; and classifier type,
  specifically linear discriminant analysis, naive Bayes and support vector machine.
- **Remedies offered.** Two, one analytical and one empirical: "analytical and empirical solutions
  (binomial formula and permutation tests) that tackle the problem by providing statistical
  significance levels (p-values) for the decoding accuracy, taking sample size into account".
- **Real-data validation.** Applied to "noise-level classifications in Magnetoencephalography (MEG)
  and intracranial EEG (iEEG) baseline recordings" — that is, to real recordings where the true
  answer is known to be chance, which is the same control logic as Varoquaux's label-inverted Haxby
  demonstration.
- **Scope.** The paper is about the chance level of a classification accuracy. It says nothing about
  the choice of split, and it is not an EEG dataset or benchmark paper; scalp EEG appears only via
  the intracranial and magnetoencephalography baseline data.
- The framing is explicitly about a discipline gap rather than a novel statistical result — the
  limitation is "widely recognized in the machine learning field" and the contribution is to
  quantify it for and communicate it to brain-signal decoding.

## Open questions / limitations

- **This card is abstract-only and its evidential support is correspondingly thin.** The Elsevier
  full text is paywalled and Unpaywall reports no open-access location as of 31 July 2026, so the
  simulation figures, the tabulated empirical chance levels as a function of sample size and class
  count, and the real-data results were not read. Every quantitative claim above except "up to 70%
  or higher" is a description of what the paper reports having done, not a value read from it.
  Specifically: the empirical chance level for a given (n, k, classifier) combination is
  **reported but not accessible** — the abstract states that the paper provides "a thorough
  quantification of the severity and the parameters affecting this limitation" without giving any of
  the numbers. Re-attempt retrieval if an institutional copy becomes available; the tabulated values
  are the part this project would actually use.
- The "up to 70% or higher" figure has no sample size attached in the abstract, so it cannot be
  applied to a specific design without the full text.
- The abstract does not state which of the two remedies the authors recommend where, nor whether the
  binomial formula and the permutation test agree in their simulations. Since the binomial assumes
  independent observations — an assumption that fails for overlapping windows and for multiple
  epochs from one participant, which is precisely this project's situation — knowing where the
  authors say it breaks down matters and is not recoverable from the abstract.
- The paper predates the deep-learning EEG literature by several years, and the classifiers studied
  are linear discriminant analysis, naive Bayes and support vector machines. Whether the same
  empirical chance levels hold for a fine-tuned transformer with millions of parameters is not
  addressed and would not be expected to follow.
- Nothing in the abstract addresses the interaction between an inflated empirical chance level and a
  leaky split; the two effects compound, and no source in this strand measures them together.

## Citations

Primary: `combrisson-2015-chance-level`

- `varoquaux-2018-cross-validation-failure` — the complementary result on the width of the interval
  around the estimate, as against the position of the null.
- `moabb` — the only suite in this strand that applies permutation or rank-based testing of the kind
  recommended here.
- `brookshire-2024-data-leakage` — reports 95% confidence intervals against a stated chance level,
  which is the practice this paper argues for.
- `kamrud-2021-data-partitioning` — reports intervals with no stated construction method, which is
  the practice this paper argues against.
