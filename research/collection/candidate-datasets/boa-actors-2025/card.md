---
slug: boa-actors-2025
type: dataset
strand: candidate-datasets
year: 2025
authors: [Hendry, Cruz-Garza, Delgado-Jiménez, Lima-Carmona, Aguilar-Herrera, Ramírez-Moreno, Ravindran, Paek, Smith, Kan, Fors, Alam, Liu, Noble, Contreras-Vidal]
venue: Scientific Data
doi: 10.1038/s41597-025-05713-2
url: https://doi.org/10.1038/s41597-025-05713-2
license: CC BY-NC-ND 4.0 (article)
modalities: [scalp-eeg, eog, blood-volume-pulse, electrodermal-activity, skin-temperature, accelerometry, video]
tags: [hyperscanning, dyadic, mobi, theatre, hardware-trigger-sync, average-reference, 32-channel, empatica-e4, event-annotation, figshare]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

Three actor dyads, a director, and three audience members were instrumented simultaneously with
32-channel mobile EEG plus wristband autonomic sensors across six rehearsals and three public
performances — one of the very few public datasets where two or more people wearing EEG were
recorded at the same time in a shared, naturalistic task.

## Summary

A longitudinal mobile brain-body imaging (MoBI) release covering a week in which a theatre
director staged one emotionally charged scene with three dyads of undergraduate acting students.
The authors describe it as "simultaneously recorded physiological and visual data using a
hyperscanning approach based on hardware triggers". Each participant wore a 32-channel mobile
EEG cap (BrainAmpDC with actiCAP and MOVE, Brain Products) sampled at 500 Hz, of which four
electrodes were used for electrooculography, so 28 EEG plus 4 EOG. Actors additionally wore an
Empatica E4 wristband giving blood volume pulse at 64 Hz, heart rate derived from it at 1 Hz,
skin temperature at 4 Hz, electrodermal activity at 4 Hz, and triaxial arm acceleration at 32 Hz,
plus an APDM Opal inertial measurement unit on the headset and a second on the body at 128 Hz.
Five video streams were recorded. Every rehearsal and performance video was annotated
instant-by-instant into a spreadsheet giving the sample-level start and end of each observed
activity, so the dataset ships with a behavioural event timeline rather than only a stimulus log.

## Relevance to the review

This is the closest published analogue to what the project believes STRUM is: two or more people
wearing EEG at the same time, doing a shared task that is neither a screen paradigm nor a resting
state, with peripheral autonomic channels alongside the EEG. It is therefore useful to this
strand as a specification of what such a recording costs and what it yields, independent of any
judgement about whether the project should use it.

Three specifications are worth pulling forward. First, the synchronisation is by custom hardware
trigger with post-hoc alignment against a filmed UTC clock, not by the Lab Streaming Layer, and
no numeric synchronisation precision is reported — so this dataset cannot bound cross-participant
timing the way `lsl-2024` can. Second, the derivation is documented explicitly: the released
`.set` structures carry `EEG.ref` as "Channel referencing to the common average", and the paper's
preprocessing re-references to the average through the PREP pipeline. An average reference is not
a per-electrode potential, which matters for any checkpoint that assumes one. Third, the labels
are video-derived behavioural annotations, not stimulus condition codes, which places this
dataset in a different label-provenance class from every screen-paradigm dataset in this strand.

## Notable details

**Fixed field set:**

- **Participants**: 10 — three dyads of student actors (N = 6), one theatre director (N = 1), and
  three audience members (N = 3). The director was instrumented for rehearsals 1 and 2; audience
  members were instrumented only at the performance.
- **Simultaneous participants per recording**: 3. Each recording covers one dyad (P01, P02) plus
  either the director or an audience member (P03), all instrumented at once.
- **Channels**: 32 per participant — "32 channels: 28 channels for EEG and the remaining 4
  channels for EOG". Exception recorded by the authors: "P01 on Dyads A/B/C included 31 EEG
  channels (27 EEG, 4 EOG), instead of 32, due to error with the electrode CP6, which had to be
  removed."
- **Sampling rate**: EEG and EOG 500 Hz. Blood volume pulse 64 Hz; heart rate 1 Hz;
  electrodermal activity 4 Hz; temperature 4 Hz; wrist acceleration 32 Hz; inertial measurement
  units 128 Hz. Video 1080p at 25 fps after post-production.
- **Peripheral channels present**: EOG (4 channels, from the EEG cap, and used as signal for
  H-infinity ocular filtering rather than only discarded), blood volume pulse, heart rate,
  electrodermal activity, skin temperature, triaxial wrist acceleration, head and body inertial
  measurement units. No electrocardiography and no respiration. Audio was recorded but is
  withheld from the release for copyright reasons.
- **Total hours**: not reported as a single figure. The paper states recording1 and recording2 are
  each "roughly an hour long" and recording3 is "roughly 7 minutes long", for three participants
  in each of three dyads.
- **Task**: rehearsal and public performance of a single emotionally charged theatre scene,
  including table readings, Meisner repetition exercises, partial and full rehearsals with
  director feedback, and three staged performances before an audience.
- **Label type**: continuous behavioural event annotation, per session, derived from video.
- **Label source**: human annotation of video by the research team, with each event carrying the
  exact sample numbers at which it starts and ends in each recorded stream.
- **License**: article CC BY-NC-ND 4.0. The data licence is not stated in the paper text and is
  recorded separately in `meta.json`.
- **Access route**: open download from FigShare, no registration described.

**Other specifications:**

- **Derivation scheme**: average reference. The released EEGLAB structure documents
  `EEG.ref` as "Channel referencing to the common average", and preprocessing applies "robust
  re-referencing though the PREP pipeline".
- **Electrode layout**: `EEG.chanlocs` carries "the spatial location of each channel N according
  to the international 10-20 system", with four of the cap's electrodes placed around the eyes for
  EOG rather than on the scalp.
- **Synchronisation**: custom hardware trigger for video, wireless EEG and head IMU, aligned in
  MATLAB; Empatica wristband data aligned by matching Unix timestamps against a filmed screen
  showing UTC from time.gov. No numeric alignment error is reported.
- **Suggested preprocessing shipped with the paper**: downsample to 240 Hz for joint EEG-video
  visualisation, H-infinity ocular filtering driven by the four EOG channels (q = 1e-10, p0 = 0.5,
  gamma = 1.15), average re-reference via PREP, 5th-order Butterworth band-pass 0.01–50 Hz, a
  second-order motion artefact filter, Artifact Subspace Reconstruction rebuilding any period whose
  amplitude exceeds "κ = 10 standard deviations", then extended Infomax ICA with dipole fitting
  against the MNI template. (ASR *reconstructs* the contaminated periods rather than rejecting
  them; this line previously read "artefact rejection at 10 standard deviations".)
- **Known data gaps recorded by the authors**: recording 3 for dyad A is missing its final two
  minutes of inertial data due to a technical error.

## Open questions / limitations

- No synchronisation precision is quantified anywhere in the paper. For a dataset whose stated
  purpose includes quantifying "synchronization of physiological activity patterns within and
  across all participating individuals", the absence of a measured cross-participant timing error
  is a real limit on what inter-participant analyses it can support.
- Ten participants total, three of them recorded only for seven minutes. This is small even by the
  standards of the datasets carded in this strand, and the design is longitudinal within a single
  week rather than cross-sectional.
- The self-described "hyperscanning" framing is looser than the recording warrants in one
  respect: the third instrumented person differs by session (director during rehearsals, a
  different audience member at each performance), so the three simultaneously recorded
  participants are not a stable triad across sessions.
- The paper describes the four eye electrodes as part of the "32-channel EEG head cap" and
  elsewhere as EOG. That is a labelling choice, not a separate amplifier: the ocular channels
  share the EEG amplifier and sampling rate. A reader treating them as an independent peripheral
  modality should know they come from the same cap.
- Audio is absent from the release, which removes the ability to time-lock any analysis to the
  spoken script — relevant here because the project's own label plan is about spoken versus
  written stimulus.

## Citations

Primary: `boa-actors-2025`

- `livewire-2024` — Pacheco-Ramírez et al., Sci Data 2024. Same laboratory, same MoBI toolchain,
  two simultaneously recorded dancers instead of actor dyads.
- `lsl-2024` — the synchronisation approach this dataset did *not* use, and the reference point
  for what a measured synchronisation error looks like.
- `amigos-2021` — the other multi-person entry in this strand, with four simultaneous viewers but
  a screen paradigm rather than a shared naturalistic task.
- Delorme & Makeig, EEGLAB — the toolbox the released `.set` files and the recommended
  preprocessing pipeline are built on.
