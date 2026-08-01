---
slug: livewire-2024
type: dataset
strand: candidate-datasets
year: 2024
authors: [Pacheco-Ramírez, Ramírez-Moreno, Kukkar, Rao, Huber, Brandt, Noble A, Noble D, Ealey, Contreras-Vidal]
venue: Scientific Data
doi: 10.1038/s41597-024-04010-8
url: https://doi.org/10.1038/s41597-024-04010-8
license: CC BY-NC-ND 4.0 (article); CC BY 4.0 (data, stated in Data Records)
modalities: [scalp-eeg, eog, inertial-measurement, video]
tags: [hyperscanning, dyadic, mobi, dance, linked-ear-reference, 28-channel, manual-trigger-sync, figshare, longitudinal, raw-data-only]
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

Two professional dancers were recorded simultaneously and in synchrony with 28-channel EEG,
4-channel EOG and head inertial sensors across ten rehearsal and performance sessions spanning
four months — a two-person recording whose data are released under an explicit CC BY 4.0 grant,
unlike most of the datasets in this strand.

## Summary

A mobile brain-body imaging release built around "LiveWire", a composition of five choreographed
music and dance sections. The authors state that recordings "were obtained simultaneously and in
synchrony for the two participants". Each dancer wore a 28-channel scalp EEG montage at 1000 Hz,
four EOG electrodes at 1000 Hz (right and left temples for horizontal movement, above and below
the right eye for vertical), and an APDM Opal inertial measurement unit on the forehead sampling
a 3-axis accelerometer, gyrometer and magnetometer at 128 Hz. Reference electrodes were placed on
both earlobes and impedances held below 50 kΩ. Ten sessions were collected over four months —
seven rehearsals and three performances — each with accompanying video for behavioural tagging.
Real-time inter-brain synchrony additionally drove stage lighting through a DMX interface during
performance, which is a property of the show rather than of the released data. All released data
are raw; the authors recommend MATLAB and EEGLAB for processing.

## Relevance to the review

Together with `boa-actors-2025` this is one of the only two entries found in this strand where
EEG from more than one person was recorded at the same time in a shared naturalistic task, so it
is part of the evidence base for how thin category 1 is.

Two specifications distinguish it from its sibling. The derivation is linked-earlobe referential
rather than average, which is the derivation a layout-flexible checkpoint can ingest most
directly: each channel is a potential at a named 10-20 site, so a coordinate can be assigned
without the midpoint approximation that a bipolar derivation forces. And the data licence is
stated in the paper itself — "hosted on FigShare ... under the terms of the Attribution 4.0
International Creative Commons License" — which is unusual in this strand and makes the
redistribution question answerable without a separate check.

The synchronisation is by manual trigger, and no precision figure is given, so like its sibling
this dataset cannot bound cross-participant timing numerically.

## Notable details

**Fixed field set:**

- **Participants**: 2. Two healthy professional dancers, "age: 32 ± 1 years, 1 male and 1
  female", designated D1 and D2, with on average 17.5 ± 2.5 years of dance experience and 11 ± 1
  years performing professionally.
- **Simultaneous participants per recording**: 2. Both dancers were instrumented and recorded at
  the same time in every session.
- **Channels**: 28 EEG plus 4 EOG per dancer. Scalp sites are enumerated in the paper and follow
  the 10-20 system (the extracted list ends "... O9, O1, Oz, O2, PO10").
- **Sampling rate**: EEG 1000 Hz; EOG 1000 Hz; inertial measurement unit 128 Hz.
- **Peripheral channels present**: EOG (4 channels, usable as signal — the paper illustrates
  ocular activity taken from them) and head inertial measurement. No electrocardiography, no
  electrodermal activity, no respiration. Note the difference from `boa-actors-2025`, which adds
  Empatica wristband autonomic channels; this dataset does not have them.
- **Total hours**: not reported. Ten sessions over four months (seven rehearsals, three
  performances); no per-session duration is given.
- **Task**: rehearsal and public performance of a five-section choreographed dance piece with
  live music.
- **Label type**: session type (rehearsal versus performance) plus video-derived behavioural
  tagging of choreography sections; the release is explicitly raw, with no epoch-level label
  files described.
- **Label source**: experimental protocol (session identity, choreography section) and human
  video tagging.
- **License**: article CC BY-NC-ND 4.0; data CC BY 4.0 as stated in Data Records.
- **Access route**: open download from FigShare collection 10.6084/m9.figshare.c.6274752. No
  registration, no data use agreement. "No custom code is needed to access the data."

**Other specifications:**

- **Derivation scheme**: referential to linked earlobes — "Reference electrodes were placed on
  both earlobes". Not bipolar, not average-referenced as distributed.
- **Synchronisation**: "Manual triggers were used to synchronize EEG, EOG and IMU data." No
  measured offset or jitter is reported.
- **Impedance criterion**: below 50 kΩ for all electrodes before each session, which is loose
  relative to the 25 kΩ used by `hinss-2023-passive-bci` and the 20 kΩ used by
  `tes-eeg-ecg-2021`, and is a consequence of the mobile active-electrode setup.

## Open questions / limitations

- Two participants. Any model fitted to this dataset is fitted to two people, so nothing
  subject-general can be established from it, and a subject-wise split has exactly two folds.
- No total recording duration is reported anywhere in the paper, so the dataset's size in hours
  cannot be stated without downloading it.
- No synchronisation precision is reported, and "manual triggers" is a weaker mechanism than the
  hardware triggers used by the same laboratory in `boa-actors-2025`. Cross-dancer timing is
  therefore unbounded in the published record.
- The two dancers are highly trained specialists in a specific movement domain, which the paper
  presents as a strength for studying expertise and which is simultaneously a limit on how far
  anything learned from them generalises.
- The released data are raw with no artefact rejection applied, and dance involves continuous
  large-amplitude head and body movement, so the usable fraction of the EEG is unknown from the
  paper.
- The stage-lighting feedback loop means the performances were not passive observation: the
  dancers' own inter-brain synchrony changed the visual environment during recording. Any
  analysis treating session as an independent variable inherits that loop.

## Citations

Primary: `livewire-2024`

- `boa-actors-2025` — same laboratory and toolchain, three actor dyads plus director and
  audience; the closest comparator, and the one that adds autonomic wristband channels.
- `lsl-2024` — the synchronisation framework not used here; the reference point for what a
  measured multi-stream timing error looks like.
- Delorme & Makeig, EEGLAB — the recommended processing environment for the released raw data.
- Basso et al., Synchronicity Hypothesis of Dance — the theoretical motivation the authors cite
  for recording two dancers rather than one.
