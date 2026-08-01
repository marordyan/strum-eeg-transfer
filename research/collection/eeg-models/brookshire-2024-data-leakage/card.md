---
slug: brookshire-2024-data-leakage
type: paper
strand: eeg-models
year: 2024
authors: [Brookshire, Kasper, Blauch, Wu, Glatt, Merrill, Gerrol, Yoder, Quirk, Lucero]
venue: Frontiers in Neuroscience 18:1373515
doi: 10.3389/fnins.2024.1373515
url: https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2024.1373515/full
license: CC BY 4.0
modalities: [scalp-eeg, clinical-eeg, 19-channel-10-20, resting-state, spectrogram-image]
tags: [data-leakage, segment-based-holdout, subject-based-holdout, cross-validation, literature-survey, negative-result, benchmark-critique, alzheimers, seizure]
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

The same convolutional network on the same Alzheimer's EEG data scores 99.8 percent under
segment-based holdout and 53.0 percent — indistinguishable from chance — under subject-based
holdout, and a survey of 63 published deep-learning EEG studies finds only 17 that unambiguously
avoided the first design.

## Summary

This is a short, deliberately narrow demonstration paper. The authors take two published CNN
architectures, apply them without modification or hyperparameter tuning to two datasets, and vary
exactly one thing: whether the train-test split respects subject boundaries. Under *segment-based
holdout*, EEG segments are assigned to train or test without regard to who they came from, so
segments from one subject appear on both sides. Under *subject-based holdout*, every segment from
a subject lands in one partition only. Experiment 1 is a between-subject task, classifying
Alzheimer's disease against subjective cognitive impairment; Experiment 2 is a within-subject
task, labelling which segments of a recording contain an epileptic seizure. The bias appears in
both. The paper then surveys the literature it is criticizing and finds that the flawed design is
the majority practice. No model is proposed and nothing is pretrained; the contribution is the
size of the effect and the frequency of the error.

## Relevance to the review

This is the methodological control on every transfer number in this strand. The project's
comparisons — a small supervised model on STRUM against a fine-tuned pretrained one — are only
interpretable if the split is subject-wise, and this paper puts a number on what happens
otherwise: on a between-subject clinical task, the difference between the two designs is the
difference between a headline result and chance.

It bears on STRUM specifically for two reasons. First, STRUM is a dyadic recording paradigm with a
limited subject pool, which is exactly the regime where the temptation to split by segment is
strongest, because subject-wise splitting leaves very few subjects per fold. Second, the paper's
mechanism — "segments of EEG from one subject are more similar to each other than to segments from
different subjects", so a network can associate a label with a subject's idiosyncratic activity
instead of with the condition — applies with equal force to the project's planned spoken-versus-
written label if any subject contributes predominantly to one condition.

The literature survey is also the strand's only systematic evidence about how common the error is,
and it should temper how any accuracy figure taken from the wider EEG deep-learning literature is
read.

## Notable details

- **Pretraining corpus and total hours**: not applicable. Nothing is pretrained; both models are
  trained from scratch on the dataset under test.
- **Parameter count**: `not reported`. Both architectures are reused from prior published work
  without modification. The seizure model is described structurally — four convolutional layers
  each with rectification, pooling and batch normalization, then fully connected layers of 256 and
  512 units, dropout, and a 2-unit classification layer — and the exact Keras specification is
  said to be in the supplementary material, but no parameter total is given for either model.
- **Input contract**: Experiment 1 (Alzheimer's): 250 Hz, eVox System (Evoke Neuroscience), 19
  electrodes of the 10-20 system (FP1, FP2, F7, F3, Fz, F4, F8, T7, C3, Cz, C4, T8, P7, P3, Pz,
  P4, P8, O1, O2), eyes-open resting block only, low-pass filtered below 125 Hz, non-overlapping
  2-second segments of 500 samples, channels stacked into (500, 19) matrices. 49 subjects with
  Alzheimer's dementia (18 male, 31 female, age 73.9 ± 6.8) against 49 with subjective cognitive
  impairment (18 male, 31 female, age 63.9 ± 11.4). Experiment 2 (seizure): Siena Scalp EEG
  Database, 14 epilepsy patients (age 20–71, nine male), 512 Hz, 10-20 system, 47 seizures in
  about 128 hours of recording; balanced by taking non-seizure data from the start of each
  recording to match seizure duration, giving 47 min 21 s per condition. Converted to
  spectrograms with a 256-sample (0.5 s) Hann window overlapping by 128 samples, cut into 1.5 s
  segments, rendered as 224 x 224 x 3 viridis RGB images.
- **Most informative transfer number, with baseline**: the two holdout designs *are* the
  comparison. Alzheimer's: 99.8 percent (95 percent CI 99.1–100.0) under segment-based holdout
  against 53.0 percent (43.1–64.8) under subject-based holdout, whose interval includes the 50
  percent chance level; Wilcoxon T = 0.0, p = 0.002. Seizure: 79.1 percent (78.8–79.4) against
  65.1 percent (61.3–69.1); Wilcoxon T = 0.0, p = 0.0001. So the inflation is 46.8 points on the
  between-subject task and 14.0 points on the within-subject task.
- **Speed of the leak**: under segment-based holdout, Alzheimer's accuracy "quickly approached
  ceiling within the first 15 training epochs" and seizure accuracy levelled out within 10. Under
  subject-based holdout, performance "remained low throughout the training epochs" in both. A
  learning curve that saturates fast is therefore itself a symptom.
- **Literature survey**: Google Scholar searched for deep-learning EEG studies of Alzheimer's,
  Parkinson's, ADHD, depression, schizophrenia and seizures, then reference-chased; 63 papers, all
  published since 2018. Of these, **only 17 (27.0 percent) unambiguously avoided subject-level
  leakage**. The remainder are classified as segment-based, "both" (different designs in different
  analyses), or "unclear". Studies that trained a separate model per subject were counted as
  segment-based.
- **No model selection**: the authors state that because they reused published architectures
  unchanged, "no model selection was performed; performing ongoing validation on the test is
  therefore not a source of data leakage" — a deliberate design choice so that the only leakage
  under study is the one being manipulated. Training ran 70 epochs with no early stopping,
  RMSProp, batch size 32, learning rate 0.00001.
- The within-subject result is the more surprising of the two: even when the task is to label
  moments *inside* a subject's own recording, holding out whole subjects still costs 14 points, so
  the leak is not confined to between-subject diagnosis.

## Open questions / limitations

- The authors describe their literature search as "non-exhaustive": Google Scholar plus reference
  chasing, restricted to six conditions and to papers from 2018 onward. The 27.0 percent figure is
  therefore a property of a convenience sample of 63 papers, not an estimate over the field, and
  the paper does not report inter-rater reliability for the classification of each study's split.
- Neither dataset is large. The Alzheimer's arm has 98 subjects total and the seizure arm 14
  patients, so the subject-based confidence intervals are wide — 43.1 to 64.8 percent in
  Experiment 1 — and the "indistinguishable from chance" conclusion rests on an interval that also
  includes 64 percent.
- The Alzheimer's dataset is proprietary, collected by the authors' company on the eVox System.
  The paper does not state whether it is available, so Experiment 1 is not reproducible; only the
  Siena database is public.
- The seizure experiment reuses a spectrogram-image pipeline from one prior study, including its
  viridis RGB rendering. Whether the leakage magnitude depends on that representation is not
  tested, and the paper compares only one architecture per task.
- The paper does not examine session-level or recording-level leakage, which is the next case
  down: a subject-wise split still permits the same *session* to be split across folds when a
  dataset has multiple recordings per subject. Its vocabulary is subject versus segment only.
- No pretrained model is examined. The result is about supervised training, and the paper makes no
  claim about whether a frozen pretrained embedding leaks subject identity in the same way — that
  question belongs to other entries in this strand.
- The classification of surveyed papers as "unclear" when the split is not stated means the true
  leakage rate could be higher or lower than 73 percent; the authors report the raw counts rather
  than imputing.

## Citations

Primary: `brookshire-2024-data-leakage`

- Demuru and Fraschini (2020) — the EEG-fingerprinting result the mechanism rests on: segments
  from one subject resemble each other more than segments from different subjects.
- Rashed-Al-Mahfuz et al. (2021) — the published seizure architecture and spectrogram pipeline
  reused unmodified in Experiment 2, and itself classified as segment-based holdout in the survey.
- Detti et al., Siena Scalp EEG Database (2020) — the public dataset behind Experiment 2.
- `lin-2026-identity-trap` — later work in this strand that cites this paper and extends the
  subject-identity argument from supervised training to frozen foundation-model embeddings.
- Acharya et al. (2018), Lee et al. (2019), Oh et al. (2020) — examples the paper names of prior
  studies reporting high accuracy under segment-based holdout.
