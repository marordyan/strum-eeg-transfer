---
slug: labram-2024
type: paper
strand: eeg-models
year: 2024
authors: [Jiang, Zhao, Lu]
venue: ICLR 2024
doi: 10.48550/arXiv.2405.18765
url: https://arxiv.org/abs/2405.18765
license: null
modalities: [scalp-eeg, clinical-eeg, 10-20-montage, variable-channel-count]
tags: [masked-eeg-modeling, vector-quantization, neural-tokenizer, fourier-spectrum-prediction, transformer, learned-spatial-embedding, released-weights, abnormal-detection, event-classification, data-scaling]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

Masked reconstruction of raw EEG failed to converge, so LaBraM predicts a discrete
vector-quantized code per channel-patch whose decoder reconstructs the patch's Fourier amplitude
and phase instead — making the tokenizer target a spectral quantity rather than the noisy waveform,
and turning masked language modeling into a workable EEG pretraining objective.

## Summary

LaBraM is a "neural Transformer" pretrained on over 2,500 hours of EEG from about 20 datasets, and
the canonical reference for the vector-quantized branch of EEG pretraining. Signals are segmented
into per-channel patches so that datasets with mismatched channel counts and lengths can be mixed.
Pretraining runs in two stages. First a neural tokenizer is trained: a codebook of discrete
embeddings is learned by quantizing patch representations to their nearest codebook entry under
L2-normalized cosine similarity, with the training signal coming from a decoder that reconstructs
the Discrete Fourier Transform amplitude and phase of the original patch. The authors state plainly
why: "the loss fails to converge while directly reconstructing raw EEG signals", because EEG has low
signal-to-noise ratio and is nonstationary. Second, the transformer is pretrained by masking a
fraction of patches and predicting their discrete codes from the visible ones. Spatial and temporal
information enter as two learned embedding lists — a temporal embedding indexed by patch position
and a spatial embedding indexed by channel — added to patch features as absolute positional
encoding. On TUAB, LaBraM-Base reaches 0.8140 balanced accuracy against 0.7966 for the best
supervised baseline; on TUEV, 0.6409 against 0.5281 for BIOT.

## Relevance to the review

LaBraM is the checkpoint most other work in this strand measures against, so it is the reference
point for reading every other card: `reve-2025`, `brainwave`, `lin-2026-identity-trap`,
`zare-2026-stress-testing`, and `sirca-2026-peft-motor-imagery` all evaluate or compare against it.
Any claim this project makes about "an off-the-shelf pretrained EEG foundation model" will be read
against LaBraM by default.

Its spatial-embedding design is the specific mechanism that makes montage transfer hard, and
therefore the thing STRUM data collides with. The spatial embedding is a learned lookup table
indexed by channel identity over the 10-20 universal channel set; a channel absent from that set
has no entry, and a channel present but rare has an entry trained on little data. This is what
`reve-2025` means when it says absolute encodings "lack the flexibility to accommodate spatial
diversity, often necessitating full fine-tuning for transfer", and it is why third parties adapt it
by force: `zare-2026-stress-testing` loads LaBraM via braindecode and *linearly interpolates its
128-channel position embeddings* to each dataset's channel count, then explicitly warns that its
LaBraM results "should not be interpreted as clean tests of pretraining objective" because of that
position-mapping mismatch.

The paper's own data-scaling result is the most load-bearing fact here for Phase 4, and it points
away from more pretraining: see Notable details.

## Notable details

- **Pretraining corpus and total hours**: over 2,500 hours from about 20 datasets, comprising public
  EEG datasets plus data collected by the authors. Appendix D lists the constituents, the largest of
  which are TUH corpora (one at 1138.53 hours, one at 92.22 hours) and an ESI NeuroScan collection
  at 342.23 hours. The four downstream datasets are excluded from pretraining. Constituent datasets
  range from 8 to 100+ subjects at 100 Hz to 2048 Hz and 19 to 64 channels.
- **Parameter count**: three sizes — LaBraM-Base 5.8M, LaBraM-Large 46M, LaBraM-Huge 369M, scaled by
  increasing transformer depth and hidden size. The authors describe 369M as "the largest models in
  BCI ever" at the time. Unless stated otherwise all results in the paper are LaBraM-Base.
- **Input contract**: resampled to 200 Hz; band-pass 0.1–75 Hz; 50 Hz notch filter for mains;
  amplitude normalized by setting the unit to 0.1 mV so values sit mainly in [-1, 1]. Patch window
  w = 200 samples (1 second), **non-overlapping**. Sequence length is capped at 256 patches, so
  channel count and window length trade off against each other — the paper's own examples are 64
  channels at 4 seconds or 32 channels at 8 seconds. Data stride between training samples is 4
  seconds. Channel ordering matters: each channel is mapped to its entry in a learned spatial
  embedding list indexed over the universal 10-20 channel set, so a channel must be nameable within
  that set to be encoded at all.
- **Most informative transfer number, with baseline**: on TUEV six-class event classification,
  LaBraM-Base at 5.8M parameters reaches 0.6409 balanced accuracy against 0.5281 for BIOT (3.2M,
  pretrained) and against a best supervised-from-scratch baseline of 0.4384 (ContraWR, 1.6M) — a
  +20.3 point margin over the best non-pretrained model. On TUAB the same comparison is much
  tighter: 0.8140 versus 0.7966 for ST-Transformer (3.5M, supervised), a +1.7 point margin. The
  baselines are taken from BIOT rather than re-run.
- **Data scaling gives a negative result at Base size**: "the performance of the Base model with 500
  hours of training exceeds that of the 2500-hour model on TUAB, while approaching over 90% of the
  2500-hour performance on TUEV". The Large model improves with data but its "growth rate slows
  after 1000 hours"; only the Huge model shows a sustained upward trend. The authors conclude
  "2,500 hours is not the answer to this question" and estimate the Huge model would need "at least
  ten thousand hours".
- **Downstream-data-in-pretraining ablation**: including TUAB and TUEV in pretraining does not
  significantly change downstream performance, which the authors read as evidence of universal
  representations. Recordings were disjoint in both conditions.
- Evaluation splits follow BIOT exactly: the dataset-provided train/test separation, with training
  *patients* split 80/20 into train and validation — so splits are subject-wise on the
  train/validation boundary. Five random seeds, mean and standard deviation reported. Metrics:
  balanced accuracy, AUC-PR, AUROC for binary; balanced accuracy, Cohen's kappa, weighted F1 for
  multi-class.
- Code is released at https://github.com/935963004/LaBraM. The paper does not state the licence of
  the code or of the released weights.

## Open questions / limitations

- The paper does not state a licence for the released weights or code, so the released-checkpoint
  question that category 3 of the brief asks cannot be answered from this source.
- On TUAB the margin over a small supervised model is +1.7 points (0.8140 versus 0.7966), and
  scaling from 5.8M to 369M parameters buys only a further +1.2 points (0.8258). Read together with
  the 500-hour result, this paper's own numbers support a reading in which most of the TUAB
  performance is available without large-scale pretraining. The authors do not draw that reading.
- All baselines are quoted from BIOT rather than re-run under the authors' pipeline, so the
  comparisons inherit BIOT's preprocessing and tuning decisions for the baselines while LaBraM gets
  the authors' own.
- The 256-patch sequence cap is a hard constraint that couples channel count to window length. A
  high-density montage forces short windows and vice versa; the paper reports no ablation over that
  trade-off, so which side to give up for a given task is undetermined.
- Both TUAB and TUEV are Temple University corpora and TUH data dominates the pretraining set. The
  two headline results are therefore close to in-domain, a point `zare-2026-stress-testing` makes
  explicitly ("TUAB is in-domain"). The paper's emotion-recognition and gait-prediction results,
  which are further from the pretraining distribution, are relegated to Appendix F.
- The learned spatial embedding has no defined behaviour for a channel outside the 10-20 universal
  set, and the paper does not test an unseen montage. Third-party use resorts to interpolating the
  position embeddings (`zare-2026-stress-testing`), an adaptation the original paper neither
  specifies nor validates.
- Whether the frozen representations are useful is not tested here at all; the paper reports only
  fine-tuning. Independent linear-probe evaluations are less favourable: `reve-2025` measures frozen
  LaBraM at 0.3715 balanced accuracy on PhysioNet-MI, and `lin-2026-identity-trap` finds LaBraM's
  frozen embeddings dominated by subject identity.
- The arXiv title carries a trailing "in BCI" that the ICLR proceedings title omits, so citation
  strings for this paper differ between sources.

## Citations

Primary: `labram-2024`

- `reve-2025` — El Ouahidi et al., NeurIPS 2025. Argues directly against LaBraM's learned spatial
  embedding and reports LaBraM's frozen-feature performance as much weaker than its own.
- Yang et al., BIOT — the immediately preceding pretrained model, the source of LaBraM's evaluation
  splits and baseline numbers, and the comparator LaBraM beats by +11.3 points on TUEV.
- Van Den Oord et al., VQ-VAE (2017) — the discrete-latent scheme LaBraM's neural tokenizer adapts;
  the L2-normalization trick for codebook utilization is from Peng et al. (2022).
- `zare-2026-stress-testing` — Zare 2026. Benchmarks LaBraM under frozen probing with negative
  controls and documents the channel-interpolation adaptation its design forces.
- `lin-2026-identity-trap` — Lin et al. 2026. Audits LaBraM's frozen representations and finds
  subject-identity variance dominant, with aperiodic 1/f as an identifiable carrier.
