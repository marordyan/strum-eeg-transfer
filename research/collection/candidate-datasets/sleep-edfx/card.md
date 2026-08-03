---
slug: sleep-edfx
type: dataset
strand: candidate-datasets
year: 2018
authors: [Kemp]
venue: PhysioNet (Sleep-EDF Database Expanded v1.0.0)
doi: 10.13026/C2X676
url: https://physionet.org/content/sleep-edfx/1.0.0/
license: Open Data Commons Attribution License v1.0
modalities: [scalp-eeg, eog, emg, respiration, body-temperature, event-marker]
tags: [polysomnography, bipolar-derivation, fpz-cz, pz-oz, edf, edf-plus, physionet, odc-by, expert-scored-hypnogram, 197-recordings]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-applicable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

197 whole-night polysomnograms with expert-scored hypnograms, distributed openly under Open Data
Commons Attribution with no registration, whose two EEG channels are *bipolar derivations*
(Fpz-Cz and Pz-Oz) rather than referential ones — which makes it the concrete test case for
whether a layout-flexible checkpoint can ingest a bipolar montage.

## Summary

The Sleep-EDF Database Expanded is PhysioNet's canonical sleep resource: "197 whole-night
PolySomnoGraphic sleep recordings, containing EEG, EOG, chin EMG, and event markers. Some records
also contain respiration and body temperature." It merges two studies. The 153 sleep-cassette
files come from a 1987–1991 study of age effects on sleep in healthy participants aged 25 to 101
with no sleep medication, recorded at home on a modified cassette recorder over two subsequent
day-night periods of about 20 hours each. The 44 sleep-telemetry files come from a 1994 study of
temazepam effects in 22 participants with mild difficulty falling asleep, recorded in hospital
over two nights of about 9 hours, one after temazepam and one after placebo. Hypnograms were
"manually scored by well-trained technicians ... according to the 1968 Rechtschaffen and Kales
manual", with stages W, R, 1, 2, 3, 4, M (movement time) and ? (not scored), and the scoring
technician is identifiable from the eighth letter of each hypnogram filename. Recordings are in
European Data Format, hypnograms in EDF+.

## Relevance to the review

Two things make this entry load-bearing for the strand rather than merely another sleep dataset.

First, the derivation. The EEG channels are stated as coming "from Fpz-Cz and Pz-Oz electrode
locations", and the page's own reference list cites van Sweden et al. (1990), "Alternative
electrode placement in (automatic) sleep scoring (Fpz-Cz/Pz-Oz versus C4-A1/C3-A2)". These are
bipolar derivations — each channel is a potential *difference* between two named sites, not a
potential at one. That is exactly the case the `eeg-models` strand found REVE handling by
substituting the midpoint of the electrode pair, an approximation whose adequacy is untested. This
dataset is the cheapest available substrate on which that approximation could actually be probed,
because it is open, large, and unambiguously bipolar.

Second, the access route. Open Data Commons Attribution v1.0, "anyone can access the files, as
long as they conform to the terms of the specified license", 8.1 GB downloadable by browser, wget
or `aws s3 sync --no-sign-request`. Compared with the end-user licence agreements behind
`deap-2012` and `amigos-2021`, and the data use agreement behind `mous-2019`, this is the
lowest-friction access route in the strand and the one that requires no institutional paperwork.

The label provenance is expert rating, which is a third class distinct from stimulus condition and
self-report, and it comes with an identifiable scorer per record — so inter-rater agreement is at
least addressable, though the page does not report it.

## Notable details

**Fixed field set:**

- **Participants**: not stated as a single figure on the landing page. 153 sleep-cassette files
  from a study of "healthy Caucasians aged 25-101" (two nights per subject, with three nights lost
  to equipment failure — the first nights of subjects 36 and 52 and the second night of subject
  13), plus 22 participants in the sleep-telemetry study contributing 44 files. Per-subject
  spreadsheets `SC-subjects.xls` and `ST-subjects.xls` ship with the data.
- **Simultaneous participants per recording**: 1.
- **Channels**: 2 EEG (Fpz-Cz, Pz-Oz), 1 horizontal EOG, 1 submental chin EMG, 1 event marker.
  Sleep-cassette files "often also contain oro-nasal respiration and rectal body temperature".
- **Sampling rate**: EEG and EOG at 100 Hz in both studies. Submental EMG is highpass filtered,
  rectified and lowpass filtered into an envelope expressed in microvolts RMS and sampled at 1 Hz.
  Oro-nasal airflow, rectal body temperature and the event marker are also sampled at 1 Hz. In the
  telemetry study EMG is sampled at 100 Hz and the event marker at 1 Hz.
- **Peripheral channels present**: electrooculography (horizontal), submental electromyography,
  oro-nasal respiration and rectal body temperature (sleep-cassette records only). No
  electrocardiography. The EOG and EMG are diagnostic signals here rather than artefact
  references — sleep staging depends on them — so they are usable as signal by construction.
- **Total hours**: not stated as a total. 153 recordings of "about 20 hours each" plus 44 of
  "about 9 hours" implies roughly 3,450 hours by arithmetic from the reported figures. Total
  uncompressed size is stated exactly: 8.1 GB.
- **Task**: none. Whole-night sleep, at home for the cassette study and in hospital for the
  telemetry study.
- **Label type**: sleep stage per 30-second epoch (W, R, 1, 2, 3, 4, M, ?), as a hypnogram in
  EDF+ annotation form.
- **Label source**: expert rating. Manual scoring by trained technicians under the 1968
  Rechtschaffen and Kales criteria, scored from the Fpz-Cz/Pz-Oz derivations rather than the
  conventional C4-A1/C3-A2.
- **License**: Open Data Commons Attribution License v1.0, for the files.
- **Access route**: open download, no registration and no agreement. Browser ZIP, `wget -r -N -c
  -np https://physionet.org/files/sleep-edfx/1.0.0/`, or `aws s3 sync --no-sign-request
  s3://physionet-open/sleep-edfx/1.0.0/`.

**Other specifications:**

- **Derivation scheme**: bipolar. Fpz-Cz and Pz-Oz. This is the distinguishing feature of the
  dataset for this strand.
- **Format**: polysomnograms in EDF, hypnograms in EDF+; "All EDF header fields also comply with
  the EDF+ specs, and unrecorded signals were removed from the ST*PSG.edf files." Readable by
  EDFbrowser, Polyman, PhysioNet's LightWAVE and the WFDB software package; WFDB 10.4.5 and later
  "can read EDF files directly with no conversion required", though it "does not decode
  annotations in EDF+ files".
- **Provenance of the labels' own basis**: the page notes hypnograms were scored "based on
  Fpz-Cz/Pz-Oz EEGs instead of C4-A1/C3-A2 EEGs, as suggested by" van Sweden et al. So the label
  and the signal come from the same two channels — a mild circularity worth naming, though it is
  intrinsic to all expert-scored sleep data.
- **No dataset paper**: PhysioNet directs users to cite Kemp et al. (2000), IEEE Trans. Biomed.
  Eng. 47(9):1185–1194, which is a methods paper on slow-wave microcontinuity rather than a
  description of this database. The landing page is the primary documentation, and is what this
  card is written from.

## Open questions / limitations

- Two EEG channels. Every foundation-model checkpoint in the `eeg-models` strand is built for
  tens of channels, and most of a spatial encoder's capacity is unused on a two-channel bipolar
  montage. Whether transfer to such a sparse layout is meaningful is untested by any paper read
  here.
- The recordings are old — 1987–1991 and 1994 — with corresponding acquisition characteristics
  (100 Hz sampling, cassette-tape recording at home for the larger cohort).
- Sleep is not a cognitive-task paradigm. Nothing in this dataset bears on the project's
  spoken-versus-written label question; it is carded for its derivation scheme, its peripheral
  inventory, and its access route.
- The label derives from the same two channels the model would see, which is the circularity risk
  category 3 of this strand names. It is unavoidable in expert-scored polysomnography, but it means
  a high sleep-staging score is not evidence that a model has learned anything beyond the scoring
  rules.
- Per-subject demographics live in Excel spreadsheets shipped with the data rather than on the
  landing page, so the exact participant count could not be stated from the snapshot.

## Citations

Primary: `sleep-edfx`

- Kemp et al. (2000), IEEE Trans. Biomed. Eng. 47(9):1185–1194 — the publication PhysioNet
  directs users to cite; a slow-wave microcontinuity methods paper, not a data descriptor.
- van Sweden et al. (1990), Sleep 13(3):279–283 — the justification for the Fpz-Cz/Pz-Oz bipolar
  derivation over the conventional C4-A1/C3-A2.
- Kemp & Olivan (2003), Clin. Neurophysiol. 114:1755–1761 — the EDF+ specification the hypnograms
  conform to.
- `nemar-2022` and `openneuro-2021` — the other registries swept for this strand; PhysioNet's
  access model (open files under a named data licence, no account) is the least restrictive of
  the three.
