---
slug: eegconformer-2023
type: paper
strand: eeg-models
year: 2023
authors: [Song, Zheng, Liu, Gao]
venue: IEEE Transactions on Neural Systems and Rehabilitation Engineering
doi: 10.1109/TNSRE.2022.3230250
url: https://doi.org/10.1109/TNSRE.2022.3230250
license: CC BY 4.0
modalities: [scalp-eeg, motor-imagery, emotion-eeg, bipolar-derivation, within-subject]
tags: [convolutional-transformer, supervised-from-scratch, no-pretraining, transfer-baseline, class-activation-mapping, segmentation-and-reconstruction-augmentation, subject-dependent, bci-competition-iv, seed]
relevance: high
imported_from: null
added: 2026-08-01

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: partial
---

## TL;DR

A shallow convolutional front end followed by six self-attention layers, trained from scratch on
one subject at a time with no pretraining at all, and the paper argues explicitly that pretraining
is unnecessary here because calibration data is scarce — which is why three of the four benchmark
suites in the sibling strand use it as the supervised reference point that pretrained checkpoints
must beat.

## Summary

EEG Conformer places a ShallowConvNet-style convolution module — a temporal convolution with 40
kernels of size (1, 25), a spatial convolution of size (ch, 1) across all electrodes, batch
normalisation, ELU, and average pooling of size (1, 75) with stride (1, 15) — in front of a
six-layer, ten-head self-attention stack and a two-layer fully connected classifier. The pooled
feature vector at each remaining time position becomes one token, so self-attention runs over time
after the spatial dimension has already been collapsed. Preprocessing is deliberately minimal: a
sixth-order Chebyshev band-pass filter and a z-score standardisation whose mean and variance are
computed on the training data and reused unchanged at test time. Training uses segmentation-and-
reconstruction augmentation, which splits same-class training trials into eight segments and
recombines them in the original time order. Evaluation is subject-dependent on three datasets: BCI
Competition IV 2a (4-class motor imagery, session 1 train / session 2 test), IV 2b (2-class, first
three sessions train / last two test), and SEED (3-class emotion, five-fold cross-validation). The
paper also contributes Class Activation Topography, a visualisation that multiplies normalised EEG
topography by gradient-weighted class activation, and uses it to show event-related
desynchronisation and synchronisation over motor cortex.

## Relevance to the review

This entry is here for two roles at once. As an architecture it is a convolutional-plus-attention
hybrid, and as a reference point it is the supervised baseline that the strand's transfer evidence
is measured against, which makes it a category 5 anchor as much as a category 2 entry. Three of the
four suites in `datasets-benchmarks` use it in exactly that role, and their results are the reason
it matters to this project's comparison 1:

- `datasets-benchmarks/omnieeg-bench`, on 54 datasets: under full fine-tuning, seven of ten
  foundation models beat EEGConformer (average rank 7.25) and nine beat EEGNet (8.24). Under the
  suite's primary frozen-backbone linear-probing protocol, only five of ten beat EEGConformer
  (average rank 6.66) and five fall behind it.
- `datasets-benchmarks/adabrain-bench`, on 13 datasets: Conformer is the best of four supervised
  baselines under cross-subject transfer at a macro-average of 58.12 against LaBraM 64.61 and
  CBraMod 62.66; under multi-subject adaptation it reaches 53.66, above BIOT (51.96) and EEGPT
  (51.67).
- `datasets-benchmarks/neuralbench`: EEGConformer sits at mean normalised rank 0.45, ninth overall,
  above EEGNet (0.47) and the pretrained BENDR (0.57) and BIOT (0.64), and below CTNet (0.32) and
  the three leading foundation models.

The gap between the fine-tuned and frozen columns of the first of those is the single most useful
fact in this card for the project: whether a pretrained checkpoint beats a small supervised model at
all depends on which adaptation regime is used, and this is the model that fixes where that line
falls.

One caution the suites do not state and this card must. EEG Conformer was designed, trained and
validated **within subject**. Its own limitations section says the method "is trained and validated
on each individual, and cannot utilize useful information from other subjects", and all three of its
datasets are split by session or by fold within a subject, never across subjects. The suites deploy
it as a cross-subject baseline. That is a legitimate use of an architecture but it is not the
setting the original numbers were obtained in, so the paper's own accuracies and the suites'
rankings are not measuring the same thing.

## Notable details

- **Pretraining corpus and total hours**: **none — the model is supervised from scratch, and this is
  a deliberate design choice, not an omission.** Section IV-E states: "In image processing,
  Transformer models often need a large amount of data for pre-training to achieve good results in
  downstream tasks. However, pre-training is not used in EEG Conformer, due to the limited data for
  calibration." Total pretraining hours are therefore zero.
- **Parameter count**: **not reported as a number in the text.** Fig. 4 plots parameter count
  against self-attention depth on a right-hand axis running 0.60 to 1.00 × 10⁶, from which the
  depth-6 configuration actually used reads at roughly 0.79 × 10⁶ for Dataset I and 0.76 × 10⁶ for
  Dataset II. The only parameter statement in prose is relative: "the parameters of the Conformer
  increase by 17.6% compared to removing the self-attention module", and the authors note the
  fully connected classifier "contributes a large number of parameters".
  `datasets-benchmarks/neuralbench` independently tabulates its EEGConformer implementation at 277K,
  which is the only absolute figure available and comes from a third party's configuration, not from
  this paper.
- **Input contract**: there is no pretrained checkpoint, so there is no fixed contract to satisfy —
  channel count enters the architecture as the spatial-convolution kernel height (ch, 1) and is set
  at build time, and window length changes the flattened classifier width. What the paper fixes is
  preprocessing: sixth-order Chebyshev band-pass, and z-score standardisation with statistics
  computed on the training split and applied to test. Per dataset: BCI IV 2a, 22 electrodes at
  250 Hz, seconds [2, 6] of each trial, band-pass 4–40 Hz; BCI IV 2b, three bipolar channels (C3,
  Cz, C4) at 250 Hz, seconds [3, 7], band-pass 4–40 Hz; SEED, 62 electrodes recorded at 1000 Hz and
  downsampled to 200 Hz, non-overlapping 1-second windows, band-pass 4–47 Hz.
- **Most informative transfer number, with baseline**: this paper reports no transfer — it has
  nothing to transfer from. Its role as a baseline supplies the equivalent number: on BCI
  Competition IV 2a it reaches 78.66% average accuracy (κ = 0.7155) against EEGNet's 74.50%
  (κ = 0.6600) and ConvNet's 72.53% (κ = 0.6337) under the same subject-dependent protocol — so it
  is 4.2 points above the small supervised baseline that pretrained models are most often compared
  to. On BCI IV 2b it reaches 84.63% against EEGNet 80.48% and ConvNet 79.37%; on SEED, 95.30%
  (κ = 0.9295) against RGNN 94.24% and SVM 86.08%.
- **Ablation**: removing the self-attention module costs 6.02 average points on Dataset I
  (p < 0.01), ranging from 3.12 points on subject 3 to 8.68 on subject 6. Removing the
  segmentation-and-reconstruction augmentation costs 3.75 points, with the largest effect on the two
  worst-performing subjects (4.86 and 5.56 points) and the smallest on the best (1.04).
- **Insensitivity to attention hyperparameters**: across self-attention depths 1 to 15 the best and
  worst average accuracies differ by 1.24 points (not significant, p > 0.05); across head counts 1
  to 40 the range is 1.43 points on Dataset I and 1.02 on Dataset II. What does matter is the
  pooling kernel, i.e. the token size: raising it from 15 to 45 gains 13.08 points (p < 0.01), after
  which the curve flattens. Depth 0 to 1 is the one significant depth step.
- Code is released at `https://github.com/eeyhsong/EEG-Conformer`. Training cost is reported as
  0.27 seconds per epoch on a single GeForce 3090.

## Open questions / limitations

- Subject-dependent throughout, by the authors' own statement, and the model "cannot utilize useful
  information from other subjects". Every number in the paper is within-subject. Any cross-subject
  ranking that uses this architecture — which is how all three benchmark suites use it — is
  measuring a re-implementation in a setting the paper did not evaluate.
- No absolute parameter count is published, which is a real gap for a model whose main function in
  the literature is to be the cheap comparison point. The figure-read value (~0.79M) and
  NeuralBench's 277K differ by roughly threefold, and nothing in either source explains the gap;
  most likely they are different configurations of the same architecture, but the paper gives no
  way to check.
- The authors flag that they validate only oscillatory paradigms (motor imagery, emotion) and not
  event-related-potential data, and that the parameter scale "is not small" for a model of this kind.
- The segmentation-and-reconstruction augmentation recombines segments drawn from the same class
  across trials. Whether the augmented trials leak information across the train/test boundary is not
  examined; the augmentation is applied to training samples only, but the paper does not say whether
  the segments are drawn within trial or across trials of the same class within the training split.
- The visualisation contribution is qualitative. Class Activation Topography is shown to recover
  contralateral activation and ipsilateral inhibition "in several subjects, such as S1, S7 and S8",
  with no quantitative measure over the full cohort.
- Publication year is ambiguous in the source. The article carries "Date of publication 16 December
  2022; date of current version 2 February 2023" and appears in volume 31 (2023), pages 710–719;
  Crossref records it as 2023. The sibling `datasets-benchmarks` cards and NeuralBench cite it as
  "Song et al., 2022". This card and the bib entry use 2023, the version-of-record year.

## Citations

Primary: `eegconformer-2023`

- `bendr-2021` — Kostas et al. Cited here (reference [34]) as the pretraining-and-fine-tuning
  approach EEG Conformer positions itself against by declining to pretrain.
- Schirrmeister et al. 2017, ConvNet / ShallowConvNet — the convolution module is explicitly derived
  from it, and it is a baseline in both motor-imagery tables.
- Lawhern et al. 2018, EEGNet — the compact convolutional baseline this model is most often compared
  to, and the one it beats by 4.2 points on BCI IV 2a.
- `datasets-benchmarks/omnieeg-bench` — Lu et al. 2026. Uses EEGConformer as the task-specific
  reference point whose average rank separates the fine-tuned from the frozen regime.
- `datasets-benchmarks/adabrain-bench` — Wu et al. 2025. Uses Conformer as the strongest of four
  supervised baselines under cross-subject transfer.
