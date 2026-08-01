---
slug: hinss-2023-passive-bci
type: dataset
strand: candidate-datasets
year: 2023
authors: [Hinss, Jahanpour, Somon, Pluchon, Dehais, Roy]
venue: Scientific Data
doi: 10.1038/s41597-022-01898-y
url: https://doi.org/10.1038/s41597-022-01898-y
license: CC BY 4.0 (article)
modalities: [scalp-eeg, ecg]
tags: [cog-bci, passive-bci, matb-ii, n-back, pvt, flanker, multi-session, per-session-electrode-scan, fpz-reference, ecg-on-tp9, bids, zenodo, lsl-triggers]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

COG-BCI: 29 participants, three sessions a week apart, four cognitive tasks including the
aviation-style MATB-II, over 100 hours of open BIDS-formatted EEG with one channel sacrificed for
electrocardiography — and it validates its task-difficulty labels against subjective scales,
behavioural performance *and* physiology rather than assuming them.

## Summary

The COG-BCI database was built because "data sharing in pBCI research is still scarce". Twenty-nine
participants (11 female, 18 male, mean age 23.9, SD 3.20) completed three sessions spaced one week
apart, performing four tasks in each: the N-back (N = 0, 1, 2), the MATB-II in which "participants
have to simultaneously perform four aviation-related subtasks", the Psychomotor Vigilance Task, and
the arrow-based Eriksen flanker task. Each session opened with a 3D head-and-cap scan, task
training, a Karolinska Sleepiness Scale rating and a two-minute resting state (one minute eyes
open, one closed); every task was presented twice in pseudorandom order and "followed systematically
by a Rating Scale Mental Effort", with an extra Karolinska rating after the vigilance task and
another resting state and rating at the end. Tasks took 65 to 80 minutes per session depending on
breaks. Acquisition used 64 active Ag-AgCl electrodes (ActiCap) on an ActiCHamp amplifier at
standard 10-20 positions, referenced at Fpz, sampled at 500 Hz with 24-bit digitisation and
0.05 µV resolution, no filtering during acquisition, impedances started below 25 kΩ, and one
electrode — TP9 — "was sacrificed to record peripheral ECG". Data are released raw, in BIDS, on
Zenodo, with a notebook giving task order and interruptions and a trigger list mapping all Lab
Streaming Layer triggers.

## Relevance to the review

Of everything read in this strand, this is the dataset that most closely matches what STRUM is
described as being: a battery of operationally flavoured tasks, passive-BCI framing, multi-session,
with cognitive-state labels defined by the experimental design. It is the natural comparator, and
because it is fully open it is also the natural stand-in if STRUM proves unobtainable.

Three specifications make it a strong candidate independently of that. First, the label validation.
The paper is explicit that "as the ground truth about the task difficulty is known by the
experimenter, the results of the classification can then be evaluated in terms of their accuracy",
and it then goes further than most datasets by validating "on a subjective, behavioral and
physiological level". Subjective via the Karolinska Sleepiness Scale and the Rating Scale Mental
Effort; behavioural via accuracies and reaction times per task; physiological via cardiac and
cerebral activity. That is agreement between three label sources on the same trials, which is
exactly the property category 3 of this strand asks about and which almost nothing else in the
strand has.

Second, the electrode positions are measured per participant *per session* with a Structure 3D
scanning camera and the `get_chanlocs` pipeline, rather than assumed from a template. For a
coordinate-based checkpoint of the kind the `eeg-models` strand carded, this is the difference
between real coordinates and inferred ones — and it is measured three times per participant, so
between-session electrode displacement is quantifiable rather than a hidden nuisance.

Third, the derivation is referential at Fpz, with a named per-channel layout. No bipolar
approximation is required to feed it to a layout-flexible model.

## Notable details

**Fixed field set:**

- **Participants**: 29 in the final dataset (11 female, 18 male; mean age 23.9, SD 3.20; 2
  left-handed by the Edinburgh Handedness scale; 25 students, 4 employees). 35 were recruited;
  6 lost to dropout and technical issues. Sample size was chosen against reference points the paper
  names: about 15 participants typical in the passive-BCI literature, about 20 in cognitive science,
  SEED at 15 and DEAP at 32.
- **Simultaneous participants per recording**: 1.
- **Channels**: 64 active Ag-AgCl electrodes (ActiCap, Brain Products) on an ActiCHamp amplifier,
  of which one (TP9) is used for ECG — so 63 EEG plus 1 ECG. For participants 1–9 the electrode Cz
  was not recorded.
- **Sampling rate**: 500 Hz, 24-bit, 0.05 µV resolution, no acquisition filtering.
- **Peripheral channels present**: one ECG channel, placed on the left fifth intercostal space,
  usable as signal — the paper uses cardiac activity in its own validation. No EOG, no respiration,
  no electrodermal activity.
- **Total hours**: "over 100 hours of open EEG data", stated by the authors. Per session, tasks took
  65 to 80 minutes plus setup, training and resting states.
- **Task**: four tasks per session — MATB-II (four simultaneous aviation subtasks), N-back at
  N = 0, 1, 2, Psychomotor Vigilance Task (10 minutes), Eriksen flanker with congruent and
  incongruent trials and trial-level feedback. Plus resting states, eyes open and eyes closed.
- **Label type**: task identity and task difficulty level, set by the experimenter; subjective
  sleepiness (Karolinska, 9-point, "1 extremely alert" to "9 extremely sleepy - fighting sleep") and
  subjective mental effort (Rating Scale Mental Effort); behavioural accuracy and reaction time per
  task.
- **Label source**: experimental design, self-report, and behavioural performance, all three
  present on the same recordings. The paper additionally uses physiological measures (cardiac and
  cerebral) as a fourth validation channel.
- **License**: article CC BY 4.0; data licence recorded separately in `meta.json`.
- **Access route**: open download from Zenodo, no registration and no agreement described.

**Other specifications:**

- **Derivation scheme**: referential, reference at Fpz. The paper's own preprocessing example then
  applies "a full-rank average referencing" before independent component analysis, but the
  distributed data are raw and referenced at Fpz.
- **Electrode layout**: extended 10-20, with per-participant per-session 3D positions captured by a
  Structure scanning camera using the `get_chanlocs` procedure. This is unusual and directly
  valuable for coordinate-based models.
- **Format**: raw data in BIDS on Zenodo, with a notebook file recording task order and any
  recording interruptions, and a trigger list file enumerating all Lab Streaming Layer triggers and
  what they refer to. Naming distinguishes resting states as eyes-closed and eyes-open, at session
  start and session end.
- **Reference preprocessing the authors describe**: interpolation of channels whose noise exceeds
  two standard deviations of the others, full-rank average re-referencing, then independent
  component analysis with ICLabel rejection of eye, muscle and heart components above 90 %
  confidence.
- **Validation findings reported**: sleepiness and performance decrement assessed by the Karolinska
  and Rating Scale Mental Effort scales; behavioural accuracy and reaction time per task; and the
  expected vigilance decrement over the 10-minute Psychomotor Vigilance Task was observed.

## Open questions / limitations

- Single-participant recordings throughout. Nothing in this dataset speaks to the dyadic or team
  structure the project's research question is about.
- No language-stimulus manipulation of any kind. This dataset cannot support a spoken-versus-written
  label, so its value as a STRUM comparator is on task structure, label validation and acquisition
  quality, not on the specific contrast the project plans.
- One ECG channel bought at the cost of one EEG channel (TP9). That is a real trade: the electrode
  is missing from the scalp layout, which matters for any model that expects a symmetric montage or
  that interpolates across the temporal chain.
- Cz is missing for participants 1 through 9, so nine of twenty-nine participants have a different
  channel set from the rest. A pipeline that assumes a fixed channel order across subjects will
  break or, worse, silently misalign.
- The card's peripheral inventory is thinner than the project's target: ECG only, no EOG and no
  respiration. Ocular artefact removal in the authors' own pipeline relies on independent component
  analysis rather than on recorded EOG.
- The paper reports "over 100 hours" without a per-task or per-session breakdown in the read text,
  so the amount of data per label class cannot be stated from this card.
- Three sessions a week apart is a genuine cross-session design, which is the dataset's headline
  feature, but 29 participants across 3 sessions is still a small subject pool for anything
  claiming subject-general transfer.

## Citations

Primary: `hinss-2023-passive-bci`

- `strum-2018` — the dataset this one is the closest open comparator to; both are passive-BCI task
  batteries with experimenter-defined state labels.
- `kothe-2023-nback-nirs` — the n-back workload label without the subjective and behavioural
  validation this dataset supplies.
- `eeg-bids-2019` — the format the Zenodo release conforms to.
- `lsl-2024` — the synchronisation framework whose triggers this dataset distributes as an explicit
  trigger list.
- `deap-2012` — cited by this paper's authors as one of the sample-size reference points for
  choosing 29 participants.
