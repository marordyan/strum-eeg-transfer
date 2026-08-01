---
slug: snoek-2019-confound-control
type: paper
strand: candidate-datasets
year: 2019
authors: [Snoek, Miletić, Scholte]
venue: NeuroImage
doi: 10.1016/j.neuroimage.2018.09.074
url: https://doi.org/10.1016/j.neuroimage.2018.09.074
license: null
modalities: [structural-mri, simulation]
tags: [label-validity, confound-control, decoding-bias, post-hoc-counterbalancing, confound-regression, cross-validated-regression, below-chance-accuracy, methods, abstract-only]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-available
pdf_path: null
md_path: source.md
md_quality: abstract-only
---

## TL;DR

The two standard ways of removing a confound from a decoding analysis both bias the result —
post hoc counterbalancing upward, confound regression downward far enough to produce significant
*below*-chance accuracy — and only confound regression performed inside every cross-validation
fold gives an unbiased estimate.

## Summary

A simulation-and-empirical study of confound control in multivariate decoding. The authors state
the problem this strand's category 3 exists for: "a fundamental limitation of using decoding
analyses is that it remains ambiguous which source of information drives decoding performance,
which becomes problematic when the to-be-decoded variable is confounded by variables that are not
of primary interest." They evaluate two previously used methods — post hoc counterbalancing and
confound regression — against a comprehensive simulation set and against an empirical case of
decoding gender from structural MRI while controlling for brain size. Both introduce strong biases.
Post hoc counterbalancing produces better-than-expected performance because "the subsampling
process ... tends to remove samples that are hard to classify or would be wrongly classified".
Confound regression produces worse-than-expected performance, "even resulting in significant below
chance performance in some realistic scenarios", and the simulations show that "below chance
accuracy can be predicted by the variance of the distribution of correlations between the features
and the target". The negative bias disappears when confound regression is applied within every
cross-validation fold, and the authors conclude that "cross-validated confound regression is the
only method that appears to appropriately control for confounds".

## Relevance to the review

This is the procedural entry in category 3. The other entries establish *that* a stimulus-condition
label can be decoded for the wrong reason; this one addresses what to do about it, and finds that
the obvious remedies are worse than nothing if applied naively.

The direct transfer to this project is a warning about two moves it might otherwise make. If a
spoken-versus-written classifier is suspected of reading the auditory-versus-visual evoked
response, the tempting fixes are to subsample trials so the nuisance variable is balanced, or to
regress the nuisance signal out of the features first. This paper says the first inflates accuracy
and the second deflates it, sometimes below chance, and that the only version that works puts the
regression inside the cross-validation loop so the confound model is fitted on training data only.
That is the same class of error as fitting a scaler on the full dataset before splitting, and it is
easy to get wrong in an EEG pipeline where preprocessing is habitually done once, up front, on the
whole recording.

The second transfer is diagnostic rather than corrective. Significant below-chance accuracy is
reported here as a *symptom of the analysis*, not as evidence about the brain. An EEG project that
sees below-chance results after removing an artefact component should read that as a possible
pipeline artefact before reading it as a finding.

## Notable details

- **Two methods evaluated**: post hoc counterbalancing (subsample so the confound is balanced
  across classes) and confound regression (regress the confound out of the features).
- **Post hoc counterbalancing bias**: positive. The stated mechanism is that "the subsampling
  process ... tends to remove samples that are hard to classify or would be wrongly classified", so
  the retained sample is easier than the population.
- **Confound regression bias**: negative, "even resulting in significant below chance performance
  in some realistic scenarios".
- **Predictor of the negative bias**: in simulation, "below chance accuracy can be predicted by the
  variance of the distribution of correlations between the features and the target".
- **The fix**: performing confound regression "in every fold of the cross-validation routine" makes
  the negative bias disappear "in both the empirical analyses and simulations", yielding "plausible
  (above chance) model performance".
- **Empirical case**: decoding gender from structural MRI while controlling for brain size. Not an
  EEG case, and deliberately chosen as one where the confound is large and uncontroversial.
- **Conclusion as stated**: "cross-validated confound regression is the only method that appears to
  appropriately control for confounds which thus can be used to gain more insight into the exact
  source(s) of information driving one's decoding analysis."

## Open questions / limitations

- **Abstract-only card.** NeuroImage full text could not be retrieved (see `meta.json`). The
  simulation parameters, the empirical accuracy figures, the exact cross-validated procedure and
  any released code are all unread, so no implementation detail should be taken from this card.
- The empirical demonstration is structural MRI with a scalar confound (brain size). An EEG
  spoken-versus-written analysis has a confound that is not a scalar but a whole time-locked evoked
  response, and whether regressing that out per fold is even well posed is not addressed by
  anything read here.
- Cross-validated confound regression removes the confound's *linear* contribution to each feature.
  Whether that suffices when the confound and the target share nonlinear structure is not something
  the abstract speaks to.
- The paper is about controlling a confound you have already identified and measured. For the
  project's case, the confound — the sensory evoked response to auditory versus visual
  presentation — is not separately measured, so there is no regressor to remove without first
  constructing one.

## Citations

Primary: `snoek-2019-confound-control`

- `ritchie-2019-decoding-limits` — the conceptual companion: even a confound-free decode does not
  establish representation.
- `simanova-2010-eeg-object-categories` — the concrete case in this strand where an unidentified
  confound (exemplar-level perceptual differences) drove decoding, diagnosed by generalisation
  rather than by regression.
- `simanova-2012-modality-independent` — the alternative strategy: test generalisation across the
  nuisance factor instead of removing it.
- `deniz-2019-modality-invariant-semantics` — establishes that for spoken versus written the
  semantic component is shared, which is what makes the residual difference a confound in the
  first place.
