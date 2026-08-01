---
slug: deniz-2019-modality-invariant-semantics
type: paper
strand: candidate-datasets
year: 2019
authors: [Deniz, Nunez-Elizalde, Huth, Gallant]
venue: The Journal of Neuroscience
doi: 10.1523/JNEUROSCI.0675-19.2019
url: https://doi.org/10.1523/JNEUROSCI.0675-19.2019
license: null
modalities: [fmri, spoken-narrative, written-narrative]
tags: [label-validity, listening-vs-reading, spoken-vs-written, voxelwise-encoding-model, cross-modality-prediction, modality-invariance, naturalistic-narrative, abstract-only]
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

Participants listened to and read the same narrative stories for several hours each, and voxelwise
semantic tuning turned out to be "highly correlated in most semantically selective regions of
cortex", with models fitted in one modality accurately predicting responses in the other — so the
cognitive content of spoken and written language is close to identical, and whatever separates the
two conditions is almost entirely not the cognitive content.

## Summary

Two fMRI experiments in which participants listened to, or read, "several hours of the same
narrative stories". The authors built voxelwise encoding models characterising semantic selectivity
per voxel and per individual participant, rather than contrasting conditions at group level, which
they present as the sensitivity improvement that makes the question answerable: "previous studies
were too insensitive to determine whether semantic representations were shared at a fine level of
detail rather than merely at a coarse scale." The result is that "semantic tuning during listening
and reading are highly correlated in most semantically selective regions of cortex, and models
estimated using one modality accurately predict voxel responses in the other modality." The
significance statement puts it flatly: "although the representation of semantic information in the
human brain is quite complex, the semantic representations evoked by listening versus reading are
almost identical."

## Relevance to the review

This is the single most consequential entry in the strand for the project's stated label plan, and
its consequence is uncomfortable rather than encouraging.

The project intends to label epochs spoken versus written and to treat the resulting classifier as
saying something about cognition. This paper is the best-powered available test of whether spoken
and written language differ in their semantic representation, and its answer is that they are
"almost identical" at the level of fine-grained voxelwise tuning, with cross-modality prediction
succeeding. If the semantic representations are near-identical, then a classifier that separates
spoken from written epochs above chance is, by elimination, separating something other than
semantics — most plausibly the modality-specific sensory and perceptual response that this paper's
encoding models factor out.

That does not make a spoken-versus-written label useless. It makes the label's meaning specific:
it is a label on the sensory channel through which language arrived, not on the linguistic or
cognitive state that resulted. A card in this strand records that specification; deciding what to
do with it is Phase 4's job.

Two design elements are directly borrowable. The stimuli were the *same* narratives in both
modalities, which removes content as a confound in a way that a design with different spoken and
written materials cannot. And the analysis is per-participant rather than group-level, which is the
form in which a small-N project would have to do it anyway.

## Notable details

- **Design**: two separate experiments, listening and reading, with participants exposed to
  "several hours of the same narrative stories" in each. Same content across modalities.
- **Method**: voxelwise encoding models fitted per voxel and per individual participant to
  characterise semantic selectivity, rather than a condition contrast.
- **Main result**: "semantic tuning during listening and reading are highly correlated in most
  semantically selective regions of cortex".
- **Cross-modality prediction**: "models estimated using one modality accurately predict voxel
  responses in the other modality" — the generalisation test, passed.
- **The authors' framing of prior work**: semantic information in spoken language is represented in
  multiple cortical regions, while "amodal semantic information appears to be represented in a few
  broad brain regions"; the contribution is showing sharing at a fine rather than a coarse scale.
- **What the authors conclude**: "the representation of language semantics is independent of the
  sensory modality through which the semantic information is received."
- **What this implies for a modality classifier** (this card's inference from the authors' claim,
  not a claim of the paper): the discriminable difference between listening and reading trials lies
  outside the semantic representation.

## Open questions / limitations

- **Abstract-only card.** The Journal of Neuroscience full text could not be retrieved (see
  `meta.json`). Participant count, story durations, model specification, the exact correlation
  values behind "highly correlated", and the cross-modality prediction accuracies are all reported
  in the paper and are all unread. Nothing quantitative should be attributed to this entry.
- This is fMRI. Modality-invariance of *semantic* representation in a haemodynamic signal says
  nothing directly about what an EEG classifier at millisecond resolution would separate, and the
  early sensory components that a spoken-versus-written EEG classifier would exploit are largely
  invisible to fMRI. The two entries are complementary: this one bounds the semantic side,
  `simanova-2010-eeg-object-categories` shows the electrophysiological components on the sensory
  side.
- "Almost identical" is a qualitative summary in an abstract. The residual difference between
  listening and reading representations could be small and real, and this card cannot say how
  large it is.
- Narrative stories are one genre. Whether the invariance holds for the kind of short operational
  utterances a neuroergonomics task battery would use is untested here.

## Citations

Primary: `deniz-2019-modality-invariant-semantics`

- `simanova-2012-modality-independent` — the earlier, lower-sensitivity cross-modal decoding result
  this paper supersedes and extends.
- `simanova-2010-eeg-object-categories` — the EEG counterpart, and the entry that names the
  early sensory components differing between spoken and written presentation.
- `mous-2019` — the dataset with the same spoken-versus-written manipulation at scale, though
  between subjects and in MEG.
- `ritchie-2019-decoding-limits` — the general argument that a decodable difference need not be a
  represented distinction.
