---
slug: mostert-2018-eye-movement-confounds
type: paper
strand: multimodal-biosignals
year: 2018
authors: [Mostert, Albers, Brinkman, Todorova, Kok, de Lange]
venue: eNeuro 5(4):ENEURO.0401-17.2018
doi: 10.1523/ENEURO.0401-17.2018
url: https://doi.org/10.1523/ENEURO.0401-17.2018
license: CC BY 4.0
modalities: [eog]
tags: [artifact-confound, meg, multivariate-decoding, visual-working-memory, gaze-position, functional-localizer, negative-result, ica-insufficient, self-correction]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

A planned working-memory decoding study was abandoned as a positive result and published as a
cautionary one: the identity of the memorised item could be decoded from two numbers — horizontal
and vertical gaze position — so the neural decoding that motivated the study was confounded, and
ICA-based artifact removal had not been sufficient to prevent it.

## Summary

Participants performed a combined visual working memory and mental imagery task while
magnetoencephalography was recorded, with gaze position and pupil dilation tracked continuously at
1200 Hz with an EyeLink 1000. The intended analysis was a three-class probabilistic classifier over
grating orientations, trained across MEG sensors with 8-fold cross-validation and extended to
temporal generalisation matrices. A control analysis repeated the identical pipeline using only
gaze position — two features, the horizontal and vertical coordinates — in place of the MEG data,
and found that the memorised orientation was decodable from gaze. The interpretation the authors
give is that "on perceiving and encoding the stimulus, subjects move their eyes in a way
systematically related to the identity of the stimulus and keep that gaze position stable
throughout the entire delay period". The paper then presents the original MEG analyses as they
would have been reported had the confound not been noticed, and proposes a remedy: train the
decoder on a separate functional localizer designed to elicit bottom-up sensory responses without
inviting stimulus-specific eye movements, then apply it to the working-memory task.

## Relevance to the review

This is the canonical demonstration that the ocular channel can produce a decoding result with no
cortical content, and it is the reference the rest of category 4 argues from. Three points bear on
this project.

The confound is *not* removed by standard preprocessing. The data had been cleaned of "regular
artifacts such as heartbeat, blinks and eye movements", and the authors state that "our results
suggest that the removal of eye movement-related artifacts was imperfect". A project that runs ICA
and considers the ocular question closed is repeating this study's original mistake. That is the
direct interaction with the epoching and cleaning choices the STRUM pipeline will make.

The confound arises from a *stimulus-locked* micro-behaviour, not from gross artifact. The eye
movements involved are small, systematic and sustained through a delay period. A spoken-versus-
written contrast is exactly the kind of manipulation that produces different, systematic and
sustained ocular behaviour by construction — reading requires saccades and listening does not — so
the mechanism this paper identifies is not merely possible in STRUM, it is close to guaranteed.

The remedy generalises. Training the decoder on a stimulus set that shares the sensory content but
not the eye-movement pattern, and testing on the task, is a design that separates the two sources.
It is more informative than a post-hoc regression, because it never lets the classifier see the
confounded distribution at training time.

The card records the paper as a `modalities: [eog]` entry, which is a deliberate abstraction: the
measurement here is video eye tracking, not electrooculography, and the recording modality is MEG,
not EEG. Neither substitution weakens the argument for this project — scalp EEG is more sensitive
to ocular potentials than MEG is, not less, and EOG electrodes measure the same corneo-retinal
dipole that the eye tracker infers from pupil position — but both should be stated when the claim
is carried forward.

## Notable details

- **Recording modality is MEG, not EEG.** The confound argument transfers to EEG a fortiori, since
  the corneo-retinal dipole projects more strongly onto scalp electrodes than onto magnetometers,
  but no EEG data are reported here.
- **The confounding decoder uses two features**: gaze x and y coordinates, run through the same
  three-class Gaussian probabilistic classifier and the same 8-fold cross-validation as the MEG
  analysis, with the signal baseline-corrected on -200 to 0 ms relative to cue onset to remove slow
  drift. The paper describes the resulting effect as significant though "only marginally" at the
  encoding stage, and stable through the delay.
- **Participants**: 36 volunteers recruited, 24 selected for the MEG experiment. The extracted text
  describing exclusions is mangled at exactly this point — it reads that "three were excluded from
  MEG analysis due to poor data quality and [...] eye movements, because the eye-tracker failed to
  track the eye reliably in those subjects" — so the exact analysed n is not recoverable from
  source.md and would need the PDF's methods paragraph.
- **Preprocessing that did not suffice**: the cleaning pipeline targeted heartbeat, blinks and eye
  movements; the authors state the eye-movement removal was imperfect. Data were then
  baseline-corrected on -200 to 0 ms relative to stimulus onset.
- **Remedy**: decoders trained on a functional localizer "specifically designed to target
  bottom-up sensory signals and as such avoids eye movements", then applied to the working-memory
  and imagery task; a continuous orientation decoder was used so that a scalar rather than a
  discrete class could be related to the true orientation.
- **The paper publishes its own wrong analysis on purpose**: "we also present the original
  analyses to highlight how these might have readily led to invalid conclusions". Very little of
  the confound literature does this, and it is what makes the entry usable as a template rather
  than only as a warning.
- Data and analysis scripts are deposited at the Donders Institute repository
  (http://hdl.handle.net/11633/di.dc-cn.DSC_3018016.04_526).
- The authors argue the phenomenon is not specific to their paradigm: "Such eye movements during
  working memory tasks have been reported before and may in fact be a common phenomenon."

## Open questions / limitations

- The paper does not quantify how much of the original MEG decoding accuracy was attributable to
  the ocular confound. It establishes that gaze carries the label; it does not report an MEG
  decoding accuracy with the gaze contribution regressed out, so the residual cortical effect is
  undetermined.
- The localizer remedy is demonstrated but not validated against a ground truth — there is no
  independent check that the localizer-trained decoder is itself gaze-free, only that the
  localizer was designed to be.
- The gaze-based decoding significance is described as marginal at encoding. A marginal effect
  that is nonetheless sufficient to invalidate a result is an uncomfortable combination, and the
  paper does not resolve how strong a gaze effect has to be before it matters.
- Sample-size accounting is unclear in the extracted text (see above), so per-subject consistency
  of the gaze effect cannot be stated from this card.
- The task is visual working memory with orientation gratings. Whether the same stimulus-specific
  gaze stabilisation occurs for auditory or linguistic stimuli — the project's case — is not
  tested, and the mechanism would be different (reading saccades rather than encoding-position
  stabilisation).

## Citations

Primary: `mostert-2018-eye-movement-confounds`

- `rotaru-2024-auditory-attention-bias` — the same argument in EEG, with an explicit EOG-only
  decoder and an additional trial-fingerprint confound.
- `wibirama-cognitive-load-eye-movement` — the mirror-image claim, that eye-movement indices are
  a legitimate decoder of cognitive state.
- Dimigen and Ehinger (2021), "Regression-based analysis of combined EEG and eye-tracking data",
  Journal of Vision 21(1):3, doi 10.1167/jov.21.1.3 — the deconvolution framework for
  co-registered EEG and eye tracking; the principled alternative to the localizer remedy. Not
  carded in this strand.
- Grootswagers et al. (2016), "Decoding dynamic brain patterns from evoked responses" — the MVPA
  tutorial whose pipeline this paper follows and then shows to be confoundable.
- `azad-2025-construction-noise` — a study whose EEG preprocessing explicitly acknowledges ocular
  sensitivity but performs no comparable control.
