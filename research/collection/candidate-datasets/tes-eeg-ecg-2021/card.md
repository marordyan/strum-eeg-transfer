---
slug: tes-eeg-ecg-2021
type: dataset
strand: candidate-datasets
year: 2021
authors: [Gebodh, Esmaeilpour, Datta, Bikson]
venue: Scientific Data
doi: 10.1038/s41597-021-01046-y
url: https://doi.org/10.1038/s41597-021-01046-y
license: CC BY 4.0
modalities: [scalp-eeg, ecg, eog, behavioral-tracking, transcranial-electrical-stimulation]
tags: [eeg-ecg-eog, 32-channel, 2khz, cpz-reference, bids, openneuro, zenodo, cc-by, vigilance, continuous-behavioral-label]
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

Twenty participants, 62 sessions of about seventy minutes each, with 32-channel EEG at 2 kHz
recorded concurrently with bipolar lead-I electrocardiography, bipolar horizontal
electrooculography and a millisecond-resolution continuous behavioural vigilance score — released
under CC BY 4.0 in Brain Imaging Data Structure form with no licence agreement.

## Summary

The dataset ("GX") combines high-definition transcranial electrical stimulation with concurrent
multimodal recording. Twenty neurologically typical adults (7 female, 13 male, aged 19–43, median
30) performed a compensatory tracking task continuously for the whole session while receiving
nine stimulation types — three cortical targets (frontal, motor, parietal) crossed with three
waveforms (direct current, 5 Hz, 30 Hz). Experiment 1 gave each participant three 70-minute
sessions with three stimulation types each and four trials per type; Experiment 2 gave two
70.5-minute sessions with 20 trials of a single type. In total "more than 783 total stimulation
trials over 62 sessions". EEG used a 32-channel wired Waveguard cap with 29 interleaved
stimulation electrode holders, sampled at 2 kHz, referenced to CPz and grounded at AFz on an ANT
Neuro eego sport amplifier, amplifier bandwidth 0–520 Hz, impedances kept below 20 kΩ.
Physiological monitoring used bipolar snap electrodes for lead-I ECG (below each clavicle, ground
at the left hip) and horizontal EOG (outer canthi). Behaviour was the tracking-task deviation
score, sampled continuously. Four participants repeated Experiment 2 for within-participant
reliability.

## Relevance to the review

For the project's third comparison — does adding peripheral physiology on top of an EEG embedding
help — this is the cleanest specimen in the strand. The peripheral channels are unambiguously
recorded as signal rather than as artefact references: the authors' stated purpose includes
testing "how variations in brain state (e.g. baseline vigilance) or physiology impact sensitivity
to tES", so the ECG is an independent variable in their own analysis. The acquisition is
research-grade and fully specified: reference electrode named, ground named, bandwidth named,
impedance criterion named, sampling rate named per modality.

The label is also a different kind from anything else here. The compensatory tracking task
"allowed for the assessment of vigilance/attention on the scale of milliseconds, facilitating its
acquisition concurrency with dynamic EEG, ECG, and EOG", so the label is a continuous behavioural
measurement rather than a categorical stimulus condition or a post-hoc rating. That places it
outside the circularity trap this strand worries about, at the cost of not being a discrete
classification target.

The confound to record is that stimulation is present throughout. Every session contains
stimulation artefacts in the EEG which the paper itself notes "produces large voltage artifacts in
the EEG during ramp-up and ramp-down", so any use of this data for pretraining or fine-tuning has
to decide what to do with stimulation periods.

## Notable details

**Fixed field set:**

- **Participants**: 20 recruited (7 female, 13 male, aged 19–43, median 30, mean 29.10 ± 6.75).
  One (participant 17) was excluded for inability to follow task instructions. Four (12, 15, 21,
  22) returned to repeat Experiment 2, and returning participants were given new identifiers.
- **Simultaneous participants per recording**: 1.
- **Channels**: 32 EEG (wired Waveguard cap, ANT Neuro), at standard 10/10 positions, plus 2 ECG
  and 2 EOG bipolar snap electrodes and 9 stimulation electrodes in interleaved holders.
- **Sampling rate**: 2 kHz for EEG; ECG and EOG acquired concurrently on the same amplifier;
  behavioural tracking deviation continuous at millisecond scale.
- **Peripheral channels present**: lead-I electrocardiography (bipolar, chest, ground at left hip)
  and horizontal electrooculography (bipolar, outer canthi). Both usable as signal. No
  respiration, no electrodermal activity.
- **Total hours**: not reported as a total. 62 sessions of 70 or 70.5 minutes each, i.e. roughly
  72 hours by arithmetic from the reported session count and duration.
- **Task**: a verified compensatory tracking task performed continuously for the whole session,
  under nine high-definition transcranial electrical stimulation conditions in a repeated-measures
  crossover design.
- **Label type**: continuous behavioural vigilance/alertness score (deviation from the centre of
  an annulus), plus the stimulation condition applied per trial, plus pre- and post-session
  self-reported wellness questionnaires and demographics.
- **Label source**: behavioural performance (the tracking deviation), experimental design (the
  stimulation condition), and self-report (the wellness scales). Three distinct provenances in one
  dataset.
- **License**: CC BY 4.0. The authors state the data are "provided without restriction under the
  Creative Commons with Attribution 4.0 license".
- **Access route**: open download, no registration. Raw `.cnt` at Zenodo
  (10.5281/zenodo.3837212); BIDS-formatted at OpenNeuro `ds003670` v1.1.0
  (10.18112/openneuro.ds003670.v1.1.0); derived per-trial figures at figshare.

**Other specifications:**

- **Derivation scheme**: referential, online reference at CPz, ground at AFz. Named explicitly,
  which is unusual among the datasets in this strand and makes the ingestion question for a
  layout-flexible checkpoint straightforward: each channel is a potential at a named 10/10 site.
- **Formats**: `.cnt` (raw), BIDS (OpenNeuro), `.mat` (derived time series, MATLAB- and
  Python-readable).
- **Stimulation electrode montages**: frontal — surround AF3, FT7, FC3 with centre F5; motor —
  surround FT7, FC3, CP3, TP7 with centre C5; parietal — surround C5, C1, P1, TP7 with centre CP3.
  A single nine-position setup was prepared for all experiments, with ring/centre assignment
  varied.

## Open questions / limitations

- Transcranial electrical stimulation is applied in every session. This is the point of the
  dataset and simultaneously the reason it is not a clean substrate for representation learning:
  the EEG contains stimulation artefacts by construction, and the paper reports removing DC
  artefacts and large ramp transients only for display purposes.
- One task, one behavioural measure. There is no categorical cognitive-state label and no
  stimulus-modality manipulation, so nothing in this dataset speaks to the spoken-versus-written
  label question.
- The two-kilohertz sampling rate and 32 channels over 70-minute continuous sessions make single
  sessions large. The memory constraint recorded in the project's `CLAUDE.md` — that one subject's
  full recording exhausts a Jupyter kernel — applies here with force; sessions must be read lazily
  and epoched before loading.
- Participant identifiers are not stable across repeats: a participant who returned appears under
  a new number (the paper notes one participant appears as 22, 23 and 24 across three runs). A
  subject-wise split built naively on the identifier column would leak.
- The ECG is a single lead. It supports heart rate and heart-rate variability but not the
  morphological analyses a multi-lead recording would.

## Citations

Primary: `tes-eeg-ecg-2021`

- `eeg-bids-2019` — the specification the OpenNeuro copy of this dataset conforms to.
- `openneuro-2021` — the platform hosting the BIDS copy, `ds003670`.
- `deap-2012` — the older EEG-plus-peripheral reference point, with more peripheral modalities but
  self-report labels and a licence agreement.
- `hinss-2023-passive-bci` — the other open, research-grade, BIDS-formatted EEG dataset in this
  strand with a peripheral cardiac channel.
