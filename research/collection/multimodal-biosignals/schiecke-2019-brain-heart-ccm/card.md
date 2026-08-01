---
slug: schiecke-2019-brain-heart-ccm
type: paper
strand: multimodal-biosignals
year: 2019
authors: [Schiecke, Schumann, Benninger, Feucht, Baer, Schlattmann]
venue: Physiological Measurement 40(11):114001
doi: 10.1088/1361-6579/ab5050
url: https://doi.org/10.1088/1361-6579/ab5050
license: null
modalities: [eeg, ecg]
tags: [convergent-cross-mapping, brain-heart-interaction, processing-scheme, surrogate-data, bootstrap, linear-mixed-effects, time-variant, frequency-dependent, topographic, temporal-lobe-epilepsy, schizophrenia]
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

The processing-and-statistics companion to `schiecke-ccm-methods`: it proposes generalised schemes
for pre-processing, graphical representation and statistical evaluation of convergent-cross-mapping
brain-heart interaction, and validates them on two clinical datasets with surrogate data,
bootstrapping and linear mixed-effects models.

## Summary

The paper's stated problem is that a multitude of complex methods exist for quantifying
interactions in physiological systems, and that the crucial points for brain-heart interaction
analysis are adequate pre-processing that respects nonlinearity, intuitive graphical
representation, and suitable statistical evaluation. Its objective is to provide generalised
processing schemes covering all three. Two datasets are used to develop them: children with
temporal lobe epilepsy analysed across pre-ictal, ictal and post-ictal periods, and patients with
paranoid schizophrenia compared with healthy controls during resting state. Interaction is
quantified with nonlinear convergent cross mapping; statistical evaluation uses surrogate data,
bootstrapping and linear mixed-effects models. The reported outcome is that CCM revealed specific
and statistically significant time- and frequency-dependent patterns of brain-heart interaction in
the epilepsy cohort, and statistically significant topographic- and frequency-dependent patterns in
the schizophrenia cohort that differed from controls, and that suitable statistical models were
found to quantify group differences. The authors state the concept is transferable to other
interaction methods and to more complex physiological systems.

## Relevance to the review

Of the three convergent-cross-mapping entries in this strand, this is the one that treats the
analysis pipeline as the object of study rather than as machinery in service of a finding. Four
elements are directly reusable if the project ever runs a coupling analysis on STRUM.

The four axes it organises the analysis along — time-variant, frequency-dependent, topographical
and statistical — are precisely the axes on which a brain-heart claim can be over-read. A CCM
coefficient computed on a whole recording hides the time course; one computed on broadband signals
hides the frequency dependence; one computed on a single electrode hides the topography; and one
reported without a null distribution hides whether it is distinguishable from chance in a system
where both signals are autocorrelated.

The statistical machinery is the part that transfers most cleanly. Surrogate data give a null for
"is this coupling above what autocorrelation alone produces"; bootstrapping gives an interval;
linear mixed-effects models handle the repeated-measures structure that any per-electrode,
per-frequency, per-interval analysis creates. `zeng-brain-heart-ccm`, the application entry in this
strand, reports no comparable machinery in its abstract, which is a reason to weight the two
differently.

The clinical framing is not the reason to keep this entry. Epilepsy and schizophrenia are out of
this project's scope; the processing schemes are not.

## Notable details

- **Four analysis axes**: time-variant, frequency-dependent, topographical and statistical
  examination of directed interactions.
- **Statistical methods**: surrogate data, bootstrapping, and linear mixed-effects models, used
  both for significance and for quantifying group differences.
- **Dataset 1**: children with temporal lobe epilepsy, analysed across pre-ictal, ictal and
  post-ictal periods — the same cohort family as `schiecke-ccm-methods`.
- **Dataset 2**: patients with paranoid schizophrenia versus healthy controls, resting state.
- **Reported outcome**: statistically significant time- and frequency-dependent patterns in the
  epilepsy data; statistically significant topographic- and frequency-dependent patterns in the
  schizophrenia data, differing from controls.
- **Direction and strength of coupling**: *reported but not accessible.* The abstract names the
  patterns as significant but gives no coupling values, no directional summary and no effect sizes.
  The IOP full text could not be retrieved despite OpenAlex recording the article as CC-BY (see
  `meta.json.notes`).
- **Cohort sizes**: *reported but not accessible.* Neither the number of children nor the number
  of patients and controls appears in the abstract.
- **Pre-processing specifics**: *reported but not accessible.* The abstract states that adequate
  pre-processing "taking into account nonlinearity of data" is the crucial point and that
  generalised schemes are provided, but does not describe them.
- **Generality claim**: "The general concept of analyses is transferable also to other methods of
  interactions analysis and data representing even more complex physiological systems." That claim
  is the reason to card this entry under category 5 rather than only as a clinical application.
- 56 citations at retrieval; same journal as `zeng-brain-heart-ccm`, seven years earlier.

## Open questions / limitations

- Every quantitative fact this entry could contribute is in the inaccessible body. The card
  records the design and the claimed outcome and nothing else, and the entry is the strand's
  strongest candidate for re-attempt with institutional access.
- Both datasets are clinical and both involve pathology of the systems being coupled. Whether the
  processing schemes behave the same on healthy task data — where coupling is presumably weaker
  and the signal-to-noise ratio lower — is not established by the abstract.
- The paper develops the schemes *on* the two datasets it validates them with, so the schemes and
  the findings are not independent. Whether any part of the pipeline was fixed before seeing the
  data is not stated.
- The relationship to `schiecke-ccm-methods` is not spelled out in the abstract. The two share
  authors, method and one cohort family; whether the 2019 paper supersedes the 2015 parameter
  analysis or complements it cannot be determined without both full texts.
- Resting-state schizophrenia and ictal epilepsy are states with large, slow autonomic changes.
  A method validated where the coupling is large may not be calibrated for the small effects a
  stimulus-modality contrast would produce.
- No comparison to alternative directed-coupling measures is named in the abstract, so the schemes
  are validated for CCM specifically rather than shown to be method-agnostic, despite the
  transferability claim.

## Citations

Primary: `schiecke-2019-brain-heart-ccm`

- `schiecke-ccm-methods` — the same group's earlier, shorter treatment of CCM's estimation
  parameters.
- `zeng-brain-heart-ccm` — the recent application whose direction claim these schemes would be
  used to evaluate.
- Sugihara et al. (2012), Science — the original convergent cross mapping method.
- `haque-hrv-stress-review` — the HRV-feature tradition against which heartbeat-resolved coupling
  analysis is positioned.
- `makowski-2021-neurokit2` — a reference implementation of the ECG and HRV pre-processing steps
  any such pipeline needs upstream.
