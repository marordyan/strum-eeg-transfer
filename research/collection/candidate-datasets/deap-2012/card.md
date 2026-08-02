---
slug: deap-2012
type: dataset
strand: candidate-datasets
year: 2012
authors: [Koelstra, Mühl, Soleymani, Lee, Yazdani, Ebrahimi, Pun, Nijholt, Patras]
venue: IEEE Transactions on Affective Computing
doi: 10.1109/T-AFFC.2011.15
url: https://doi.org/10.1109/T-AFFC.2011.15
license: null
modalities: [scalp-eeg, eog, emg, electrodermal-activity, respiration, blood-volume-pulse, skin-temperature, face-video]
tags: [affect, peripheral-physiology, 32-channel, biosemi, 512-hz, self-report-labels, eula, thirteen-peripheral-channels, source-self-contradiction]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

DEAP is the reference point for "EEG plus peripheral physiology" in this literature — 32
participants, 32 research-grade EEG channels at 512 Hz and thirteen simultaneously recorded
peripheral channels — but the paper is internally inconsistent about whether electrocardiography is
among them, with two of its own methods passages naming an ECG channel and two enumerating the
peripheral set without one.

## Summary

A multimodal affect dataset in which "the electroencephalogram (EEG) and peripheral physiological
signals of 32 participants were recorded as each watched 40 one-minute long excerpts of music
videos". Participants rated each video on arousal, valence, like/dislike, dominance and
familiarity; frontal face video was additionally recorded for 22 of the 32. EEG was acquired "at a
sampling rate of 512 Hz using 32 active AgCl electrodes (placed according to the international
10-20 system)", and "thirteen peripheral physiological signals" were recorded alongside. The paper
also contributes a stimulus-selection method that used affective tags retrieved from last.fm,
video highlight detection, and an online assessment, so the 40 clips are not an arbitrary
selection. Baseline single-trial classification results are reported separately for EEG,
peripheral signals and multimedia content analysis, which makes DEAP one of the few datasets in
this strand whose original paper already separates the contribution of the peripheral modality
from that of the EEG.

## Relevance to the review

DEAP is the canonical instance of the design the project's third comparison needs: EEG and
peripheral physiology recorded synchronously in the same session, with a paper that reports what
each modality contributes on its own. Whatever the project ends up doing with STRUM, DEAP is the
dataset the field will read the third comparison against.

Its peripheral inventory is the richest of any entry in this strand — electrooculography,
electromyography, electrodermal activity, respiration, blood volume pulse and skin temperature —
and crucially those channels are treated as signal by the original authors, not as artefact
references. The EOG and EMG channels have a dual character worth noting: four electrodes for EOG
and four for EMG on zygomaticus major and trapezius, which are simultaneously the standard
artefact references for eye movement and jaw/neck tension and, in an affect paradigm, the
facial-expression measure of interest.

The limit for this project is that every label is a self-report rating thresholded into two
classes ("On the 9-point rating scales, the threshold was simply placed in the middle"), which is
a different label-provenance class from the stimulus-condition labels the project plans to use.

## Notable details

**Fixed field set:**

- **Participants**: 32. Frontal face video for the first 22 of them.
- **Simultaneous participants per recording**: 1.
- **Channels**: 32 EEG, "placed according to the international 10-20 system", plus thirteen
  peripheral physiological channels.
- **Sampling rate**: **512 Hz at acquisition, down-sampled to 256 Hz** in the paper's own
  processing. "EEG was recorded at a sampling rate of 512 Hz using 32 active AgCl electrodes
  (placed according to the international 10-20 system)"; and, of the peripheral set, "All the
  physiological responses were recorded at a 512Hz sampling rate and later down-sampled to 256Hz
  to reduce processing time." The EEG analysis pipeline likewise reports the data "average
  referenced, down-sampled to 256Hz, and high-pass filtered with a 2 Hz cutoff-frequency".

  **Corrected 2026-08-01, Phase 4 audit.** This field previously read "512 Hz for EEG (the widely
  distributed preprocessed version is downsampled to 128 Hz; the paper describes both the raw rate
  and the preprocessing)". The paper describes no such thing: **the string "128 Hz" does not occur
  anywhere in `source.md`**, and the only down-sampling rate the paper gives is 256 Hz, in the two
  passages quoted above. The 128 Hz figure is *unverified here* — it may well describe the
  distributed preprocessed `.dat` files, which are documented on the dataset website rather than in
  the paper, but that page was unreachable at retrieval time (see `meta.json`) and nothing in the
  archived record supports it. It is retained as an explicitly unverified note rather than deleted,
  and must not be presented as the paper's own figure in the comparison table.
- **Peripheral channels present**: uncontested are electrooculography (4 electrodes),
  electromyography (4 electrodes, zygomaticus major and trapezius), galvanic skin response,
  respiration, blood volume by plethysmograph, and skin temperature. Section 3 states "Thirteen
  peripheral physiological signals" were recorded. **Whether a distinct ECG channel is among them
  is contradicted within the paper and is recorded here unresolved**, with all four passages
  quoted; see Open questions.

  **Corrected 2026-08-01, Phase 4 audit.** The earlier version described the contradiction as
  holding between *two* passages and then resolved it against ECG, stating "this card does not
  assert that DEAP carries ECG". Both parts were wrong. There are four relevant passages, not two,
  and they split evenly, so the resolution was a coin-flip presented as a rule application. Under
  the standing rule for self-contradicting sources the card now records both readings and picks
  neither.
- **Total hours**: not reported as a total. 40 trials of one minute per participant for 32
  participants, i.e. on the order of 21 hours of trial data plus baselines by arithmetic from the
  reported design.
- **Task**: passive viewing of 40 one-minute music video excerpts, with a self-assessment after
  each.
- **Label type**: self-reported arousal, valence, like/dislike, dominance and familiarity on
  nine-point scales, thresholded at the midpoint into binary low/high classes for the baseline
  experiments.
- **Label source**: participant self-report. The authors state explicitly that "the participants'
  ratings during the experiment are used as the ground truth".
- **License**: not stated in the paper; distributed under a signed end-user licence agreement.
- **Access route**: registration plus a printed, signed and scanned end-user licence agreement
  uploaded through a request form, after which credentials are issued. The dataset host was
  returning HTTP 503 throughout retrieval (see `meta.json`).

**Other specifications:**

- **Derivation scheme**: not stated in the accessible text. The acquisition is a BioSemi
  ActiveTwo, whose native output is referenced to the CMS/DRL driven-right-leg loop and is
  conventionally re-referenced offline, but the paper does not describe the derivation of the
  distributed data, so it is recorded as unknown rather than assumed from the hardware. The one
  reference statement the paper does make — the EEG was "average referenced" — describes the
  authors' *own analysis* pipeline, alongside their down-sampling and 2 Hz high-pass, not the
  derivation of what is distributed. Noted here so a later reader who finds that line does not read
  it as settling the distributed data's reference.
- **Electrode layout**: international 10-20, 32 active AgCl electrodes.
- **Audio delivery**: stereo speakers at a "relatively loud" level, adjusted per participant for
  comfort — a per-participant stimulus variation that is not logged as a covariate.

## Open questions / limitations

- **The paper contradicts itself about ECG, and the contradiction is not resolvable from the paper.**
  Four passages bear on it, two each way, and the card picks neither.

  *For an ECG channel.* Section 6.1's enumeration: "The following peripheral nervous system signals
  were recorded: GSR, respiration amplitude, skin temperature, electrocardiogram, blood volume by
  plethysmograph, electromyograms of Zygomaticus and Trapezius muscles, and electrooculogram
  (EOG)." And the preprocessing description, which refers to the channels as shipped: "The trend of
  the ECG and GSR signals was removed by subtracting the temporal low frequency drift. The low
  frequency drift was computed by smoothing the signals on each ECG and GSR channels with a 256
  points moving average."

  *Against one.* The Fig. 3 caption, "Placement of peripheral physiological sensors", enumerates
  "[Four] Electrodes were used to record EOG and 4 for EMG (zygomaticus major and trapezius
  muscles). In addition, GSR, blood volume pressure (BVP), temperature and respiration were
  measured" — no cardiac electrode. And Table 5, the peripheral feature table, has rows for skin
  conductance, blood volume pressure, respiration pattern, skin temperature, and EMG/EOG, with no
  ECG row; its heart-rate and heart-rate-variability features sit under **blood volume pressure**,
  i.e. derived from the plethysmograph rather than from a cardiac electrode.

  This is not a pedantic distinction for this project: blood volume pulse and ECG support
  different heart-rate-variability measures, and the third comparison would be built on whichever
  one is actually there. Resolving it requires the distributed channel list, and the dataset page
  was unreachable at retrieval time — so this is a "reported but not accessible" case, and
  re-retrieval of the channel list would settle it.

  Note on the frontmatter: `modalities` does not list `ecg`. That reflects the unresolved state,
  not a finding of absence, and should not be read as the card asserting DEAP has no ECG.
- The "thirteen peripheral physiological signals" figure does not obviously reconcile with the
  eight signal *types* the paper enumerates; it is presumably a per-electrode count (four EOG plus
  four EMG plus GSR, respiration, plethysmograph, temperature is twelve). The card carries the
  paper's stated figure and flags that it could not be reconciled.
- Every label is a self-report, so DEAP cannot be used to test whether a stimulus-condition label
  supports a cognitive claim — it has no stimulus-condition labels. Its value to this strand is as
  a peripheral-physiology specification, not as a label-validity case.
- Thirty-two participants watching commercial music videos is a narrow generalisation base, and
  the stimulus set is selected for affective extremity by design, which makes the elicited states
  less like the sustained operational states a neuroergonomics dataset targets.
- The access route requires a signed licence agreement, which is a real friction for a project
  that wants to fine-tune on several datasets, and the host's availability at retrieval time was
  poor.

## Citations

Primary: `deap-2012`

- `amigos-2021` — the successor from an overlapping author group, adding a group-viewing social
  context and ECG but on a 14-channel consumer headset.
- Soleymani et al., MAHNOB-HCI, `10.1109/T-AFFC.2011.25` — the contemporaneous multimodal affect
  database with ECG, respiration and eye gaze; no open copy was obtainable, so it is not carded.
- `tes-eeg-ecg-2021` — a later EEG-plus-ECG release under CC BY with no licence agreement, and the
  contrast case for access route.
- `hinss-2023-passive-bci` — cites DEAP's 32 participants as one of the reference points for
  choosing its own sample size.
