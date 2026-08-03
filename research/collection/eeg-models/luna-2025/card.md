---
slug: luna-2025
type: paper
strand: eeg-models
year: 2025
authors: [Döner, Ingolfsson, Benini, Li]
venue: NeurIPS 2025 (arXiv preprint 2510.22257)
doi: null
url: https://arxiv.org/abs/2510.22257
license: null
modalities: [scalp-eeg, clinical-eeg, bipolar-derivation, emotion-eeg, 3d-electrode-coordinates, arbitrary-electrode-layout]
tags: [learned-queries, cross-attention, channel-unification, masked-patch-reconstruction, nerf-positional-encoding, linear-in-channels, rope, full-fine-tuning, unseen-montage, model-scaling]
relevance: medium
imported_from: null
added: 2026-08-01

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

Cross-attending a small fixed set of learned queries to the channel dimension collapses any
electrode set into a fixed-size latent before any temporal attention runs, which makes the encoder
linear rather than quadratic in channel count and gives every downstream head the same input width
regardless of how many electrodes a recording has.

## Summary

LUNA (Latent Unified Network Architecture) is a masked-patch-reconstruction model whose distinctive
component is a Channel-Unification Module. Each channel is patched into 40-sample segments,
embedded by two parallel pathways — a 1D convolutional temporal encoder and an MLP over the Fourier
magnitude and phase of the same patch — and given a positional encoding computed from its
normalised 3D electrode coordinate through a NeRF-style sinusoidal encoding plus an MLP. Q learned
queries, orthogonally initialised and carrying no batch dimension, then cross-attend to the C
channel features at each patch position, producing a fixed Q × E latent. Only after that do
transformer blocks with rotary positional embeddings run, over the patch dimension alone, so the
temporal sequence length is S rather than S · C. Pretraining reconstructs masked patches under a
Smooth L1 loss, with a secondary query-specialisation loss penalising off-diagonal similarity in
the query-to-channel affinity matrix; a per-channel decoder query set, indexed by channel label,
recovers channel-specific values and is discarded after pretraining. Trained on TUEG plus Siena
(21,928 hours across 20-, 22- and 29-channel recordings), LUNA reports state-of-the-art AUROC on
artifact detection (0.921 on TUAR) and slowing classification (0.802 on TUSL), competitive but not
leading results on TUAB, and a deficit against CBraMod on an unseen 62-channel emotion dataset.

## Relevance to the review

This is the strand's second mechanism for feeding a checkpoint an electrode set it never saw, and
it works differently from `reve-2025`'s. REVE keeps one token per channel and generates its
positional encoding from coordinates, so an unseen layout enters the sequence directly. LUNA
projects the channel set onto a fixed number of learned queries first, so the layout never reaches
the temporal encoder at all. The consequence for a project with a non-standard recording setup is
the same in kind but different in cost: LUNA's compute does not grow with channel count, and its
downstream feature width is fixed at Q · E, but any layout-specific structure has to survive a
bottleneck of 4 to 8 queries.

The paper is candid about where that bottleneck costs it, and this is the result most worth carrying
forward. On SEED-V, a 62-channel layout absent from pretraining, LUNA-Huge reaches 39.00% balanced
accuracy against CBraMod's 40.91% and LaBraM-Base's 39.76%, and the authors write that
"generalizing zero-shot to vastly different, high-density layouts remains challenging, possibly due
to positional encoding constraints". A topology-agnostic architecture that still loses on the one
genuinely unseen topology in its own evaluation is exactly the evidence Phase 3 needs about what
"montage-agnostic" buys in practice.

Two precision points about the terminology. First, what the mechanism supports is an arbitrary
*electrode layout*, a set of positions; the paper's abstract and title say "topology-agnostic" and
its conclusion says "montage-agnostic", which is looser. Second, and unlike `reve-2025`, LUNA does
not say how it assigns a 3D coordinate to a bipolar derivation, even though its entire Temple
University pretraining and evaluation set is processed into a bipolar "double-banana" montage
(the 20 longitudinal pairs are listed in Appendix A.7) while Siena and SEED-V stay unipolar. So
the coordinate fed to the NeRF encoding for a channel such as Fp1–F7 is unspecified in the source.

## Notable details

- **Pretraining corpus and total hours**: TUEG (14,987 subjects, 21,787.32 hours, 20 or 22 channels,
  bipolar) plus the Siena Scalp EEG Database (14 subjects, 141.0 hours, 29 channels, unipolar) —
  21,928.32 hours in total. Precision note added in the Phase 4 audit: Table 11 lists the two
  per-dataset figures but states no total, so 21,928.32 is this card's sum of them, not a value the
  paper prints. The abstract and introduction both round to "over 21,000 hours" while Section 4.1
  says "over 21,900 hours (see Table 11)"; the summed table figure is the value carded. All
  subjects and recordings from TUAB, TUAR, TUSL and SEED-V were excluded from pretraining.
- **Parameter count**: Base 7M, Large 43M, Huge 311.4M. The three differ in transformer depth
  (8 / 10 / 24), hidden size (256 / 576 / 1024), number of queries (4 / 6 / 8) and query size
  (64 / 96 / 128), with 8 / 12 / 16 attention heads. `datasets-benchmarks/neuralbench` independently
  tabulates the LUNA checkpoint it ran at 40.4M, consistent with LUNA-Large.
- **Input contract**: 256 Hz after resampling; band-pass 0.1–75 Hz; 50 or 60 Hz notch; per-channel
  z-score within each sample. Patches are 40 samples (0.156 s at 256 Hz), non-overlapping. Samples
  are 5-second non-overlapping segments for all datasets except SEED-V, which keeps its native
  1-second segmentation. Each channel requires a normalised 3D coordinate. Channel count is
  unconstrained by construction; pretraining saw only 20-, 22- and 29-channel sets, and the
  Temple University data is converted to a 20-pair longitudinal bipolar montage before use.
- **Most informative transfer number, with baseline**: on SEED-V — the only dataset whose electrode
  layout was absent from pretraining, and the only non-clinical task — LUNA-Huge reaches 0.3900
  balanced accuracy against 0.3678 for CNN-Transformer, the best of the five supervised models in
  the same table, a 2.2-point gain at 311.4M parameters against 3.2M. The gain is not monotonic in
  size: LUNA-Large (43M) reaches 0.3918, above Huge. On the paper's headline task the margin is
  larger — TUSL AUROC 0.802 for LUNA-Huge against 0.721 for EEG-GNN, the best supervised model there
  — but TUSL is a Temple University subset under a randomised sample-level split, whereas SEED-V is
  the case closest to this project's regime.
- **Where it does not lead**: on TUAB, LUNA-Huge reaches 81.57% balanced accuracy against 82.58%
  for LaBraM-Huge and 82.49% for CBraMod, and its 0.8957 AUROC trails both. Against the supervised
  baselines in that table it is 1.9 points above ST-Transformer (79.66%) at roughly 100 times the
  parameters. On SEED-V it trails CBraMod on all three reported metrics.
- **Split protocol**: TUAB uses its official train-test split. TUAR and TUSL use "an 80%/10%/10%
  randomized sample-level split", chosen for like-for-like comparison with EEGFormer, and the
  authors state plainly that "subject-independent splits are the gold standard for assessing
  clinical generalization and recommend them for future benchmark comparisons". SEED-V splits its
  fifteen trials equally into train, validation and test per session, which is within-subject.
  Results are mean and standard deviation over three seeds.
- **Fine-tuning budget**: full fine-tuning with a single learned aggregation query attending to the
  encoder output, then an MLP; AdamW, 50 epochs, early stopping at patience 10, layer-wise
  learning-rate decay 0.5 (Base) or 0.8 (Large/Huge). No linear-probing or frozen-backbone result is
  reported.
- **Ablations are small and honestly reported as such**: replacing learned queries with predefined
  anatomical regions costs 0.004–0.006 AUROC, "within seed variation"; removing the
  query-specialisation loss costs 0.003–0.006, also within variation; the largest single effect is
  removing the frequency embedding, up to 0.012 AUROC. The authors keep the specialisation loss for
  its regularising role rather than for a measured gain. Under a fixed Q · E = 256 budget, 4 × 64
  beats 2 × 128 and 8 × 32 on TUAB and TUSL.
- Code is at `https://github.com/pulp-bio/biofoundation`. The NeurIPS checklist states weights
  "will be released upon publication" and that "we do not release any new assets yet", so no licence
  for the released checkpoint is stated.

## Open questions / limitations

- Three of the four evaluation datasets are Temple University subsets from the same corpus that
  supplies 99.4% of the pretraining hours, with subject overlap removed. The one dataset outside
  that distribution, SEED-V, is where LUNA loses. The paper's topology-generalisation claim
  therefore rests on the case it handles least well.
- How a bipolar derivation gets a 3D coordinate is never stated, even though the bipolar montage
  covers all Temple University data. The Appendix A.7 pair list makes the derivation explicit but
  not the coordinate assignment, so the positional encoding's input for those channels is unknown
  from the source.
- Two of the four benchmarks use a randomised sample-level split by the authors' own description.
  They flag the problem rather than fix it, so the TUAR and TUSL numbers should not be read as
  cross-subject results.
- No frozen-backbone or linear-probe result exists, so nothing here speaks to whether LUNA's
  representation is usable without full fine-tuning — the regime this project's third comparison
  would need.
- Scaling is inconsistent. Base to Huge is 44 times the parameters for 0.94 balanced-accuracy points
  on TUAB and 1.9 AUROC points on TUAR, and on SEED-V the Large model beats the Huge one on all
  three metrics. The paper reports the SEED-V case as "positive scaling from Base to Large" without
  noting that Huge reverses it. Related, and worth knowing before quoting the abstract: its headline
  pair — "balanced accuracies of 81.57% on TUAB and 39.18% on SEED-V" — takes the TUAB figure from
  LUNA-Huge and the SEED-V figure from LUNA-Large, without saying so. There is no single LUNA
  variant that achieves both.
- The pretraining hours figure appears as three different roundings (>21,000 in the abstract and
  introduction, >21,900 in Section 4.1, 21,928.32 summing Table 11) with no discrepancy noted.
- No dyadic or two-person recording, and no peripheral physiology. The channel-unification module is
  modality-agnostic in principle — it consumes a set of positioned time series — but nothing in the
  paper tests a non-EEG channel.

## Citations

Primary: `luna-2025`

- `femba-2025` — Tegon et al., EMBC 2025. Same laboratory and code base; supplies the TUAR and TUSL
  baseline tables LUNA compares against and is the model it reports beating on both.
- `cbramod-2025` — Wang et al. The alternating spatial/temporal-attention design LUNA's complexity
  argument is aimed at, and the model that beats it on SEED-V.
- `labram-2024` — Jiang et al., ICLR 2024. The flatten-channels-and-time design whose
  O((S·C)²) cost LUNA's channel unification is meant to avoid.
- `reve-2025` — El Ouahidi et al., NeurIPS 2025. The other coordinate-based route to layout
  flexibility in this strand; `datasets-benchmarks/neuralbench` ranks the two first and third.
- `datasets-benchmarks/neuralbench` — Banville et al. 2026. Third-party evaluation placing LUNA
  third by mean normalised rank (0.30) behind REVE (0.20) and LaBraM (0.21), and noting that CTNet
  at 150K parameters overtakes it when the dataset set is widened.
