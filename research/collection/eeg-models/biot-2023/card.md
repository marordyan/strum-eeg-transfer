---
slug: biot-2023
type: paper
strand: eeg-models
year: 2023
authors: [Yang, Westover, Sun]
venue: Advances in Neural Information Processing Systems 36 (NeurIPS 2023)
doi: 10.48550/arXiv.2305.10351
url: https://arxiv.org/abs/2305.10351
license: CC BY 4.0 (arXiv posting)
modalities: [scalp-eeg, clinical-eeg, 16-bipolar-derivations, 2-channel-sleep-eeg, ecg, wearable-accelerometer]
tags: [biosignal-tokenization, learned-channel-embedding, linear-attention, contrastive-objective, byol-style-predictor, missing-channel-robustness, released-weights, seizure-detection, cross-modality-pretraining]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

Flattening each channel's fixed-length segments into one long "biosignal sentence", with a learned
embedding per channel *name* and a parameter-free sinusoidal position embedding, lets one encoder
ingest recordings with mismatched channels, different lengths and missing segments — and lets a
model pretrained on resting EEG, sleep EEG and ECG be fine-tuned on any of them.

## Summary

BIOT (Biosignal Transformer) addresses format heterogeneity rather than scale. Every recording is
resampled to a common rate, each channel is normalized by the 95th percentile of its own absolute
amplitude, each channel is then cut into fixed-duration tokens with a fixed overlap, and all
tokens from all channels are flattened into a single sequence. Each token embedding is the sum of
its content embedding, a learned embedding indexed by the channel's name, and a sinusoidal
relative position embedding that carries no learnable parameters. Because the channel embedding is
a lookup by name and the sequence is a flat list, a sample missing a channel is simply a shorter
sentence, and a sample with an unfamiliar length is simply a longer one. The encoder is a 4-layer,
8-head transformer with linear (low-rank) attention. Unsupervised pretraining perturbs a sample by
dropping channels and tokens, predicts the unperturbed embedding from the perturbed one through a
two-layer predictor, and trains with a contrastive cross-entropy loss. Evaluation spans four EEG
tasks, one ECG task and one wearable-sensor task, plus a simulated-missingness study on TUEV and
two supervised-pretraining transfer studies.

## Relevance to the review

BIOT is the model that named the format-mismatch problem for this literature, and its solution is
the one this strand should contrast with coordinate-based approaches. The mechanism is a learned
embedding table indexed by channel *name*: an electrode the model never saw during pretraining has
no row in that table. This is what determines whether STRUM's montage can be fed to a BIOT
checkpoint at all — not the sequence length, which is genuinely unconstrained, but whether STRUM's
electrode names intersect the pretraining vocabulary.

A terminology note that matters for reading the paper. BIOT's EEG datasets use "the common 16
bipolar montage channels in the international 10-20 system", so what the channel-embedding table
indexes are bipolar *derivations* (differences between electrode pairs), not electrode positions.
For BIOT this is coherent — a derivation has a name and can own a row like anything else — but it
means the pretrained channel vocabulary is a vocabulary of derivations, and a referentially
recorded dataset does not share it.

The missing-channel study is the other directly relevant piece: it simulates dropping up to 4 of
16 channels and up to 5 half-second segments per channel, which is the failure mode of a real
dyadic recording session.

## Notable details

- **Pretraining corpus and total hours**: three unlabelled corpora, with sizes given as recordings
  and samples rather than hours. SHHS, sleep EEG, 5,445 recordings, 125 Hz, channels C3-A2 and
  C4-A1, 30-second samples, 5,093,522 samples. PREST, a proprietary unlabelled resting EEG
  dataset, 6,478 recordings, 200 Hz, 16 montage channels, 10-second samples, 5,110,992 samples.
  Cardiology (ECG), 21,264 recordings, 500 Hz, 6 or 12 leads, 10-second samples, 495,970 samples.
  **Total hours: `not reported`** — the string "hours" does not appear in the paper. Sample counts
  and per-sample durations are given in Table 1, so a duration could be computed, but the paper
  does not state one and the card does not substitute an arithmetic result for a reported figure.
  The abstract-level description is "5 million resting EEG samples (16 channels, 10s, 200Hz) and
  5 million sleep EEG samples (2 channels, 30s, 125Hz)".
- **Parameter count**: `not reported`. The paper specifies 4 transformer layers, 8 attention
  heads, linear attention with a rank-d approximation to the N x N softmax attention, and a
  two-layer predictor head for pretraining, but gives no parameter total and no token embedding
  dimension (it is written only as the symbol l).
- **Input contract**: resample all data to one rate by linear interpolation — 200 Hz for EEG,
  500 Hz for ECG, 50 Hz for wearable sensors. Per-channel normalization by the 95th percentile of
  absolute amplitude. Tokens are formed by FFT with an FFT size of 200 points and hop length of
  100 points for EEG, i.e. 1-second tokens with 0.5-second overlap (1000/200 points for ECG,
  100/10 for wearables). EEG tasks use the 16 common bipolar derivations of the 10-20 system.
  Channel identity enters through a learned lookup keyed on the channel; recording length is
  unconstrained; missing channels and missing segments are supported by construction.
- **Most informative transfer number, with baseline**: on CHB-MIT seizure detection, vanilla BIOT
  trained from scratch reaches 0.6640 ± 0.0037 balanced accuracy against the best supervised
  baseline, CNN-Transformer, at 0.6389 ± 0.0067 — a 2.5-point margin — while SPaRCNet reaches only
  0.5876. (The authors' actual wording is narrower than an earlier version of this card implied:
  "SPaRCNet is a strong model among all the baselines except on the CHB-MIT task", not the
  strongest overall.) Pretraining then adds a
  further 4.3 points: BIOT pretrained on six EEG datasets reaches 0.7068 ± 0.0457. So the
  architecture is worth about 2.5 points over the best supervised comparator and pretraining is
  worth about 4.3 points on top of the same architecture, which is the separation this strand
  needs.
- **Cross-modality pretraining works but weakly**: pretraining on PREST alone gives 0.6942 on
  CHB-MIT; adding SHHS (2-channel sleep EEG at 125 Hz) gives 0.6788 balanced accuracy but higher
  AUROC (0.8752 versus 0.8679). Adding all six EEG sources gives the best balanced accuracy.
  On the multi-class IIIC Seizure task the same progression moves balanced accuracy only from
  0.5762 (vanilla) to 0.5800 (PREST+SHHS), under 0.4 points.
- **Missing-data study**: recordings are perturbed by masking 0 to 5 half-second segments per
  channel independently, 0 to 4 of 16 channels, or both, with the stated assumption that masking
  does not alter the label. Figure 3 runs this on TUEV *and* IIIC Seizure, not TUEV alone as an
  earlier version of this bullet said. Baselines are made compatible by zero-imputing the masked
  regions. Finding: "'Missing channels' affects the performance more than 'Missing segments',
  which makes sense as segment masking still preserves information from all channels."
- **Supervised transfer with format change (corrected during the Phase 4 audit).** An earlier
  version of this bullet said the models were "supervised-pretrained on IIIC Seizure or TUEV under
  five channel/duration formats (8 or 16 channels, 2.5 to 10 seconds)" and "fine-tuned on CHB-MIT
  and TUEV". Three of those four particulars are wrong. Verbatim, Section 3.5: "We pre-train on
  the training set of CHB-MIT, IIIC Seizure, TUAB and fine-tunes on TUEV (which has 16 channels
  and 5s duration). All datasets use 200Hz sampling rate. We design three sets of configurations
  for the pre-trained datasets: Format (i) uses the first 8 channels and 10s duration; Format (ii)
  uses the full 16 channels but only the first 5s recording; Format (iii) uses full 16 channels and
  full 10s recording." So: **three** formats, not five; pretraining sources are CHB-MIT, IIIC
  Seizure and TUAB, not IIIC Seizure or TUEV; durations are 5 s and 10 s, with no 2.5 s condition;
  fine-tuning in the main text is on TUEV only, with the CHB-MIT version in Appendix B.2. The
  prediction layer is indeed swapped. What changes: the format sweep is coarser than the card
  claimed, and the one comparison it licenses is Format (ii) versus Format (iii) — the paper finds
  that "the configuration of (16 channels, 10 seconds) encodes longer duration and works
  consistently better" even though Format (ii) matches TUEV's own format, i.e. more pretraining
  signal beats format alignment. The authors attribute the transfer benefit to shared content:
  "TUAB and TUEV are both recorded from Temple University and share some common information, while
  IIIC seizure and TUEV are both related to seizure detection and may share some latent patterns."
- **Release**: code and pretrained models at https://github.com/ycq091044/BIOT. No licence is
  stated for the released weights in the paper.
- Compute: eight RTX A6000 GPUs, 512 GB memory. Results in the main tables are the mean and
  standard deviation over five random seeds; the figures use three.

## Open questions / limitations

- **The paper contradicts itself on the contrastive temperature.** Section 2 states
  "T represents the temperature (T = 0.2 throughout the paper)"; Appendix A.2 states "T = 2 as the
  temperature in unsupervised pre-training by default". Both are presented as the default. The
  card does not adopt either value, because the two statements are of equal standing — one is
  method-section prose and the other is an implementation-detail appendix — and the tables do not
  disambiguate. Anyone reproducing the pretraining needs to resolve this against the released
  code.
- The abstract claims "3% improvement over baselines in balanced accuracy" on CHB-MIT, while
  Table 2 gives vanilla BIOT at 0.6640 against the best baseline at 0.6389, a 2.5-point margin.
  The 3-point figure holds against ContraWR (0.6344) but not against the best comparator. The
  card quotes the table.
- PREST, one of the two EEG pretraining corpora and the larger of the two by sample count, is
  described only as "a large unlabeled proprietary resting EEG dataset". It cannot be inspected,
  so the pretraining corpus is not reproducible even though the weights are released.
- No parameter count, no compute-hours figure, and no pretraining-duration figure are given, so
  the cost of the 4.3-point pretraining gain cannot be assessed.
- The channel embedding is a lookup by channel identity. The paper does not say what happens when
  a downstream dataset presents a channel absent from the pretraining vocabulary — the missing-
  channel study removes known channels rather than introducing unknown ones.
- CHB-MIT splits are by patient (1–19 train, 20–21 validation, 22–23 test, then validation and
  test swapped and averaged), which is subject-wise, but the split assignment for the other
  datasets is described only in an appendix and is not summarized in the main text.
- The largest reported gains cluster on CHB-MIT, IIIC Seizure and HAR, which the authors
  themselves attribute to those datasets rewarding spectral features, since BIOT tokenizes via
  FFT. That is a statement about which tasks suit the tokenizer, and it bounds how far the
  results generalize.

## Citations

Primary: `biot-2023`

- `labram-2024`, `cbramod-2025` — later masked-modelling EEG models that adopt BIOT's
  patch-segmentation scheme and use its public baseline implementations.
- Grill et al., BYOL (2020) — the source of the predictor-on-perturbed-view structure BIOT uses
  in pretraining.
- Katharopoulos et al. and Wang et al. (Linformer) — the linear-attention approximations BIOT
  adopts to make the flattened channel-by-time sentence tractable.
- Jing et al., SPaRCNet (2023) — the strongest supervised baseline in the comparison, and the
  source of the IIIC Seizure dataset.
- Shoeb, CHB-MIT (2009) — the dataset carrying the paper's headline transfer result.
