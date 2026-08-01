---
slug: amigos-2021
type: dataset
strand: candidate-datasets
year: 2021
authors: [Miranda-Correa, Abadi, Sebe, Patras]
venue: IEEE Transactions on Affective Computing
doi: 10.1109/TAFFC.2018.2884461
url: https://doi.org/10.1109/TAFFC.2018.2884461
license: null
modalities: [scalp-eeg, ecg, electrodermal-activity, rgb-video, depth-video]
tags: [group-recording, four-simultaneous-viewers, emotiv-epoc, consumer-eeg, 14-channel, self-report-labels, external-annotation, personality, eula]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

AMIGOS recorded EEG, electrocardiography and electrodermal activity from four people watching
long videos together at the same time — the only screen-paradigm dataset found in this strand
with genuinely simultaneous multi-person physiological recording — but it does so on a
14-channel consumer headset with entirely self-report labels.

## Summary

An affective-computing dataset built around two experiments and two social contexts. In the short
videos experiment, 40 participants each watched 16 emotional video clips alone. In the long videos
experiment, participants watched four longer videos, some alone and some in groups: the paper's
participant table lists 17 individual participants and five groups of four (Group1 through
Group5, 20 participants), with group members' identifiers listed "in the order in which
participants were seated, from a front view, from left to right". Three physiological modalities
were recorded with wearable sensors: EEG on an Emotiv EPOC headset (14 channels, 128 Hz, 14-bit),
electrocardiography on a Shimmer 2R platform with an ECG module (256 Hz, 12-bit, three
electrodes), and electrodermal activity on a Shimmer 2R with a galvanic skin response module.
Frontal HD video plus RGB and depth full-body video were also recorded. Affect was annotated both
internally, by participant self-assessment of valence, arousal, dominance, liking, familiarity and
basic emotions, and externally, by annotators scoring twenty-second segments. Personality
(Big Five) and mood (PANAS) questionnaires were collected after the long videos experiment.

## Relevance to the review

This is the third multi-person entry in category 1 and the only one where more than two people
were instrumented at once. Four participants in a group all wore EEG, ECG and GSR sensors
simultaneously, driven from a single PC that both "present[ed] the stimuli" and "get[s] and
synchronize[s] signals". That makes it a specification of what a four-way simultaneous
physiological recording looks like in practice, which is the concrete thing category 1 is short of.

Its specification is also a useful contrast on peripheral modality. Unlike `boa-actors-2025` and
`livewire-2024`, which carry EOG and autonomic wristband channels but no cardiac signal, AMIGOS
carries a proper three-electrode ECG at 256 Hz that the authors describe as allowing "precise
identification of heart beats as well as the full ECG QRS complex". That is the kind of peripheral
channel the project's third comparison would need — usable as signal, not recorded for artefact
rejection.

The cost is at the other end. Fourteen consumer-grade channels at 128 Hz is a thin electrode
layout by the standards of the checkpoints in the `eeg-models` strand, and every label is
subjective rather than stimulus-defined.

## Notable details

**Fixed field set:**

- **Participants**: 40 in the short videos experiment. In the long videos experiment, 17 in the
  individual setting and 20 in the group setting (five groups of four).
- **Simultaneous participants per recording**: 4 in the group setting; 1 in the individual
  setting and in the whole short videos experiment.
- **Channels**: 14 EEG. Named in the paper as AF3, F7, F3, FC5, T7, P7, O1, O2, P8, T8, FC6, F4,
  F8, AF4, "according to the 10-20 system". Plus 3 ECG electrodes and a GSR module.
- **Sampling rate**: EEG 128 Hz at 14-bit resolution; ECG 256 Hz at 12-bit; GSR sampled by the
  Shimmer platform (rate not stated in the extracted text).
- **Peripheral channels present**: electrocardiography and galvanic skin response, both usable as
  signal — the paper's own framing is that EEG, ECG and GSR "have shown good performance in affect
  estimation studies". No EOG, no respiration.
- **Total hours**: not reported. Sixteen short videos per participant for 40 participants, plus
  four long videos across 37 participants in the long videos experiment.
- **Task**: passive viewing of emotional video clips, alone or as part of an audience of four,
  with self-assessment between trials.
- **Label type**: self-reported affect (arousal, valence, dominance, liking, familiarity, and
  selection of basic emotions from Neutral, Disgust, Happiness, Surprise, Anger, Fear, Sadness),
  externally annotated valence and arousal per twenty-second segment, personality traits, mood,
  and the social context itself (individual versus group).
- **Label source**: participant self-report, external human annotation, and standardised
  questionnaires (Big Five personality, PANAS mood). The social-context label is the only one
  defined by the experimental design rather than by a rating.
- **License**: not stated in the paper. Access is by end-user licence agreement (see
  `meta.json`).
- **Access route**: registration and signed end-user licence agreement, then download. The
  project page at eecs.qmul.ac.uk was returning HTTP 503 at retrieval time.

**Other specifications:**

- **Derivation scheme**: not stated in the accessible text. The Emotiv EPOC uses a fixed
  proprietary reference pair (CMS/DRL at P3/P4 in the standard configuration), but the paper does
  not describe the derivation, so this is recorded as unknown rather than assumed from the
  hardware.
- **Synchronisation**: a single PC (Intel Core i7, 3.4 GHz) both presented the stimuli and
  "get[s] and synchronize[s] signals". Shimmer sensors connected over Bluetooth; the Emotiv
  headset over a proprietary wireless standard. No measured synchronisation error is reported, and
  none is reported for the four participants in a group relative to one another.
- **Social-context effect the authors themselves tested**: they compared self-assessments between
  the individual set (17 participants) and the group set (20 participants) and report that "the
  difference of distribution of ratings, for each of the seven dimensions of personality and
  PANAS, between the participants of individual and group settings, is not significant (p > 0.1
  according to a two sample t-test for every dimension)".

## Open questions / limitations

- The self-reported form was administered on paper in the long videos experiment because "having
  a digital form for every participant of the groups was not practical". The authors state they
  used paper in both settings to keep the assessment consistent, but the format difference from
  the short videos experiment's digital form remains.
- No cross-participant synchronisation precision is reported for the group recordings, so the
  four simultaneous streams cannot be relied on for millisecond-level inter-participant analysis
  without independent verification.
- Fourteen channels at 128 Hz on a consumer headset is a hard constraint on what a pretrained
  checkpoint can do with this data. Several models in the `eeg-models` strand expect 200 Hz or
  higher input and were pretrained on much denser layouts; ingesting AMIGOS would require
  upsampling and would leave most of the model's spatial capacity unused.
- Every label except social context is a rating, so the circularity question this strand cares
  about takes a different form here: the risk is not that the label leaks into the signal, it is
  that the label may not correspond to any state the signal contains.
- Publication year is ambiguous across indexes: Crossref and IEEE date the issue to 2021,
  Semantic Scholar reports 2017, and the arXiv preprint used for the extraction is from 2017. The
  card uses the Crossref publication year, 2021, and the bib entry records the discrepancy.

## Citations

Primary: `amigos-2021`

- `deap-2012` — the direct predecessor from an overlapping author group, individual-viewing only,
  with a denser research-grade EEG montage and more peripheral channels.
- Soleymani et al., MAHNOB-HCI, `10.1109/T-AFFC.2011.25` — the other multimodal affect database
  AMIGOS positions itself against; no open copy was obtainable, so it is not carded here.
- `boa-actors-2025` and `livewire-2024` — the other multi-person entries in this strand, both
  naturalistic tasks rather than screen paradigms.
- `tes-eeg-ecg-2021` — the other EEG-plus-ECG dataset carded here, research-grade and
  open-licensed but single-participant.
