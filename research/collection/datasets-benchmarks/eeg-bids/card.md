---
slug: eeg-bids
type: standard
strand: datasets-benchmarks
year: 2019
authors: [Pernet, Appelhoff, Gorgolewski, Flandin, Phillips, Delorme, Oostenveld]
venue: Scientific Data 6:103 (Comment)
doi: 10.1038/s41597-019-0104-8
url: https://doi.org/10.1038/s41597-019-0104-8
license: CC BY 4.0
modalities: [scalp-eeg]
tags: [data-standard, bids, events-tsv, stimulus-markers, channels-vs-electrodes, coordsystem, edf, brainvision, hed, validator]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

The specification that makes an EEG dataset machine-readable without a human reading the lab's
notes — and, for this project specifically, the one that requires stimulus markers to be written out
explicitly as an `events.tsv` file rather than left implicit in a trigger channel.

## Summary

EEG-BIDS extends the Brain Imaging Data Structure to scalp electroencephalography, building on the
earlier magnetoencephalography extension and released alongside the intracranial extension. It
defines a subject-and-session directory layout, a set of required and optional sidecar files, and a
restricted list of permitted raw data formats. Two "official" formats are recommended, European Data
Format and the BrainVision Core Data Format, chosen for community uptake, open documentation with
open-source readers and writers in at least two widely used languages, and numerical precision
("EDF: 16 bits, BrainVision Core Data Format: 32 bits"); two "unofficial" formats are also allowed,
the EEGLAB `.set`/`.fdt` pair and Biosemi `.bdf`. Critically, the format choice is made not to matter
for metadata: "critical metadata about the recording are always available in BIDS .tsv and .json
files". The paper also disambiguates two term pairs the field uses loosely, electrode versus channel
and fiducial versus anatomical landmark, and points to a validator, exemplar datasets, and
converters in FieldTrip, EEGLAB, MNE-Python and SPM12. It is explicitly limited to raw data;
derivatives are deferred to a separate extension proposal.

## Relevance to the review

Three parts of this specification bear on the project directly.

The first is `events.tsv`, and it is the reason this card is `relevance: medium` rather than low. This project's labels
come from stimulus markers, and the specification's rationale for requiring an events file is exactly
the problem that creates: "while such information is often present as one or several binary 'trigger'
channels in the EEG recordings, the representation of events is rarely explicit in the original
data". An `events.tsv` "should be present, encoding all of the parameters of the experimental design
(onset of events, trial type, duration, responses, etc.)", with a `stim_file` column able to
reference the presented stimulus in the dataset's `stimuli/` directory. Whether STRUM's spoken and
written conditions are recoverable as an explicit event table or only as trigger codes needing a
lab-specific decoding key is a concrete question this specification frames, and the answer determines
how much of the label pipeline this project has to write.

The second is the electrode-versus-channel distinction, which the paper states precisely: "(i) An EEG
electrode is a contact point attached to the skin, (ii) a channel is the combination of the analog
differential amplifier and analog-to-digital converter that result in a potential (voltage)
difference being stored in the EEG dataset", and "the 'reference' and 'ground' electrodes should in
general not be referred to as channels and only as electrodes". This is the same distinction that
matters for whether a coordinate-based checkpoint can ingest a dataset: `channels.tsv` describes the
stored signals, `electrodes.tsv` plus `coordsystem.json` describe positions in a named coordinate
frame. A model like REVE needs the latter; a dataset that ships only the former forces the
approximation documented on the `reve-2025` card.

The third is the connection to the corpus, which this paper only gestures at — "Accessibility is not
directly addressed by BIDS, but by repositories that build on BIDS, such as OpenNeuro
(https://openneuro.org)" — and which the `openneuro` card supplies. Per `openneuro`, that is
Markiewicz et al. 2021 and not this paper, every upload to OpenNeuro "must first pass a BIDS
validation step" and "more than 60 EEG datasets have been deposited since the publication of the
BIDS-EEG standard in 2019". So the growth in the heterogeneous, non-clinical part of the pretraining
corpora that `reve-2025` and `omnieeg-bench` both depend on is downstream of this specification.
*Correction, made during review: an earlier version of this card stated the validation rule and
quoted the 60-dataset sentence inside the discussion of this 2019 paper, with no attribution. Neither
is in this paper, which could not report deposits made since its own publication; both are in the
`openneuro` source.*

## Notable details

- **Directory layout.** Dataset root holds `dataset_description.json`, `README`, `participants.tsv`
  with an optional `participants.json`, and optional `sourcedata/`, `stimuli/` and `code/`
  directories. Per subject: `sub-XX/[ses-YY/]eeg/`. JSON sidecars at higher levels are inherited by
  lower levels unless overridden — the Inheritance Principle.
- **Required files in the `eeg/` directory.** The raw file `sub-XX_task-YY_eeg.<extension>`; an
  `sub-XX_task-YY_eeg.json` that "exhaustively specifies among other metadata details of the
  experimental task and the EEG recording system"; `sub-XX_task-YY_channels.tsv`, which "must be
  specified"; and `sub-XX_task-YY_events.tsv`. `sub-XX_task-YY_electrodes.tsv` and
  `sub-XX_task-YY_coordsystem.json` "should be specified if the positions of the electrodes are
  known".
- **Events.** `events.tsv` encodes "onset of events, trial type, duration, responses, etc.", with a
  `stim_file` column referencing the `stimuli/` directory. The Hierarchical Event Descriptor system
  "for precise annotation of events has been integrated". The formal column requirements are in the
  linked specification and in the paper's Figure 1, which is an image and did not survive extraction;
  this card therefore does not enumerate required columns.
- **Channel and electrode metadata.** `channels.tsv` "can contain information not present in the raw
  EEG data file such as filter settings and channel status (good/bad)"; `electrodes.tsv` plus
  `coordsystem.json` "provide electrode locations and specify which coordinate framework to use".
- **Permitted raw formats.** Official: European Data Format and BrainVision Core Data Format.
  Unofficial but allowed: EEGLAB `.set`/`.fdt` and Biosemi `.bdf`.
- **Tooling.** The `bids-validator`, "a JavaScript application that runs locally as a command line
  version (using Node.js) or within an Internet browser"; the BIDS starter kit; a BIDS-examples
  repository with zero-byte data files; exporters `std_tobids.m` in EEGLAB and `data2bids.m` in
  FieldTrip; readers `spm_bids.m` in SPM12 and MNE-BIDS.
- **Scope limit.** Raw data only: "the development of BIDS for EEG derivatives is also already
  underway (BIDS Extension Proposal 21)".
- **Article type**: this is a Comment in *Scientific Data*, not a research article. Licence CC BY 4.0.
  Declared competing interest: one author is a part-time Kaggle research consultant for Google.
- The paper's motivation for standardization is analytic reproducibility rather than machine
  learning: it cites COBIDAS-MEEG and observes that "even the simplest processing pipeline already
  contains eight separate steps", concluding that EEG-BIDS "is the first necessary step toward
  achieving validated and reproducible data analysis".

## Open questions / limitations

- **The requirement level for `electrodes.tsv` is stated two ways.** The summary says the electrodes
  and coordinate-system files "should be specified if the positions of the electrodes are known";
  the specific-considerations section says researchers "must specify a 'channels.tsv' file and may in
  addition specify an 'electrodes.tsv' file". A conditional *should* and an unconditional *may* are
  not the same obligation, and the difference decides whether a coordinate-based checkpoint can rely
  on positions being present in a conformant dataset.
- **"Only two" official formats, then four are permitted**, in the same paragraph. The word "only" is
  doing loose work; a tool that supports the two official formats will not read all conformant
  datasets.
- **The column specifications are not in this document.** Figure 1 carries the directory tree and
  the TSV previews where the actual column names for `events.tsv`, `channels.tsv` and
  `electrodes.tsv` appear, and it is an image. Anyone implementing against this needs the online
  specification, not the paper. This card records what the paper says and no more.
- **No `run-` entity appears.** The naming pattern given is `sub-XX_task-YY_eeg.<extension>`, with no
  run index, and the word "run" does not occur in the paper. Since Brain Imaging Data Structure does
  define a run entity, the paper's naming examples are incomplete rather than authoritative — but for
  a project reasoning about run-wise versus session-wise splits, the paper offers no guidance and
  uses "session" for at least three different things: a directory level, a study-design unit, and a
  span of time.
- **The specification says nothing about evaluation, splits, or leakage.** That is out of its scope,
  but it means it does not require the one piece of metadata that `kamrud-2021-data-partitioning`
  argues every release needs: nothing in EEG-BIDS obliges a pre-partitioned release to document its
  grouping. Subject identity is recoverable from the directory structure, which is the necessary
  condition; whether a derived split respects it is not the standard's concern.
- The paper is seven years old (received 16 January 2019, accepted 7 May 2019, published in volume 6
  of 2019) and the specification has moved; version numbers of the standard are not
  given anywhere in the paper, so it cannot be used to determine what a current conformant dataset
  contains.
- Small-caps rendering in the retrieved PDF flattens author names and headings to lowercase
  ("arnaud Delorme", "Swart center for computational neuroscience" for Swartz Center), and the
  two-column author block interleaves names and affiliation superscripts, so the author order on this
  card was reconstructed by matching superscripts against the Author Contributions section.

## Citations

Primary: `eeg-bids`

- `openneuro` — the archive that enforces this specification at upload, and where most conformant EEG
  datasets live.
- `edf-plus` — one of the two official raw formats, and the one whose annotation mechanism
  `events.tsv` supersedes for label storage.
- `mne-python` — one of the named readers, via MNE-BIDS.
- Robbins et al., Hierarchical Event Descriptors — the event-annotation system the specification
  states has been integrated; not carded separately in this strand.
- `neuralbench` — a benchmark whose YAML task configuration reads event types and event fields in the
  form this specification standardizes.
