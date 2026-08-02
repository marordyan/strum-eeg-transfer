# Ontology of the `eeg-models` strand

Phase 3 synthesis, strand A. Input is the 22 entries in
`research/collection/eeg-models/` and nothing else; where a fact is grounded in a sibling
strand's card, that card is linked instead.

This document says what the strand contains and how its pieces relate. It is not the gap
analysis: it does not enumerate what the field is missing, does not rank entries, and does not
recommend a checkpoint. Where two cards disagree, both readings are recorded and neither is
picked. Where a claim is repeated by several cards but traces to one measurement, it is counted
once and the repetition is named as repetition.

Every concrete claim below carries a card link. Every leaf of the tree is a card link. All 22
entries appear; the coverage table at the end says where each one sits.

---

## Why this tree, and not the brief's five categories

`_briefs/strand-eeg-models.md` scopes the strand into five categories: pretraining objectives,
architectures, released checkpoints and reproducibility, transfer and fine-tuning evidence, and
negative and null results. The collection was run against those categories and the strand's
`INDEX.md` is organized by them. This ontology departs from them deliberately, for a reason
visible in the index itself: eight of the 22 entries are cross-listed under two headings, and
every one of the five headings carries a trailing prose paragraph beginning "also relevant" or
"checkpoint facts also sit inside other cards", because the load-bearing facts would not stay in
one box. The brief's categories are a *collection* instrument — they tell a collector what to go
and find — and they discriminate well on provenance of the paper. They discriminate badly on the
properties that distinguish one entry from another once collected.

Three examples of the mismatch, each grounded:

- "Architectures" and "released checkpoints" split facts about the same object. The single most
  discriminating property of an architecture in this corpus is how it binds spatial identity, and
  that property *is* the input contract — the thing category 3 asks for. Category 2 holds
  [reve-2025](../collection/eeg-models/reve-2025/card.md)'s coordinate encoding while category 3
  holds [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md)'s inventory of
  what channel counts those same checkpoints accept.
- "Transfer evidence" and "negative results" are not two kinds of work; they are two possible
  outcomes of one kind. [sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md)
  and [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) are
  cross-listed under both for exactly that reason.
- The property that most changes how a transfer number should be read is not which category the
  paper sits in but whether the backbone was frozen. That axis cuts across all five categories and
  is invisible in the index.

The tree below is organized by four questions a reader can ask of any entry, plus two guard nodes:

1. **Spatial identity** — what a checkpoint requires of your electrode set (§1).
2. **Provenance** — what it was made from: objective, corpus, scale (§2).
3. **Evidence** — who measured it, under which adaptation protocol, against what baseline, under
   which split (§3).
4. **Where it fails** — the negative and null results, positioned against the positive ones (§4).
5. **What is not transfer evidence at all** — the motivation line and the second-hand entries (§5).
6. **Where the corpus disagrees with itself** — a register, not a resolution (§6).

Nodes 1 and 3 are the two that reorder the corpus relative to the index. Node 1 is the strand's
sharpest structural axis because it is a hard admissibility condition rather than a matter of
degree: the project's target recording is 206 EEG channels
([strum-2018](../collection/candidate-datasets/strum-2018/card.md)), and several mechanisms in §1.1
have no defined behaviour at that width, while every mechanism in §1.2 and §1.3 does. Node 3 is the
axis that changes the ordering of the models without changing a single model.

---

## 1. Spatial identity: how a checkpoint binds a channel to a place

The question this node answers: for each entry, what does the model need to know about an
electrode before it can encode that electrode's signal, and what happens when the electrode set is
one the model never saw. The five mechanisms below are mutually exclusive; each entry that ships a checkpoint sits in
exactly one.

### 1.1 Bound to a learned per-channel parameter

A row, slot or table entry exists per channel identity. An identity absent from pretraining has no
parameter, so the electrode set is bounded by the pretraining vocabulary.

- [labram-2024](../collection/eeg-models/labram-2024/card.md) — a learned spatial embedding list
  indexed by channel over the universal 10-20 channel set, added to patch features as absolute
  positional encoding. A channel must be nameable within that set to be encoded at all. A second,
  independent bound applies: the sequence is capped at 256 patches, so channel count and window
  length trade against each other, the paper's own examples being 64 channels at 4 seconds or 32
  channels at 8 seconds.
- [biot-2023](../collection/eeg-models/biot-2023/card.md) — a learned embedding indexed by channel
  *name*, summed with a parameter-free sinusoidal position embedding. Recording length is genuinely
  unconstrained and missing channels and segments are representable by construction, because the
  sample is simply a shorter sentence; the binding constraint is vocabulary, not length. The card
  records that the paper does not say what happens when a downstream dataset presents a channel
  absent from that vocabulary — the missing-channel study removes known channels rather than
  introducing unknown ones. A consequence of keying on a name rather than a position, and the only
  demonstrated case of it in §1: the vocabulary is not confined to EEG. BIOT pretrains on a
  cardiology corpus of 21,264 six- or twelve-lead ECG recordings and reports an ECG downstream task,
  so an ECG lead occupies a row in the same channel table as an EEG derivation. Other mechanisms
  here neither admit nor exclude a peripheral channel by construction; the one that excludes it
  explicitly is [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) in §1.2, whose
  type vocabulary has exactly three values.
- [bendr-2021](../collection/eeg-models/bendr-2021/card.md) — the crudest mechanism in the strand
  and stated plainly as such: a fixed 20-slot index map (Deep1010, from the DN3 library), surplus
  channels ignored and missing channels set to zero. The authors' own stated limitation is that it
  is "presently unclear to what degree" the model leverages spatial information, and that an absent
  electrode is indistinguishable from a flat one.
- [femba-2025](../collection/eeg-models/femba-2025/card.md) — a 2D convolution over patches spanning
  4 channels × 32 samples with learnable positional embeddings, illustrated at C = 22. The paper
  states no sampling rate, filtering or referencing specification at all — the card records that the
  string "Hz" does not occur anywhere in it — so the contract has to be recovered from released code.
  The one channel-side constraint on record comes from outside the paper: `omnieeg-bench` classes
  FEMBA among the checkpoints that require predefined bipolar derivations.

### 1.2 Computed from physical coordinates or sensor metadata

Spatial identity is a function of where the sensor is, not of what it is called. An unseen
electrode set costs no new parameters.

- [reve-2025](../collection/eeg-models/reve-2025/card.md) — a 4D positional encoding: each
  electrode's (x, y, z) plus a scaled temporal patch index, projected into a multi-frequency Fourier
  basis and summed with a learned projection of the same 4D coordinate. Because nothing is looked up
  by channel name, an unseen electrode set requires no new parameters. The requirement it does
  impose is that every channel carry a 3D coordinate; channels without an identifiable name or
  position were excluded from pretraining.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — a Sensor Encoder embedding of
  a 6-dimensional position-and-orientation vector plus a type label (0 EEG, 1 gradiometer,
  2 magnetometer). One tokenizer covers devices from 19 to 306 channels. The type vocabulary has
  exactly three values, so a channel that is not one of those three has no representation.
- [luna-2025](../collection/eeg-models/luna-2025/card.md) — a NeRF-style sinusoidal encoding of the
  normalised 3D coordinate through an MLP, followed by 4 to 8 learned queries that cross-attend to
  the channel dimension before any temporal attention runs.

A structural distinction *inside* this node that no single card states, and that follows from two:
coordinate-based ingestion does not by itself give a fixed downstream feature width.
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) compresses any C to C′ = 16 latent
source variables and [luna-2025](../collection/eeg-models/luna-2025/card.md) to Q × E, so the head
sees a constant width whatever the electrode count; whereas
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) records that
REVE "needs no interpolation because it consumes 3D coordinates, but its embedding dimension scales
with channel count since it does not spatially pool". Admissibility and fixed feature width are
separate properties, and this node separates on the first, not the second.

The compression that buys the fixed width is itself bounded, by both cards' own evidence:
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) justifies C′ = 16 only by a
reconstruction-loss curve and never compares other values of C′ on a downstream task, and
[luna-2025](../collection/eeg-models/luna-2025/card.md) reports that on SEED-V — the one electrode
layout absent from its pretraining — LUNA-Huge reaches 0.3900 balanced accuracy against CBraMod's
0.4091 and LaBraM-Base's 0.3976, with the authors writing that "generalizing zero-shot to vastly
different, high-density layouts remains challenging, possibly due to positional encoding
constraints".

### 1.3 Generated from local context, neither indexed nor coordinate-derived

- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — asymmetric conditional positional
  encoding: a one-layer depthwise 2D convolution over each patch's channel-by-time neighbourhood,
  with a kernel longer in the channel dimension than in time. Nothing is indexed and no coordinate
  is required, so an unfamiliar channel count needs no new positional parameters. The card is
  explicit that this is a property of the encoding rather than something demonstrated at pretraining
  time: all pretraining used the same 19 channels of the 10-20 system.

### 1.4 Learned remap onto a fixed superset

- [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) — a trainable 1×1 convolution, an
  "adaptive spatial filter", maps an arbitrary downstream channel set onto the model's fixed
  58-electrode superset. This is neither a name lookup nor a coordinate function: it costs a small
  number of trainable parameters per new dataset but requires no pretrained row per electrode. The
  card notes the superset is presented in a figure and never listed in text.

### 1.5 Position-blind

- [brainwave](../collection/eeg-models/brainwave/card.md) — channel attention relates patches that
  co-occur in time across channels, making the model channel-count agnostic without using electrode
  position at all. The card states the consequence precisely: the paper reports no required channel
  ordering, no reference or montage convention, and no position information, so channel-count
  agnosticism does not imply montage generalization in the sense §1.2 provides. Its distinct move is
  on the *rate* axis instead — a scale-alignment layer fixes spectrogram window and hop as a ratio
  of a 1-second patch, so recordings at different sampling rates need no resampling.

### 1.6 No checkpoint, therefore no contract

- [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) — channel count enters as
  the spatial-convolution kernel height (ch, 1) and is set at build time; window length changes the
  flattened classifier width. There is nothing pretrained to satisfy. What the paper does fix is
  preprocessing: a sixth-order Chebyshev band-pass and z-score standardisation with statistics taken
  from the training split.

### 1.7 What each mechanism does with a bipolar derivation

A derivation is a difference between two electrodes, not a signal at one, so it has no single
position. The corpus contains four different answers and one silence, and they are not equivalent:

- [reve-2025](../collection/eeg-models/reve-2025/card.md) — the midpoint of the pair. The card flags
  this as lossy in a way the paper does not examine: two different pairs can share a midpoint, and
  the midpoint discards the orientation and separation that a differential recording measures. No
  ablation compares the choice against alternatives.
- [bendr-2021](../collection/eeg-models/bendr-2021/card.md) — the first electrode of the pair.
  FPz-Cz and Pz-Oz were "simply mapped" to FPz and Pz, discarding the second electrode entirely, and
  the paper's one large-dataset result and its one null result both rest on it.
- [biot-2023](../collection/eeg-models/biot-2023/card.md) — the derivation owns a row like any other
  name. Internally coherent, with the consequence the card names: the pretrained channel vocabulary
  is a vocabulary of *derivations*, and a referentially recorded dataset does not share it.
- [luna-2025](../collection/eeg-models/luna-2025/card.md) — unspecified. The entire Temple University
  pretraining and evaluation set is converted to a 20-pair longitudinal bipolar montage, the pairs
  are listed in an appendix, and the coordinate fed to the NeRF encoding for a channel such as
  Fp1–F7 is never stated.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — not discussed; every downstream
  EEG dataset is used in referential form, so the question does not arise in the paper and is
  unanswered for the model.

[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) shows the
issue biting on a result rather than in principle: its one clean positive, CHB-MIT ictal detection,
uses bipolar derivations with approximate positional coordinates, "which matters specifically for
REVE, whose whole mechanism is coordinate-based".

### 1.8 What third parties report it actually takes to load these

Three entries record loading behaviour from outside the model papers. These are the only
statements in the strand about the mechanism as encountered rather than as designed.

- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — the supported-channel
  inventory for four released checkpoints: BIOT 18 fixed, EEGPT 58, LaBraM 137, CBraMod arbitrary via
  input-conditioned channel embedding. It states the BIOT bottleneck explicitly: fixed 18 channels
  "is incompatible with downstream tasks such as SEED and SEED-IV (62 channels)". (Its LaBraM figure
  is contested; see §6.1.)
- [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) — the
  per-model exceptions a single harmonised pipeline had to make: BENDR resampled back to 256 Hz after
  a shared 70 Hz band limit, with 21-channel inputs truncated and 19-channel inputs zero-padded with
  a dead channel; LaBraM's 128-channel position embeddings linearly interpolated to each dataset's
  channel count; EEGMamba excluded from the 19- and 18-channel cohorts entirely by its fixed
  channel-count-specific patch embeddings. The author states the consequence — the BENDR and LaBraM
  results "should not be interpreted as clean tests of pretraining objective".
- [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) — two
  answers to one problem, in the same pipeline. For LaBraM, the quietest version: "only data from
  electrodes which were present in the global list provided were used", so the evaluation silently
  discards channels for any dataset whose montage exceeds LaBraM's vocabulary, and the paper does
  not say how many. For NeuroGPT, an explicit montage-repair procedure rather than a drop, added to
  the card during the audit: "For any expected channels which are not included in the benchmark
  data, the nearest available electrode's data is used (if the location is within a few
  centimeters), otherwise the channel data are set to zero." Two checkpoints in one harness get
  incomparable channel treatments, which is the same hazard
  [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) names above.

### 1.9 A terminology drift that crosses this axis

Three cards independently flag the same slippage, so it is a property of the literature rather than
of one paper, and it is the slippage most likely to make §1.2 look broader than it is.
[reve-2025](../collection/eeg-models/reve-2025/card.md) records that the paper's abstract and
conclusion say "montages" where its methods section says "arbitrary electrode layouts", and the card
instructs that the precise claim be carried forward.
[luna-2025](../collection/eeg-models/luna-2025/card.md) records that its title and abstract say
"topology-agnostic" and its conclusion "montage-agnostic", both looser than what the mechanism
supports. [biot-2023](../collection/eeg-models/biot-2023/card.md) records that BIOT's "16 bipolar
montage channels" are derivations, not positions. A layout is a set of positions; a montage is a
derivation scheme; the mechanisms in §1.2 generalize over the first.

---

## 2. Provenance: objective, corpus, and scale

### 2.1 Pretraining objective families

Six families, by what the loss is computed against. Objectives are carded under the architecture
that implements them, per the index's own decision, so this node is a re-cut of entries that live
elsewhere.

Masked reconstruction of raw signal:

- [reve-2025](../collection/eeg-models/reve-2025/card.md) — L1 on raw signal under joint
  spatio-temporal *block* masking (55% ratio, 3 cm spatial radius, 3 s temporal radius, plus 10%
  whole-channel dropout), with a secondary loss reconstructing the same masked patches from one
  attention-pooled global token. The card attributes REVE's frozen-feature advantage specifically to
  that secondary loss.
- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — mean squared error on the raw
  normalized signal at a 50 percent mask ratio.
- [femba-2025](../collection/eeg-models/femba-2025/card.md) — Smooth L1 over masked patches only,
  60 percent of patches zeroed.
- [luna-2025](../collection/eeg-models/luna-2025/card.md) — Smooth L1, plus a query-specialisation
  loss penalising off-diagonal similarity in the query-to-channel affinity matrix. The card records
  that removing the specialisation loss costs 0.003 to 0.006 AUROC, within seed variation, and that
  the authors keep it for its regularising role rather than for a measured gain.

Discrete-token prediction over a learned codebook:

- [labram-2024](../collection/eeg-models/labram-2024/card.md) — a vector-quantized neural tokenizer
  whose decoder reconstructs patch Fourier amplitude and phase, then masked prediction of the
  discrete codes.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — 4-layer residual vector
  quantisation over the compressed latent grid, then masked prediction of all four quantisation
  layers non-autoregressively at a 50 percent mask ratio.

Masked reconstruction in the time-frequency domain:

- [brainwave](../collection/eeg-models/brainwave/card.md) — masked reconstruction of a Gaussian-window
  spectrogram computed per 1-second patch.

Contrastive and perturbation-matching:

- [bendr-2021](../collection/eeg-models/bendr-2021/card.md) — wav2vec 2.0's contrastive loss,
  reproducing masked encoder outputs against distractors sampled from elsewhere in the same sequence.
- [biot-2023](../collection/eeg-models/biot-2023/card.md) — a BYOL-style predictor maps a
  channel-and-token-dropped view onto the unperturbed embedding, trained with contrastive
  cross-entropy.

Alignment against a learned representation rather than against the signal:

- [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) — a reconstruction loss plus an
  *alignment* loss matching the predictor's output for masked positions against a momentum encoder
  applied to the unmasked signal.

Temporal-context pretext tasks, compared head to head:

- [banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md)
  — relative positioning, temporal shuffling, contrastive predictive coding and a plain autoencoder,
  read out by the same linear probe. This is the only entry in the strand that isolates the
  objective from the architecture, and the isolation holds *within* a dataset rather than across the
  paper: the card records two embedders, not one — StagerNet at 62,307 trainable parameters on PC18
  and ShallowNet at 170,860 on TUH Abnormal — with all four objectives sharing the encoder for a
  given dataset. Those counts, and a compute budget of "1 or 2 Nvidia Tesla V100 GPUs for anywhere
  from a few minutes to 7h", were carded as absences until the audit; they make this the strand's
  smallest measured encoder by a wide margin.

The map of the space, rather than an instance of it:

- [guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md)
  — 81 surveyed articles, of which 13 self-supervised with ten from 2022 onward, plus a taxonomy of
  the *reasons* for wanting an embedding (transfer, robustness, algorithmic bridge, structure
  discovery). The autoencoder count is not quotable as a single number: the card records three
  values from the same paper — 31 in the abstract, 34 in Section 2, "approximately half" of 81 in
  the discussion — and adopts none. Any figure this document might have used would have been one
  arm of a self-contradicting source (§6.2).

### 2.2 The raw-signal reconstruction problem, and three responses to it

This is the strand's clearest objective-level relation, and it is a measured finding rather than a
convention.

- The measurement:
  [banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md)
  ran a plain autoencoder against three temporal-context objectives on the same encoder. It "never
  exceeded 53.0%" on TUH Abnormal against a 50 percent chance level, and the authors' explanation is
  mechanistic: mean-squared-error reconstruction is dominated by low frequencies, which carry the
  largest amplitudes under EEG's 1/f power law and the least neurobiological information.
- Response one, change the target to a spectral quantity:
  [labram-2024](../collection/eeg-models/labram-2024/card.md) states plainly that "the loss fails to
  converge while directly reconstructing raw EEG signals", and routes around it by making the
  tokenizer's decoder reconstruct Fourier amplitude and phase.
- Response two, change the target to a learned representation:
  [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) argues that reconstructing raw EEG
  optimizes toward a low-SNR target and adds a momentum-encoder alignment loss. Its ablation supports
  the argument in a specific and unusual way — removing the alignment loss costs 6 to 9 percent
  downstream while barely changing the reconstruction loss, and removing layer normalization on the
  reconstruction targets *lowers* the pretraining loss while costing 1 to 7 percent downstream.
- Response three, keep the raw target anyway:
  [reve-2025](../collection/eeg-models/reve-2025/card.md) (L1) and
  [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) (MSE) reconstruct the raw signal
  directly and both report a positive pretraining ablation on the same task, +10.7 and +2.2 points
  respectively on PhysioNet-MI.

The corpus does not reconcile these. Nothing in it isolates the loss function while holding masking
scheme, corpus and architecture fixed, so the relation between the four positions is recorded here
as unresolved rather than as a progression.

### 2.3 Pretraining scale, and why "hours" is not a comparable unit across this strand

Reported hours, each as its own card states it:

- [reve-2025](../collection/eeg-models/reve-2025/card.md) — 61,415 h, 92 datasets, 24,274 subjects.
  The card flags that this is a corpus size and not a curation claim: the authors name removing
  low-quality recordings as future work.
- [brainwave](../collection/eeg-models/brainwave/card.md) — 40,907 h, 15,997 individuals, EEG and
  intracranial EEG in roughly balanced patch counts.
- [luna-2025](../collection/eeg-models/luna-2025/card.md) — 21,928.32 h summing its own Table 11
  (TUEG 21,787.32 plus Siena 141.0).
- [femba-2025](../collection/eeg-models/femba-2025/card.md) — "over 21,000 hours" of TUEG.
- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — "longer than 9000 hours" retained
  from a 27,062-hour corpus. The retained figure is never given exactly while the corpus figure it
  derives from is, so the retained fraction cannot be computed from the paper.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — 2,653 h (1,997 EEG plus 656
  MEG), with the paper stating its own scale limit.
- [labram-2024](../collection/eeg-models/labram-2024/card.md) — 2534.78 h from about 20 datasets.
  The exact figure is in Appendix D; "over 2,500 hours" is the body's rounding of it. Both are the
  same measurement, which matters downstream because a third party's tabulation of 2,535 h is a
  rounding of the primary rather than a competing figure.

Four entries never report hours at all, and the cards say so rather than computing a substitute:
[bendr-2021](../collection/eeg-models/bendr-2021/card.md) (corpus given in terabytes and subjects;
the string "hour" does not occur), [biot-2023](../collection/eeg-models/biot-2023/card.md) (sample
counts and per-sample durations given, total never stated),
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) (five datasets, 279 subjects), and
[banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md)
(recordings and windows only). The Banville entry is half-reconstructible rather than wholly
unreconstructible, which is a correction to an earlier version of this line: PC18's 891,668
non-overlapping 30 s windows come to about 7,430 h, while TUH Abnormal genuinely resists it because
each recording is cropped to at most 20 minutes. Neither figure is stated by the paper, so neither
enters the list above.

One entry has zero by design:
[eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) declines pretraining, and
the card records the reason in the authors' words — "pre-training is not used in EEG Conformer, due
to the limited data for calibration".

One entry proposes a replacement unit:
[kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)
introduces *channel-hours*, recording duration multiplied by channel count, to make scalp and
intracranial corpora comparable — and the card records both that it could not be determined for
some of the ten reviewed models, and that the unit conflates a long single-channel recording with a
short high-density one and is never tested against any outcome.

### 2.4 Most of the strand was pretrained on one corpus

TUEG, the Temple University Hospital EEG corpus, is the pretraining substrate for
[bendr-2021](../collection/eeg-models/bendr-2021/card.md),
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
[femba-2025](../collection/eeg-models/femba-2025/card.md), and
[luna-2025](../collection/eeg-models/luna-2025/card.md) — the last at 99.4 percent of its hours. TUH
data also dominates [labram-2024](../collection/eeg-models/labram-2024/card.md) and contributes
26,847 of [reve-2025](../collection/eeg-models/reve-2025/card.md)'s 61,415 hours.
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) is the explicit exception: TUEG is
not among its 22 sources, and its largest EEG contributions are developmental and resting-state
cohorts.

The structural consequence, stated by the cards themselves rather than inferred: evaluation tends to
land back inside the pretraining distribution. All three of
[femba-2025](../collection/eeg-models/femba-2025/card.md)'s downstream tasks are Temple University
subsets of its own pretraining corpus with only subject overlap removed; three of four for
[luna-2025](../collection/eeg-models/luna-2025/card.md); and both headline results of
[labram-2024](../collection/eeg-models/labram-2024/card.md) are Temple University corpora, which
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) states
directly as "TUAB is in-domain".
[kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)
generalises the observation over its own review set: in four of ten reviewed studies the downstream
evaluation datasets were already used for pretraining.

### 2.5 Scale is not the variable that orders the corpus

Six independent observations, from six cards, each measured rather than asserted. They agree in
direction, so they are listed as six observations of one regularity and not as six pieces of
evidence:

- [labram-2024](../collection/eeg-models/labram-2024/card.md) — its Base model trained on 500 hours
  exceeds the same model trained on 2,500 hours on TUAB; the authors conclude "2,500 hours is not
  the answer".
- [femba-2025](../collection/eeg-models/femba-2025/card.md) — Base (47.7M) to Huge (386M) is eight
  times the parameters for 0.77 points of TUAB balanced accuracy, and Tiny beats both larger
  variants under two of the four TUAR protocols.
- [luna-2025](../collection/eeg-models/luna-2025/card.md) — Base to Huge is 44 times the parameters
  for 0.94 points on TUAB, and on SEED-V the Large model beats the Huge one on all three metrics.
- [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) — accuracy rises monotonically across
  eight sizes with one inversion, the 76M variant falling below the 25M one, from which the card
  reads that summary-token count and depth matter more than raw size at that scale.
- [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) — "parameter
  count alone does not order the models", resting on BENDR being the largest in its panel and not
  the best. (That parameter figure is itself contested; see §6.1.)
- [kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md) —
  across ten models, "the evidence for data scaling is weak, if any", NeuroLM's TUAB and TUEV
  performance was not sensitive to model size, and its HMC and Workload performance *decreased* with
  larger variants.

Two entries sit on the other side and are recorded as such:
[reve-2025](../collection/eeg-models/reve-2025/card.md) reports that performance improves with model
size, while noting no scaling law is fitted and only a qualitative trend shown; and
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) reports its tiny model beating its
base model on MDD (0.886 against 0.877).

### 2.6 Descent and shared code

The strand is not a set of independent efforts. Four relations, each recorded on the cards:

- A tokenization-and-baseline lineage:
  [biot-2023](../collection/eeg-models/biot-2023/card.md) → [labram-2024](../collection/eeg-models/labram-2024/card.md)
  (adopts BIOT's patch segmentation, evaluation splits and baseline numbers) →
  [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) (adopts LaBraM's 100 µV
  normalization convention, treats it as strongest pretrained baseline) →
  [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) (builds its stage-2 model from
  CBraMod's Criss-Cross Transformer block and extends LaBraM's vector-quantised lineage).
- A positioning-against relation:
  [reve-2025](../collection/eeg-models/reve-2025/card.md) argues directly against
  [labram-2024](../collection/eeg-models/labram-2024/card.md)'s learned spatial embedding, and
  [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) positions itself against
  [bendr-2021](../collection/eeg-models/bendr-2021/card.md) by declining to pretrain.
- A same-laboratory pair: [femba-2025](../collection/eeg-models/femba-2025/card.md) and
  [luna-2025](../collection/eeg-models/luna-2025/card.md) share a code base
  (`pulp-bio/biofoundation`), and LUNA reuses FEMBA's TUAB and TUAR baseline tables and reports
  beating FEMBA on TUAR and TUSL.
- A cross-modality precedent: [brainwave](../collection/eeg-models/brainwave/card.md) (EEG plus
  intracranial EEG) is cited by [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)
  (EEG plus MEG) as the closest precedent for training one model across two recording modalities,
  and both report a joint-pretraining ablation beating either single-modality variant.

One consequence of the lineage matters for reading §3: baseline numbers are copied along it. See
§3.7.

---

## 3. Evidence: who measured it, under which protocol, against what

### 3.1 First-party evaluation, on benchmarks the authors chose

Eleven entries report evidence about their own model:
[reve-2025](../collection/eeg-models/reve-2025/card.md),
[labram-2024](../collection/eeg-models/labram-2024/card.md),
[brainwave](../collection/eeg-models/brainwave/card.md),
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
[bendr-2021](../collection/eeg-models/bendr-2021/card.md),
[biot-2023](../collection/eeg-models/biot-2023/card.md),
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md),
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md),
[luna-2025](../collection/eeg-models/luna-2025/card.md),
[femba-2025](../collection/eeg-models/femba-2025/card.md),
[eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md).

[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)'s card states the general
separation most explicitly, and it applies to this whole node: the paper's evidence is "self-run on
a chosen benchmark set under full fine-tuning with a two-layer MLP head" while a suite's is
"third-party, under a frozen backbone with a linear head, on datasets the authors did not choose",
and "neither substitutes for the other".

### 3.2 Third-party re-runs

Five entries measure someone else's checkpoint. This is where the strand's like-for-like comparisons
live.

- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — four released
  checkpoints (BIOT, EEGPT, LaBraM, CBraMod) against four supervised architectures (EEGNet, LDMA,
  ST-Transformer, Conformer) on 13 datasets under one adaptation pipeline and three transfer
  regimes, plus four ablations. Its pipeline is released under an MIT licence, which its card records
  as the only licence stated for any released artefact anywhere in the strand — and that licence
  covers the benchmark's own pipeline code, not a checkpoint. Every model paper that releases weights
  states no licence for them, and each card records the omission individually:
  [labram-2024](../collection/eeg-models/labram-2024/card.md),
  [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
  [biot-2023](../collection/eeg-models/biot-2023/card.md),
  [bendr-2021](../collection/eeg-models/bendr-2021/card.md),
  [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md),
  [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md); while
  [femba-2025](../collection/eeg-models/femba-2025/card.md) releases code without saying whether the
  weights are released at all, and [luna-2025](../collection/eeg-models/luna-2025/card.md)'s NeurIPS
  checklist says weights "will be released upon publication" and that "we do not release any new
  assets yet".
- [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) — two
  checkpoints in three configurations (LaBraM, NeuroGPT full and encoder-only) against EEGNet and
  EEG-Inception on five tasks under an identical protocol, with paired t-tests.
- [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) — three
  checkpoints (LaBraM, CBraMod, REVE) across four datasets, 12 model-by-dataset pairs, under one
  fixed input contract, with a five-diagnostic frozen-representation protocol.
- [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) — six
  checkpoints on five clinical tasks under frozen linear probing, plus a targeted negative-control
  battery (random initialisation, random features, label permutation, scrambled-label fine-tuning,
  projection-method sensitivity) applied to REVE only.
- [sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md) —
  one checkpoint (LaBraM) under partial fine-tuning and LoRA against DeepConvNet on one 54-subject
  dataset.

### 3.3 No experiment of their own

- [kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md) —
  every number is taken from the reviewed papers; the card records that no reproduction is attempted
  and the review inherits any error in them.
- [guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md)
  — no results table exists in it at all; its quantitative content is bibliometric.
- [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md) —
  runs experiments but on no pretrained model. It is the methodological control for §3.6, not
  transfer evidence.

### 3.4 The adaptation protocol axis

The single property that most changes how a number should be read. Four regimes appear.

Frozen-backbone evidence only:

- [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) — linear probing is the only evaluation
  reported. The authors justify it as avoiding "the overfitting problem when a large parameter model
  is fine-tuned using a limited number of samples", and argue that because the trainable module is
  so simple, "the performance is solely determined by the encoder". The card records the flip side:
  there is no fine-tuned EEGPT number anywhere, so the paper cannot say how much of the gap to
  fine-tuned baselines is attributable to the frozen protocol.

Fine-tuning evidence only, no frozen number reported:

- [luna-2025](../collection/eeg-models/luna-2025/card.md) — no linear-probing or frozen-backbone
  result is reported.
- [femba-2025](../collection/eeg-models/femba-2025/card.md) — likewise, none anywhere in the paper.
- [sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md) —
  neither a frozen probe nor a full fine-tune appears in the condition list; it compares a CNN,
  partial fine-tuning and LoRA.

Both measured:

- [reve-2025](../collection/eeg-models/reve-2025/card.md),
  [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
  [bendr-2021](../collection/eeg-models/bendr-2021/card.md),
  [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md),
  [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md),
  [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md),
  [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md),
  [banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md),
  [labram-2024](../collection/eeg-models/labram-2024/card.md).

**LaBraM's placement changed after this document was drafted, and the change is structural rather
than numeric.** An earlier version of this node placed
[labram-2024](../collection/eeg-models/labram-2024/card.md) under "fine-tuning evidence only", on
the card's statement that whether the frozen representations are useful "is not tested in the paper
at all". The card was corrected: Appendix K, Table 10 reports five adaptation regimes on both
headline datasets, including a linear probe. Balanced accuracy, TUAB then TUEV, in the table's own
row labels — All 0.8140 / 0.6409; Transformer(12) 0.8141 / 0.6541; Transformer(8) 0.8134 / 0.6611;
Transformer(4) 0.8074 / 0.6188; Linear Probe 0.7954 / 0.3461. Two consequences for this node.
First, the strand's most-cited checkpoint does have a first-party frozen number, so the third-party
probes of §3.5 corroborate a measurement rather than fill an absence. Second, the entry that most
nearly counted as "reports only one regime" no longer does, which leaves LUNA, FEMBA and SIRCA as
the whole of the fine-tuning-only category.

One caution that keeps this node honest: "frozen" is not one protocol.
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)'s frozen table uses the same
two-layer MLP head as everywhere else, so its "freeze" is not a linear probe, and the card says so.
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) leaves pooling to
each backbone's release default rather than re-pooling.

Partial and parameter-efficient adaptation as a third position between the two:

- [labram-2024](../collection/eeg-models/labram-2024/card.md) — the same Appendix K table. Partial
  fine-tuning of the last eight transformer blocks gives 0.6611 on TUEV, the best value anywhere in
  the table and above full fine-tuning's 0.6409, while the last four blocks fall back to 0.6188.
  This is first-party evidence that the best adaptation depth is interior rather than at either
  end, and it is the only such measurement in the strand.
- [reve-2025](../collection/eeg-models/reve-2025/card.md) — a two-stage recipe, frozen-backbone
  linear probe then unfreeze as one continuous run, with LoRA on the QKVO projections.
- [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) — LoRA at
  ranks 1 to 16 across module combinations, reducing trainable parameters by one to two orders of
  magnitude without loss, and concluding that "the attention layers might not capture as important
  information as their temporal encoding parts".
- [sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md) —
  LoRA against partial fine-tuning on the same checkpoint: two orders of magnitude fewer trainable
  parameters and 35 percent less training time per epoch, with partial fine-tuning described as
  unstable.

### 3.5 The protocol reorders the models — the corpus demonstrates this rather than asserting it

Read in one direction, freezing collapses most checkpoints:

- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — PhysioNet-MI falls from 0.6417 to
  0.3845 and FACED from 0.5509 to 0.3146 with the backbone fixed, and the authors conclude the model
  "cannot currently serve as a fixed-parameter feature extractor like CLIP and SAM".
- [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) — frozen
  means of 0.635, 0.647 and 0.663 against 0.731 and 0.733 for the fully trained small baselines,
  which the authors summarize as lagging "by a large margin of almost 8-10%"; frozen LaBraM reaches
  0.297 on motor imagery.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — freezing costs 14.2 points on
  TUEV and 5.7 on AD65 but only 1.0 on TUAB, so the cost of freezing is itself task-dependent.
- [labram-2024](../collection/eeg-models/labram-2024/card.md) — the same task dependence, first
  party and much sharper: linear probing costs 1.9 balanced-accuracy points on TUAB (0.8140 →
  0.7954) and 29.5 on TUEV (0.6409 → 0.3461), which the authors describe as "much worse than other
  settings". This is the largest freezing cost recorded anywhere in the strand, and it sits on the
  checkpoint the rest of the corpus uses as its reference point (§3.7).
- [bendr-2021](../collection/eeg-models/bendr-2021/card.md) — the two frozen configurations "often
  stayed marginally above chance".
- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — "linear evaluation
  consistently yields lower performance across most datasets", CBraMod on BCI-IV-2A falling from
  47.71 to 32.32.
- [kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md) —
  five of ten reviewed models reported linear probing at all, and those results "were relatively
  worse", which the review reads as casting "doubt on the quality of the representations learned via
  self-supervision in EEG-FMs". This is a tendency with named exceptions rather than a uniform
  result, and the card was corrected to say so: of the five, Neuro-GPT is the clear negative case,
  while BrainBERT's linear probe reached AUROC "similar to those of the fully supervised models" and
  both fine-tuned and linear-probed Brant "outperformed other supervised and EEG-FM baselines" on
  seizure and pathology detection. Two of five going the other way is a weaker premise than the
  review's headline reads as, and this list is where the difference lands.

Read in the other direction, fine-tuning buys little over a probe, and the ordering flips:

- [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) — across 12
  model-by-dataset pairs, full fine-tuning beats the frozen linear probe in only 2, and 10 fall
  within one percentage point of the corresponding probe.
- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — EEGPT reaches 25.81
  balanced accuracy on 4-class BCI-IV-2A under full fine-tuning, where chance is 25, and 47.89 under
  linear probing on the same checkpoint. The benchmark changed protocol per model as a result,
  reporting linear probing for EEGPT and full fine-tuning for the other three.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — on AD65 the frozen
  BrainOmni_base (0.771) exceeds fully fine-tuned LaBraM (0.711) and CBraMod (0.681), so freezing one
  model can beat fine-tuning another.
- [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) — the cleanest statement of
  the reordering, because it holds the reference point fixed: on 54 datasets, seven of ten foundation
  models beat EEGConformer under full fine-tuning (average rank 7.25), while only five of ten beat it
  under the same suite's frozen linear-probing protocol (average rank 6.66).
- [reve-2025](../collection/eeg-models/reve-2025/card.md) — under linear probing on PhysioNet-MI,
  REVE-Base reaches 0.5371 against CBraMod 0.3845, LaBraM 0.3715 and BIOT 0.3698, and across ten
  tasks REVE-Large averages 0.654 against CBraMod's 0.501 — a much wider separation than the
  fine-tuned tables show.

These two readings are not contradictory but they are not the same claim, and an entry that reports
only one regime (§3.4) cannot be placed on both. That is the reason this axis is a node rather than
a remark.

### 3.6 Split geometry

The yardstick, and the only entry in the strand that measures the effect directly:

- [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md) — the
  same CNN on the same Alzheimer's EEG scores 99.8 percent under segment-based holdout and 53.0
  percent under subject-based holdout, an inflation of 46.8 points; on a within-subject seizure task
  79.1 against 65.1, an inflation of 14.0 points. Of 63 surveyed deep-learning EEG studies, only 17
  unambiguously avoided the flawed design. The mechanism is that "segments of EEG from one subject
  are more similar to each other than to segments from different subjects". The card also names the
  limit of the vocabulary: subject versus segment only, with session-level leakage unexamined.

Entries whose headline numbers rest on a sample-level or within-subject split, by their own
description:

- [luna-2025](../collection/eeg-models/luna-2025/card.md) — TUAR and TUSL under "an 80%/10%/10%
  randomized sample-level split", with the authors stating that subject-independent splits are the
  gold standard and recommending them for future work; SEED-V split within subject.
- [femba-2025](../collection/eeg-models/femba-2025/card.md) — TUAR and TUSL under an 80/10/10
  randomized split described at sample level with no statement that it is subject-wise; two of its
  three headline tasks.
- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — subject-wise for FACED,
  PhysioNet-MI and SHU-MI but trial-wise for SEED-V, where the same subject appears in train,
  validation and test. The paper does not flag the difference.
- [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) — subject-dependent
  throughout by design, and the card names the consequence: three benchmark suites deploy it as a
  cross-subject baseline, which is not the setting its own numbers were obtained in.

Entries with subject-wise splits stated:
[lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) (10-fold
subject-independent, explicitly constructed so no participant appears in both sides),
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)
(subject-stratified group 5-fold),
[sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md)
(leave-one-subject-out over 54 subjects),
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) (strict cross-subject 5-fold),
[bendr-2021](../collection/eeg-models/bendr-2021/card.md) (leave-one- or leave-multiple-subjects-out),
[biot-2023](../collection/eeg-models/biot-2023/card.md) (CHB-MIT by patient, other datasets described
only in an appendix), and
[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) (cross-subject as a
defined regime, alongside a multi-subject one it proposes as "a natural upper bound").

Entries where the split is inherited or record-level rather than established:

- [reve-2025](../collection/eeg-models/reve-2025/card.md) — reuses the splits of CBraMod, LaBraM and
  BIOT and does not state per-dataset whether they are subject-wise, so the cross-subject claim rests
  on protocols defined elsewhere.
- [labram-2024](../collection/eeg-models/labram-2024/card.md) — follows BIOT exactly; subject-wise on
  the train/validation boundary.
- [banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md)
  — record-wise, which equals subject-wise on PC18 (994 recordings from 994 individuals) but not on
  TUH Abnormal (2,993 recordings from 2,329 patients), where validation-set leakage is real and
  undiscussed.
- [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) — CAUEEG
  primary cross-validation is recording-level because public patient identifiers are unavailable; the
  patient-disjoint split is offered as a sensitivity bound only.

And one measured instance of the yardstick applied to a published foundation-model number:
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) records a 45-point
reproduction gap, where a prior evaluation reporting 0.9047 balanced accuracy under a fixed 80/10/10
split with the same subjects in different folds falls to 0.43–0.50 under subject-disjoint
cross-validation.

### 3.7 What the baseline was, and whether it was re-run

The comparator determines what a transfer number means, and the corpus varies on three levels.

No supervised baseline at all:

- [brainwave](../collection/eeg-models/brainwave/card.md) — every comparator is another pretrained
  model (LaBraM, BrainBERT, MOMENT). The card is explicit that the source text contains no occurrence
  of EEGNet, ShallowConvNet, SPaRCNet, BIOT, "from scratch", or the word "baseline", so every headline
  number establishes only that BrainWave is the best of four pretrained models on these tasks.

Baselines quoted from another paper rather than re-run:

- [labram-2024](../collection/eeg-models/labram-2024/card.md) — all baselines taken from BIOT, so the
  comparisons inherit BIOT's preprocessing and tuning for the baselines while LaBraM gets the authors'
  own.
- [reve-2025](../collection/eeg-models/reve-2025/card.md) — every comparison is to numbers "displayed
  in existing studies" except CBraMod under linear probing, which was reproduced; the linear-probing
  table is therefore the paper's only baseline comparison under the authors' own control.
- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — baseline parameter counts taken
  from LaBraM rather than recomputed.
- [femba-2025](../collection/eeg-models/femba-2025/card.md) and
  [luna-2025](../collection/eeg-models/luna-2025/card.md) — share tables between them.

This means a chain of copied baseline numbers runs along the descent relation of §2.6, which is why
§6.1's ST-Transformer disagreement splits exactly along that chain rather than randomly.
[guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md)
names the general hazard: "there is always a concern that authors applying a method as a baseline
may not be using it to its fullest potential", and the card marks that caution as applying to every
transfer number in this strand.

A related note on weighting. LaBraM is the comparator in
[reve-2025](../collection/eeg-models/reve-2025/card.md),
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md),
[brainwave](../collection/eeg-models/brainwave/card.md),
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md),
[luna-2025](../collection/eeg-models/luna-2025/card.md),
[femba-2025](../collection/eeg-models/femba-2025/card.md),
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md),
[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md),
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md),
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md),
[lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) and
[sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md).
That is a fact about the corpus's comparator graph — LaBraM is the default reference point — and it
is not evidence about LaBraM's quality. Several of those twelve mentions are the same quoted number
travelling along the chain above rather than twelve measurements.

---

## 4. Negative and null results, positioned against the positive ones

The negatives in this strand are not a separate literature; they are the same measurements read at a
different operating point. This node places them against the positives rather than listing them
apart, because the regularity that connects the two — §4.1 — is what makes each individually
interpretable.

### 4.1 The positive results, and the regularity in their shape

Within-paper pretraining ablations, where the same architecture is measured with and without
pretraining, which is the cleanest form of positive evidence in the corpus:

- [reve-2025](../collection/eeg-models/reve-2025/card.md) — 0.6480 against 0.5409 on PhysioNet-MI,
  a +10.7 point gain attributable to pretraining rather than architecture.
- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — the same ablation on itself, 0.6417
  against 0.6196, a +2.2 point gain, with the remaining margin over EEGNet attributed to architecture.
- [biot-2023](../collection/eeg-models/biot-2023/card.md) — the architecture worth about 2.5 points
  over the best supervised comparator on CHB-MIT and pretraining a further 4.3 points on top of the
  same architecture.
- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — third-party and
  across 13 datasets: LaBraM and CBraMod with pretraining beat their non-pretrained counterparts "by
  over 10% and 7% in average", with gains "more pronounced on datasets with limited scale of training
  data". Its transfer scores, averaged across few-shot ratios, are CBraMod 0.2761, LaBraM 0.1773,
  EEGPT 0.0789 and BIOT −0.0573, the last driven by a single ratio.

The regularity: **the size of the advantage is a property of the task, not of the checkpoint**, and
it swings by an order of magnitude inside single papers' own tables.

- [labram-2024](../collection/eeg-models/labram-2024/card.md) — +20.3 points over the best
  non-pretrained model on TUEV, +1.7 points over ST-Transformer on TUAB.
- [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) — an 18.5-point margin on TUEV and a
  0.17-point margin on TUAB, well inside the standard deviations.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — 23.0 points on TUEV, 1.4 points
  on MDD, and second place to CBraMod on PhysioNet-MI.

Two entries explain the regularity in the same terms.
[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) attributes the
small-margin cases to the downstream datasets being large enough that supervised learning suffices.
[banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md)
measured that as a curve rather than asserting it: the self-supervised advantage over full
supervision is 22.8 points at one label per class, shrinks monotonically, and inverts above roughly
10,000 examples per class, after which full supervision leads by 1.6 to 3.5 percent.

### 4.2 A small supervised or classical model matches or beats the checkpoint

Six entries, of which four are third-party.

- [sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md) —
  DeepConvNet achieved the highest overall accuracy across all calibration sizes against both
  partially fine-tuned and LoRA-adapted LaBraM, leave-one-subject-out on 54 subjects. The sign and
  the comparator are on record; the magnitude is behind a paywall (§5.3).
- [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) — the best
  fine-tuned foundation model averages 0.745 against EEGNet's 0.731 at 2,394 trainable parameters, a
  1.4-point margin at roughly 300 times the parameter count, and LaBraM's advantage over
  EEG-Inception is statistically significant on exactly one of five tasks. The 0.745 belongs to
  NeuroGPT encoder-only at 717,958 trainable parameters, and naming the model matters here because
  the card's own headline had priced the same 1.4-point gain against LaBraM and the full NeuroGPT
  (5.85M to 78.5M), a ratio of roughly 33,000×; the audit corrected it to the ~300× carried above.
  Those two larger models score *below* the 0.745, at 0.742 and 0.736, so within this comparison
  more parameters did not buy more accuracy.
- [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) — on EEGMAT, a
  classical handcrafted-feature logistic regression reaches 0.847 balanced accuracy against the best
  foundation-model tier at 0.755 and EEGNet from scratch at 0.671.
- [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) — on CAUEEG,
  classical features reach 0.769 AUROC against frozen REVE's 0.568, and classical features beat frozen
  REVE by at least 12.7 points under every tested condition; no foundation model beats classical
  features on the 2-channel Sleep-EDF task.
- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — on clinical monitoring
  tasks foundation models perform "comparable or even worse than traditional models": EEGNet's 72.29
  beats every foundation model on Siena and Conformer's 73.84 does so on HMC, and in the
  macro-average two of the four checkpoints (BIOT 58.42, EEGPT 55.00) are level with or below the
  best supervised model (Conformer 58.12).
- [bendr-2021](../collection/eeg-models/bendr-2021/card.md) — the strand's earliest instance, and
  first-party: on its largest downstream dataset, fine-tuning the pretrained model is "mostly on par
  with the fully supervised counterpart", which the authors attribute to there being enough labelled
  data for supervised learning to work.

The one entry that supplies the supervised reference point rather than a negative result is
[eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md), which reaches a reported
78.66 percent on BCI Competition IV 2a against a reported 74.50 percent for EEGNet, with no
pretraining at all. **Both figures are now marked unverified on the card and the hedge belongs
here.** All four of the paper's tables came through as captions with empty bodies, and the bodies
are not in the PDF's text layer either, so thirteen carded numbers cannot be audited from the
repository. Dataset II's triple is corroborated by prose margins ("improvements of 5.25% and 4.15%
for ConvNet (p < 0.05) and EEGNet (p < 0.01)"); Dataset III's has no prose margin at all and must
not be propagated; and Dataset I — the row quoted here — has only a margin against FBCSP, "our
Conformer significantly improves the accuracy by 10.91% over FBCSP (p < 0.01)", which says nothing
about the EEGNet value. What survives independently of the tables is the paper's *other* claim of
the same shape, on Dataset II: +4.15 points over EEGNet at p < 0.01. The reference point therefore
still exists, but it should be quoted from Dataset II rather than from the 2a row above, and the
two 2a accuracies are provisional pending re-obtaining the tables.

### 4.3 The model can score by recognising identity rather than by decoding the task

Two entries, arguing the same shape of failure at two different levels of identity. They are
independent — different authors, different checkpoints, different cohorts — so they are two claims,
not one repeated.

- [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) — *subject*
  identity. Frozen embeddings of LaBraM, CBraMod and REVE are dominated by subject identity at 13 to
  89 times a random-Gaussian null in 12 of 12 pairs, and that dominance rises under fine-tuning in
  all 12 by 10 to 63 percentage points. The axis is linearly removable: closed-form LEACE erasure
  drives a subject probe to chance in all 12 pairs, and where the label varies within subject,
  erasing identity *improves* label decoding by 6 to 12 points. The carrier is model-specific —
  removing the aperiodic 1/f component drops the subject probe by 9 to 19 points for LaBraM and
  CBraMod but shifts REVE's by at most 1.2 points, REVE's already sitting at or above 0.93.
- [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) — *dataset*
  identity. A linear probe separates dataset pairs from frozen REVE embeddings at AUROC 1.000,
  holding after projection to the top 50 principal components and at 0.9998 under a band-limited
  replication, while the same PCA-50 pipeline decodes the 3-way diagnosis at 0.528. Separately, a
  randomly-initialised encoder of the same architecture outperforms pretrained REVE on that task,
  0.659 against 0.570.

Both cards bound their own claims, and the bounds belong here.
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) states that
the identity probes confound site with hardware, preprocessing, population, diagnosis composition
and dataset history, establishing decodable dataset membership "and nothing more".
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) states that its
three-model panel differs along five design axes at once, so no cross-model contrast can be
attributed to any single axis, and that it has one dataset per cell of its 2×2 layout.

The upstream mechanism is the same one measured in §3.6:
[brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
established for supervised training that segments from one subject resemble each other more than
segments from different subjects, and its card records that
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) is the later work
extending that argument from supervised training to frozen foundation-model embeddings. Brookshire's
own card notes it makes no claim about frozen pretrained embeddings, so the extension is Lin's
result, not Brookshire's.

### 4.4 The measurement itself is unsound

- [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md) —
  split geometry, quantified (§3.6).
- [kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md) —
  rankability and in-distribution evaluation: of ten EEG foundation models, four were evaluated on
  data that was also in their pretraining corpora, only two performed out-of-distribution evaluation
  on unseen datasets, and "even when considering the TUAB and TUEV tasks, only four out of the ten
  EEG-FMs can be ranked". It also records that TUAB "may already have saturated (85-87% accuracy)
  with traditional approaches", which sets a ceiling on what a result there can show. Its own card
  notes the reflexive limit: most of the review's negative conclusions are about *reporting* rather
  than capability, and whether EEG foundation models actually fail to transfer, as opposed to not
  having been measured properly, is left open.
- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — a benchmark whose own
  card records that no statistical testing is reported anywhere in it: no confidence intervals, no
  repeated runs, no significance tests, with several conclusions resting on macro-average differences
  of a few points across 13 heterogeneous datasets and metrics. Its transfer score is defined as
  relative improvement over a from-scratch counterpart, so a model with a weak from-scratch baseline
  scores well for reasons unrelated to representation quality, and the metric is not validated
  against anything.

### 4.5 One controlled positive inside the negative literature

The negatives are conditional and the corpus contains the condition.
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md), the entry
whose whole design is a negative-control battery, reports one clean positive: on CHB-MIT
cross-subject ictal detection over the full 23-patient cohort with held-out patients, pretrained
REVE reaches 0.793 AUROC against 0.701 for a randomly-initialised encoder of the same architecture,
0.505 for random features and 0.500 under label permutation, stable to a ±30 s guard band and to
drawing negatives from separate seizure-free recordings. The author attributes the cleanliness to
positives and negatives sharing recording sessions, which reduces session-level confounding — which
is to say the same session structure that produces the failure in §4.3 produces the clean result
here when it falls on both sides of the label.

---

## 5. What must not be read as transfer evidence

### 5.1 The theory line, capped at two by the brief

Both entries are motivation for applying sequence models to neural time series. Neither establishes
that a checkpoint transfers, and both cards say so in their own words. The brief caps this line at
two entries and both cards record that the cap is reached, so the line cannot be extended without
reopening the scoping decision.

- [muller-2024-transformers-cortical-waves](../collection/eeg-models/muller-2024-transformers-cortical-waves/card.md)
  — an opinion piece with no model, no dataset, no baseline and no evaluation of its own. Its card
  states outright that "a direction paper that cites it as evidence that EEG foundation models work
  would be making an argument the source does not make". Two further limits are on record: the
  mechanism operates over a topographic map resolved by arrays and optical imaging, and the article
  itself says of non-invasive recording that "signal blurring poses a significant challenge to
  quantifying spatiotemporal dynamics"; and the mechanistic link the authors actually derive runs
  through Toeplitz and circulant state-space matrices, not through attention, with the transformer
  comparison in the title being the looser framing.
- [alexander-2019-cortical-waves](../collection/eeg-models/alexander-2019-cortical-waves/card.md) —
  an empirical study, not a theory paper, carded on the motivation line by a scoping decision the
  card records. What it establishes is narrow: future phase at one site is predicted better from the
  whole-array wave pattern than from that site's own past, at PLV-error 0.73 in the best subject and
  0.32 in the worst *over all trials*. The condition matters and was missing from an earlier version
  of this bullet: the paper's tabulated headline (Table 1) is the power-selected condition, top 25
  percent of trials by past mean log power, where the range is 0.94 to 0.51 with a subject-wise mean
  of 0.72. Selecting trials by power, like selecting the best site, is a convention the paper adopts
  from the prior literature it compares against. Three limits bound the result. Its data contains no
  EEG at all — MEG and ECoG only — so nothing in it establishes that the structure survives volume
  conduction and scalp blurring. Only the single best-predicted site per subject is reported. And
  the margin over the temporal-only baseline cannot be quoted here — but for a different reason
  than this document first gave. It is not unmeasured: the paper runs a mixed linear model over all
  trials and reports the coefficients and standard errors in S1 Table, concluding that the temporal
  Fourier model "performed less well" while the large-scale model and a third comparator, the local
  event-related model, "did not differ in mean performance". S1 Table is supplementary and outside
  the carded source, so the effect size is inaccessible rather than absent — the same distinction
  §5.3 draws for a different entry, and it changes what a later reader should do from "the paper did
  not measure this" to "re-obtain the supplement".

This is also the one entry in the strand whose subject matter falls outside the strand's own
inclusion criterion, which the brief defines as work that pretrains an EEG model, evaluates one, or
critiques that practice. It is present by explicit scoping decision recorded in
`_briefs/strand-eeg-models.md` and repeated on the card, not by the inclusion rule.

### 5.2 Reviews whose every number is second-hand

Distinct from §5.1 in that these entries are *about* transfer evidence, but they report none of
their own, so a number quoted through them inherits its source's errors.

- [kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md) — no
  reproduction is attempted; the review's own card records that it inherits any error in the papers
  it reviews, that its comparative figures place numbers from different papers on shared axes while
  stating the tasks and metrics differ, and that its set of ten does not include CBraMod, EEGPT or
  REVE.
- [guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md)
  — a survey with no experiments and no results table, whose quantitative content is bibliometric.
  Its headline finding that no EEG foundation model has been adopted by the BCI community is, as its
  card records, a statement about the field before LaBraM, CBraMod, EEGPT and REVE existed; the card
  instructs that it be cited for its taxonomy and methodological cautions, not for that verdict. The
  cutoff is now on record and dates the verdict precisely — "This search was conducted on April
  1<sup>st</sup> 2024", over articles published after 2014, with a full stage-by-stage selection flow
  and a figure summarizing it. What the review does lack is an inter-rater statistic, and 25 of its
  81 articles were added by author judgement outside the search protocol, which is the reproducibility
  limit that actually applies.

### 5.3 One entry whose decisive number is inaccessible rather than unreported

- [sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md) —
  carded from the publisher abstract and bibliographic record only, the full text being paywalled
  with no open copy. The card makes the distinction explicit and it should be preserved downstream:
  the baseline (DeepConvNet), the protocol (leave-one-subject-out, 54 subjects) and the sign
  (baseline higher at every calibration size) are on record; the magnitude is not, because it is
  inaccessible, not because the paper omitted it. The card states the consequence directly — a claim
  that a supervised CNN beat LaBraM on motor imagery is supportable from it, a claim about how much
  is not.

---

## 6. Where the corpus disagrees with itself

A register. Nothing here is resolved, because resolving it would require the sources, and in three
cases the sources contradict themselves so there is nothing to resolve to.

### 6.1 Disagreements about the same quantity across different cards

**BENDR's parameter count — four values, none of them from BENDR's own paper.**

| value | card |
|---|---|
| no headline figure; "over one billion parameters" trained in configuration 1 (full fine-tune of convolutional stage, transformer and head) | [bendr-2021](../collection/eeg-models/bendr-2021/card.md) |
| 0.39M, in its TUAB comparison table | [femba-2025](../collection/eeg-models/femba-2025/card.md) |
| 3.97M, in the suite's Table 1 | [datasets-benchmarks/brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) |
| 157M, the largest model in a six-model panel | [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) |

The spread is nearly three orders of magnitude, and it is load-bearing:
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)'s conclusion
that "parameter count alone does not order the models" rests specifically on BENDR being the largest
model in its panel and not the best. Under either of the other two figures BENDR is among the
smallest. The disagreement therefore propagates into a conclusion and is not merely bookkeeping. The
original paper cannot adjudicate, since [bendr-2021](../collection/eeg-models/bendr-2021/card.md)
publishes no total.

**LaBraM's supported channel count — 136, 137, or 128, and the strand's two cards of the same work
took different sides.**

| value | card |
|---|---|
| 137 channels, from the benchmark's body text | [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) |
| 136 channels, from the benchmark's Table 7, with the body/table conflict flagged as an internal inconsistency of the source | [datasets-benchmarks/adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) |
| 128-channel position embeddings, linearly interpolated to each dataset's channel count | [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) |
| no count stated; the spatial embedding is indexed "over the universal 10-20 channel set" | [labram-2024](../collection/eeg-models/labram-2024/card.md) |

Two features of this one are worth recording precisely. First, the 136/137 disagreement originates
*inside a single source*, AdaBrain-Bench, whose table and body differ; the two cards each carded a
different side, and only the `datasets-benchmarks` copy flags the conflict. Second, the corpus's
standing rule prefers tables over body prose, which would select 136 — the value the `eeg-models`
card did not take. The two cards are the deliberate cross-listing described in the strand INDEX's
cross-strand section, so this is a divergence between two records of one work, not two independent
readings of the field.

**BIOT's fixed channel count — 16 or 18.**
[biot-2023](../collection/eeg-models/biot-2023/card.md) states that its EEG datasets use "the common
16 bipolar montage channels in the international 10-20 system" and describes its PREST pretraining
corpus as 16 montage channels;
[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) records BIOT as
supporting 18 fixed channels and builds an argument on it, calling that count the model's bottleneck
against 62-channel downstream tasks.

**ST-Transformer's parameter count — 3.5M or 3.2M, splitting along the copied-baseline chain of §3.7.**
3.5M in [labram-2024](../collection/eeg-models/labram-2024/card.md) and
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md), both of which take their baseline tables
from BIOT; 3.2M in [femba-2025](../collection/eeg-models/femba-2025/card.md) and
[luna-2025](../collection/eeg-models/luna-2025/card.md), which share tables with each other. Each of
the four papers uses the figure to size a claim about parameter efficiency — LUNA at "roughly 100
times the parameters", FEMBA at "roughly 120 times".

**NeuroLM's parameter count — 1.7B or 169.60M.**
[kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md) gives
"3.3M in BIOT to 1.7B in NeuroLM" as the parameter range of the whole reviewed field, so its
model-scaling conclusion is anchored on that upper bound;
[datasets-benchmarks/brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) tabulates
NeuroLM at 169.60M. Unlike the cases above, this one cannot be adjudicated inside the corpus at all:
the strand holds no card for NeuroLM, so there is no primary record to check either figure against.

**CBraMod's pretraining hours and parameter count — four and three values respectively.**
Hours: "longer than 9000" retained from 27,062
([cbramod-2025](../collection/eeg-models/cbramod-2025/card.md)); "approximately 27,000 hours"
([adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md), whose own card flags
that this is the raw corpus size and not the retained set, and that the benchmark's argument about
EEGPT's scale is built by comparing it against the others); "~9,000-hour cleaned subset"
([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)); "9,200 h"
([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)). Parameters:
4.0M ([cbramod-2025](../collection/eeg-models/cbramod-2025/card.md), criss-cross variant, computed
with Thop); 4.9M backbone and 8.1M with task heads
([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)); 4.88M
([datasets-benchmarks/brain4fms](../collection/datasets-benchmarks/brain4fms/card.md)).

**EEGPT's pretraining hours — 246, 198, or unreported.**
[eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) reports none;
[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) says 246 hours;
[datasets-benchmarks/adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)
records 198 hours in that same benchmark's Table 7 against 246 in its body.

### 6.2 Sources that contradict themselves, carded faithfully

Distinct from §6.1: here one paper disagrees with itself and the card records both readings rather
than silently picking. Fourteen of the 22 entries carry at least one such record, which makes it a
property of the corpus rather than of any one entry.

- [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) — model size reported three ways that
  cannot all be true: 10M in the abstract, contributions and conclusion; 4.7M and 25M in the results
  tables; 101M for the "large" variant the text says was used everywhere, whose scaling-table
  accuracy matches the reported downstream number. The card adopts 101M by matching accuracies and
  states that any efficiency claim derived from the abstract's 10M is unsupported.
- [femba-2025](../collection/eeg-models/femba-2025/card.md) — pretraining subjects given as "more
  than 5,000", 14,987 and "more than 14,000"; the Huge model as 386M and 389M; the conclusion naming
  four downstream tasks where the abstract and the results say three, with no neonatal seizure result
  anywhere; TUSL at 38 subjects in Table I and 1,000 in the body.
- [biot-2023](../collection/eeg-models/biot-2023/card.md) — the contrastive temperature stated as
  T = 0.2 in the method section and T = 2 in the appendix, both as the default. The card adopts
  neither, because the two statements are of equal standing.
- [luna-2025](../collection/eeg-models/luna-2025/card.md) — pretraining hours as three roundings,
  "over 21,000" in the abstract and introduction, "over 21,900" in Section 4.1, and 21,928.32 summing
  Table 11, with no discrepancy noted by the authors.
- [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) — the second attention stream called
  V-Attention in the pretraining-settings paragraph and T-Attention in the method section, figure and
  eight other places.
- [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) — Table 6 shows removing the
  sensor embedding *gaining* 0.4 points on TUEV while the prose reports it as harmful. The card was
  corrected here and the correction narrows the entry: the prose qualifies itself by dataset
  difficulty ("especially on challenging MEG and EMEG datasets") rather than claiming uniform harm,
  so what the source does is decline to name the one dataset where the ablation helps, not overstate
  its own table.
- [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) — "Seven
  pretrained EEG foundation models" in Section 3.1 against six in the abstract, Table 1 and the
  conclusion.
- [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) — the classical
  comparator called a random forest in prose and a logistic regression in Table 2 and Section 3.6,
  with the value 0.847 consistent across both.
- [guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md)
  — the autoencoder count given three ways: "31 articles using autoencoders" out of 81 in the
  abstract, 38 percent; "34 articles employed autoencoders" in Section 2; and "approximately half"
  in the discussion, about 40. Two of the three are specific and both are the authors'. The card
  records all three and adopts none, so no autoencoder proportion should be quoted through this
  document.
- [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) — the normalization
  table labelling the EEGMAT dataset "EDMAT"; the `datasets-benchmarks` card of the same work records
  four further internal inconsistencies in the source.
- [bendr-2021](../collection/eeg-models/bendr-2021/card.md) — the transformer's internal feed-forward
  dimension printed as 3076 where 3072 would be conventional for a model dimension of 1536; verified
  against the published PDF, so the card records what the source says.
- [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) — publication year
  ambiguous between 2022 and 2023 across the article's own date lines, Crossref, and the sibling
  strand's citations. Separately, its parameter count exists only as a figure axis reading of roughly
  0.79 × 10⁶ against a third party's tabulation of 277K, a roughly threefold gap that nothing in
  either source explains — and the axis reading is itself now marked unverified, because Fig. 4's
  labels and data points are absent from both the extraction and the PDF's text layer. Only the
  caption and the remark that "the number of parameters increases proportionally with depth"
  survive, so this is a gap between one tabulated figure and one unrecoverable one.
- [labram-2024](../collection/eeg-models/labram-2024/card.md) — the arXiv title carries a trailing
  "in BCI" that the ICLR proceedings title omits, so citation strings differ between sources.
- [brainwave](../collection/eeg-models/brainwave/card.md) — the arXiv record is at v7 (September
  2025) with a 2024 first posting, and the text summarized on the card is v7, so a reader comparing
  against the v1 abstract will find different numbers.

### 6.3 Differences that look like disagreements and are not

Recorded so they are not mistaken for §6.1. REVE's pretraining corpus appears as 61,415 hours in
[reve-2025](../collection/eeg-models/reve-2025/card.md), "~60,000 hours" in
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) and "60,000 h" in
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md); its Base model
appears as 69M, 69.4M and 69.19M across
[reve-2025](../collection/eeg-models/reve-2025/card.md),
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) and
[datasets-benchmarks/brain4fms](../collection/datasets-benchmarks/brain4fms/card.md). These are
roundings of one figure. Likewise a third party's tabulation of a LUNA checkpoint at 40.4M is
consistent with LUNA-Large's 43M rather than in conflict with it, as
[luna-2025](../collection/eeg-models/luna-2025/card.md) records, and
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)'s 33M base against a third party's
32.71M is the same case.

---

## Coverage: all 22 entries and where each sits

Every entry appears at least twice in this tree, because the axes are orthogonal by construction:
every checkpoint has a spatial mechanism (§1), a provenance (§2) and an evidence profile (§3). The
"primary" column names the node where the entry is most distinguishing.

| entry | primary node | also appears in |
|---|---|---|
| [adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) | §3.2 third-party re-run | §1.8, §3.5, §3.6, §4.1, §4.2, §4.4, §6.1, §6.2 |
| [alexander-2019-cortical-waves](../collection/eeg-models/alexander-2019-cortical-waves/card.md) | §5.1 motivation, not evidence | — (the only entry confined to one node) |
| [banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md) | §2.1 objectives isolated from architecture | §2.2, §2.3, §3.4, §3.6, §4.1 |
| [bendr-2021](../collection/eeg-models/bendr-2021/card.md) | §1.1 learned per-channel parameter | §1.7, §2.1, §2.3, §2.4, §2.6, §3.4, §3.5, §3.6, §4.2, §6.1, §6.2 |
| [biot-2023](../collection/eeg-models/biot-2023/card.md) | §1.1 learned per-channel parameter | §1.7, §1.9, §2.1, §2.3, §2.6, §3.6, §4.1, §6.1, §6.2 |
| [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) | §1.2 coordinates and sensor metadata | §2.1, §2.3, §2.4, §2.5, §2.6, §3.1, §3.4, §3.5, §3.6, §4.1, §6.2, §6.3 |
| [brainwave](../collection/eeg-models/brainwave/card.md) | §1.5 position-blind | §2.1, §2.3, §2.6, §3.1, §3.7, §6.2 |
| [brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md) | §3.6 split geometry | §3.3, §4.3, §4.4 |
| [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) | §1.3 positional encoding from local context | §2.1, §2.2, §2.3, §2.4, §2.6, §3.4, §3.5, §3.6, §3.7, §4.1, §6.1, §6.2 |
| [eegconformer-2023](../collection/eeg-models/eegconformer-2023/card.md) | §1.6 no checkpoint, no contract | §2.3, §3.1, §3.5, §3.6, §4.2, §6.2 |
| [eegpt-2024](../collection/eeg-models/eegpt-2024/card.md) | §1.4 learned remap onto a fixed superset | §2.1, §2.2, §2.3, §2.5, §3.1, §3.4, §4.1, §4.2, §6.1, §6.2 |
| [femba-2025](../collection/eeg-models/femba-2025/card.md) | §1.1 learned per-channel parameter | §2.1, §2.3, §2.4, §2.5, §2.6, §3.1, §3.4, §3.6, §3.7, §6.1, §6.2 |
| [guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md) | §5.2 second-hand review | §2.1, §3.3, §3.7, §6.2 |
| [kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md) | §4.4 the measurement is unsound | §2.3, §2.4, §2.5, §3.3, §3.5, §5.2, §6.1 |
| [labram-2024](../collection/eeg-models/labram-2024/card.md) | §1.1 learned per-channel parameter | §2.1, §2.2, §2.3, §2.4, §2.5, §2.6, §3.1, §3.4, §3.5, §3.6, §3.7, §4.1, §4.2, §6.1, §6.2 |
| [lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) | §4.2 supervised baseline matches or beats | §1.8, §3.2, §3.4, §3.5, §3.6 |
| [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) | §4.3 scoring on identity, subject level | §3.2, §3.4, §3.5, §3.6, §4.2, §6.1, §6.2 |
| [luna-2025](../collection/eeg-models/luna-2025/card.md) | §1.2 coordinates and sensor metadata | §1.7, §1.9, §2.1, §2.3, §2.4, §2.5, §2.6, §3.1, §3.4, §3.6, §3.7, §6.1, §6.2, §6.3 |
| [muller-2024-transformers-cortical-waves](../collection/eeg-models/muller-2024-transformers-cortical-waves/card.md) | §5.1 motivation, not evidence | — |
| [reve-2025](../collection/eeg-models/reve-2025/card.md) | §1.2 coordinates and sensor metadata | §1.7, §1.9, §2.1, §2.2, §2.3, §2.4, §2.5, §2.6, §3.1, §3.4, §3.5, §3.6, §3.7, §4.1, §4.3, §4.5, §6.3 |
| [sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md) | §5.3 decisive number inaccessible | §3.2, §3.4, §3.6, §4.2 |
| [zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) | §4.3 scoring on identity, dataset level | §1.7, §1.8, §2.4, §2.5, §3.2, §3.6, §4.2, §4.5, §6.1, §6.3 |

Two entries sit in exactly one node —
[muller-2024-transformers-cortical-waves](../collection/eeg-models/muller-2024-transformers-cortical-waves/card.md)
and [alexander-2019-cortical-waves](../collection/eeg-models/alexander-2019-cortical-waves/card.md).
That is the intended shape rather than a placement failure: they have no spatial mechanism, no
pretraining corpus and no transfer evidence to profile, which is precisely the property §5.1 exists
to make legible. No entry failed to fit a node.
