---
slug: openneuro-2021
type: platform
strand: candidate-datasets
year: 2021
authors: [Markiewicz, Gorgolewski, Feingold, Blair, Halchenko, Miller, Hardcastle, Wexler, Esteban, Goncavles, Jwa, Poldrack]
venue: eLife
doi: 10.7554/eLife.71774
url: https://doi.org/10.7554/eLife.71774
license: CC BY 4.0
modalities: [mri, scalp-eeg, meg, ieeg, pet]
tags: [registry, cc0-by-default, bids-validated, no-data-use-agreement, long-tail-datasets, versioned-snapshots, datalad, access-route]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

OpenNeuro releases data "by default under a Creative Commons Zero (CC0) Public Domain Dedication
which places no restrictions on who can use the data or what can be done with them" — the most
permissive access route available for candidate datasets, and the only registry in this strand with
no data use agreement at all.

## Summary

A platform paper for openneuro.org, a BIDS-validated archive that "enables FAIR-compliant data
sharing for a growing range of neuroscience data types (currently including magnetic resonance
imaging [MRI], electroencephalography [EEG], magnetoencephalography [MEG], and positron emission
tomography [PET])". At the time of writing it "presently shares more than 600 datasets including
data from more than 20,000 participants, comprising multiple species and measurement modalities and
a broad range of phenotypes", with "more than 150 publications" reusing the data. Its stated
positioning on access is explicit and comparative: "There is a range of restrictiveness across data
archives with regard to their data use agreements. At one end of the spectrum are highly restricted
databases such as the Alzheimer's Disease Neuroimaging Initiative, which requires researchers to
submit their scientific question for review ... OpenNeuro represents the other pole of
restrictiveness, by releasing data (by default) under a Creative Commons Zero (CC0) Public Domain
Dedication." The archive's motivating target is "a 'long tail' of smaller neuroimaging datasets
that have been collected in service of specific research questions", not the large consortium
studies. Automated BIDS validation is the mechanism that replaced the manual curation the
predecessor project OpenfMRI required, since with an ad hoc scheme "there was no way to directly
validate whether a particular dataset met the standard".

## Relevance to the review

This entry is carded for category 4 as an access route rather than as a source of any particular
dataset. Three properties bear on feasibility.

First, CC0 by default. For a project that may want to combine several fine-tuning corpora and
publish derived artefacts, CC0 is the only licence in this strand that raises no attribution-chain
or share-alike question at all. Compare `deap-2012` and `amigos-2021` (signed end-user licence
agreement), `mous-2019` (data use agreement with registration), and `sleep-edfx` (Open Data Commons
Attribution). The friction ranking is a fact about the access route, not a judgement about the data.

Second, BIDS validation is enforced rather than encouraged, so an OpenNeuro EEG dataset is
guaranteed to have `channels.tsv` and to be readable by BIDS-aware tooling. It is *not* guaranteed
to have `electrodes.tsv` and `coordsystem.json`, since those are recommended rather than required
by `eeg-bids-2019` — so validation certifies structure, not the electrode coordinates a
coordinate-based checkpoint wants.

Third, the "long tail" framing describes exactly the size regime this project sits in. OpenNeuro is
built for datasets of tens of participants collected for a specific question, which is what a
STRUM-scale corpus is.

One negative result belongs on this card, recorded here because the strand brief asks for registry
sweeps to be documented: OpenNeuro's own GraphQL search interface was queried for multi-person EEG
datasets during this collection, and it returned nothing usable. See `INDEX.md` for the queries.

## Notable details

- **Default licence**: CC0 Public Domain Dedication, which "places no restrictions on who can use
  the data or what can be done with them". The authors note that "while not legally required,
  researchers using the data are expected to abide by community norms and cite the data following
  the guidelines included within each dataset."
- **Stated motivation for CC0**: "it makes the data maximally accessible to the largest possible
  number of researchers and citizen-scientists."
- **Scale at time of publication**: more than 600 datasets, more than 20,000 participants, more
  than 150 reuse publications.
- **Modalities**: MRI, EEG, MEG, PET at the time of writing, via BIDS modality extensions — MEG
  (Niso et al. 2018), scalp EEG (Pernet et al. 2019, carded here as `eeg-bids-2019`), intracranial
  EEG (Holdgraf et al. 2019), PET (Norgaard et al. 2021), arterial spin labelling.
- **Validation as the curation mechanism**: OpenfMRI's custom naming scheme "was ad hoc and limited
  in its coverage, and datasets often required substantial manual curation (involving laborious
  interaction with data owners)". Automated BIDS validation replaced that.
- **Access-route spectrum, as the platform itself frames it**: the Alzheimer's Disease Neuroimaging
  Initiative at the restrictive pole (scientific question reviewed in advance, consortium as
  corporate author), OpenNeuro at the permissive pole.
- **Relevant holdings for this strand**: `ds003670`, the BIDS copy of `tes-eeg-ecg-2021`.

## Open questions / limitations

- CC0 is the *default*, not a guarantee. Individual datasets may carry different terms, so the
  licence of any specific OpenNeuro dataset must still be read from its own `dataset_description.json`
  rather than assumed from the platform.
- The scale figures are as of 2021 and will understate current holdings. Any count taken from this
  card is a historical snapshot.
- The archive's search interface is poor for the queries this strand needed. Its GraphQL
  `advancedSearch` accepts only a fixed set of structured filters (modality, tasks, keywords,
  subject count, and so on) with no free-text field, and keyword queries for hyperscanning, dyadic,
  conversation and joint action against EEG modality all returned zero results. Whether that means
  no such datasets exist or that they are not tagged with those keywords cannot be distinguished
  from the interface, which is itself a finding about registry coverage.
- CC0 removes legal restrictions but not ethical ones, and the paper is explicit that de-identification
  and participant consent remain the depositor's responsibility. A dataset being CC0 does not
  certify that its consent covers model pretraining.
- The paper describes the platform, not any dataset. It contributes no recording specification.

## Citations

Primary: `openneuro-2021`

- `eeg-bids-2019` — the specification OpenNeuro validates EEG datasets against.
- `nemar-2022` — the EEG/MEG/iEEG gateway built on top of OpenNeuro, adding modality-specific
  quality assessment and compute.
- `tes-eeg-ecg-2021` — the dataset in this strand hosted here as `ds003670`.
- Jwa & Poldrack (2021) — the analysis of data-use-agreement restrictiveness this paper cites when
  positioning OpenNeuro at the permissive pole.
