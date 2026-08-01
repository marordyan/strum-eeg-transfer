---
slug: femba-2025
type: paper
strand: eeg-models
year: 2025
authors: [Tegon, Ingolfsson, Wang, Benini, Li]
venue: 2025 47th Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)
doi: 10.1109/EMBC58623.2025.11252697
url: https://arxiv.org/abs/2502.06438
license: null
modalities: [scalp-eeg, clinical-eeg, bipolar-derivation, tuh-corpus]
tags: [state-space-model, mamba, bidirectional, masked-reconstruction, patch-embedding, edge-deployment, full-fine-tuning, abnormal-eeg-detection, artifact-detection, model-scaling]
relevance: medium
imported_from: null
added: 2026-08-01

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

Replacing the transformer encoder with a stack of bidirectional Mamba blocks makes the encoder's
cost linear rather than quadratic in sequence length, and the paper's claim is that this costs
almost nothing in accuracy — its largest model lands within 0.8 points of the best transformer
result on abnormal-EEG detection at roughly 70% fewer floating-point operations.

## Summary

FEMBA (Foundational EEG Mamba + Bidirectional Architecture) pretrains a bidirectional state-space
encoder on the Temple University Hospital EEG corpus with a masked-patch reconstruction objective.
Input is tokenised by a 2D convolution over patches spanning 4 channels × 32 samples, 60% of the
resulting patches are zeroed, and a two-convolution decoder plus linear projection reconstructs them
under a Smooth L1 loss computed only over masked patches. The encoder stacks bidirectional Mamba
blocks in which a forward and a temporally reversed backward pass are summed; the hidden state size
is fixed at 80 across all four sizes, which differ only in block count and embedding dimension.
Downstream, the decoder is discarded and the encoder is fine-tuned end to end with either a small
fully-connected head (~0.5M parameters) or one extra Mamba block before the linear layer (up to
0.7M). Evaluation covers three Temple University subsets: abnormal-versus-normal (TUAB), artifact
detection under four labelling protocols (TUAR), and slowing-event classification (TUSL). The
headline results are 81.82% balanced accuracy on TUAB for FEMBA-Huge and 0.949 AUROC on binary TUAR
for FEMBA-Base, both reported alongside floating-point-operation and peak-memory counts that are
the paper's actual argument.

## Relevance to the review

This is the strand's only entry whose backbone is a state-space model rather than attention, and its
value here is the efficiency-versus-accuracy trade curve rather than any transfer claim: the paper
reports parameter count, floating-point operations and peak memory for every variant alongside
accuracy, which is the shape of evidence needed to decide whether a pretrained encoder is affordable
at all for a small project. FEMBA-Tiny at 7.8 million parameters and 1.31 billion floating-point
operations is the smallest pretrained checkpoint carded in this strand that still reports a
state-of-the-art result on one of its tasks.

Its transfer evidence is narrow in a way that matters. All three downstream tasks are clinical
Temple University subsets drawn from the same corpus the model was pretrained on, with only the
subject overlap removed. There is no cognitive, motor-imagery or naturalistic-stimulus task, so the
paper supplies no evidence about the regime STRUM sits in. `datasets-benchmarks/omnieeg-bench`
supplies the missing breadth from outside: re-running FEMBA on 54 datasets, it places FEMBA third
under full fine-tuning at an average rank of 5.42, behind CBraMod (4.51) and LaBraM (4.88) — a
substantially weaker position than FEMBA's own three-task results suggest, though the two are not
measured under the same protocol. That same suite records FEMBA as one of the checkpoints that
"require ... predefined bipolar derivations", which is an input-contract constraint the FEMBA paper
itself never states.

## Notable details

- **Pretraining corpus and total hours**: the Temple University Hospital EEG corpus (TUEG), "over
  21,000 hours" of unlabelled clinical EEG. The subject count is self-contradictory: the
  contributions list says "more than 5,000 participants" while Table I gives TUEG 14,987 subjects
  and Section II-A says TUEG contains "more than 14,000 patients". Subjects appearing in TUAB, TUAR
  or TUSL were filtered out of the pretraining set to prevent leakage, so the effective pretraining
  subject count is below whichever figure is meant and is not stated.
- **Parameter count**: Tiny 7.8M, Base 47.7M, Large 77.8M, Huge 386M. The Huge figure is also given
  as 389M in the contributions list; 386M appears in Section III-A and in Tables II and III and is
  the value carded. Configurations are (blocks, embedding dim): Tiny (2, 35), Base (12, 35), Large
  (4, 79), Huge (20, 79), with hidden state size 80 throughout. Floating-point operations:
  1.31B / 7.52B / 12.48B / 58.74B; peak memory at batch size 8: 53.36 / 240.50 / 548.71 / 1886.17 MB.
- **Input contract**: the model consumes a raw tensor of C channels × T samples, illustrated in
  Fig. 1 as C = 22, T = 1280, patched at 4 channels × 32 samples with learnable positional
  embeddings. Normalisation is quartile-based: each channel is scaled by its interquartile range.
  **Sampling rate: not reported** — the string "Hz" does not occur anywhere in the paper, so the
  duration of a 1280-sample window cannot be derived from the source, and neither band-pass nor
  notch filtering is described. Referencing is not stated either; `datasets-benchmarks/omnieeg-bench`
  records FEMBA as requiring predefined bipolar derivations, which is consistent with the 22-channel
  Temple University convention but is that suite's statement, not this paper's.
- **Most informative transfer number, with baseline**: on TUAB, FEMBA-Huge reaches 81.82% balanced
  accuracy against 79.66% for ST-Transformer, the best of the five supervised models in the same
  table — a 2.16-point gain at 386M parameters against 3.2M, roughly 120 times the size. Every FEMBA
  variant beats every supervised model on this task, but FEMBA-Base (47.7M) reaches 81.05%, so
  most of the pretrained advantage over the supervised baselines is present at one eighth the size.
  On TUAR under the multiclass protocol the margin is far larger: FEMBA-Tiny at 7.8M reaches 0.918
  AUROC against 0.752 for EEGNet.
- **A counter-result in the paper's own tables**: on TUSL, FEMBA-Base leads on AUROC (0.731 against
  EEGFormer-Base 0.713 and EEG-GNN 0.721) but its area under the precision-recall curve, 0.289,
  trails EEGFormer-Large's 0.389 by 10 points and also trails the supervised EEGNet (0.351), TCN
  (0.344), EEG-GNN (0.381) and GraphS4mer (0.359). The paper attributes this to class imbalance. So
  on the strand's ranking metric of choice the direction of the result depends on which metric is
  read.
- **Split protocol**: TUAB uses its predefined train-test split. TUAR and TUSL have no official test
  split, and the authors "adopt an 80/10/10 randomized training/validation/test split" — described at
  sample level with no statement that it is subject-wise. Under `brookshire-2024-data-leakage` that
  is the split geometry that inflates results, and two of the three headline tasks use it.
- **Fine-tuning budget**: full end-to-end fine-tuning of encoder plus classifier, Adam at 1e-4 with
  cosine decay and early stopping on validation loss, layer-wise learning-rate decay of 0.75 during
  pretraining. No linear-probing or frozen-backbone result is reported anywhere in the paper.
- Code is released at `https://github.com/pulp-bio/BioFoundation`. The paper does not state whether
  the pretrained weights are released or under what licence.

## Open questions / limitations

- The three downstream tasks are all Temple University corpora, so the evaluation measures transfer
  within the pretraining distribution with subjects removed, not transfer to a new recording setup.
  The paper's own future-work section concedes this, naming sleep staging and BCI as untested and
  neonatal EEG as a known domain shift.
- No sampling rate, filtering or referencing specification appears in the paper. Anyone wanting to
  feed the checkpoint data outside TUEG's conventions has to recover the contract from the released
  code, not from the publication.
- The conclusion states experiments "across multiple downstream tasks (abnormal EEG detection,
  artifact recognition, slowing event classification, and neonatal seizure detection)". No neonatal
  seizure result appears anywhere in the paper, and the abstract says three downstream tasks. Carded
  as three.
- Table I gives TUSL 38 subjects while Section II-B says the TUSL task "consists of 1000 subjects".
  Both cannot be right; Table I is the value carded, following the standing rule to prefer tables
  over body prose.
- The efficiency comparison against EEGFormer is approximate by the authors' own statement: EEGFormer
  has no released code, so its floating-point operations and memory "are approximated based on the
  limited details available in the literature". The 27× claim for FEMBA-Tiny rests on that estimate.
- The scaling result is weak and the paper does not say so: from Base (47.7M) to Huge (386M),
  TUAB balanced accuracy rises 0.77 points for eight times the parameters and eight times the
  floating-point operations, and on TUAR the Tiny model beats both larger variants under two of the
  four protocols.
- No dyadic task, no peripheral physiology, and no cross-subject protocol distinct from the corpus's
  own splits.

## Citations

Primary: `femba-2025`

- `labram-2024` — Jiang et al., ICLR 2024. The transformer benchmark FEMBA measures itself against
  on TUAB, and the source of the LaBraM-Base/Large/Huge numbers in its Table II.
- `bendr-2021` — Kostas et al. Cited as the contrastive predecessor that "faced scalability issues",
  and included in the TUAB table at 0.39M parameters.
- `biot-2023` — Yang et al. One of the self-supervised comparison points on TUAB.
- `luna-2025` — Döner et al., NeurIPS 2025. Same laboratory and code base; reuses FEMBA's TUAB and
  TUAR tables as baselines and reports beating FEMBA-Large on TUAR and TUSL.
- `datasets-benchmarks/omnieeg-bench` — Lu et al. 2026. Third-party evaluation placing FEMBA third
  under full fine-tuning across 54 datasets.
