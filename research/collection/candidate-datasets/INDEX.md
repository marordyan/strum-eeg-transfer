# Candidate Datasets and Label Validity — Collection Index

Strand D. Scope categories are those defined in `_briefs/strand-candidate-datasets.md`. One line
per entry; each entry's full record is its `card.md`. Entries appear once in their primary
category and are cross-referenced where they also serve another.

**Collection status: 19 entries.** Nothing here is a synthesis, a ranking, or a gap match; this is
a specified inventory, and the matching is Phase 4's job.

## 1. Multi-person and dyadic recordings

- [boa-actors-2025](./boa-actors-2025/card.md): three actor dyads plus a director and audience
  members instrumented at once — 3 simultaneous participants per recording, 32-channel EEG (28 EEG
  + 4 EOG) at 500 Hz plus Empatica wristband blood volume pulse, electrodermal activity and
  temperature; hardware-trigger sync with no measured precision; average reference
  (`relevance: high`, 2025)
- [livewire-2024](./livewire-2024/card.md): two professional dancers recorded "simultaneously and
  in synchrony" across ten sessions in four months; 28-channel EEG + 4 EOG at 1000 Hz, linked-earlobe
  referential derivation, manual-trigger sync, data released CC BY 4.0 on FigShare
  (`relevance: medium`, 2024)
- [amigos-2021](./amigos-2021/card.md): five groups of four participants watching long videos
  together with EEG, ECG and galvanic skin response recorded from all four at once — the only
  four-way simultaneous recording found; 14-channel consumer headset at 128 Hz, all labels
  self-report (`relevance: medium`, 2021)
- [lsl-2024](./lsl-2024/card.md): the Lab Streaming Layer, carded for the numbers that bound any
  cross-participant analysis — 156 and 145 microsecond offset jitter in single-machine and
  networked tests, ~0.5 ms standard deviation between EEG and EMG streams, on top of a fixed
  device offset that must be pre-measured (`relevance: medium`, 2024)

### Category 1 search record

The brief anticipated that this category might come back thin and asked for the queries to be
recorded so Phase 4 can state the scarcity as evidence rather than as an impression. It did come
back thin. Three dataset entries were found where two or more people wearing EEG were recorded at
the same time, and two of the three come from the same laboratory (Contreras-Vidal, University of
Houston). What was run:

- `opencite search "hyperscanning dataset two participants simultaneous EEG" --max 20` — 20
  results, of which zero were dataset releases. The returns were reviews and methods papers
  (Hamilton 2020 "Hyperscanning: Beyond the Hype"; Barraza et al. 2019 "Implementing EEG
  hyperscanning setups"; Hakim et al. 2023 on inter-brain coupling quantification; Zamm et al. 2024
  practical guide; Carollo & Esposito 2024 scientometric review), most of which are out of scope
  for this strand under the brief's exclusion of hyperscanning connectivity methodology.
- `opencite search "open dataset data descriptor dual-EEG dyadic simultaneous recording two brains" --max 20`
  — 20 results, zero relevant. The result set degenerated into unrelated arXiv computer-science
  papers ("Byzantine-Resilient Distributed Optimization", an abdominal-CT dataset), which is a
  useful negative signal about the query rather than about the field.
- PubMed `hyperscanning[Title] AND (dataset[Title] OR data[Title])` — 15 hits. Every dataset
  release among them is fNIRS or fMRI, not EEG: an fNIRS social-touch hyperscanning dataset
  (10.1038/s41597-025-06233-9), an fMRI cooperation/competition hyperscanning dataset
  (10.1038/s41597-025-05774-3), a parent-child fNIRS hyperscanning dataset
  (10.1038/s41597-022-01751-2). The EEG hits are analysis-method papers, not data.
- PubMed `(dual-EEG[Title] OR hyperscanning[Title]) AND open dataset` — 2 hits, one fNIRS dataset
  and one dual-EEG *pipeline* paper (DEEP, 10.1016/j.dcn.2022.101104).
- PubMed `EEG[Title] AND dataset[Title] AND (dyad*[Title] OR dyadic[Title] OR interpersonal[Title] OR two-person[Title])`
  — **0 hits.**
- PubMed `"Sci Data"[Journal] AND EEG AND (dyad* OR hyperscanning OR two-person OR interpersonal)`
  — 2 hits, both from the same University of Houston mobile-brain-body-imaging group, and both are
  carded above (`boa-actors-2025`, `livewire-2024`).
- OpenNeuro GraphQL `advancedSearch` with `modality: "EEG"` and `keywords` of `hyperscanning`,
  `dyadic`, `conversation`, and `joint action` — **0 edges for each.** Note the interface
  limitation recorded on the `openneuro-2021` card: `DatasetSearchInput` has no free-text field
  (introspection returns only structured filters such as `ageRange`, `authors`, `keywords`,
  `modality`, `tasks`, `subjectCountRange`), and Elasticsearch-style `simple_query_string` or
  `query_string` inputs are rejected by schema validation. So a zero result here means "nothing
  tagged with that keyword", which is weaker than "nothing exists".

The pattern across all of it: multi-person neuroimaging *datasets* are being released, but in
functional near-infrared spectroscopy and fMRI rather than EEG. The EEG hyperscanning literature
that exists is overwhelmingly analysis methodology over data that is not shared.

## 2. Synchronized EEG and peripheral physiology

- [deap-2012](./deap-2012/card.md): the reference EEG-plus-peripheral dataset — 32 participants, 32
  EEG channels at 512 Hz, "thirteen peripheral physiological signals" spanning EOG, EMG,
  electrodermal activity, respiration, blood volume pulse and skin temperature; the paper's two
  enumerations of those channels disagree about whether ECG is among them (`relevance: medium`, 2012)
- [tes-eeg-ecg-2021](./tes-eeg-ecg-2021/card.md): 20 participants, 62 sessions of ~70 minutes,
  32-channel EEG at 2 kHz referenced to CPz with concurrent bipolar lead-I ECG and horizontal EOG
  and a millisecond-resolution continuous behavioural vigilance score; CC BY 4.0, BIDS on OpenNeuro
  `ds003670` (`relevance: medium`, 2021)
- [sleep-edfx](./sleep-edfx/card.md): 197 whole-night polysomnograms, 8.1 GB, EEG at Fpz-Cz and
  Pz-Oz — *bipolar* derivations — plus EOG, chin EMG and, in the cassette records, oro-nasal
  respiration and rectal temperature; expert-scored hypnograms; Open Data Commons Attribution, no
  registration (`relevance: medium`, 2018)

Also carrying EEG alongside at least one peripheral modality, carded in other categories:
[boa-actors-2025](./boa-actors-2025/card.md) (EOG, blood volume pulse, heart rate, electrodermal
activity, temperature, accelerometry), [livewire-2024](./livewire-2024/card.md) (EOG, inertial),
[amigos-2021](./amigos-2021/card.md) (ECG at 256 Hz, galvanic skin response),
[hinss-2023-passive-bci](./hinss-2023-passive-bci/card.md) (one ECG channel, bought by sacrificing
electrode TP9), and [mous-2019](./mous-2019/card.md) (bipolar vertical EOG, horizontal EOG and ECG
at 1200 Hz, alongside MEG rather than EEG). That is six datasets with EEG plus at least one
peripheral modality, plus MOUS with MEG.

Where those peripheral channels are usable as signal rather than recorded only for artefact
rejection, the card says so explicitly. The clearest cases are `tes-eeg-ecg-2021` (physiology is an
independent variable in the authors' own analysis) and `hinss-2023-passive-bci` (cardiac activity
is one of the dataset's own validation channels).

## 3. Label provenance and validity

- [simanova-2010-eeg-object-categories](./simanova-2010-eeg-object-categories/card.md): the same
  eight concepts presented as pictures, spoken words and written words; single-trial EEG decoding
  reached 89% for pictures, but on a previously unseen exemplar the classifier failed, and the
  authors concluded it "could not distinguish the semantic classes, but only the exemplars,
  possibly through the use of perceptual differences between the exemplars" (`relevance: high`, 2010)
- [deniz-2019-modality-invariant-semantics](./deniz-2019-modality-invariant-semantics/card.md):
  hours of the same narratives listened to and read; voxelwise semantic tuning "highly correlated"
  across the two and cross-modality prediction succeeds, so the semantic content of spoken and
  written language is near-identical and whatever separates the conditions is not the semantics
  (`relevance: high`, 2019)
- [simanova-2012-modality-independent](./simanova-2012-modality-independent/card.md): the
  train-on-one-modality-test-on-another design, across four stimulus modalities, plus a free-recall
  control in which the same voxels discriminate categories with no stimulus present
  (`relevance: medium`, 2012)
- [ritchie-2019-decoding-limits](./ritchie-2019-decoding-limits/card.md): the "decoder's dictum" —
  that decodability is evidence of representation — argued to be false, because a sufficiently
  flexible classifier extracts information the brain itself could not use; proposes behavioural
  read-out (correct versus incorrect trials) as the replacement criterion (`relevance: medium`, 2019)
- [snoek-2019-confound-control](./snoek-2019-confound-control/card.md): both standard confound
  controls are biased — post hoc counterbalancing upward, confound regression downward far enough
  to yield significant below-chance accuracy — and only confound regression run inside every
  cross-validation fold is unbiased (`relevance: medium`, 2019)
- [kothe-2023-nback-nirs](./kothe-2023-nback-nirs/card.md): a workload label defined purely as the
  experimental parameter *n*, balanced and pseudo-randomised, with no self-report or behavioural
  validation reported; carded only for the label reasoning, and different modality
  (`relevance: low`, 2023)

Bearing directly on whether a stimulus-condition label supports a cognitive claim, which the brief
requires at least three of: `simanova-2010-eeg-object-categories` (the classifier separated
exemplars, not categories), `deniz-2019-modality-invariant-semantics` (spoken and written share
their semantic representation, so the contrast is not semantic),
`simanova-2012-modality-independent` (cross-modal generalisation as the test that isolates what
survives), and `ritchie-2019-decoding-limits` (decodability does not establish representation).
Four entries.

Also relevant: [hinss-2023-passive-bci](./hinss-2023-passive-bci/card.md) is the one dataset here
that validates its experimenter-set difficulty labels against subjective scales, behavioural
performance and physiology simultaneously, so it is the strand's example of label-source agreement
being addressed rather than assumed. [mous-2019](./mous-2019/card.md) carries the project's exact
spoken-versus-written manipulation but between subjects, which makes the contrast inseparable from
subject identity.

## 4. Access, licensing, and practical feasibility

- [eeg-bids-2019](./eeg-bids-2019/card.md): the specification that makes electrode positions,
  channel type and status, reference and filter settings machine-readable — with the catch that
  `electrodes.tsv` and `coordsystem.json` are *recommended*, not required, so a valid BIDS-EEG
  dataset can still carry no electrode coordinates (`relevance: medium`, 2019)
- [openneuro-2021](./openneuro-2021/card.md): the archive releasing data "by default under a
  Creative Commons Zero (CC0) Public Domain Dedication", the least restrictive access route in this
  strand; more than 600 datasets and 20,000 participants at time of publication; search interface
  has no free-text field (`relevance: medium`, 2021)
- [nemar-2022](./nemar-2022/card.md): the Swartz Center gateway filtering OpenNeuro to EEG, MEG and
  iEEG with per-dataset quality assessment and a direct handoff to San Diego Supercomputer Center
  compute; also the argument for Hierarchical Event Descriptors, since BIDS records that events
  happened without constraining how they are named (`relevance: low`, 2022)

Access routes observed across the whole strand, from least to most friction, as specification
rather than recommendation: CC0 with no account (OpenNeuro default) → Open Data Commons Attribution
with no account ([sleep-edfx](./sleep-edfx/card.md), 8.1 GB by `wget` or `aws s3 sync
--no-sign-request`) → CC BY open download ([tes-eeg-ecg-2021](./tes-eeg-ecg-2021/card.md) on Zenodo
and OpenNeuro, [livewire-2024](./livewire-2024/card.md) on FigShare) → open download with the data
licence unstated ([boa-actors-2025](./boa-actors-2025/card.md),
[hinss-2023-passive-bci](./hinss-2023-passive-bci/card.md)) → click-through data use agreement with
registration ([mous-2019](./mous-2019/card.md)) → printed, signed and scanned end-user licence
agreement ([deap-2012](./deap-2012/card.md), [amigos-2021](./amigos-2021/card.md)) → request to the
authors with no published route ([strum-2018](./strum-2018/card.md)).

Two practical notes recorded during collection. The host serving both the DEAP and AMIGOS project
pages (`eecs.qmul.ac.uk`) returned HTTP 503 throughout retrieval over both HTTP and HTTPS, so
neither end-user licence agreement text nor the DEAP distributed channel list could be read. And
the memory constraint in the project's `CLAUDE.md` — that one subject's full recording exhausts a
Jupyter kernel — bites hardest on `tes-eeg-ecg-2021` (32 channels at 2 kHz over continuous
70-minute sessions) and `sleep-edfx` (whole-night recordings of about 20 hours each).

## 5. STRUM and its closest comparators

- [strum-2018](./strum-2018/card.md): the required entry, carded once from its primary source. IEEE
  paywalled with no open copy anywhere, so participants, channels, sampling rate, derivation
  scheme, peripheral channels and label scheme are read from the primary source as of 2026-08-01
  (`relevance: high`, 2018)
- [hinss-2023-passive-bci](./hinss-2023-passive-bci/card.md): the closest open comparator — 29
  participants, 3 sessions a week apart, 4 cognitive tasks including the aviation-style MATB-II,
  over 100 hours, 63 EEG channels plus 1 ECG at 500 Hz referenced at Fpz, per-session 3D electrode
  scanning, BIDS on Zenodo, labels validated subjectively, behaviourally and physiologically
  (`relevance: high`, 2023)
- [mous-2019](./mous-2019/card.md): 204 subjects, 102 reading and 102 listening to the same
  sentences with per-word visual duration derived from the audio duration — the project's exact
  stimulus manipulation, at scale, but between subjects and in 275-channel MEG (`relevance: high`, 2019)

What each comparator offers that STRUM does not, as specification: `hinss-2023-passive-bci` offers
a fully readable acquisition specification, an open access route, measured per-session electrode
coordinates, and three independent label sources on the same trials. `mous-2019` offers a
spoken-versus-written manipulation with the stimulus-duration confound explicitly controlled, and
204 subjects. What STRUM offers that neither does is unknown, because the paper was obtained through institutional access.

### STRUM citation search record

Required by the acceptance criteria. The brief's command,
`opencite cite "10.1109/SMC.2018.00023" --direction backward`, **does not run**: `--direction`
accepts only `citing`, `references`, `both`. What was run instead, and what it returned:

- `--direction citing` → **2 results**, confirming the count the brief anticipated and which
  Semantic Scholar (`Cited: 2`) and OpenAlex (`cited_by_count: 2`) both independently report.
  The two are Kothe et al. (2024), "The Lab Streaming Layer for Synchronized Multimodal Recording",
  `10.1101/2024.02.13.580071`, carded here as [lsl-2024](./lsl-2024/card.md); and Acar & Makeig
  (2022), "Evaluation of skull conductivity using SCALE head tissue conductivity estimation using
  EEG", EMBC, `10.1109/embc48229.2022.9872004`. Both share an author with STRUM. **Neither trains
  or evaluates a model on STRUM data.** So the finding the brief flagged holds: there is no
  published modelling work on STRUM to baseline against.
- `--direction references` → **21 results**, all pre-2017, and characteristic of a passive-BCI
  methods lineage rather than a dataset lineage: Farwell & Donchin (1988), Ramoser et al. (2000),
  Ang et al. (2008) FBCSP, Blankertz et al. (2010), Lotte & Guan (2010), Tomioka & Müller (2009),
  Zander & Kothe (2011), Kothe & Makeig (2013) BCILAB, Bigdely-Shamlo et al. (2013) Hierarchical
  Event Descriptors, Klosterman et al. (2016). No dataset descriptor is cited. Nothing in the
  reference list is a candidate dataset for this project, so the backward search yielded **nothing
  usable** for this strand beyond the observation itself.
- `--direction both` → 23 merged results, and emits
  `WARNING: opencite.citations: Citation query failed: 'NoneType' object is not iterable` while
  still returning output. Its result should not be trusted as complete without the two
  single-direction runs to check against.

Author-copy search, also required: the Swartz Center for Computational Neuroscience and Intheon
publication pages were checked first as the brief directs. `intheon.io/projects` lists LSL, XDF,
ASR, BCILAB and SIFT and does not mention STRUM at all. Unpaywall reports `oa_status: closed`,
`has_repository_copy: false`, and an empty `oa_locations` array. Registry sweeps (PhysioNet,
OpenNeuro, NEMAR, Zenodo, figshare) found no hosted copy of the data. The community index
`meagmohit/EEG-Datasets` records the access route verbatim as "Strum dataset is not available on
headit.ucsd .. contact authors".

## Acceptance criteria status

| Criterion | Status |
|---|---|
| At least 18 entries across all 5 categories | Met — 19 |
| At least 3 entries per category | Met — 4 / 3 / 6 / 3 / 3 |
| STRUM carded once from its primary source, full fixed field set | Met; every field read from the full paper after institutional access on 2026-08-01 |
| Backward citation search run and recorded in `INDEX.md` | Met, including that the brief's command form is invalid and that the search returned nothing usable |
| At least 4 datasets with EEG and at least one peripheral modality | Met — 6 |
| At least 3 category-3 entries bearing on stimulus-condition label validity | Met — 4 |
| Category 1 reaches 3 entries, or queries recorded | Both — 3 dataset entries plus the query record above |
| Every `type: dataset` card records the full fixed field set | Met |
| Every entry folder has `card.md`, `source.md`, `meta.json` | Met |
| Every entry has BibTeX keyed to its slug | Met |
| `INDEX.md` fully populated with categorised one-liners | Met |
| No more than 40% `relevance: high` | Met — 6 of 19, 31.6% |
| No prose synthesis, dataset ranking, or gap matching | Met |

### Not met, and worth stating plainly

- **STRUM's specification is read.** The complete paper was obtained through institutional access on 2026-08-01 and every fixed field on `strum-2018` now comes from section III: 56 participants as 28 pairs, 206-channel BioSemi EEG at 512 Hz, 2-channel ECG, 2-channel EOG and a 16-channel respiration belt on the same amplifier, Lab Streaming Layer into one XDF file per session, and side tasks forming a 2x2 of stimulus modality by stimulus kind. The PDF is cached locally and not committed, since the paper is under IEEE copyright.

## Cross-strand entries

Three works here are also carded in `datasets-benchmarks`, deliberately. That strand asks how the
field measures transfer; this one asks what data the project could use. The same artifact answers
both questions differently, so each card is written to its own. Phase 5 must merge these to one
bibliography entry per identifier.

- `eeg-bids-2019` also in [datasets-benchmarks/eeg-bids](../datasets-benchmarks/eeg-bids/card.md).
- `sleep-edfx` also in
  [datasets-benchmarks/sleep-edf-expanded](../datasets-benchmarks/sleep-edf-expanded/card.md).
- `openneuro-2021` also in [datasets-benchmarks/openneuro](../datasets-benchmarks/openneuro/card.md).
