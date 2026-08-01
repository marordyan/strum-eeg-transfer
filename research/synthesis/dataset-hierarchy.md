# The dataset hierarchy

Phase 3 synthesis. This is the **data layer** of the corpus: what recordings exist across all four
strands, how they stand to one another, what each is specified to be, and what role each plays for
which model or suite. It is the document to read when the question is *what data is there*, prior to
any question about what should be done with it.

Its inputs are the four strand ontologies, the cross-strand
[science map](./science-map.md), and the 84 cards those documents organize. Where a fact is grounded
on a card, that card is linked.

**What it is not.** It is not the two dataset ontologies re-cut.
[datasets-benchmarks](./datasets-benchmarks-ontology.md) is keyed on *how the field measures* —
split protocol, what a suite fixes, how wide the interval is — and
[candidate-datasets](./candidate-datasets-ontology.md) on *fitness for fine-tuning* — label
provenance, manipulation geometry, ingestion contract. Both hold recordings as instances of those
questions. This document holds the recordings themselves and lets the questions attach to them as
attributes. Nothing below should be movable into either ontology unchanged; where a section would
be, it has been cut to a link.

It is also not the gap analysis. "Which dataset should the project use" and "no recording covers X"
are Phase 4. Where a card states an absence about its own dataset, quoting it is a property
statement and belongs here. The handful of sentences that sit on the line are marked **[boundary]**,
following the convention the `multimodal-biosignals` ontology established.

---

## 0. The organizing key, and the vocabulary it has to fix

### 0.1 Why a hierarchy keyed on "kind of dataset" collapses

The science map's theme 9 states the problem and this document's subject is its resolution: **one
recording plays several roles.** TUAB and TUEV are BIOT's and CBraMod's pretraining data *and* their
evaluation sets ([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) Table 7).
PhysioNet-MI is EEGPT's pretraining data, a benchmark EEGPT is compared on, the largest of MOABB's
twelve datasets and a Brain4FMs task
([physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md)). Sleep-EDF is a benchmark
([sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)) and a candidate
fine-tuning substrate ([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)) — the same
recording, carded twice, to two different questions. A dataset reached *through* MOABB can be
pretraining data for a checkpoint that a MOABB-derived NeuralBench task then evaluates
([moabb](../collection/datasets-benchmarks/moabb/card.md),
[neuralbench](../collection/datasets-benchmarks/neuralbench/card.md),
[reve-2025](../collection/eeg-models/reve-2025/card.md)).

A top level of "pretraining corpora / downstream benchmarks / candidate corpora" therefore either
files those recordings three times or picks one arbitrarily. The `datasets-benchmarks` ontology
already reached this conclusion for its own strand and departed from the brief's categories for
exactly this reason.

### 0.2 The key: the recording, in a derivation chain, with roles as attributes

The property that survives is **the recording** — the body of acquired signal — placed in the chain
that produced the object a model actually consumed. That chain has four levels, and the corpus
routinely uses one word for all four.

| level | what it is | example |
|---|---|---|
| **archive** | a container that distributes many recordings under one access route and, sometimes, one licence | [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md), [openneuro](../collection/datasets-benchmarks/openneuro/card.md), PhysioNet, [nemar-2022](../collection/candidate-datasets/nemar-2022/card.md) |
| **acquisition** | the recording as performed: participants, channels, sampling rate, reference, peripheral inventory, task | the 16,986 Temple University sessions; STRUM's 28 pair-sessions |
| **release** | the distributed artifact: files, format, version, licence, access route, and any partition that ships with it | TUAB v3.0.1's fixed train/evaluation split; DEAP's 128 Hz preprocessed version against its 512 Hz acquisition |
| **preparation** | one consumer's version: channel selection, re-derivation, resampling, windowing, split | AdaBrain-Bench's TUAB at 23 channels in 10-second windows; BIOT's 16 bipolar derivations of TUEV |

Every level below the archive can be renamed, re-channelled and re-partitioned without any statement
that it happened, and §6 registers the cases where a preparation's figure is in circulation as a
property of the acquisition.

**Role is an attribute of a (recording, consumer) pair, not a level.** Five values occur in the
corpus:

- **pretraining substrate** — the recording is inside a checkpoint's self-supervised corpus.
- **evaluation benchmark** — a suite or a checkpoint's own paper reports a number on it.
- **candidate fine-tuning corpus** — the `candidate-datasets` strand's question: could this project
  train on it.
- **ablation or control substrate** — the recording exists in the corpus to support a negative
  control, a leakage demonstration or a probe, rather than a leaderboard.
  [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)'s
  ds004504-versus-CAUEEG dataset-identity probe and
  [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)'s
  proprietary Alzheimer's cohort are the clean cases.
- **reserved holdout** — excluded from pretraining *at pretraining time* so that it can serve as a
  cross-dataset generalisation test. The corpus contains this in the peripheral strand only:
  [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) excludes
  UHN-ECG entirely, and
  [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) holds some datasets out
  as out-of-domain.

### 0.3 What this fixes that theme 9 left open

Theme 9 records that the three strands name the overlap three different ways — *in-domain
evaluation* in the models strand
([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)),
*pretraining-to-evaluation overlap* in the benchmark strand
([neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)), and not at all in the
candidate strand — and that all three are talking about one structural property. What it does not
supply is the unit the property is a property *of*. On the vocabulary above, the overlap is not a
defect of a dataset and not a defect of a checkpoint: it is **two roles held by one recording, with
the two role-holders separated in time**. That is why the remedy from theme 1 does not reach it, and
[tuab](../collection/datasets-benchmarks/tuab/card.md) says so directly — a patient-disjoint
fine-tuning split is chosen at the *preparation* level, while the contamination happened at the
*acquisition* level, one archive up and one stage earlier.

The same vocabulary makes the corpus's two dual-carded recordings legible as design rather than as
filing error. [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) and
[sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) are one
acquisition, one release, two roles, two cards; their divergences (§3.6, and
`candidate-datasets` §9.1a) are card-level defects sitting on top of an object that is not in
dispute.

---

## 1. The census

**Counting rule.** A *recording* is a distinct body of acquired signal with an identity in the
corpus — a name, or an unnamed study-own cohort attributable to exactly one card. Aliases collapse
to one recording (PhysioNet-MI = PhysioMI = MMI = EEGMMIDB = MOABB's "PhysioNet"; BCI-IV-2a =
BCIC-2A = BNCI2014-001; Things-EEG = ThingsEEG2; Sleep-EDF = Sleep-EDFx = SSC; DEAP = DEAP-arousal;
HGD = High Gamma; TUEG = TUH EEG Corpus). A derived subset with its own name and its own access path
counts separately from its parent archive, because it has its own release and its own roles.
Archives, registries, formats and frameworks are *not* recordings and are counted separately in
§2.0.

On that rule the corpus's data layer holds **154 distinct recordings**:

| | count |
|---|---|
| **carded** — the recording has its own card directory | **14** (across 15 cards; Sleep-EDF is carded twice) |
| **only named** — the recording appears solely inside another card's text | **140** |

The 14 carded recordings are exactly the 15 `type: dataset` cards, minus the Sleep-EDF duplicate:
[strum-2018](../collection/candidate-datasets/strum-2018/card.md),
[mous-2019](../collection/candidate-datasets/mous-2019/card.md),
[hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md),
[tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md),
[deap-2012](../collection/candidate-datasets/deap-2012/card.md),
[amigos-2021](../collection/candidate-datasets/amigos-2021/card.md),
[boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md),
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md),
Sleep-EDF ([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) /
[sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)),
[tuab](../collection/datasets-benchmarks/tuab/card.md),
[tuev](../collection/datasets-benchmarks/tuev/card.md),
[tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md),
[physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) and
[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md).

Three properties of that count, each a fact about the record rather than about the field.

**The 140 is a floor, not a total.** Two suites do not enumerate their scope on their cards.
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) covers 54 datasets and its
card names six, because "the detailed per-dataset accuracies live in supplementary tables 5, 6 and 7
that are not part of the main text"; [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)
covers 94 datasets and its card names none of them by name, reaching them through MOABB and
OpenNeuro instead. [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) names ten of its
eighteen. Two pretraining corpora are likewise unenumerated at source:
[reve-2025](../collection/eeg-models/reve-2025/card.md) names 92 datasets and accounts hours by
archive rather than per dataset, and
[brainwave](../collection/eeg-models/brainwave/card.md)'s 40,907 hours are "reported as a total and
a modality split, not per source dataset".

**Carding tracks the strand's question, not the recording's importance.** All nine
candidate-strand dataset cards are recordings nobody in the corpus has modelled; the six
benchmark-strand dataset cards are the ones everybody has. The recordings under most of the field's
pretraining — PREST, the Temple subsets other than TUAB and TUEV, LaBraM's and BrainOmni's source
lists — are carded nowhere.

**Two recordings are carded twice and one framework three times.** Sleep-EDF has a card in each
dataset strand; [openneuro](../collection/datasets-benchmarks/openneuro/card.md) /
[openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) is the same for the
archive; AdaBrain-Bench is carded in `datasets-benchmarks` and `eeg-models`. Both INDEX files record
that Phase 5 must merge these to one bibliography entry per identifier.

---

## 2. The hierarchy

Ordered by archive where an archive exists, then by what the recording is, then by role. Ordering
carries no ranking.

### 2.0 The layer beneath: archives, registries, containers and readers

Not recordings, but the thing every recording below sits inside, and the level at which access,
licence and discoverability are actually decided.

- **[tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md)** — archive and
  acquisition at once, which is why it appears twice in this document. 16,986 sessions from 10,874
  patients, one clinical site, one country. Signed form to `help@nedcdata.org`, then ssh keys and
  `rsync -auvxL` (the `-L` is required because every subset is symlinked back to the parent). **No
  data licence** in either the paper or the downloads page; the card states the consequence
  precisely, that "registration and a signed form are not a licence grant".
- **[openneuro](../collection/datasets-benchmarks/openneuro/card.md) /
  [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md)** — 604 datasets and
  20,989 participants as of 9 October 2021, of which 81 scalp-EEG and 8 intracranial; median dataset
  size 23 subjects; CC0 by default with no authentication; mandatory BIDS validation at submission;
  snapshots as git tags with DOIs; GDPR-covered data excluded. CC0 is a default rather than a
  guarantee, and the archive's GraphQL `advancedSearch` has no free-text field, so a zero result
  means "nothing tagged", not "nothing exists".
- **[nemar-2022](../collection/candidate-datasets/nemar-2022/card.md)** — the EEG/MEG/iEEG-scoped
  gateway over OpenNeuro, with per-dataset quality assessment and a handoff to San Diego
  Supercomputer Center compute. Holds no data of its own; reports no dataset count.
- **PhysioNet** — host of [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) and
  [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md), Open Data Commons Attribution
  v1.0, no registration, `wget` or `aws s3 sync --no-sign-request`. Not carded as an archive, though
  it supplies 22,707 of REVE's 61,415 pretraining hours.
- **[moabb](../collection/datasets-benchmarks/moabb/card.md)** — a framework that is also an access
  layer over twelve motor-imagery datasets, and therefore a recording aggregator: NeuralBench reaches
  its motor-imagery and P300 datasets through it and REVE draws 384 pretraining hours from it.
- **Hosts named but not carded** — Zenodo, FigShare, the Donders Institute repository,
  `bbci.de/competition/iv/`, `eecs.qmul.ac.uk` (down throughout retrieval, §3.6), and
  `headit.ucsd.edu`, STRUM's stated distribution point, which no longer resolves.
- **Formats and readers** — [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md),
  [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) /
  [eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md),
  [mne-python](../collection/datasets-benchmarks/mne-python/card.md),
  [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) and XDF, GDF, BrainVision, EEGLAB
  `.set`. What they make recordable is the `datasets-benchmarks` ontology's §6 and is not restated;
  what matters at this level is only that the file layer is where the specification fields of §3
  either survive or do not — EDF+ stores channel labels and **has no mechanism at all for electrode
  coordinates**, and `channels.tsv` is the only machine-readable statement of channel *type*
  anywhere in the corpus.

### 2.1 The Temple University Hospital family

One archive, eight named members, and the substrate under most of the field's pretraining.

| member | carded | role | what the corpus states about it |
|---|---|---|---|
| **TUEG** (TUH EEG Corpus) | [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) | pretraining substrate | parent archive; 16,986 sessions / 10,874 patients; 31 channels most common, range 20–36; 87% at 250 Hz; **no montage stated, the word does not occur**; labels are the neurologist's free-text report plus an optional six-class per-channel event annotation; no cognitive, behavioural or stimulus label exists |
| **TUAB** | [tuab](../collection/datasets-benchmarks/tuab/card.md) | pretraining substrate (BIOT, CBraMod) **and** evaluation benchmark (all four suites) | selected from sessions recorded with an average-reference configuration, "about 45% of the data in the overall corpus"; ships a fixed train/evaluation partition whose patient-disjointness is **not asserted anywhere the corpus could read** |
| **TUEV** | [tuev](../collection/datasets-benchmarks/tuev/card.md) | pretraining substrate (BIOT, CBraMod) **and** evaluation benchmark | the corpus's own documentation is one paragraph; participants, channels, rate, hours, class balance and partition are all unknown from the primary source |
| **TUAR** | only named | pretraining substrate (CBraMod); evaluation for FEMBA and LUNA under four labelling protocols | named on [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md); no specification anywhere |
| **TUEP** | only named | pretraining substrate (CBraMod, LaBraM) | no specification anywhere |
| **TUSE** | only named | pretraining substrate (CBraMod) | no specification anywhere |
| **TUSL** | only named | pretraining substrate (CBraMod); evaluation for FEMBA and LUNA | no specification anywhere |
| **TUSZ** | only named | pretraining substrate (LaBraM) | no specification anywhere |

Two properties of the family that only appear when it is drawn as a tree.

**The derivation scheme is not a property of the family at any level.**
[tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) states no montage;
[tuab](../collection/datasets-benchmarks/tuab/card.md)'s only derivation statement is a *selection
criterion* (average-reference sessions) and its thesis's 22-channel transverse-central-parietal
montage is a re-derivation the author applied; [tuev](../collection/datasets-benchmarks/tuev/card.md)
inherits nothing and acquires the field's 16 bipolar convention from BIOT's release scripts, "a field
convention with no documented provenance in the corpus". So every checkpoint pretrained on TUH data
chose its own derivation and none of those choices is recoverable from the archive.

**The subsets carry roles the parent does not.** TUEG is pretraining substrate only and never an
evaluation set. TUAB and TUEV are both, for the same two checkpoints, and are between them reported
on by BIOT, EEGPT, LaBraM, CBraMod, REVE, BENDR, BrainOmni, FEMBA, Neuro-GPT, NeuroLM, EEGMamba and
LUNA across the four suites. The five unspecified subsets are pretraining-only. The role therefore
attaches to the *subset*, one level below the archive that supplies the signal.

### 2.2 PhysioNet

| recording | carded | role |
|---|---|---|
| **PhysioNet-MI** (EEGMMIDB / PhysioMI / MMI) | [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) | pretraining substrate (EEGPT) **and** evaluation benchmark (REVE, CBraMod, LaBraM, BIOT, BENDR, BrainOmni, Lee's battery), **and** MOABB's largest dataset, **and** a Brain4FMs task |
| **Sleep-EDF Expanded** (Sleep-EDFx / SSC) | [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md), [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) | evaluation benchmark (AdaBrain-Bench, OmniEEG-Bench, Brain4FMs, NeuralBench, BENDR, EEGPT, Lee, Zare) **and** candidate fine-tuning corpus |
| **PhysioNet/CinC Challenge 2018** (PC18) | only named | self-supervision substrate **and** evaluation set, both inside [banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md) — 994 overnight recordings from 994 individuals, two of six channels retained |
| **PhysioNet 2021** (CinC ECG challenge) | only named | pretraining substrate for [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) |
| **PhysioNet, as an archive line item** | not carded as such | 22,707 of [reve-2025](../collection/eeg-models/reve-2025/card.md)'s 61,415 pretraining hours, with no per-dataset breakout |
| **PhysioP300** | only named | evaluation for [bendr-2021](../collection/eeg-models/bendr-2021/card.md) and [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) |

PhysioNet is the only archive in the corpus whose recordings carry an explicit data licence at the
archive level, and the two carded ones are the corpus's lowest-friction access route.

### 2.3 OpenNeuro and NEMAR

OpenNeuro contributes 10,194 hours to REVE and is one of NeuralBench's standardized data sources, so
it is a pretraining archive, an evaluation archive and a candidate-dataset registry at once. Two
individual OpenNeuro datasets are named in the corpus: **`ds003670`**, which is
[tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md)'s BIDS release, and
**`ds004504`**, the Alzheimer's cohort that
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) uses as one
side of its dataset-identity probe — a linear probe separates it from CAUEEG on frozen REVE
embeddings at AUROC 1.000. NEMAR is the EEG-scoped browsable layer over the same holdings, and its
card notes the difference between "600 datasets, mostly MRI" and a browsable EEG inventory. STRUM is
in neither.

### 2.4 MOABB's twelve

All motor imagery, all subsampled to 128 Hz for the benchmark, 275 subjects in total. Only two are
carded elsewhere. The remaining ten are named only in
[moabb](../collection/datasets-benchmarks/moabb/card.md)'s reproduction of Table I, with imagery
type, channels, trials, sessions, subjects and epoch window each — which makes MOABB the only
consumer in the corpus that publishes a full specification row for every recording it uses.

| recording | channels / trials / sessions / subjects | note |
|---|---|---|
| Cho 2017 | 64 / 200 / 1 / 49 | only named |
| PhysioNet | 64 / 40–60 / 1 / 109 | = [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md); the largest in the table |
| Shin 2017 | 25 / 60 / 3 / 29 | only named |
| BNCI2014-001 | 22 / 144 / 2 / 9 | = [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md), restricted to two classes; MOABB's own figures call it "001-2014" |
| BNCI2014-002 | 15 / 160 / 1 / 14 | only named |
| BNCI2014-004 | 3 / 120–160 / 5 / 9 | only named |
| BNCI2015-001 | 13 / 200 / 2–3 / 13 | only named |
| BNCI2015-004 | 30 / 70–80 / 2 / 10 | only named |
| AlexandreMotorImagery | 16 / 40 / 1 / 9 | only named |
| Yi 2014 | 60 / 160 / 1 / 10 | only named; "Weibo 2014" in every MOABB figure |
| Zhou 2016 | 14 / 100 / 3 / 4 | only named |
| Grosse-Wentrup 2009 | 128 / 300 / 1 / 10 | only named; the densest layout in the table |

### 2.5 Proprietary and unreleased substrate

Four recordings that a checkpoint or a demonstration rests on and that cannot be inspected at all.

- **PREST** — [biot-2023](../collection/eeg-models/biot-2023/card.md)'s larger EEG pretraining
  corpus by sample count: 6,478 recordings, 200 Hz, 16 montage channels, 10-second samples,
  5,110,992 samples, described only as "a large unlabeled proprietary resting EEG dataset". BIOT's
  weights are released and its pretraining is therefore not reproducible.
- **The Cardiology (ECG) corpus** — BIOT's third pretraining source, 21,264 recordings, 500 Hz, 6 or
  12 leads, 495,970 samples. The corpus's only instance of an ECG corpus used as pretraining
  substrate for a model that also ingests EEG, one modality at a time.
- **The eVox Alzheimer's cohort** —
  [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)'s
  Experiment 1: 49 AD against 49 subjective cognitive impairment, 250 Hz, 19 electrodes, collected
  by the authors' company and therefore not reproducible. This is the recording on which the
  corpus's largest measured split effect — 99.8% against 53.0% — was obtained.
- **[sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md)'s
  54-subject motor-imagery dataset**, unnamed in the paper, so overlap with LaBraM's pretraining
  corpus cannot be checked at all.

### 2.6 Standalone released EEG acquisitions — the candidate tier

Nine recordings, all carded, none of them consumed by any checkpoint or suite in the corpus. Full
specification in §3; ordered here by the number of people instrumented at once, because that is the
property the project's setting turns on.

| recording | simultaneous participants | total participants | EEG channels |
|---|---|---|---|
| [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) | 4 | 40 (17 individual, 20 in five groups of four) | 14 |
| [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) | 3 | 10 | 28 EEG + 4 EOG |
| [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) | 2 | 2 | 28 EEG + 4 EOG |
| [strum-2018](../collection/candidate-datasets/strum-2018/card.md) | 2 | 56, as 28 pairs | **206** |
| [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) | 1 | 29 | 63 EEG + 1 ECG |
| [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) | 1 | 20 | 32 |
| [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | 1 | 32 | 32 |
| [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) | 1 | not stated as a figure; 197 recordings | 2 bipolar |
| [mous-2019](../collection/candidate-datasets/mous-2019/card.md) | 1 | 204 | none — 275 MEG axial gradiometers |

### 2.7 Named-only EEG evaluation and probe recordings

The recordings the field reports numbers on, carded nowhere. Grouped by the consumer that names them,
because that is the only handle the corpus gives them.

**AdaBrain-Bench's evaluation table** — the corpus's most complete public specification of a
benchmark's scope, at nine recordings not carded elsewhere, each given as sampling rate / channels /
window / subjects / samples ([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)):
SEED (1,000 Hz / 62 / 1 s / 15 / 144,852), SEED-IV (1,000 Hz / 62 / 1 s / 15 / 151,845), EEGMAT
(500 Hz / 19 / 4 s / 36 / 1,080), SEED-VIG (200 Hz / 17 / 8 s / 21 / 20,355, a regression target),
SHU (250 Hz / 32 / 4 s / 25 / 11,988), Things-EEG (1,000 Hz / 63 / 1 s / 10 / 821,600), Siena
(512 Hz / 29 / 10 s / 14 / 51,307), HMC (256 Hz / 4 / 30 s / 151 / 137,243) and SHHS (125 Hz / 1 /
30 s / 329 / 324,854). Every one of those figures is a **preparation** figure and the card says so.

**Named as pretraining substrate only, with no specification anywhere** — CHB-MIT, IIIC Seizure
(BIOT); HGD, TSU, M3CV (EEGPT); BCI-IV-1, Emobrain, SPIS, Grasp and Lift, Inria P300, and the ESI
NeuroScan collection at 342.23 hours (LaBraM). CHB-MIT is the one of these that also holds three
other roles: a Brain4FMs epilepsy task at 23 subjects, a BrainWave evaluation set, and the substrate
for the single clean controlled positive in
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) —
cross-subject ictal detection at 0.793 AUROC against 0.701 for a randomly initialised encoder.

**BrainOmni's twenty-two sources**, of which the card names eighteen and none is carded
([brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)): EEG — HBN-EEG, HBN EO/EC, SRM,
RestCog, PEARL-Neuro, Features-EEG, MusicEEG, HFO, Go-Nogo, Awakening, the EEG half of Kymata-SOTO;
MEG — CC700 (Cam-CAN), OMEGA, MEG-MASC, SMN4Lang, THINGS-MEG, Kymata-SOTO; and two device systems
held out entirely for the cross-device test, Gloups-MEG and PerceiveImagine. TUEG is explicitly not
among them, which makes BrainOmni the corpus's one checkpoint whose substrate is developmental and
resting-state rather than clinical. Its four downstream sets — AD65, ASD74, MDD and SomatoMotor —
are likewise named only.

**Brain4FMs's named ten**, of which eight are new here
([brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)): MAYO (iEEG, 25 subjects), FNUSA
(iEEG, 14), Dep-BDI (122), MDD-64 (30 healthy + 43 MDD), SD-28 (28), UCSD (31 healthy + 15
Parkinson's), Chisco-R and Chisco-I (125 channels, 500 Hz, 58.6 h, 39 subjects each). Eight of its
eighteen are not named at all.

**OmniEEG-Bench's six named**, of which four are new
([omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)): PD31,
Broderick-Cocktail-party, Broderick-reverse and Monitoring-Errp. The two Broderick sets are the
corpus's nearest published analogue to a spoken-language contrast; forty-eight of the suite's
fifty-four are unrecoverable from the card.

**Named by one checkpoint or critique each** — FACED (CBraMod emotion downstream), BCI-IV-2b
(EEGConformer's second dataset and an EEGPT evaluation set), KaggleERN / ERN (BENDR, EEGPT), ISRUC
(REVE, fed 30-second windows by a model pretrained on 10-second segments), CAUEEG (Zare's external
Korean dementia cohort, where a randomly initialised encoder beats pretrained REVE, 0.659 against
0.570), ds004504 (§2.3), an ERP paradigm from Korea University and an unnamed working-memory dataset
([lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md)), and the
"Workload" task on which NeuroLM's performance decreased with model size
([kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)).

**The four FMScope cells plus one irreproducible headline** —
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)'s 2×2 is one
recording per cell and all four are named only: ADFTD (65 subjects, 19-channel 10-20, 200 Hz,
single-session), EEGMAT (36 subjects × 72 recordings), SleepDep (36 × 72) and Stress-DASS (17
subjects × 70 recordings, 30 channels — the only cell not on a 19-channel montage). The Komarov
stress dataset, whose published 0.9047 headline the paper fails to reproduce by roughly 45 points
under subject-disjoint cross-validation, is a fifth.

**Kamrud's five replication corpora**, unnamed in the source and specified only by cohort
([kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)):
driver fatigue (12 participants, 30 usable channels), confused students (10 or 9, a single-channel
NeuroSky MindSet), alcoholism (122, 64 scalp + 2 EOG at 256 Hz), PTSD (12, 31 EEG at 5,000 Hz
downsampled to 250) and schizophrenia (30, BioSemi ActiveTwo 64 + 2 mastoid at 1,024 Hz). These are
the corpus's five recordings whose only role is to demonstrate what a split boundary costs.

### 2.8 Peripheral and non-EEG corpora

The data layer of the third comparison. Twenty-two recordings, none carded, split by what they carry.

- **ECG at scale** — MIMIC-IV-ECG (ECG-FM's pretraining source and its released public benchmark,
  split by patient only because acquisition dates are imprecise), UHN-ECG (**reserved holdout**, the
  corpus's one instance of the role), PhysioNet 2021
  ([mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md)).
- **PPG at scale** — VitalDB (5,866 participants, 17,355 hours, 500 Hz intraoperative finger PPG),
  the MIMIC-III waveform matched subset (125 Hz, the rate everything is resampled to) and the MESA
  sleep sub-study (256 Hz native), all pretraining substrate for
  [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md); plus its downstream sets
  PPG-BP (219 subjects), nuMom2B, SDB (146) and VV (231, stratified over the six-level Fitzpatrick
  scale). VitalDB is dual-role: it is also the entire data source for
  [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md),
  6,388 surgical patients reduced to 1,022 by an exclusion cascade.
- **EEG-plus-peripheral affect and load corpora, named only** — WESAD, CASE, DREAMER, MAHNOB-HCI,
  ASCERTAIN (58 subjects), CLAS, MAUS, WAUC (48 subjects at three exercise levels), COLET (eye
  tracking), CL-Drive (21 subjects, the study's own release in
  [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)),
  and the Prince of Songkla stress dataset that
  [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md)
  re-analyses (66 students, **distributed as a feature table rather than raw signal**). SEED-V
  belongs here too, as the EEG-plus-eye-movement corpus that
  [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
  [luna-2025](../collection/eeg-models/luna-2025/card.md) and
  [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md)
  all report on.
- Two of those names carry a card-stated contradiction about what modality they contain. WESAD's
  chest RespiBAN "carries ECG, EDA, EMG, respiration, temperature and acceleration, and no EEG", and
  CASE "distributes no EEG" — both recorded on
  [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md),
  which names them as its EEG-plus-ECG sources. Whether DEAP carries an ECG channel is held three
  ways by three cards in two strands (science map §11).

### 2.9 Study-own recordings with no released identity

Twenty-five recordings that exist in the corpus only as the data behind one carded paper. They carry
no name, no access route and in most cases no possibility of reuse, and they are listed because a
reader counting "what recordings exist" would otherwise count them at zero when several carry the
corpus's most consequential measurements.

EEG and MEG: [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)'s
60-electrode 500 Hz recording (fully specified, and the only label-validity paper in the strand for
which that is true); [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
and [deniz-2019-modality-invariant-semantics](../collection/candidate-datasets/deniz-2019-modality-invariant-semantics/card.md)
(fMRI, both abstract-only); [snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)'s
structural-MRI cohort; [kothe-2023-nback-nirs](../collection/candidate-datasets/kothe-2023-nback-nirs/card.md)'s
43-participant dual-channel NIRS recording;
[alexander-2019-cortical-waves](../collection/eeg-models/alexander-2019-cortical-waves/card.md)'s
20-subject 151-sensor CTF MEG cohort and its three-patient ECoG trio (ECOG1–3, no EEG anywhere);
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)'s
MEG-plus-EyeLink recording at 1200 Hz;
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)'s
16 participants at 64-channel EEG plus 4-channel EOG on a BioSemi ActiveTwo at 8,192 Hz — the
highest sampling rate in the corpus.

Peripheral and mixed:
[zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) (32-channel
EEG + single-lead ECG under VR video);
[schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md)
and [schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md)
(children with temporal lobe epilepsy, and a paranoid-schizophrenia cohort);
[hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
(14 participants, EEG + skin conductance + respiration + ECG + pupil size + blinks, with body
movement and visual input held constant);
[ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
(40 analysed, eye tracking + heart rate, no EEG);
[ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md)'s
inaccessible validation cohort;
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)'s
25 participants and the Hwang et al. recording it re-runs against; and
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)'s
EEG stream, whose provenance its card records as unverifiable.

Methodological evidence cohorts:
[varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)'s
Haxby et al. data (label-inverted so chance is the true answer), its Kaggle schizophrenia-challenge
cohort of 144 subjects, and its within-subject fMRI, across-subject fMRI and MEG cohorts at roughly
212, 241 and 199 samples; and
[combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)'s
unnamed MEG and intracranial baseline recordings. Finally the **MNE sample dataset**, a test fixture
that is also a recording, shipped with [mne-python](../collection/datasets-benchmarks/mne-python/card.md)
and used as [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)'s smoke-test task.

---

## 3. Specification

The fields that decide what can ingest what. Values are given only for the 14 carded recordings,
because for the other 140 the corpus holds at most a name, a subject count and a benchmark's
preparation row. Where the source is silent the cell says so; where the source reports it and the
corpus could not read it, the cell says that instead, and §3.6 keeps the two apart.

### 3.1 Acquisition

| recording | participants | sessions / recordings | EEG channels | sampling rate |
|---|---|---|---|---|
| [strum-2018](../collection/candidate-datasets/strum-2018/card.md) | 56 as 28 pairs; the sex breakdown "13 f, 49 m" sums to 62, and the paper does not restate the count after "3 datasets were excluded" | 28 two-participant sessions, ~3.5 h each | **206** (section III); section IV says 205; 269 channels per subject in total | acquired 2048 Hz, resampled to **512 Hz** |
| [mous-2019](../collection/candidate-datasets/mous-2019/card.md) | 204, 102 reading and 102 listening | 1 per subject, plus MRI and fMRI | none — 275 MEG axial gradiometers | 1200 Hz, 300 Hz anti-aliasing cutoff |
| [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) | 29 final (35 recruited) | **3 sessions one week apart**, 65–80 min of task each | 63 EEG (64 electrodes, TP9 given to ECG); **Cz absent for participants 1–9** | 500 Hz, 24-bit, 0.05 µV, no acquisition filtering |
| [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) | 20 recruited, 1 excluded; identifiers not stable across repeats | 62 sessions of 70–70.5 min, >783 stimulation trials | 32 at 10/10 sites, 9 stimulation electrodes interleaved | 2 kHz, amplifier bandwidth 0–520 Hz |
| [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | 32 (face video for the first 22) | 40 one-minute music videos each | 32 | 512 Hz acquired; the widely distributed preprocessed version is **128 Hz** |
| [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) | 40 short-video; 17 individual + 20 in groups of four for long videos | 16 short clips, 4 long videos | 14, named | 128 Hz, 14-bit |
| [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) | 10 (6 actors, 1 director, 3 audience) | 6 rehearsals + 3 performances in one week; two ~1 h, one ~7 min | 28 EEG + 4 EOG of a 32-channel cap; **P01 has 31, CP6 removed** | 500 Hz |
| [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) | 2 professional dancers | **10 sessions over 4 months**, 7 rehearsals + 3 performances | 28 EEG + 4 EOG | 1000 Hz |
| Sleep-EDF ([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)) | not stated as a figure; 22 in the telemetry study | **197 whole-night polysomnograms** = 153 cassette + 44 telemetry; 3 cassette nights lost | 2 bipolar derivations | 100 Hz |
| [tuab](../collection/datasets-benchmarks/tuab/card.md) | **not stated** — the thesis counts files; 2,383 is AdaBrain-Bench's preparation | 2,785 training + 280 evaluation files, all >15 min | **not stated for TUAB**; 31 (parent), 22 (thesis re-derivation), 23 (benchmark) | **not stated**; parent range 250/256/400/512 Hz |
| [tuev](../collection/datasets-benchmarks/tuev/card.md) | **not stated**; 370 is AdaBrain-Bench's preparation | not stated | **not stated**; 31 (parent), 23 (benchmark), 16 bipolar (field convention) | **not stated**; 256 Hz in the benchmark |
| [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) | 10,874, 51% female, ages <1 to >90; the reported "average 51.6, stdev 55.9" is not internally coherent | 16,986 sessions, 1.56 per patient, max 37 | 31 most common EEG-only, as few as 20; overview page says 24–36 | 250 Hz (87%), 256 (8.3%), 400 (3.8%), 512 (1%) |
| [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) | 109, inferred from the manifest S001–S109; **the prose never gives a number** | 14 runs per participant | 64 on the 10-10 system | 160 Hz |
| [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) | 9 | 2 sessions on different days, 288 trials each | 22 EEG (+3 EOG), 25 in the file | 250 Hz |

### 3.2 Ingestion: derivation, coordinates, format

The two fields a coordinate-driven checkpoint needs, plus the file layer that has to carry them. The
five-way derivation split is the `candidate-datasets` ontology's §4.1 and is not restated; what is
new here is that the benchmark-strand recordings extend the same split with a sixth value —
*not stated at any level of the family*.

| recording | derivation / reference | electrode coordinates | format |
|---|---|---|---|
| [strum-2018](../collection/candidate-datasets/strum-2018/card.md) | referential by hardware (BioSemi CMS/DRL), **unstated in text**; the reference used for any released version is unstated | **absent**; the paper does not say whether coordinates were digitised or a template assumed | XDF, one time-synchronized file per two-participant session; HED 1.0-extended event ontology |
| [mous-2019](../collection/candidate-datasets/mous-2019/card.md) | n/a for gradiometers; the three peripheral channels are explicitly bipolar | n/a; three head-localiser coils, position held within 5 mm | BIDS, MEG in CTF, MRI defaced |
| [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) | referential, **Fpz** | **measured, per participant per session** — Structure 3D scan via `get_chanlocs`, so between-session displacement is quantified | BIDS on Zenodo, plus a task-order notebook and an LSL trigger list |
| [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) | referential, **CPz** reference and **AFz** ground, both named | named 10/10 sites; no per-subject digitisation | `.cnt` raw, BIDS on OpenNeuro `ds003670`, `.mat` derived |
| [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | BioSemi ActiveTwo, but the derivation of the distributed data is **not described** — recorded as unknown rather than assumed | 10-20 layout only | not stated on the card (host unreachable) |
| [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) | **unknown**; the Emotiv EPOC's fixed proprietary pair is not described in the paper and the card declines to infer | named 10-20 sites only | not stated on the card (host unreachable) |
| [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) | **common average**, with robust re-referencing through PREP; the card notes an average reference is not a per-electrode potential | template 10-20 positions in `EEG.chanlocs` | EEGLAB `.set` on FigShare |
| [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) | referential to **linked earlobes**; impedances below 50 kΩ | named 10-20 sites | raw; MATLAB and EEGLAB recommended |
| Sleep-EDF | **bipolar** — Fpz-Cz and Pz-Oz | none; bipolar labels only | EDF for the polysomnograms, EDF+ for the hypnograms |
| [tuab](../collection/datasets-benchmarks/tuab/card.md) | selection criterion only: sessions recorded with an average-reference configuration, ~45% of the parent | none | EDF |
| [tuev](../collection/datasets-benchmarks/tuev/card.md) | none stated; the field uses BIOT's 16 bipolar derivations | none | EDF / EDF+ |
| [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) | **not stated — the word "montage" does not occur** | **none at all** | EDF (overview page says EDF+), converted from Nicolet NicVue |
| [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) | not stated beyond 10-10 placement | a position figure ships with the distribution, `64_channel_sharbrough.pdf` | EDF+, one file per run, with an annotation channel |
| [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) | monopolar-referential, left mastoid reference, right mastoid ground | described as 10-20; **the 22 positions are never enumerated in text and the figure did not survive extraction** | GDF, readable with BioSig; **not on MNE-Python's supported list** |

### 3.3 Peripheral channels

Sorted by the distinction the `candidate-datasets` ontology establishes — what the source's own
analysis did with the channel — and extended across the benchmark tier. Rates are given because the
EEG-to-peripheral ratio is what any fusion architecture has to resolve, and it runs from 1:1 to
100:1 inside this table.

| recording | peripheral inventory | rate relative to EEG |
|---|---|---|
| [strum-2018](../collection/candidate-datasets/strum-2018/card.md) | 2-ch ECG, 2-ch EOG, **16-ch respiration belt**, 43-ch EMG neckband — plus force plate, head-mounted eye tracker, two cameras, microphone, instrumented controller, PhaseSpace motion capture at 480 Hz | **all on the same 24-bit BioSemi amplifier as the EEG**, therefore 1:1 and hardware-synchronous; no cross-device alignment required |
| [mous-2019](../collection/candidate-datasets/mous-2019/card.md) | bipolar vertical EOG, horizontal EOG, ECG; plus analogue audio for the auditory subjects only. No respiration, no EDA | 1:1 at 1200 Hz |
| [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) | **1 ECG channel, bought by sacrificing electrode TP9**. No EOG, no respiration | 1:1 at 500 Hz |
| [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) | bipolar lead-I ECG, bipolar horizontal EOG; single lead, so heart rate and HRV but not morphology | same amplifier; no separate rate stated |
| [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | 4 EOG + 4 EMG (zygomaticus, trapezius) + GSR + respiration + plethysmograph + temperature; the paper's two enumerations disagree about whether ECG is present | **no per-channel rates given for any peripheral channel** |
| [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) | 3-electrode ECG at 256 Hz, 12-bit; GSR (rate not stated); frontal HD and RGB-D video | 2:1 against 128 Hz EEG |
| [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) | 4 EOG from the EEG cap; Empatica E4 BVP 64 Hz, heart rate 1 Hz, EDA 4 Hz, temperature 4 Hz, wrist acceleration 32 Hz; two APDM Opal IMUs at 128 Hz. No ECG, no respiration | EOG 1:1; wristband channels 8:1 to **500:1** |
| [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) | 4 EOG; one head IMU at 128 Hz. Nothing autonomic | EOG 1:1 at 1000 Hz |
| Sleep-EDF | horizontal EOG at 100 Hz; submental chin EMG (1 Hz envelope in the cassette study, 100 Hz in telemetry); oro-nasal respiration and rectal temperature at 1 Hz, cassette records only; event marker at 1 Hz. **No ECG** | 1:1 for EOG, **100:1** for the EMG envelope and respiration |
| [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) | 3 monopolar EOG at 250 Hz, 1 mV sensitivity — **provided for artifact processing and, per the protocol, they "must not be used for classification"** | 1:1 |
| [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) family | files "typically also carry supplementary channels such as detected bursts, electrocardiography, electromyography and photic stimuli" — no counts, no rates | unstated |
| [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) | **none** | — |

Two relations the table makes visible and neither dataset ontology states.

**Hardware synchrony is rare and it is not correlated with anything else.** Four recordings put the
peripheral channels on the EEG amplifier — STRUM, MOUS, COG-BCI and GX — and the other five split
across devices at ratios from 2:1 to 500:1. No dataset in the corpus reports a *measured*
cross-participant timing error, and the only measured synchronisation numbers anywhere are
device-to-device, in [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md): 156 µs of offset
jitter single-machine on a fixed 12.20 ms offset, 145 µs networked on a 6.26 ms offset, ~0.5 ms
standard deviation between jitter-corrected EEG and EMG streams — and that card declines the
extrapolation to two capped participants itself.

**The benchmark tier's peripheral channels are present and discarded; the candidate tier's are
present and unanalysed.** Sleep-EDF is the one recording carded on both sides, and the two cards
give opposite readings of the same channels — "present, standardized, and universally discarded"
([sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)) against "usable
as signal by construction" ([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)) —
because one asks what the field did and the other what could be done.

### 3.4 Distribution: licence and access route

| recording | article licence | data licence | access route |
|---|---|---|---|
| [strum-2018](../collection/candidate-datasets/strum-2018/card.md) | IEEE copyright, `oa_status: closed` | **unknown** | **request to the authors, no published route**; the paper's footnote gives `headit.ucsd.edu`, which no longer resolves, while the abstract calls it "a new open dataset" |
| [mous-2019](../collection/candidate-datasets/mous-2019/card.md) | CC BY 4.0 | not CC — a Data Use Agreement | registration plus click-through DUA at the Donders repository |
| [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) | CC BY 4.0 | not stated in the paper | open download from Zenodo, no registration |
| [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) | CC BY 4.0 | **CC BY 4.0, stated** | open download, Zenodo and OpenNeuro `ds003670` |
| [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | not stated | not stated | **printed, signed, scanned end-user licence agreement**, then credentials |
| [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) | not stated | not stated | printed, signed, scanned end-user licence agreement |
| [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) | CC BY-NC-ND 4.0 | **not stated in the paper at all** | open download from FigShare |
| [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) | CC BY-NC-ND 4.0 | **CC BY 4.0, stated in Data Records** | open download from FigShare |
| Sleep-EDF | no dataset paper exists | Open Data Commons Attribution v1.0 | open download; browser, `wget` or `aws s3 sync --no-sign-request` |
| [tuab](../collection/datasets-benchmarks/tuab/card.md) | the naming document is a 2017 master's thesis distributed as `.docx` | **none stated** | signed form, then ssh key and `rsync -L` |
| [tuev](../collection/datasets-benchmarks/tuev/card.md) | **no descriptive document at all** | **none stated** | signed form, then ssh key and `rsync -L` |
| [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) | CC BY | **none stated**, in either the paper or the downloads page | form to `help@nedcdata.org`, approval in 24–48 h, then ssh and rsync; an 8 TB USB drive mailed to the maintainers is offered |
| [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) | n/a; the landing page is the primary source | Open Data Commons Attribution v1.0 | open download, no registration |
| [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) | CC BY (the Frontiers review) | **none formally stated** | free from `bbci.de/competition/iv/` with a citation condition |

The article licence and the data licence come apart in every recording where both are recorded — the
CC BY Temple paper over unlicensed data, the CC BY-NC-ND BOA and LiveWire articles over CC BY 4.0
data in one case and unstated data in the other, the CC BY MOUS article over a DUA. The
`candidate-datasets` and `datasets-benchmarks` ontologies each state this for their own tier; held
together it holds for all fourteen.

### 3.5 Which fields are populated, and which are not

Counting over the 14 carded recordings, and treating "the source does not state it" as unpopulated
regardless of whether a card could infer it.

| field | stated by the source | inferred, computed or preparation-sourced | not stated |
|---|---|---|---|
| access route | **14** | 0 | 0 |
| file format | 12 | 0 | 2 (both because the host was down, §3.6) |
| EEG channel count | 10 | 1 (STRUM, which states two) | 3 (the TUH family) |
| sampling rate | 11 | 0 | 3 (the TUH family) |
| participants | 10 | 1 (PhysioNet-MI, from the file manifest) | 3 (TUAB, TUEV, Sleep-EDF) |
| peripheral inventory | 10 | 0 | 4 (the TUH family unspecified, PhysioNet-MI has none) |
| article licence | 10 | 0 | 4 |
| derivation / reference | 7 | 3 (hardware-constrained, text-silent: STRUM, DEAP, AMIGOS) | 4 |
| **data licence** | **5** | 0 | **9** |
| **total hours** | **1** | 5 (four computed by their own cards; one channel-summed) | **8** |
| **electrode coordinates** | **1 measured, 1 shipped as a file** | 5 template-derivable from named sites | **7** |

**Best populated: the access route, at 14 of 14.** Every carded recording has a route recorded, even
where the route is "ask the authors" and even where the licence governing what may then be done is
absent.

**Worst populated: electrode coordinates, total hours and the data licence.** Coordinates are
*measured* in exactly one recording,
[hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md), three
times per participant, and shipped as a distribution file in exactly one more,
[physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md). Total hours is *reported* by
exactly one source, COG-BCI's "over 100 hours"; four cards compute a figure and mark it as arithmetic
(STRUM ~98 session-hours, GX ~72, DEAP ~21, Sleep-EDF ~3,450), one card explicitly declines to
compute the same Sleep-EDF figure its sibling computes, and
[tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md)'s "29.1 years" is summed
over channels and "is routinely misquoted as recording duration". Nine of fourteen have no data
licence, including all three Temple entries under most of the field's pretraining.

**Beyond the carded fourteen the fields are essentially empty.** For the eleven pretraining corpora
named in [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s Table 7 — PREST,
CHB-MIT, IIIC Seizure, HGD, TSU, M3CV, BCI-IV-1, Emobrain, SPIS, Grasp and Lift, Inria P300 — no
further specification is given on any card in the corpus. For AdaBrain-Bench's nine uncarded
evaluation sets the five fields that exist are the preparation's, not the recording's. **[boundary]**
Stated as a property of the set rather than as an enumeration of the individual entries: the
specification fields are populated in inverse proportion to how much of the field's pretraining and
evaluation rests on the recording.

### 3.6 Reported-but-unread against never-reported

The distinction the practice brief requires to survive, applied to the data layer specifically. The
two have opposite implications: the first is a retrieval problem, the second is not.

**Reported by the source and unread here — re-retrieval would resolve it.**

- [tuab](../collection/datasets-benchmarks/tuab/card.md) and
  [tuev](../collection/datasets-benchmarks/tuev/card.md) — the release's `_AAREADME` sits behind the
  registration wall and probed public URLs returned 404. This is where the partition's
  patient-disjointness would be recorded, which makes it the data layer's most consequential
  inaccessible item.
- [tuev](../collection/datasets-benchmarks/tuev/card.md) — the annotation guidelines are published
  as a separate consortium document that was not retrieved, so rater criteria and inter-rater
  agreement are unrecorded.
- [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) — the signed access
  form's text, which any redistribution question turns on; and the explicit date range, which
  "appears only in a lost figure".
- Sleep-EDF — `SC-subjects.xls` and `ST-subjects.xls` ship with the data and were not retrieved, so
  the exact participant count is unavailable to both cards.
- [deap-2012](../collection/candidate-datasets/deap-2012/card.md) and
  [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) — `eecs.qmul.ac.uk`, the host
  serving both project pages, returned HTTP 503 throughout retrieval over both HTTP and HTTPS. The
  DEAP case is the sharp one: the paper contradicts itself about whether an ECG channel exists and
  the object that would settle it, the distributed channel list, is the inaccessible one.
- [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) — the
  figure showing the 22 electrode positions did not survive extraction and the positions are never
  enumerated in text.
- [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) and
  [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) — the per-dataset tables that
  would name the rest of the 54 and the 18 are in supplementary material and an appendix.
- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is the inverse case and the one
  that matters most here: the complete six-page paper *was* obtained through institutional access on
  2026-08-01 and every fixed field is read from section III. Its PDF is inaccessible **to
  redistribution**, under IEEE copyright, and cached locally uncommitted. Its specification is not
  inaccessible at all.

**Never reported by the source — re-retrieval of the same document would not help.**

- [tuev](../collection/datasets-benchmarks/tuev/card.md) — participants, channels, sampling rate,
  hours, class balance and the partition, all of them, with no descriptive document existing.
- [tuab](../collection/datasets-benchmarks/tuab/card.md) — no subject count, no total hours, and
  patient-disjointness not asserted in the document the corpus names as its description.
- [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) — no montage, no
  recording-hours total, no bit depth in the paper.
- [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) — no total hours, no
  participant count in prose, and no errata or exclusion list for the subjects the BCI literature
  routinely drops.
- Sleep-EDF — no participant count, no total hours, no per-recording durations.
- [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) — no total hours and no
  per-session duration, so the dataset's size cannot be stated without downloading it.
- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — the reference used for any
  released version, the electrode coordinates, the usable session count after exclusions, and any
  corpus total.
- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md),
  [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md),
  [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) and
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — no measured cross-participant
  synchronisation precision, in any of the four multi-person recordings.

---

## 4. Roles

### 4.1 Recordings holding more than one role

The set the whole document is keyed to accommodate. Each row is one recording; each column is a role;
the source of the role attribution is given because in most cases it is not the checkpoint's own
paper (§4.2).

| recording | pretraining substrate | evaluation benchmark | candidate corpus | control / probe substrate |
|---|---|---|---|---|
| [tuab](../collection/datasets-benchmarks/tuab/card.md) | BIOT, CBraMod | all four suites; BIOT, EEGPT, LaBraM, CBraMod, FEMBA, LUNA, BrainOmni first-party | — | Banville's SSL comparison; "TUAB is in-domain" |
| [tuev](../collection/datasets-benchmarks/tuev/card.md) | BIOT, CBraMod | AdaBrain-Bench, OmniEEG-Bench; LaBraM, BIOT, EEGPT, CBraMod, BrainOmni, REVE first-party | — | CBraMod's held-out-corpus re-pretraining check |
| [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) | EEGPT | REVE, CBraMod, LaBraM, BIOT, BENDR, BrainOmni, Lee; MOABB's largest; a Brain4FMs task | — | REVE's +10.7-point pretraining ablation, the cleanest in the corpus |
| Sleep-EDF | BIOT indirectly, via SHHS | AdaBrain-Bench, OmniEEG-Bench, Brain4FMs, NeuralBench; BENDR, EEGPT, Lee, Zare | [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) | the cheapest open bipolar substrate on which the midpoint approximation could be probed |
| CHB-MIT | BIOT | Brain4FMs, BrainWave, CBraMod's FLOP measurement | — | Zare's one clean controlled positive |
| SEED | EEGPT; "SEED series" for LaBraM | AdaBrain-Bench, EEGConformer, liu-2022 | — | — |
| SHHS | BIOT | AdaBrain-Bench's subject-count ablation | — | — |
| Siena | LUNA (141.0 h) | AdaBrain-Bench; LaBraM lists it as pretraining | — | Brookshire's Experiment 2 |
| TUEG | BENDR, CBraMod, FEMBA, LUNA, LaBraM, REVE | never | — | — |
| [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) | none reports it; LaBraM lists BCI-IV-1 | AdaBrain-Bench, Brain4FMs, MOABB, EEGConformer, EEGPT, BENDR | — | the one withheld-test-label regime in the corpus, and its stated expiry |
| DEAP | — | OmniEEG-Bench as DEAP-arousal; ding-2025, li-2023, liu-2022 | [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | — |
| OpenNeuro (archive) | REVE, 10,194 h | a NeuralBench data source | [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) as the access reference point | host of `ds004504` for Zare's identity probe |
| MOABB (aggregator) | REVE, 384 h | NeuralBench reaches motor-imagery and P300 through it | — | — |
| VitalDB | PaPaGei | PaPaGei's ICU-admission and operation-type tasks | — | the entire data source for wang-2025 |
| MIMIC-IV-ECG | ECG-FM | ECG-FM's released public benchmark | — | — |

Two role patterns are singletons and worth naming as such. **UHN-ECG is the corpus's only reserved
holdout**, excluded from pretraining at pretraining time specifically "to serve as a cross-dataset
generalisation test"
([mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md)); the nearest
EEG analogue is CBraMod's re-pretraining with TUEV excluded, which is a check run after the fact
rather than a corpus reserved in advance. And **TUEG is the only large recording in the corpus that
is pretraining substrate and nothing else** — its two carded subsets absorb the evaluation role
entirely.

### 4.2 The role attribution is usually third-party, and traces to two tables

Nearly every checkpoint-to-corpus fact above traces to
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s Table 7 or
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)'s Table 1 rather than to the
checkpoint's own paper. The `datasets-benchmarks` ontology registers this as its single-sourcing
finding and it is not restated; the consequence *for the role map specifically* is that the
pretraining column of §4.1 is mostly one document read many times, and that document is internally
inconsistent about exactly the fields it propagates — EEGPT at 198 hours in Table 7 against 246 in
the body, CBraMod at 9,246 against ~27,000, LaBraM at 2,535 h and 136 channels against ~2,500 h and
137. A reader who sees the same pretraining assignment on five cards is reading one source five
times.

Three checkpoints make the role map unresolvable rather than merely single-sourced.
[brainwave](../collection/eeg-models/brainwave/card.md) reports its corpus as a total and a modality
split only, so overlap with its evaluation sets cannot be audited;
[reve-2025](../collection/eeg-models/reve-2025/card.md) accounts 92 datasets by archive; and
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) does not state whether any
of its ten checkpoints was pretrained on any of its 54 evaluation datasets. Each card states this
about itself.

---

## 5. Concentration

Structure, stated as counts rather than as a complaint.

### 5.1 What the pretraining rests on

Of the nine checkpoints in the corpus that state a pretraining corpus at all, **six rest on Temple
University Hospital data**: [bendr-2021](../collection/eeg-models/bendr-2021/card.md),
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
[femba-2025](../collection/eeg-models/femba-2025/card.md),
[luna-2025](../collection/eeg-models/luna-2025/card.md) (99.4% of its hours),
[labram-2024](../collection/eeg-models/labram-2024/card.md) (its two largest constituents) and
[reve-2025](../collection/eeg-models/reve-2025/card.md) (26,847 of 61,415 hours). BIOT rests on TUAB
and TUEV plus a proprietary corpus.
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) is the explicit exception, with 22
sources and no TUEG. [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) has
zero by design.

That concentration is on a single clinical site in a single country, where "'clinical-grade' data is
inherently more variable with respect to parameters such as electrode location, clinical
environment, equipment, and noise", 75% of the parent archive's records are classified abnormal, and
no montage is stated at any level
([tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md)).

The four archives that supply the field's hours are TUH, PhysioNet, OpenNeuro and MOABB, in that
order of magnitude, and they are known in that shape from exactly one source: REVE's own accounting.
Two of them supply along different axes, and the only tested scaling analysis in the corpus
separates them — [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) finds the
*number of pretraining datasets* significantly associated with better average rank (median ρ = −0.27,
p = 1.1×10⁻⁷) against training hours at −0.08, with TUH being the source of hours and OpenNeuro the
source of dataset count.

### 5.2 What the evaluation rests on

TUAB and TUEV are between them reported on by twelve checkpoints across four suites. AdaBrain-Bench's
full per-dataset table has five rows and three of them are TUH-family or Sleep-EDF; the two smallest
are EEGMAT at 1,080 samples and BCI-IV-2a at 5,184 (which is arithmetic, 9 × 2 × 288, not a stated
figure). Of the four suites, only [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)
carries a dummy and a chance baseline as reported rows, and only
[moabb](../collection/datasets-benchmarks/moabb/card.md) runs a cross-dataset inference procedure —
and MOABB covers no pretrained models and one paradigm.

Three properties of the evaluation layer's shape follow from §1 and are worth holding together.
Coverage is *broad on paper*: 54, 94, 22 and 13 datasets across the four suites. It is *narrow in
what is checkable*: the 54 and the 94 are not enumerable from the cards, so the recordings behind
most of the field's published leaderboard rows have no identity in this corpus. And it is *shallow in
what is comparable*: four suites reporting on LaBraM are four different quantities, because the four
differ on the holdout boundary, the adaptation regime, the metric and the comparator set.

### 5.3 The only-named tail

140 of 154 recordings appear solely inside another card. That tail is not uniform. It contains the
substrate under BrainOmni's entire pretraining run (18 named sources, none specified beyond a name),
the substrate under BIOT's (PREST, proprietary and un-inspectable), eight of Brain4FMs's eighteen
datasets and forty-eight of OmniEEG-Bench's fifty-four (not named at all), and twenty-five study-own
cohorts that will never have a release. The recordings with the fullest specification in the corpus
— the nine candidate-tier acquisitions of §2.6 — are the ones no model has touched.

---

## 6. A register of level errors

Not a contradiction register: the per-strand registers already hold those, and the three kinds of
contradiction are kept apart there. This is the specific failure the §0.2 vocabulary exists to name —
**a figure that is a property of one level circulating as a property of another** — collected across
families because it is invisible from inside any one of them. Each row names where it is already
recorded, so nothing is double-counted.

| the figure | the level it actually belongs to | the level it is read at | where registered |
|---|---|---|---|
| TUAB 2,383 subjects / 409,083 samples | AdaBrain-Bench's preparation | the corpus's own scale | [tuab](../collection/datasets-benchmarks/tuab/card.md) calls it "a benchmark artefact" |
| TUEV 370 subjects / 112,237 samples | AdaBrain-Bench's preparation | the corpus's own scale | [tuev](../collection/datasets-benchmarks/tuev/card.md) |
| Sleep-EDF 78 subjects / 414,961 windows | AdaBrain-Bench's preparation | the dataset's own scale, against 197 recordings | [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) |
| BCI-IV-2a 5,184 samples | arithmetic over a preparation | a reported figure | [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) |
| TUAB "22 channels" | a re-derivation the thesis's author applied | the recording montage | [tuab](../collection/datasets-benchmarks/tuab/card.md) |
| TUEV "16 channels" | BIOT's bipolar derivation scheme | an electrode count | [tuev](../collection/datasets-benchmarks/tuev/card.md), which states the distinction the corpus documentation never makes |
| TUEG "29.1 years" | duration summed over channels | recording duration | [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md): "routinely misquoted" |
| DEAP 128 Hz | the distributed preprocessed release | the acquisition, which is 512 Hz | [deap-2012](../collection/candidate-datasets/deap-2012/card.md) |
| STRUM 512 Hz | the release | the acquisition, which is 2048 Hz | [strum-2018](../collection/candidate-datasets/strum-2018/card.md) |
| Sleep-EDF "Version 1.0.0, Oct 2013" | a stale release string | the content, expanded in March 2018 | [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) |
| TUH v0.6.0 / v0.6.3 / v2.0.2 | three releases | one archive; "none of the counts above should be assumed current" | [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) |
| Sleep-EDF's five AASM classes | a benchmark's label space | the release's eight-label R&K hypnogram, with the mapping stated by neither source | [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) |
| PhysioNet-MI's T1 / T2 | resolvable only against the run index | a self-contained annotation | [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) |
| BIOT's 18 fixed channels | AdaBrain-Bench's account of the checkpoint | the checkpoint's own 16 | science map §11; cross-strand, not a corpus defect |

Four preparations in the corpus change the *derivation class* of the recording they prepare, which is
the most consequential form of the same error because it is the one no leaderboard shows.
[reve-2025](../collection/eeg-models/reve-2025/card.md) gives each of TUEV's 16 bipolar derivations
"the average position of each bipolar montage", a single midpoint;
[bendr-2021](../collection/eeg-models/bendr-2021/card.md) "simply maps" Sleep-EDF's FPz-Cz and Pz-Oz
to FPz and Pz, discarding the second electrode of each pair;
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)'s harmonised
pipeline applies a common average reference to every model in its panel, including models pretrained
on referential data; and BENDR's MMI preparation uses 19 of PhysioNet-MI's 64 channels. None of the
four is ablated anywhere.

---

## 7. Where STRUM sits

Specification, dimension by dimension, against the distributions established above. No dimension
below carries a verdict, and the question of whether the position is favourable is Phase 4's.
STRUM's fields are now read in full from the primary source
([strum-2018](../collection/candidate-datasets/strum-2018/card.md), section III, obtained through
institutional access on 2026-08-01), so what follows is specification rather than inference except
where marked.

- **Participants — 56, recorded as 28 pairs.** Above every other multi-person EEG recording in the
  corpus by an order of magnitude (LiveWire 2, BOA 10, AMIGOS 20 in groups) and mid-range against the
  single-participant candidate tier (MOUS 204, AMIGOS 40, DEAP 32, COG-BCI 29, GX 20). Three orders
  of magnitude below the TUH archive at 10,874. The card records that the sex breakdown sums to 62
  rather than 56 and that the surviving count after three excluded sessions is not restated.
- **Channels — 206 EEG, 269 per subject, 538 across the pair.** The densest EEG layout in the
  corpus. The next densest are Grosse-Wentrup 2009 at 128 in MOABB's table, Chisco at 125 in
  Brain4FMs, and Things-EEG at 63. Against the checkpoints: BENDR, BIOT and CBraMod index spatial
  identity by channel name and, per the card, "cannot ingest a 206-channel set without channel
  selection or interpolation"; REVE's pretraining corpus spans 396 unique electrode names, so the
  count is inside that vocabulary while the layout is not one it saw; LaBraM's spatial embedding is
  recorded at 136 or 137 channels depending on which card of AdaBrain-Bench is read.
- **Sampling rate — acquired at 2048 Hz, released at 512 Hz.** Inside the corpus's range, which runs
  from Sleep-EDF's 100 Hz to Rotaru's 8,192 Hz, and above every checkpoint's expected input, all of
  which resample.
- **Derivation — referential by hardware, unstated in text.** The class shared with
  [deap-2012](../collection/candidate-datasets/deap-2012/card.md) and, one degree looser,
  [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md). Not bipolar, so the midpoint
  approximation of §6 does not apply. "The paper does not name the reference used for any released
  version of the data, so what re-referencing has already been applied is unknown."
- **Coordinates — absent.** One of seven carded recordings with none, and the one where the absence
  compounds with the channel count: the checkpoints that could ingest an arbitrary layout are exactly
  the ones that need a coordinate per channel, and a template for a non-standard high-density cap
  may not exist. The one recording in the corpus with measured coordinates is COG-BCI, at 63
  channels.
- **Peripheral inventory — 2-channel ECG, 2-channel EOG, a 16-channel respiration belt and a
  43-channel EMG neckband, all on the same 24-bit BioSemi amplifier as the EEG.** The only recording
  in the corpus carrying all three of the project's named peripheral modalities. MOUS carries vEOG,
  hEOG and ECG at 1200 Hz, "exactly the project's target set minus respiration"; Sleep-EDF carries
  EOG, EMG, respiration and temperature but no ECG and at 1 Hz for three of the four; COG-BCI carries
  one ECG channel bought by sacrificing an electrode. Hardware synchrony puts STRUM in a set of four
  (with MOUS, COG-BCI and GX) where no cross-device alignment is required at all. Against that, no
  first-party analysis of those channels is on record: the paper's own analysis is of a slice.
- **Simultaneity — 2 at once, at 206 channels.** One of four multi-person EEG recordings in the
  corpus, and the only one that is both dense and multi-person. Like the other three, it reports no
  measured cross-participant timing error, though it writes both participants into one LSL XDF file
  — the corpus's only container holding two participants' data in one file.
- **Format — XDF.** Read by the LSL toolchain
  ([lsl-2024](../collection/candidate-datasets/lsl-2024/card.md)); not BIDS, not EDF, not EEGLAB.
  Events are HED-tagged under an ontology extended from HED 1.0, which is the annotation standard
  [nemar-2022](../collection/candidate-datasets/nemar-2022/card.md) argues for and identifies as
  "precisely the gap in which a label like 'spoken' versus 'written' gets defined inconsistently
  across datasets".
- **Licence and access — data licence unknown, access by request to the authors with no published
  route.** The highest-friction position on the candidate strand's ladder, below the printed-and-signed
  EULAs of DEAP and AMIGOS and the click-through DUA of MOUS. The abstract calls it "a new open
  dataset"; the community index records "not available on headit.ucsd .. contact authors"; no
  registry sweep located a hosted copy.
- **Scale in hours — ~3.5 hours per session reported, ~98 session-hours by arithmetic**, marked as
  arithmetic by its own card. No corpus total is reported. Against REVE's 61,415 pretraining hours
  and TUEG's 21,000–27,000, and against COG-BCI's "over 100 hours", the only reported total in the
  candidate tier.
- **Role — candidate fine-tuning corpus, and nothing else.** STRUM is named in essentially every card
  in the corpus as the target the collection is written against, and holds no role in any model's or
  suite's actual pipeline. It has 2 citations, agreeing across Semantic Scholar and OpenAlex, and
  neither citing work trains or evaluates a model on it; one of the two is
  [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md). Its card reads the citation count
  as "a fact about visibility, not about quality", consistent both with a dataset nobody modelled and
  with one nobody could obtain.
- **The design property that has no analogue anywhere else in the data layer** — the side tasks form
  an explicit factorial, "broken down by stimulus modality (auditory/visual) and stimulus kind
  (verbal/non-verbal), yielding a matrix of four tasks, plus one additional task with natural visual
  stimuli", manipulated within subject. The `candidate-datasets` ontology's §3 works out what the
  factorial affords and that reasoning is not restated; what belongs here is only the specification
  fact that no other recording in the corpus crosses those two factors, and that MOUS — the one
  recording carrying the same contrast at scale — manipulates it *between* subjects, 102 readers
  against 102 listeners.

---

## 8. Coverage

Every recording in the census, its primary node, and everywhere else it appears. `C` marks a carded
recording; everything unmarked is named only. Rows are grouped as in §2; within a group, ordering
carries no ranking.

| recording | C | primary node | also in |
|---|:-:|---|---|
| TUEG / TUH EEG Corpus | C | §2.1 archive and acquisition | §2.0, §3.1–§3.6, §4.1, §5.1, §6 |
| TUAB | C | §2.1 dual-role Temple subset | §3.1–§3.6, §4.1, §5.2, §6 |
| TUEV | C | §2.1 dual-role Temple subset | §3.1–§3.6, §4.1, §5.2, §6 |
| TUAR, TUEP, TUSE, TUSL, TUSZ | | §2.1 pretraining-only Temple subsets | §3.5, §5.1 |
| PhysioNet-MI | C | §2.2 four roles on one recording | §2.4, §3.1–§3.6, §4.1, §6 |
| Sleep-EDF Expanded | C | §2.2 carded in both dataset strands | §0.3, §3.1–§3.6, §4.1, §5.2, §6 |
| PhysioNet/CinC 2018 (PC18) | | §2.2 substrate and evaluation in one paper | §5.1 |
| PhysioNet 2021 (CinC ECG) | | §2.2 | §2.8 |
| PhysioP300 | | §2.2 | §2.7 |
| `ds003670` | | §2.3 a *release* of a carded recording, not a recording of its own — listed so it is not counted twice | §3.2, §3.4 |
| `ds004504` | | §2.3 identity-probe substrate | §2.7 |
| Cho 2017, Shin 2017, BNCI2014-002, BNCI2014-004, BNCI2015-001, BNCI2015-004, AlexandreMotorImagery, Yi 2014, Zhou 2016, Grosse-Wentrup 2009 | | §2.4 MOABB's Table I | §5.1, §7 (Grosse-Wentrup, as the next-densest layout) |
| PREST | | §2.5 proprietary pretraining substrate | §2.7, §3.5, §5.1, §5.3 |
| Cardiology (ECG) corpus | | §2.5 | §2.8 |
| eVox Alzheimer's cohort | | §2.5 proprietary control substrate | §2.9 |
| Sirca's 54-subject MI dataset | | §2.5 unnamed, so overlap uncheckable | §4.2 |
| STRUM | C | §7 where STRUM sits | §1, §2.6, §3.1–§3.6, §4.1 (as candidate only), §6 |
| MOUS | C | §2.6 candidate tier | §3.1–§3.4, §7 |
| COG-BCI (Hinss) | C | §3.2 the only measured coordinates | §2.6, §3.1, §3.3–§3.6, §7 |
| GX (Gebodh) | C | §3.3 named reference, ECG and EOG as signal | §2.3, §2.6, §3.1–§3.6 |
| DEAP | C | §2.6 candidate tier | §2.7, §2.8, §3.1–§3.6, §4.1, §6 |
| AMIGOS | C | §2.6 four simultaneous participants | §3.1–§3.6, §7 |
| BOA actors | C | §2.6 three simultaneous participants | §3.1–§3.6 |
| LiveWire | C | §2.6 two simultaneous participants | §3.1–§3.6 |
| SEED, SEED-IV, EEGMAT, SEED-VIG, SHU, Things-EEG, Siena, HMC, SHHS | | §2.7 AdaBrain-Bench's evaluation table | §3.5, §4.1 (SEED, SHHS, Siena), §5.2, §6 |
| CHB-MIT | | §2.7 four roles, no card | §4.1, §5.1 |
| IIIC Seizure, HGD, TSU, M3CV, BCI-IV-1, Emobrain, SPIS, Grasp and Lift, Inria P300, ESI NeuroScan | | §2.7 pretraining substrate, unspecified | §3.5, §5.1 |
| HBN-EEG, HBN EO/EC, SRM, RestCog, PEARL-Neuro, Features-EEG, MusicEEG, HFO, Go-Nogo, Awakening, Kymata-SOTO, CC700, OMEGA, MEG-MASC, SMN4Lang, THINGS-MEG, Gloups-MEG, PerceiveImagine | | §2.7 BrainOmni's sources | §5.1, §5.3 |
| AD65, ASD74, MDD, SomatoMotor | | §2.7 BrainOmni's downstream sets | — |
| MAYO, FNUSA, Dep-BDI, MDD-64, SD-28, UCSD, Chisco-R, Chisco-I | | §2.7 Brain4FMs's named ten | §5.3, §7 (Chisco, as a density comparator) |
| PD31, Broderick-Cocktail-party, Broderick-reverse, Monitoring-Errp | | §2.7 OmniEEG-Bench's named six | §5.3 |
| FACED, BCI-IV-2b, KaggleERN, ISRUC, CAUEEG | | §2.7 one consumer each | §2.3 (CAUEEG, with ds004504) |
| Korea University ERP, Lee's working-memory dataset, NeuroLM's "Workload" | | §2.7 named without specification | — |
| ADFTD, SleepDep, Stress-DASS, Komarov stress dataset | | §2.7 the FMScope cells | — |
| BCI-IV-2a | C | §2.4 and §2.7 | §3.1–§3.6, §4.1, §5.2, §6 |
| Kamrud's driver fatigue, confused students, alcoholism, PTSD, schizophrenia | | §2.7 split-cost demonstration corpora | §2.9 |
| MIMIC-IV-ECG, UHN-ECG | | §2.8 ECG at scale | §4.1 |
| VitalDB, MIMIC-III waveform matched subset, MESA, PPG-BP, nuMom2B, SDB, VV | | §2.8 PPG at scale | §4.1 (VitalDB) |
| WESAD, CASE, DREAMER, MAHNOB-HCI, ASCERTAIN, CLAS, MAUS, WAUC, COLET, CL-Drive, Prince of Songkla stress dataset, SEED-V | | §2.8 EEG-plus-peripheral, named only | §5.3 |
| Simanova 2010 EEG; Simanova 2012 fMRI; Deniz 2019 fMRI; Snoek 2019 MRI; Kothe 2023 NIRS; Alexander 2019 MEG; Alexander 2019 ECoG; Mostert 2018 MEG; Rotaru 2024 EEG+EOG; Zeng EEG+ECG; Schiecke TLE; Schiecke schizophrenia; Hogervorst 2014; Ahmad 2020; Ha validation cohort; Azad 2025; Hwang et al.; Kumar's EEG stream; Haxby et al.; Kaggle schizophrenia challenge; Varoquaux's three cohorts; Combrisson's baselines; MNE sample dataset | | §2.9 study-own, no released identity | §3.6 (the abstract-only three); §7 (Rotaru, as the highest sampling rate) |
| OpenNeuro (archive) | C | §2.0 and §2.3 | §4.1, §5.1 |
| NEMAR | C | §2.0 gateway | §2.3, §7 |
| MOABB (aggregator) | C | §2.0 and §2.4 | §4.1, §5.1, §5.2 |
| PhysioNet (archive) | | §2.0 | §2.2, §5.1 |

The table's rows sum to §1's census of 154 — 14 carded and 140 named only — plus two kinds of row
that the counting rule excludes and that are listed anyway so a reader can see they were considered:
`ds003670`, which is a release of an already-counted recording, and the four archive and aggregator
rows at the foot, which are containers rather than recordings.

Every recording appears in exactly one primary node. Fourteen appear in six nodes or more, and all
fourteen are carded; the 140 only-named recordings appear in one to three, which is the intended
shape rather than a placement failure — for most of them the corpus holds a name, a consumer and
nothing else, so most facets have no value to record. No recording failed to fit a node.
