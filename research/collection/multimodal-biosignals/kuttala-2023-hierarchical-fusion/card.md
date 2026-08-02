---
slug: kuttala-2023-hierarchical-fusion
type: paper
strand: multimodal-biosignals
year: 2023
authors: [Kuttala, Subramanian, Oruganti]
venue: IEEE Access 11
doi: 10.1109/ACCESS.2023.3237545
url: https://doi.org/10.1109/ACCESS.2023.3237545
license: CC BY 4.0
modalities: [ecg, eda]
tags: [intermediate-fusion, mmtm, hierarchical-cnn-features, no-eeg, subject-independent, ascertain, clas, maus, wauc, frequency-band-features, pyhrv, stress-detection]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

Fuses electrodermal activity and ECG by concatenating low-, mid- and high-level CNN features
within each modality and then recalibrating across modalities with a Multimodal Transfer Module —
a peripheral-only fusion architecture with no EEG anywhere, evaluated subject-independently on
four benchmarks.

## Summary

The premise is that the low, mid and high-level features of a convolutional network are each
discriminative and that concatenating all three gives a more comprehensive representation than
using the final layer alone. The method builds such a hierarchical feature set independently for
each of two peripheral modalities — electrodermal activity and electrocardiogram — and then fuses
the two hierarchical sets with the Multimodal Transfer Module (MMTM), which recalibrates each
modality's features using the other's, followed by late fusion for the stressed/unstressed
decision. Experiments are run both on raw frequency-domain data and on features extracted from
frequency bands, so the effect of that choice can be separated. ECG contributes 51 frequency-domain
HRV measures per band computed with pyHRV over Welch power spectral densities; EDA contributes 40
statistical characteristics (five bands, eight features each: max, min, standard deviation,
variance, skewness, kurtosis, median, min). Signals are cut into five-second segments and subject
IDs are used to keep training and test subjects disjoint. Evaluation covers four benchmarks —
ASCERTAIN (58 subjects), CLAS, MAUS and WAUC (48 subjects, 45 after removing incomplete records) —
with the proposed method reported to outperform existing models by 1–2% on frequency-band features.
The gain from using all three feature levels is stated twice and inconsistently: 2–4% in the
abstract, 9–15% on band features in the Results.

## Relevance to the review

Two things justify keeping a paper with no EEG in an EEG-centred strand.

The MMTM-based recalibration is a specific, reusable answer to the brief's category 2 question
about intermediate fusion on embeddings. Unlike concatenation, MMTM lets each modality's features
be reweighted conditional on the other's, which is a middle ground between early fusion (where the
modalities share a representation from the start) and late fusion (where they never interact until
the decision). If this project bolts a head onto frozen EEG and peripheral encoders, MMTM is one
of the few mechanisms in this strand that operates at exactly that interface.

The hierarchical-feature finding is the transferable empirical claim: taking low, mid and
high-level activations rather than only the last layer helps. How much it helps cannot be stated,
because the abstract says 2–4% and the Results say 9–15% on the same comparison (see the
split-reading note under Notable details). For a project using a frozen pretrained encoder, the
analogous question — which layer's representation to probe — is live, and this is weak evidence
that the answer is "more than one", with the magnitude unusable until the discrepancy is resolved
against the paper's Tables 2 and 3.

Everything else argues for `relevance: low`. There is no EEG arm, so the paper contributes nothing
to the project's third comparison and is explicitly not counted toward the category 3 criterion.
The construct is stress. The gains are small and reported as ranges rather than per-dataset values
that can be checked.

## Notable details

- **No EEG.** The two modalities are EDA and ECG only. This is worth stating plainly because the
  paper surfaces in EEG-adjacent searches and its title does not signal the absence.
- **Fusion mechanism**: Multimodal Transfer Module (MMTM) applied to the two hierarchical feature
  sets, then late fusion for the binary stressed/unstressed decision.
- **Hierarchical feature construction**: low, mid and high-level CNN activations concatenated
  within each modality, described in the architecture as phases 1, 2 and 3.
- **ECG features**: 51 frequency-domain measures per band from pyHRV over Welch power spectral
  densities of HRV derived from each of five bands.
- **EDA features**: 40 statistical characteristics — five bands times eight features (max, min,
  standard deviation, variance, skewness, kurtosis, median, min; the paper lists "min" twice,
  which is either a typographic error or an undocumented distinction).
- **Bands**: five, with the highest listed as 0.35–0.45 Hz (band d) and 0.45–0.50 Hz (band e); the
  rationale given is that low- and high-frequency bands are affected by autonomic nervous system
  activity.
- **Segmentation and split**: signals split into five-second segments to increase sample count;
  "Subject IDs were established for training and testing to ensure subject independence. The first
  36,18, 43 and 42 subject samples from WAUC, MAUS, CLAS and ASCERTAIN datasets are used for
  training. The remaining 9 WAUC, 4 MAUS and 16 CLAS and ASCERTAIN subject samples are employed for
  the testing." The split is therefore subject-disjoint on all four datasets, and fixed rather than
  cross-validated.
- **Datasets**: ASCERTAIN (58 subjects, physiological signals plus face activity, emotional video
  clips, stress labels derived from valence and arousal quadrants), CLAS, MAUS (N-back task,
  complexity as ground truth), WAUC (48 subjects at three exercise levels on a cycle or rowing
  machine, NASA-TLX binarised at the mean; 45 subjects after removing incomplete records).
- **Reported gains — the abstract and the Results section disagree, and neither is adopted here.**
  The abstract: "The proposed method showed its effectiveness by outperforming existing models by
  1-2%, respectively, on frequency band features. It is observed that the hierarchical feature set
  from all three levels performed better than all other combinations by 2-4%." Section IV-A of the
  Results: "Concatenating all level features (phases 1, 2, and 3) enhanced the model's overall
  performance more than other combinations (phases 1, 2, and 3 alone and its combinations) by 12-15%
  on raw data, 9-15% on band features and 12.15% on highest band features of ECG and EDA on WAUC
  dataset." So the hierarchical-fusion gain is 2-4% by the abstract and 9-15% by the Results, a
  factor of three to five apart. Recorded as a self-contradiction rather than reconciled.
- **What the Results' own "2-4%" refers to** is a different comparison entirely: Section IV-C says
  "in all the datasets, we have observed the same shift in the performance of raw data and frequency
  band features by 2-4%", i.e. band features beat raw data by 2-4%. An earlier version of this card
  attached the 2-4% to the hierarchical-feature gain, following the abstract, and used it in the
  Relevance section as the transferable number.
- **Per-dataset accuracies**: **not recorded on this card, and the reason was re-verified in the
  Phase 4 audit.** `source.md` contains no markdown table rows at all — the captions "TABLE 1. List
  of abbrevations.", "TABLE 2. Classification results.", "TABLE 3. Classification results WAUC
  dataset on highest performed band of ECG and EDA." and "TABLE 4. Comparison to state-of-art
  findings." survive with empty bodies. This is the one entry in the strand whose tables did not
  come back after the pymupdf4llm re-extraction, which is why `md_quality` stays `rough`. The
  numbers exist in the paper; they are not in the archived markdown. An access limitation, not an
  omission by the paper.

## Open questions / limitations

- No EEG arm and therefore no bearing on whether peripheral physiology adds to EEG. The entry is
  category 2 only.
- The reported improvements are ranges over four datasets with no per-dataset value in the
  accessible text, no variance, and no significance test. A 1–2% improvement over "existing models"
  without confidence intervals is not distinguishable from run-to-run variation — and the paper
  cannot keep its own two statements of the hierarchical gain consistent, which is a reason to
  treat all of its reported margins as approximate.
- Stress labels on ASCERTAIN are derived by thresholding valence and arousal ratings into a
  quadrant, which is a construct substitution the paper adopts from prior work rather than
  validating; on WAUC the label is binarised NASA-TLX at the mean, i.e. a median-split of a
  subjective scale.
- Splitting signals into five-second segments "to increase the sample count" inflates the effective
  sample size within each subject. The subject-independent split protects against cross-subject
  leakage but not against the optimism that many correlated segments per subject introduce in the
  variance estimate.
- WAUC's cognitive-load manipulation is exercise intensity on a cycle or rowing machine, so the
  peripheral signals track physical exertion directly. Decoding "cognitive load" from ECG and EDA
  under that manipulation is close to decoding the exercise level, which is a confound the paper
  does not discuss.
- MMTM is adopted without an ablation against simpler cross-modal recalibration, so its specific
  contribution is not isolated from the hierarchical-feature contribution.

## Citations

Primary: `kuttala-2023-hierarchical-fusion`

- `ding-2025-cross-attention-fusion` — the cross-attention alternative to MMTM-style
  recalibration, with EEG in the loop.
- `azad-2025-construction-noise` — decision-level fusion of EEG and EDA, with the unimodal arms
  this paper lacks.
- `makowski-2021-neurokit2` — the reference implementation family that pyHRV belongs to, for the
  HRV features used here.
- `wang-2025-sedation-non-eeg` — the other peripheral-only decoding entry in this strand.
- Joze et al., MMTM (Multimodal Transfer Module) — the cross-modal recalibration mechanism this
  paper applies.
