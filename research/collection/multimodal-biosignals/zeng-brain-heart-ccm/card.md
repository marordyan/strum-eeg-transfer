---
slug: zeng-brain-heart-ccm
type: paper
strand: multimodal-biosignals
year: 2026
authors: [Zeng, Zhang, Dong, Bian, de Albuquerque, Wu]
venue: Physiological Measurement 47(6):065005
doi: 10.1088/1361-6579/ae7c55
url: https://doi.org/10.1088/1361-6579/ae7c55
license: null
modalities: [eeg, ecg]
tags: [convergent-cross-mapping, brain-heart-interaction, directed-coupling, heartbeat-evoked-potential, emotion, virtual-reality, descending-coupling, lateralization, nonlinear-causality]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-available
pdf_path: null
md_path: source.md
md_quality: abstract-only
---

## TL;DR

Convergent cross mapping between 32-channel EEG and single-lead ECG during emotional virtual-
reality stimulation finds coupling that is directionally asymmetric — descending, cortex-to-heart,
influence stronger and more sustained than ascending — which is the direction that would predict a
peripheral channel adding little beyond a good EEG model.

## Summary

The paper argues that conventional brain-heart interaction analysis, which relates EEG rhythms to
heart-rate variability, cannot capture heartbeat-resolved dynamics of the bidirectional interaction
between cortical and cardiac activity. It applies convergent cross mapping — a nonlinear
state-space causality framework — to 32-channel EEG and single-lead ECG recorded while participants
viewed validated virtual-reality videos designed to elicit positive or negative affect. Rather than
using band powers and HRV indices, it models heartbeat-evoked potentials and full cardiac waveforms
as evolving dynamical systems. The reported result is a pronounced directional asymmetry:
descending (cortical-to-cardiac) coupling is "stronger, more sustained, and spatially focused" than
ascending (cardiac-to-cortical) effects. Positive and negative emotional conditions are associated
with differential bidirectional coupling patterns, with preferential enhancement of the descending
direction. Spatially, the modulation is left-lateralised and concentrated over frontal and central
electrodes. The authors position the findings as support for embodied models of affect in which
cardiac dynamics are an active component of emotion-related coordination rather than a passive
readout.

## Relevance to the review

This entry asks the mechanistic question that the fusion papers assume away, and its answer bears
directly on how much the project's third comparison should expect to gain.

If cardiac activity during an affective or cognitive state is largely *downstream* of the same
central state the EEG already measures — which is what a dominant descending direction means —
then an ECG channel added to an EEG embedding is closer to a noisy copy of information the encoder
already has than to a new source. A measured gain would then need another explanation: better
signal-to-noise on a slow component, a different temporal integration window, or artifact. That is
a testable prediction rather than a hand-wave, and it is the reason this entry is `relevance: high`
despite being abstract-only.

Conversely, the paper does report bidirectional coupling that differs between positive and negative
conditions, which leaves room for an ascending component that carries condition-specific
information. The asymmetry is a matter of degree, not an absence of ascending coupling, and the
abstract does not quantify the degree.

The methodological caution belongs on the record here rather than only in the methods entry. A
convergent-cross-mapping direction claim is a function of embedding dimension, lag and library
size as much as of physiology; `schiecke-ccm-methods` is the entry that establishes this, and
Phase 3 should read the two together before treating "descending dominates" as a fact about the
nervous system.

## Notable details

- **Signals**: 32-channel EEG and single-lead ECG, recorded simultaneously.
- **Stimulus**: validated virtual-reality videos eliciting positive or negative affect.
- **Method**: convergent cross mapping applied to heartbeat-evoked potentials and to full cardiac
  waveforms treated as evolving dynamical systems, in place of the conventional EEG-rhythm-versus-HRV
  approach.
- **Direction of coupling**: descending (cortical-to-cardiac) stronger, more sustained and more
  spatially focused than ascending (cardiac-to-cortical).
- **Condition effect**: positive and negative conditions show differential bidirectional coupling,
  with preferential enhancement of the descending direction.
- **Topography**: left-lateralised, concentrated over frontal and central electrodes.
- **Strength of coupling**: *reported but not accessible.* The abstract states the direction and
  the qualitative asymmetry but gives no coupling coefficients, no significance levels and no
  effect sizes. The full text is behind an IOP anti-bot barrier (see `meta.json.notes`).
- **Time scales**: *reported but not accessible.* The abstract says the descending effects are
  "more sustained" without stating over what interval, and heartbeat-resolved analysis implies a
  sub-second to few-second scale, but the lags used are not given.
- **Participant count**: *not stated in the abstract*, and not recoverable. Whether this is a
  not-reported or a not-accessible case cannot itself be determined without the full text; it is
  almost certainly reported in the methods, so treat it as not accessible.
- **Control for shared task structure**: *not addressed in the abstract.* Whether the analysis
  controlled for the video stimulus driving both signals — the single most important control for
  a coupling claim of this kind — is unknown from the accessible text. This is the fact the brief
  specifically asked for and it could not be obtained.

## Open questions / limitations

- The three facts the brief required — strength of coupling, time scales, and control for shared
  task structure — are all in the inaccessible body. This card records the direction claim and
  nothing quantitative, and the entry should be re-attempted with institutional access before
  Phase 3 relies on it.
- A convergent-cross-mapping asymmetry between two signals measured with very different
  signal-to-noise ratios is not automatically a physiological asymmetry: the method's ability to
  detect cross-mapping in one direction depends on how well each system's attractor is
  reconstructed from its own observable. Single-lead ECG reconstructs a cardiac attractor far more
  cleanly than 32-channel scalp EEG reconstructs a cortical one, which could bias the detected
  direction. Nothing in the abstract addresses this.
- Emotional virtual-reality video is a stimulus that drives both systems simultaneously. Without
  the shared-input control, "descending coupling" and "the stimulus drives cortex first and heart
  second with a lag" are not distinguished.
- The left-lateralised frontal-central topography is consistent with a genuine affective
  asymmetry and equally consistent with ocular and muscular contamination of frontal channels
  during video viewing; the abstract reports no artifact handling.
- The construct is emotion, not language modality. Whether the same directional asymmetry holds
  for a cognitive or linguistic contrast is untested.

## Citations

Primary: `zeng-brain-heart-ccm`

- `schiecke-ccm-methods` — the parameter-sensitivity treatment that determines how much weight a
  CCM direction claim can bear.
- `schiecke-2019-brain-heart-ccm` — the same method applied to brain-heart interaction with
  explicit statistical machinery (surrogates, bootstrapping, linear mixed-effects models).
- `salam-eeg-ecg-stress` — the classification counterpart: what an EEG-plus-ECG fusion actually
  buys when the coupling question is not asked.
- `haque-hrv-stress-review` — the HRV-index tradition this paper argues is too coarse to resolve
  heartbeat-level dynamics.
- `rotaru-2024-auditory-attention-bias` — the same "is this real or is it shared task structure"
  question for the ocular channel.
