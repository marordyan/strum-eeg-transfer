---
slug: azad-2025-construction-noise
type: paper
strand: multimodal-biosignals
year: 2025
authors: [Azad, Lee, Choi]
venue: Sensors 25(21):6775
doi: 10.3390/s25216775
url: https://doi.org/10.3390/s25216775
license: CC BY 4.0
modalities: [eeg, eda]
tags: [auditory-stimulus, annoyance, decision-level-fusion, temperature-scaling, groupkfold, subject-independent, cnn, bi-lstm, ablation, near-null-fusion-gain, tonic-phasic]
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

Under subject-independent folds, adding electrodermal activity to EEG moved annoyance-classification
accuracy from 0.794 to 0.796 — and the authors' own fusion rule falls back to EEG whenever fusion
fails to beat it on a validation subset, which is an admission in code that the peripheral channel
often does not help.

## Summary

Twenty-five participants were exposed to impulsive noise from pile drivers and tonal noise from
earth augers at three intensity levels (40, 60 and 80 dB) while EEG and electrodermal activity
were recorded simultaneously. Trials were rated for annoyance on a 1–10 scale and binarised into
normal (1–7) versus high (8–10), giving 5013 EEG–EDA segments in a 67:33 class ratio. A CNN
processes 2 s EEG windows at 128 Hz; a bidirectional LSTM processes 20 s EDA windows at 4 Hz after
a 1.9 Hz low-pass and a tonic/phasic decomposition (10 s centred moving average for tonic, residual
for phasic). Each model's logits are temperature-scaled on a held-out calibration subset and then
combined by stacked late fusion. Evaluation is 5-fold subject-independent GroupKFold with all
windows from a participant confined to one fold. The fused model reaches accuracy 0.796 (95% CI
0.769–0.823), macro-F1 0.766, AUROC 0.856; EEG alone reaches 0.794 (0.768–0.820), F1 0.765; EDA
alone 0.557 (0.528–0.586), F1 0.539. An extensive ablation varies window lengths, batch size,
weight decay, augmentation and calibration.

## Relevance to the review

Three properties make this the most directly transferable category-3 entry for STRUM, despite the
construct being noise annoyance rather than anything this project decodes.

First, the stimulus is auditory and the design manipulates it parametrically. This project has a
separate auditory stimulus marker and a spoken-versus-written contrast, so the question of whether
a peripheral channel adds anything when the manipulation is acoustic is the closest available
analogue, and the answer here is essentially no.

Second, the split is honestly subject-independent (GroupKFold on participant), the calibration and
threshold subsets are carved out of the training folds only, and the test folds are used for
nothing but testing. That is the protocol this project should copy, and it is the protocol under
which the fusion gain evaporates: +0.002 accuracy, +0.001 F1, with overlapping confidence
intervals.

Third, and most instructive, the authors build the null into their own inference rule. On each
fold, "fusion was used on the test set only if it outperformed EEG in terms of both accuracy and
F1 on the fusion-validation subset; otherwise, predictions defaulted to EEG." A system that has to
gate its own fusion behind a per-fold check is a system whose designers observed that fusion
sometimes hurts. Any project reporting a fused number should say whether a comparable gate is in
place, because a gated fused number is not the same object as an ungated one.

The EDA arm at 0.557 against a 67% majority class is below the majority-class baseline in
accuracy terms, which is worth stating plainly: on this task electrodermal activity alone carries
close to nothing.

## Notable details

- **EEG-only number**: accuracy 0.794 (95% CI 0.768–0.820), macro-F1 0.765 (0.733–0.797), AUROC
  0.856, AUPRC 0.851; fold-to-fold coefficient of variation 7.07% for accuracy, 3.86% for F1.
- **Peripheral-only number**: EDA accuracy 0.557 (0.528–0.586), F1 0.539 (0.517–0.561), AUROC
  0.555. Below the 67% majority-class rate, with low variance, so the authors conclude "the
  performance gap is systematic and not due to high variance".
- **Combined number**: accuracy 0.796 (0.769–0.823), macro-F1 0.766 (0.733–0.798), AUROC 0.856
  (0.819–0.892). Coefficient of variation at most 5% across metrics.
- **Split protocol**: 5-fold subject-independent GroupKFold; all windows from a given participant
  assigned to a single fold. Within each training fold, 15% held out for validation and split 1:1
  into a temperature-scaling calibration subset and a fusion/threshold subset.
- **Participants**: 25.
- **Baseline windowing**: EEG non-overlapping 2 s at 128 Hz, EDA non-overlapping 20 s at 4 Hz. The
  ablation finds 6 s EEG and 5–10 s EDA windows, smaller batch sizes and moderate weight decay to
  be most stable, and a retrained ablation-informed configuration improves overall accuracy.
- **Class balance**: 3356 normal-annoyance vs 1657 high-annoyance segments (67:33). Handled with
  class-weighted cross-entropy, macro-averaged metrics, minority duplication and Gaussian-noise
  augmentation (sigma up to 0.10), with augmentation disabled for validation and test.
- Under a matched re-run using the annoyance cutoff of an earlier study (Hwang et al.), this
  paper's unimodal EEG reaches 0.834 accuracy against that study's 0.6383, and its fused model
  0.846 against 0.6517 — so its late fusion beats the earlier early-fusion approach even though
  its own fusion gain over EEG is negligible.
- Annoyance rises sharply with the highest condition: for the earth auger, 1 of 25 participants
  reported high annoyance at the lowest level and 20 of 25 at the highest; for the pile driver,
  2 of 25 and 17 of 25.
- EEG preprocessing was done in EEGLAB and the paper notes explicitly that scalp EEG is sensitive
  to ocular and muscular contamination.

## Open questions / limitations

- Only two modalities, and the peripheral one is EDA — slow, tonic, and the least likely of the
  peripheral channels to track a stimulus-locked contrast. The null here is weaker evidence about
  ECG or EOG than about autonomic arousal generally.
- The 20 s EDA window against a 2 s EEG window means the two branches are not decoding the same
  temporal object. Some of the EDA arm's weakness is a resolution mismatch rather than an absence
  of information, and the paper does not separate the two.
- The paper labels its noise conditions inconsistently: the abstract and the class-distribution
  prose describe three intensity levels of "40, 60, and 80 dB", while Table 3 and the accompanying
  text label the same conditions "40 Hz", "60 Hz" and "80 Hz". Decibels are almost certainly
  intended; the frequency labelling appears to be an error, and it is repeated often enough that
  it is not a single typographic slip.
- Annoyance is a self-reported affective judgement binarised at 8 of 10. The choice of cutoff is
  justified by a citation that is rendered in the text as the literal word "(reference)", i.e. an
  unresolved placeholder left in the published paper.
- The validation-gated fallback to EEG means the reported fused number is a mixture: on some folds
  it is the fused model's output and on others it is the EEG model's. The paper does not report
  how often the gate fired, so the 0.796 cannot be read as "the fused model's accuracy".
- No permutation test or chance-corrected metric; the comparison to chance rests on the class
  ratio.
- Twenty-five participants across five folds means each fold holds out five participants, so the
  confidence intervals are driven by a small number of subject-level draws.

## Citations

Primary: `azad-2025-construction-noise`

- `hogervorst-2014-workload-comparison` — the same null two decades earlier, with classical
  features and a within-subject temporal split.
- `angkan-2024-invehicle-cognitive-load` — a positive but small LOSO gain from three peripheral
  channels including EDA.
- `salam-eeg-ecg-stress` — the large-gain counterexample, on arousal-driven stress rather than an
  acoustic stimulus.
- `makowski-2021-neurokit2` — reference implementation of the tonic/phasic EDA decomposition this
  paper hand-rolls with a 10 s moving average.
- Hwang et al. — the earlier construction-noise study using engineered features, tree models and
  early fusion, which this paper re-runs under matched labels as its comparator.
