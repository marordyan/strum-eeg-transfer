---
slug: openneuro
type: platform
strand: datasets-benchmarks
year: 2021
authors: [Markiewicz, Gorgolewski, Feingold, Blair, Halchenko, Miller, Hardcastle, Wexler, Esteban, Goncavles, Jwa, Poldrack]
venue: eLife 10:e71774
doi: 10.7554/eLife.71774
url: https://doi.org/10.7554/eLife.71774
license: CC BY 4.0 (article); hosted data default CC0
modalities: [scalp-eeg, intracranial-eeg, meg, mri, pet]
tags: [data-archive, pretraining-source, cc0, bids-validation, snapshots-and-dois, defacing, gdpr-exclusion, datalad, registry, access-route]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

The archive that supplies a large share of the heterogeneous, non-clinical EEG in modern pretraining
corpora, and the one place in this strand where the data licence is unambiguous: hosted datasets
default to a CC0 public domain dedication, with no authentication required to download.

## Summary

OpenNeuro is a BRAIN Initiative data archive that grew out of OpenfMRI and launched in June 2017. It
accepts brain imaging data across modalities — magnetic resonance imaging, electroencephalography,
magnetoencephalography and positron emission tomography — on the condition that every upload passes
Brain Imaging Data Structure validation at submission: "all data in OpenNeuro are compliant with the
BIDS specifications at upload time". Datasets are versioned through immutable snapshots implemented
as git tags via DataLad, each of which can be assigned a digital object identifier. As of 9 October
2021 the archive held 604 datasets with data from 20,989 participants, of which 574 datasets are
human. Its stated position on access is the permissive end of a spectrum: "OpenNeuro represents the
other pole of restrictiveness, by releasing data (by default) under a Creative Commons Zero (CC0)
Public Domain Dedication which places no restrictions on who can use the data or what can be done
with them", with citation an expected community norm rather than a legal requirement. Reuse is
documented: 165 publications reusing 111 datasets, and 406 terabytes distributed.

## Relevance to the review

OpenNeuro is carded here because it is a named component of a pretraining corpus, not because this
project would fine-tune on it. `reve-2025` records 10,194 of its 61,415 pretraining hours as coming
from OpenNeuro, second only to Temple University Hospital and PhysioNet. That matters for two
reasons.

First, it is where the non-clinical variety in those corpora comes from. Temple University Hospital
supplies clinical resting and routine EEG; OpenNeuro supplies task-based cognitive experiments from
individual laboratories, which is the distribution a stimulus-condition study like this one sits in.
`omnieeg-bench` reports that "the number of pretraining datasets" is significantly associated with
better average rank (median Spearman ρ = −0.27, p = 1.1×10⁻⁷) while training hours and subject count
are not, which makes an archive of many small heterogeneous studies more valuable per hour than a
single large clinical archive. OpenNeuro is the main source of that heterogeneity.

Second, the CC0 default removes the licensing obstacle that Temple University Hospital's
registration route creates. If this project wanted to continue pretraining rather than only
fine-tune, OpenNeuro is the part of the standard corpus it could actually redistribute derivatives
from. The exclusion of data collected under the General Data Protection Regulation — "data collected
in countries covered by GDPR cannot be shared through OpenNeuro at present due to the requirement
for restrictive data use agreements" — is the corresponding limit, and it also tells Phase 4
something about the geographic skew that `reve-2025` flags in its own corpus.

## Notable details

- **What it is**: a BRAIN Initiative data archive at openneuro.org, RRID:SCR_005031, evolved from
  OpenfMRI, launched June 2017.
- **Scale at time of writing (9 October 2021)**: 604 datasets, 20,989 individual participants. 574
  datasets (95%) are human; the rest are mouse (17), rat (6), non-human primate (2), dog (1) and
  juvenile pig (1). Median dataset size 23 subjects, 31 studies over 100 subjects, maximum 928.
- **EEG specifically**: 81 scalp electroencephalography datasets and 8 intracranial
  electroencephalography datasets in Table 1, with "more than 60 EEG datasets ... deposited since the
  publication of the BIDS-EEG standard in 2019". For comparison, anatomical magnetic resonance
  imaging 501, functional magnetic resonance imaging 445, diffusion-weighted 53, magnetoencephalography
  23, positron emission tomography 10, arterial spin labeling 3.
- **Data licence**: Creative Commons Zero public domain dedication by default. "While not legally
  required, researchers using the data are expected to abide by community norms and cite the data."
- **Access route**: no authentication. Web download, the OpenNeuro command line tool, DataLad, or
  Amazon S3 directly.
- **Validation**: mandatory client-side Brain Imaging Data Structure validation before upload.
- **De-identification**: 18 HIPAA identifiers removed, plus mandatory removal of facial features from
  magnetic resonance imaging before upload, currently checked by a human curator. Consent based on
  the Open Brain Consent is recommended for prospective depositors.
- **Versioning**: snapshots "unequivocally point to one specific point in the lifetime of a dataset",
  implemented as git tags, with a digital object identifier assigned per snapshot and an embargo
  period supported before public release.
- **Software licence**: MIT, at github.com/OpenNeuroOrg/openneuro.
- **Reuse**: 165 publications identified reusing 111 datasets; 407 publication digital object
  identifiers recorded against datasets; 406 terabytes distributed; 1,329 citations.
- **Scope limit**: "At present, OpenNeuro only shares raw data" — derivatives are not hosted.
- **Relationship to BIDS**: co-developed, now independent, "strongly synergistic". Modality
  extensions named: magnetoencephalography, scalp electroencephalography, intracranial
  electroencephalography, positron emission tomography, arterial spin labeling.
- **Checkpoints pretrained on it**: REVE (10,194 h of 61,415). `neuralbench` reaches OpenNeuro among
  its standardized data sources. No checkpoint in this corpus reports OpenNeuro as a downstream
  benchmark, because it is a registry rather than a dataset.

## Open questions / limitations

- **Two dataset counts for the same cutoff date.** "The database contains 604 datasets comprising
  data from 20,989 individual participants" against "the 502 OpenNeuro datasets available via
  DataLad as of 10/9/2021", both dated 9 October 2021. The 102-dataset gap is never reconciled. Any
  downstream statement of scale must say which figure it uses; the 604 is the archive total and the
  502 is the DataLad-accessible subset the paper's own reuse analysis is computed over.
- **Table 1's modality counts sum to 1,124 against 604 total datasets**, and the paper never states
  that a dataset may be counted under more than one modality. The "81 EEG datasets" figure is
  therefore not a count of EEG-only datasets, and using it as one would be a misreading the source
  invites.
- **The abstract rounds where the results are precise** — "more than 600 datasets ... more than
  20,000 participants ... more than 150 publications" against 604, 20,989 and 165. Not a
  contradiction, but two sets of numbers for the same quantities.
- **CC0 is called a dedication, a licence and an agreement in three places** ("a Creative Commons
  Zero (CC0) Public Domain Dedication", "CC0 licensing", and "a clear data use agreement (currently
  defaulting to a CC0 public domain dedication)"). CC0 is a waiver, and the difference matters for
  anyone reasoning about downstream obligations. The precise body statement should be the one
  carried forward.
- **CC0 is the default, not a guarantee.** The paper says datasets are released "by default" under
  CC0 and does not say what fraction depart from it, nor what alternatives are permitted. A project
  relying on the licence must check per dataset.
- **"Session" is used in two senses** in the same paper: the Brain Imaging Data Structure acquisition
  session, and a scanner visit in the cost-of-reuse calculation, which silently equates one BIDS
  session with one scanner visit at $1000. Only the first sense is relevant to data structure.
- **"Dataset" is overloaded** between an upload and a snapshot of it; reuse counts are per dataset,
  and the paper does not say whether reuse of different snapshots was distinguished.
- The archive is a moving target. Every count on this card is from October 2021 and the paper is now
  five years old; a project planning to pretrain would need current figures.
- The paper reports no evaluation, protocol or split, so nothing here bears on category 4.

## Citations

Primary: `openneuro`

- `eeg-bids` — the specification every OpenNeuro EEG upload must validate against.
- `reve-2025` (strand `eeg-models`) — the checkpoint that draws 10,194 pretraining hours from this
  archive.
- `neuralbench` — reaches OpenNeuro through its standardized data interface.
- `tuh-eeg-corpus` — the contrasting access model: a larger single-site clinical archive with no
  stated data licence and a registration requirement.
- `mne-python` — one of the tools that reads Brain Imaging Data Structure EEG datasets from this
  archive.
