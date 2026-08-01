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
modalities: [scalp-eeg, unknown-peripheral]
tags: [strum, neuroergonomics, passive-bci, task-battery, real-world-bci, paywalled, access-by-request, two-citations, project-target-dataset]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: partial
---

## TL;DR

The dataset this project intends to fine-tune on is described only in a six-page paywalled IEEE
proceedings paper with no open copy anywhere; page 77 was later obtained through institutional
access and establishes that recordings are genuinely two-person and that events carry extended
HED 1.0 tags, but the recording specification — channel count, sampling rate, derivation scheme,
peripheral channels — sits on pages 78 to 82 and is still unread; two papers cite it, neither of
them a modelling study.

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
among alternative methods". Everything above is quoted from the abstract, which is the entire
extent of the accessible text: the paper is behind the IEEE paywall, Unpaywall reports
`oa_status: closed` with zero open-access locations and `has_repository_copy: false`, and the
author-side pages named in the strand brief (Swartz Center for Computational Neuroscience,
Intheon) do not host a copy.

## Relevance to the review

STRUM is the dataset the project proposes to fine-tune on, so its specification determines
whether any of the checkpoints carded in the `eeg-models` strand can ingest it at all. That
specification is currently unread, which is the single largest open item in this strand and is
recorded as such rather than guessed at.

Two facts that are accessible do bear on the project directly. First, the citation count is 2 in
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

**Source note, 2026-08-01.** The first page of the paper was obtained through institutional access
and is cached locally as `source.local.pdf`; `source.md` is its extraction. It is **page 77 only, one
page of six**, ending mid-sentence in section "C. Spatial Layout", and it is not committed because
the paper is under IEEE copyright. Fields below marked `reported but not accessible` are therefore
facts the source carries on pages 78 to 82, which have not been read. Fields that page 77 does settle
are now marked as sourced.

**Fixed field set** (per the strand brief; `reported but not accessible` distinguishes facts the
primary source certainly carries from facts no source states, following
`_briefs/collection-practice.md`):

- **Participants**: reported but not accessible: the abstract calls the data "this large trove
  of data" and does not give a participant count. No secondary source consulted gives one, and it is
  not on page 77.
- **Simultaneous participants per recording**: **two**, now sourced. Page 77 states the laboratory
  space "includes two identical seats for the subjects, each equipped with three vertically mounted"
  displays, the sentence breaking at the page boundary. STRUM is therefore a genuinely two-person
  simultaneous recording, which was previously a project assumption this card declined to card as
  fact. Whether the two participants interact, and whether labels are per-participant or per-dyad,
  remains unread.
- **Channels**: reported but not accessible.
- **Sampling rate**: reported but not accessible.
- **Peripheral channels present**: reported but not accessible. The project plan assumes
  electrocardiography, electrooculography and respiration are present; no read source confirms
  this.
- **Total hours**: reported but not accessible.
- **Task**: partially sourced. "A task battery modeled after a complex real-world scenario", and page
  77 adds that the paradigm is multi-task and "puts heavy emphasis on selective attention in visual
  and auditory domains", that "task load, fatigue, and attention distribution are expected to vary",
  and that individual tasks "are designed to elicit frequent perceptual and response errors". The
  constituent tasks are named on pages not read.

  This bears directly on the project's label plan. The paradigm deliberately manipulates attention
  across the visual and auditory domains, so a visual-versus-auditory contrast is built into the
  design rather than incidental to it. That makes the concern recorded in
  `simanova-2010-eeg-object-categories` sharper, not weaker: a classifier separating spoken from
  written stimuli in STRUM would be separating two modalities the experiment was constructed to drive
  apart. Whether anything beyond sensory response distinguishes them is the open question.
- **Label type**: reported but not accessible for the task labels, but the marker mechanism is
  sourced: page 77 states that "events are recorded in great detail and described using an ontology
  extended from the HED 1.0 event marker specification". Labels therefore come from Hierarchical
  Event Descriptor tags rather than from bare trigger codes, which means the stimulus conditions
  should be recoverable from the event annotations without inference. Which tags exist is unread.
- **Label source**: stimulus and event annotation via the extended HED 1.0 ontology, per page 77. The
  intended constructs named on that page are task load, fatigue, and attention distribution; whether
  any is separately labelled, for instance by self-report, is unread.
- **License**: unknown for the data. The paper is under IEEE copyright.
- **Access route**: request to authors. The community list `meagmohit/EEG-Datasets` records
  STRUM verbatim as "Strum dataset is not available on headit.ucsd .. contact authors", and no
  registry sweep (PhysioNet, OpenNeuro, NEMAR, Zenodo, figshare) located a hosted copy. The
  abstract calls it "a new open dataset"; the practical access route contradicts that word, and
  the contradiction is a fact about the record rather than a resolvable question.

**Derivation scheme and electrode layout** (requested specifically, because it decides whether a
layout-flexible checkpoint can ingest STRUM without approximation):

- **Derivation scheme**: reported but not accessible. Whether STRUM's channels are referential
  (and to what reference), bipolar, or average-referenced could not be determined from any read
  source. This is the load-bearing gap. `reve-2025` in the `eeg-models` strand accepts an
  arbitrary electrode *layout* — a set of 3D positions — but has no native representation for a
  bipolar *derivation*, and its authors handle bipolar data by substituting the midpoint of the
  electrode pair. If STRUM is bipolar, every layout-flexible checkpoint in strand A ingests it
  only through that approximation; if it is referential with a standard 10-20 or 10-10 layout,
  they ingest it directly.
- **Electrode positions**: reported but not accessible. No source read states whether individual
  electrode coordinates were digitised or whether a template layout is assumed.

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
- **Backward citations (references)**: 21 works, all pre-2017, and characteristic of a passive-BCI
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
  The card and the bib entry follow dblp and Semantic Scholar, and the discrepancy is recorded
  here so a later reader does not assume the bib was checked against the publisher's own page.
  It was not.

## Open questions / limitations

- Every field that decides whether this project is feasible is unread. Until the paper is
  obtained through institutional IEEE access, or the data are obtained from the authors, the
  channel count, sampling rate, derivation scheme, peripheral channel inventory, participant
  count, and label scheme are all unknown, and no downstream phase should treat this card as
  supplying them.
- The abstract says "open dataset" while the only recorded access route is contacting the
  authors. Whether the data were ever hosted publicly, and whether they still are, is unresolved.
- Whether STRUM was recorded with the Lab Streaming Layer is unverified. The strand brief flags
  this as plausible and instructs confirming it from the STRUM methods rather than assuming it;
  the methods could not be read, and the fact that the LSL paper cites STRUM establishes only
  that LSL's authors cite it, not that STRUM used LSL. Carded as unresolved.
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
