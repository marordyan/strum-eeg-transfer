---
slug: mous-2019
type: dataset
strand: candidate-datasets
year: 2019
authors: [Schoffelen, Oostenveld, Lam, Uddén, Hultén, Hagoort]
venue: Scientific Data
doi: 10.1038/s41597-019-0020-y
url: https://doi.org/10.1038/s41597-019-0020-y
license: CC BY 4.0 (article)
modalities: [meg, fmri, mri, eog, ecg, audio]
tags: [spoken-vs-written, listening-vs-reading, between-subjects-modality, 204-subjects, ctf-275, bids, data-use-agreement, donders, scrambled-sentences, bipolar-eog-ecg]
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

The Mother Of Unification Studies is the largest dataset with the project's exact stimulus
manipulation — 102 subjects read the sentences and 102 listened to the same ones — but the
manipulation is *between* subjects, which means the spoken-versus-written contrast in it can never
be decoded within a participant, and any classifier trained on it would be decoding subject
identity as much as stimulus modality.

## Summary

A multimodal neuroimaging release from the Donders Institute and the Max Planck Institute for
Psycholinguistics covering 204 native Dutch speakers (100 male). Each participant was measured with
structural MRI, functional MRI at rest and during task, and magnetoencephalography at rest and
during task. The language task presented "linguistic utterances that either consisted of normal or
scrambled sentences. Half of the subjects were reading the stimuli, the other half listened to the
stimuli." Visual stimuli were shown word by word in a black monospaced font on grey, with a mean
per-word duration of 351 ms (300 ms minimum, 1400 ms maximum) computed from a formula tying the
visual presentation rate to the duration of the audio recording of the spoken version, the number
of letters and the number of words — so the two modalities are matched on total duration by design.
MEG used a 275-channel axial gradiometer CTF system at 1200 Hz with a 300 Hz anti-aliasing cutoff,
plus "three bipolar Ag/AgCl electrode pairs ... to measure the horizontal and vertical
electro-oculogram, and the electrocardiogram", and, for the auditory subjects, the audio signal
recorded on an analogue-to-digital channel sampled synchronously at 1200 Hz. Resting state was
5 minutes eyes-open in MEG and 7 minutes eyes-closed in fMRI. Everything is distributed in BIDS.

## Relevance to the review

This is the strand's specification of what a spoken-versus-written dataset looks like when built
properly, and it makes one design decision that the project needs to see clearly before it commits
to its own label.

The presentation-modality factor is between subjects. Every participant experienced exactly one
modality. That has a consequence the project should register: in MOUS there is no such thing as a
within-subject spoken-versus-written classifier, and any across-subject classifier trained on the
contrast is separating two disjoint groups of people, so its accuracy is confounded with subject
identity at the maximum possible strength. The `eeg-models` strand has already recorded that frozen
foundation-model embeddings are dominated by subject identity; a between-subjects modality label is
the worst possible case for that failure mode. STRUM does manipulate modality *within* subject: its
side tasks run concurrently for every participant, in a 2x2 of stimulus modality by stimulus kind,
which the full paper settled on 2026-08-01. So STRUM has the design property MOUS lacks, and the
subject-identity confound that dominates the MOUS contrast does not apply to it in the same way.

The second transferable element is the stimulus timing control. MOUS derives each word's visual
presentation duration from the duration of the spoken recording of the same sentence, so the two
modalities are matched on total stimulus duration rather than only on content. Without that, a
spoken-versus-written contrast is also a contrast in trial length, and epoch length is trivially
decodable. This is the concrete form the "auditory stimuli are spread out in time, whereas the
others are presented instantaneously" problem — flagged by `simanova-2010-eeg-object-categories` —
takes at sentence level, and MOUS shows what controlling it costs.

Finally, the peripheral inventory is exactly the project's target set minus respiration: bipolar
vertical EOG, bipolar horizontal EOG and bipolar ECG, on named channels EEG057, EEG058 and EEG059,
sampled at the same 1200 Hz as the neural data.

## Notable details

**Fixed field set:**

- **Participants**: 204 native speakers of Dutch, 100 male. Split 102 reading, 102 listening.
- **Simultaneous participants per recording**: 1.
- **Channels**: 275-channel axial gradiometer MEG (CTF), plus three bipolar peripheral pairs —
  EEG057 (bipolar vertical EOG), EEG058 (bipolar horizontal EOG), EEG059 (bipolar ECG) — plus
  UADC003/UADC004 analogue audio channels for the auditory subjects only. Also structural MRI and
  fMRI per subject.
- **Sampling rate**: MEG and peripheral channels at 1200 Hz, analogue anti-aliasing cutoff 300 Hz.
  Audio channel sampled synchronously at 1200 Hz.
- **Peripheral channels present**: vertical EOG, horizontal EOG, ECG, all bipolar. Usable as signal.
  No respiration, no electrodermal activity.
- **Total hours**: not reported as a total. Per subject: MEG resting state 5 minutes plus the
  language task, and fMRI resting state 7 minutes plus the language task.
- **Task**: sentence comprehension. Stimuli were normal sentences or word lists ("scrambled
  sentences"), presented either visually word by word or auditorily, with occasional probe
  questions.
- **Label type**: stimulus condition on two crossed factors — sentence versus word list (within
  subject) and auditory versus visual presentation (between subjects) — plus behavioural responses
  to probe questions.
- **Label source**: experimental design. Note that the paper flags a gap: "The subjects'
  performance on the probe questions is not represented as such in the `events.tsv` files", so the
  behavioural label has to be recovered from the original Presentation log files in `sourcedata`.
- **License**: article CC BY 4.0. Data licence is governed by a data use agreement rather than a
  Creative Commons licence; see `meta.json`.
- **Access route**: registration plus a click-through Data Use Agreement at the Donders Institute
  repository. The paper states that "potentially identifying data (such as imaging data) ... can
  only be shared to researchers following explicit approval of a Data Use Agreement (DUA), hence
  the requirement for registration and requesting access", and that "neither the authors nor the
  data manager is involved in granting access to specific external researchers, this is only based
  on the complete registration of the researcher and follows a 'click-through' procedure." The data
  are owned by the Max Planck Institute for Psycholinguistics (Neurobiology of Language department).

**Other specifications:**

- **Derivation scheme**: not applicable to the MEG sensors (axial gradiometers, not electrodes). The
  three peripheral channels are explicitly bipolar.
- **Head position control**: three head localiser coils at nasion and both ear canals, continuously
  monitored; subjects repositioned during breaks and "generally able to maintain a head position
  within 5 mm of the original position over the whole session".
- **Visual stimulus timing formula, quoted because it is the control that makes the modality
  contrast fair**: word duration in ms = `(nletters/sumnletters) * (audiodur + 2000 - 150*nwords)`,
  with no word shown for less than 300 ms, where `audiodur` is the duration of the audio recording
  of the spoken version of the same sentence. Each word is separated by a 300 ms blank screen.
  (Transcription note: the extraction drops the formula's operators, rendering it as
  "(nletters/sumnletters) (audiodur + 2000150 nwords)". The multiplication and the minus above are
  reconstructed from context and are not verbatim; check against the PDF before relying on the
  exact constants.)
- **Known timing offset**: the paper records a delay "on the order of slightly more than 60
  milliseconds" between the trigger and the actual auditory presentation, and notes that "detailed
  temporal alignment can be achieved comparing the audio traces in the MEG data with the
  corresponding stimulus wav-files." An uncorrected 60 ms offset is larger than most early evoked
  components.
- **No empty-room recording**: "We did not include an empty room recording in the MEG measurement
  protocol", so noise covariance must be estimated from the data.
- **Format**: BIDS, with MEG in CTF format, MRI converted DICOM-to-NIfTI, anatomical scans defaced,
  and the conversion scripts included in a `code` folder.

## Open questions / limitations

- **MEG, not EEG.** Two hundred and seventy-five axial gradiometers are not scalp electrodes, and
  no EEG checkpoint in the `eeg-models` strand ingests MEG without a substantial adaptation. This
  dataset is carded as a design comparator and a label-provenance case, not as a fine-tuning target.
- **The modality factor is between subjects**, which is the single most important thing on this
  card. It makes MOUS unusable for the exact within-subject spoken-versus-written decoding the
  project plans, and it makes any across-subject version of that decoding maximally confounded with
  subject identity.
- The behavioural responses are not in `events.tsv` and must be recovered from raw Presentation
  logs, so probe-question accuracy — the only measure of whether a participant actually comprehended
  a given trial — is not available at the level the BIDS files expose.
- The 60 ms auditory trigger delay applies only to the auditory half of the sample, so it is a
  systematic timing difference between the two modality groups on top of the group difference
  itself. It is correctable using the recorded audio traces, but only for subjects who have them.
- The data use agreement is click-through and therefore low friction, but it is still an agreement:
  the data cannot be redistributed and derived artefacts may inherit conditions the paper does not
  spell out.
- Dutch only, one site, one scanner, one MEG system. Cross-language generalisation of anything
  learned here is untested.

## Citations

Primary: `mous-2019`

- `deniz-2019-modality-invariant-semantics` — the within-subject listening-versus-reading study
  MOUS's between-subjects design cannot support, and the result that the semantic representations
  are nearly identical across the two.
- `simanova-2010-eeg-object-categories` — the EEG study naming the timing asymmetry between spoken
  and written presentation that MOUS's duration formula is designed to neutralise.
- `eeg-bids-2019` and `openneuro-2021` — the format MOUS uses, and the more permissive access model
  it does not.
- `strum-2018` — the dataset this one is a comparator for. MOUS makes concrete what a
  between-subjects modality contrast costs; STRUM's own 2x2 is within-subject, so MOUS reads as the
  cautionary comparison rather than the model to follow.
