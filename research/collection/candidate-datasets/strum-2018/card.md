---
slug: strum-2018
type: dataset
strand: candidate-datasets
year: 2018
authors: [Kothe, Mullen, Makeig]
venue: 2018 IEEE International Conference on Systems, Man, and Cybernetics (SMC)
doi: 10.1109/SMC.2018.00023
url: https://ieeexplore.ieee.org/document/8616018/
license: null
modalities: [scalp-eeg, ecg, eog, resp, emg, eye-tracking, motion-capture]
tags: [strum, neuroergonomics, passive-bci, task-battery, dyadic, high-density-eeg, 206-channel, biosemi, xdf, lab-streaming-layer, hed-annotations, factorial-modality-by-kind, paywalled, access-by-request, two-citations, project-target-dataset]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

STRUM is 56 participants recorded as 28 simultaneous pairs, each wearing a 206-channel BioSemi EEG
montage plus 2-channel ECG, 2-channel EOG, a 16-channel respiration belt and a 43-channel EMG
neckband on the same amplifier at 512 Hz, synchronized with Lab Streaming Layer into one XDF file per
session; its side tasks form a 2x2 of stimulus modality (auditory/visual) by stimulus kind
(verbal/non-verbal), which means the project's spoken-versus-written label is one cell of a factorial
design whose other cells are the control for the sensory confound that would otherwise invalidate it.

## Summary

STRUM is presented by its authors as "a task battery modeled after a complex real-world
scenario, together with a new open dataset for BCI research". The stated motivation is that
brain-computer interface applications have expanded from clinical use into "entertainment,
automotive, workplace, and military domains" but have "yet to pass the prototype stage", and
that testing this requires "sufficiently realistic and rich datasets that allow for benchmarking
competing approaches". The paper reports "an exemplary analysis of a slice of this large trove
of data" and concludes that "the data mirror some of the challenges encountered in real-world
deployments, with various well-known BCI algorithms showing a pronounced performance
differential to highly simplified lab experiments", plus "significant performance differences
among alternative methods".

The paper remains closed to redistribution: Unpaywall reports `oa_status: closed` with zero
open-access locations and `has_repository_copy: false`, and the author-side pages named in the strand
brief (Swartz Center for Computational Neuroscience, Intheon) do not host a copy. It is readable
here only through UCSD institutional access, so the full text informs this card while the PDF stays
uncommitted.

The name is an acronym the abstract does not expand: **Small Team Reconnaissance Urban Missions**.
Section III supplies the full recording specification, given below.

## Relevance to the review

STRUM is the dataset the project proposes to fine-tune on, so its specification determines whether
the checkpoints carded in the `eeg-models` strand can ingest it at all. That specification is now
read, and it settles three questions the review had been carrying as open.

The third comparison is viable: ECG, EOG and respiration are all present, on the same amplifier as
the EEG, so they are hardware-synchronous rather than aligned after the fact. The project assumed
this; it is now established.

Ingestion is a real obstacle but not a blocking one. At 206 EEG channels, STRUM sits far outside
every checkpoint's pretraining distribution, and the models that index spatial identity by channel
name (LaBraM, BIOT, CBraMod) cannot take it without selecting or interpolating down to their expected
layout. The coordinate-driven models (REVE, and LUNA on the same principle) can take an arbitrary
layout, and since BioSemi records referentially rather than bipolar, they avoid the midpoint
approximation both resort to for bipolar data. 512 Hz needs resampling for all of them.

The label question changes character entirely. The side tasks are a 2x2 of stimulus modality by
stimulus kind, so spoken-versus-written is one cell of a factorial design rather than a bare
contrast, and the other cells are the control for the sensory confound. See the Task field below;
this is the single most useful thing the full paper contributes.

Two further facts bear on the project. First, the citation count is 2 in
both Semantic Scholar and OpenAlex, and both citing works are the authors' own orbit rather than
modelling work (see Notable details). There is therefore effectively no published baseline on
STRUM to compare against, which changes what a first modelling result on it can claim: it is not
"we beat the state of the art on STRUM", it is "we establish the first". Second, the abstract's
own framing — that established BCI algorithms show "a pronounced performance differential to
highly simplified lab experiments" on these data — is a claim by the dataset's authors that
STRUM is harder than the benchmarks the pretrained checkpoints in strand A were evaluated on.
If that holds, the transfer numbers reported by those checkpoints are upper bounds rather than
expectations.

## Notable details

**Source note, 2026-08-01.** The complete six-page paper was obtained through UCSD institutional
access and is cached as `source.local.pdf`, gitignored and not committed because the paper is under
IEEE copyright. `source.md` is its pymupdf4llm extraction, all six pages with intact text layers.
Every field below is now read from the primary source. Nothing in this card is inferred from
secondary descriptions.

**Fixed field set**, all values read from section III, Data Collection, unless noted:

- **Participants**: **56, as 28 pairs**, UCSD students under UCSD IRB approval, mean age 20.3 +/- 2.3
  years. "3 datasets were excluded due to interruptions in the experiment", so usable sessions are
  fewer than 28; the paper does not restate the surviving count. The sex breakdown given is "13 f,
  49 m", which sums to 62 rather than 56. The paper is internally inconsistent here and the
  discrepancy is recorded rather than reconciled, per the standing rule for self-contradicting
  sources.
- **Simultaneous participants per recording**: **two**. "The data for each two-participant session
  were recorded into a single time-synchronized file in XDF format."
- **Channels**: **206-channel EEG**, plus a 43-channel electromyography neckband, 2-channel
  electrocardiography, 2-channel electrooculography, and a 16-channel respiration belt, all on the
  same 24-bit BioSemi amplifier. That is 269 channels per subject on one amplifier, so 538 across the
  pair.
- **Sampling rate**: acquired at **2048 Hz, resampled to 512 Hz**. Separately, a room-scale PhaseSpace
  motion-capture system samples hand and head position at 480 Hz.
- **Peripheral channels present**: **confirmed, and richer than the project assumed**. 2-channel ECG,
  2-channel EOG, and a 16-channel respiration belt, on the same amplifier as the EEG and therefore
  hardware-synchronous with it. Also present, and not in the project's plan: 43-channel EMG neckband,
  force plate, head-mounted eye tracker with scene camera, two video cameras, desk microphone, and an
  instrumented Xbox 360 controller. The third comparison's premise is sound.
- **Total hours**: **about 3.5 hours per session.** "The overall experiment takes ca. 3.5 hours to
  maximize the amount of data collected per subject, and also to induce a moderate degree of
  fatigue." The paper does not give a corpus total; 28 pairs at roughly 3.5 hours is on the order of
  98 session-hours, but that is arithmetic rather than a reported figure.
- **Task**: a multi-task battery. The side tasks form an explicit factorial design: "broken down by
  stimulus modality (auditory/visual) and stimulus kind (verbal/non-verbal), yielding a matrix of
  four tasks, plus one additional task with natural visual stimuli". Each task presents a stimulus
  sequence, a fraction of which is followed by a query about the preceding, no-longer-displayed
  stimulus; queries match their task's modality and kind. Responses alternate between touchscreen and
  voice, self-paced, with a penalty for more than 15 successive uses of one modality.

  **This is the most consequential thing the full paper settles, and it changes the label plan from a
  liability into a testable design.** The project's "spoken versus written" contrast is, in STRUM's
  own terms, auditory-verbal versus visual-verbal: one cell of a 2x2. Because the same 2x2 contains
  non-verbal tasks in both modalities, the sensory confound that
  [simanova-2010-eeg-object-categories](../simanova-2010-eeg-object-categories/card.md) demonstrates
  is not merely a risk to acknowledge, it is a factor the dataset lets you subtract. A classifier
  trained on the verbal cells can be tested on the non-verbal ones: if it transfers, it is reading
  modality rather than language, which is precisely the failure Simanova reports. The design supplies
  its own control, and any modelling on this label should use it.
- **Label type**: stimulus condition, derived from event annotations. Task, modality, kind, query
  type, response modality, and correctness are all recorded per trial.
- **Label source**: events "recorded in great detail and described using an ontology extended from
  the HED 1.0 event marker specification", so conditions come from Hierarchical Event Descriptor tags
  rather than bare trigger codes. Scoring is explicit, with per-trial points and audiovisual feedback,
  and subject bonus pay tied to final score, capped at 20 dollars.
- **Synchronization and format**: Lab Streaming Layer, with each two-participant session written to a
  single time-synchronized XDF file. The Lab Streaming Layer lead recorded in this strand's brief as
  an inference is therefore confirmed by the primary source.
- **License**: unknown for the data. The paper is under IEEE copyright.
- **Access route**: request to authors. The community list `meagmohit/EEG-Datasets` records
  STRUM verbatim as "Strum dataset is not available on headit.ucsd .. contact authors", and no
  registry sweep (PhysioNet, OpenNeuro, NEMAR, Zenodo, figshare) located a hosted copy. The
  abstract calls it "a new open dataset"; the practical access route contradicts that word, and
  the contradiction is a fact about the record rather than a resolvable question.

**Derivation scheme and electrode layout** (requested specifically, because it decides whether a
layout-flexible checkpoint can ingest STRUM without approximation):

- **Derivation scheme**: **not stated explicitly, but constrained by the hardware.** The paper says
  only "a 206-channel EEG montage (24-bit BioSemi amplifier)", using "montage" in the loose sense of
  a cap layout rather than a derivation scheme. BioSemi systems acquire referentially against the
  CMS/DRL driven-feedback pair and do not record bipolar derivations; re-referencing is an offline
  choice left to the analyst. So STRUM is not bipolar as recorded, and the midpoint approximation
  that `reve-2025` and `luna-2025` both resort to for bipolar data does not apply here. The
  layout-flexible checkpoints can ingest STRUM's channels directly, given coordinates.

  Two caveats. The paper does not name the reference used for any released version of the data, so
  what re-referencing has already been applied is unknown. And 206 channels is far outside the range
  any checkpoint in strand A was pretrained on: REVE's corpus spans 396 unique electrode names but
  its recordings mostly follow 10-5, and the learned-per-channel-embedding models (LaBraM, BIOT,
  CBraMod) index spatial identity by channel name, so they cannot ingest a 206-channel set without
  channel selection or interpolation down to their expected montage.
- **Electrode positions**: not stated. The paper does not say whether individual electrode
  coordinates were digitised per subject or whether a template layout is assumed. For a 206-channel
  cap this matters more than usual, since a coordinate-driven model needs a position per channel and
  a template for a non-standard high-density cap may not exist.

**Practical consequences for the project**, from the specification above:

- **Resampling is required.** 512 Hz against REVE's 200 Hz contract, and 200 or 256 Hz for the
  others.
- **The memory constraint in `CLAUDE.md` is now explained rather than merely observed.** 269 channels
  per subject at 512 Hz, two subjects in one XDF file, is on the order of gigabytes per session hour.
  Loading a whole recording exhausting a kernel is the expected behaviour of this format, not a
  configuration problem.
- **The peripheral branch has more to work with than planned**: ECG, EOG and respiration as assumed,
  plus EMG, eye tracking, force plate and motion capture, all hardware-synchronous.

**Citation record:**

- **Citation count**: 2, agreeing across Semantic Scholar (`opencite lookup`, "Cited: 2") and
  OpenAlex (`cited_by_count: 2`). The figure asserted in the strand brief at brief-writing time
  still holds at retrieval time.
- **Forward citations (the 2 citing works)**: Kothe et al. (2024), "The Lab Streaming Layer for
  Synchronized Multimodal Recording", bioRxiv `10.1101/2024.02.13.580071` — carded here as
  `lsl-2024`, shares an author with STRUM; and Acar & Makeig (2022), "Evaluation of skull
  conductivity using SCALE head tissue conductivity estimation using EEG", EMBC,
  `10.1109/embc48229.2022.9872004` — a forward-model methods paper, also sharing an author.
  Neither trains or evaluates a model on STRUM data.
- **Backward citations (references)**: OpenAlex lists 21 works, while the printed bibliography
  numbers 24; the years below come from the indexes rather than the printed list, and three of
  them disagree with it (Blankertz 2011, Lotte and Guan 2011, Tomioka and Mueller 2010). All
  pre-2017, and characteristic of a passive-BCI
  methods lineage rather than a dataset lineage — Farwell & Donchin (1988), Ramoser et al. (2000)
  common spatial patterns, Ang et al. (2008) FBCSP, Blankertz et al. (2010), Lotte & Guan (2010),
  Tomioka & Müller (2009), Zander & Kothe (2011) passive BCI, Kothe & Makeig (2013) BCILAB,
  Bigdely-Shamlo et al. (2013) Hierarchical Event Descriptors, Klosterman et al. (2016) on
  day-to-day variability in hybrid passive BCIs. No dataset descriptor is cited, which is
  consistent with STRUM being positioned as a first-of-kind release rather than as a successor to
  an existing corpus.

**Bibliographic discrepancy, unresolved:**

- Author order differs between indexes. dblp (`conf/smc/MullenKM18`) and Semantic Scholar both
  give Mullen, Kothe, Makeig. Crossref's IEEE deposit and OpenAlex both give Kothe (sequence
  `first`, corresponding author, affiliation "Intheon Labs, Intheon, San Diego, CA, USA"), then
  Mullen, then Makeig. The IEEE Xplore page, which would settle it, blocks automated retrieval.
  **Settled by the PDF title block**, which gives Kothe, then Mullen, then Makeig, matching Crossref
  and OpenAlex against dblp and Semantic Scholar. The card frontmatter follows the paper. The bib
  entry still carries the dblp order and is corrected alongside this note.

## Open questions / limitations

This section was written before the paper was obtained and has been rewritten against the full text.
The specification is no longer among the open questions; what follows is what the paper genuinely
leaves open.

- **The reference is not stated.** BioSemi acquires against its CMS/DRL pair, so the recording is
  referential rather than bipolar, but the paper never says what reference any released version of
  the data carries, nor whether re-referencing was applied before distribution.
- **Electrode positions are not stated.** Whether per-subject coordinates were digitised, or a
  template is assumed, is unrecorded. For a 206-channel cap this decides whether a coordinate-driven
  checkpoint can be given a position per channel at all.
- **The paper contradicts itself on channel count.** Section III says "206channel EEG montage";
  section IV says "the 205-channel EEG was subsampled to a subset of 64 approximately equidistant
  channels". Both are quoted here rather than reconciled. The card's fixed field set uses 206, from
  the data-collection section, following the standing rule to prefer the section that describes the
  recording over one describing an analysis.
- **The paper contradicts itself on participants.** 56 as 28 pairs, against a sex breakdown of
  "13 f, 49 m" summing to 62.
- **The usable session count is not restated** after "3 datasets were excluded due to interruptions".
- The abstract says "open dataset", and the paper's own footnote gives a distribution point:
  "Available from http://headit.ucsd.edu/". So the data were published, and the community list
  recording "not available on headit.ucsd .. contact authors" describes a host that has since gone
  away rather than a dataset that was never released. What remains open is whether the authors will
  supply it now, not whether it was ever public.
- The two-citation figure is a fact about visibility, not about quality, and the same figure is
  consistent with a dataset that was never distributed widely enough to be modelled. Which of
  those explains it is not determinable from what was read.
- The strand brief's retrieval command, `opencite cite "<doi>" --direction backward`, is not a
  valid invocation; `--direction` accepts only `citing`, `references`, `both`. The numbers above
  come from `--direction citing` and `--direction references` run separately. `--direction both`
  additionally emits `WARNING: opencite.citations: Citation query failed: 'NoneType' object is
  not iterable` while still returning 23 merged results, so its output should not be trusted
  as complete without the two single-direction runs to check it against.

## Citations

Primary: `strum-2018`

- `lsl-2024` — Kothe et al., bioRxiv 2024. One of the two works citing STRUM; the synchronisation
  toolchain STRUM may or may not have been recorded with.
- Acar & Makeig (2022), EMBC, `10.1109/embc48229.2022.9872004` — the other citing work; head
  tissue conductivity estimation, not a modelling use of STRUM.
- Zander & Kothe (2011), J. Neural Eng. `10.1088/1741-2560/8/2/025005` — the passive-BCI framing
  STRUM is built inside, and one of its references.
- Klosterman et al. (2016), EMBC `10.1109/embc.2016.7591015` — a STRUM reference on day-to-day
  variability in hybrid passive BCIs, the closest thing in its reference list to a prior dataset
  study.
- `hinss-2023-passive-bci` — the open multi-session passive-BCI dataset carded here as STRUM's
  nearest specified comparator.
