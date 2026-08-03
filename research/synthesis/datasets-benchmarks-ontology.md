# Ontology of the `datasets-benchmarks` strand

Phase 3 synthesis, strand C. Input is the 18 entries in
`research/collection/datasets-benchmarks/` and nothing else; where a fact is grounded in a sibling
strand's card, that card is linked instead.

This strand asks how the field measures transfer and whether the measurement can be trusted. This
document says what the strand contains and how its pieces relate. It is not the gap analysis: it
does not enumerate what the field is missing, does not rank suites or datasets, and does not
recommend an evaluation protocol. Where two suites disagree, both prescriptions are recorded and
neither is preferred — the disagreement is the finding. Where a claim is repeated by several cards
but traces to one table, it is counted once and the repetition is named as repetition.

Every concrete claim below carries a card link. Every leaf of every facet is a card link. All 18
entries appear; the coverage table at the end says where each one sits.

**Relation to the pilot.** `eeg-models-ontology.md` §3 covers evaluation protocol from the model
side: which checkpoint was measured by whom, under which adaptation regime, against what baseline,
and what split its own paper used. This document covers the same territory from the measurement
side: what an instrument fixes, what it leaves free, where two instruments disagree, and how large
the instrument's own error is. The two overlap at exactly one place — the linear-probe versus
fine-tuning reordering — and the pilot reads it as a property of the checkpoints while §2.2 below
reads it as a property of the suites. Nothing else is duplicated deliberately; where a fact appears
in both, this document says so and links across.

---

## Why these facets, and not the brief's five categories

`_briefs/strand-datasets-benchmarks.md` scopes the strand into five categories: pretraining corpora,
downstream benchmarks, benchmark suites, protocol conventions and their critiques, and formats and
tooling. The collection was run against those categories and the strand's `INDEX.md` is organized by
them. This ontology departs, for three reasons visible in the index and the cards themselves.

**Categories 1 and 2 are not disjoint in this corpus, and the entries that break the boundary are
the ones that matter most.** The index files [tuab](../collection/datasets-benchmarks/tuab/card.md)
and [tuev](../collection/datasets-benchmarks/tuev/card.md) under "downstream benchmarks", and the
TUAB line in the index itself says in bold that BIOT and CBraMod "were both pretrained on it and are
then evaluated on it". [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) is
EEGPT's pretraining data and a benchmark it is compared on; TUH data is both the substrate under
four checkpoints and, through its two derived subsets, the field's two most reported evaluation
sets. A partition that separates "what a model was made from" from "what a model is scored on"
cannot hold when the same recordings are both.

**Category 3 supplies categories 1 and 2 with their facts.** Three of the five index sections carry
a trailing paragraph beginning "also bearing on this category" or "cross-referenced from category
3", because the load-bearing content would not stay in one box. Nearly every checkpoint-to-corpus
fact carded on the five dataset entries is sourced to one table in
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) or one in
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md). That is a structural property of
the corpus — see §5.2 — and a category scheme that hides it invites a reader to treat five cards as
five sources.

**The property that most changes how a number should be read is not the category an entry sits in
but what unit of data was held out**, and that axis runs through categories 2, 3 and 4 and touches
5: a format that cannot reliably express which file belongs to which session cannot support a
session-wise split ([edf-plus](../collection/datasets-benchmarks/edf-plus/card.md)), and a standard
that does not oblige a pre-partitioned release to document its grouping cannot deliver the reporting
requirement a critique paper demands ([eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md),
[kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)).
That axis is invisible in the index.

The facets below are eight questions a reader can ask of any entry:

1. **Split protocol** — what unit is held out, and what the corpus measures about the cost of
   holding out a smaller one (§1).
2. **What each suite fixes and what it leaves free** — the instrument's specification, and where the
   instruments disagree (§2).
3. **The measurement's own uncertainty** — where the null sits, how wide the interval is, and
   whether anyone tests (§3).
4. **The corpus layer** — what the checkpoints were made from, on what terms, and how far the
   evaluation sets sit inside the pretraining ones (§4).
5. **The checkpoint-to-benchmark mapping** — who has been measured on what, and which two tables the
   mapping comes from (§5).
6. **The substrate** — what the formats and the reference reader make recordable at all (§6).
7. **Reported-but-unread versus never-reported** — a distinction carried forward from collection,
   because it decides whether re-retrieval is worth anything (§7).
8. **Where the corpus disagrees with itself** — a register, not a resolution (§8).

Nodes 1 and 2 are the two that reorder the strand relative to the index. Node 1 is the sharpest axis
because a change of holdout unit is measured, in this corpus, to move a headline number by up to
46.8 percentage points onto an interval containing chance
([eeg-models/brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)),
which is larger than any difference between checkpoints anywhere in §5. Node 3 is the axis the
pilot does not cover at all.

---

## 1. The split-protocol axis: what unit is held out

The question this node answers: for any number in the corpus, which data unit was held out, and what
does the corpus establish about what changes when a smaller unit is used.

### 1.1 The measured cost of moving the boundary

Two entries measure it directly, on different populations, with different mechanisms, and they agree
in direction. They are independent measurements, not one claim repeated.

- [eeg-models/brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
  — the segment-versus-subject boundary, in the clinical setting. The same convolutional network on
  the same Alzheimer's EEG scores 99.8 percent (95% CI 99.1–100.0) under segment-based holdout and
  53.0 percent (43.1–64.8) under subject-based holdout, an interval that contains the 50 percent
  chance level; Wilcoxon T = 0.0, p = 0.002. That is an inflation of 46.8 points. On a
  *within-subject* seizure task the same manipulation costs 14.0 points, 79.1 against 65.1, so the
  leak is not confined to between-subject diagnosis. The mechanism is that segments of EEG from one
  subject resemble each other more than segments from different subjects. Of 63 surveyed
  deep-learning EEG studies published since 2018, only 17 — 27.0 percent — unambiguously avoided the
  flawed design. The card records the survey's own bound: Google Scholar plus reference chasing over
  six conditions, non-exhaustive, with no inter-rater statistic, so 27.0 percent is a property of a
  convenience sample rather than an estimate over the field.
- [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  — the participant boundary, in the cognitive-state setting. Cross-participant models built twice
  on each of five datasets with training and test volume held constant. **Not five replications:**
  the card was corrected here, and only three of the five reproduce a published model (Min et al. on
  driver fatigue, Ni et al. on confused students, Farsi et al. on alcoholism). For PTSD and
  schizophrenia the authors state there was nothing to replicate — "there is no machine learning
  workflow we are attempting to replicate" — so those two use the authors' own multilayer
  perceptron, plus a random forest on schizophrenia. That matters for how the entry is weighted: two
  of the five cells compare a protocol against itself on a model of the authors' choosing rather
  than against a published result. Error rises on every one: driver fatigue 0.09 → 0.466, confused
  students 0.31 → 0.416, alcoholism 0.16 → 0.31 against a chance error of 0.36, PTSD 0.005 → 0.197,
  schizophrenia 0.008 → 0.50 where "no model was able to perform better than random chance" — one
  dataset at chance, not two. The mechanism is formalized rather than asserted: covariate shift
  under the Shimodaira loss-rescaling weight, evidenced by principal-component weight-ratio heat
  maps and by t-SNE embeddings that cluster by participant, and confirmed by a manipulation. The
  manipulation is narrower than an earlier version of this bullet said: of the two transformations
  that artificially reduce inter-participant variability, only shift-to-median raises
  proper-protocol accuracy (entropy features 0.50 → 0.80, spectral 0.50 → 0.72) while leaving the
  improper numbers untouched at 0.91 and 0.82, "because the model has seen each participant's input
  distribution". The other, shifted Heaviside, leaves proper accuracy at 0.50 and 0.47 and *lowers*
  the improper figures by 19 and 16 points, which the paper reads as reduced variability without a
  performance effect.

Two further properties of this node, both stated by the cards rather than inferred.

The prevalence figures are independent and close: 17 of 63 in Brookshire's survey, and 23 of 108
cross-participant models in the Roy et al. 2019 review that
[kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
cites, with cross-participant studies outnumbering within-participant ones by over 5:1.

And the rule has a stated exemption.
[kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
explicitly permits the improper protocol where the inference is narrower — "if a cross-participant
model is only intended to perform classification on the same population that it is training upon
... then ensuring the model is tested with unseen individuals is not necessary" — provided the paper
says so. The paper does not reject cross-validation either: "CV merely needs to be modified so that
for each fold, participants used in training are not also used for validation."

### 1.2 The units between segment and subject, which each critique names as its own limit

The two entries above have a two-valued vocabulary, and each says so about itself:

- [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  — "the word 'session' appears only descriptively, never as a partitioning unit". Its
  proper-versus-improper dichotomy collapses record-wise splitting, window-overlap leakage and every
  other non-participant-disjoint scheme into one category. Its own improper condition mixes two
  mechanisms without separating them: for the confused-students dataset the data were segmented with
  overlapping windows (15 samples, sliding by 12) and then shuffled, so participant overlap and
  window overlap leak together.
- [eeg-models/brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
  — "its vocabulary is subject versus segment only", and the card names session-level leakage as
  unexamined: a subject-wise split still permits the same session to be split across folds where a
  dataset has multiple recordings per subject.
- [varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
  — "'session' and 'run' are used interchangeably and neither is defined", though the paper does
  state the design principle: with several sessions per subject, care must be taken to avoid having
  different sessions of the same subject in train and test, "to prevent subject-identification to be
  driving prediction".

The structural point, which follows from those three self-declared limits together with §1.3 and
which no single card states: **two of the four foundation-model suites define a primary or secondary
protocol at precisely the boundary none of the three critiques measures.**
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s multi-subject setting is
"same subject cohort, held-out recording sessions or trials", and
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)'s multi-subject setting
splits each subject's samples 8:1:1 over trials and pools across subjects. Both report those numbers
on the same leaderboards as their cross-subject ones. *(This sentence states a relation between
entries, which is Phase 3; the further step — that the corpus therefore cannot say what a session-wise
split is worth — is a property of the set and belongs to Phase 4. Marked.)*

### 1.3 Where each suite puts the boundary, and whether it estimates the variance at all

| suite | holdout unit | ratio | resampling | what varies across runs |
|---|---|---|---|---|
| [moabb](../collection/datasets-benchmarks/moabb/card.md) | **none** — within-session | 5-fold | within-session 5-fold CV, splits identical across pipelines | fold |
| [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) | subject (test subjects "explicitly excluded from training") | **not stated in the paper** | apparently single splits; few-shot averaged over 3 runs | few-shot sampling only |
| [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) | subject | 8:1:1 | 3 pre-generated fixed splits from different seeds (5 for few-shot and channel masking) | the split |
| [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) | subject ("leave-subjects-out") | ≈3:1:1 | group-wise cross-validation, subject as grouping variable | fold |
| [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) | **per task**, one of four strategies | per task | a single train/valid/test partition per task | weight initialization only (3 seeds) |

Two relations across the row set, each recorded on a card:

- [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) makes the second-order point
  explicitly: because it runs group-wise cross-validation while OmniEEG-Bench runs three fixed
  seeded splits and AdaBrain-Bench appears to run single splits, "the three suites also differ in
  how much of the reported variation is estimated at all, not only in where the boundary falls".
- [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) states the consequence of its
  own choice: three seeds varying only weight initialization means "the reported standard errors do
  not capture split-to-split variance at all", and the authors name single-partition evaluation as a
  limitation and invite stochastic partitioning.

[neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)'s four strategies are worth
enumerating because they are the widest position in the set: "(1) predefined splits when provided by
the authors, (2) 'leave-concept-out' for cognitive decoding tasks, (3) cross-subject splits, with
optional stratification for clinical tasks, or (4) random splits when very few examples are
available." Its own card identifies option 4 as the sharpest disagreement in the set, because a
random split over segments is the protocol
[eeg-models/brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
shows inflates accuracy by tens of points. The suite's mitigation is labelling: each results panel
carries its split type and its example count, which makes NeuralBench the only source in this strand
where a reader can see, per task, which protocol produced the number. The labelled random-split
numbers nonetheless enter the same average-rank computation as the cross-subject ones.

[moabb](../collection/datasets-benchmarks/moabb/card.md) is the only entry whose primary protocol is
not subject-disjoint at all, and it is deliberate and flagged: within-session five-fold
cross-validation "represents the best-case scenario for any pipeline, with minimal
non-stationarity", and because of that "regularization is at its least useful — which means that it
would be inappropriate to dismiss regularization in the case of CSP out of hand". Cross-session is
named once as future work and described as "a task that is currently infeasible" given how few
multi-session datasets existed. The card draws the comparability consequence: a MOABB number and a
cross-subject number from any other suite are not comparable quantities even on the same dataset.

### 1.4 Splits that are inherited from a distributed artifact rather than established by the paper

For the three most-reported benchmarks in this strand, the partition is a property of the released
data, and its grouping is undocumented in public.

- [tuab](../collection/datasets-benchmarks/tuab/card.md) — a fixed train/evaluation partition ships
  with the corpus (full set: 1,387 normal plus 1,398 abnormal training files against 150 normal plus
  130 abnormal evaluation files). The document the corpus itself names as its description, Lopez de
  Diego's 2017 master's thesis, describes selection, demographic balance, file counts, **patient
  counts per partition** (2,138 training, 253 evaluation) and hours (1,064.7 and 104.4), and says
  the data "was divided into two sets", **without asserting that no patient contributes to both**.
  Counting patients separately on each side is consistent with disjointness and does not state it,
  which is the corrected form of this point: the card no longer says the thesis counts only files.
  The parent archive averages 1.56 sessions per patient and one patient contributed 37
  ([tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md)), so the question is
  live rather than pedantic. Every foundation-model TUAB number in this corpus inherits that
  partition. The card is careful about its own epistemic position: it is very likely patient-disjoint
  in the released versions, but the card cannot say so from what was read, and the release's
  `_AAREADME` sits behind the registration wall (see §7).
- [tuev](../collection/datasets-benchmarks/tuev/card.md) — the same, one degree worse: the corpus
  page carries no descriptive document for TUEV at all, so participants, channels, sampling rate,
  hours, class balance and the partition are all unknown from the primary source, and everything
  quantitative on the card comes from benchmark papers.
- [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) — the
  labels for the second session were withheld during the competition and released afterwards, so
  every modern result on this dataset is post-hoc work on released test labels (§1.5).

The pattern extends into the model strand: [eeg-models/reve-2025](../collection/eeg-models/reve-2025/card.md)
reuses the TUEV splits of CBraMod, LaBraM and BIOT "for comparability" rather than defining its own,
which [tuev](../collection/datasets-benchmarks/tuev/card.md) records from the other direction.

### 1.5 The one protocol in the strand built to resist these failures, and its stated expiry

[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) is the
strand's clearest historical example of an evaluation regime designed against overfitting, and its
components have no analogue in any modern suite carded here: test labels withheld, so "software had
to be submitted" rather than predicted labels; "All algorithms had to be causal"; and "in
order to check whether the causality criterion and the artifact processing requirements were
fulfilled, all submissions had to be open source". The organizers also forbade non-causal
exploitation of the unlabelled test block, noting they were "aware of the problem, that this use of
data is non-causal and unrealistic". The competition metric was kappa, with chance at κ = 0, and the
winner reached 0.57 averaged over nine subjects against 0.52, 0.31, 0.30 and 0.29.

The same review states the regime's expiry in advance, in three sentences the card records: any
post-competition improvement "should be reported with a note of caution, as it could merely reflect
random fluctuations"; "any post-competition work on the same data has been performed under the
advantage of knowing the competition outcome, knowing the specific shortcomings of the submitted
algorithms"; and the test labels' "use should be restricted to finally determine the performance of
a method". The review also disclaims systematicity for itself: "the competitions are by no means a
systematic evaluation of all available algorithms". None of
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md),
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md),
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) or
[neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) withholds test labels, and none
acknowledges the released-label status of this dataset.

---

## 2. What each suite fixes and what it leaves free

A suite that fixes the adaptation recipe is answering a different question from one that fixes only
the datasets. This node states, per suite, which variables are held and which are released, because
that determines what its leaderboard is a leaderboard of.

### 2.1 The specification matrix

| | [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) | [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) | [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) | [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) | [moabb](../collection/datasets-benchmarks/moabb/card.md) |
|---|---|---|---|---|---|
| scope | 13 datasets, 7 task families | 54 datasets, 6 task families | 22 tasks from 18 datasets, scalp + intracranial | 36 tasks, 94 datasets, 9,478 subjects, 13,603 h | 12 datasets, 275 subjects, one paradigm |
| split rule | subject-disjoint test; ratio not in the paper | 8:1:1 subject-level | ≈3:1:1 leave-subjects-out, group-wise CV | one of four strategies per task, incl. random | within-session 5-fold |
| primary adaptation | **full fine-tuning**, linear probing secondary | **linear probing**, full fine-tuning additionally on every dataset | full fine-tuning only; no linear-probing protocol defined | end-to-end fine-tuning under one shared recipe | not applicable, classical pipelines |
| budget | 50 epochs, batch 64, AdamW wd 0.05, LR grid-searched per strategy/setting, no early stopping mentioned | linear head over frozen backbone; sampling capped at 40 samples per subject per class | up to 50 epochs, early stopping patience 5, Adam/AdamW, **original optimizers retained for some models** | linear projection head over average-pooled tokens, AdamW | hyperparameters by cross-validation; nesting not stated |
| primary metric | balanced accuracy; secondary per dataset; plus a transfer score | balanced accuracy, mean ± sd, ranked by average rank | AUROC-led, split by task type: AUROC/accuracy/F1/F2 for binary, AUROC/accuracy/macro-F1/Cohen's κ for multi-class | one metric per task type; plus normalized score against dummy and ceiling | ROC-AUC |
| uncertainty | none on the leaderboard | sd over 3 or 5 runs; no per-comparison test | sd across CV folds | sd over 3 initialization seeds | **per-dataset test, Stouffer combination, Bonferroni, effect size** |
| checkpoints | BIOT, EEGPT, LaBraM, CBraMod | BENDR, BIOT, LaBraM, CBraMod, BrainOmni, FEMBA, Neuro-GPT, NeuroLM, EEGMamba, REVE | SppEEGNet, BIOT, BENDR, MBrain, Brant, BFM, BrainBERT, CBraMod, NeuroGPT, LaBraM, BrainWave, REVE, BrainOmni, EEGPT-1, NeuroLM | BENDR, LaBraM, BIOT, CBraMod, LUNA, REVE | **none** |
| supervised comparators | EEGNet, LDMA, ST-Tran, Conformer | EEGConformer, EEGNet | SPaRCNet, DeprNet, CCNSE, MSCARNet — purpose-built per task family | ShallowFBCSPNet, Deep4Net, EEGNet, BDTCN, ATCNet, EEGConformer, SimpleConvTimeAgg, CTNet, plus handcrafted, chance and dummy baselines | six classical pipelines |

Two entries in that table are worth pulling out because they are the only ones of their kind in the
strand. [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) is the only suite whose
supervised comparators are purpose-built per task family rather than generic EEG networks — SPaRCNet
for epilepsy, DeprNet for depression, CCNSE for sleep staging, MSCARNet for communication and
affective computing — and it finds SPaRCNet outperforming three foundation models on epilepsy in
both AUROC and accuracy, and DeprNet remaining "a strong baseline" on MDD-64 though surpassed by
REVE, BrainOmni and BrainWave. And [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)
is the only one carrying a dummy baseline (majority class or training-set mean) and a chance baseline
(an untrained randomly initialized model) as reported rows, and the only one that rescales its
metric against them: `s̃ = (s − s_dummy)/(s_perfect − s_dummy)`.

### 2.2 The disagreement is demonstrated inside the corpus, not merely asserted between cards

Each of the four suite cards records the conflict with its siblings in its own "Open questions /
limitations", in near-identical terms, and each closes with the same sentence — that which protocol
should govern is a Phase 3 question. This section answers only the descriptive half of that: what
the disagreement is, and what evidence exists that it changes conclusions.

**The demonstration.** [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) runs
both regimes on the same ten checkpoints and the same 54 datasets and reports that "the model
rankings change substantially" between them. Under its primary cross-subject linear-probing protocol
BrainOmni takes the best average rank, followed by CBraMod and REVE; under full fine-tuning CBraMod,
LaBraM and FEMBA lead at average ranks 4.51, 4.88 and 5.42. Held against a fixed reference point the
reordering is sharper still: under full fine-tuning seven of ten foundation models beat EEGConformer
(average rank 7.25) and nine beat EEGNet (8.24), while under linear probing only five beat
EEGConformer and five fall behind it, which the authors summarize as "frozen pretrained
representations remain substantially limited for direct transfer".

**The second demonstration, inside the other suite.**
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) finds the same regime
dependence with the opposite sign for one checkpoint: CBraMod on BCI-IV-2A falls from 47.71 under
full fine-tuning to 32.32 under linear probing, while EEGPT *rises* from 25.81 to 47.89 on the same
dataset and from 70.21 to 73.82 on HMC, which the authors attribute to overfitting of its larger
parameter count under full fine-tuning. So the regime does not simply scale all models down; it
exchanges their order. The model-side reading of the same numbers, including that AdaBrain-Bench
changed protocol per model as a result, is at
[eeg-models/adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) and pilot
§3.5.

**The disagreement, stated as five positions rather than resolved.** On the holdout boundary:
within-session only ([moabb](../collection/datasets-benchmarks/moabb/card.md)), subject-level at
8:1:1 ([omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)), leave-subjects-out
at ≈3:1:1 with group-wise cross-validation
([brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)), subject-disjoint at an unstated
ratio ([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)), and per-task
choice among four including random
([neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)). On the adaptation regime:
full fine-tuning primary (AdaBrain-Bench, Brain4FMs, NeuralBench), linear probing primary
(OmniEEG-Bench), not applicable (MOABB). Because the regime reorders the models and the boundary
moves the absolute values, two suites reporting on the same checkpoint and the same dataset are not
reporting the same quantity, and no entry in this corpus converts between them.

### 2.3 Whether the adaptation recipe is a nuisance parameter or part of the model: four answers

- [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) — the recipe is a
  nuisance parameter and is fixed. Preprocessing is specified end to end: 0.1–75 Hz band-pass, notch
  at the power-line frequency identified per site by FFT, resampling to whatever the evaluated model
  expects, z-score normalization using global statistics across all trials, with 95th-percentile
  normalization for SHU and a rescale to roughly [−1, 1] for Things-EEG as the stated exceptions.
  Models with incompatible channel requirements (BIOT, EEGPT) are given a 1×1 channel-wise
  convolution to adapt. Its stated motivation is exactly this: "even for identical tasks, the data
  splitting strategies and data preprocessing pipelines are inconsistent across studies, causing
  significant performance fluctuations".
- [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) — the recipe is fixed and the
  fixing is named as a limitation. One shared end-to-end recipe for all models, "to focus the
  comparison on model architecture and pretraining methodology", with the authors flagging that
  "alternative strategies, such as linear probing, parameter-efficient finetuning ... may further
  improve performance and differentiate models from one another".
- [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) — the recipe is partly released.
  For a small number of models the authors' original optimizers were retained "to avoid unintended
  performance degradation caused by altering model specific training designs". This is the only
  suite that treats a model's own training design as part of the model rather than as a variable to
  standardize.
- [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) — the recipe is fixed at
  its most restrictive, and the restriction bounds the data. Sampling is capped at "up to 40 samples
  per subject per class for linear probing", justified by a variance-stabilization analysis, "from
  which all subsequent splits derive". The card records the untested interaction: two datasets with
  the same subject count but very different trials-per-subject are reduced to comparable training-set
  sizes, which may flatten real differences in data efficiency.

[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) also fixes the storage
layer — 54 datasets unified behind one HDF5 schema whose root level holds subject-level attributes
such as montage and sampling rate — and specifies each task with a task-card covering preprocessing,
inputs and outputs, and metrics. [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)
fixes the configuration layer instead: tasks are YAML files naming data source, split strategy,
preprocessing, target processing, trainer settings and metrics, and no data ships with the package.

### 2.4 What all four leave free

- **Preprocessing effects.** [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)
  states that it has not systematically evaluated them, while itself fixing notch filters at 50 and
  60 Hz plus harmonics, channel-wise robust scaling at the recording level, and clamping at 20. No
  suite ablates its own preprocessing.
- **Per-comparison inference.** None of the four reports a significance test on its leaderboard; see
  §3.3 and §3.4.
- **Pretraining-to-evaluation overlap.** Only
  [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) raises it, and its handling is
  precise about its own weakness: it marks the affected cells with hashed bars so that "the reported
  performance could be overinflated since test subjects or examples may have been seen by the model",
  keeps them in the leaderboard "as we did not notice a clear trend suggesting pretraining 'leakage'
  improves downstream performance on the same data", and neither excludes nor separately analyses
  them. Its own card records that this justification is an impression, not a test.
  [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) does not state whether any
  of its ten checkpoints was pretrained on any of the 54 evaluation datasets.
  [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) asserts "ensuring no data leakage"
  for the subject grouping and does not address corpus overlap at all.
  [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)'s own Table 7 contains
  the evidence of the overlap and its results tables carry no qualification. See §4.3.
- **Withheld test labels.** None. The regime in §1.5 has no modern instance in this strand.

### 2.5 The suite that predates the question, and the object model the others inherited

[moabb](../collection/datasets-benchmarks/moabb/card.md) sits in this node despite covering no
pretrained models — the words "pretrained", "foundation model" and "deep learning" do not appear in
it, and the only "pre-trained" occurrence describes human subjects. Its contribution is the
decomposition the later suites reproduce without citing it as such: an experiment is
dataset × context × pipeline, where context splits into a *paradigm* object (imagery type, trial
length and overlap, band-pass, pre- and post-event windows) and an *evaluation* object (train/test
splitting and the reported metric), "and these must be fixed identically for a given analysis". The
task-card of [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) and the YAML
task specification of [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) are the
same object under other names.

Its empirical result is the deflationary one the framework exists to produce: "different datasets can
result in very different results for identical processing pipelines ... many previously validated
methods do not hold up when applied across different datasets", with Tikhonov-weighted CSP's
published advantage "not validated in this analysis" and filter-bank CSP's significance going "in
both directions depending on the dataset". Its diagnosis of the cause is two-part and both parts
recur later in this strand: over-reliance on a handful of competition datasets — "over a thousand
journal and conference submissions have been written on the BCI Competition III and IV datasets ...
with less than 50 subjects total" — and code scarcity, which forces each lab to "compare either
against other work from the same lab, or old, easily implementable standards".

MOABB is also load-bearing infrastructure rather than only a precedent, and the resulting loop is
worth stating: [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) reaches its
motor-imagery and P300 comparison datasets *through* MOABB, and
[eeg-models/reve-2025](../collection/eeg-models/reve-2025/card.md) draws 384 pretraining hours *from*
MOABB. So a dataset reached through MOABB can be pretraining data for a checkpoint that a
MOABB-derived NeuralBench task then evaluates.

### 2.6 The suite-to-suite coverage graph, and what it is not evidence of

Checkpoints covered by more than one suite, from the four cards' own overlap statements: BIOT,
LaBraM and CBraMod by all four; BENDR and REVE by
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md),
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) and
[neuralbench](../collection/datasets-benchmarks/neuralbench/card.md); EEGPT by
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) and
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md); BrainOmni, NeuroGPT and NeuroLM by
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) and
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md). Checkpoints covered by exactly one:
FEMBA and EEGMamba (OmniEEG-Bench); LUNA (NeuralBench); SppEEGNet, MBrain, Brant, BFM and BrainBERT
(Brain4FMs).

Four suites reporting on LaBraM is not four times the evidence about LaBraM. But it is not one
measurement either, and the reason is the subject of this whole node: the four suites differ on the
holdout boundary, the adaptation regime, the metric and the comparator set, so four LaBraM numbers
are four different quantities rather than four estimates of one. The graph is structure, and it is
labelled non-evidential.

The genuinely single-sourced part of the corpus is not the results but the *descriptions* of the
checkpoints — see §5.2.

---

## 3. The measurement's own uncertainty: the null, the interval, and whether anyone tests

The pilot's §3 asks who measured a checkpoint and under what protocol. This node asks the prior
question about any number so produced: what is it being compared against, and how wide is it. Three
entries answer, and they are the strand's answer to "can the measurement be trusted" at a level
below the split.

### 3.1 The null is not the theoretical chance level

- [combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
  — classifying pure Gaussian noise at small n yields "decoding accuracies of up to 70% or higher in
  two-class decoding", so 50 percent for two classes and 25 for four are not the thresholds a
  decoding result should be judged against. The theoretical levels "hold for an infinite number of
  data samples but not for small data sets", a limitation the paper describes as "widely recognized
  in the machine learning field" but "sometimes still overlooked or ignored in the emerging field of
  brain signal classification". The severity is quantified as a function of sample size, class
  number, cross-validation parameters (k-fold, leave-one-out, and repetition number) and classifier
  type (LDA, naive Bayes, SVM), and two remedies are offered: an analytical binomial p-value and an
  empirical permutation p-value, both computed with the actual sample size. Validation is on
  MEG and intracranial baseline recordings where the true answer is known to be chance.

Two limits on this entry are load-bearing and are recorded on the card. The first is scope: the
paper predates the deep-learning EEG literature and studies LDA, naive Bayes and SVMs, so whether the
same empirical chance levels hold for a fine-tuned transformer is not addressed. The second is
access: the card is abstract-only and the tabulated empirical chance levels — the part a user would
actually apply — are **reported but not accessible** (§7). The finding that the number of
cross-validation repetitions moves the empirical chance level is on record; the values are not.

### 3.2 The interval is wider than the statistic that would naturally be reported

- [varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
  — at neuroimaging sample sizes, "sample sizes of many neuroimaging studies inherently lead to large
  error bars, eg ±10% for 100 samples", and "the standard error across folds strongly underestimates
  them". The literature sample it is calibrated against is 642 studies with a median of 89 samples.

  **The headline table is now marked unverified on the card, and the hedge has to travel with the
  numbers.** An earlier version of this bullet gave Table 1 as ±15 / ±10 / ±6 / ±3 percentage points
  at n = 30 / 100 / 300 / 1000. The table's body is not in the extraction — only its caption
  survives, itself truncated at a page break — so of those four rows only n = 100 is stated anywhere
  in the source, twice: "eg ±10% for 100 samples" in the abstract and "A typical sample size in
  neuroimaging, 100 observations, leads to ±10% errors in prediction accuracy" in the conclusion.
  The other three rows are unverified rather than wrong; the nearest supported values are the paper's
  own Figure 1 readings, −20%/+18% at n = 30 under leave-one-out simulation and −15%/+12% under the
  binomial, −6%/+6% at n = 300 and −3%/+3% at n = 1000. The caption's caveat, that actual bounds
  "may be significantly larger in adverse situations such as with correlated observations or very
  unstable classi-", survives intact up to that break.

The card records three specifics that matter more than the table. **The bias is worst for the scheme
with the best true error bars**: for 50 repeated random splits with 20 percent held out, the
standard-error-implied interval at n = 100 is ±2.0 percent against an empirical ±8.1 percent, an
understatement factor of 0.26, while leave-one-out understates by 0.73 — because "repeated random
splits create more correlations across fold". **Vibration effects** are the mechanism by which trying
several reasonable pipelines produces a number that will not replicate: on Haxby et al.'s data with
labels inverted so that chance is the true answer, roughly 50 pipelines score 44–52 percent using all
12 sessions, "going up to 57% for 6 sessions and 71% for 4 sessions", and such gains "are meaningless
as they will not carry over to predicting on new data". And **the binomial is a floor, not a
description**: with 100 tosses the binomial bounds lie ±7 percent from the true accuracy, which "is a
best-case scenario for errors on the accuracy measure: observations are i.i.d. and there is no
additional variability from training a decoder", whereas real data "is strife with correlation across
samples and confounding effects".

The card also records the paper's own limits, and one of them intersects §1 directly: the x-axis
deliberately mixes units — samples means "less than 100 observations given to the classifier, trials
or sub-jects depending on the settings" — so for EEG, where one participant contributes thousands of
epochs, which n the table refers to is exactly the question
[kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
and [eeg-models/brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
show is decisive, and this paper does not settle it. Its real-data results are balanced binary
classification in within-subject fMRI, across-subject fMRI and MEG; no EEG, and continuous outcomes
are not analysed at all. Two narrowings from the audit: voxel-based morphometry appears only in the
paper's description of an earlier study and contributes no number here, and unbalanced multiclass
*is* handled quantitatively — Appendix A.2's Table A1 gives binomial bounds for expected accuracies
of 10, 25, 50, 75 and 90 percent at n = 30, 100 and 300, so a four-class EEG task has a stated
reference point in this source after all.

### 3.3 The two are complementary halves, and the corpus contains exactly one procedure that meets both

[combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
quantifies how far the *null* moves from its theoretical value;
[varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
quantifies the width of the interval around the *estimate*. Each card names the other as the
complement, and the Combrisson card draws the joint consequence: a study that fixes only one of the
two still cannot say whether a number is real.

The only entry in this strand implementing inference of the kind either recommends is
[moabb](../collection/datasets-benchmarks/moabb/card.md), and its procedure is worth recording in
full because nothing else in the corpus approaches it: per pipeline pair, within each dataset, a
one-tailed permutation-based paired t-test for datasets with fewer than 20 subjects and a Wilcoxon
signed-rank test otherwise; p-values combined across datasets by Stouffer's method weighted by the
square root of the subject count; Bonferroni correction across the N_pipelines − 1 comparisons; a
standardized mean difference within datasets as the meta-effect size, combined with the same
weighting; and 95 percent intervals per dataset in forest plots. Sample meta-effect p-values against
CSP + LDA run from 3.58e-21 (channel log-variance + optSVM) to 3.02e-02 (TRCSP). The design decision
underneath it is a refusal to pool: subjects are not pooled across datasets because "differences in
trial amount, sampling rate, and even location and hardware mean that we cannot expect subjects
across datasets to be naively comparable".

MOABB's own reflexive conclusions belong here too: "what this analysis shows most clearly is that
the sample size problem in BCIs is bigger than we might have expected", and "for studies with very
few subjects ... the confidence intervals make even very strong standardized effects quite
untrustworthy". Its own card records the corresponding gap: whether the hyperparameter search is
nested inside the reported 5-fold cross-validation is not stated, and if it is not, the reported
ROC-AUCs are optimistically biased by selection on the test folds — the failure Varoquaux describes
as vibration effects.

### 3.4 What each entry reports instead

- [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) — no confidence
  intervals or significance tests on the main leaderboard tables; the few-shot results are averaged
  over three runs and the rest appear to be single runs. Its own card notes that with EEGMAT at 1,080
  samples and BCI-IV-2A at 5,184, the differences between adjacent models are not obviously larger
  than run-to-run variance, and the paper does not let a reader check.
- [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) — mean and standard
  deviation over three runs (five for few-shot and channel masking), each run using "a pre-generated,
  fixed data split derived from a different random seed", and model orderings drawn from average
  ranks with no per-comparison significance test. There is one exception, and it is a sharp one: the
  factor analysis *does* use a Wilcoxon signed-rank test on per-dataset Spearman correlations, so the
  scaling claim (publication year ρ = −0.40, pretraining-dataset count ρ = −0.27 at p = 1.1×10⁻⁷, log
  parameter count −0.21, training hours −0.08, subject count −0.10) is tested where the leaderboard
  claims are not.
- [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) — standard deviations across
  cross-validation folds, which is the only variance estimate in the four that is over folds of a
  resampling scheme rather than over seeds.
- [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) — three seeds varying only
  weight initialization, so as its own card states the reported standard errors do not capture
  split-to-split variance at all.
- [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  — 95 percent confidence intervals on every value and comparison by interval dominance, with no
  p-values, t-tests, permutation tests or Wilcoxon tests anywhere, though Table 3's caption
  nonetheless says the proper method "always reveals a significantly greater error rate".

That last entry produces the node's sharpest relation, and it is *not* a contradiction of any of the
three kinds in §8, so it is recorded here. The entry that reports uncertainty most conscientiously is
the one whose intervals another entry's analysis implies cannot be right: an error rate of 0.09 given
as (0.083, 0.097) implies pooling over observations rather than over participants or folds, and under
participant-disjoint evaluation the sampling unit is the participant, with n between 10 and 122. The
Kamrud card makes the judgment about itself, and the Varoquaux card names Kamrud as the entry
reporting intervals its analysis suggests cannot be right. Both cards agree; neither is contradicting
the other.

### 3.5 The margins in this corpus, placed against the bounds

Recorded as a property of the entries jointly, not as a verdict on any of them. The margins between
the best pretrained and the best supervised model in the one suite that publishes a full per-dataset
table ([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md), cross-subject
balanced accuracy):

| dataset | best pretrained | best supervised | margin | scale as tabulated |
|---|---|---|---|---|
| [tuab](../collection/datasets-benchmarks/tuab/card.md) | LaBraM 81.50 | ST-Tran 81.04 | +0.46 | 2,383 subjects, 409,083 samples |
| [tuev](../collection/datasets-benchmarks/tuev/card.md) | LaBraM 59.05 | Conformer 54.06 | +4.99 | 370 subjects, 112,237 samples |
| [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) | LaBraM 54.98 | EEGNet 47.83 | +7.15 | 9 subjects, 5,184 samples |
| EEGMAT | CBraMod 88.89 | 73.89 | +15.00 | 36 subjects, 1,080 samples |
| [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) | CBraMod 69.47 | ST-Tran 69.55 | **−0.08** | 78 subjects, 414,961 samples |

The Sleep-EDF row is the only one of the five above where a supervised model takes the top spot on
balanced accuracy — but not, as an earlier version of this line said on the card's authority, the
only such row in AdaBrain-Bench's Table 2. The card was corrected: there are three, all in the
suite's clinical-monitoring group, the other two being Siena (Conformer 72.87 over BIOT 71.67) and
HMC (Conformer 73.84 over LaBraM 71.94), with SHHS the group's fourth member going to CBraMod at
73.51 against ST-Tran's 68.67. The five rows tabulated here are the datasets this strand cards, not
the suite's full table, and the supervised-wins pattern is concentrated in a task family this table
under-samples. The TUAB row is what
[tuab](../collection/datasets-benchmarks/tuab/card.md) calls a saturated benchmark, consistent with
[neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) listing pathology among the
tasks near saturation. And
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) reports no interval for
any cell in that table. Whether the +0.46 row and the +15.00 row can be separated as evidence is a
question about what the corpus as a whole supports, which §3.1 of this document declines to answer
and which belongs to Phase 4; recorded here only as the property of that one table.

---

## 4. The corpus layer: what the checkpoints were made from, and on what terms

### 4.1 Recording context, and what each corpus contributes

- [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) — the clinical archive.
  16,986 sessions from 10,874 patients, 51 percent female, ages under 1 to over 90; 87 percent
  sampled at 250 Hz with 256, 400 and 512 Hz making up the rest; 24 to 36 channels with 31 the most
  common EEG-only count; converted from Nicolet NicVue to EDF and de-identified to the 18 HIPAA
  identifiers. **No task**: this is archival routine and long-term monitoring EEG ordered for
  diagnosis, and its labels are the neurologist's free-text report per session plus an optional
  per-channel six-class event annotation (SPSW, PLED, GPED, ARTF, EYEM, BCKG). The authors are
  explicit about what distinguishes it: "'clinical-grade' data is inherently more variable with
  respect to parameters such as electrode location, clinical environment, equipment, and noise". It
  is single-site and single-country, and 75 percent of the parent archive's records are classified
  abnormal in the reports. **No montage information at all** appears in the paper — the word does not
  occur — so the derivation scheme each pretraining paper used is that paper's choice.
- [openneuro](../collection/datasets-benchmarks/openneuro/card.md) — the heterogeneity source. 604
  datasets and 20,989 participants as of 9 October 2021, of which 81 are scalp-EEG and 8 intracranial.
  Median dataset size 23 subjects, 31 studies over 100 subjects, maximum 928 — these three width
  figures come from the paper's Figure 3 analysis and so are computed over the 502 DataLad-accessible
  datasets, not the 604, which the card records and this document previously did not. Every upload
  passes BIDS validation at submission; snapshots are git tags with DOIs. What it supplies that TUH does not
  is task-based cognitive experiments from individual laboratories.
- [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) — a laboratory task corpus
  that doubles as a benchmark. 109 participants, 64 channels on the 10-10 system at 160 Hz, EDF+ with
  annotation channels, 14 runs per participant.
- [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) — 197
  whole-night polysomnograms with expert hypnograms, two EEG derivations at 100 Hz plus peripheral
  channels, from two studies with different populations (153 healthy home recordings aged 25–101; 44
  hospital nights from 22 people in a temazepam-versus-placebo crossover).

**Concentration.** TUH data is the substrate under CBraMod, BIOT, LaBraM and REVE, with
[eeg-models/reve-2025](../collection/eeg-models/reve-2025/card.md) accounting 26,847 of its 61,415
hours to Temple University Hospital, 22,707 to PhysioNet, 10,194 to OpenNeuro and 384 to MOABB. The
model-side version of this observation, including which checkpoints evaluate back inside their own
pretraining distribution, is pilot §2.4; this node records the corpus-side facts it rests on.

**The two corpora contribute along different axes of the only scaling analysis in the strand**, and
this relation is stated by no single card. [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)
finds the *number of pretraining datasets* significantly associated with better average rank (median
Spearman ρ = −0.27, Wilcoxon p = 1.1×10⁻⁷) while training hours (−0.08) and number of training
subjects (−0.10) show weaker associations. [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md)
is the field's source of hours; [openneuro](../collection/datasets-benchmarks/openneuro/card.md) is
its source of dataset count, with "more than 60 EEG datasets ... deposited since the publication of
the BIDS-EEG standard in 2019". The OpenNeuro card makes the first half of this observation; the
pairing is recorded here.

### 4.2 Access terms split three ways, and the split decides what is possible

- **No data licence, signed form, ssh and rsync.**
  [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md),
  [tuab](../collection/datasets-benchmarks/tuab/card.md) and
  [tuev](../collection/datasets-benchmarks/tuev/card.md). The article is CC BY; the data has no
  licence in either the paper or the downloads page. Access is a form emailed to help@nedcdata.org
  from an institutional address, approval in 24 to 48 hours, then ssh keys and rsync as of January
  2026, with `-L` required because all subsets are symlinked back to the parent. An 8 TB USB drive
  mailed to the maintainers is offered where connectivity is a problem. The card states the
  consequence precisely: "registration and a signed form are not a licence grant", and neither
  document states redistribution or derivative terms.
- **Open with an explicit licence.**
  [openneuro](../collection/datasets-benchmarks/openneuro/card.md) at CC0 by default with no
  authentication — "while not legally required, researchers using the data are expected to abide by
  community norms and cite the data" — bounded by the exclusion of GDPR-covered data, which "cannot
  be shared through OpenNeuro at present due to the requirement for restrictive data use agreements".
  [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) and
  [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) at Open Data
  Commons Attribution v1.0, no registration, `wget` or `aws s3 sync --no-sign-request`.
- **Free with a citation condition and no formal licence.**
  [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md): freely
  accessible "with the only restriction that the present article is referenced upon any publication
  of results".

Two cross-cutting properties. The article licence and the data licence come apart in three of the
four dataset entries — the TUH paper is CC BY over unlicensed data, the BCI-IV review is CC BY over an
informally released dataset — which is why the collection brief asks for them to be recorded
separately. And [openneuro](../collection/datasets-benchmarks/openneuro/card.md)'s card notes that CC0
is a waiver called a dedication, a licence and an agreement in three places in the same paper, and
that CC0 is the default rather than a guarantee, with the paper not stating what fraction of datasets
depart from it. The sibling reading of the same access ladder, ordered by friction for a project
choosing data to fine-tune on, is in
[candidate-datasets/openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) and its
strand index; this node records access terms only as they bear on whether an evaluation can be
audited or a pretraining corpus rebuilt.

### 4.3 The evaluation sets are inside the pretraining corpora

Recorded per checkpoint, with the reporting source, because this is the property that most directly
conditions how a benchmark number reads.

| checkpoint | pretrained on, among others | then evaluated on | source of the mapping |
|---|---|---|---|
| BIOT | TUAB, TUEV (of six corpora: PREST, SHHS, CHB-MIT, IIIC Seizure, TUAB, TUEV) | TUAB, TUEV | [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) Table 7 |
| CBraMod | TUAB, TUAR, TUEP, TUEV, TUSE, TUSL | TUAB, TUEV | [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) Table 7 |
| EEGPT | PhysioNet-MI, HGD, TSU, SEED, M3CV | motor-imagery benchmarks (not PhysioNet-MI itself in that table) | [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) Table 7 |
| LaBraM | BCI-IV-1 (not 2a), Emobrain, SPIS, Grasp and Lift, Inria P300, SEED series, Siena, TUEP, TUSZ | TUAB, TUEV, BCI-IV-2a | [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) Table 7 |
| REVE | TUH 26,847 h, PhysioNet 22,707 h, OpenNeuro 10,194 h, MOABB 384 h | TUEV, PhysioNet-MI | [eeg-models/reve-2025](../collection/eeg-models/reve-2025/card.md) |

[tuab](../collection/datasets-benchmarks/tuab/card.md) states the consequence that a split cannot
fix: even a patient-disjoint fine-tuning split does not remove the overlap, because the
self-supervised pretraining saw the evaluation subjects' recordings. And the four suites' handling of
it is the §2.4 list: only [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) flags
it, on the leaderboard, with a justification its own card calls weak.
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) publishes both the Table 7
that documents the overlap and the results tables that ignore it. The model-strand generalization —
that in four of ten reviewed studies the downstream evaluation datasets were already used for
pretraining — is at
[eeg-models/kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)
and pilot §2.4.

### 4.4 The peripheral channels every suite discards

[sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) carries horizontal
EOG, submental chin EMG and, in the sleep-cassette subset, oro-nasal respiration and rectal body
temperature, alongside its two EEG derivations. Every one of those channels is discarded by every
checkpoint and suite in this corpus:
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) tabulates Sleep-EDF as 2
channels at 100 Hz in 30-second windows, meaning the two EEG derivations only.
[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) is still
the stronger case, but it is weaker than this document previously made it, and the difference is
structural rather than numeric.

**What changed.** This section asserted that for BCI-IV-2a "the exclusion is a protocol requirement
rather than a modelling choice", quoting the three EOG channels as "provided for the subsequent
application of artifact processing methods and must not be used for classification". The card was
corrected and that quotation cannot be sourced to data set 2a. Two things went wrong at once. The
card's `source.md` had held the official Brunner dataset description appended behind a delimiter,
and a re-extraction run over the PDF alone dropped it, so nothing on the card is now sourced to that
document (§7). And the surviving review says "must not be used for" only in its section 6.2.2, which
describes data set **2b**; its section 5.2.1, on 2a, ends the corresponding sentence at "The EOG
channels are provided for the subsequent application of artifact processing methods (Fatourechi et
al.,2007)". So the prohibition on classifying from EOG belongs to a different dataset in the same
review.

**What survives.** The review's section 5.4 does impose a requirement, on the competition's
submitted software rather than on the data: "Since three EOG channels were provided, the software
was required to remove EOG artifacts before the subsequent data processing using artifact removal
techniques such as high pass filtering or linear regression". That is enough to keep the downstream
observation, on a narrower footing: benchmark preparations that feed all 25 channels or skip
artifact removal are not running the protocol the competition specified, and the card records that
no suite carded here states what it did. What no longer holds is the sharper claim that using an EOG
channel as a *feature* on this dataset violates a stated prohibition. Re-appending the official
description would settle it; until then the prohibition should be attributed to BCI-IV-2b.

The concern behind that requirement is not pedantic, and the corpus contains the demonstration in a
sibling strand:
[multimodal-biosignals/mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
reports a control analysis in which the memorised item was decodable from two numbers — horizontal
and vertical gaze position — with ICA-based artifact removal having been insufficient to prevent it.

**Boundary note.** Whether these peripheral channels are usable as signal is the
`candidate-datasets` question, and that strand's card of the same dataset,
[candidate-datasets/sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md), answers it
there by recording the EOG and EMG as diagnostic signals rather than artefact references. What is
recorded here is the measurement-practice fact: the channels are present, standardized, and
universally unused by the suites that report on the dataset.

---

## 5. The checkpoint-to-benchmark mapping, and the two tables it comes from

The mapping is this strand's category-2 deliverable. It is what lets a reader tell an established
result from a novel one.

### 5.1 The mapping, per carded dataset

- [tuab](../collection/datasets-benchmarks/tuab/card.md) — *pretrained on it*: BIOT, CBraMod.
  *Evaluated on it*: BIOT 78.07, EEGPT 80.54, LaBraM 81.50, CBraMod 80.05 balanced accuracy in
  AdaBrain-Bench's cross-subject setting, against supervised EEGNet 77.58, LDMA 78.37, ST-Tran 81.04,
  Conformer 78.92; AUC-PR 86.93, 89.36, 90.08, 89.19 against 86.48, 86.97, 90.41, 87.95. Also in
  OmniEEG-Bench's epilepsy-and-abnormality subtype and NeuralBench's pathology task.
- [tuev](../collection/datasets-benchmarks/tuev/card.md) — *pretrained on it*: BIOT, CBraMod.
  *Evaluated on it*: BIOT 51.78, EEGPT 42.89, LaBraM 59.05, CBraMod 57.69 balanced accuracy with
  weighted F1 75.17, 74.65, 79.62, 78.69, against supervised EEGNet 32.65, LDMA 32.88, ST-Tran 38.68,
  Conformer 54.06; and REVE at 0.696 by souping ten fine-tuning runs. Also in OmniEEG-Bench's
  epilepsy-and-abnormality subtype, and a benchmark in the LaBraM and BIOT papers themselves, which
  is where the splits REVE reuses come from.
- [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) — *pretrained on it*: EEGPT;
  REVE draws 22,707 hours from PhysioNet overall without breaking out this dataset. *Evaluated on
  it*: REVE 0.6480 fine-tuned four-class balanced accuracy against 0.5409 from scratch and 0.5371
  frozen; CBraMod 0.6417 with pretraining, 0.6196 without, 0.3845 frozen; LaBraM 0.3715 frozen; BIOT
  0.3698 frozen, all per [eeg-models/reve-2025](../collection/eeg-models/reve-2025/card.md). The
  largest of MOABB's twelve datasets at 109 subjects, two-class only there; a few-shot task family in
  OmniEEG-Bench; and present in Brain4FMs as EEGMMIDB.
- [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) — *no
  checkpoint in this corpus reports pretraining on 2a*; LaBraM lists BCI-IV-1. *Evaluated on it*:
  BIOT 42.53, EEGPT 25.81 (47.89 under linear probing), LaBraM 54.98, CBraMod 47.71 cross-subject,
  against EEGNet 47.83, LDMA 36.20, ST-Tran 31.42, Conformer 44.88; under the multi-subject setting
  the same four reach 50.67, 54.01, 60.75, 59.03. In Brain4FMs's communication and affective
  computing family, and in MOABB as BNCI2014-001, restricted to two classes.
- [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) — *pretraining*:
  named as a source for BIOT indirectly via SHHS rather than Sleep-EDF itself. *Evaluated on it*:
  BIOT 64.95, EEGPT 60.99, LaBraM 68.94, CBraMod 69.47, against ST-Tran at 69.55. Sleep staging is a
  task family in OmniEEG-Bench, Brain4FMs and NeuralBench.
- [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) — pretraining substrate
  only; not itself an evaluation set. Its two derived subsets are, between them, reported on by BIOT,
  EEGPT, LaBraM, CBraMod, REVE, BENDR, BrainOmni, FEMBA, Neuro-GPT, NeuroLM, EEGMamba and LUNA across
  the four suites.
- [openneuro](../collection/datasets-benchmarks/openneuro/card.md) — pretraining source (REVE, 10,194
  h) and a NeuralBench data source; not a benchmark, because it is a registry rather than a dataset.

The mapping's reach is wider than the five datasets above, and the rest of it is recorded on the
suite cards rather than on dataset cards. The further evaluation sets named there are SEED, SEED-IV,
SEED-VIG, EEGMAT, SHU, Things-EEG, Siena, HMC and SHHS
([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)); CHB-MIT, MAYO, FNUSA,
Dep-BDI, MDD-64, SD-28, UCSD, ADFD, ADHDAdult, ADHDChild, ISRUC, SleepEDFx, DEAP, SEED-IV, EEGMat,
EEGMMIDB, BCI-2a and Chisco
([brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)); PD31, DEAP-arousal,
Broderick-Cocktail-party, Broderick-reverse, ThingsEEG2 and Monitoring-Errp
([omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)).

The Brain4FMs list is longer than it was, and the lengthening matters for §2.6 rather than only for
bookkeeping. An earlier version named nine datasets, which was all the card then carried; the card
was corrected to record all eighteen from the suite's Table 2. Five of the nine added — SleepEDFx,
EEGMat, EEGMMIDB, BCI-2a and SEED-IV — are datasets this strand already tracks through
AdaBrain-Bench or MOABB, so the overlap between suites is wider than the coverage graph in §2.6
suggests, and §2.6's warning that a shared dataset name across two suites does not make two
comparable numbers applies to more rows than it appeared to. Two carded parameters also changed
with it: BCI-2a is 9 subjects and 4 classes in that table, not "4 subject groups", and Chisco is
5 subjects and 39 categories, not 39 subjects.

### 5.2 The mapping and the dataset parameters both come from two tables

This is the strand's clearest instance of the rule that repetition is not evidence but the
comparator graph is structure.

Nearly every checkpoint-to-corpus fact in §4.3 and §5.1 traces to
**[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) Table 7** — which
tabulates BIOT at 3.2M parameters, 59,304 h and 18 fixed channels; EEGPT at 25M, 198 h and 58
channels; LaBraM at 5.8M, 2,535 h and 136 channels; CBraMod at 4.0M, 9,246 h and a flexible channel
count, each with its named pretraining corpora — or to
**[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) Table 1**, which does the same for
fifteen models with parameter count, pretraining modality and feature domain. The strand INDEX says
as much: Table 7 "is the single most complete public statement of what BIOT, EEGPT, LaBraM and
CBraMod were pretrained on".

The same is largely true of the *dataset* parameters. TUAB's 2,383 subjects and 409,083 samples,
TUEV's 370 subjects and 112,237 samples, Sleep-EDF's 78 subjects and 414,961 windows, and
BCI-IV-2a's 5,184 samples are all AdaBrain-Bench preparation figures, and each card says so
explicitly rather than presenting them as the corpora's own —
[tuev](../collection/datasets-benchmarks/tuev/card.md) calls 370 "a benchmark figure rather than the
corpus's own",
[sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) records that 78
"comes from benchmark preparations rather than from the dataset itself", and
[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) records that
5,184 "is arithmetic (9 × 2 × 288), not a figure stated by either source".

**TUAB is now the exception, and the exception matters more than the rule it breaks.** An earlier
version of this section said [tuab](../collection/datasets-benchmarks/tuab/card.md) "calls 2,383 a
benchmark artefact" because the primary documentation had no subject count of its own. The card was
corrected: the thesis's file-statistics tables carry a `Patients` column beside the `Files` column,
giving 2,138 training plus 253 evaluation patients — 2,391 for the release the thesis describes —
and an `Hours` column giving 1,064.7 plus 104.4. So TUAB does have a primary subject count and a
primary hours total, and AdaBrain-Bench's 2,383 is a near-miss against it rather than the only
figure in existence. Whether the eight-patient gap is a release difference, an exclusion or a
counting convention is not determinable from either source.

Two consequences follow, and both are properties of the corpus rather than of the field.

First, **a reader who sees the same figure on several cards is usually reading one source several
times**. Those cards are not independent corroborations of AdaBrain-Bench's numbers; they are cards
that could not obtain the figure from the primary documentation and said so. The TUAB correction is
the counter-case and narrows the claim: for one of the five, the figure *was* obtainable from the
primary and the card had missed it, which is a defect in our reading rather than a property of the
documentation.

Second, **that single source is internally inconsistent about the very fields the mapping uses**.
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) records five internal
inconsistencies in its own source, three of them in Table 7 against the body: EEGPT at 198 h versus
"246 hours", CBraMod at 9,246 h versus "approximately 27,000 hours", and LaBraM at 2,535 h and 136
channels versus "about 2,500 hours ... supporting 137 EEG channels". So the hours and channel figures
that the mapping propagates are exactly the figures the source disagrees with itself about. §8.1 and
§8.2 record the resulting disagreements.

One of the three is now adjudicable, which was not true when this section was written. The LaBraM
card gained the exact pretraining total from the primary's Appendix D — 2534.78 hours — so
AdaBrain-Bench's 2,535 and its body's "about 2,500" are two roundings of one correct figure rather
than two competing claims ([eeg-models/labram-2024](../collection/eeg-models/labram-2024/card.md),
pilot §2.3). What remains a genuine conflict on that row is the channel count, 136 against 137,
which the primary states neither way. EEGPT's 198-versus-246 is untouched, because that primary
reports no hours figure at all.

A third observation, of a related but weaker shape, sits on the parameter side. An earlier version
of this section held that the counts behind
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)'s log-parameter correlation
(ρ = −0.21 with per-dataset rank) were unrecoverable. **That was wrong, and review caught it**: the
retrieved source carries Supplementary Table 2, "Summary of 10 EEG foundation models included in the
benchmark", with a `#Params` column for all ten, so the correlation is checkable and its inputs are
on the record. What remains true, and is the weaker claim, is that those counts sit alongside
independent tabulations elsewhere in this corpus that disagree with each other by up to three orders
of magnitude for BENDR (§8.1). The suite is internally consistent; the corpus around it is not.

---

## 6. The substrate: what the formats and the reference reader make recordable

The three category-5 entries are not infrastructure notes. They determine whether the metadata a
sound protocol needs — subject identity, session identity, electrode position, an explicit event
table — is present in a file at all.

### 6.1 Where a stimulus marker lives, and what shape it has

- [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) — events are not a trigger line but
  a reserved *signal*: "text, time-keeping, events and stimuli are coded as text annotations in this
  'EDF Annotations' signal", stored as Time-stamped Annotations Lists with an onset in seconds
  relative to the file start, an optional duration, and one or more UTF-8 strings, delimited by the
  unprintable bytes 20 and 21. An EDF+ file must contain at least one such signal even with no
  annotations, because the first annotation of each data record carries that record's start time. So
  reading labels from EDF+ is a parsing problem, not a thresholding problem. The format also imposes
  a constraint on label design: "in order to support automatic averaging and superimposition,
  identical events or stimuli that occur several times in one file must be coded each time by the
  same, unique annotation", and different events "must differ from this unique annotation".
- [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) — `events.tsv` is required, and the
  rationale is the state of the raw layer: "while such information is often present as one or several
  binary 'trigger' channels in the EEG recordings, the representation of events is rarely explicit in
  the original data". The file "should be present, encoding all of the parameters of the experimental
  design (onset of events, trial type, duration, responses, etc.)", with a `stim_file` column able to
  reference the presented stimulus in the dataset's `stimuli/` directory, and Hierarchical Event
  Descriptors integrated for precise annotation.
- [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) is the worked instance and
  the worked trap: three codes T0, T1, T2 in EDF+ annotation channels, where T1 means left fist in
  one run type and both fists in another, so "a pipeline that reads annotations without also reading
  the run index will silently mislabel half the data".

The relation across the two standards: BIDS requires an explicit event table precisely because the
raw layer stores events either in a trigger channel or as free text in an annotation signal, which is
the mechanism EDF+ specifies.

### 6.2 What the raw layer cannot express, and what that costs a coordinate-based model

[edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) stores channel *labels*, standardized
as texts, and **has no mechanism at all for electrode coordinates** — with a bound the card added
during the audit and which belongs here: the word "coordinate" does not occur in the specification
page, but the page's linked companion, the standard-texts list at `edftexts.html`, is not in the
carded source, so the absence is established for the specification proper and not for the document
it defers to. Re-derivation is described as label manipulation, "because electrode locations are
specified using standard texts, re-montaging (i.e. re-referencing) EEG derivations can be done
automatically". The card also records that the
specification conflates "montage", "derivation" and "re-referencing" in a single sentence — which
matters here because the format stores labels only and cannot express a position.

[eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) supplies what the format lacks, and
supplies with it the definition the field uses loosely: "(i) An EEG electrode is a contact point
attached to the skin, (ii) a channel is the combination of the analog differential amplifier and
analog-to-digital converter that result in a potential (voltage) difference being stored in the EEG
dataset". `channels.tsv` describes the stored signals; `electrodes.tsv` plus `coordsystem.json`
describe positions in a named coordinate frame. The requirement level of the second pair is stated
two ways in the same paper — a conditional "should be specified if the positions of the electrodes
are known" against an unconditional "may in addition specify" — and the difference decides whether a
coordinate-based checkpoint can rely on positions being present in a conformant dataset. (The
sibling card of the same paper resolves the ambiguity rather than recording it; see §8.1.)

The consequences appear in the dataset entries, not in the standards. TUEV is preprocessed by the
field's convention into 16 bipolar derivations from BIOT's release scripts, and a coordinate-based
model must approximate: [eeg-models/reve-2025](../collection/eeg-models/reve-2025/card.md) uses "the
average position of each bipolar montage", a single midpoint, which
[tuev](../collection/datasets-benchmarks/tuev/card.md) records as invisible in any leaderboard,
unablated, and applied by a model reporting TUEV numbers competitive with models that have no such
constraint. [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)'s
Fpz-Cz and Pz-Oz are bipolar too, and the card records that the same approximation applies and is
mentioned by no suite that reports Sleep-EDF numbers. And
[tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) states no montage at all,
so the derivation scheme underneath most of the field's pretraining is whatever each pretraining
paper's preprocessing chose. The model-side treatment of bipolar derivations, mechanism by mechanism,
is pilot §1.7.

### 6.3 What the substrate says about splits: nothing, and the gap is named

- [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) predates any machine-learning use of
  these files and says nothing about evaluation, splits or leakage. Its one adjacent provision is the
  derived-file naming convention — an analysis of `R.edf` is stored as `RA.edf`, copying the
  80-character patient identification line and keeping start date and time consistent — which makes
  recording-level linkage recoverable, though the specification does not frame it that way. Working
  against that, the card records that "one session in one file" is promised twice and prohibited
  once: different techniques or different amplifier settings "must be stored in separate files", and
  the worked example duly splits one session across several. **A session is therefore not reliably
  one file**, which bears directly on the session-wise boundary of §1.2.
- [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) says nothing about splits either.
  Subject identity is recoverable from the directory structure, which is the necessary condition, but
  nothing in the standard obliges a pre-partitioned release to document its grouping. That is exactly
  the reporting requirement
  [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  proposes to the IEEE Standards Association Neurotechnologies for Brain–Machine Interfacing group:
  de-identified participant labels must ship with any released EEG so a downstream user *can*
  partition properly, and where a repository pre-partitions data, "proper dataset partitioning
  guidelines should be followed". No standard carded in this strand carries that obligation. The card
  also records that the BIDS paper defines no `run-` entity and uses "session" for a directory level,
  a study-design unit and a span of time.

### 6.4 The reference reader, and the example both reference implementations ship

[mne-python](../collection/datasets-benchmarks/mne-python/card.md) reads BTI/4D, KIT, EDF, Biosemi
BDF and BrainVision, plus Neuromag FIF natively, and reaches BIDS datasets through MNE-BIDS. It does
**not** read the General Data Format, which is what
[bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) is
distributed in, so that benchmark needs BioSig or a conversion step. Its access-on-demand design is
the documented mechanism for bounded memory — "this access-on-demand principle can also be inherited
by other classes that build upon Raw (such as Epochs and Evoked, below), which offers the possibility
to process data with a very limited memory usage" — with two limits the card records, the second
added during the audit. It is asserted rather than measured: no benchmark, no memory profile, no
guidance on when preloading is required. And the sentence usually quoted as the mechanism's warrant,
"It offers for example the ability to read data from disk only when needed", has the FIF format as
its subject, not the `Raw` class; the paper does not extend the claim to the EDF, BDF and BrainVision
readers listed above. That is the case an EDF+ pipeline actually hits, so the bounded-memory
guarantee is documented for a format this strand's datasets are mostly not distributed in.

MNE-Python is also infrastructure for two other entries:
[moabb](../collection/datasets-benchmarks/moabb/card.md) is built on it for preprocessing and channel
selection, and [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) uses its sample
dataset as a smoke-test task.

One relation between two entries that neither states about the other: **both reference
implementations in this strand ship a worked example whose split is a random partition over epochs
from a single recording with no grouping key** — MNE-Python's decoding demonstration uses
`ShuffleSplit(len(X), 10, test_size=0.2)` over epochs pooled from two conditions in one subject, and
NeuralBench's worked YAML uses `SklearnSplit` with `valid_split_ratio: 0.2`, `test_split_ratio: 0.2`,
`stratify_by: description` and no grouping key on a sub-300-example single-subject dataset. Each card
independently notes that this is the configuration a new user is most likely to copy, and each links
it to the split-inflation result of §1.1. Different authors and different decades, so these are two
instances of one hazard rather than one claim repeated.

---

## 7. Reported-but-unread versus never-reported

Collection practice distinguishes "the source does not report it" from "the source reports it and we
could not read it". The strand has enough of both that a footnote would mix them, and the two have
opposite implications for whether re-retrieval is worthwhile.

**Reported but not accessible.** Re-retrieval would resolve these.

- [combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
  — abstract-only; Elsevier full text paywalled with no open location as of 31 July 2026. The
  tabulated empirical chance levels as a function of sample size, class count, cross-validation
  parameters and classifier are explicitly recorded as reported but not accessible, and they are the
  part a user would actually apply. Every quantitative claim on that card except "up to 70% or
  higher" is a description of what the paper reports having done.
- [tuab](../collection/datasets-benchmarks/tuab/card.md) and
  [tuev](../collection/datasets-benchmarks/tuev/card.md) — the release's `_AAREADME` sits behind the
  registration wall; probed public URLs returned 404. This is where patient-disjointness of the
  distributed partition would be recorded, which makes it the strand's most consequential
  inaccessible item.
- [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) — **removed by the audit,
  and retained only to record the removal.** This entry said per-dataset accuracies live in
  supplementary tables 5, 6 and 7 outside the main text, so only average ranks and a handful of
  named values were verifiable. The card was corrected: Supplementary Tables 2, 5, 6 and 7 are all
  present in the regenerated extraction, including the `#Params` column for all ten checkpoints, so
  the per-dataset accuracies and the inputs to the log-parameter correlation are verifiable from
  this source. §5.2 already carried half of this correction; the other half was still stated here
  and in §8.1, and both are now consistent with it.
- [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) — **this entry was removed by the
  audit and is retained only to record the removal.** An earlier version listed Brain4FMs here on the
  grounds that full results were deferred to Appendix D and that Cohen's κ was absent from the
  recovered tables. Appendix D is in the extraction in full, Tables 8 through 29, and κ is reported
  in seven of them; the metrics are split by task type rather than omitted, AUROC/Acc/F1/F2 for
  binary tasks and AUROC/Acc/macro-F1/κ for multi-class. Nothing about this suite is
  reported-but-unread.
- [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) — the numeric split
  ratios exist in the GitHub repository rather than the paper, which its own card calls a
  reproducibility gap in a document whose purpose is reproducibility.
- [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) — Figure 1 carries the directory
  tree and the TSV previews where the actual column names appear, and it is an image that did not
  survive extraction, so the card does not enumerate required columns.
- [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) — the
  figure showing the 22 electrode positions did not survive extraction and the positions are never
  enumerated in text. **And a second, larger item, which is a regression rather than a retrieval
  failure:** the card's `source.md` had held the official Brunner data-set-2a description appended
  behind a delimiter banner, and a 2026-08-01 re-extraction run over the review PDF alone dropped
  it. Nothing on the card is now sourced to that document. This is the only entry in the strand
  where the corpus lost a source it had already obtained, and it is what removed the footing under
  the EOG claim in §4.4. Re-appending `desc_2a.pdf` restores it; the document itself is still public
  at bbci.de.
- [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) — `md_quality: partial` for a
  specific reason: the unprintable delimiter bytes 20 and 21 *are* the specification, and the
  HTML-to-text conversion silently dropped them, so every worked annotation example in the extraction
  has lost its field boundaries. The byte layout on the card was reconstructed from surrounding prose.
- [moabb](../collection/datasets-benchmarks/moabb/card.md) — `pdf_status: not-available`. The version
  of record is open access under CC BY 3.0 but two download attempts returned an IOP bot-manager
  captcha, so the arXiv preprint was read instead.
- [varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
  — the carded version is the arXiv preprint of 26 June 2017, not the NeuroImage version of record;
  any change made in revision is not captured. Added by the audit: Table 1's body is not in the
  extraction either, only a truncated caption, so the ±15 / ±6 / ±3 bounds this document used to
  quote are marked unverified on the card and here (§3.2). Re-retrieving the version of record would
  resolve both at once.
- [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) — per-subject
  detail is in `SC-subjects.xls` and `ST-subjects.xls`, not retrieved.
- [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) — the signed access
  form's actual text was not retrieved, which is what any redistribution question turns on.

**Never reported by the source.** Re-retrieval of the same document would not help.

- [tuev](../collection/datasets-benchmarks/tuev/card.md) — the corpus's own documentation is one
  paragraph; participants, channels, sampling rate, hours, class balance and the partition are all
  unknown from the primary source, and there is no descriptive document at all, unlike TUAB's thesis
  or the parent corpus's data report.
- [tuab](../collection/datasets-benchmarks/tuab/card.md) — **only one of the three items previously
  listed here survives.** Patient-disjointness is indeed simply not asserted in the document the
  corpus names as its description, and that remains the strand's most consequential silence. The
  other two were wrong: the thesis tabulates patient counts (2,138 + 253) and hours (1,064.7 +
  104.4) alongside its file counts, and the card was corrected to say so. What is genuinely absent
  is any subject count or hours figure on the corpus *landing page*, which is a different and much
  weaker claim than the one this section used to make.
- [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) — no recording-hours
  total (only the channel-summed 29.1 years), no montage, no bit depth in the paper.
- [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) — no total hours, no
  per-run durations beyond "one-minute" and "two-minute", no participant count in prose, and no
  errata or exclusion list of any kind. The card now carries an **unverified** marking on the reason
  that absence matters, and the marking has to travel: that several subjects have anomalous run
  timings or sampling rates and are routinely dropped is field knowledge, stated by no source read
  in this strand, and it needs a citation before anything rests on it. What the landing page
  establishes is only the absence of errata, not that there is something an erratum should have
  covered.
- [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) — no participant
  count, no total hours, no per-recording durations.
- [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) — no total
  hours, and the per-subject kappa breakdown for 2a does not exist in the review (only for 2b).
- [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) — no licence statement and no
  maintainership statement anywhere on the specification page.
- [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) — no confidence
  intervals or significance tests anywhere.
- [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) — does not state whether
  any of its ten checkpoints was pretrained on any of its 54 evaluation datasets.
- [mne-python](../collection/datasets-benchmarks/mne-python/card.md) — no version number anywhere in
  the paper; the word "version" appears only in "version control system".

Three entries have a paywalled *requested* citation that is not a data descriptor, so the
inaccessibility costs little: [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md)
requests Schalk et al. 2004, a paper about the BCI2000 software system;
[sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) requests Kemp et
al. 2000, a study of slow-wave microcontinuity; and
[edf-plus](../collection/datasets-benchmarks/edf-plus/card.md)'s journal article duplicates the
freely available specification page. Each card says which document it actually used.

---

## 8. Where the corpus disagrees with itself

A register. Nothing here is resolved, because resolving it would require the sources, and in most
cases the sources contradict themselves so there is nothing to resolve to.

### 8.1 Kind 1 — two cards disagreeing about the same quantity

**LaBraM's supported channel count — 136 or 137, and the disagreement is between two cards of the
same paper.** [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) records 136
from the benchmark's Table 7 and flags the body/table conflict as an internal inconsistency of the
source; [eeg-models/adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md)
records 137 from the body, in two places, without flagging it. The primary source
([eeg-models/labram-2024](../collection/eeg-models/labram-2024/card.md)) states no count, indexing
its spatial embedding "over the universal 10-20 channel set", and
[eeg-models/zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)
reports 128-channel position embeddings interpolated per dataset. **This is a defect in our corpus
rather than a fact about the field: two cards of one work took different sides of that work's own
internal conflict, and only one records that there is a conflict.** A synthesis document cannot fix a
card; the entry is named so it can be filed. The corpus's standing rule prefers tables over body
prose, which selects 136. Also registered in pilot §6.1 from the model side.

**EEGPT's pretraining hours — 198 or 246, same shape, same pair of cards.**
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) records 198 h from Table 7
and flags "246 hours" in the body;
[eeg-models/adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) records 246.
[eeg-models/eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) reports no hours figure at all,
so the primary cannot adjudicate. **A second instance of the same corpus defect, in the same pair of
cards.**

**BIOT's fixed channel count — 16 or 18.**
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) records BIOT as supporting
18 fixed channels and builds an argument on it, calling that count the model's bottleneck against
62-channel downstream tasks; [eeg-models/biot-2023](../collection/eeg-models/biot-2023/card.md)
states that its EEG datasets use "the common 16 bipolar montage channels in the international 10-20
system" and describes its PREST pretraining corpus the same way. This one is cross-strand and is not
a corpus defect: a benchmark's account of a checkpoint disagrees with the checkpoint's own paper, and
the disagreement is load-bearing for the benchmark's argument.

**BENDR's parameter count — 3.97M, 0.39M, 157M, or unpublished.**
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) Table 1 gives 3.97M;
[eeg-models/femba-2025](../collection/eeg-models/femba-2025/card.md) gives 0.39M;
[eeg-models/zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)
gives 157M as the largest model in its six-model panel; and
[eeg-models/bendr-2021](../collection/eeg-models/bendr-2021/card.md) publishes no total. The full
register including how the spread propagates into Zare's conclusion is pilot §6.1. What this strand
adds is the second consumer of those counts: BENDR is one of the ten checkpoints over which
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) computes its
log-parameter-count correlation with per-dataset rank. An earlier version of this line added that
the suite's own counts were not recoverable from what was read; that is no longer true, and the
change alters what should be done about it rather than resolving it. Supplementary Table 2 carries a
`#Params` column for all ten checkpoints, so OmniEEG-Bench does state a BENDR figure and it is
readable from the carded source; this document has not read it off, and a later reader should,
because it would be a fourth entry beside Brain4FMs's 3.97M, FEMBA's 0.39M and Zare's 157M — in the
one place in the strand where a parameter count is an independent variable in a statistical claim
(§5.2, §7).

**CBraMod's parameter count and pretraining hours — three and four values.** Parameters: 4.88M in
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) Table 1, 4.0M computed with Thop in
[eeg-models/cbramod-2025](../collection/eeg-models/cbramod-2025/card.md), and 4.9M backbone / 8.1M
with task heads in
[eeg-models/zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md).
Hours: 9,246 in [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) Table 7
against "approximately 27,000" in that same paper's body; "longer than 9000" retained from a
27,062-hour corpus in [eeg-models/cbramod-2025](../collection/eeg-models/cbramod-2025/card.md); 9,200
in Zare; and "~9,000-hour cleaned subset" in
[eeg-models/lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md). The
9,246-versus-27,000 pair is a single source disagreeing with itself (§8.2); the rest are consistent
with the retained figure being roughly 9,000 hours out of roughly 27,000, which the primary never
states exactly.

**NeuroLM's parameter count — 169.60M or 1.7B.**
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) Table 1 tabulates 169.60M;
[eeg-models/kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)
gives "3.3M in BIOT to 1.7B in NeuroLM" as the parameter range of its reviewed field, so its
model-scaling conclusion is anchored on that upper bound. Neither source cites a primary for the
figure, and pilot §6.1 records why this one cannot be adjudicated inside the corpus.

**The requirement level of `electrodes.tsv` — recorded as ambiguous or resolved, by two cards of the
same paper.** [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) records that the paper
states it two ways, a conditional "should be specified if the positions of the electrodes are known"
against an unconditional "may in addition specify", and treats the difference as unresolved;
[candidate-datasets/eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md) states
flatly that `channels.tsv` is required while `electrodes.tsv` and `coordsystem.json` are "recommended
rather than required, so a fully valid BIDS-EEG dataset can contain no electrode coordinates at all",
and builds a consequence on it. The two are compatible in substance and different in epistemic
status, and only one records that the source is ambiguous. **A milder instance of the same corpus
defect, between two cards of one paper.**

**OpenNeuro's scale — 604/20,989/165 with an unreconciled 502, or the abstract's rounded figures.**
[openneuro](../collection/datasets-benchmarks/openneuro/card.md) records 604 datasets, 20,989
participants and 165 reuse publications, and flags both that the abstract rounds ("more than 600 ...
more than 20,000 ... more than 150") and that "the 502 OpenNeuro datasets available via DataLad as of
10/9/2021" appears in the same paper on the same cutoff date with the 102-dataset gap never
reconciled. [candidate-datasets/openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md)
records the rounded pair. Not numerically incompatible, but the 604-versus-502 gap is recorded on one
side only. **Same-paper divergence; the weakest of the four, and listed for completeness.**

### 8.2 Kind 2 — sources contradicting themselves, carded faithfully

Fifteen of the 18 entries carry at least one such record, which makes it a property of the corpus
rather than of any one entry. The three without are
[tuev](../collection/datasets-benchmarks/tuev/card.md),
[physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) and
[combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md),
and in each case the reason is that the source is too short to contradict itself.
[tuab](../collection/datasets-benchmarks/tuab/card.md) was a fourth until the audit found one in its
thesis; see the entry below.

- [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) — five, plus two more.
  Table 7 against the body for EEGPT (198 h / 246 h), CBraMod (9,246 h / ~27,000 h) and LaBraM
  (2,535 h and 136 ch / ~2,500 h and 137 ch); few-shot sampling ratios `[0.02, 0.05, 0.3, 0.5]` in
  Methods against `[0.02, 0.05, 0.1, 0.3, 0.5]` in the Figure 2 caption and results text; a
  learning-rate grid that lists `5e-4` twice and omits an obvious fifth value. Separately, SHHS is
  6,441 subjects in the body against the 329 selected healthy subjects the benchmark actually uses;
  the normalization table labels the EEGMAT dataset "EDMAT"; and the arXiv landing-page abstract for
  v2 differs in wording from the abstract in the v2 PDF.
- [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) — the primary leaderboard
  mixes protocols, scoring longitudinal
  test-retest under the multi-subject fallback while including it in the same average-rank
  computation as the cross-subject tasks, so the headline ranking is not uniformly a cross-subject
  ranking.
- [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) — "BFM" is used both as the
  abbreviation for the class of brain foundation models and as the name of one specific
  708.96M-parameter model, so the token is ambiguous in that source. That is now the whole of the
  entry: the second half, that Cohen's κ is listed among the reported metrics and does not appear in
  the recovered result tables, was an extraction artefact and not a property of the source, and the
  card was corrected (§7).
- [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) — the pretraining-overlap
  conclusion rests on "we did not notice a clear trend" rather than a test, while the overlapping
  cells are neither excluded nor separately analysed.
- [moabb](../collection/datasets-benchmarks/moabb/card.md) — Section III specifies a
  permutation-based paired t-test for datasets with fewer than 20 subjects and Wilcoxon otherwise,
  but the Figure 2 and Figure 3 captions attribute all per-dataset p-values to "the one-tailed
  Wilcoxon signed-rank test", including datasets with 4, 9, 10, 13 and 14 subjects. Which test
  produced the small-dataset p-values is unresolved in the paper. Dataset naming also differs between
  table and figures: "Yi et al. 2014" against "Weibo 2014", "BNCI2014-001" against "001-2014".
- [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  — the headline 3,900 percent figure is attributed to schizophrenia in the Discussion ("all the way
  up to a 3900% increase in error rate in the case of the schizophrenia dataset"),
  but 0.197/0.005 ≈ 39× is the PTSD ratio and the paper's own section 4.4 calls PTSD "the
  2nd largest difference", while the schizophrenia MLP ratio is roughly 62×. Further: driver-fatigue
  proper error 0.46 in the body against 0.466 in Table 3 with an interval centred on 0.46;
  driver-fatigue proper accuracy 0.540 in the body against 0.50 in Table 1; PTSD observations per
  participant 200 then 260 three sentences later; alcoholism channels 64 in the body and 62 in the
  appendix; confused-students participants 10 in Table 2 against "Sessions from all nine
  participants were merged together" in the passage describing the replicated protocol; the
  confused-students effect "over 33%" in the body and 35 percent in the abstract. And Table 3's
  caption claims a significant difference in a paper that runs no test.
- [varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
  — the main text states the standard-error underestimation as "a factor of 0.7 in the best case"
  while the appendix gives 0.73 for leave-one-out and 0.26 for repeated splits, so a reader quoting
  only the main text understates the repeated-splits problem by nearly threefold. The headline
  summary is also optimistic relative to the paper's own real cohorts: at n = 30 the binomial gives
  −15/+12 while the simulations give −20/+18 and the appendix's empirical leave-one-out bound is
  ±18.9, and the stated ±10 percent at n = 100 sits against a −21/+18 within-subject fMRI cohort at
  ~212 samples. (This comparison was previously anchored on Table 1's ±15 at n = 30, which the audit
  marked unverified; the point survives on the binomial row instead.) And two statements about
  repeated splits versus leave-one-out are left unreconciled.
- [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) — the body announces
  release v0.6.0 while the reference list cites v0.6.3; the reported age statistics are not
  internally coherent ("average 51.6, stdev 55.9" on a distribution bounded between under 1 and over
  90); the annotation-class enumeration announces six classes then lists three before reconciling
  them a paragraph later; and "record", "session", "EEG" and "scan" are used interchangeably, with
  the max-per-patient statistic switching unit mid-sentence.
- [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) — section
  5.1 calls the data "a three class motor imagery task" while section 5.2.1 and Table 1 both say
  four; the review pluralizes the test sessions where there are exactly two per subject; and "test"
  and "evaluation" name the same files in different places, Table A1's columns headed Training and
  Test against section 5.4's "evaluation data sets". All three were previously stated as clashes
  between the review and the official Brunner description; that document is no longer in the carded
  source (§7), and all three turn out to be internal to the review, which is where they now sit.
- [openneuro](../collection/datasets-benchmarks/openneuro/card.md) — 604 datasets against "the 502
  OpenNeuro datasets available via DataLad", both dated 9 October 2021, never reconciled; Table 1's
  modality counts sum to 1,124 against 604 total datasets with no statement that a dataset may be
  counted under more than one modality, so "81 EEG datasets" is not a count of EEG-only datasets; CC0
  called a dedication, a licence and an agreement in three places; "session" used in two senses and
  "dataset" overloaded between an upload and a snapshot of it.
- [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) — the `electrodes.tsv` requirement
  stated as a conditional "should" and an unconditional "may"; "only two" official formats named in
  the same paragraph that permits four; no `run-` entity in the naming pattern although BIDS defines
  one.
- [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) — "one session in one file" promised
  twice and prohibited once; "epoch" used for a data record and for a sleep-scoring interval with no
  disambiguation, and "window" as a third near-synonym; a sleep-stage nomenclature that gives
  "W,1,2,3,4,R,M" in section 2.3 and "Sleep stage N1/N2/N3" in the section 3.3 annotation example
  with no mapping and no stage 4; a table-of-contents heading that does not match its section
  heading. Two details were corrected on the card and both were external conventions this document
  had absorbed: the specification states no scoring-epoch length anywhere, so the "30-second"
  qualifier is not the source's, and it never names the Rechtschaffen-and-Kales or AASM schemes,
  so the identification of the two nomenclatures is ours and not the specification's. The mismatch
  itself is real either way.
- [tuab](../collection/datasets-benchmarks/tuab/card.md) — **new to this node after the audit.**
  Lopez de Diego's thesis, the document the corpus names as TUAB's description, contradicts itself
  on its own best-system error rates: the body says the hybrid HMM-SdA system "was able to achieve
  an error rate of 22.9%" while Table 16 records 22.1%. The card records both and prefers neither.
  Separately, and not a contradiction, the card previously misread that table: 24.6% is the
  epoch-based HMM with majority vote, not the stacked-denoising-autoencoder system, and the thesis's
  best result is CNN-MLP at 21.2%. No figure from that table was used in this document.
- [mne-python](../collection/datasets-benchmarks/mne-python/card.md) — "epoch" and "trial" used as
  synonyms; two typographical errors in the source itself. The card's further claim that "epoch"
  also does duty as a training hyperparameter was removed by the audit: every occurrence in the
  decoding section is the data-segment sense, and the decoder there is a support vector machine,
  which has no epoch parameter.

### 8.3 Kind 3 — differences that look like disagreements and are not

Recorded so a later reader does not promote one into §8.1.

- **Channel counts for the Temple University subsets name three different objects.** For
  [tuab](../collection/datasets-benchmarks/tuab/card.md): 31 typical in the parent recording, 22 in
  the thesis's transverse-central-parietal re-derivation, 23 in AdaBrain-Bench's preparation. For
  [tuev](../collection/datasets-benchmarks/tuev/card.md): 31 in the parent, 23 in AdaBrain-Bench, 16
  bipolar derivations in the field's BIOT-derived convention. These are a recording, a benchmark's
  channel selection and a derivation scheme, and the TUEV card states the distinction the corpus
  documentation never makes: 16 bipolar channels is a montage in the strict sense, whereas 23 or 31
  is an electrode count. This is the strand's most common trap, because "channels" names both.
- **Roundings of one figure.** BIOT at 3.19M in
  [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) against 3.2M in
  [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md); LaBraM at 5.80M in both;
  REVE at 69.19M in Brain4FMs against 69M and 69.4M elsewhere, which pilot §6.3 also registers.
- **Unit changes that are not conversions.**
  [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) reports "a grand total of
  29.1 years (total duration summed over all EEG channels)", a channel-summed figure that is not
  convertible to recording hours without the per-file channel count, against REVE's 26,847 hours from
  Temple University Hospital in its own accounting. The card records that the 29.1-year figure "is
  routinely misquoted as recording duration".
- **Counts of different units.** [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)'s 197
  *recordings* and 153/44 file split do not map cleanly onto the 78 *subjects* quoted from benchmark
  preparations, because most subjects contributed two nights and three nights were lost.
  [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md)'s 5,184 is
  arithmetic from 9 × 2 × 288 rather than a stated figure.
- **One case that has moved out of this node.** TUAB used to sit above as a units difference — the
  thesis counting 2,785 training and 280 evaluation *files* against AdaBrain-Bench's 2,383
  *subjects*. The card was corrected: the thesis counts patients too, 2,138 plus 253, so the two
  sources are now naming the same unit and differ by eight. That is a small unexplained numeric
  disagreement rather than a category confusion, and neither source lets a reader resolve it (§5.2).
  It is recorded here rather than promoted to §8.1 because the gap is within rounding distance of a
  release difference and nothing rests on it.
- **Reconcilable count pairs the sources do not reconcile.**
  [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)'s "15 BFMs and 18 public datasets"
  against "22 downstream classification tasks from 18 public datasets" — reconcilable, but a reader
  quoting "18" should say whether they mean datasets or tasks.
  [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md)'s 94 datasets against 97
  task-datasets, and 14 architectures resolving as 8 task-specific plus 6 foundation models.
  [moabb](../collection/datasets-benchmarks/moabb/card.md)'s "over 250 subjects" in the abstract and
  conclusion against Table I's own total of 275, which the prose never states.
- **Two label schemes that need a mapping nobody states.**
  [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)'s hypnograms are
  Rechtschaffen and Kales with stages W, 1, 2, 3, 4, R, M and "?", while
  [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) reports its sleep-staging
  datasets under the AASM five-class scheme. Merging stages 3 and 4 into N3 and dropping movement time
  is the usual mapping, but neither source states it, so a five-class Sleep-EDF result and the
  dataset's own eight-label hypnogram are not the same label space. The same mismatch appears
  internally in [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) (§8.2), though there
  it appears as two stage vocabularies rather than as two named schemes — the specification names
  neither, as the audit established.

### 8.4 One tension that is none of the three kinds

Recorded so it is not filed as a kind-1 disagreement.
[kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
reports 95 percent confidence intervals on every value with the construction unstated, and
[varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)'s
analysis implies those intervals cannot be right. That is not two cards disagreeing about a quantity
and not a source contradicting itself: it is one entry's method assessed against another entry's
standard, and both cards state the relation in the same direction. See §3.4.

---

## Coverage: all 18 entries and where each sits

The facets are orthogonal by construction, so most entries appear several times: every suite has a
split rule (§1), a specification (§2), an uncertainty practice (§3) and a checkpoint set (§5), and
every dataset has a recording context (§4), a place in the mapping (§5) and a documentation status
(§7). The "primary" column names the node where the entry is most distinguishing.

| entry | primary node | also appears in |
|---|---|---|
| [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) | §2.3 fixes the recipe, states no ratio | §1.2, §1.3, §2.1, §2.2, §2.4, §3.4, §3.5, §4.3, §5.1, §5.2, §7, §8.1, §8.2, §8.3 |
| [bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md) | §1.5 the protocol built to resist, and its expiry | §1.4, §3.5, §4.2, §4.4, §5.1, §6.4, §7, §8.2, §8.3 |
| [brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) | §2.1 the only per-task-family supervised comparators | §1.3, §2.2, §2.3, §2.4, §2.6, §3.4, §5.1, §5.2, §7, §8.1, §8.2, §8.3 |
| [combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md) | §3.1 the null is not the theoretical chance level | §3.3, §7 |
| [edf-plus](../collection/datasets-benchmarks/edf-plus/card.md) | §6.1 where a stimulus marker lives | §1.2, §6.2, §6.3, §7, §8.2, §8.3 |
| [eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) | §6.2 what the raw layer cannot express | §4.1, §6.1, §6.3, §7, §8.1, §8.2 |
| [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md) | §1.1 the measured cost of moving the boundary | §1.2, §3.4, §6.3, §8.2, §8.4 |
| [mne-python](../collection/datasets-benchmarks/mne-python/card.md) | §6.4 the reference reader | §2.5, §6.1, §7, §8.2 |
| [moabb](../collection/datasets-benchmarks/moabb/card.md) | §3.3 the corpus's only cross-dataset inference procedure | §1.3, §2.1, §2.4, §2.5, §5.1, §7, §8.2, §8.3 |
| [neuralbench](../collection/datasets-benchmarks/neuralbench/card.md) | §1.3 per-task split strategy, labelled per panel | §2.1, §2.2, §2.3, §2.4, §2.5, §2.6, §3.4, §4.3, §5.1, §6.4, §8.2, §8.3 |
| [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md) | §2.2 demonstrates that the regime reorders the models | §1.2, §1.3, §2.1, §2.3, §2.4, §2.6, §3.4, §4.1, §5.2, §7, §8.1, §8.2 |
| [openneuro](../collection/datasets-benchmarks/openneuro/card.md) | §4.2 the one unambiguous data licence | §4.1, §5.1, §6.1, §8.1, §8.2 |
| [physionet-mi](../collection/datasets-benchmarks/physionet-mi/card.md) | §5.1 the cleanest pretraining ablation in the mapping | §2.5, §4.1, §4.2, §4.3, §6.1, §7 |
| [sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md) | §4.4 the peripheral channels every suite discards | §3.5, §4.1, §4.2, §5.1, §6.2, §7, §8.2, §8.3 |
| [tuab](../collection/datasets-benchmarks/tuab/card.md) | §1.4 an inherited split whose grouping is undocumented | §3.5, §4.2, §4.3, §5.1, §5.2, §7, §8.2, §8.3 |
| [tuev](../collection/datasets-benchmarks/tuev/card.md) | §6.2 what a bipolar convention costs a coordinate model | §1.4, §3.5, §4.2, §4.3, §5.1, §5.2, §7, §8.3 |
| [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) | §4.1 the clinical substrate under most checkpoints | §4.2, §4.3, §5.1, §6.2, §7, §8.2, §8.3 |
| [varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md) | §3.2 the interval is wider than the reported statistic | §1.2, §3.3, §3.5, §7, §8.2, §8.4 |

Two entries sit in three nodes or fewer —
[combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
and [mne-python](../collection/datasets-benchmarks/mne-python/card.md). That is the intended shape
rather than a placement failure: neither prescribes a split, neither reports a checkpoint result, and
neither is a corpus, so most facets have no value to record for them. No entry failed to fit a node.
