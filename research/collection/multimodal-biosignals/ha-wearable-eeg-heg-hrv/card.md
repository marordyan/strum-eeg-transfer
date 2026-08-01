---
slug: ha-wearable-eeg-heg-hrv
type: paper
strand: multimodal-biosignals
year: 2015
authors: [Ha, Lee, Kim, Roh, Bae, Kim, Yoo]
venue: IEEE Transactions on Biomedical Circuits and Systems 9(6), 758-766
doi: 10.1109/TBCAS.2015.2504959
url: https://doi.org/10.1109/TBCAS.2015.2504959
license: null
modalities: [eeg, ecg]
tags: [hardware, wearable, heg, nirs, hrv, transcranial-electrical-stimulation, canonical-correlation-analysis, tkcca, acquisition-constraints, asic, synchronization]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: abstract-only
---

## TL;DR

A custom-silicon headband and earplug system acquiring EEG, hemoencephalography and heart-rate
variability simultaneously with transcranial electrical stimulation, reporting a 19% maximum
classification improvement from multimodal over single-domain monitoring — a hardware-side entry
whose modality set only partly overlaps this project's.

## Summary

The system is a wearable mental-health monitor in the form of a headband and earplugs, weighing
under 200 g, that measures three physiological domains simultaneously — neural (EEG), vascular
(hemoencephalography, sensed by near-infrared spectroscopy) and autonomic (heart-rate variability)
— while delivering transcranial electrical stimulation (tES) in real time. The analogue front end
is the paper's substance: a multi-loop low-noise amplifier achieving over 130 dB common-mode
rejection ratio for EEG sensing, and a capacitive correlated-double-sampling transimpedance
amplifier for the HEG and HRV channels. The measured three-domain signals are combined with
canonical correlation analysis and temporal kernel canonical correlation analysis (tkCCA) to
identify neural-vascular-autonomic coupling. The paper reports that this "supports highly accurate
classification with the 19% maximum improvement with multimodal monitoring". The stimulator is
reconfigurable to support multi-channel stimulation, after-effect maximisation monitoring and
sympathetic-nerve-disorder monitoring. The chip is 3.37 x 2.25 mm² with a two-channel EEG front
end, a two-channel NIRS front end, a NIRS current driver for a dual-wavelength VCSEL and a 6-bit
DAC current source for the tES mode, dissipating 24 mW at 2 mA stimulation current and 5 mA NIRS
driver current.

## Relevance to the review

The brief directs that this entry be marked `relevance: low` if the modality set does not overlap
enough to inform the STRUM design, and it does not. Hemoencephalography is a haemodynamic measure
with a several-second response, not one of this project's channels; heart-rate variability is
derived here from an optical earplug sensor rather than from ECG electrodes; and there is no
respiration or ocular channel. Two of the three domains therefore do not map onto what STRUM
records.

What does transfer is at the acquisition and synchronisation level, which is what the brief asked
the card to capture.

The system establishes that simultaneous acquisition of a cortical electrical signal and a
peripheral optical signal is achievable in one head-worn device at 200 g, which is the practical
constraint any dyadic or team-neuroergonomics setup runs into once a second participant's sensors
are added. The 130 dB common-mode rejection figure is the specification that makes it possible:
the EEG channel has to reject the stimulation and the optical driver currents sharing the same
head.

The tES capability is the part with no analogue in this project and it is worth naming as an
exclusion rather than leaving implied — nothing in STRUM stimulates, so the reconfigurable
stimulator, the after-effect monitoring mode and the associated artifact-rejection burden are out
of scope.

The 19% multimodal improvement is a claim about coupling-derived features from three domains
against a single domain, computed with CCA and tkCCA rather than with a classifier over
concatenated features. It is a category-3-shaped claim in a hardware paper, but the arms, the
task, the participant count and the split are all in the paywalled body.

## Notable details

- **Form factor and weight**: headband plus earplugs, under 200 g total.
- **Analogue front end**: multi-loop low-noise amplifier (MLLNA) with over 130 dB CMRR for EEG;
  capacitive correlated-double-sampling transimpedance amplifier (CCTIA) for HEG and HRV.
- **Chip**: 3.37 x 2.25 mm²; two-channel EEG front end, two-channel NIRS front end, NIRS current
  driver for a dual-wavelength VCSEL, 6-bit DAC current source for tES. Power dissipation 24 mW
  at 2 mA stimulation and 5 mA NIRS driver current.
- **Fusion method**: canonical correlation analysis and temporal kernel CCA (tkCCA), used to find
  neural-vascular-autonomic coupling rather than to classify directly.
- **Claimed multimodal benefit**: "19% maximum improvement with multimodal monitoring".
- **EEG-only number**: **reported but not accessible.** The 19% is stated as an improvement, so a
  baseline exists in the paper; its value, and which domain it corresponds to, are not in the
  abstract. IEEE Xplore is paywalled (see `meta.json.notes`).
- **Combined number**: reported but not accessible.
- **Split protocol and participant count**: **not accessible.** Neither appears in the abstract.
  For a circuits-and-systems paper the validation cohort is often very small, which is itself worth
  checking before the 19% is carried anywhere.
- **Channel count**: two EEG channels. This is an order of magnitude below a research montage and
  well below what a pretrained EEG encoder expects.
- **Title discrepancy**: the brief renders the title with "transcranial Electrical Stimulation"
  spelled out; the published title abbreviates it to "tES". The record is otherwise an exact match
  (see `meta.json.notes`).
- **Author list**: the brief names six authors; the published record has seven, adding Hoi-Jun Yoo.
- **Year discrepancy**: PubMed gives the issue as IEEE Trans Biomed Circuits Syst 9(6), 758-766,
  December 2015; Crossref and OpenAlex both record 2016, which is the online-publication year.
  This card and the bib entry use 2015, the issue of record, and the DOI suffix agrees.

## Open questions / limitations

- The three-domain coupling result is the paper's only claim relevant to this strand and none of
  its supporting numbers are accessible. The card records the claim's existence, not its
  magnitude.
- Two EEG channels cannot support any spatial analysis and would not satisfy the input contract of
  any of the pretrained EEG encoders in the `eeg-models` strand, most of which expect a named or
  positioned electrode set.
- HRV from an optical earplug sensor is a photoplethysmographic derivation, not ECG. Beat-interval
  estimates from PPG carry pulse-transit-time variability that ECG-derived intervals do not, so
  HRV features are not interchangeable between the two.
- Hemoencephalography's response is haemodynamic and therefore slow relative to a stimulus-locked
  EEG epoch. Any coupling found between HEG and EEG operates on a different timescale from the one
  this project would epoch at.
- The tES capability introduces a stimulation artifact problem that the paper solves in hardware.
  That solution is not needed here and its presence may distort the front-end design choices away
  from what a passive recording would want.
- Published in December 2015, this predates every foundation model in the corpus. Its relevance is
  to acquisition constraints, not to modelling.

## Citations

Primary: `ha-wearable-eeg-heg-hrv`

- `haque-hrv-stress-review` — the engineered-HRV feature literature this device's autonomic
  channel would feed.
- `makowski-2021-neurokit2` — a reference implementation for the HRV and PPG processing such a
  device requires downstream.
- `lee-2025-biosignal-fm-review` — the modern counterpart at the modelling rather than the
  acquisition layer.
- `schiecke-2019-brain-heart-ccm` — a more developed statistical treatment of the same
  brain-to-periphery coupling question this device's CCA analysis attempts.
- `zeng-brain-heart-ccm` — the directed-coupling framing that supersedes symmetric CCA for asking
  which system drives which.
