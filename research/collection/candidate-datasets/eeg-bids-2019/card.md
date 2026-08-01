---
slug: eeg-bids-2019
type: standard
strand: candidate-datasets
year: 2019
authors: [Pernet, Appelhoff, Gorgolewski, Flandin, Phillips, Delorme, Oostenveld]
venue: Scientific Data
doi: 10.1038/s41597-019-0104-8
url: https://doi.org/10.1038/s41597-019-0104-8
license: CC BY 4.0
modalities: [scalp-eeg, metadata-standard]
tags: [bids, format-standard, channels-tsv, electrodes-tsv, coordsystem-json, edf, brainvision, eeglab, electrode-coordinates, machine-readable-metadata]
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

EEG-BIDS is the extension of the Brain Imaging Data Structure that makes electrode positions,
channel status, reference and filter settings machine-readable in fixed sidecar files — which is
exactly the metadata a layout-flexible pretrained checkpoint needs and which most non-BIDS datasets
leave in prose.

## Summary

An extension to the Brain Imaging Data Structure covering EEG, "along with tools and references to
a series of public EEG datasets organized using this new standard". Within each subject directory,
an `eeg` subdirectory holds files named `sub-XX_task-YY_eeg.<extension>`. A
`sub-XX_task-YY_channels.tsv` "must be specified describing the parameters of the data
acquisition", and `sub-XX_task-YY_electrodes.tsv` plus `sub-XX_task-YY_coordsystem.json` "should be
specified if the positions of the electrodes are known". The `channels.tsv` file "can contain
information not present in the raw EEG data file such as filter settings and channel status
(good/bad)"; the `coordsystem.json` file specifies "which coordinate framework to use to interpret
the electrode locations (for example with respect to a T1 weighted MRI scan)". An `events.tsv` file
records all events and can reference the presented stimuli through a `stim_file` column into the
dataset's `stimuli` directory. Optional `sourcedata` and `code` directories allow the conversion
and preprocessing to be reproduced. The specification names only two recommended official data
formats: the European Data Format, "an ongoing international effort ... that began in 1992", and
the BrainVision Core Data Format.

## Relevance to the review

The `eeg-models` strand recorded that a layout-flexible checkpoint takes one 3D coordinate per
channel, and that when a coordinate is not available the model falls back on inferring it from a
standard label — or, for a bipolar derivation, on the midpoint of the electrode pair. That
fallback chain is the reason this specification belongs in this strand rather than being pure
infrastructure. A dataset with `electrodes.tsv` and `coordsystem.json` populated hands the
checkpoint measured coordinates in a named frame; a dataset without them forces the fallback. So
whether a candidate dataset is BIDS-compliant, and specifically whether those two optional files
are present, is a concrete predictor of whether a checkpoint can ingest it without approximation.

`channels.tsv` matters for a second reason specific to this project. It is the file that records
channel *type* and status, so it is where the distinction this strand cares about — which
peripheral channels are present, and whether a channel is EEG, EOG, ECG, EMG or MISC — is machine
readable rather than buried in a methods paragraph. Two of the candidate datasets carded here
(`tes-eeg-ecg-2021` and `hinss-2023-passive-bci`) are distributed in BIDS and therefore expose
their peripheral inventory in this form.

## Notable details

- **Required and recommended sidecars**: `channels.tsv` is required. `electrodes.tsv` and
  `coordsystem.json` are recommended, conditional on electrode positions being known — which means
  their absence is permitted and is therefore common.
- **What `channels.tsv` adds over the raw file**: "filter settings and channel status (good/bad)",
  i.e. information "not present in the raw EEG data file".
- **What `coordsystem.json` fixes**: the coordinate framework in which `electrodes.tsv` positions
  are to be interpreted, for example relative to a T1-weighted MRI.
- **Recommended formats, only two**: European Data Format (EDF) and the BrainVision Core Data
  Format. The authors note that although BrainVision "was designed by Brain Products GmbH for its
  proprietary EEG recording equipment and analysis software", it is open. The stated criteria for
  admitting a format include meeting "the technical requirements of neuroscientific workflows, such
  as saving numerical data with high precision".
- **Events and stimuli**: `events.tsv` records everything that happened and can point at the actual
  stimulus files through `stim_file`, so a dataset with a language manipulation can make its
  stimulus modality machine-readable rather than implicit in condition codes.
- **Reproducibility directories**: `sourcedata` for original unformatted data, `code` for
  conversion and preprocessing scripts, `stimuli` for the presented materials.
- **Adoption in this strand**: `tes-eeg-ecg-2021` (OpenNeuro `ds003670`), `hinss-2023-passive-bci`
  (Zenodo, BIDS) and `mous-2019` (Donders repository, BIDS) are all distributed in this format;
  `boa-actors-2025`, `livewire-2024`, `deap-2012`, `amigos-2021` and `sleep-edfx` are not.

## Open questions / limitations

- Compliance is a floor, not a guarantee. `electrodes.tsv` and `coordsystem.json` are recommended
  rather than required, so a fully valid BIDS-EEG dataset can contain no electrode coordinates at
  all — precisely the case where a coordinate-based checkpoint has to fall back on label inference.
  Validity therefore does not certify the property this project needs.
- The specification standardises *where* metadata lives, not whether it is correct. A
  `channels.tsv` can name a reference that does not match what was recorded, and nothing in the
  format detects that.
- Neither recommended format expresses a derivation scheme as a first-class concept. A bipolar
  channel appears in `channels.tsv` as a channel with a name like `Fpz-Cz`; whether downstream
  tooling parses that as a difference between two sites is left to convention.
- This is the 2019 specification. BIDS has continued to evolve, so any current claim about required
  versus optional fields should be checked against the live specification rather than against this
  paper.
- The paper is a specification announcement, so it reports no measurements. There is nothing here to
  contradict or to verify numerically.

## Citations

Primary: `eeg-bids-2019`

- `openneuro-2021` — the archive that enforces and hosts BIDS datasets, including the BIDS copy of
  `tes-eeg-ecg-2021`.
- `nemar-2022` — the EEG/MEG/iEEG-specific gateway layered on OpenNeuro, which runs quality
  assessment over BIDS-formatted neuroelectromagnetic data.
- Kemp & Olivan (2003), EDF+ — one of the two recommended data formats, and the format
  `sleep-edfx` is distributed in.
- Gorgolewski et al. (2016), the original BIDS specification this extends.
