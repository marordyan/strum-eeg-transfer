---
slug: zheng-2018-emotionmeter
type: paper
strand: multimodal-biosignals
year: 2018
authors: [Zheng, Liu, Lu, Lu, Cichocki]
venue: IEEE Transactions on Cybernetics 49(3)
doi: 10.1109/TCYB.2018.2797176
url: https://doi.org/10.1109/TCYB.2018.2797176
license: null
modalities: [eeg, eog]
tags: [seed-iv, eye-movement, modality-fusion, six-electrode-montage, wearable, cross-session, complementarity, emotion-recognition, deep-neural-network]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: abstract-only
---

## TL;DR

The most-cited demonstration that eye movements and EEG are complementary rather than redundant
for emotion recognition — fusion reaches 85.11% on four classes against a lower single-modality
result, and the two modalities are shown to be good at *different* emotions.

## Summary

EmotionMeter combines EEG with eye-movement features for four-class emotion recognition (happy,
sad, fear, neutral). To make the system wearable, the authors design a six-electrode placement
above the ears rather than a full cap. Modality fusion with multimodal deep neural networks is
reported to significantly enhance performance relative to a single modality, with a best mean
accuracy of 85.11% for the four emotions. The paper then examines where the two modalities differ:
EEG has the advantage in classifying happy, whereas eye movements outperform EEG in recognising
fear. Stability over time is tested by having each subject perform the experiment three times on
different days; across sessions, EmotionMeter obtains a mean recognition accuracy of 72.39% with
the six-electrode EEG and eye-movement features. The associated data are part of the SEED-IV
release from the same laboratory.

## Relevance to the review

The complementarity finding is the specific claim this strand needs and the reason to card an
otherwise inaccessible paper. Most fusion papers report that combining helps and stop there;
this one localises *where* the peripheral channel helps — a different emotion class from where
EEG helps — which is the shape of evidence that distinguishes genuine added information from a
redundant copy. If the project's third comparison produces a gain, the analogous check is whether
the gain is concentrated in one stimulus condition or spread evenly, and this paper is the
precedent for running it.

Two features make the transfer imperfect and worth stating. The eye-movement features come from an
SMI eye tracker, not from electrooculography, so the modality is gaze and pupil behaviour rather
than an ocular potential; the card records `eog` per the controlled vocabulary, but the
measurement is eye tracking. And the six-electrode above-the-ear montage is a deliberate reduction
that puts EEG at a disadvantage relative to a full cap, which inflates the apparent value of the
eye channel in a way that would not carry over to a high-density STRUM recording.

The cross-session number is the more useful one for this project. Within-session 85.11% drops to
72.39% across sessions on the same subjects — a 12.7-point cost from session change alone, larger
than most reported fusion gains in this strand. Any gain the project measures should be reported
against that scale.

## Notable details

- **Combined number**: best mean accuracy 85.11% for four emotions (happy, sad, fear, neutral),
  within session. Partially corroborated from a second source: `ding-2025-cross-attention-fusion`
  lists EmotionMeter at 85.11% on SEED-IV in its Table 4.
- **EEG-only number**: **reported but not accessible.** The abstract states that "modality fusion
  with multimodal deep neural networks can significantly enhance the performance compared with a
  single modality" and that EEG and eye movements have complementary strengths by emotion class,
  but gives no single-modality accuracy. IEEE Xplore is paywalled (see `meta.json.notes`).
- **Peripheral-only number**: reported but not accessible, same reason.
- **Cross-session number**: 72.39% mean recognition accuracy with the six-electrode EEG plus
  eye-movement features, over three sessions per subject on different days.
- **Complementarity**: EEG better at happy; eye movements better at fear.
- **Montage**: a six-electrode placement above the ears, chosen for feasibility and wearability.
  This is an electrode *layout* decision, not a derivation scheme.
- **Split protocol**: **not accessible.** Whether the 85.11% is within-subject or cross-subject is
  not stated in the abstract; the 72.39% is explicitly across sessions within subject, so at least
  that number is within-subject.
- **Participant count**: **not accessible** from the abstract.
- The work is the source of the SEED-IV dataset's EEG-plus-eye-movement pairing, which recurs
  throughout the multimodal emotion literature including `liu-2022-multimodal-robustness` and
  `ding-2025-cross-attention-fusion`.
- Year note: the DOI and OpenAlex record 2018 (early access); the issue of record is IEEE TCYB
  49(3), 1110–1122, 2019. 1207 citations at retrieval.

## Open questions / limitations

- The EEG-only and eye-only accuracies — the two numbers that make this a category 3 entry rather
  than a fusion-only entry — are not in the accessible text. The card records the comparison as
  reported but not its magnitude, which is a gap in this corpus's access rather than in the
  literature.
- The six-electrode montage confounds the modality comparison with an electrode-count decision.
  A fair complementarity test would compare eye movement against a full-cap EEG baseline, and this
  paper does not.
- Eye-movement features from an eye tracker are not the same measurement as EOG. The
  fear-recognition advantage may rest on pupil dilation or fixation duration, neither of which an
  EOG derivation recovers well.
- "Significantly enhance" is not accompanied in the abstract by a test statistic or a correction
  for the number of comparisons across four emotion classes and three sessions.
- The emotion labels are stimulus-induced categories in a film-clip paradigm; a class-specific
  advantage for eye movements on "fear" could reflect stimulus properties (a fear clip may have
  different visual dynamics) rather than an affective mechanism. Nothing in the abstract
  distinguishes these.
- Three sessions on different days is a genuine strength, but the 72.39% is reported without a
  matching single-modality cross-session figure, so it does not say whether fusion helps *more* or
  *less* when the session changes.

## Citations

Primary: `zheng-2018-emotionmeter`

- `liu-2022-multimodal-robustness` — the same laboratory's later systematic comparison of fusion
  models on SEED, SEED-IV, SEED-V, DEAP and DREAMER, including EEG-feature ablation.
- `ding-2025-cross-attention-fusion` — a recent SEED-IV entrant that reports 89.12% against this
  paper's 85.11%, and is the second source corroborating the 85.11% figure.
- `wibirama-cognitive-load-eye-movement` — eye-movement indices as a standalone decoder of
  cognitive state.
- `rotaru-2024-auditory-attention-bias` — why an eye-derived modality can improve a decoder
  without carrying the intended construct.
- Lu, Zheng, Li and Lu (2015), "Combining eye movements and EEG to enhance emotion recognition" —
  the earlier conference paper by an overlapping author set that this work extends.
