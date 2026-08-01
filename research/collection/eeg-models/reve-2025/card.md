---
slug: reve-2025
type: paper
strand: eeg-models
year: 2025
authors: [El Ouahidi, Lys, Thölke, Farrugia, Pasdeloup, Gripon, Jerbi, Lioi]
venue: NeurIPS 2025 (arXiv preprint 2510.21585)
doi: null
url: https://arxiv.org/abs/2510.21585
license: CC BY-NC-ND 4.0 (arXiv posting)
modalities: [scalp-eeg, high-density-eeg, clinical-eeg, arbitrary-electrode-layout, 3d-electrode-coordinates]
tags: [masked-autoencoder, transformer, 4d-positional-encoding, layout-flexible, bipolar-as-midpoint, linear-probing, lora, model-souping, released-weights, motor-imagery, sleep-staging]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

Generating positional encodings directly from each patch's 3D electrode coordinate and time
index — rather than looking them up in a learned per-channel table — lets one masked-autoencoder
encoder be pretrained across 92 heterogeneous EEG datasets and then applied to electrode layouts
and recording lengths it never saw, which is what makes its frozen embeddings usable without
full fine-tuning.

## Summary

REVE is a spatio-temporal transformer trained with a modified masked-autoencoder (MAE) objective
on 61,415 hours of EEG drawn from 92 datasets and 24,274 subjects (19 TB raw, 6 TB after
preprocessing) — the largest non-invasive EEG pretraining corpus reported at the time of writing.
Its central mechanism is a 4D positional encoding: the (x, y, z) coordinate of each electrode plus
a scaled temporal patch index are each projected into a multi-frequency Fourier basis (Cartesian
product across the four dimensions, then sine and cosine), and the result is summed with a
learnable linear/GELU/LayerNorm projection of the same 4D coordinate. Because nothing is looked up
by channel name, an unseen electrode set requires no new parameters. Pretraining uses joint
spatio-temporal *block* masking (55% total ratio, 3 cm spatial radius, 3 s temporal radius, plus a
10% whole-channel dropout) with an L1 reconstruction loss on raw signal, and a secondary loss that
reconstructs the same masked patches from a single attention-pooled global token. On nine
classification benchmarks REVE-Base reaches 0.7150 average balanced accuracy against 0.6898 for
CBraMod and 0.5941 for EEGNet. Code, weights at three sizes, and loaders that accept arbitrary 3D
coordinates are released.

## Relevance to the review

This is the strand's most direct answer to whether a pretrained checkpoint can be fed STRUM data
at all. The competing checkpoints named in the paper (BIOT, LaBraM, CBraMod) bind spatial identity
to a learned embedding table indexed by channel, which is why the paper describes them as
"often necessitating full fine-tuning for transfer"; REVE's encoding is computed from coordinates,
so an electrode layout absent from pretraining costs nothing structurally. The paper substantiates
this on two axes STRUM will exercise: TUEV is preprocessed into 16 bipolar channels the model never
saw in pretraining, and HMC/ISRUC feed 30-second windows to a model pretrained on 10-second segments.

A terminology caution that matters for how far this claim can be carried. What the mechanism supports
is an arbitrary *electrode layout*, meaning a set of positions. A *montage* in the strict sense is a
derivation scheme, and a bipolar derivation is a difference between two electrodes rather than a
signal at one. REVE does not represent that difference natively: per Appendix C, bipolar channels are
given "the average position of each bipolar montage", a single midpoint coordinate. The paper's own
abstract and conclusion say "montages" where its methods section says "arbitrary electrode layouts",
so the looser reading comes from the source, not from this card. Phase 3 should carry the precise
claim, not the abstract's. The two-stage
fine-tuning recipe (frozen-backbone linear probe, then unfreeze, as one continuous run, with LoRA
on the QKVO projections) is also directly transferable to a small dataset like STRUM, and the
paper's own framing of why — EEG datasets are "limited in size, subject-dependent, and prone to
distribution shifts" — matches this project's regime.

The paper also supplies the single most useful ablation in the strand for comparison 1 versus
comparison 2: it reports REVE trained from scratch on the downstream task, so the contribution of
pretraining is separable from the contribution of the architecture.

## Notable details

- **Pretraining corpus and total hours**: 61,415 hours, 92 datasets, 24,274 subjects, 150,833
  sessions. Breakdown by category: clinical 50,581 h / 19,290 subjects / 8 datasets; cognition
  10,376 h / 4,193 subjects / 56 datasets; BCI 457 h / 791 subjects / 28 datasets. Sources include
  TUH (26,847 h), PhysioNet (22,707 h), OpenNeuro (10,194 h), MOABB (384 h). 396 unique electrode
  names; most recordings follow the 10-5 system. The paper contrasts this with 9,000 h for CBraMod
  and 2,534 h for LaBraM, attributing part of the difference to not discarding signals above
  100 µV.
- **Parameter count**: three encoder sizes — Small 12M (depth 4, 8 heads, dim 512), Base 69M
  (depth 22, 8 heads, dim 512), Large 408M (depth 22, 19 heads, dim 1250). Fourier frequencies per
  dimension n_freq = 4 for Small/Base, 5 for Large.
- **Input contract**: 200 Hz after resampling; band-pass 0.5–99.5 Hz; float32; z-score
  normalization with statistics computed across the recording session, then clipping at 15 standard
  deviations. Patches are 1 s windows with 0.1 s overlap, taken per channel. Channel count and
  ordering are unconstrained — the model requires a 3D coordinate per channel (used directly when
  available, otherwise inferred from the standard label), and channels without an identifiable name
  or position were excluded from pretraining. Signals must be at least 1 second long and a multiple
  of one second; Gaussian noise of σ = 0.25 cm is added to electrode coordinates during pretraining
  as augmentation.
- **Most informative transfer number, with baseline**: on PhysioNet-MI 4-class, REVE-Base with
  pretraining reaches 0.6480 balanced accuracy versus 0.5409 for the identical architecture trained
  from scratch — a +10.7 point gain attributable to pretraining rather than architecture. In the
  same table CBraMod gains only ~2 points from its pretraining (0.6417 with, 0.6196 without), and
  without pretraining CBraMod *beats* REVE by roughly 8 points. Against a small supervised
  baseline, REVE-Base averages 0.7150 balanced accuracy across nine tasks versus EEGNet at 0.5941.
- **How bipolar derivations are handled**: TUEV is preprocessed with BIOT's scripts into 16 common
  bipolar channels in the 10-20 system, and the paper states in Appendix C that "to provide our model
  with the electrode positions, we used the average position of each bipolar montage". So a
  derivation is represented by the midpoint of its electrode pair. This is a preprocessing decision
  by the authors rather than a property of the positional encoding, which takes one coordinate per
  channel and has no representation for a difference between two sites.
- **Frozen-feature transfer**: with the backbone frozen on PhysioNet-MI, REVE-Base reaches 0.5371
  balanced accuracy against 0.3845 (CBraMod), 0.3715 (LaBraM), 0.3698 (BIOT). Across ten tasks
  under linear probing, REVE-Large averages 0.654 versus CBraMod at 0.501. The paper attributes the
  frozen-feature advantage specifically to the attention-pooling secondary loss.
- **Scaling and souping**: performance improves with model size; averaging the weights of at least
  five fine-tuning runs adds ~1.5 points on average (REVE-Base reaches 0.696 on TUEV by souping ten
  runs), but souping "showed limited benefits for the small models and sometimes led to negative
  outcomes".
- Evaluation reuses the train/val/test splits of CBraMod, LaBraM, and BIOT for comparability, with
  one deviation: REVE's ISRUC numbers exclude a chin electrode that the baseline code had included
  in place of an EEG electrode, so the ISRUC column is not strictly like-for-like.

## Open questions / limitations

- The paper's own stated limits: inputs must be at least one second and a whole number of seconds;
  the corpus is unfiltered for quality and demographically skewed toward North America and Europe;
  no scaling law is fitted, only a qualitative scaling trend.
- The 61,415-hour figure is a corpus size, not a curation claim. The authors explicitly flag
  "removing low-quality recordings, balancing distributions, and identifying representative
  subsets" as future work, so the number should not be read as 61,415 hours of usable signal.
- Every reported comparison is to numbers "displayed in existing studies" rather than re-run,
  except CBraMod under linear probing, which was reproduced. The linear-probing table is therefore
  the only baseline comparison in the paper measured under the authors' own control.
- Cross-subject generalization is inherited from the baselines' split protocols rather than
  independently established. The paper does not state per-dataset whether splits are subject-wise,
  so the claim that REVE generalizes across subjects rests on protocols defined elsewhere.
- The generalization claim is demonstrated on TUEV's bipolar channels and on longer windows, not on a
  systematically held-out electrode layout. How far the coordinate-based encoding extrapolates, for
  example to a layout denser or sparser than anything in the 92 datasets, is untested.
- Representing a bipolar derivation by the midpoint of its electrode pair is lossy in a way the paper
  does not examine. Two different pairs can share a midpoint, and the midpoint discards the
  orientation and separation of the pair, which is what a differential recording actually measures.
  No ablation compares this choice against alternatives, so its adequacy rests on the TUEV result
  alone. This bears directly on the project: whether it matters for STRUM depends on the derivation
  scheme STRUM uses, which the `candidate-datasets` strand must record.
- No task in the evaluation set is a dyadic or two-person recording, and none of the ten downstream
  datasets is smaller than roughly 1,700 samples, so the paper provides no evidence at STRUM's
  sample scale.
- Model souping's negative results at small model size are reported without the failing numbers.

## Citations

Primary: `reve-2025`

- `labram-2024` — Jiang et al., ICLR 2024. The learned-spatial-embedding baseline REVE argues
  against, and one of the three foundation models it compares to.
- Wang et al., CBraMod (arXiv 2412.07236) — the strongest baseline in REVE's tables and the only
  one the authors reproduced themselves; listed as a lead in the strand brief.
- Yang et al., BIOT — the patch-segmentation scheme REVE adopts ("following BIOT") and an absolute
  positional-encoding baseline.
- He et al., Masked Autoencoders Are Scalable Vision Learners (2022) — the MAE structure REVE
  modifies, notably by reusing one positional encoding for encoder and decoder.
- Défossez et al. (2023) — the 2D Fourier positional encoding REVE extends to 4D.
