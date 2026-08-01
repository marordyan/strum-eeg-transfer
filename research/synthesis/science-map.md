# Cross-strand science map

Phase 3 synthesis. Input is the four strand ontologies in this directory and the 84 entries they
organize. This document inventories the analytic and methodological themes that **cut across
strands**, theme by theme.

The four ontologies organize entries *within* a strand and do that job completely: every entry has a
home, every leaf is a card link, and each strand's coverage table proves nothing was dropped. What
none of them can do is put two strands' cards side by side. That is the only thing this document
does.

**The constraint that defines it.** A theme appears below only if it draws on cards from at least
two strands. A theme confined to one strand is an ontology node and already has a home; if a section
here restates one, it should be deleted. The test applied to every candidate was: does holding these
strands' cards together say something none of
[eeg-models](./eeg-models-ontology.md),
[datasets-benchmarks](./datasets-benchmarks-ontology.md),
[multimodal-biosignals](./multimodal-biosignals-ontology.md) or
[candidate-datasets](./candidate-datasets-ontology.md) says alone.

**What this document is not.** It is not the gap analysis. Every theme closes with **open questions
the literature leaves** — absences the cards state about themselves — and not with gaps in our
corpus, coverage claims about the set, or recommendations. The practice brief's test is applied
throughout: when the cards state the absence about themselves, quoting them is a property statement
and belongs here; when only the synthesis can see the absence, it is coverage and belongs to Phase 4.
The handful of sentences that sit on that line are marked **[boundary]**, following the convention
the `multimodal-biosignals` ontology established.

**Ordering carries no ranking.** Themes 1 to 2 are about what a reported number is a number *of*;
3 to 6 about what the signal is and what is done to it before a model sees it; 7 to 8 about what a
number is compared against; 9 to 11 about the corpus's own structure. Nothing is ranked by
importance and nothing is recommended.

**A note on coverage tables.** `_briefs/synthesis-practice.md` makes a coverage table mandatory,
and requires that every entry in the strand appear. That rule was written for within-strand
documents and does not transfer: a cross-cutting document has no strand whose entries it must
exhaust, and an entry that participates in no cross-strand theme is correctly absent rather than
dropped. What replaces it here is §12's theme-by-strand matrix, which discharges the rule this
document does have — that every theme cross at least two strands.

---

## 1. What a reported number means depends on the unit that was held out

**Strands crossed:** `datasets-benchmarks`, `eeg-models`, `multimodal-biosignals`,
`candidate-datasets`.

Each strand holds this property at a different level, and the four levels are not interchangeable.

**As a property of the instrument.** Five suites put the boundary in five places: within-session
five-fold with no subject holdout at all
([moabb](../collection/datasets-benchmarks/moabb/card.md)), subject-level 8:1:1
([omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)), leave-subjects-out with
group-wise cross-validation ([brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)),
subject-disjoint at a ratio the paper never states
([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)), and one of four
per-task strategies including a plain random split
([neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)).

**As a property of the checkpoint's own paper.** Headline numbers rest on sample-level splits in
[luna-2025](../collection/eeg-models/luna-2025/card.md) and
[femba-2025](../collection/eeg-models/femba-2025/card.md); on a mixture within one paper in
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md), subject-wise for three datasets and
trial-wise for SEED-V with the difference unflagged; and on subject-*dependent* evaluation by design
in [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md), which three benchmark
suites nevertheless deploy as a cross-subject baseline.

**As the thing that sets the size of a fusion gain.**
[angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
holds its four-modality input fixed and moves only the protocol: binary accuracy falls 74.78% →
67.04% and ternary 60.90% → 47.80%. Those drops, 7.74 and 13.1 points, are each larger than the
entire EEG-to-all-four modality gain measured under the harder protocol, 5.84 and 6.21 points. In
the same strand the three entries whose split geometry is stated and subject-disjoint report +5.84,
+0.002 and a difference their own authors call not significant, while the two double-digit gains
belong to the two entries whose denominators their cards flag as unverifiable
([salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md),
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)).

**As a property of the experimental design, upstream of any protocol.** This is the level the other
three strands have no representation for.
[mous-2019](../collection/candidate-datasets/mous-2019/card.md) manipulates spoken versus written
*between* subjects — 102 readers and 102 listeners — so the label and subject identity are the same
variable and no choice of holdout unit separates them. The card states it flatly: any across-subject
classifier trained on that contrast "is separating two disjoint groups of people". A suite's choice
between 8:1:1 and leave-subjects-out is downstream of a design property that the benchmark strand
never mentions and that the candidate strand has no benchmark to attach it to. The same strand
records identifier-level traps that defeat a correctly chosen protocol at the file level: one
participant appears as IDs 22, 23 and 24 across repeats in
[tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md), and
[sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)'s 197 files over two nights per
subject mean a recording-level split is not a subject-level split.

**The magnitudes, placed together.** The split effect has been measured in four settings by cards in
three strands, and in each it exceeds the effect the study was trying to measure.
[brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md): 99.8%
under segment holdout against 53.0% under subject holdout, 46.8 points, onto an interval containing
chance.
[kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md):
error rises on all five replicated models, driver fatigue 0.09 → 0.466 and schizophrenia 0.008 →
0.50, "no model was able to perform better than random chance".
[angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md):
7.74 and 13.1 points. And
[zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md): 12.7
points from a session change alone, holding subject and system fixed. Against these, the per-dataset
margins between the best pretrained and best supervised model in the one suite publishing a full
table run from −0.08 to +15.00
([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)), and the readable fusion
deltas from +0.002 to +12.6.

**Different words for the same thing.** "Cross-subject", "subject-independent",
"leave-one-subject-out", "participant-disjoint", "patient-ID-level", "GroupKFold",
"subject-stratified group 5-fold" and "leave-subjects-out" name one boundary across the four
strands; "sample-level", "trial-wise", "record-wise", "segment-based", "random split" and "improper"
name the other side of it. The strand that measures the effect calls it *leakage*
([brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)); the
strand that formalizes it calls it *covariate shift* under a Shimodaira loss-rescaling weight
([kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md));
the strand that designs against it calls it *manipulation geometry*
([mous-2019](../collection/candidate-datasets/mous-2019/card.md)).

**Open questions the literature leaves.**

- What a session-wise boundary is worth is declared unmeasured by all three critiques, each about
  itself: [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
  ("subject versus segment only"),
  [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  ("the word 'session' appears only descriptively, never as a partitioning unit"), and
  [varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
  ("'session' and 'run' are used interchangeably and neither is defined"). Two suites report
  leaderboard numbers at exactly that boundary:
  [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s multi-subject setting
  holds out recording sessions or trials, and
  [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)'s splits each subject's
  samples 8:1:1 over trials.
- Which sampling unit the published error bars refer to is left open by the paper that publishes
  them. [varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
  records that its x-axis deliberately mixes units — samples meaning "trials or sub-jects depending
  on the settings" — which for EEG, where one participant contributes thousands of epochs, is the
  decisive question and one the paper does not settle.
- When the improper protocol is legitimate is stated as a rule with no test attached.
  [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  permits it where the inference is narrower, "if a cross-participant model is only intended to
  perform classification on the same population that it is training upon", provided the paper says
  so — and no entry states how a reader tells, after the fact, which regime a published number was
  intended for.
- Whether protocol and adaptation regime interact is unmeasured by the suites that vary both:
  [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) demonstrates that the
  regime reorders the models and
  [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) demonstrates it with the
  opposite sign for EEGPT, but neither crosses regime with holdout unit.

---

## 2. Models can score by recognizing identity rather than by decoding the task

**Strands crossed:** `eeg-models`, `datasets-benchmarks`, `multimodal-biosignals`,
`candidate-datasets`.

The corpus contains the same failure mode at six levels of granularity, described by cards in four
strands, in four vocabularies, and almost no citations between them: of the pairs checked, only
two are connected.

| level of identity | what was measured | card |
|---|---|---|
| dataset / site | a linear probe separates dataset pairs from frozen REVE embeddings at AUROC 1.000, holding after projection to 50 principal components and at 0.9998 band-limited, while the same PCA-50 pipeline decodes the 3-way diagnosis at 0.528 | [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) |
| subject | frozen embeddings of LaBraM, CBraMod and REVE dominated by subject identity at 13–89× a random-Gaussian null in 12 of 12 model-by-dataset pairs, rising under fine-tuning in all 12 by 10–63 points | [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) |
| subject (independently) | t-SNE embeddings cluster by participant; of two transformations that artificially reduce inter-participant variability, shifting to the median raises proper-protocol accuracy (0.50 → 0.80) while a shifted Heaviside does not help; neither changes the improper protocol | [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md) |
| session | not measured anywhere; named as its own limit by three critiques (§1) | — |
| segment | segments of EEG from one subject resemble each other more than segments from different subjects; 46.8 points of inflation | [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md) |
| trial | the same CSP pipeline retrained to predict *which trial* a segment came from reaches median 100%, 99.9%, 99.7% and 99.6% across four conditions, significantly above the attention accuracies it was built to report | [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md) |
| exemplar | a decoder trained on some exemplars and tested on an unseen concept "could not distinguish the semantic classes, but only the exemplars, possibly through the use of perceptual differences between the exemplars" | [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md) |

**What holding them together shows.** The same mechanism — a nuisance variable that is more
decodable than the label and is collinear with it in the design — is discovered independently in a
clinical deep-learning survey, a cognitive-state replication study, a foundation-model probing paper,
an auditory-attention BCI study and a semantic-decoding ERP study. Only one pair is connected:
[brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)'s card
records [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) as the
later work extending the argument from supervised training to frozen embeddings, and Brookshire's own
card notes it makes no claim about frozen embeddings, so the extension is Lin's result.
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
supplies the generalization that connects the trial level to the design level: where a study has one
label per trial, the label and the trial identity are the same variable — which is
[mous-2019](../collection/candidate-datasets/mous-2019/card.md)'s between-subject case one level
coarser.

**Five remedies, none compared against another.** The corpus holds five procedures for the same
problem, in three strands (`eeg-models`, `candidate-datasets`, `multimodal-biosignals`), and no
entry runs two of them.

- Post-hoc erasure of a linearly removable axis: closed-form LEACE drives a subject probe to chance
  in all 12 pairs, and where the label varies within subject, erasing identity *improves* label
  decoding by 6–12 points
  ([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)).
- Confound regression inside every cross-validation fold — the only one of two obvious methods that
  is unbiased, post hoc counterbalancing biasing accuracy upward and plain confound regression
  downward far enough to produce significant below-chance accuracy
  ([snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)).
- A held-out generalization test across exemplars or modalities
  ([simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md),
  [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)).
- Training the decoder on a separate functional localizer designed to elicit the sensory response
  without inviting stimulus-specific eye movements
  ([mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)).
- Tying decodability to behavioural read-out — decodable shape information in two regions, only one
  of which shows stronger patterns on correct than incorrect trials
  ([ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md)).

**The same structure produces the failure and the one clean success.**
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md), the entry
whose whole design is a negative-control battery, reports one clean positive: CHB-MIT cross-subject
ictal detection at 0.793 AUROC against 0.701 for a randomly initialised encoder, 0.505 for random
features and 0.500 under label permutation — and attributes the cleanliness to positives and
negatives sharing recording sessions, which reduces session-level confounding. The session structure
that produces the identity failure elsewhere produces the clean result here because it falls on both
sides of the label.

**Different words for the same thing.** *Data leakage* (`eeg-models`), *improper partitioning* and
*covariate shift* (`datasets-benchmarks`), *the identity trap* (`eeg-models`), *trial fingerprints*
(`multimodal-biosignals`), *confound* (`candidate-datasets`, `multimodal-biosignals`), and
*exemplar rather than category* (`candidate-datasets`).

**Open questions the literature leaves.**

- What carries subject identity is model-specific and unidentified for one of the three models
  measured: removing the aperiodic 1/f component drops the subject probe by 9–19 points for LaBraM
  and CBraMod but shifts REVE's by at most 1.2 points, REVE's already sitting at or above 0.93
  ([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)).
- Whether erasing identity helps in general is untestable from the panel that measured it: its 2×2
  layout has one dataset per cell and its three models differ along five design axes at once, so no
  cross-model contrast is attributable to any single axis (same card).
- What dataset identity actually consists of is bounded by the paper that measured it: site,
  hardware, preprocessing, population, diagnosis composition and dataset history are confounded,
  establishing decodable dataset membership "and nothing more"
  ([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)).
- The residual after removing the confound is undetermined in the study that found it:
  [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  establishes that gaze carries the label and reports no neural decoding accuracy with the gaze
  contribution regressed out, and the gaze effect is itself significant "only marginally" at
  encoding — a combination the paper does not resolve.
- The one remedy stated as a general principle is in declared tension with the premise of transfer:
  [ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md)
  recommends restricting classifier flexibility and its card records that this "sits in direct
  tension with the entire premise of transfer from a large pretrained model", left unadjudicated
  because the paper predates that literature.

---

## 3. Spatial identity, derivation, and what a montage is

**Strands crossed:** `eeg-models`, `candidate-datasets`, `datasets-benchmarks`.

The models strand's mechanism split and the candidate strand's recording specifications are two
halves of one admissibility question, and the formats strand holds the third.

**Admissibility is a three-way conjunction that no strand states alone.** A coordinate-driven
checkpoint needs (i) a position per channel, (ii) a derivation that *has* a position, and (iii) a
file layer that can carry it.

- (i) and (ii) are the models strand's axis:
  [reve-2025](../collection/eeg-models/reve-2025/card.md) and
  [luna-2025](../collection/eeg-models/luna-2025/card.md) require a 3D coordinate per channel;
  [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) requires a
  six-dimensional position-and-orientation vector plus one of exactly three type labels.
- (ii) is where the corpus fractures. A bipolar derivation is a difference between two electrodes and
  has no single position, and the strand contains four different answers and one silence: the
  midpoint of the pair ([reve-2025](../collection/eeg-models/reve-2025/card.md)), the first electrode
  of the pair ([bendr-2021](../collection/eeg-models/bendr-2021/card.md), where FPz-Cz and Pz-Oz were
  "simply mapped" to FPz and Pz), a vocabulary row of its own
  ([biot-2023](../collection/eeg-models/biot-2023/card.md)), unspecified for a model whose entire
  Temple University pretraining set was converted to a 20-pair bipolar montage
  ([luna-2025](../collection/eeg-models/luna-2025/card.md)), and not discussed at all
  ([brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)).
- (iii) is the formats strand's finding:
  [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) stores channel labels and "has no
  mechanism at all for electrode coordinates", and
  [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) supplies `electrodes.tsv` and
  `coordsystem.json` at a requirement level the paper states two ways.
  [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md), the substrate under
  most of the field's pretraining, states no montage at all — the word does not occur — so the
  derivation scheme is each pretraining paper's own choice.

**The candidate strand supplies the values, and they do not line up with the mechanisms.** Eleven
datasets split five ways on derivation: referential to a named reference
([hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md),
[tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md),
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md),
[simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)),
common average ([boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md), whose
card states that "an average reference is not a per-electrode potential"), bipolar
([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)), referential-but-unstated
([strum-2018](../collection/candidate-datasets/strum-2018/card.md),
[deap-2012](../collection/candidate-datasets/deap-2012/card.md)), and unknown
([amigos-2021](../collection/candidate-datasets/amigos-2021/card.md)). Coordinates split three ways,
and measured coordinates exist in exactly one entry — a 3D head-and-cap scan run at the start of each
of three sessions, so between-session electrode displacement is quantified rather than assumed away
([hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md)).

**The two properties compound in the one place they both matter.**
[strum-2018](../collection/candidate-datasets/strum-2018/card.md) is 206 channels — the checkpoints
that could ingest an arbitrary layout are exactly the ones that need a coordinate per channel, and
the paper does not say whether coordinates were digitised or a template assumed, while also using
"montage" in the loose cap-layout sense. The card also reasons the derivation class from the hardware
rather than the text, since BioSemi acquires referentially against a CMS/DRL pair, and records that
the reference used for any released version is unstated.

**A harmonised pipeline can change the derivation class silently.**
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)'s shared
pipeline applies a common average reference to every model in its panel, including models pretrained
on referential data — and the card that states why that is a change of object is in a different
strand ([boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md)). The same
pipeline forced per-model exceptions its author names as limitations rather than results: BENDR
resampled back to 256 Hz after a shared 70 Hz band limit with 21-channel inputs truncated and
19-channel inputs zero-padded with a dead channel, LaBraM's 128-channel position embeddings linearly
interpolated per dataset, EEGMamba excluded from two cohorts entirely.

**Different words for the same thing — six cards, three strands, no citation between them.** This is
the corpus's strongest instance of independent convergence on a vocabulary defect.
[reve-2025](../collection/eeg-models/reve-2025/card.md) records that its abstract and conclusion say
"montages" where its methods say "arbitrary electrode layouts", and instructs that the precise claim
be carried forward. [luna-2025](../collection/eeg-models/luna-2025/card.md) records "topology-agnostic"
in its title and "montage-agnostic" in its conclusion, both looser than the mechanism supports.
[biot-2023](../collection/eeg-models/biot-2023/card.md) records that "16 bipolar montage channels"
are derivations, not positions. [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) records
that the specification conflates "montage", "derivation" and "re-referencing" in a single sentence.
[tuev](../collection/datasets-benchmarks/tuev/card.md) records that "channels" names three different
objects for one corpus — 31 in the parent recording, 23 in a benchmark's selection, 16 bipolar
derivations in the field's convention — and states the distinction the corpus documentation never
makes. [strum-2018](../collection/candidate-datasets/strum-2018/card.md) uses "montage" for a cap
layout. A layout is a set of positions; a montage is a derivation scheme; the coordinate-based
mechanisms generalize over the first.

**Open questions the literature leaves.**

- What the midpoint substitution costs is measured nowhere.
  [reve-2025](../collection/eeg-models/reve-2025/card.md) runs no ablation comparing it against
  alternatives; [tuev](../collection/datasets-benchmarks/tuev/card.md) records that it is "invisible
  in any leaderboard, unablated, and applied by a model reporting TUEV numbers competitive with
  models that have no such constraint"; and
  [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) records the same
  approximation applying to Fpz-Cz and Pz-Oz and being mentioned by no suite that reports Sleep-EDF
  numbers.
- Whether BIDS conformance guarantees a coordinate is unresolved in the specification itself:
  [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) records the requirement level stated
  two ways in one paper, a conditional "should be specified if the positions of the electrodes are
  known" against an unconditional "may in addition specify".
- Whether a name-indexed mechanism uses spatial information at all is declared unclear by its own
  authors: [bendr-2021](../collection/eeg-models/bendr-2021/card.md) states it is "presently unclear
  to what degree" the model leverages spatial information, and that an absent electrode is
  indistinguishable from a flat one.
- Layout generality fails on the one unseen layout in the paper that advertises it:
  [luna-2025](../collection/eeg-models/luna-2025/card.md) reports LUNA-Huge at 0.3900 balanced
  accuracy on SEED-V against CBraMod's 0.4091 and LaBraM-Base's 0.3976 — behind two name-indexed
  models — with the authors writing that "generalizing zero-shot to vastly different, high-density
  layouts remains challenging, possibly due to positional encoding constraints".
- What a checkpoint pretrained on one derivation class does when given another is unstated:
  [biot-2023](../collection/eeg-models/biot-2023/card.md) does not say what happens when a downstream
  dataset presents a channel absent from its vocabulary, its missing-channel study removing known
  channels rather than introducing unknown ones.

---

## 4. Temporal scale: three windows that do not agree, and one word for four objects

**Strands crossed:** `multimodal-biosignals`, `eeg-models`, `datasets-benchmarks`,
`candidate-datasets`.

The fusion strand names a two-way mismatch. Held against the other three, it is a three-way one.

**The peripheral integration window: 5 to 60 seconds.** 60 s segments
([papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md)), 5 s non-overlapping
([mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md),
[kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)),
10 s ([kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)),
20 s of EDA at 4 Hz against 2 s of EEG at 128 Hz in one study
([azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)),
and a sweep from 2 to 20 s buying about 0.012 AUROC
([wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)).
[makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) is the
toolkit-level recognition: event-related and interval-related analyses are distinct pipelines because
a stimulus-locked epoch is one and HRV or tonic EDA is the other.

**The model input window: 2 to 4 seconds, with a hard ceiling.** 4-second windows at 256 Hz
([eegpt-2024](../collection/eeg-models/eegpt-2024/card.md)), 4.0-second non-overlapping windows in a
third-party harmonised pipeline
([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)), and across
ten reviewed foundation models "context length ... does not exceed 90 seconds"
([kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)). The
window is not free of the spatial axis: [labram-2024](../collection/eeg-models/labram-2024/card.md)'s
256-patch sequence cap couples channel count to window length, the paper's own examples being 64
channels at 4 seconds or 32 channels at 8 seconds, and its card records that the paper reports no
ablation over that trade-off. Two models are constructed to escape the constraint rather than to
satisfy it: [biot-2023](../collection/eeg-models/biot-2023/card.md), where recording length is
genuinely unconstrained because a shorter recording is simply a shorter sentence, and
[brainwave](../collection/eeg-models/brainwave/card.md), whose scale-alignment layer fixes
spectrogram window and hop as a ratio of a 1-second patch so different sampling rates need no
resampling.

**The stimulus epoch, fixed by the design and asymmetric between modalities.** This is the axis the
fusion strand has no representation for.
[simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
states it at word level: "Auditory stimuli are spread out in time, whereas the others are presented
instantaneously." [mous-2019](../collection/candidate-datasets/mous-2019/card.md) shows what
controlling it costs at sentence level — each word's visual presentation duration computed from the
audio duration of the spoken version of the same sentence by an explicit formula with a 300 ms floor
— and records the residual the control does not remove, a trigger-to-auditory-onset delay of slightly
more than 60 ms applying to the auditory half of the sample only, larger than most early evoked
components.

**A window fixed by pretraining is routinely a different window at evaluation, and the corpus records
it happening.** [reve-2025](../collection/eeg-models/reve-2025/card.md) is pretrained on 10-second
segments and fed 30-second windows for HMC and ISRUC, which its card presents as an axis the model
handles. [bendr-2021](../collection/eeg-models/bendr-2021/card.md) pretrains on 60-second sequences
and fine-tunes on 2-second, 6-second and 30-second trials, "which the architecture tolerates".
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) tabulates Sleep-EDF as
2 channels at 100 Hz in 30-second windows, a benchmark preparation parameter that every model in the
comparison inherits regardless of its own native window.

**Different words for the same thing — "epoch" names at least four objects.** A data record and a
30-second sleep-scoring interval, with "window" as a third near-synonym, all inside one specification
([edf-plus](../collection/datasets-benchmarks/edf-plus/card.md)); a stimulus-locked trial segment
and a pass through the training set, used as synonyms in one reference implementation's
documentation ([mne-python](../collection/datasets-benchmarks/mne-python/card.md), where "epoch" and
"trial" are synonyms while "epoch" also does duty as a training hyperparameter). The measurement
strand flags the ambiguity about its own sources; the model strand uses the third and fourth senses
in the same sentence without disambiguation —
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s budget is "50 epochs"
while [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)'s
pipeline z-scores "within each accepted epoch".

**Open questions the literature leaves.**

- What a window-length change costs a pretrained encoder is measured nowhere.
  [labram-2024](../collection/eeg-models/labram-2024/card.md) reports no ablation over the
  channel-count-versus-window-length trade-off its own cap imposes;
  [bendr-2021](../collection/eeg-models/bendr-2021/card.md) states the architecture tolerates the
  change and reports no comparison.
- Whether a 5-second segment supports HRV or a stimulus-locked contrast is declared awkward for both
  by the model that uses it:
  [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md)'s card records
  5 s as "long relative to a stimulus-locked EEG epoch and short relative to reliable HRV
  estimation — an awkward middle for either use", and the paper measures the cost at neither end.
- What looking longer buys the peripheral branch is small where it has been measured and untested
  elsewhere: 2 s to 20 s is worth about 0.012 AUROC in the one entry that sweeps it, and its card
  notes a 20 s window cannot resolve a stimulus-locked contrast at all
  ([wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)).
  [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) does not
  specify its HRV window, so the temporal resolution of its fused decision is unstated.
- Whether an auditory and a visual condition can be epoched comparably is stated as an asymmetry and
  controlled once: [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  names it, [mous-2019](../collection/candidate-datasets/mous-2019/card.md) controls it at sentence
  level and still carries an uncorrected 60 ms auditory offset except where audio traces exist.

---

## 5. Whether peripheral physiology adds information beyond the central signal

**Strands crossed:** `multimodal-biosignals`, `candidate-datasets`, `datasets-benchmarks`,
`eeg-models`.

Four strands hold four different pieces of this question and use four vocabularies for the same
channels.

**The models strand: the peripheral channel is out of contract, and the cards say so about
themselves.** [bendr-2021](../collection/eeg-models/bendr-2021/card.md)'s input contract states that
"reference electrodes, EOG and other auxiliary channels" are dropped.
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)'s Sensor Encoder type vocabulary
has exactly three values (EEG, gradiometer, magnetometer), and its card states the consequence
directly: "an ECG, EOG or respiration channel has no representation in the current model". The one
apparent exception is not a fusion exception:
[biot-2023](../collection/eeg-models/biot-2023/card.md) is pretrained on resting EEG, sleep EEG and
ECG and can be fine-tuned on any of them, one modality at a time, an ECG lead owning a row in the same
name vocabulary as an EEG derivation — cross-modality *pretraining*, not a combined input.

**The benchmark strand: the channels are present, standardized, and discarded.**
[sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) carries horizontal
EOG, submental chin EMG and, in the cassette subset, oro-nasal respiration and rectal body
temperature, and
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) tabulates the dataset as
2 channels at 100 Hz, the two EEG derivations only.
[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) is the
stronger case, because there the exclusion is a protocol requirement rather than a modelling choice:
the three EOG channels "are provided for the subsequent application of artifact processing methods
and must not be used for classification", and the card records that no suite states what it did.

**The candidate strand: the channels exist, in quantity, and their status turns on what the source's
own analysis did with them.** Eight of eleven datasets carry EEG alongside at least one peripheral
modality. [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is the strongest
specification and the weakest evidence at once: 2-channel ECG, 2-channel EOG and a 16-channel
respiration belt, together with a 43-channel EMG neckband, all on the *same* 24-bit BioSemi amplifier
as the EEG at 269 channels per subject — hardware-synchronous, so no cross-device alignment is
required — and no first-party analysis of those channels on record, the paper's own analysis being an
exemplary analysis of a slice.
[mous-2019](../collection/candidate-datasets/mous-2019/card.md) carries bipolar vertical EOG,
horizontal EOG and ECG at 1200 Hz, the same rate as the neural data.

**The fusion strand: the ablation partition, and what the readable arms show.** Only four entries run
three arms on one split. In two of the four the peripheral-only arm sits at or below a trivial
baseline — [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md)'s
three-class ECG arm has a Matthews correlation of 0.0 at 71.3% accuracy, and
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)'s
EDA arm sits below the 67% majority-class rate — yet one of those two reports the strand's largest
gain and the other its smallest. In a third, the peripheral arm beats every EEG arm, so the result is
"EEG adds to ECG" rather than the converse
([kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)).
And the strand contains a mechanistic prediction that the gain should be small:
[zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) reports
descending cortical-to-cardiac coupling as "stronger, more sustained, and spatially focused" than
ascending, which if true makes a cardiac channel closer to a noisy copy of what the encoder already
has than to a new source.

**Three crossings the ontologies cannot make.**

*The same discard, three justifications, no measurement.* The models strand drops the channels as out
of contract, the benchmark strand as not-EEG or as protocol-prohibited, and the fusion strand argues
simultaneously that ocular activity is artifact
([mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md),
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md))
and that it is signal
([wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md),
[ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md),
[hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)).
Neither side of that argument reports what removal costs, and two cards name the same missing arm
independently.

*One dataset, carded in two strands, makes the two questions come apart explicitly.*
[sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) records the
peripheral channels as "present, standardized, and universally discarded";
[sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) records the same channels as
diagnostic signals that sleep staging depends on, "usable as signal by construction". Same
recordings, opposite readings, both correct, because one strand asks what the field did with them and
the other asks what could be done with them.

*The best-specified substrate and the best-measured arms are disjoint.* The fusion strand's cleanest
protocol is the one where the gain evaporates
([azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md),
+0.002 under 5-fold GroupKFold, and gated per fold so that the headline is a mixture of the fused and
the EEG-only model's outputs), while the candidate strand's strongest peripheral specification carries
no arms at all ([strum-2018](../collection/candidate-datasets/strum-2018/card.md)).

**Different words for the same channels.** The fusion strand calls them the *peripheral branch*; the
models strand calls them *auxiliary channels*
([bendr-2021](../collection/eeg-models/bendr-2021/card.md)); the format strand calls them a channel
*type*, EEG / EOG / ECG / EMG / MISC in `channels.tsv`
([eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md)); and the candidate strand sorts them
by *use* — signal versus artifact reference — according to what the source's own analysis did
([deap-2012](../collection/candidate-datasets/deap-2012/card.md), whose four EOG and four EMG
electrodes are simultaneously the standard artifact references and, in an affect paradigm, the
measure of interest). Only the format strand's version is machine-readable, and it records type, not
use.

**Open questions the literature leaves.**

- Whether ocular activity carries task information is argued from both sides, and the arm that would
  settle it is named as missing by cards on both sides:
  [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  reports no "EEG with ocular components projected out" condition, and
  [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  reports no neural decoding with gaze regressed out.
- Whether the cardiac channel is downstream of the cortical state is claimed and unsupported by its
  own accessible record: [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md)
  reports no coefficients, no significance levels and no control for the video stimulus driving both
  signals — which its card calls "the single most important control for a coupling claim of this
  kind" — and the direction detected may be biased by single-lead ECG reconstructing a cardiac
  attractor more cleanly than 32-channel EEG reconstructs a cortical one.
- Whether the coupling prediction or the large fusion gains are right is unadjudicated: the entries
  consistent with redundancy are
  [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md),
  [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
  and the EEG+ECG cell of
  [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)'s
  grid; the two inconsistent entries both carry split or provenance flags.
- Whether the peripheral foundation models work as fusion components is untested by the papers that
  propose them: [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) is framed as
  "both a feature extractor and an encoder for multimodal models" and "no multimodal experiment
  appears in the evaluation".
- Whether published results on the one dataset with an explicit prohibition complied with it is not
  determinable: no suite carded here states what it did with
  [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md)'s EOG
  channels or its mandatory artifact-removal step.

---

## 6. What preprocessing removes, and what nobody ablates

**Strands crossed:** `eeg-models`, `datasets-benchmarks`, `multimodal-biosignals`,
`candidate-datasets`.

**In the models strand, "artifact" is almost always the name of a downstream task rather than a step in an input
contract.** Across the 22 entries the word appears as a benchmark name in
[femba-2025](../collection/eeg-models/femba-2025/card.md) and
[luna-2025](../collection/eeg-models/luna-2025/card.md) (TUAR, artifact recognition and detection),
as a step in a *third party's* harmonisation in
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md), as a
dataset-selection criterion in
[lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) (datasets
"specifically chosen for their minimal spurious artifacts"), and as a finding about what the field
does not do in
[kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md): across
ten models, "most EEG-FMs perform minimal and simple data preprocessing steps, namely filtering and
resampling", outlier removal, artifact suppression and site harmonization "were not explicitly
pursued", and normalization strategies "were not sufficiently described in most studies". One
checkpoint states no sampling rate, filtering or referencing specification at all, the string "Hz"
not occurring in the paper ([femba-2025](../collection/eeg-models/femba-2025/card.md)).

**In the fusion strand, artifact removal is the central dispute.** The step the models strand does not
specify is the one the fusion strand argues about:
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
cleaned "regular artifacts such as heartbeat, blinks and eye movements" and its authors state the
removal "was imperfect", the confound surviving into the result; and
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
applies ICA to remove eye, muscle *and cardiac* interference from its EEG stream while ECG is the
second modality — which its card flags as "the one preprocessing step that would suppress the shared
component" the fusion is supposed to exploit.

**In the benchmark strand, preprocessing is fixed and unablated.**
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) specifies it end to end —
0.1–75 Hz band-pass, notch at the per-site power-line frequency identified by FFT, resampling to
whatever the evaluated model expects, global z-score — and names inconsistent preprocessing as its own
motivation. [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) fixes notch filters
at 50 and 60 Hz plus harmonics, channel-wise robust scaling at recording level and clamping at 20,
while stating that it has not systematically evaluated preprocessing effects. No suite ablates its own
preprocessing.

**In the candidate strand, the procedure and the trap are both on record.**
[snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
establishes that of the two obvious ways to remove an identified confound, post hoc counterbalancing
biases accuracy upward and confound regression biases it downward far enough to produce significant
below-chance performance, and only confound regression performed inside every cross-validation fold
is unbiased. [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md)
relies on ICA rather than on a recorded ocular channel for artifact removal, which is the case
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
reports as insufficient. And
[boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) applies robust
re-referencing through the PREP pipeline, changing the derivation class (§3).

**Normalization is the one preprocessing choice in the corpus with a measured downstream effect, and
it is measured once.** [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md)'s ablation removing
layer normalization on the reconstruction targets *lowers* the pretraining loss while costing 1 to 7
percent downstream — a result whose shape is that the pretraining objective and the downstream
outcome move in opposite directions. Set against
[kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)'s
finding that normalization strategies are not sufficiently described in most studies, and against a
normalization convention travelling down a descent chain unexamined — LaBraM's 100 µV convention
adopted by [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md).

**Different words for the same thing.** What the models strand calls the *input contract*, the
benchmark strand calls the *recipe* or the preprocessing specification, the fusion strand calls a
*pipeline*, and the candidate strand records as *acquisition plus what the release already applied*.
The last is the only version that distinguishes what was recorded from what was distributed, and
that distinction is load-bearing: two candidate datasets are referential by hardware and unstated in
text, so what re-referencing has already been applied to the released data is unknown
([strum-2018](../collection/candidate-datasets/strum-2018/card.md),
[deap-2012](../collection/candidate-datasets/deap-2012/card.md)).

**Open questions the literature leaves.**

- What ocular artifact removal costs in task accuracy is named as missing by two cards arguing
  opposite sides (§5), and by neither side's paper.
- Whether a checkpoint pretrained on minimally preprocessed clinical EEG behaves differently on
  cleaned data is not evaluated by any source:
  [kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)
  establishes that the corpora are minimally preprocessed and does not test the interaction.
- Whether harmonisation produces results or artifacts is flagged by the author who harmonised:
  [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) states that
  the BENDR and LaBraM results "should not be interpreted as clean tests of pretraining objective"
  because of the exceptions the shared pipeline forced.
- Whether a below-chance result is a finding or a symptom has a stated diagnostic and no reported
  instance: [snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
  says significant below-chance accuracy should be read as a symptom of the analysis first, and the
  card is abstract-only, so the simulation parameters, empirical accuracies and exact cross-validated
  procedure are reported by the source and unread here — "no implementation detail should be taken
  from this card".
- Whether preprocessing choices change conclusions is measurable in exactly one tool and measured by
  nobody: [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md)'s
  `method` argument propagates through the internal functions "so that the sensitivity of a result to
  preprocessing choices is measurable rather than assumed", and the card records that the validation
  evidence behind "validated pipelines" is itself not accessible.

---

## 7. What a number is a number over: the comparator and the null

**Strands crossed:** `eeg-models`, `datasets-benchmarks`, `multimodal-biosignals`,
`candidate-datasets`.

Distinct from §1: that theme is about what was held out, this one about what the result is compared
against. The corpus uses six kinds of reference point interchangeably and they are not exchangeable.

| reference point | instance | card |
|---|---|---|
| another pretrained model, and nothing else | every comparator is LaBraM, BrainBERT or MOMENT; the source contains no occurrence of EEGNet, ShallowConvNet, SPaRCNet, BIOT, "from scratch" or the word "baseline" | [brainwave](../collection/eeg-models/brainwave/card.md) |
| the same architecture without pretraining | +10.7 points on PhysioNet-MI ([reve-2025](../collection/eeg-models/reve-2025/card.md)); +2.2 on the same task ([cbramod-2025](../collection/eeg-models/cbramod-2025/card.md)) | — |
| a small supervised network | EEGNet's 72.29 beats every foundation model on Siena and Conformer's 73.84 on HMC | [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) |
| classical handcrafted features | logistic regression at 0.847 on EEGMAT against the best foundation-model tier at 0.755 ([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)); classical features beating frozen REVE by at least 12.7 points under every tested condition ([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)) | — |
| a dummy and a chance baseline, as reported rows | majority class or training-set mean, plus an untrained randomly initialized model, with the metric rescaled against both | [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) |
| the theoretical chance level | shown to be the wrong threshold: classifying pure Gaussian noise reaches "decoding accuracies of up to 70% or higher in two-class decoding" at small n | [combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md) |

**The margins are mostly smaller than the intervals, and the two facts live in different places.**
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s per-dataset margins run
from −0.08 to +15.00 with no interval reported for any cell, and its BCI-IV-2a row has nine subjects;
[varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
puts the error bar at ±15 / ±10 / ±6 / ±3 points at n = 30 / 100 / 300 / 1000, and records that "the
standard error across folds strongly underestimates them" — worst, at a factor of 0.26, for the
scheme with the best true error bars. The measurement strand holds the bound; the model strand's
within-paper ablations and the fusion strand's deltas are reported with no bound attached at all, and
several fusion entries report an accuracy with no chance level or class balance
([salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md),
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md),
[wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md),
whose card says "multiclass" without a class count "makes 0.8780 uninterpretable as an effect size").

**A quoted comparator is not a measured one, and the corpus contains the hazard in two strands.**
[guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md)
names the general form — "there is always a concern that authors applying a method as a baseline may
not be using it to its fullest potential" — and its card marks the caution as applying to every
transfer number in that strand.
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)'s
card states it for itself: "the comparator numbers are quoted from other papers rather than re-run,
so the ranking inherits every difference in preprocessing and splits among them" — and the
consequence is measurable, since its 10.4-point margin over DCCA becomes 1.6 under the first-party
figure (§11).

**The comparator can be defined so that a weak baseline scores well.**
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s transfer score is
relative improvement over a from-scratch counterpart, so a model with a weak from-scratch baseline
scores well for reasons unrelated to representation quality, and the metric is not validated against
anything.

**The corpus contains exactly one cross-dataset inference procedure, in the strand with no pretrained
models.** [moabb](../collection/datasets-benchmarks/moabb/card.md) runs a permutation-based paired
t-test or Wilcoxon per dataset, combines p-values by Stouffer's method weighted by the square root of
subject count, applies Bonferroni across comparisons, and reports a standardized mean difference as
the meta-effect size — and refuses to pool subjects across datasets because "differences in trial
amount, sampling rate, and even location and hardware mean that we cannot expect subjects across
datasets to be naively comparable". Its own reflexive conclusion is the deflationary one: "the sample
size problem in BCIs is bigger than we might have expected".

**Different words for the same thing.** *Baseline* names three different objects across strands: the
same architecture without pretraining (`eeg-models` ablations), a different and smaller architecture
(the suites' supervised comparators), and a pre-stimulus interval used for normalization (the
candidate and fusion strands' acquisition descriptions). *Chance* names the theoretical level, the
majority-class rate, an untrained randomly initialized model
([neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)) and a permutation null
([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)'s
label-permutation control at 0.500), and only one entry reports more than one of them.

**Open questions the literature leaves.**

- By how much the empirical chance level departs from the theoretical one is reported by the source
  and unreadable here: the tabulated levels as a function of sample size, class count,
  cross-validation parameters and classifier "are the part a user would actually apply" and are
  recorded as reported-but-not-accessible
  ([combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)).
- Whether that inflation applies to a fine-tuned transformer is outside the paper's scope by its own
  statement, which studies LDA, naive Bayes and SVMs and predates the deep-learning EEG literature
  (same card).
- Whether learned peripheral representations beat engineered ones is declared unanswerable by both
  entries that would answer it:
  [haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md)
  "predates the peripheral-foundation-model literature and therefore cannot say whether learned
  representations beat these engineered features", and
  [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md)
  records the same absence.
- Whether the field's most reported benchmark can still discriminate is questioned by the review that
  uses it: TUAB "may already have saturated (85-87% accuracy) with traditional approaches", and only
  four of ten reviewed models can be ranked even on TUAB and TUEV
  ([kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)).
- The behavioural read-out criterion is unavailable where it is most needed:
  [ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md)'s
  card records that a passive stimulus condition with no task response has no correct/incorrect split
  to condition on.

---

## 8. Scale is not the variable that orders anything, in either modality

**Strands crossed:** `eeg-models`, `datasets-benchmarks`, `multimodal-biosignals`.

**Six measured observations in the models strand, agreeing in direction.** These are set out in
full in [eeg-models-ontology](./eeg-models-ontology.md) §2.5 and are summarized here only so the
cross-modal claim below has its within-strand half in view; the theme's own contribution starts with
the PPG result that follows.
[labram-2024](../collection/eeg-models/labram-2024/card.md)'s Base model trained on 500 hours exceeds
the same model trained on 2,500 hours on TUAB, the authors concluding "2,500 hours is not the answer".
[femba-2025](../collection/eeg-models/femba-2025/card.md): eight times the parameters for 0.77 points
of TUAB balanced accuracy, with Tiny beating both larger variants under two of four TUAR protocols.
[luna-2025](../collection/eeg-models/luna-2025/card.md): 44 times the parameters for 0.94 points, and
Large beating Huge on SEED-V on all three metrics.
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md): one inversion across eight sizes, the 76M
variant below the 25M one.
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md): "parameter
count alone does not order the models".
[kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md): "the
evidence for data scaling is weak, if any", with NeuroLM's HMC and Workload performance *decreasing*
with larger variants. Two entries sit on the other side:
[reve-2025](../collection/eeg-models/reve-2025/card.md) reports improvement with size while fitting
no scaling law, and [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) reports its tiny
model beating its base model on MDD.

**The same shape in the peripheral literature, with no citation between them.**
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) reports "outperforming models
70 times larger", which its card reads as suggesting "the useful capacity for a single-channel
peripheral signal is small". And
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
frames its own result as "a 5–10% increase in accuracy from multimodal fusion against a 2–3x increase
in computational cost", at 42.7 M parameters against 14.7 M for its EEG-only backbone.

**The one *tested* scaling claim in the corpus is in the benchmark strand, and it does not corroborate
the parameter axis.** [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)'s
factor analysis is the only place in that strand where a Wilcoxon signed-rank test is applied at all —
on per-dataset Spearman correlations, while the leaderboard beside it carries no per-comparison test.
It finds the *number of pretraining datasets* significantly associated with better average rank
(median ρ = −0.27, p = 1.1×10⁻⁷), with publication year at −0.40, log parameter count at −0.21,
training hours at −0.08 and subject count at −0.10. So the axis with a significance test attached is
corpus diversity, not size — and the two archives that supply the field's corpora supply them along
different axes, [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) being the
source of hours and [openneuro](../collection/datasets-benchmarks/openneuro/card.md) the source of
dataset count.

**Hours are not a comparable unit across the corpus.** Four EEG checkpoints never report hours at all
and their cards say so rather than computing a substitute
([bendr-2021](../collection/eeg-models/bendr-2021/card.md),
[biot-2023](../collection/eeg-models/biot-2023/card.md),
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md),
[banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md)).
[tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md)'s headline "29.1 years" is
summed over channels and its card records that it "is routinely misquoted as recording duration".
And the one proposed replacement unit, *channel-hours*, is recorded by its own card as conflating a
long single-channel recording with a short high-density one and as never tested against any outcome
([kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)).

**Open questions the literature leaves.**

- No source isolates model size while holding masking scheme, corpus and architecture fixed — the same
  shape of absence the models strand records for the loss function, where nothing reconciles the four
  positions on raw-signal reconstruction.
- Publication year is the strongest association in the only tested analysis and is offered without a
  mechanism ([omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)).
- Which unit scale should be measured in is unresolved by the entry proposing the alternative, which
  never tests channel-hours against an outcome and could not determine it for some of the ten models
  it reviewed ([kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)).
- Whether the useful capacity for a single peripheral channel really is small is an inference from one
  parameter-efficiency result on one modality, and the card marks it as such
  ([papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md)).

---

## 9. One recording, several roles, and no vocabulary shared between the strands that hold them

**Strands crossed:** `datasets-benchmarks`, `eeg-models`, `candidate-datasets`,
`multimodal-biosignals`.

The corpus's four identifiers carded in two strands each are not an accident of filing; they are the
visible part of a structural property. The same recordings serve as pretraining substrate, as
evaluation benchmark, and as candidate fine-tuning corpus, and each strand names the resulting
problem differently.

- **TUAB and TUEV** are BIOT's and CBraMod's pretraining data and their evaluation sets, per
  [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s Table 7.
- **PhysioNet-MI** is EEGPT's pretraining data, a benchmark it is compared on, the largest of MOABB's
  twelve datasets, and a Brain4FMs task
  ([physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md)).
- **OpenNeuro** is 10,194 of REVE's 61,415 pretraining hours
  ([reve-2025](../collection/eeg-models/reve-2025/card.md)), a NeuralBench data source, the candidate
  strand's access reference point
  ([openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md)), and the host of a
  candidate dataset ([tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md),
  `ds003670`).
- **MOABB** closes a loop the benchmark strand states explicitly:
  [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) reaches its motor-imagery and
  P300 comparison datasets *through* MOABB while
  [reve-2025](../collection/eeg-models/reve-2025/card.md) draws 384 pretraining hours *from* it, so a
  dataset reached through MOABB can be pretraining data for a checkpoint that a MOABB-derived task
  then evaluates ([moabb](../collection/datasets-benchmarks/moabb/card.md)).
- **Sleep-EDF** is a benchmark
  ([sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)), a candidate
  fine-tuning substrate ([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)), and — per
  the candidate card — the cheapest open bipolar substrate on which the midpoint approximation of §3
  could be probed.

**What each strand calls it.** The models strand calls it *in-domain* evaluation or evaluating inside
the pretraining distribution, and generalizes it: in four of ten reviewed studies the downstream
evaluation datasets were already used for pretraining
([kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)), and
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) states
"TUAB is in-domain" directly. The benchmark strand calls it *pretraining-to-evaluation overlap* and
handles it four different ways: hashed bars on the leaderboard with the cells retained
([neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)), silence on whether any of ten
checkpoints saw any of 54 evaluation datasets
([omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)), an assertion of "ensuring
no data leakage" that addresses subject grouping only
([brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)), and publishing both the table that
documents the overlap and the results tables that ignore it
([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)). The candidate strand
does not name it at all.

**The remedy from §1 does not reach it, and one card says so.**
[tuab](../collection/datasets-benchmarks/tuab/card.md) states that even a patient-disjoint fine-tuning
split does not remove the overlap, because the self-supervised pretraining saw the evaluation
subjects' recordings. A holdout unit is chosen at fine-tuning time; the contamination happened at
pretraining time.

**The one design in the corpus that separates the roles in advance is in the peripheral strand.**
[mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) splits
MIMIC-IV-ECG by patient and excludes UHN-ECG from pretraining entirely "to serve as a cross-dataset
generalisation test" — an evaluation corpus reserved at pretraining time rather than a split chosen
at fine-tuning time. Set against the four handlings enumerated above, it is the one entry in either
model strand whose card records the reservation as a design decision rather than the overlap as a
caveat. The peripheral encoder beside it does the same thing one degree less strictly:
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) pretrains on VitalDB, the
MIMIC-III waveform matched subset and the MESA sleep sub-study, and evaluates on 20 tasks across 10
datasets with *some datasets held out entirely as out-of-domain* and held-out test sets retained for
the pretraining datasets — the distinction the four EEG suites either do not draw, do not state, or
draw and then pool into one leaderboard.

**Open questions the literature leaves.**

- Whether overlap inflates results is unanswered by the only suite that raises it:
  [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) keeps the affected cells
  because "we did not notice a clear trend suggesting pretraining 'leakage' improves downstream
  performance on the same data", which its card records as an impression rather than a test, and
  neither excludes nor separately analyses them.
- What the checkpoints actually consumed is not enumerable from the sources:
  [reve-2025](../collection/eeg-models/reve-2025/card.md) names 92 datasets and accounts hours by
  archive (TUH 26,847, PhysioNet 22,707, OpenNeuro 10,194, MOABB 384) rather than per dataset, and
  [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) does not state whether any
  of its ten checkpoints was pretrained on any of its 54 evaluation datasets.
- Whether the field's most reported partition is even patient-disjoint is not asserted anywhere the
  corpus could read: [tuab](../collection/datasets-benchmarks/tuab/card.md)'s thesis describes the
  data as "divided into two sets" without asserting that no patient contributes to both, the parent
  archive averages 1.56 sessions per patient with one patient contributing 37
  ([tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md)), and the release's
  `_AAREADME` sits behind the registration wall.
- Whether a subject-level guarantee is possible for a re-derived subset is unaddressed by the standard
  that would carry it: [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) makes subject
  identity recoverable from the directory structure but nothing obliges a pre-partitioned release to
  document its grouping, which is exactly the reporting requirement
  [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  proposes to a standards body.

---

## 10. What the field distributes, and on what terms

**Strands crossed:** `eeg-models`, `multimodal-biosignals`, `datasets-benchmarks`,
`candidate-datasets`.

Three classes of artefact — model weights, data, and code — and the same omission in all three, split
across four strands so that no ontology sees more than one class of it.

**Weights.** Every EEG model paper that releases weights states no licence for them, and each card
records the omission individually:
[labram-2024](../collection/eeg-models/labram-2024/card.md),
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
[biot-2023](../collection/eeg-models/biot-2023/card.md),
[bendr-2021](../collection/eeg-models/bendr-2021/card.md),
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md),
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md). Two more do not resolve whether
weights exist: [femba-2025](../collection/eeg-models/femba-2025/card.md) releases code without saying
whether the weights are released, and [luna-2025](../collection/eeg-models/luna-2025/card.md)'s
NeurIPS checklist says weights "will be released upon publication" and "we do not release any new
assets yet". The peripheral strand records the identical position for its two released encoders, and
one of its cards makes the cross-strand link itself:
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md)'s card states that "the
licence attached to the released weights is not stated in the extracted text, which is the same gap
the `eeg-models` strand records for its checkpoints";
[mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) is the same case.
**[boundary]** Stated as a set property rather than as an enumeration of the individual cards, the
corpus holds no released checkpoint of either modality with a licence attached.

**Data.** [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) has no data
licence in either the paper or the downloads page — access is a signed form, ssh keys and rsync — and
its card states the consequence precisely: "registration and a signed form are not a licence grant",
with neither document stating redistribution or derivative terms.
[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) is free with
a citation condition and no formal licence.
[openneuro](../collection/datasets-benchmarks/openneuro/card.md) records CC0 called a dedication, a
licence and an agreement in three places in one paper, and as a default rather than a guarantee. The
candidate strand's ladder runs from CC0 through a click-through agreement
([mous-2019](../collection/candidate-datasets/mous-2019/card.md)) and a printed, signed, scanned
end-user licence ([deap-2012](../collection/candidate-datasets/deap-2012/card.md),
[amigos-2021](../collection/candidate-datasets/amigos-2021/card.md)) to request-to-the-authors with no
published route ([strum-2018](../collection/candidate-datasets/strum-2018/card.md), whose abstract
calls it "a new open dataset" against a practical route its card records as contact-the-authors).

**Code.** The one licence stated for any released artefact in the models strand is
[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md)'s MIT, and it covers the
benchmark's own pipeline code rather than a checkpoint.
[makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) records
the split explicitly: the article is bronze open access with no Creative Commons statement while the
software repository is MIT, "and that licence, not the article's, governs use of the code".
[edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) carries no licence statement and no
maintainership statement anywhere on the specification page.

**The article licence and the artefact licence come apart everywhere both are recorded, in two
strands.** Three of four dataset entries in the benchmark strand — a CC BY paper over unlicensed data
for TUH, a CC BY review over an informally released dataset for BCI-IV-2a — and two of the candidate
strand's naturalistic datasets, where
[boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) and
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) are both CC BY-NC-ND as
articles while LiveWire's *data* are CC BY 4.0 and BOA's data licence is not stated in the paper at
all.

**Open questions the literature leaves.**

- Under what terms the released EEG and peripheral checkpoints may be used, fine-tuned or
  redistributed is not stated by any source in the corpus.
- Whether TUH data may be redistributed or derived from turns on a document whose text was not
  retrieved: [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) records the
  signed access form as the thing any redistribution question depends on and as unread.
- Whether archived consent covers model pretraining is raised on one card and answered nowhere:
  [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) records that CC0 "removes
  legal restrictions but not ethical ones" and that a dataset being CC0 "does not certify that its
  consent covers model pretraining".
- What fraction of an archive departs from its stated default is not reported by the archive's own
  paper ([openneuro](../collection/datasets-benchmarks/openneuro/card.md)).

---

## 11. The disagreements about basic quantities are structured, not random

**Strands crossed:** `eeg-models`, `datasets-benchmarks`, `multimodal-biosignals`,
`candidate-datasets`.

Each strand's §6, §8 or §9 registers its own disagreements. Held together, four distinct mechanisms
appear, each with a different hazard, and three of them are invisible from inside a single strand.

**Mechanism 1 — copied baselines.** One measurement travelling through several papers' comparison
tables. [labram-2024](../collection/eeg-models/labram-2024/card.md) takes all baselines from BIOT;
[reve-2025](../collection/eeg-models/reve-2025/card.md) quotes numbers "displayed in existing studies"
except one reproduction; [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) takes baseline
parameter counts from LaBraM; [femba-2025](../collection/eeg-models/femba-2025/card.md) and
[luna-2025](../collection/eeg-models/luna-2025/card.md) share tables with each other. The signature is
that a disagreement follows the chain rather than being random: ST-Transformer's parameter count is
3.5M in the two papers taking their tables from BIOT and 3.2M in the two sharing tables with each
other, and each of the four uses the figure to size a claim about parameter efficiency.

**Mechanism 2 — single-sourced descriptions.** Several cards independently failing to obtain a fact
from primary documentation and each falling back to the same secondary table, honestly. Nearly every
checkpoint-to-corpus fact in the benchmark strand traces to
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s Table 7 or
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)'s Table 1, and so do the *dataset*
parameters: TUAB's 2,383 subjects, TUEV's 370, Sleep-EDF's 78 and BCI-IV-2a's 5,184 are all benchmark
preparation figures, and each of the four cards says so
([tuab](../collection/datasets-benchmarks/tuab/card.md) calling 2,383 "a benchmark artefact",
[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) recording
that 5,184 "is arithmetic (9 × 2 × 288), not a figure stated by either source"). The hazard is that a
reader counts five cards as five corroborations. The aggravating fact is that the single source is
internally inconsistent about exactly the fields it propagates: EEGPT at 198 h in Table 7 against 246
in the body, CBraMod at 9,246 against ~27,000, LaBraM at 2,535 h and 136 channels against ~2,500 h and
137 channels.

**Mechanism 3 — quoted comparators in a strand with no re-runs.** No entry in the fusion strand
re-runs another entry's model, so every cross-entry comparison is a quotation. DCCA on SEED-IV is
87.5% first-party ([liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md))
and 78.74 in a comparator table
([ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)),
an 8.8-point spread that turns a claimed 10.4-point margin into 1.6.

**Mechanism 4 — same-paper card divergence, which is a defect in our records rather than a fact about
the field.** This is the one that only a reader holding all four ontologies can count. The corpus
carries four identifiers in two strands each, and **all four pairs diverge**:

| identifier | divergence | filed by |
|---|---|---|
| AdaBrain-Bench | LaBraM at 137 channels from the body, unflagged ([adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md)) against 136 from Table 7 with the conflict flagged ([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)); and EEGPT at 246 h against 198 h, same pair of cards | pilot §6.1 and `datasets-benchmarks` §8.1 |
| EEG-BIDS | `electrodes.tsv` recorded as flatly "recommended, not required" ([eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md)) against the source stating the requirement level two ways with the ambiguity flagged ([eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md)); plus "only two" formats against four permitted | `candidate-datasets` §9.1a and `datasets-benchmarks` §8.1 |
| OpenNeuro | the abstract's rounded figures ([openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md)) against exact figures plus three flagged internal inconsistencies including the unreconciled 604-versus-502 gap ([openneuro](../collection/datasets-benchmarks/openneuro/card.md)) | `candidate-datasets` §9.1a |
| Sleep-EDF | "roughly 3,450 hours by arithmetic" ([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)) against an explicit refusal to compute a total ([sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)) | `candidate-datasets` §9.1a |

The pattern within the pattern, stated more carefully after review. In **three** of the four the
divergence is not two cards asserting different facts but **one card flagging an ambiguity in the
source and the other not**. Sleep-EDF is the exception and is a different shape: both cards flag,
and they applied opposite conventions to the same non-figure, one computing a total by arithmetic
and one declining to. Of the three that do share the shape, the sub-claim that the unflagging card
is the one whose strand builds an argument on the value is attested for EEG-BIDS; for AdaBrain the
argument rests on an undisputed value, and for OpenNeuro the second card is used for licence and
access rather than scale. A synthesis
document cannot fix a card; the entries are named so they can be filed.

**How far a single disputed quantity propagates.** BENDR's parameter count is 0.39M
([femba-2025](../collection/eeg-models/femba-2025/card.md)), 3.97M
([brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)), 157M
([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)) and
unpublished by the model's own paper
([bendr-2021](../collection/eeg-models/bendr-2021/card.md)). The spread is nearly three orders of
magnitude and it is load-bearing twice, in two strands. First,
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)'s conclusion
that parameter count does not order the models rests specifically on BENDR being the largest model in
its panel and not the best; under either of the two smaller figures it is among the smallest. Second,
BENDR is one of the ten checkpoints over which
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) computes its
log-parameter-count correlation with per-dataset rank (ρ = −0.21), and that suite's own per-model
counts are not recoverable from what was read of it. A published correlation is therefore computed
over a quantity this corpus holds at three orders of magnitude of spread, with no way to check which
value entered it.

**Two more that are load-bearing across strands.** BIOT's fixed channel count is 16 in its own paper
([biot-2023](../collection/eeg-models/biot-2023/card.md), "the common 16 bipolar montage channels")
and 18 in the benchmark that builds an argument on it, calling that count the model's bottleneck
against 62-channel downstream tasks
([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)) — a cross-strand
disagreement between a benchmark's account of a checkpoint and the checkpoint's own paper, and not a
corpus defect. And whether DEAP carries an ECG channel is held three ways by three cards in two
strands — as an inferred modality tag
([li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md),
marked provisional by its own card), as an enumeration of eight peripheral channels containing no ECG
([ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)),
and as an unresolved self-contradiction inside the DEAP paper itself, one enumeration naming
"electrocardiogram" while the sensor-placement figure does not
([deap-2012](../collection/candidate-datasets/deap-2012/card.md)). The candidate card names why it
matters rather than treating it as pedantry: "blood volume pulse and ECG support different
heart-rate-variability measures, and the third comparison would be built on whichever one is actually
there".

**Source self-contradiction is a property of the corpus rather than of any entry.** Fourteen of 22
`eeg-models` entries, fourteen of 18 `datasets-benchmarks` entries and seven of 19
`candidate-datasets` entries carry at least one, each recorded faithfully by its own card with both
readings preserved. This is the second kind of contradiction and conflating it with the first would be
a defect: the disagreement is in the literature, not in our records.

**Open questions the literature leaves.**

- BENDR's parameter count cannot be adjudicated against a primary, because
  [bendr-2021](../collection/eeg-models/bendr-2021/card.md) publishes no total; nor can NeuroLM's
  169.60M against 1.7B, because no card exists for that model.
- AdaBrain-Bench's Table 7 disagrees with its own body about hours or channels for three of four
  checkpoints, and the benchmark builds an argument about EEGPT's scale by comparing those very
  figures against the others
  ([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)).
- Whether "channels" means electrodes, a benchmark's channel selection, or derivations is left
  unresolved by the corpus documentation, and one card states the distinction the sources never make
  ([tuev](../collection/datasets-benchmarks/tuev/card.md)).
- Whether a headline efficiency claim is supportable is undecidable inside the paper that makes it:
  [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) reports its model size three ways that
  cannot all be true — 10M in the abstract, 4.7M and 25M in the results tables, 101M for the variant
  the text says was used everywhere — and its card adopts 101M by matching accuracies, noting that any
  efficiency claim derived from the abstract's 10M is unsupported.

---

## 12. Theme-by-strand matrix

The rule this document has to discharge in place of a coverage table: every theme crosses at least
two strands. `E` = `eeg-models`, `D` = `datasets-benchmarks`, `M` = `multimodal-biosignals`,
`C` = `candidate-datasets`.

| theme | E | D | M | C | strands |
|---|:-:|:-:|:-:|:-:|:-:|
| 1. The holdout unit | • | • | • | • | 4 |
| 2. Identity rather than task | • | • | • | • | 4 |
| 3. Spatial identity and derivation | • | • | | • | 3 |
| 4. Temporal scale | • | • | • | • | 4 |
| 5. Peripheral information | • | • | • | • | 4 |
| 6. Preprocessing | • | • | • | • | 4 |
| 7. Comparator and null | • | • | • | • | 4 |
| 8. Scale does not order | • | • | • | | 3 |
| 9. One recording, several roles | • | • | • | • | 4 |
| 10. Terms of distribution | • | • | • | • | 4 |
| 11. Structured disagreement | • | • | • | • | 4 |

Theme 5 draws on `multimodal-biosignals` for the arms, `candidate-datasets` for what the data
carries, `datasets-benchmarks` for what the suites discard, and `eeg-models` for the input contracts
that exclude the channels; theme 8's `multimodal-biosignals` contribution is
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) and
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
rather than the strand's centre of gravity. Theme 3 has no `multimodal-biosignals` component because
that strand's spatial content is peripheral electrode placement rather than scalp geometry, and theme
8 has no `candidate-datasets` component because that strand records recording scale rather than model
scale.

---

## 13. Terms that name the same thing across strands

Collected because the ontologies structurally cannot: each records the vocabulary drift it sees
inside its own strand, and drift between strands is visible only from here. Every row is grounded on
a card that states the usage.

| the thing | `eeg-models` | `datasets-benchmarks` | `multimodal-biosignals` | `candidate-datasets` |
|---|---|---|---|---|
| holding out whole people | cross-subject, subject-wise, leave-one-subject-out ([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)) | subject-disjoint, leave-subjects-out, subject-level 8:1:1, "proper" ([kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)) | subject-independent, GroupKFold, patient-ID-level ([azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)) | manipulation geometry: within- versus between-subject ([mous-2019](../collection/candidate-datasets/mous-2019/card.md)) |
| the nuisance variable that is more decodable than the label | the identity trap, dataset identity ([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md), [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)) | covariate shift, improper partitioning ([kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)) | trial fingerprints, confound ([rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)) | exemplar rather than category; confound ([simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)) |
| a set of electrode positions | electrode layout, and "montage" loosely ([reve-2025](../collection/eeg-models/reve-2025/card.md)) | electrodes and coordinate system, distinguished from channels ([eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md)) | — | montage, used for a cap layout ([strum-2018](../collection/candidate-datasets/strum-2018/card.md)) |
| a difference between two electrodes | bipolar derivation, or a channel name ([biot-2023](../collection/eeg-models/biot-2023/card.md)) | montage, derivation and re-referencing in one sentence ([edf-plus](../collection/datasets-benchmarks/edf-plus/card.md)) | — | derivation scheme ([sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)) |
| a segment of signal fed to a model | window, patch ([eegpt-2024](../collection/eeg-models/eegpt-2024/card.md)) | window; also data record, sleep interval, and training pass, all as "epoch" ([edf-plus](../collection/datasets-benchmarks/edf-plus/card.md), [mne-python](../collection/datasets-benchmarks/mne-python/card.md)) | window, segment, epoch ([kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)) | trial, epoch ([strum-2018](../collection/candidate-datasets/strum-2018/card.md)) |
| a non-EEG channel on the same recording | auxiliary channel, dropped ([bendr-2021](../collection/eeg-models/bendr-2021/card.md)) | channel type in `channels.tsv`; artifact reference ([eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md), [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md)) | the peripheral branch, the peripheral modality ([ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)) | signal versus artifact reference, decided by what the source's analysis did ([deap-2012](../collection/candidate-datasets/deap-2012/card.md)) |
| ocular measurement | not represented | channel type `EOG` ([eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md)) | `eog` as a controlled tag covering both electrooculography and eye tracking, with six cards recording the substitution ([wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)) | EOG channels, with their placements recorded ([boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md)) |
| evaluating on data the model was trained on | in-domain evaluation ([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)) | pretraining-to-evaluation overlap, leakage ([neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)) | — | not named |
| the reference a result is measured against | baseline, meaning the same architecture unpretrained ([cbramod-2025](../collection/eeg-models/cbramod-2025/card.md)) | supervised comparator, dummy, chance, ceiling ([neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)) | unimodal arm, EEG-only arm ([angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)) | ground truth, label source ([hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md)) |

The `eog` row is worth reading twice. The fusion strand's controlled vocabulary was fixed so a
modality matrix could be built mechanically, and it is doing that job — but six of its entries carry
an `eog` tag whose instrument is an eye tracker rather than electrooculography electrodes, and every
one of those cards states the substitution itself. The format strand's `channels.tsv` type is the only
machine-readable version of the same distinction anywhere in the corpus, and it records the electrode
type, not the instrument. The candidate strand records placements. Three levels of specificity, one
tag.
