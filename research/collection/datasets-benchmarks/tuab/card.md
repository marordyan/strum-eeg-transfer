---
slug: tuab
type: dataset
strand: datasets-benchmarks
year: 2017
authors: [Lopez de Diego]
venue: MS thesis, Temple University (corpus distributed by the Neural Engineering Data Consortium)
doi: null
url: https://isip.piconepress.com/projects/nedc/html/tuh_eeg/
license: null (no data licence stated; access by signed form and registration)
modalities: [scalp-eeg, clinical-eeg, average-reference, tcp-montage]
tags: [benchmark-dataset, binary-classification, normal-vs-abnormal, temple-university-hospital, checkpoint-mapping, registration-required, class-balanced, split-provenance-unclear]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-applicable
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

The single most reported benchmark in the EEG foundation-model literature — binary normal versus
abnormal clinical EEG, distributed with a fixed train/evaluation partition — and the document the
corpus itself names as its description does not state whether that partition is patient-disjoint.

## Summary

The Temple University Hospital Abnormal EEG Corpus is a subset of the Temple University Hospital
EEG Corpus in which each recording is labelled clinically normal or abnormal. It was constructed by
screening the medical reports of all sessions recorded with an average-reference electrode
configuration using natural language processing, then having a team of students manually review each
signal and its report to confirm the automatic assignment. The corpus documentation names Silvia
Lopez de Diego's 2017 master's thesis as its description. That thesis defines two data sets: a short
set of 162 training and 106 evaluation recordings used for pilot work, and a full set of 1,387 normal
plus 1,398 abnormal training files against 150 normal plus 130 abnormal evaluation files, tabulated
alongside patient counts (2,138 training, 253 evaluation) and hours (1,064.7 training, 104.4
evaluation). Selection
was demographically balanced by age and gender, restricted mostly to patients over 20 because
"pediatric EEGs are very different in nature from adult EEGs", with ages 20 to 90 excluding outliers,
mean 46.6 and standard deviation 14.7. One EDF file was selected per session, all longer than 15
minutes. The thesis's own baselines reach 26.1% error with a hidden Markov model on the full
dataset, 24.6% with epoch-based hidden Markov model plus majority vote, and 21.2% with its best
system, a convolutional network with a multilayer-perceptron head.

## Relevance to the review

TUAB is the benchmark on which the foundation-model literature's headline pathology numbers are
produced, and this project needs three things from it.

First, the checkpoint mapping, which is dense: TUAB is reported on by BIOT, EEGPT, LaBraM and
CBraMod in `adabrain-bench`, appears in the epilepsy-and-abnormality family of `omnieeg-bench`, is a
pathology task in `neuralbench`, and is part of the *pretraining* corpus of both BIOT and CBraMod.
That last point is the one that matters most: a suite reporting CBraMod's TUAB score is reporting a
number on a dataset CBraMod was pretrained on. `neuralbench` is the only source in this strand that
flags such overlap; the others do not.

Second, the scale contrast. `adabrain-bench` tabulates TUAB as 2,383 subjects and 409,083 samples of
10 seconds each. Balanced accuracies cluster in the high 70s to low 80s across every model class
there, with LaBraM at 81.50 and ST-Tran, a supervised transformer, at 81.04 — a 0.46-point gap. This
is what a saturated benchmark looks like, and it is the reason `neuralbench` lists pathology among
the tasks "close to saturation". A pretrained-versus-supervised comparison run on TUAB would tell
this project almost nothing.

Third, the split-provenance problem. Everything downstream inherits the corpus's fixed
training/evaluation partition, and the thesis that documents that partition never states that no
patient appears on both sides. Given `brookshire-2024-data-leakage` and `kamrud-2021-data-partitioning`,
that is not a pedantic gap — it is the difference between the field's most reported number meaning
something and meaning nothing. It is very likely patient-disjoint in the released versions, but this
card cannot say so from what was read.

## Notable details

Fixed field set required of every `type: dataset` card in this strand:

- **Participants**: 2,138 in the full training set and 253 in the full evaluation set, per the
  thesis's own file-statistics tables — training "**Abnormal** | | 1398 | | 50.2% | | 899 | 42.1% |
  | 546.4" and "**Normal** | | 1387 | | 49.8% | | 1239 | 58.0% | | 518.3", total "2138"; evaluation
  "**Abnormal** | 130 | | 46.4% | | 105 | | | 41.5% | | 48.9" and "**Normal** | 150 | | 53.6% | |
  148 | | | 58.5% | | 55.4", total "253". *Correction, made during review: an earlier version of
  this card said the count was "not stated as a subject count in the corpus documentation or in the
  thesis, which counts files". The thesis counts both — the tables carry a `Patients` column
  beside the `Files` column. The corpus landing page still states no count, saying only that TUAB
  is "a corpus of EEGs that have been annotated as normal or abnormal".* `adabrain-bench` Table 6
  separately records 2,383 subjects and 409,083 samples for its own preparation of TUAB, a
  benchmark preparation figure that is close to but not identical with the thesis's 2,138 + 253 =
  2,391.
- **Channels**: not stated for TUAB specifically. The parent corpus is 24 to 36 channels with 31 the
  most common EEG-only count. The thesis analyses "each one of the 22 channels in the transverse
  central parietal (TCP) montage (ACNS, 2006), which accentuates spike activity", which is a
  re-derivation the author applied, not the recording montage. The corpus itself was selected from
  sessions recorded with an average-reference electrode configuration, which "accounts for about 45%
  of the data in the overall corpus". `adabrain-bench` uses 23 channels in its preparation. So three
  different channel figures circulate and they refer to three different things: the recording, a
  derived TCP montage, and a benchmark's preprocessing.
- **Sampling rate**: not stated for TUAB. The parent corpus is 87% at 250 Hz, with 256, 400 and 512 Hz
  making up the rest. `adabrain-bench` records "250/256/512 Hz" for TUAB, consistent with the parent.
- **Total hours**: 1,169.1 for the full set — 1,064.7 training plus 104.4 evaluation, both read from
  the thesis's file-statistics tables, whose last column is headed "**Hours**" (training: abnormal
  546.4, normal 518.3, "Total ... 1064.7") and "**hours**" (evaluation: abnormal 48.9, normal 55.4,
  "Total ... 104.4"). The card does not sum them for the reader beyond noting the arithmetic; the
  thesis states the two partition totals and no grand total. *Correction, made during review: an
  earlier version of this card said "unknown ... Neither the corpus page nor the thesis gives a
  total", citing only the thesis's remark that all files used are longer than 15 minutes. That
  remark is real, but the hours are tabulated.* The corpus landing page still gives no hours figure.
- **Task**: none. Archival clinical EEG; the binary label is a retrospective classification of the
  recording, not an experimental condition.
- **Label type**: expert-derived clinical label, normal or abnormal, obtained by natural-language
  screening of the physician's report followed by manual review of signal and report by a student
  team. It is therefore a report-derived label with human verification, not an independent
  adjudication.
- **Licence**: none stated, for either TUAB or the parent corpus.
- **Access route**: as for the parent corpus — signed form emailed to help@nedcdata.org, then ssh key
  and rsync at `data/tuh_eeg/tuh_eeg_abnormal/v3.0.1`. The `-L` option is required because the subset
  is symlinked back to the parent.
- **Checkpoints pretrained on or evaluated against it**:
  *Pretrained on TUAB* — BIOT (which lists TUAB among six pretraining corpora) and CBraMod (whose
  pretraining set is TUAB, TUAR, TUEP, TUEV, TUSE, TUSL), both per `adabrain-bench` Table 7.
  *Evaluated on TUAB* — BIOT 78.07, EEGPT 80.54, LaBraM 81.50, CBraMod 80.05 balanced accuracy in
  `adabrain-bench`'s cross-subject setting, against supervised EEGNet 77.58, LDMA 78.37, ST-Tran
  81.04 and Conformer 78.92; AUC-PR 86.93, 89.36, 90.08, 89.19 against 86.48, 86.97, 90.41, 87.95.
  TUAB is also in `omnieeg-bench`'s epilepsy-and-abnormality subtype and is the pathology task in
  `neuralbench`.

Other details:

- **Full-set composition** per the thesis: training 1,387 normal and 1,398 abnormal files; evaluation
  150 normal and 130 abnormal.
- **Short-set composition**: training 80 abnormal and 82 normal; evaluation 55 abnormal and 51 normal.
- **Demographics**: age range 20 to 90 excluding a small number of outliers, mean 46.6, standard
  deviation 14.7; gender kept balanced across training and evaluation.
- **Context statistic worth carrying**: "75% of the records present in TUH EEG are classified as
  abnormal in the EEG reports" — so TUAB's near-balance is the product of deliberate selection, not
  of the underlying archive.
- **Thesis baselines**, from its own summary table (Table 16, "Summary of results for the
  implemented abnormal EEG classification systems", short-dataset / full-dataset error):
  kNN (k=20) 41.8% / N/A; RF (Nt=50) 31.7% / N/A; PCA-HMM 25.6% / 32.6%; GMM-HMM 17.0% / 26.1%;
  Epoch-Based HMM-Majority Vote 26.6% / 24.6%; Epoch-Based HMM-SdA 27.2% / 22.1%; CNN-MLP N/A /
  21.2%. *Correction, made during review: an earlier version of this card read "hidden Markov model
  plus stacked denoising autoencoder at 24.6%". 24.6% is the majority-vote system, not the
  stacked-denoising-autoencoder one; Table 16 puts HMM-SdA at 22.1% on the full dataset and CNN-MLP,
  the best system in the thesis, at 21.2%.* Note that the thesis contradicts itself on the HMM-SdA
  figure: the body says "This hybrid HMM-SdA system was able to achieve an error rate of 22.9%"
  while Table 16 records 22.1%. Both readings are recorded and neither is preferred here.
  Also a convolutional network on four scalp regions. Features are
  mel-frequency-cepstral-coefficient-like, 26 dimensions per frame, with the first 60 seconds of one
  channel stacked into a 15,600-dimensional vector before reduction.
- The corpus version distributed at retrieval time was v3.0.1; the thesis describes an earlier
  release.

## Open questions / limitations

- **Patient-disjointness of the released partition is not stated in the document the corpus names as
  its description.** The thesis describes selection, demographic balance, file counts, patient
  counts and hours per partition, and says the data "was divided into two sets", without asserting
  that no patient contributes to both. Counting patients separately on each side is consistent with
  disjointness but does not state it. Given
  that the parent corpus averages 1.56 sessions per patient and one patient contributed 37, the
  question is live. Every foundation-model TUAB number in this corpus inherits this partition. This
  is the single most important thing to resolve before any TUAB result is weighed in Phase 4, and
  resolving it requires the release's own `_AAREADME` file, which is behind the registration wall
  (probed URLs returned 404 without credentials).
- **Three incompatible channel counts circulate** — 31 typical in the parent, 22 in the thesis's TCP
  derivation, 23 in AdaBrain-Bench's preparation — and none of the sources states which the released
  files contain. A project checking whether a checkpoint's input contract fits TUAB cannot answer it
  from these documents.
- **Two subject counts circulate and they are not the same number.** The thesis's tables give 2,138
  training plus 253 evaluation patients, i.e. 2,391 for the release it describes; `adabrain-bench`
  records 2,383 for its own preparation. Whether the 8-patient difference is a release difference
  (the thesis predates v3.0.1), an exclusion, or a counting convention is not determinable from
  either source, and the corpus landing page states no subject count at all.
- **Two checkpoints were pretrained on this corpus and are then evaluated on it.** BIOT and CBraMod
  both list TUAB as pretraining data in AdaBrain-Bench's own Table 7, and AdaBrain-Bench reports
  their TUAB scores without comment. Even a patient-disjoint fine-tuning split does not remove this,
  because the self-supervised pretraining saw the evaluation subjects' recordings. `neuralbench` is
  the only source here that treats this as a problem worth flagging.
- **The label is derived from the physician's report, which is also the only ground truth.** There is
  no independent adjudication and no inter-rater statistic. The manual review verified agreement
  between the natural-language screening and the report, not the correctness of the report.
- The corpus was selected only from average-reference sessions, roughly 45% of the parent archive, so
  it is not a random sample of Temple University Hospital EEG.
- The thesis is a 2017 master's thesis distributed as a `.docx` file, not a peer-reviewed data
  descriptor. It is what the corpus page points to, but it is describing the corpus in service of its
  own modelling experiments rather than specifying it.

## Citations

Primary: `tuab`

- `tuh-eeg-corpus` — the parent archive, its access route and its recording characteristics.
- `tuev` — the sibling subset, six-class event classification, drawn from the same archive.
- `adabrain-bench` — the source of the checkpoint-by-benchmark numbers quoted above and of the
  pretraining-corpus table showing the BIOT and CBraMod overlap.
- `neuralbench` — the only suite that flags pretraining-data overlap on its leaderboard.
- `brookshire-2024-data-leakage` — why the unstated patient-disjointness of the fixed partition
  matters.
