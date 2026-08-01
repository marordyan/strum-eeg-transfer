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
with the proposed method reported to outperform existing models by 1–2% on frequency-band features
and the three-level hierarchical set to beat other level combinations by 2–4%.

## Relevance to the review

Two things justify keeping a paper with no EEG in an EEG-centred strand.

The MMTM-based recalibration is a specific, reusable answer to the brief's category 2 question
about intermediate fusion on embeddings. Unlike concatenation, MMTM lets each modality's features
be reweighted conditional on the other's, which is a middle ground between early fusion (where the
modalities share a representation from the start) and late fusion (where they never interact until
the decision). If this project bolts a head onto frozen EEG and peripheral encoders, MMTM is one
of the few mechanisms in this strand that operates at exactly that interface.

The hierarchical-feature finding is the transferable empirical claim: taking low, mid and high-level
activations rather than only the last layer is worth 2–4%. For a project using a frozen pretrained
encoder, the analogous question — which layer's representation to probe — is live, and this is
weak evidence that the answer is "more than one".

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
  "Subject IDs were established for training and testing to ensure subject independence", with the
  first 36, 18, 43 and 42 subjects used for training on WAUC, MAUS and the other two datasets.
- **Datasets**: ASCERTAIN (58 subjects, physiological signals plus face activity, emotional video
  clips, stress labels derived from valence and arousal quadrants), CLAS, MAUS (N-back task,
  complexity as ground truth), WAUC (48 subjects at three exercise levels on a cycle or rowing
  machine, NASA-TLX binarised at the mean; 45 subjects after removing incomplete records).
- **Reported gains**: outperforms existing models by 1–2% on frequency-band features; the
  three-level hierarchical set beats other combinations by 2–4%.
- **Per-dataset accuracies**: **not recorded on this card.** Tables 2 and 3 collapse entirely in
  the two-column extraction, and the abstract and body give only the relative ranges above. This
  is an access limitation, not an omission by the paper.

## Open questions / limitations

- No EEG arm and therefore no bearing on whether peripheral physiology adds to EEG. The entry is
  category 2 only.
- The reported improvements are ranges over four datasets with no per-dataset value in the
  accessible text, no variance, and no significance test. A 1–2% improvement over "existing models"
  without confidence intervals is not distinguishable from run-to-run variation.
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
