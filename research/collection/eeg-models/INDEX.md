# EEG Representation Learning and Foundation Models — Collection Index

Strand A. Scope categories are those defined in `_briefs/strand-eeg-models.md`. One line per entry;
each entry's full record is its `card.md`.

**Collection status: PILOT, 6 of at least 18 entries.** This is a deliberately small first pass run
to expose process problems on 6 entries rather than on 79. Category coverage is therefore
incomplete: categories 1 and 3 have no entries yet, and the brief's acceptance criteria (at least 3
entries per category, at least 6 distinct model families) are not met. Nothing here is a synthesis
or a ranking; that is Phase 3.

## 1. Pretraining objectives

No entries yet. The brief's two seed entries on the theoretical-motivation line
(`muller-2024-transformers-cortical-waves`, `alexander-2019-cortical-waves`) were not in the pilot
set, and that line is capped at 2.

Objective descriptions do exist inside the pilot's category 2 cards — masked autoencoding on raw
signal in [reve-2025](./reve-2025/card.md), vector-quantized spectral tokenization in
[labram-2024](./labram-2024/card.md), masked time-frequency reconstruction in
[brainwave](./brainwave/card.md) — but they are carded under the architecture that implements them,
not as objective entries.

## 2. Architectures

- [reve-2025](./reve-2025/card.md): spatio-temporal transformer whose 4D Fourier positional encoding
  is computed from 3D electrode coordinates plus patch index, so an unseen montage needs no new
  parameters; masked autoencoder on 61,415 h (`relevance: high`, 2025)
- [labram-2024](./labram-2024/card.md): the canonical vector-quantized EEG model — a neural
  tokenizer trained to reconstruct patch Fourier amplitude and phase, then masked code prediction;
  spatial identity enters as a learned per-channel embedding table (`relevance: medium`, 2024)
- [brainwave](./brainwave/card.md): joint EEG and intracranial EEG pretraining, with a
  scale-alignment layer that fixes spectrogram window and hop as a ratio of a 1 s patch and so needs
  no resampling across sampling rates (`relevance: medium`, 2024)

## 3. Released checkpoints and reproducibility

No entries yet as a primary category. Checkpoint facts collected so far sit inside other cards:
parameter counts and input contracts in [reve-2025](./reve-2025/card.md) and
[labram-2024](./labram-2024/card.md), and a third-party account of what it actually takes to load six
released checkpoints — channel interpolation, resampling, and dead-channel padding — in
[zare-2026-stress-testing](./zare-2026-stress-testing/card.md). Licences for released weights are
unrecorded in every source read so far, which is itself a gap for this category.

## 4. Transfer and fine-tuning evidence

- [sirca-2026-peft-motor-imagery](./sirca-2026-peft-motor-imagery/card.md): DeepConvNet beat both
  partially fine-tuned and LoRA-adapted LaBraM on overall accuracy at every calibration size
  (54 subjects, leave-one-subject-out); LoRA gave more consistent per-subject gains at two orders of
  magnitude fewer trainable parameters. Paywalled, so the magnitude is not recorded
  (`relevance: medium`, 2026)
- [brainwave](./brainwave/card.md): cross-subject, cross-hospital, and cross-subtype transfer plus
  frozen-prototype few-shot classification — but every comparator is another pretrained model, so it
  carries no supervised-baseline evidence (`relevance: medium`, 2024)

Also bearing directly on this category from other groups: [reve-2025](./reve-2025/card.md) reports
the strand's cleanest pretraining ablation (+10.7 points on PhysioNet-MI for the same architecture
with versus without pretraining), and both category 5 entries are transfer evaluations whose results
happen to be negative.

## 5. Negative and null results

- [lin-2026-identity-trap](./lin-2026-identity-trap/card.md): frozen embeddings of LaBraM, CBraMod,
  and REVE are dominated by subject identity at 13–89x a random null in 12 of 12 pairs; erasing that
  axis *improves* label decoding; fine-tuning beats a frozen linear probe in only 2 of 12 pairs; a
  classical feature baseline (0.847) beats every pretrained tier on EEGMAT (`relevance: high`, 2026)
- [zare-2026-stress-testing](./zare-2026-stress-testing/card.md): a randomly-initialised encoder
  beats pretrained REVE on Korean dementia (0.659 vs 0.570 AUROC); dataset identity decodes from
  frozen embeddings at AUROC 1.000 while the diagnosis decodes at 0.528; classical features beat
  frozen REVE by at least 12.7 points under every tested condition (`relevance: medium`, 2026)
- [sirca-2026-peft-motor-imagery](./sirca-2026-peft-motor-imagery/card.md): cross-listed from
  category 4 — a supervised CNN outperforming an adapted foundation model is a null result for
  pretraining on this task (`relevance: medium`, 2026)

Also relevant: [labram-2024](./labram-2024/card.md) contains its own data-scaling null — its Base
model trained on 500 hours exceeds the same model trained on 2,500 hours on TUAB, and the authors
conclude "2,500 hours is not the answer".
