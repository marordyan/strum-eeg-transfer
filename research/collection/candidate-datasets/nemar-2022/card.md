---
slug: nemar-2022
type: platform
strand: candidate-datasets
year: 2022
authors: [Delorme, Truong, Youn, Sivagnanam, Stirm, Yoshimoto, Poldrack, Majumdar, Makeig]
venue: Database (Oxford)
doi: 10.1093/database/baac096
url: https://doi.org/10.1093/database/baac096
license: CC BY-NC
modalities: [scalp-eeg, meg, ieeg]
tags: [registry, gateway, openneuro, quality-assessment, hed, neuroscience-gateway, sdsc-compute, bids, sccn, access-route]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-available
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

NEMAR is a gateway, maintained at SDSC and authored from the Swartz Center orbit, that filters
OpenNeuro down to the neuroelectromagnetic
modalities, adds per-dataset quality visualisation, and connects the selected data directly to San
Diego Supercomputer Center compute through the Neuroscience Gateway — so it is the registry to
browse when the question is specifically "which EEG datasets exist and are any of them usable".

## Summary

"NEMAR.org, a web gateway to OpenNeuro data for human neuroelectromagnetic data. NEMAR allows users
to search through, visually explore and assess the quality of shared electroencephalography (EEG),
magnetoencephalography and intracranial EEG data and then to directly process selected data using
high-performance computing resources of the San Diego Supercomputer Center via the Neuroscience
Gateway (nsgportal.org, NSG), a freely available web portal to high-performance computing serving a
variety of neuroscientific analysis environments and tools." The motivating argument is that "high-
density EEG, magnetoencephalography (MEG), and intracranial EEG (iEEG) recordings have no sensors
in common", and that physical differences exist across the dozens of available collection systems,
so cross-dataset work needs a modality-aware layer above a general archive. The paper also
describes the Hierarchical Event Descriptor standard as the complement to BIDS: "although
BIDS-formatted data sets contain detailed metadata, the BIDS standards in themselves do not
constitute a system for adequately describing the timeline of the recording", which HED supplies.
The stated position is that "OpenNeuro, NEMAR and NSG form an efficient, integrated data, tools and
compute resource".

## Relevance to the review

Carded for category 4 as a registry and access route, at low relevance because it adds a layer over
a platform already carded rather than holding data of its own.

Two things make it worth an entry rather than a footnote. First, it is the registry to actually
browse for this project's purposes: OpenNeuro's own search has no free-text field and returns
nothing for the queries this strand needed, whereas NEMAR is scoped to EEG/MEG/iEEG by construction
and exposes per-dataset quality summaries, which is the difference between "600 datasets, mostly
MRI" and a browsable EEG inventory. Second, its treatment of event description is directly relevant
to the label-validity question this strand owns. HED exists because BIDS records *that* events
happened without constraining *how they are named*, which is precisely the gap in which a label like
"spoken" versus "written" gets defined inconsistently across datasets. A project intending to
compare label schemes across corpora will run into that gap.

There is also a provenance note worth recording, with a caveat on its basis. The Swartz Center
connection — one of the two institutional homes named in the strand brief as places to check for a
STRUM author copy — rests on the author list (Delorme, Makeig) rather than on the paper text. The
extraction carries no affiliation block, and the only institutional home `source.md` states for the
site itself is SDSC: "The NEMAR website (nemar.org), maintained and developed at SDSC, uses the
HUBzero web framework". SCCN appears in the source only as the home of EEGLAB. STRUM is not in
NEMAR — no registry sweep located it.

## Notable details

- **What it is**: a gateway to OpenNeuro filtered to neuroelectromagnetic modalities — EEG, MEG,
  iEEG — not a separate archive with separate holdings.
- **What it adds over OpenNeuro**: search, visual exploration, and quality assessment per dataset,
  plus a direct handoff to high-performance computing at the San Diego Supercomputer Center through
  the Neuroscience Gateway.
- **Why a modality-specific layer**: "high-density EEG, magnetoencephalography (MEG), and
  intracranial EEG (iEEG) recordings have no sensors in common", and "important physical
  differences exist between the dozens of available EEG/iEEG data collection systems". This is the
  same heterogeneity problem the `eeg-models` strand records at the model level, stated at the
  archive level.
- **The HED argument**: "Archived time series data typically require that standardized terms be
  used to describe the nature of all experimental events of interest ... Although BIDS-formatted
  data sets contain detailed metadata, the BIDS standards in themselves do not constitute a system
  for adequately describing the timeline of the recording."
- **Stated motivation for the whole stack**: enabling analyses that "cannot exploit consistencies in
  complex data that can only be identified in and extracted from large to very large data
  collections using new statistical and machine learning methods" — which is the pretraining
  argument, made in 2022 by the archive builders.
- **Database URL**: https://nemar.org.
- **Incidental sighting during retrieval**: Unpaywall's repository record for the ISRUC-Sleep paper
  points at a NEMAR DOI (`10.82901/nemar.nm000111`), so NEMAR mints its own dataset identifiers and
  those identifiers propagate into open-access indexes. Anyone resolving a NEMAR DOI expecting a
  paper will get a dataset.

## Open questions / limitations

- NEMAR holds no data of its own. Every access-route, licence and format question resolves to the
  underlying OpenNeuro dataset, so this card cannot certify anything about a specific corpus.
- **Scale figures, as of the paper's own snapshot dates** (this bullet previously asserted the
  paper reported none of these):

  "As of February 2022, there were 72 EEG datasets (from 2664 participants) on NEMAR, 22 MEG
  datasets (from 365 participants) and 12 iEEG datasets (from 202 participants). Of the 72 EEG
  datasets, 37 use the EEGLAB data format and have likely been formatted using the bids-matlab-tools
  EEGLAB plug-in". For the underlying archive: "The OpenNeuro archive (8) currently offers more than
  644 open neuroimaging datasets from more than 22 000 participants." And a usage figure: "As of
  January 2022, the bids-matlab-tools plug-in, available from the EEGLAB plug-in manager, had been
  downloaded 844 times."

  **Corrected 2026-08-01, Phase 4 audit.** The bullet previously read "The paper reports no dataset
  count, no per-modality inventory and no usage figures in the text read here, so this card carries
  no scale numbers." All three sub-claims are false, and the missing figures are exactly the
  per-modality inventory a strand deciding where to look for EEG data needs. Note the 72 EEG
  datasets are the whole of NEMAR's EEG holdings as of February 2022 — a small number, which
  strengthens rather than weakens this card's point that the registry sweep for a STRUM-like dyadic
  corpus had little to find. Note also that NEMAR's restatement of OpenNeuro's size (644 datasets,
  22 000 participants) is larger than the "more than 600 datasets" quoted from `openneuro-2021`
  elsewhere on this card; the two are snapshots at different dates, not a conflict.
- The compute integration is tied to the Neuroscience Gateway and San Diego Supercomputer Center
  allocations. Whether it is usable by an arbitrary external project, and under what allocation
  process, is not something the read text settles.
- HED is described as necessary but the paper does not report what fraction of the archived EEG
  datasets actually carry HED annotations. Without that, the event-description gap it identifies is
  named rather than closed.
- No PDF is archived: the article is CC BY-NC per Europe PMC but the Oxford University Press PDF
  endpoint and the Europe PMC full-text repository endpoint both refused automated download (see
  `meta.json`).

## Citations

Primary: `nemar-2022`

- `openneuro-2021` — the archive NEMAR is a gateway to; every dataset is ultimately an OpenNeuro
  dataset.
- `eeg-bids-2019` — the EEG formatting standard NEMAR requires, sharing one author (Delorme) with
  this paper. (This line previously said two; the author lists intersect only in Delorme.)
- `strum-2018` — the Swartz Center connection; STRUM was not located in NEMAR or in any other
  registry swept for this strand.
- Bigdely-Shamlo et al., Hierarchical Event Descriptors — the event-annotation standard this paper
  positions as BIDS's necessary complement, and also a reference in STRUM's own bibliography.
