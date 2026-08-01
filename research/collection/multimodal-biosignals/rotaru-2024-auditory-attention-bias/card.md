---
slug: rotaru-2024-auditory-attention-bias
type: paper
strand: multimodal-biosignals
year: 2024
authors: [Rotaru, Geirnaert, Heintz, Van de Ryck, Bertrand, Francart]
venue: Journal of Neural Engineering 21(1):016017
doi: 10.1088/1741-2552/ad2214
url: https://lirias.kuleuven.be/handle/20.500.12942/735480
license: null
modalities: [eeg, eog]
tags: [artifact-confound, eye-gaze-bias, trial-fingerprint, spatial-auditory-attention, common-spatial-patterns, random-cv-leakage, audiovisual-congruence, negative-result, feature-drift]
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

An EEG decoder of spatial auditory attention was shown to be reading eye-gaze direction and
per-trial recording fingerprints rather than attention: four EOG channels alone decode above
chance when gaze and attention are congruent, and a classifier asked to predict *which trial* a
segment came from reaches 99.6–100%.

## Summary

Sixteen participants listened to two competing talkers while 64-channel EEG and 4-channel EOG were
recorded (BioSemi ActiveTwo, 8192 Hz) under an audiovisual protocol in which the spatial locus of
visual attention was made either congruent or incongruent with the attended talker. Four visual
conditions were used: moving video (MV), moving target (MTN), no visuals (NV) and static video
(SV); only SV is audiovisually congruent. Decoders were deliberately simple — common spatial
pattern (CSP) filters followed by linear discriminant analysis or k-means clustering — and were
evaluated both across and within trials. Three findings follow. Decoding accuracy peaks in the
congruent SV condition and, for subject-independent CSP filters, is significant *only* there,
which is the signature of an eye-gaze-driven decoder rather than an attention-driven one. Training
CSP filters on the four external EOG channels alone (two filters per band, matched to the EEG
comparison) yields accuracies that are lower than 64-channel EEG in every condition but still
above the significance level in SV. And when the same pipeline is trained to predict trial
identity instead of attention, median accuracies are 100%, 99.9%, 99.7% and 99.6% for MV, MTN, NV
and SV — significantly higher than the attention decoding itself.

## Relevance to the review

This is the strand's strongest single argument that an apparent physiological decoding result can
be an artifact, and it is unusually close to this project's setting: the task is auditory
attention, the confounding channel is EOG, and the failure mode is a decoder trained with random
cross-validation on trials that were recorded at different times.

Three specific transfers to STRUM. First, the *direction* of the argument is the one this project
needs. If adding an EOG channel to an EEG model improves decoding of a spoken-versus-written
contrast, this paper is the reason to suspect the improvement is ocular rather than cortical: the
two stimulus conditions differ in where the participant looks and how often they blink, and CSP-
class spatial filters pick that up from the EEG itself, not only from the dedicated EOG channels.

Second, the trial-fingerprint result generalises past ocular artifact entirely. The authors show
that EEG signal statistics drift enough between recording blocks that a linear classifier can
identify the block at ceiling, and that random cross-validation over short windows within a block
lets that fingerprint leak into the attention label. Where a study has "a single attention label
per trial", the attention label and the trial label are the same variable. Any stimulus-blocked
design — including a spoken block followed by a written block — inherits this exactly.

Third, the paper is explicit that the vulnerability scales with model capacity: "It is expected
that more complicated non-linear models based on deep neural networks, which are often used for
Sp-AAD, are even more vulnerable to such biases." A fine-tuned foundation model is the extreme of
that scale.

## Notable details

- **Cohort and recording**: 16 participants; 64-channel EEG plus 4-channel EOG at 8192 Hz on a
  BioSemi ActiveTwo. EOG sensors placed 1.5 cm above and below the right eye for vertical
  oculomotor activity, and approximately 1 cm lateral to each eye for horizontal.
- **EOG-only decoder**: CSP filters trained on the four EOG channels alone (two filters per
  frequency band, to match the EEG comparison) under the same random 5-fold cross-validation.
  Median accuracies are consistently lower than 64-channel EEG — Wilcoxon signed-rank p = 0.001,
  0.15, 0.03 and 0.04 for MV, MTN, NV and SV — but exceed the significance level in the SV
  condition.
- **Condition asymmetry**: subject-independent CSP accuracies are significant only in SV, the one
  audiovisually congruent condition, "despite a comparable amount of training data for all
  conditions". The authors read this as evidence that CSP decoding "is predominantly driven by
  signal components that originate from the motion of the eyeballs (i.e., EOG-related components),
  and therefore have no neurological component whatsoever".
- **Trial-fingerprint decoding**: with trial labels instead of attention labels, subject-specific
  CSP plus LDA on 5 s windows reaches median 100% (MV), 99.9% (MTN), 99.7% (NV) and 99.6% (SV),
  significantly above the corresponding attention accuracies (p = 3e-5, 2.5e-4, 3e-5, 6.1e-5). The
  authors conclude "trial fingerprints are even more dominant than spatial auditory attention
  patterns", implying strong feature drift over time between blocks.
- **Mechanism of the leak**: under random cross-validation, "different short-term windows within a
  trial are randomly divided between the test and train set", so a test segment usually has a
  training segment nearby in time carrying the same time-specific fingerprint.
- **Residual genuine signal**: decoding above the significance threshold also occurs in the three
  AV-incongruent conditions (MV, MTN, NV) in the subject-specific case, which the authors take as
  evidence that some genuine lateralisation of auditory attention is present. The paper does not
  claim all decoding is artifact.
- Retraining on the test trial with an unsupervised algorithm did not rescue trial generalisation,
  so the drift is not merely a calibration offset.

## Open questions / limitations

- The decoders are deliberately linear (CSP plus LDA or k-means). The paper argues by extension
  that deep models are more vulnerable, but does not demonstrate it, so the magnitude of the
  problem for a fine-tuned foundation model is asserted rather than measured.
- Sixteen participants, and the per-condition significance results rest on Wilcoxon tests across
  those sixteen.
- The paper does not report what fraction of the SV decoding accuracy is attributable to ocular
  components after their removal — there is no "EEG with ocular components projected out" arm to
  compare against the raw 64-channel result. That is the arm this project would most want, because
  it is the one that says what ocular artifact removal costs.
- The audiovisual manipulation is specific to a two-talker spatial paradigm. Whether the same
  gaze-attention coupling exists in a task with no spatial audio component — such as a
  spoken-versus-written stimulus contrast — is not addressed, though the trial-fingerprint result
  is paradigm-independent.
- The archived copy is the accepted author manuscript, so figure and table numbering may differ
  from the version of record and page-level citation is unsafe.
- Head position: the paper notes participants "spontaneously, even unconsciously, changed their
  head position during the EEG data collection, thus slightly changing the range of the visual
  angle", which is an uncontrolled source of variation in the gaze-related component.

## Citations

Primary: `rotaru-2024-auditory-attention-bias`

- `mostert-2018-eye-movement-confounds` — the same argument in MEG, where the memorised item is
  decodable from gaze position alone.
- `wibirama-cognitive-load-eye-movement` — the constructive counterpart: eye-movement indices
  decode cognitive load well enough that removing them from EEG discards task information.
- `angkan-2024-invehicle-cognitive-load` — a study that adds gaze as a modality and reports a gain,
  without a control of this kind.
- `zeng-brain-heart-ccm` — the analogous question for the cardiac channel: whether coupling is
  genuine or reflects shared task structure.
- Puffay et al. (2023) — cited here for the same red flag about accuracies obtained with random
  cross-validation in auditory attention decoding.
