# Pretraining Corpora, Benchmarks, and Evaluation Protocols — Collection Index

Strand C. Scope categories are those defined in `_briefs/strand-datasets-benchmarks.md`. One line per
entry; each entry's full record is its `card.md`. Nothing here is a synthesis, a ranking, or a
protocol recommendation; those are Phases 3 and 4.

**Collection status: 18 entries, quota met.** Category counts: 3 in category 1, 4 in category 2,
5 in category 3, 3 in category 4, 3 in category 5. Relevance distribution: 6 high (33.3%), 10 medium,
2 low.

These counts were stale until the Phase 2 review: they still described 19 entries, because
`brookshire-2024-data-leakage` was collected independently by this strand and by `eeg-models`, and
the near-identical duplicate here was removed in favour of a cross-reference. Category 4 lost that
entry from its count but not its evidence; see the cross-reference in that section.

## 1. Large EEG pretraining corpora

- [tuh-eeg-corpus](./tuh-eeg-corpus/card.md): 16,986 clinical sessions from 10,874 patients at 250 Hz
  on 24–36 channels with the neurologist's report attached; the substrate under CBraMod, BIOT, LaBraM
  and REVE, distributed by signed form and rsync under **no stated data licence**
  (`relevance: medium`, 2016)
- [openneuro](./openneuro/card.md): 604 datasets and 20,989 participants including 81 scalp-EEG
  datasets, all BIDS-validated at upload and released by default under CC0; supplies 10,194 of REVE's
  61,415 pretraining hours and is the source of the non-clinical heterogeneity in modern corpora
  (`relevance: low`, 2021)
- [sleep-edf-expanded](./sleep-edf-expanded/card.md): 197 whole-night polysomnograms with expert
  hypnograms under an Open Data Commons Attribution licence; carries EOG, chin EMG, respiration and
  body temperature alongside two EEG derivations, none of which any checkpoint or suite in this
  corpus uses (`relevance: low`, 2018)

Also bearing on this category: [adabrain-bench](./adabrain-bench/card.md) Table 7 is the single most
complete public statement of what BIOT, EEGPT, LaBraM and CBraMod were pretrained on, in hours,
channel counts and named corpora, and is the source of most checkpoint-to-corpus mappings recorded on
the cards above. [brain4fms](./brain4fms/card.md) Table 1 does the same for fifteen models including
intracranial ones.

## 2. Downstream benchmarks the checkpoints report on

The checkpoint-to-benchmark mapping is recorded on each dataset card under "Notable details", in the
fixed field "Checkpoints pretrained on or evaluated against it", with the reporting source named.

- [tuab](./tuab/card.md): binary normal-versus-abnormal clinical EEG, the most reported benchmark in
  the foundation-model literature; **BIOT and CBraMod were both pretrained on it and are then
  evaluated on it**, and the document the corpus names as its description does not state whether the
  distributed partition is patient-disjoint (`relevance: medium`, 2017)
- [tuev](./tuev/card.md): six-class epileptiform-event classification; the benchmark where the
  field's standard preprocessing is sixteen bipolar derivations from BIOT's scripts, which forces a
  coordinate-based model to represent a differential recording as a single midpoint
  (`relevance: medium`, 2016)
- [physionet-mi](./physionet-mi/card.md): 109 subjects, 64 channels at 160 Hz, motor execution and
  imagery with stimulus markers in EDF+ annotation channels; the dataset on which REVE reports the
  cleanest pretraining ablation in the corpus, +10.7 balanced-accuracy points for the same
  architecture with versus without pretraining (`relevance: medium`, 2009)
- [bci-competition-iv-2a](./bci-competition-iv-2a/card.md): 9 subjects, 288 four-class motor-imagery
  trials per session over two sessions; withheld test labels, submitted executables, enforced
  causality and mandatory open source made this a stronger anti-overfitting regime than any modern
  suite operates, and the review warns in advance that post-release work on the same data overfits
  (`relevance: medium`, 2012)

Cross-referenced from category 3: the per-dataset checkpoint results themselves are tabulated in
[adabrain-bench](./adabrain-bench/card.md) (four checkpoints × thirteen datasets, three settings),
[omnieeg-bench](./omnieeg-bench/card.md) (ten checkpoints × fifty-four datasets),
[brain4fms](./brain4fms/card.md) (fifteen models × twenty-two tasks) and
[neuralbench](./neuralbench/card.md) (six foundation models and eight task-specific architectures ×
thirty-six tasks).

## 3. Benchmark suites and standardized protocols

Each card records the suite's split rule, metric, fine-tuning budget and covered checkpoints. The four
foundation-model suites prescribe **conflicting split protocols**; the conflict is recorded in each
card's "Open questions / limitations" and is deliberately not resolved here.

- [adabrain-bench](./adabrain-bench/card.md): 13 datasets, 7 tasks, 4 checkpoints; cross-subject,
  multi-subject and few-shot settings with **full fine-tuning as primary** and **no split ratio stated
  anywhere in the paper**; balanced accuracy plus a transfer score against the from-scratch
  counterpart (`relevance: high`, 2025)
- [omnieeg-bench](./omnieeg-bench/card.md): 54 datasets, 6 task families, 10 checkpoints; **8:1:1
  subject-level split with linear probing as primary**, and the finding that model rankings "change
  substantially" between linear probing and full fine-tuning on the same data
  (`relevance: high`, 2026)
- [brain4fms](./brain4fms/card.md): 22 tasks from 18 datasets, 15 models spanning scalp and
  intracranial EEG; **approximately 3:1:1 leave-subjects-out with group-wise cross-validation**,
  AUROC-led, plus a channel-permutation probe for dataset-specific spatial structure
  (`relevance: medium`, 2026)
- [neuralbench](./neuralbench/card.md): 36 tasks, 94 datasets, 14 architectures; **four splitting
  strategies chosen per task including random splits where examples are few**, and the only suite that
  flags on its leaderboard which models were pretrained on the dataset they are evaluated on
  (`relevance: high`, 2026)
- [moabb](./moabb/card.md): the pre-foundation-model standard the others depart from — 12 datasets,
  275 subjects, 6 classical pipelines; **within-session 5-fold cross-validation only**, declared a
  best case; ROC-AUC; and the corpus's only cross-dataset inference procedure (per-dataset Wilcoxon or
  permutation test, Stouffer combination weighted by √n, Bonferroni, standardized mean difference)
  (`relevance: medium`, 2018)

## 4. Evaluation protocol conventions and their critiques

The strand's centre of gravity. Four entries here, of which all four critique a protocol or
demonstrate leakage or a metric failure rather than merely describing convention.

- Brookshire et al. 2024, data leakage in translational EEG deep learning, is carded in the
  `eeg-models` strand as
  [eeg-models/brookshire-2024-data-leakage](../eeg-models/brookshire-2024-data-leakage/card.md).
  It was collected in both strands independently; the two cards were near-identical, so the
  duplicate here was removed rather than maintained. It remains the evidential basis for this
  category: the same network on the same data scores 99.8% under segment-based holdout and 53.0%,
  a confidence interval containing chance, under subject-based holdout, and only 17 of 63
  surveyed studies unambiguously avoided the flawed design.
- [kamrud-2021-data-partitioning](./kamrud-2021-data-partitioning/card.md): five published
  cross-participant models replicated under shuffled versus participant-disjoint partitioning across
  five datasets; error rates rise on every one, from 0.09 to 0.466 on driver fatigue and 0.008 to 0.50
  (chance) on schizophrenia, with covariate shift from individual differences and non-stationarity as
  the demonstrated mechanism (`relevance: high`, 2021)
- [varoquaux-2018-cross-validation-failure](./varoquaux-2018-cross-validation-failure/card.md): even a
  correctly split cross-validation carries ±10 percentage points of uncertainty at n = 100, and the
  standard error across folds understates that by a factor of 0.73 for leave-one-out and 0.26 for
  repeated random splits; ~50 reasonable pipelines reach 71% on data guaranteed to be at chance
  (`relevance: high`, 2018)
- [combrisson-2015-chance-level](./combrisson-2015-chance-level/card.md): classifying Gaussian noise
  at small n yields "decoding accuracies of up to 70% or higher in two-class decoding", so the
  theoretical chance level is the wrong comparator; offers binomial and permutation p-values as
  remedies. Abstract-only, and the tabulated empirical chance levels are reported but not accessible
  (`relevance: medium`, 2015)

**Cross-references, not carded here.** Two shortcut-learning works named in this strand's brief were
collected by the `eeg-models` agent and must not be duplicated:

- `../eeg-models/lin-2026-identity-trap/card.md` — frozen embeddings of LaBraM, CBraMod and REVE are
  dominated by subject identity at 13–89× a random null in 12 of 12 model-by-dataset pairs, and
  erasing that axis *improves* label decoding. This is the entry that shows the subject-disjoint split
  recommended by `brookshire-2024-data-leakage` and `kamrud-2021-data-partitioning` is necessary but
  not sufficient. Depended on by both of those cards and by
  [omnieeg-bench](./omnieeg-bench/card.md).
- `../eeg-models/zare-2026-stress-testing/card.md` — dataset identity decodes from frozen REVE
  embeddings at AUROC 1.000 while the diagnosis decodes at 0.528, and a randomly initialised encoder
  beats pretrained REVE on Korean dementia. The critique-side analogue of
  [brain4fms](./brain4fms/card.md)'s channel-permutation probe, and cross-referenced from that card.

Also bearing on this category from other groups: [neuralbench](./neuralbench/card.md) documents
pretraining-data overlap between checkpoint corpora and downstream evaluation sets and flags it on the
leaderboard; [tuab](./tuab/card.md) and [tuev](./tuev/card.md) record that BIOT and CBraMod were
pretrained on the benchmarks they are scored against; [bci-competition-iv-2a](./bci-competition-iv-2a/card.md)
carries the competition organizers' own warning that post-release use of the test labels overfits;
and [moabb](./moabb/card.md) is the only suite in the corpus that runs a significance test at all.

## 5. Formats and tooling standards

- [eeg-bids](./eeg-bids/card.md): the BIDS extension for scalp EEG; requires stimulus markers to be
  written out as an explicit `events.tsv` because "the representation of events is rarely explicit in
  the original data", and separates `channels.tsv` (stored signals) from `electrodes.tsv` plus
  `coordsystem.json` (positions in a named frame) (`relevance: medium`, 2019)
- [edf-plus](./edf-plus/card.md): the format nearly every corpus here is distributed in; stores events
  and stimuli not as a trigger line but as time-stamped UTF-8 text in a reserved `EDF Annotations`
  signal, and has **no mechanism at all for electrode coordinates** (`relevance: medium`, 2003)
- [mne-python](./mne-python/card.md): the reference implementation that reads EDF, BDF, BrainVision,
  BTI/4D, KIT and FIF, and whose access-on-demand design is inherited by its epoching and averaging
  containers — the documented answer to this project's recorded memory constraint
  (`relevance: high`, 2013)

## Notes on collection

- **Identifier resolution.** `adabrain-bench` was supplied without an identifier and is absent from
  OpenAlex under both `title.search:AdaBrain-Bench` and `title.search:AdaBrain` (count 0 for each);
  the arXiv Atom API was rate-limited. It resolved to arXiv 2507.09882 through the arXiv web search
  interface on the exact title, returning exactly one hit. `brain4fms` (OpenAlex W7128864510) and
  `neuralbench` (OpenAlex W7161091175) were resolved to arXiv 2602.11558 and 2605.08495 through the
  OpenAlex REST interface, which `opencite lookup` cannot do. No identifier was constructed or guessed
  and no entry took the `not-available` path for want of an identifier.
- **Archival.** Seven of nineteen entries have a committed `source.pdf`; all seven are
  Creative-Commons-licensed journal articles. All four arXiv preprints are under arXiv's default
  non-exclusive licence, which conveys no third-party redistribution right, so they are
  `not-redistributable` with markdown extractions only. One entry, [moabb](./moabb/card.md), is
  `not-available`: its version of record is open access under CC BY 3.0 but two download attempts
  returned an IOP bot-manager captcha page, so the arXiv preprint was read instead and the failure is
  documented in `meta.json` for re-attempt.
- **Boundary with `candidate-datasets`.** Every dataset carded here is carded because a strand A
  checkpoint was pretrained on it or benchmarked against it, which is the dividing line the two briefs
  set. Sleep-EDF was the only close call, since it carries EOG, EMG and respiration and could read as
  a peripheral-physiology candidate; it is carded here to the question of what the checkpoints report
  on, and its card records that the peripheral channels exist and that no suite uses them, leaving
  their usability as signal to strand D.

## Cross-strand entries

Four works in this strand are also carded elsewhere. This is deliberate, not duplication to be
cleaned up: each card answers its own strand's question, and the partition exists because a work can
be a benchmark and a candidate at the same time without the two readings being interchangeable. The
validator warns on every shared identifier so the pairing stays visible; Phase 5 must merge these to
one bibliography entry per identifier.

- `eeg-bids` also in [candidate-datasets/eeg-bids-2019](../candidate-datasets/eeg-bids-2019/card.md).
  Here: how a format makes stimulus markers explicit and machine-readable. There: whether a candidate
  dataset arrives in a form the project can read.
- `sleep-edf-expanded` also in [candidate-datasets/sleep-edfx](../candidate-datasets/sleep-edfx/card.md).
  Here: a benchmark the checkpoints report on. There: a dataset carrying peripheral physiology, whose
  peripheral channels every suite in this corpus discards.
- `openneuro` also in [candidate-datasets/openneuro-2021](../candidate-datasets/openneuro-2021/card.md).
  Here: a source of pretraining corpora. There: a registry to search for candidate datasets.
- `adabrain-bench` also in [eeg-models/adabrain-bench-2025](../eeg-models/adabrain-bench-2025/card.md).
  Here: what the suite fixes, meaning datasets, splits, adaptation recipe. There: what it found about
  the checkpoints, including that pretrained models lose outright on every clinical-monitoring task.
