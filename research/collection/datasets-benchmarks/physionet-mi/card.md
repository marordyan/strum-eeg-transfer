---
slug: physionet-mi
type: dataset
strand: datasets-benchmarks
year: 2009
authors: [Schalk]
venue: PhysioNet (EEG Motor Movement/Imagery Dataset v1.0.0)
doi: 10.13026/C28G6P
url: https://physionet.org/content/eegmmidb/1.0.0/
license: Open Data Commons Attribution License v1.0
modalities: [scalp-eeg, motor-imagery, motor-execution, 10-10-montage, 64-channel]
tags: [benchmark-dataset, pretraining-corpus, motor-imagery, open-data-commons, edf-plus, stimulus-markers, bci2000, checkpoint-mapping, largest-open-motor-imagery]
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

64-channel motor imagery and execution from 109 participants at 160 Hz, in EDF+ with annotation
channels, under an Open Data Commons Attribution licence and no registration — the benchmark on which
REVE reports the cleanest pretraining ablation in the whole corpus, +10.7 balanced-accuracy points
for the same architecture with versus without pretraining.

## Summary

The EEG Motor Movement/Imagery Dataset was contributed to PhysioNet by the developers of the BCI2000
instrumentation system. Each participant completed 14 experimental runs: two one-minute baseline
recordings with eyes open and eyes closed, then three repetitions each of four two-minute task
conditions. The conditions pair execution against imagery and unilateral against bilateral movement:
opening and closing the left or right fist in response to a left or right visual target, and opening
and closing both fists or both feet in response to a top or bottom target, each condition run both
as actual movement and as imagined movement. Signals were recorded according to the international
10-10 electrode placement system at 160 Hz and are provided in EDF+ with accompanying annotation
channels. Event labels use three codes: T0 for rest, T1 for left-fist or both-fists movement or
imagery depending on the run type, and T2 for right-fist or both-feet movement or imagery.

## Relevance to the review

This dataset carries the single most useful number in the strand for separating this project's first
comparison from its second. `reve-2025` reports REVE-Base at 0.6480 balanced accuracy on the
four-class PhysioNet-MI task with pretraining against 0.5409 for the identical architecture trained
from scratch — a 10.7-point gain attributable to pretraining rather than to architecture. In the
same table CBraMod gains about 2 points from its pretraining, and without pretraining CBraMod beats
REVE by roughly 8 points. That is the shape of evidence this project's comparisons 1 and 2 are meant
to produce, on a dataset where someone has already produced it.

It is also the benchmark where frozen features are most starkly worse than fine-tuned ones:
REVE-Base under a frozen backbone reaches 0.5371 against 0.3845 for CBraMod, 0.3715 for LaBraM and
0.3698 for BIOT — all four far below their fine-tuned scores. A project intending to attach
peripheral-physiology features to a frozen EEG embedding, which is this project's third comparison,
should note that the frozen regime on a four-class motor task costs roughly 11 points relative to
fine-tuning even for the model designed for it.

Two structural properties make it a good reference point beyond the numbers. The labels come from
stimulus markers stored in EDF+ annotation channels, which is the same label provenance this project
plans to use, and the annotation mechanism is the one described in `edf-plus`. And it is one of the
few standard benchmarks that is genuinely open — Open Data Commons Attribution, no registration,
direct S3 access — which makes it usable as a pipeline smoke test before STRUM data is touched.

## Notable details

Fixed field set required of every `type: dataset` card in this strand:

- **Participants**: 109. The landing page's prose does not state a count; the file manifest lists
  subject folders S001 through S109. `adabrain-bench` and `moabb` both record 109.
- **Channels**: 64, "according to the international 10-10 electrode placement system". The
  distribution includes an electrode-position figure, `64_channel_sharbrough.pdf`.
- **Sampling rate**: 160 Hz.
- **Total hours**: not stated. Each participant contributes two one-minute baselines plus twelve
  two-minute runs, so roughly 26 minutes of task and baseline per participant before overhead, but
  the page gives no total and this card does not compute one. Total uncompressed size 3.4 GB, ZIP
  1.9 GB.
- **Task**: motor execution and motor imagery, cued by visual targets. Four two-minute conditions,
  three repetitions each, plus two one-minute eyes-open and eyes-closed baselines. Conditions:
  execute or imagine unilateral fist movement to a left or right target; execute or imagine bilateral
  fist or foot movement to a top or bottom target.
- **Label type**: stimulus-condition labels from event markers stored in the EDF+ annotation channel.
  Three codes: T0 rest, T1 left fist or both fists, T2 right fist or both feet, with the referent of
  T1 and T2 depending on the run type. Note the consequence: the label is not self-contained per
  annotation; it must be resolved against which run the segment came from.
- **Licence**: Open Data Commons Attribution License v1.0. "Anyone can access the files, as long as
  they conform to the terms of the specified license."
- **Access route**: open download, no registration. ZIP, `wget -r -N -c -np
  https://physionet.org/files/eegmmidb/1.0.0/`, or `aws s3 sync --no-sign-request
  s3://physionet-open/eegmmidb/1.0.0/`.
- **Checkpoints pretrained on or evaluated against it**:
  *Pretrained on it* — EEGPT, whose pretraining set is PhysioNet-MI, HGD, TSU, SEED and M3CV per
  `adabrain-bench` Table 7. REVE draws 22,707 hours from PhysioNet overall, though the paper does not
  break out this dataset specifically.
  *Evaluated on it* — REVE (0.6480 fine-tuned four-class balanced accuracy, 0.5409 from scratch,
  0.5371 frozen), CBraMod (0.6417 with pretraining, 0.6196 without, 0.3845 frozen), LaBraM (0.3715
  frozen), BIOT (0.3698 frozen), all per `reve-2025`; it is a few-shot task family in
  `omnieeg-bench` where "several models like BrainOmni defy this saturation trend"; it is the largest
  dataset in `moabb`'s twelve at 109 subjects, 40 to 60 trials, one session, 64 channels, 1–3 s
  epochs; and it appears in `brain4fms` as EEGMMIDB, where BrainOmni performs strongly.

Other details:

- **Format**: EDF+, one file per run per subject, with an annotation channel.
- **Citation requested**: Schalk G. (2009), *EEG Motor Movement/Imagery Dataset* (version 1.0.0),
  PhysioNet, RRID:SCR_007345, doi 10.13026/C28G6P; plus the original publication, Schalk,
  McFarland, Hinterberger, Birbaumer and Wolpaw (2004), "BCI2000: A General-Purpose Brain-Computer
  Interface (BCI) System", *IEEE Transactions on Biomedical Engineering* 51(6):1034–1043; plus the
  standard PhysioNet citation.
- Published 9 September 2009, version 1.0.0, with no later version.
- The dataset was "developed to support research on brain-computer interfaces, motor execution, and
  motor imagery"; the page frames its value as covering both actual and imagined movement in the same
  participants.

## Open questions / limitations

- **The participant count is inferred from the file manifest, not stated in prose.** S001 through
  S109 are listed under Files; the abstract and background sections never give a number. Widely
  cited as 109, and consistent with `moabb`'s table, but the landing page does not assert it.
- **No total-hours figure and no per-run durations beyond "one-minute" and "two-minute".**
- **Known data-quality problems are not mentioned on the landing page.** It is well established in
  the BCI literature that several subjects in this dataset have anomalous run timings or sampling
  rates and are routinely excluded; the page carries no errata and no exclusion list. Any figure
  computed over "109 subjects" and any figure computed over the usual excluded subset are different
  quantities, and no source read here states which was used. `moabb` records 109 subjects with no
  exclusions.
- **Trial counts vary.** `moabb` records "40–60" trials per subject, without stating the source of
  the variation. `adabrain-bench` does not include this dataset. So the per-subject sample size is
  not fixed and is not documented on the landing page.
- **The T1/T2 label semantics are run-dependent**, which is a documented trap: the same annotation
  code means left fist in one run type and both fists in another. A pipeline that reads annotations
  without also reading the run index will silently mislabel half the data. The page states this
  clearly, which is more than most; it is recorded here because it is exactly the kind of
  stimulus-marker resolution step this project will have to implement for STRUM.
- **`moabb` uses only the two-class left-versus-right subset**; `reve-2025` reports four-class. A
  PhysioNet-MI number is uninterpretable without the class count, and chance differs accordingly
  (50% versus 25%).
- **EEGPT was pretrained on this dataset and is then evaluated on motor imagery benchmarks** in
  `adabrain-bench`, though not on PhysioNet-MI itself in that suite's table. The overlap is worth
  tracking wherever an EEGPT motor-imagery number appears.
- The primary citation (Schalk et al. 2004) is a paper about the BCI2000 software system, not a data
  descriptor for this dataset. It is paywalled and was not retrieved; the landing page is the primary
  source for this card.

## Citations

Primary: `physionet-mi`

- `reve-2025` (strand `eeg-models`) — the source of the pretraining ablation and the frozen-feature
  numbers quoted above.
- `moabb` — includes this dataset as its largest, with within-session 5-fold cross-validation and
  ROC-AUC.
- `edf-plus` — the format and the annotation mechanism the stimulus markers are stored in.
- `sleep-edf-expanded` — the other PhysioNet dataset carded here, same access policy and licence.
- Schalk G, McFarland DJ, Hinterberger T, Birbaumer N, Wolpaw JR (2004), *IEEE Trans. Biomed. Eng.*
  51(6):1034–1043 — the BCI2000 system paper the landing page asks users to cite; paywalled and not
  retrieved.
