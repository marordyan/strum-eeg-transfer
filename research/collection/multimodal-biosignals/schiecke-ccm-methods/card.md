---
slug: schiecke-ccm-methods
type: paper
strand: multimodal-biosignals
year: 2015
authors: [Schiecke, Pester, Feucht, Leistritz, Witte]
venue: 37th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC 2015)
doi: 10.1109/EMBC.2015.7320106
url: https://doi.org/10.1109/EMBC.2015.7320106
license: null
modalities: [eeg, ecg]
tags: [convergent-cross-mapping, methods, estimation-parameters, state-space-reconstruction, nonlinear-causality, simulation-study, temporal-lobe-epilepsy, heart-rate, interval-based-analysis]
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

The methods reference for convergent cross mapping in this corpus: it demonstrates on simulated
data that CCM outcomes depend on estimation parameters, and then adapts an interval-based CCM to
heart rate and EEG components in children with temporal lobe epilepsy.

## Summary

Convergent cross mapping (CCM) tests for nonlinear causal interaction between two time series by
reconstructing each system's state space from its own observable and asking whether one attractor
can predict the other. This conference paper sets out the basic concept, uses simulated data to
demonstrate the influence of estimation parameters on the result, and then applies an
interval-based adaptation of CCM to real recordings, investigating interactions between heart rate
and specific EEG components in children with temporal lobe epilepsy. The stated aim is "to
investigate the general applicability, and to show potentials and limitation of CCM" in a setting
where "nothing or only little is known about the underlying dynamic system", which is the position
any brain-heart analysis starts from.

## Relevance to the review

Convergent cross mapping appears three times in this strand's seed set, and every coupling claim
made with it inherits whatever sensitivity the method has to analysis choices. This is the entry
that says the sensitivity is real: the abstract states plainly that "influence of estimation
parameters could be demonstrated by means of simulated data". That single sentence is what licenses
Phase 3 to treat the direction claim in `zeng-brain-heart-ccm` as conditional on its parameter
settings rather than as a fact about the nervous system.

For the project's third comparison the chain of reasoning is: if the cardiac signal is downstream
of the same central state the EEG carries, adding ECG should buy little; `zeng-brain-heart-ccm`
reports that the dominant direction is indeed cortex-to-heart; and this entry establishes that
whether such a direction claim holds depends on embedding dimension, lag and library size. Without
this entry the coupling literature would enter Phase 3 as settled; with it, the coupling literature
enters as a claim with a stated dependency.

The second thing this entry supplies is the *interval-based* adaptation. Standard CCM assumes a
stationary system and a long observation; physiological recordings during a task are neither. An
interval-based application, which is what the paper adapts for the epilepsy data, is the form any
stimulus-locked analysis in this project would need.

## Notable details

- **Entry type**: conference paper, IEEE EMBC 2015, pages 7418–7421. Recorded here as
  `@inproceedings` in the strand bib; OpenAlex's page range is the truncated PubMed-style
  "7418-21".
- **What the simulation shows**: that estimation parameters influence CCM outcomes. *Which*
  parameters, over what ranges, and by how much are **reported but not accessible** — the abstract
  names the finding without naming the parameters, and the full text is paywalled (see
  `meta.json.notes`). This is the single fact the brief most wanted from this entry.
- **What the paper recommends**: **reported but not accessible.** The abstract states that
  potentials and limitations are shown but gives no recommended settings.
- **Real-data application**: interval-based CCM between heart rate and specific EEG components in
  children with temporal lobe epilepsy. Cohort size, EEG montage, interval length and the specific
  EEG components involved are all not accessible.
- **Framing**: "In neuroscience, data are typically generated from neural network activity. Complex
  interactions between measured time series are involved, and nothing or only little is known about
  the underlying dynamic system." CCM is offered as a way to proceed without a model of that
  system.
- **Same group** as `schiecke-2019-brain-heart-ccm`, which develops the processing schemes and the
  statistical machinery (surrogates, bootstrapping, linear mixed-effects models) four years later
  on overlapping clinical data. The two should be read as one line of work, not two independent
  results.
- Thirty citations at retrieval, which for a four-page conference paper indicates it is used as the
  standard methods citation rather than as an empirical result.

## Open questions / limitations

- The card cannot list which estimation parameters matter or by how much, which is exactly the
  fact that would let Phase 3 weigh `zeng-brain-heart-ccm`. A four-page conference abstract is a
  thin basis for a methods reference, and the entry should be re-attempted with institutional
  access, or substituted with the fuller treatment in `schiecke-2019-brain-heart-ccm`.
- CCM's standard assumptions — a deterministic, low-dimensional, weakly coupled dynamical system
  observed with little noise — are a poor match for scalp EEG, and the abstract does not say
  whether the paper addresses that mismatch or only demonstrates parameter sensitivity within
  cases where the assumptions hold.
- The clinical application is epilepsy, where both the EEG and the heart-rate dynamics are
  pathological. Whether parameter sensitivity behaves the same way in healthy task data is not
  established here.
- The simulated-data demonstration is the paper's strongest element and is the part least
  recoverable from the abstract; nothing about the simulation's generating model is stated.
- No comparison against alternative directed-coupling measures (Granger causality, transfer
  entropy, phase-slope index) is mentioned, so the choice of CCM over them is not justified in the
  accessible text.

## Citations

Primary: `schiecke-ccm-methods`

- `schiecke-2019-brain-heart-ccm` — the same group's fuller treatment, with processing schemes and
  statistical evaluation for brain-heart interaction.
- `zeng-brain-heart-ccm` — the application in this corpus whose direction claim this entry
  conditions.
- Sugihara et al. (2012), "Detecting causality in complex ecosystems", Science — the original
  convergent cross mapping paper, cited by all three CCM entries in this strand.
- Takens (1981), delay-embedding theorem — the state-space reconstruction result CCM rests on.
- `salam-eeg-ecg-stress` — the classification-based alternative to asking the coupling question at
  all.
