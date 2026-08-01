---
slug: eegpt-2024
type: paper
strand: eeg-models
year: 2024
authors: [Wang, Liu, He, Xu, Ma, Li]
venue: Advances in Neural Information Processing Systems 37 (NeurIPS 2024)
doi: 10.52202/079017-1239
url: https://proceedings.neurips.cc/paper_files/paper/2024/hash/4540d267eeec4e5dbd9dae9448f0b739-Abstract-Conference.html
license: null
modalities: [scalp-eeg, 58-electrode-superset, motor-imagery, ssvep, erp, sleep-eeg]
tags: [masked-modeling, dual-self-supervised, spatio-temporal-alignment, momentum-encoder, summary-tokens, adaptive-spatial-filter, linear-probing-only, released-weights, released-code, reporting-inconsistency]
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

A masked EEG model trained with a second loss that aligns the encoder's own representations
against a momentum encoder rather than against the raw signal, evaluated *only* under linear
probing with a 1x1 convolution to remap channels — and reported with three mutually inconsistent
parameter counts across its abstract, its results tables, and its scaling table.

## Summary

EEGPT is a ViT-style encoder trained with two losses at once. The reconstruction loss recovers
masked patches, and an *alignment* loss makes the predictor's output for masked positions match
the output of a momentum encoder applied to the unmasked signal. The authors' argument for the
second loss is that reconstructing raw EEG optimizes toward a low-SNR target, so alignment against
a learned representation gives a better-conditioned objective; the ablation supports this, with
removal of the alignment loss costing 6 to 9 percent downstream while barely changing the
reconstruction loss. The encoder emits S learnable summary tokens per time segment, in the manner
of a class token, and downstream use is deliberately restricted to linear probing: the backbone is
frozen and only a 1x1 convolutional adaptive spatial filter (which remaps an arbitrary channel set
onto the model's 58-electrode superset) and a linear head are trained. Pretraining uses five
public datasets spanning motor imagery, motor execution, SSVEP and emotion; evaluation covers
seven downstream datasets including TUAB and TUEV under BIOT's splits and BCIC-2A/2B, Sleep-EDFx,
KaggleERN and PhysioP300 under BENDR's leave-one-subject-out protocol.

## Relevance to the review

Two features make EEGPT directly relevant to this project's design.

The first is that linear probing is not one option among several here — it is the only evaluation
the paper reports. The authors justify it explicitly as avoiding "the overfitting problem when a
large parameter model is fine-tuned using a limited number of samples", which is precisely STRUM's
situation, and they argue that because the trainable module is so simple, "the performance is
solely determined by the encoder". That makes EEGPT the strand's cleanest case of a checkpoint
designed to be used frozen.

The second is the channel-adaptation mechanism, which is neither a name lookup nor a coordinate
function but a learned 1x1 convolution — an adaptive spatial filter trained downstream to map the
dataset's channels onto the model's fixed 58-electrode input. This costs a small number of
trainable parameters per new dataset but requires no pretrained row per electrode, so an unfamiliar
montage is handled by learning a linear remap rather than by having seen the electrode.

Against this, the paper's reporting of its own model size is unreliable (see limitations), which
directly affects whether its efficiency claim can be quoted.

## Notable details

- **Pretraining corpus and total hours**: five public datasets — PhysioMI (109 subjects, motor
  imagery and execution), HGD (14, motor imagery), TSU (35, SSVEP), SEED (15, emotion), M3CV
  (106, multi-paradigm) — for 279 subjects in total. **Total hours: `not reported`**; the strings
  "hour" and "Hour" do not occur anywhere in the paper, which describes the corpus only by dataset
  and subject count. Ten percent of each pretraining dataset was held out for validation.
- **Parameter count**: the paper gives three incompatible answers, so the card records all of
  them. (i) The abstract and the contributions list say "a novel 10-million-parameter pretrained
  transformer model", and the conclusion says "over 10 million parameters". (ii) The TUAB and TUEV
  results tables label the evaluated models "Ours-Tiny 4.7M" and "Ours 25M". (iii) The
  model-variant table lists eight configurations — 0.4M, 0.5M, 1.6M, 6.4M, 19M, 25M, 76M, 101M —
  of which the largest ("large": embedding dimension 512, 8/8/8 layers, 4 summary tokens, 101M) is
  the one the text says was used: "we used the optimal large model for testing on all downstream
  tasks". The variant table's BCIC-2A balanced accuracy for the large model, 58.46, matches the
  0.5846 reported for "Ours" in the cross-model comparison table, so **the model behind the
  headline downstream results is the 101M one**, and that is what this card treats as the
  parameter count. No configuration anywhere in the paper has 10M or 4.7M parameters.
- **Input contract**: 256 Hz after resampling; 4-second windows (T = 1024 samples); patches of
  64 samples, i.e. 250 ms; 58 electrodes (M = 58) as the model's channel superset; average
  re-referencing; amplitude scaled to mV; 0–38 Hz band-pass applied to the motor-imagery
  downstream datasets only. An arbitrary downstream channel set is mapped onto the 58 electrodes
  by a trainable 1x1 convolution. Masking during pretraining is 50 percent of time patches and
  80 percent of channel patches.
- **Most informative transfer number, with baseline**: on TUEV 6-class event classification,
  EEGPT reaches 0.6232 ± 0.0114 balanced accuracy against the best small supervised baseline,
  ContraWR at 1.6M parameters, at 0.4384 ± 0.0349 — an 18.5-point margin — with SPaRCNet (0.79M)
  at 0.4161 and ST-Transformer (3.5M) at 0.3984. The same comparison on TUAB is far less
  favourable: EEGPT reaches 0.7983 ± 0.0030 against ST-Transformer at 0.7966 ± 0.0023, a margin of
  0.17 points and well inside the standard deviations. The pretrained model's advantage over small
  supervised models is therefore task-dependent by an order of magnitude in this paper's own
  tables.
- **Comparison against other pretrained models under linear probing**: on BCIC-2A, EEGPT reaches
  0.5846 balanced accuracy against LaBraM 0.5613, BENDR 0.4899 and BIOT 0.4590. On KaggleERN,
  0.5837 against BENDR 0.5672, LaBraM 0.5439 and BIOT 0.5118. On Sleep-EDFx, 0.6917 against LaBraM
  0.6771. The authors note the BENDR comparison is not like-for-like in EEGPT's disfavour: "BENDR
  used full model fine-tuning while our model only fine-tuned an additional linear layer".
- **Alignment-loss ablation** (on the large model): removing the alignment loss leaves the
  reconstruction loss "comparable" but costs 6 to 9 percent downstream (BCIC-2A balanced accuracy
  falls from 0.5846 to 0.5287, BCIC-2B AUROC from 0.8059 to 0.7264, KaggleERN AUROC from 0.6621 to
  0.5752). Removing layer normalization on the reconstruction targets *lowers* the pretraining
  loss while costing 1 to 7 percent downstream. Both are instances of pretraining loss failing to
  track downstream performance.
- **Scaling**: balanced accuracy on BCIC-2A rises monotonically with model size across the eight
  variants, 49.19 percent at 0.4M to 58.46 percent at 101M, with one inversion — base3 (76M,
  512-dim, 6 layers, 1 summary token) at 54.47 falls below base2 (25M, 256-dim, 8 layers, 4
  summary tokens) at 56.48, so summary-token count and depth matter more than raw size at that
  scale.
- **Splits**: TUAB and TUEV follow BIOT's splits exactly, for comparability. The other five
  datasets follow BENDR's configuration with leave-one-subject-out, except KaggleERN (4-fold
  cross-validation with 10 test subjects) and Sleep-EDFx (10-fold, 6:2:2). Each experiment
  repeated three times.
- **Release**: code at https://github.com/BINE022/EEGPT. Trained on 8 Nvidia 3090 GPUs, 200
  epochs, batch size 64, AdamW with OneCycle scheduling, 16-bit mixed precision. No licence is
  stated for the released weights.

## Open questions / limitations

- **The model size is reported three ways and they cannot all be true.** 10M in the abstract,
  contributions and conclusion; 4.7M and 25M in the results tables; 101M for the "large" variant
  the text says was used everywhere, whose scaling-table accuracy matches the reported downstream
  number. Following the standing rule of preferring tables, and resolving the conflict *between*
  tables by matching the reported accuracy, this card uses 101M — but the discrepancy is
  unresolved in the source, and any efficiency claim derived from the abstract's 10M figure is
  unsupported.
- Relatedly, the TUAB and TUEV tables report "Ours 25M" while the evaluation section says the
  large model was used for all downstream tasks. Either those two tables used a different model
  from the rest, or the size labels are wrong. The paper does not say which.
- Only linear probing is reported. There is no fine-tuned EEGPT number anywhere, so the paper
  cannot say how much of the gap to fully fine-tuned baselines is attributable to the frozen
  protocol. The authors present this as a strength; it is also a missing measurement.
- The pretraining corpus is small and task-skewed: 279 subjects across five datasets, four of
  which are motor imagery, motor execution, SSVEP or emotion. Downstream gains are largest on
  TUEV, a clinical event dataset unlike anything in pretraining, and smallest on TUAB, also
  clinical. No explanation is offered for that pattern.
- The 58-electrode superset is presented in a figure and never listed in text, so the exact
  electrode set the adaptive spatial filter maps onto cannot be read from the paper's prose.
- The paper reports its own appendix comparison in which LaBraM (5.8M) reaches 0.8140 balanced
  accuracy on TUAB against EEGPT's 0.7983, i.e. a much smaller pretrained model beating it on that
  task. This appears in an appendix table and is not discussed in the main text.
- Improvements are quoted throughout as percentages relative to a comparator ("improves the
  balanced accuracy by 9.5%") without stating whether these are absolute or relative points. On
  TUEV, 0.6232 versus BIOT's 0.5281 is 9.5 absolute points, so the convention appears to be
  absolute, but it is never stated.

## Citations

Primary: `eegpt-2024`

- `biot-2023` — supplies the TUAB and TUEV splits and baseline set EEGPT reuses, and is one of
  the four pretrained comparators.
- `bendr-2021` — supplies the leave-one-subject-out configuration for the five non-TUH datasets,
  and is the comparator the authors flag as advantaged by full fine-tuning.
- `labram-2024` — the strongest pretrained comparator under linear probing, and the model that
  beats EEGPT on TUAB in the appendix.
- Dosovitskiy et al., ViT (2021) — the architecture the encoder, predictor and reconstructor
  follow.
- Grill et al., BYOL / momentum-encoder line — the structure behind the alignment loss, which
  targets a momentum encoder's output rather than the raw signal.
