---
slug: sleep-edf-expanded
type: dataset
strand: datasets-benchmarks
year: 2018
authors: [Kemp]
venue: PhysioNet (Sleep-EDF Database Expanded v1.0.0)
doi: 10.13026/C2X676
url: https://physionet.org/content/sleep-edfx/1.0.0/
license: Open Data Commons Attribution License v1.0
modalities: [scalp-eeg, eog, emg, respiration, body-temperature, polysomnography]
tags: [sleep-staging, benchmark-dataset, pretraining-corpus, open-data-commons, edf-plus, hypnogram, two-channel-eeg, peripheral-physiology, physionet, checkpoint-mapping]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-applicable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

197 whole-night polysomnograms with expert hypnograms under an Open Data Commons Attribution
licence, two EEG derivations at 100 Hz — the sleep benchmark that BIOT, LaBraM, CBraMod, EEGPT and
REVE all report on, and one of the few standard benchmarks that ships peripheral physiology
alongside the EEG.

## Summary

The Sleep-EDF Database Expanded on PhysioNet contains 197 whole-night polysomnographic sleep
recordings with EEG, electrooculography, chin electromyography and event markers; some also carry
oro-nasal respiration and rectal body temperature. Each recording is paired with a hypnogram
manually scored by a trained technician. The data come from two studies. The 153 sleep-cassette
files were recorded in a 1987–1991 study of age effects on sleep in healthy participants aged 25 to
101 who took no sleep-related medication, two roughly 20-hour polysomnograms per participant over
consecutive day-night periods at their homes using a modified cassette recorder. The 44
sleep-telemetry files were recorded in a 1994 study of temazepam effects in 22 participants with
mild difficulty falling asleep but otherwise healthy, two roughly 9-hour nights in hospital, one
after temazepam and one after placebo. Scoring followed the 1968 Rechtschaffen and Kales manual, but
"based on Fpz-Cz/Pz-Oz EEGs instead of C4-A1/C3-A2 EEGs".

## Relevance to the review

Sleep-EDF is in this strand as a benchmark that pretrained checkpoints report on, and it is the one
whose properties most resemble what a peripheral-physiology comparison would need — which makes it
useful as a negative control on this project's third comparison rather than as a candidate dataset.
Every recording carries electrooculography and chin electromyography as recorded signals, and the
sleep-cassette subset adds oro-nasal airflow and body temperature. Yet no checkpoint or benchmark
suite in this corpus uses any of those channels: `adabrain-bench` tabulates Sleep-EDF as 2 channels
at 100 Hz in 30-second windows, meaning the two EEG derivations only. The peripheral channels are
present, standardized, and universally discarded. That is a fact about the field's practice that
bears directly on whether adding peripheral physiology to an EEG embedding is a novel contribution
or a neglected one, and it is exactly the kind of thing Phase 4 needs recorded rather than assumed.

The second use is as a scale reference. Sleep-EDF yields 414,961 labelled 30-second windows from 78
subjects in AdaBrain-Bench's preparation. Sleep staging is one of the tasks `neuralbench` reports as
"close to saturation". Any claim that foundation models transfer well should be read against the
fact that the tasks they are best at are the ones with hundreds of thousands of labelled epochs and
a physiologically stereotyped target — the opposite regime from a small dyadic language study.

A terminology caution for anyone reading the two derivations: the recordings are Fpz-Cz and Pz-Oz,
which are bipolar derivations, not signals at single electrodes. A checkpoint whose positional
encoding is computed from an electrode coordinate has no native representation for a difference
between two sites; `reve-2025` handles the analogous case on TUEV by substituting the midpoint of
the pair. That approximation applies here too and is not mentioned by any suite that reports
Sleep-EDF numbers.

## Notable details

Fixed field set required of every `type: dataset` card in this strand:

- **Participants**: not stated as a single number on the landing page. The sleep-cassette study is
  described as covering "healthy Caucasians aged 25-101" across 153 files, two nights per subject,
  with three nights lost ("the first nights of subjects 36 and 52, and the second night of subject
  13"); the sleep-telemetry study covers "22 Caucasian males and females". The commonly cited figure
  of 78 subjects for the sleep-cassette subset comes from benchmark preparations such as
  `adabrain-bench`, not from the landing page. Per-subject detail is in the `SC-subjects.xls` and
  `ST-subjects.xls` spreadsheets, which were not retrieved.
- **Channels**: 2 EEG derivations, Fpz-Cz and Pz-Oz, plus horizontal electrooculography, submental
  chin electromyography, and an event marker. Sleep-cassette files "often also contain oro-nasal
  respiration and rectal body temperature".
- **Sampling rate**: EEG and electrooculography at 100 Hz in both studies. Electromyography differs
  between the subsets. Sleep-cassette: "The submental-EMG signal was electronically highpass
  filtered, rectified and low-pass filtered after which the resulting EMG envelope expressed in uV
  rms (root-mean-square) was sampled at 1Hz. Oro-nasal airflow, rectal body temperature and the
  event marker were also sampled at 1Hz." Sleep-telemetry: "EOG, EMG and EEG signals were sampled at
  100 Hz, and the event marker at 1 Hz." *Correction, made during review: an earlier version of this
  card gave the 1 Hz rectified electromyography envelope as a property of the dataset as a whole. It
  is a property of the sleep-cassette subset; telemetry electromyography is at 100 Hz.*
- **Total hours**: not stated. Derivable in principle — 153 recordings of about 20 hours and 44 of
  about 9 hours — but the landing page gives no total and the durations are approximate, so this card
  does not compute one. Total uncompressed size is 8.1 GB.
- **Task**: none; whole-night sleep. The sleep-cassette participants "continued their normal
  activities but wore a modified Walkman-like cassette-tape recorder" at home; the sleep-telemetry
  participants were recorded in hospital under a temazepam-versus-placebo crossover.
- **Label type**: expert-scored hypnogram, "manually scored by well-trained technicians (identified
  by the eighth letter of the hypnogram filename)" per the 1968 Rechtschaffen and Kales manual.
  Stages W, R, 1, 2, 3, 4, M (movement time) and ? (not scored). Note that this is the
  Rechtschaffen and Kales scheme, not the American Academy of Sleep Medicine scheme that
  `adabrain-bench` states it uses for its sleep-staging tasks — a mapping is required and neither
  source states it here.
- **Licence**: Open Data Commons Attribution License v1.0. Access policy: "Anyone can access the
  files, as long as they conform to the terms of the specified license."
- **Access route**: open download, no registration. ZIP (8.1 GB), `wget -r -N -c -np
  https://physionet.org/files/sleep-edfx/1.0.0/`, or `aws s3 sync --no-sign-request
  s3://physionet-open/sleep-edfx/1.0.0/`.
- **Checkpoints pretrained on or evaluated against it**: evaluated by BIOT, EEGPT, LaBraM and
  CBraMod under `adabrain-bench` (balanced accuracy 64.95, 60.99, 68.94, 69.47 respectively in the
  cross-subject setting, against 69.55 for the best supervised model, ST-Tran — one of three
  datasets in that table where a supervised model takes the top spot on balanced accuracy, the
  others being Siena, where Conformer's 72.87 beats BIOT's 71.67, and HMC, where Conformer's 73.84
  beats LaBraM's 71.94. *Correction, made during review: an earlier version of this card called
  Sleep-EDF "the one dataset in that table where a supervised model takes the top spot on balanced
  accuracy". AdaBrain-Bench's Table 2 has three such rows, all in its clinical-monitoring group; the
  fourth member of that group, SHHS, goes to CBraMod at 73.51 against ST-Tran's 68.67.* Named as a
  pretraining source for BIOT indirectly via SHHS rather than Sleep-EDF itself. Sleep staging is
  among the task families in `omnieeg-bench`, `brain4fms` and `neuralbench`.

Other details:

- **Format**: polysomnograms in European Data Format; hypnograms in EDF+. "All EDF header fields also
  comply with the EDF+ specs, and unrecorded signals were removed from the ST*PSG.edf files."
- **File naming**: `SC4ssNEO-PSG.edf` for cassette and `ST7ssNJ0-PSG.edf` for telemetry, where ss is
  the subject number and N the night.
- **Version history**: a small subset contributed in 2002; expanded to 61 polysomnograms in 2013;
  expanded to 197 in March 2018. The PhysioNet page is dated "Published: Oct. 24, 2013. Version:
  1.0.0" while describing the 2018 expansion, so the version string does not track the content.
- **Citation requested**: Kemp, Zwinderman, Tuk, Kamphuisen and Oberyé (2000), *IEEE Transactions on
  Biomedical Engineering* 47(9):1185–1194, plus the standard PhysioNet citation.
- **Marker semantics** for the telemetry subset: "the physical marker dimension ID+M-E relates to the
  fact that pressing the marker (M) button generated two-second deflections from a baseline value
  that either identifies the telemetry unit (ID = 1 or 2 if positive) or marks an error (E) in the
  telemetry link if negative."

## Open questions / limitations

- **No participant count is stated on the landing page**, and the widely used figure of 78 comes from
  benchmark preparations rather than from the dataset itself. Two published numbers for "Sleep-EDF"
  may therefore refer to different subject sets, and the 153/44 file split does not map cleanly onto
  a subject count because most subjects contributed two nights and three nights were lost.
- **No total-hours figure and no per-recording durations**, only "about 20 hours" and "about 9 hours".
- **Two scoring schemes are in play across the literature.** The dataset is scored under
  Rechtschaffen and Kales with stages W, 1, 2, 3, 4, R, M; `adabrain-bench` reports its sleep-staging
  datasets as labelled "in accordance with the AASM standard: REM, N1, N2, N3, and Wake". Merging
  stages 3 and 4 into N3 and dropping movement time is the usual mapping, but neither source states
  it, so a five-class Sleep-EDF result and the dataset's own eight-label hypnogram are not the same
  label space.
- **Scored on non-standard derivations.** The hypnograms were produced from Fpz-Cz and Pz-Oz rather
  than the C4-A1/C3-A2 the Rechtschaffen and Kales manual specifies. The landing page cites a
  reference justifying this, but it means the labels are not strictly manual-conformant and a model
  learning them is learning a variant scoring.
- **The two subsets are not one population.** Sleep-cassette is healthy home recording aged 25 to
  101; sleep-telemetry is a hospital drug study in 22 people with mild insomnia. Pooling them, which
  is what a "197 recordings" figure implies, mixes a healthy-ageing cohort with a pharmacological
  crossover. No suite carded here states which subset it used.
- **The peripheral channels are present but unused by every checkpoint and suite in this corpus.**
  Whether they are usable as signal or only as artefact references is not addressed by the landing
  page, and belongs to the `candidate-datasets` strand's question rather than this one; recorded here
  only as an observation about benchmark practice.
- The PhysioNet page's version metadata is inconsistent with its own content history, as noted above.
- The primary reference (Kemp et al. 2000, IEEE TBME) is a study of slow-wave microcontinuity, not a
  data descriptor, and is paywalled. It was not retrieved; the landing page is the primary source
  for this card.

## Citations

Primary: `sleep-edf-expanded`

- `adabrain-bench` — reports all four of its checkpoints on this dataset and supplies the
  post-preprocessing counts quoted above.
- `edf-plus` — the format the hypnograms use and whose annotation mechanism carries the sleep stages.
- `physionet-mi` — the other PhysioNet dataset carded in this strand, under the same access policy
  and licence.
- Kemp B, Zwinderman AH, Tuk B, Kamphuisen HAC, Oberyé JJL (2000), *IEEE Trans. Biomed. Eng.*
  47(9):1185–1194 — the citation the landing page requests; paywalled and not retrieved.
- `neuralbench` — reports sleep staging as a task family close to saturation.
