---
slug: brainwave
type: paper
strand: eeg-models
year: 2024
authors: [Yuan, Shen, Li, Yu, Wu, Tan, Yang]
venue: arXiv preprint 2402.10251 (v7, September 2025)
doi: 10.48550/arXiv.2402.10251
url: https://arxiv.org/abs/2402.10251
license: null
modalities: [scalp-eeg, intracranial-eeg, ieeg, clinical-eeg, variable-channel-count, variable-sampling-rate]
tags: [masked-modeling, time-frequency-reconstruction, transformer, channel-attention, scale-alignment, few-shot, prototypical-network, cross-hospital-transfer, seizure-detection, released-weights]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

Pretraining one masked-modeling encoder jointly on scalp EEG and intracranial EEG beats
pretraining on either alone, and a scale-alignment layer that fixes the spectrogram window and hop
as a *ratio* of a one-second patch removes the need to resample recordings to a common rate at all.

## Summary

BrainWave is a transformer encoder pretrained by masked reconstruction of time-frequency
representations on 40,907 hours (13.79 TB) of electrical brain recordings from 15,997 individuals
spanning infancy to over 90 years, covering both scalp EEG and intracranial EEG (iEEG). Its two
architectural moves are a scale-alignment layer and a channel-attention block. The scale-alignment
layer cuts each channel into 1-second patches and computes a Gaussian-window spectrogram per
patch, holding the window size and hop size at a fixed ratio of the patch length; because the ratio
rather than the absolute sample count is fixed, recordings at different sampling rates yield
time-frequency maps of the same time-axis length (the frequency axis length varies) and no
resampling is required. The transformer then encodes each channel independently, after which a
channel-attention step relates patches that co-occur in time across channels, making the model
channel-count agnostic. Evaluation covers a purpose-built benchmark of 15 datasets and 20 tasks
under cross-subject, cross-hospital, and cross-subtype splits, plus few-shot classification via
class prototypes with no parameter updates. Across 10 cross-subject datasets BrainWave reports an
average relative improvement of 11.93% AUROC and 17.59% balanced accuracy over the second-best
method in each task, and 93.82% AUROC on zero-shot FNUSA-to-Mayo-Clinic transfer.

## Relevance to the review

The scale-alignment layer is a second, distinct answer to the montage-and-rate problem that
`reve-2025` solves with coordinate-based positional encoding: BrainWave never resamples, whereas
REVE resamples everything to 200 Hz and instead generalizes over electrode *position*. For a
project that must decide what preprocessing STRUM data needs before it touches a checkpoint, the
contrast matters — BrainWave tolerates an arbitrary sampling rate but is agnostic about where
electrodes sit, so it carries no mechanism for exploiting or requiring a montage. Its
channel-count-agnostic channel attention means a channel set unseen in pretraining is structurally
admissible.

Two of its evaluation designs are directly relevant to this project's framing. The few-shot
protocol computes class prototypes from frozen pretrained representations with no parameter updates
at all, which is a cheaper probe than even a linear probe and a plausible first check on STRUM. The
cross-hospital and cross-subtype settings fine-tune on one dataset and apply the result to another
without adaptation, which is the closest analogue in this strand to asking whether a checkpoint
tuned elsewhere transfers to a new recording site.

The card's main caution for Phase 3 is recorded under limitations: every comparison in this paper
is against another pretrained model, so it cannot by itself support any claim about pretraining
versus a small supervised baseline.

## Notable details

- **Pretraining corpus and total hours**: 40,907 hours, 13.79 TB, 15,997 individuals, ages under 1
  to over 90. Split into 3,162,233,694 one-second signal patches — 1,739,447,411 EEG and
  1,422,786,283 iEEG — which the authors note are "relatively balanced" between the two
  modalities. Pretraining iEEG ran at 1000 Hz to 4096 Hz with 48 to 238 channels; pretraining EEG
  at 100 Hz to 1024 Hz with 1 to 64 channels.
- **Parameter count**: the paper does not report a total parameter count. It reports the encoder
  configuration instead: hidden size 768, intermediate size 2048, 10 layers, 16 attention heads,
  absolute positional encoding with maximum sequence length 61 (60 signal patches plus a [CLS]
  token). Pretraining used gradient accumulation over 16 forward/backward passes per update and
  took 100 hours.
- **Input contract**: 1-second patches, arbitrary sampling rate (no resampling step — the
  scale-alignment layer absorbs the rate difference by holding spectrogram window and hop as a
  ratio of patch length). A 50 Hz or 60 Hz notch filter is applied, chosen by local mains
  frequency. Maximum 60 patches, i.e. 60 seconds, per sequence. Channel count is unconstrained and
  handled by channel attention rather than by padding or interpolation. **The paper does not state a
  required channel ordering or a reference/montage convention**, and does not report any electrode
  position information being used, so the model appears to be position-blind.
- **Most informative transfer number, with baseline**: on 10 cross-subject clinical datasets,
  average relative improvement of 11.93% AUROC and 17.59% BACC over the second-best model per task,
  where the comparison set is LaBraM, BrainBERT, and MOMENT. The largest single gain is
  schizophrenia diagnosis (Schizophrenia-28): +37.44% AUROC and +41.59% BACC over the best
  comparison model. Seizure detection on CHB-MIT: +26.18% over second best. Significance
  (p < 0.001) on 9 of the 10 datasets. **The baseline in every one of these numbers is another
  pretrained foundation model, not a supervised-from-scratch model** — see limitations.
- **Few-shot, frozen**: class prototypes computed from frozen representations with no parameter
  updates beat LaBraM by 2.27% average AUROC, BrainBERT by 26.40%, and MOMENT by 14.87%. BrainWave
  also shows lower seed-to-seed fluctuation than LaBraM (5.74% versus 6.06%).
- **Joint-pretraining ablation**: BrainWave outperforms both single-modality variants
  (BrainWave-EEG, BrainWave-iEEG), including by 4.98% AUROC on few-shot classification, which is
  the paper's evidence that EEG and iEEG pretraining are synergistic rather than merely additive.
- Evaluation datasets are 19-channel 10-20 at 250 Hz or 256 Hz in most cases, with segment lengths
  of 3, 10, and 60 seconds across tasks.

## Open questions / limitations

- **No supervised-from-scratch baseline anywhere in the paper.** The comparison set is LaBraM,
  BrainBERT, and MOMENT — all pretrained models. The text of `source.md` contains no occurrence of
  EEGNet, ShallowConvNet, SPaRCNet, BIOT, "from scratch", or the word "baseline". Every headline
  number therefore establishes only that BrainWave is the best of four pretrained models on these
  tasks, not that pretraining beats training small and supervised. For this project's comparison 1
  versus comparison 2, this card supplies an architecture and an input contract but no evidence.
- All improvements are reported as *relative* percentages over a per-task second-best model that
  changes between tasks, so the absolute AUROCs and the identity of the comparator have to be read
  off the figures rather than a table. The extraction in `source.md` renders those figures as
  unusable character soup, so absolute per-task numbers are not recoverable from the committed text.
- Parameter count is absent, which makes any claim about parameter efficiency or about scale
  relative to `labram-2024` (5.8M/46M/369M) or `reve-2025` (12M/69M/408M) unsupported from this
  source. Independently, `zare-2026-stress-testing` does not include BrainWave in its six-model
  benchmark, so no third party has published its parameter count either.
- The model is position-blind as far as the paper states. Nothing in the described architecture
  uses electrode coordinates, so its channel-count agnosticism does not imply montage
  generalization in the sense `reve-2025` demonstrates. Whether feeding a 32-channel cognitive
  montage to a model whose EEG pretraining was mostly clinical is sound is untested here.
- Corpus composition is reported as a total and a modality split, not per source dataset with
  licences, so overlap between the 40,907 pretraining hours and the evaluation datasets cannot be
  audited from the paper. CHB-MIT appears as an evaluation dataset; whether it also appears in
  pretraining is not stated. (`zare-2026-stress-testing` flags exactly this class of in-domain
  contamination for BIOT.)
- The identifier situation is worth flagging for Phase 3: the strand brief lists BrainWave with no
  resolvable identifier, and the arXiv record is now at v7 (September 2025) with a 2024 first
  posting. The card year is the first-posting year, but the text summarized here is v7, so a reader
  comparing against the v1 abstract will find different numbers.

## Citations

Primary: `brainwave`

- `labram-2024` — Jiang et al., ICLR 2024. The strongest of the three comparison models and the
  only one BrainWave beats by a narrow margin in few-shot (2.27% AUROC).
- Wang et al., BrainBERT — iEEG-oriented pretrained model; the weakest few-shot comparator
  (BrainWave +26.40% AUROC), which the paper attributes to its representations.
- Goswami et al., MOMENT — general-purpose time-series foundation model pretrained on 13 domains
  and 1.23 billion timestamps; included as a non-neural-specific control.
- `reve-2025` — El Ouahidi et al. REVE's own text cites BrainWave (as Yuan et al. 2024a) as the
  largest prior pretraining effort at ~40,000 hours, noting it "primarily relied on intracranial
  EEG rather than non-invasive EEG".
- `zare-2026-stress-testing` — Zare 2026. Benchmarks six EEG foundation models under negative
  controls but does not include BrainWave, so its cautions are not directly tested on this model.
