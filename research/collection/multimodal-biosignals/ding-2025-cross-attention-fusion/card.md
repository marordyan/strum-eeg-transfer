---
slug: ding-2025-cross-attention-fusion
type: paper
strand: multimodal-biosignals
year: 2025
authors: [Ding, Ma, Li]
venue: Frontiers in Psychiatry 16:1713559
doi: 10.3389/fpsyt.2025.1713559
url: https://doi.org/10.3389/fpsyt.2025.1713559
license: CC BY
modalities: [eeg, eog, eda, resp, ppg]
tags: [multi-head-cross-attention, dual-branch, representation-learning, deap, seed-iv, intermediate-fusion, no-unimodal-arm, differential-entropy, eye-tracking]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

A dual-branch encoder feeding multi-head cross attention, where one modality's representation
queries the other's full sequence rather than being concatenated with it — a clean instance of
intermediate fusion on embeddings, but with no unimodal arm, so it cannot say what the peripheral
branch contributes.

## Summary

The stated problem is that existing multimodal fusion methods fail to capture complex, dynamic
interactions between modalities and so under-use complementary information. The proposed framework
has two stages. A dual-branch representation-learning module processes EEG and peripheral signals
in separate streams, each producing a complete feature *sequence* that preserves temporal
information rather than a single static feature vector. A multi-head cross-attention module then
uses one modality's representation as the Query to attend over the other modality's sequence, so
each new feature vector in the enhanced sequence is a weighted sum over the entire peripheral
sequence, with weights set by relevance to the current EEG feature. On DEAP the peripheral data
are consolidated into eight channels — two electrooculography, two electromyography, one galvanic
skin response, one skin temperature, one respiration and one blood volume pressure — with mean,
variance and entropy per channel giving a 24-dimensional peripheral feature vector. On SEED-IV,
differential entropy is extracted from five EEG bands using a short-time Fourier transform with a
4 s non-overlapping Hanning window, giving 62 x 5 = 310 EEG dimensions, alongside eye-tracking
features from an SMI tracker. Reported accuracy is 94.88% valence and 95.26% arousal on DEAP, and
89.12% four-class on SEED-IV.

## Relevance to the review

The architecture is the reason to card this and the missing arm is the reason it is
`relevance: low`.

On architecture, this is the configuration the project would most plausibly adopt: separate
per-modality encoders, no early concatenation, and a cross-attention layer that lets the EEG
representation decide, per time step, which parts of the peripheral sequence are relevant. The
paper's own justification for the dual-branch design — that it "respects the heterogeneity of the
different modalities" and produces "high-quality representations for subsequent computations" —
is the argument for bolting a head onto frozen encoders rather than training end to end. The
sequence-preserving detail matters too: most fusion work reduces each modality to a static vector
before combining, which discards exactly the temporal offset between a cortical response and its
peripheral consequence.

On evidence, the paper compares only against other *multimodal* methods: BDAE (85.20 / 80.50 on
DEAP), DCCA (85.62 / 84.33), HC-MFB (90.46 / 93.22), MMResLSTM (92.30 / 92.87) and, on SEED-IV,
DCCA (78.74), EmotionMeter (85.11) and MFFNN (87.06). There is no EEG-only arm and no
peripheral-only arm anywhere in the paper. Per the brief, an entry reporting only combined
performance cannot answer the project's question and is marked `relevance: low` unless it serves
another category; it serves category 2, and is carded there.

One incidental value: its Table 4 independently lists EmotionMeter at 85.11% on SEED-IV, which
corroborates the one number recoverable from that paywalled entry.

## Notable details

- **Combined numbers**: DEAP 94.88% valence, 95.26% arousal (binary); SEED-IV 89.12% four-class
  (happy, neutral, sad, fear).
- **EEG-only number**: **not reported.** No unimodal arm of any kind appears in the paper. This is
  a gap in the source, not in this corpus's access.
- **Peripheral-only number**: not reported.
- **Comparators** (all multimodal): DEAP — BDAE 85.20 / 80.50, DCCA 85.62 / 84.33, HC-MFB
  90.46 / 93.22, MMResLSTM 92.30 / 92.87. SEED-IV — DCCA 78.74, EmotionMeter 85.11, MFFNN 87.06.
- **DEAP peripheral channel set**: 8 channels — 2 EOG, 2 EMG, 1 GSR, 1 skin temperature, 1
  respiration, 1 blood volume pressure — reduced to 24 features (mean, variance, entropy per
  channel). Note how little this is: three scalars per channel against 310 EEG dimensions on
  SEED-IV, a 13:1 imbalance in representational budget before any learning happens.
- **SEED-IV EEG features**: differential entropy over five bands, 62 channels, STFT with a 4 s
  non-overlapping Hanning window, 310 dimensions.
- **Fusion mechanism**: multi-head cross attention with one modality as Query over the other's full
  sequence; each attention head is described as learning a specific type of cross-modal dependency.
- **Split protocol**: **not stated in the accessible text.** The extraction is the worst in this
  strand (Frontiers two-column template shredded into pipe fragments) and no train/test description
  was recoverable. Given the accuracies and the DEAP and SEED-IV conventions, a within-subject
  protocol is likely, but that is an inference and not a reading.
- **Participant count**: not stated by the paper beyond the public datasets' own cohorts (DEAP 32,
  SEED-IV 15).
- The authors' own limitation section notes that DEAP and SEED-IV "were both collected in
  controlled laboratory environments" and that video- and music-induced emotions "differ
  significantly from the complex, spontaneous emotions experienced in real life", so real-world
  performance "remains to be validated".
- They also acknowledge that "the model's performance fluctuates across" subjects, which is as
  close as the paper comes to a cross-subject statement.

## Open questions / limitations

- No unimodal arms at all, so the paper contributes nothing to the project's third comparison
  beyond the architecture.
- No ablation of the cross-attention module itself is visible in the accessible text, so even the
  architectural claim — that cross attention beats concatenation — rests on comparison to other
  papers' models rather than to its own model with the module removed.
- The 24-dimensional peripheral representation on DEAP is three summary statistics per channel.
  Whatever the cross-attention mechanism does, it is attending over a very coarse peripheral
  description, and the paper does not test whether a richer peripheral encoder changes anything.
- Split protocol unstated. Accuracies of 94.88% and 95.26% on DEAP valence and arousal are far
  above typical cross-subject figures for that dataset and are only interpretable with the
  protocol named.
- The comparator numbers are quoted from other papers rather than re-run, so the ranking inherits
  every difference in preprocessing and splits among them.
- The extraction quality is poor enough that a downstream reader should check the two comparison
  tables against the PDF before quoting them.
- EMG is in the DEAP peripheral set and is not in the strand's controlled modality vocabulary; the
  frontmatter omits it, and Phase 3's modality-by-task matrix will therefore under-report this
  entry by one channel.

## Citations

Primary: `ding-2025-cross-attention-fusion`

- `li-2023-incongruity-fusion` — the cross-modal-transformer approach that treats disagreement
  rather than relevance as the useful signal.
- `liu-2022-multimodal-robustness` — DCCA and BDAE, two of this paper's comparators, with an
  EEG-feature ablation this paper lacks.
- `zheng-2018-emotionmeter` — the SEED-IV comparator at 85.11%, corroborated here.
- `kumar-2026-attention-eeg-ecg-stress` — attention fusion with the unimodal arms this paper omits.
- `angkan-2024-invehicle-cognitive-load` — what a full modality grid looks like when it is
  reported.
