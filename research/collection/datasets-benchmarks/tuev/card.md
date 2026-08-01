---
slug: tuev
type: dataset
strand: datasets-benchmarks
year: 2016
authors: [Obeid, Picone]
venue: Neural Engineering Data Consortium, Temple University (corpus landing page)
doi: null
url: https://isip.piconepress.com/projects/nedc/html/tuh_eeg/
license: null (no data licence stated; access by signed form and registration)
modalities: [scalp-eeg, clinical-eeg]
tags: [benchmark-dataset, six-class-classification, epileptiform-events, temple-university-hospital, checkpoint-mapping, registration-required, class-imbalance, bipolar-derivations, event-annotations]
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

The six-class epileptiform-event benchmark that every major EEG checkpoint reports on, and the one
where the preprocessing the field has standardized on — sixteen bipolar derivations from BIOT's
scripts — forces coordinate-based models to represent a difference between two electrodes as a
single midpoint.

## Summary

The Temple University Hospital EEG Events Corpus is a subset of the parent Temple University
Hospital EEG Corpus carrying annotations of EEG segments in one of six classes: spike and sharp wave,
generalized periodic epileptiform discharges, periodic lateralized epileptiform discharges, eye
movement, artifact, and background. Three of these are signal classes and three are noise classes,
following the parent corpus's own framing that "three events are used to model background noise". It
is distributed through the same registration and rsync route as the rest of the Temple University
Hospital collection, at path `data/tuh_eeg/tuh_eeg_events/v2.0.1` at retrieval time. Unlike TUAB,
whose description the corpus page points to a master's thesis for, TUEV has no linked descriptive
document on the corpus page; the annotation classes and the parent corpus's recording
characteristics are all the primary documentation provides.

## Relevance to the review

TUEV earns its place here on the checkpoint mapping and on one specific methodological detail.

The mapping is as dense as TUAB's and slightly more informative, because TUEV is the harder task and
the model spread is wider. In `adabrain-bench`'s cross-subject setting, balanced accuracies are BIOT
51.78, EEGPT 42.89, LaBraM 59.05, CBraMod 57.69, against supervised EEGNet 32.65, LDMA 32.88,
ST-Tran 38.68 and Conformer 54.06. That is a 5-point margin for the best pretrained model over the
best supervised one on balanced accuracy, and a 26-point margin over EEGNet — the widest
pretrained-versus-small-supervised gap in that whole table apart from EEGMAT. Six classes with strong
imbalance is a setting where pretraining appears to help most, which is worth carrying into Phase 4
alongside the caution that TUEV is also in CBraMod's and BIOT's pretraining corpora.

The methodological detail is the montage. `reve-2025` records that TUEV "is preprocessed with BIOT's
scripts into 16 common bipolar channels in the 10-20 system", and that because REVE's positional
encoding takes one three-dimensional coordinate per channel, the authors used "the average position
of each bipolar montage" — a midpoint standing in for a differential recording between two sites.
That approximation is invisible in any leaderboard, it is unablated, and it is applied by a model
that reports TUEV numbers competitive with models that have no such constraint. For a project
deciding whether a coordinate-based checkpoint can ingest its own recordings, TUEV is the worked
example of what happens when the answer is "not natively".

## Notable details

Fixed field set required of every `type: dataset` card in this strand:

- **Participants**: not stated on the corpus landing page. `adabrain-bench` Table 6 records 370
  subjects for its preparation of TUEV, which is a benchmark figure rather than the corpus's own.
- **Channels**: not stated for TUEV specifically. The parent corpus is 24 to 36 channels with 31 the
  most common EEG-only count. `adabrain-bench` uses 23 channels; `reve-2025` uses BIOT's 16 bipolar
  derivations in the 10-20 system. Three figures, three different objects — the recording, one
  benchmark's channel selection, and a bipolar re-derivation. Note the distinction the corpus
  documentation never makes: 16 bipolar channels is a *derivation scheme*, a montage in the strict
  sense, whereas 23 or 31 is an *electrode count*.
- **Sampling rate**: not stated for TUEV. The parent corpus is 87% at 250 Hz with 256, 400 and 512 Hz
  making up the rest. `adabrain-bench` records 256 Hz for TUEV.
- **Total hours**: unknown. `adabrain-bench` reports 112,237 samples of 5 seconds in its preparation,
  which is about 156 hours of segmented data, but that is a count of the benchmark's extracted
  windows, not of the corpus.
- **Task**: none. Archival clinical EEG; the six classes are annotations of events occurring in
  routine and long-term monitoring recordings, not experimental conditions.
- **Label type**: expert per-segment event annotation in six classes — spike and sharp wave (SPSW),
  generalized periodic epileptiform discharges (GPED), periodic lateralized epileptiform discharges
  (PLED), eye movement (EYEM), artifact (ARTF), background (BCKG). The parent corpus's annotation
  format is per-channel with start and stop times.
- **Licence**: none stated.
- **Access route**: signed form emailed to help@nedcdata.org, then ssh key and rsync at
  `data/tuh_eeg/tuh_eeg_events/v2.0.1`, with `-L` required because the subset is symlinked to the
  parent.
- **Checkpoints pretrained on or evaluated against it**:
  *Pretrained on TUEV* — BIOT (TUEV is among its six pretraining corpora) and CBraMod (TUAB, TUAR,
  TUEP, TUEV, TUSE, TUSL), both per `adabrain-bench` Table 7.
  *Evaluated on TUEV* — BIOT, EEGPT, LaBraM and CBraMod at balanced accuracy 51.78, 42.89, 59.05 and
  57.69 with weighted F1 75.17, 74.65, 79.62 and 78.69 in `adabrain-bench`'s cross-subject setting;
  REVE, which reaches 0.696 on TUEV by souping ten fine-tuning runs and preprocesses with BIOT's
  16-bipolar-channel scripts; and the epilepsy-and-abnormality subtype of `omnieeg-bench`. TUEV is
  also a benchmark in the LaBraM and BIOT papers themselves, which is where the reused splits in
  `reve-2025` come from.

Other details:

- The six classes are three signal and three noise, per the parent corpus paper.
- The corpus documentation gives no descriptive document for TUEV, unlike TUAB (a linked master's
  thesis) or the parent corpus (a Frontiers data report).
- Version at retrieval time: v2.0.1.
- Evaluation splits used by REVE are inherited from CBraMod, LaBraM and BIOT "for comparability"
  rather than being defined by the corpus.

## Open questions / limitations

- **The corpus's own documentation is one paragraph.** Everything quantitative on this card beyond
  the class list and the access route comes from benchmark papers, not from the corpus. Participants,
  channels, sampling rate, hours, class balance and the train/evaluation partition are all
  `unknown` from the primary source. The release's `_AAREADME` would carry them and is behind the
  registration wall; probed public URLs returned 404.
- **Whether the distributed partition is patient-disjoint is not stated anywhere that was read.** The
  same concern applies as for `tuab`, and with the same consequence: every TUEV number in the
  foundation-model literature inherits a partition whose grouping property is undocumented in public.
- **Two of the four checkpoints commonly reported on TUEV were pretrained on it.** BIOT and CBraMod
  both list TUEV among their pretraining corpora in AdaBrain-Bench's own Table 7, and the same paper
  reports their TUEV scores without qualification.
- **The 16-bipolar-channel preprocessing is a field convention with no documented provenance in the
  corpus.** It comes from BIOT's release scripts and has been adopted by LaBraM, CBraMod and REVE for
  comparability. A model with no representation for a differential recording must approximate it —
  REVE substitutes the midpoint of the electrode pair, which discards the pair's orientation and
  separation, and two different pairs can share a midpoint. No ablation of that choice exists.
- Class imbalance is severe by construction — background is one of six classes in a corpus of
  routine clinical EEG — which is why weighted F1 rather than accuracy is the standard secondary
  metric, and why the gap between balanced accuracy (around 42 to 59) and weighted F1 (around 75 to
  80) is so large on this benchmark. A reader comparing the two metrics across papers is comparing
  very different quantities.
- The annotation guidelines are published by the consortium as a separate document that was not
  retrieved, so how a rater distinguishes, for example, generalized from periodic lateralized
  epileptiform discharges is not recorded here, and no inter-rater agreement statistic was found.

## Citations

Primary: `tuev`

- `tuh-eeg-corpus` — the parent archive; the source of the recording characteristics and the six-class
  annotation scheme.
- `tuab` — the sibling subset, binary normal versus abnormal, same access route and same
  documentation gap.
- `adabrain-bench` — the source of the checkpoint-by-benchmark numbers and of the pretraining-corpus
  table showing the BIOT and CBraMod overlap.
- `reve-2025` (strand `eeg-models`) — documents the 16-bipolar-channel preprocessing and the midpoint
  approximation it forces.
- `labram-2024` (strand `eeg-models`) — one of the checkpoints whose TUEV splits the later papers
  reuse.
