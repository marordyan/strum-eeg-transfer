---
slug: lee-2025-lbms-capable-yet
type: paper
strand: eeg-models
year: 2025
authors: [Lee, Barmpas, Panagakis, Adamos, Laskaris, Zafeiriou]
venue: arXiv preprint 2507.01196
doi: null
url: https://arxiv.org/abs/2507.01196
license: CC BY 4.0 (arXiv posting)
modalities: [scalp-eeg, motor-imagery, erp, working-memory, sleep-eeg, eyes-open-closed]
tags: [negative-result, null-result, foundation-model-critique, parameter-efficiency, lora, frozen-backbone, subject-independent-cv, eegnet-baseline, eeg-inception-baseline, neurogpt, labram]
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

Across five BCI benchmarks under subject-independent cross-validation, the best fine-tuned
foundation model averages 0.745 accuracy against EEGNet's 0.731 — a 1.4-point gain bought with
2,394 versus 5.85 million to 78.5 million parameters — and with the backbone frozen the same
models fall 8 to 10 points *below* the small supervised baselines.

## Summary

Lee and colleagues fine-tune two Large Brainwave Foundation Models (LaBraM base, and NeuroGPT in
both full-model and encoder-only configurations) on five benchmark tasks — motor imagery from High
Gamma, an ERP paradigm from Korea University, a working-memory dataset, Sleep-EDF sleep staging,
and eyes-open versus eyes-closed from PhysioNet — and compare them against two small supervised
architectures, EEGNet and EEG-Inception, trained from scratch under the identical protocol: 20
epochs, 10-fold subject-independent cross-validation with no participant in both training and
validation. The headline comparison is a mean accuracy table with parameter counts alongside. The
paper then runs two further studies: freezing everything but the classification head, and applying
LoRA at ranks 1 to 16 to every combination of attention, fully-connected and convolutional
modules. Its conclusion is that the gains are real but marginal, that they do not survive freezing
the backbone, and that the attention layers matter less than the convolutional front end.

## Relevance to the review

This is the paper that most directly measures the question this strand exists to answer: under
what conditions does EEG pretraining beat a small supervised baseline. Its answer, on five tasks
under a clean subject-independent protocol, is "by about one point, sometimes not at all, and
never when frozen".

Three specifics matter for this project's design. First, the protocol is the one STRUM needs:
10-fold subject-independent cross-validation, explicitly constructed "such that no participant
would be present in both the training and validation sets". Second, the parameter accounting is
explicit and includes classification heads, so the efficiency comparison is quotable — EEGNet at
2,394 trainable parameters reaches 0.731 mean accuracy while NeuroGPT's full model at 78,536,146
reaches 0.736. Third, the frozen-backbone result bears on the project's third comparison: if the
plan is to add peripheral physiology on top of a frozen EEG embedding, this paper reports that
frozen LBM embeddings are 8 to 10 points behind a small supervised model before any fusion
happens.

The paired t-tests are the part a direction paper should cite rather than the means: LaBraM's
advantage over EEG-Inception is statistically significant on exactly one of five tasks.

## Notable details

- **Pretraining corpus and total hours**: not applicable to this paper, which pretrains nothing.
  It reports the corpora of the models it evaluates: NeuroGPT was "trained on 20,000 EEG
  recordings from the TUH corpus dataset with a total duration of 5656 hours". No corpus figure is
  given for LaBraM.
- **Parameter count**: trainable parameters including classification heads, from Table 1 —
  EEGNet 2,394; EEG-Inception 22,366; LaBraM 5,854,288; NeuroGPT full model 78,536,146; NeuroGPT
  encoder-only 717,958. Under LoRA, LaBraM's trainable count drops as low as 19,401 (attention
  only, rank 2) and 549 (convolution only).
- **Input contract**: dictated per model by its pretraining. For LaBraM: 200 Hz, band-pass
  0.5–45 Hz, notch at 50, 60 and 100 Hz, trials cut into 1-second patches taken across channels
  giving 256 patches per sample, with temporal embeddings (patch position within the trial) and
  spatial embeddings (channel position within a global list of known electrodes) supplied as
  input — and, critically, "only data from electrodes which were present in the global list
  provided were used". For NeuroGPT: 250 Hz, band-pass 0.05–100 Hz, notch at 50, 60 and 100 Hz
  and harmonics.
- **Most informative transfer number, with baseline**: mean accuracy across the five tasks —
  NeuroGPT encoder-only 0.745, LaBraM 0.742, NeuroGPT full model 0.736, against EEG-Inception
  0.733 (22,366 parameters) and EEGNet 0.731 (2,394 parameters). The best foundation model beats
  the best small supervised baseline by 1.2 points at roughly 32 times the parameter count, and
  beats EEGNet by 1.4 points at roughly 300 times. Per task, EEGNet is the outright best on ERP
  (0.912) and memory is won by EEG-Inception (0.669); the foundation models lead on motor
  (NeuroGPT encoder 0.695 against EEGNet 0.657), sleep (LaBraM 0.704 against EEG-Inception 0.688)
  and eyes (NeuroGPT encoder 0.843 against EEG-Inception 0.823).
- **Statistical significance**: paired t-tests against EEG-Inception give LaBraM p > 0.05 on four
  of five tasks (only ERP, p = 0.0123, is significant). NeuroGPT full model is significant on
  motor (0.0314), ERP (0.0401) and memory (0.0041) but not sleep or eyes; NeuroGPT encoder is
  significant on four of five, failing only on eyes (0.1056). The memory result for NeuroGPT full
  model is significant *against* it — 0.610 versus EEG-Inception's 0.669.
- **Frozen-backbone result**: with all parameters except the classification head frozen, mean
  accuracy falls to 0.635 (LaBraM), 0.647 (NeuroGPT full) and 0.663 (NeuroGPT encoder), against
  0.731 and 0.733 for the fully trained small baselines. The authors summarize this as lagging
  "traditional deep learning approaches by a large margin of almost 8-10%". The collapse is
  extreme on motor imagery, where frozen LaBraM reaches 0.297.
- **LoRA**: reduces trainable parameters by one to two orders of magnitude without loss. The
  authors' ablation finds that adapting a single module type is usually worse than adapting two or
  three, and that attention-plus-convolution and fully-connected-plus-convolution perform
  identically — from which they conclude that "for these state-of-the-art brainwave foundation
  models the attention layers might not capture as important information as their temporal
  encoding parts". Rank behaves as expected for NeuroGPT but peaks at rank 2 for LaBraM.
- **Dropout on LoRA adapters** (LaBraM only, probability 0.5, chosen high because the base model
  is only 5.8M parameters): matches or improves accuracy, with the improvement growing with rank
  and concentrated on the memory and sleep tasks.
- Datasets were "specifically chosen for their minimal spurious artifacts, reducing the likelihood
  of specious performance during training", and the authors note that both foundation models had
  motor, ERP, sleep and eyes paradigms in their pretraining data — so the benchmarks are, if
  anything, favourable to the pretrained models.

## Open questions / limitations

- **The LoRA tables drop the motor task.** Table 1's mean is over five benchmarks; Tables 5 and 6
  report ERP, memory, sleep and eyes only, over four. LaBraM's "0.780" mean under LoRA is
  therefore not comparable with its "0.742" mean under full fine-tuning, and the paper's claim
  that LoRA "yields an additional performance boost" is made across that change of denominator
  without comment. Motor imagery is the task where the foundation models' advantage is largest,
  so its omission cuts against the LoRA claim rather than for it.
- Only two foundation models are evaluated, in three configurations. The abstract's claim about
  "state-of-the-art LBMs" rests on LaBraM and NeuroGPT; CBraMod, BIOT, EEGPT, BENDR and REVE are
  not tested.
- Every model is trained for exactly 20 epochs, chosen "to avoid overfitting". A fixed short
  budget applied to models spanning 2,394 to 78.5 million parameters is not obviously fair in
  either direction, and no learning curves are shown.
- Standard deviations across the 10 folds are large relative to the differences being claimed —
  motor accuracies carry standard deviations of 0.083 to 0.096 for a spread of 0.105 between best
  and worst model — which is why the t-test table matters more than the means, and why the
  1.2-point mean advantage should not be read as robust.
- The LaBraM preprocessing note that "only data from electrodes which were present in the global
  list provided were used" means the evaluation silently discards channels for any dataset whose
  montage exceeds LaBraM's vocabulary. The paper does not say how many channels were dropped per
  dataset, so part of the performance difference may be an input difference.
- No hyperparameter search is reported for the small baselines, and no confidence intervals are
  given for the frozen-backbone table (Table 3 reports single values with no spread).
- This preprint is closely related to a shorter paper by an overlapping author group, "Assessing
  the Capabilities of Large Brainwave Foundation Models" (MLSP 2025, doi
  10.1109/mlsp62443.2025.11204282, which adds Stylianos Bakas to the author list). Whether that is
  a version of this work or a companion is not stated by either record available at retrieval
  time; this card describes the arXiv preprint only.

## Citations

Primary: `lee-2025-lbms-capable-yet`

- `labram-2024` — one of the two evaluated checkpoints, and the one whose advantage over a small
  supervised baseline is statistically significant on only one of five tasks.
- Cui et al., NeuroGPT (2024) — the other evaluated checkpoint, pretrained on 20,000 TUH
  recordings totalling 5,656 hours, and the source of the claim that encoder-only fine-tuning
  matches or beats full-model fine-tuning, which this paper's Table 1 supports.
- Lawhern et al., EEGNet (2018) — the 2,394-parameter supervised baseline that the foundation
  models beat by 1.4 points on average.
- Hu et al., LoRA (2022) — the adaptation method applied here to brainwave models for the first
  time, per the authors' claim.
- Dettmers et al. (2023) — the source of the LoRA dropout guidance the authors deliberately
  deviate from, using 0.5 rather than 0.1 because LaBraM is small.
