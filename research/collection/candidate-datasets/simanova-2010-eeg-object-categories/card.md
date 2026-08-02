---
slug: simanova-2010-eeg-object-categories
type: paper
strand: candidate-datasets
year: 2010
authors: [Simanova, van Gerven, Oostenveld, Hagoort]
venue: PLoS ONE
doi: 10.1371/journal.pone.0014465
url: https://doi.org/10.1371/journal.pone.0014465
license: CC BY 4.0
modalities: [scalp-eeg, spoken-words, written-words, pictures]
tags: [label-validity, spoken-vs-written, cross-exemplar-generalization, decoding-confound, exemplar-not-category, erp-timing, 60-channel, linked-mastoids, negative-result]
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

The same eight concepts were presented as pictures, spoken words and written words, and single-trial
EEG classification succeeded — but when the classifier was tested on a *previously unseen exemplar*
it failed for words, and the authors concluded it "could not distinguish the semantic classes, but
only the exemplars, possibly through the use of perceptual differences between the exemplars".

## Summary

Twenty-four native Dutch speakers took part, four of them a pilot group, leaving twenty in the
analysis; they saw four animals and four tools, each presented eighty times in each of three
stimulus modalities: as a spoken Dutch word, as a black line drawing, and as a written Dutch word.
All exemplars were monosyllabic and matched for lemma frequency; pictures were matched for
familiarity and complexity. EEG was recorded on a 64-channel ActiCap system, 60 scalp electrodes on
an equidistant cap, filtered 0.2–200 Hz, sampled at 500 Hz, recorded against a right-mastoid
reference and converted offline to linked mastoids, with bipolar EOG computed from electrodes around
the eyes. Classification used Bayesian logistic regression with a multivariate Laplace prior on
one-second epochs from −300 ms. Within-modality single-trial accuracy reached 89 % for pictures and
was "lower though still significant for some subjects" for spoken and written words. The authors
then ran a leave-one-exemplar-out test — training on some concepts and testing on a concept the
classifier had never seen — and a cross-modal transfer-learning analysis (pictures 0.83, spoken
words 0.66, written words 0.61, these three over a hand-picked subset of four high-performing
subjects rather than the full group).

## Relevance to the review

This is the entry in the strand that speaks most directly to the project's own label plan. The
project intends to label epochs spoken versus written, which is a property of the stimulus. This
paper is the closest published case of a classifier being run over exactly those three stimulus
modalities, and its conclusion is the cautionary one.

Two findings carry over almost verbatim. First, decoding succeeded *within* modality but the
authors' own diagnosis of what it was reading is not the intended one: "for these modalities, the
classifier failed to predict the semantic category of a previously unseen item, suggesting that the
classifier could not distinguish the semantic classes, but only the exemplars, possibly through the
use of perceptual differences between the exemplars." Above-chance accuracy on the intended label
did not license the intended interpretation, and the generalization test is what revealed it. The
methodological transfer to this project is direct: if a classifier separates spoken from written
epochs, the test that distinguishes "it decoded modality of comprehension" from "it decoded the
auditory versus visual evoked response" is a held-out generalization test, not an accuracy number.

Second, the features the classifier used are locatable in time and space, and they are early and
sensory. The important features for pictures were at "central parieto-occipital sites 43 and 44
(POz, PO3)" as early as 100 ms, corresponding to "the N1-P2 waveform complex". Spoken words elicited
a centro-posterior N1 peaking at 130 ms; written words a posterior P1-N1 with a left-lateralised N1.
An early posterior visual complex and an early centro-posterior auditory complex are precisely the
low-level sensory signature that separates a visual from an auditory stimulus, which is the confound
the strand brief names.

Third, and useful as a negative result: the cross-modal transfer analysis did not recover
modality-independent semantics. The authors report that "the important electrophysiological patterns
for the cross-modal classification were largely located in occipital cortical sites", and conclude
"it is likely that picture trials biased the classification algorithm such that mostly data
features in occipital sites were selected". They offer timing as one explanation — "Auditory stimuli are spread out in time,
whereas the others are presented instantaneously" — which is itself a structural asymmetry between
spoken and written stimuli that any spoken-versus-written epoching scheme inherits.

## Notable details

- **Design**: 4 animals and 4 tools (Dutch: koe, beer, leeuw, aap; bijl, schaar, kam, pen), all
  monosyllabic, matched for frequency per million (18.25 ± 9.55, CELEX). A third "task" category
  (clothing or vegetables, varying across subjects) provided the overt response target so
  participants categorised without overtly discriminating the relevant classes.
- **Three stimulus modalities**: auditory (spoken Dutch, 16-bit, 44.1 kHz), visual (black line
  drawings on white), orthographical (written Dutch, black letters on white). Text and picture
  stimuli were shown for 300 ms.
- **Repetitions**: 80 per relevant item per modality; task items 16 repetitions, roughly one per
  ten relevant items.
- **Acquisition**: 64-channel ActiCap (Brain Products), 60 equidistant scalp electrodes, 0.2–200 Hz,
  500 Hz sampling; right-mastoid reference converted offline to linked mastoids; bipolar EOG from
  horizontal and vertical periocular electrodes. Epochs of 1 s from −300 ms.
- **Headline accuracy**: for pictures, "the highest classification accuracy reached over all
  subjects was 0.89", with "a mean value of 0.79 (SD = 0.07)" and significance for all twenty
  analysed subjects. 0.89 is the best single subject, not the group result; quoting it alone
  overstates the paper, and the mean is the number synthesis should carry. Auditory and orthographical
  "lower though still significant for some subjects" — for written words significant in only two of
  twenty subjects.
- **Cross-modal transfer learning** (Table 2): pictures 0.83 (SD 0.05), spoken words 0.66 (SD 0.04),
  written words 0.61 (SD 0.03). **These are means over four hand-picked subjects, not over the
  20-subject analysis group.**

  **Corrected 2026-08-01, Phase 4 audit.** These three figures were previously given with no
  indication of their basis, immediately alongside genuine 20-subject group means (0.79 for
  pictures, and the within-modality results above), which invited exactly the misreading the card
  is careful to head off for the 0.89 figure. The source: "For this analysis we selected a subset of
  four subjects that showed high classification accuracies in all the modalities (subjects nr 4, 5,
  7, 14)." The same applies to the importance maps this card leans on in "Relevance to the review",
  which are "averaged over five subjects that showed highest classification performance in each
  modality (Figure 5)". Neither is a group result, and neither should enter a comparison table as
  one.

  A source-internal discrepancy, recorded rather than reconciled: the body text gives "0.83 (SD =
  0.06) for pictures, 0.66 (SD = 0.02) for audio and 0.62 (SD = 0.03) for text", against Table 2's
  0.83 / 0.66 / 0.61 with SDs 0.05 / 0.04 / 0.03. The card follows Table 2 and flags that the paper
  disagrees with itself on the written-word mean and on all three standard deviations.
- **The generalization test and its outcome** — the single most transferable finding: the classifier
  "failed to predict the semantic category of a previously unseen item", and the authors' inference
  is that it separated exemplars rather than categories, "possibly through the use of perceptual
  differences between the exemplars".
- **The authors' own control observation**: "in contrast to pictures, for spoken or written words
  there are no perceptual differences that are characteristic of one or the other semantic class."
  So the perceptual-difference explanation applies at the exemplar level even where it cannot apply
  at the category level.
- **Repetition caveat raised by the authors**: "in our experiment the stimuli were repeated many
  times, and it has been shown previously that category-related effects reduce with repeated
  stimuli". They add: "These issues should be taken into account in the design of future semantic
  encoding experiments."
- **ERP morphology by modality**, useful because it names exactly the components a
  spoken-versus-written classifier would exploit: pictures — P1 at ~110 ms, visual N1 at ~160 ms,
  largest at infero-temporal and occipital sites, followed by broad negativity 280–550 ms; spoken
  words — N1 at centro-posterior sites peaking at 130 ms, P2-N2 at 220–310 ms, N400 peaking
  450–550 ms; written words — posterior P1-N1 with larger left-hemisphere N1, anterior negativity at
  100 ms, frontal negativity at ~300 ms.

## Open questions / limitations

- The decoding target here is semantic category (animals versus tools) *within* each stimulus
  modality, not stimulus modality itself. The paper does not run the spoken-versus-written classifier
  the project plans to run, so it does not report what such a classifier would score. What it
  supplies is the diagnostic procedure and the ERP evidence about which components differ between
  modalities.
- Twenty participants, eight concepts, and eighty repetitions each is a highly repetitive design.
  The authors themselves flag repetition as suppressing category effects, so the low word-modality
  accuracies may understate what a less repetitive design would achieve.
- The cross-modal analysis is confounded by the picture trials dominating feature selection, which
  the authors state as a likely explanation rather than test directly. Whether amodal semantic
  patterns exist in EEG and were missed, or do not exist at this signal-to-noise ratio, is not
  settled by this study.
- Only Dutch monosyllables, one laboratory, one task. Generalisation of the exemplar-versus-category
  finding to continuous or sentence-level language is untested here.
- The transfer-learning table reports significance values with a second value in parentheses
  (spoken words 1.7×10⁻⁵ (0.001), written words 0.02 (0.32)). The parenthetical is the
  **Bonferroni-corrected** p-value: the Table 2 footnote reads "p-values, and Bonferroni corrected
  p-values."

  **Corrected 2026-08-01, Phase 4 audit.** This bullet previously said the footnote's meaning was
  undetermined because "the extraction did not preserve [it] legibly", and declined to assert the
  uncorrected/corrected reading. The footnote is present and legible in `source.md`, four lines
  below the table. This was a false absence claim of the kind that wrongly discourages
  re-retrieval — nothing needed re-retrieving.

## Citations

Primary: `simanova-2010-eeg-object-categories`

- `simanova-2012-modality-independent` — the same group's fMRI follow-up, which explicitly trains on
  one presentation modality and tests on another; the design this paper's cross-modal analysis was
  reaching for.
- `deniz-2019-modality-invariant-semantics` — the listening-versus-reading fMRI result that finds
  semantic representation invariant to stimulus modality, and so bounds what a modality contrast can
  be about.
- `snoek-2019-confound-control` — the methodological treatment of the general problem this paper
  hits: which source of information actually drives decoding performance.
- `ritchie-2019-decoding-limits` — the argument that decodability does not establish representation,
  of which this paper is a concrete instance.
- `mous-2019` — the largest dataset in this strand with an explicit spoken-versus-written
  manipulation, though between subjects and in MEG.
