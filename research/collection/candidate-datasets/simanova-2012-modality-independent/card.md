---
slug: simanova-2012-modality-independent
type: paper
strand: candidate-datasets
year: 2012
authors: [Simanova, Hagoort, Oostenveld, van Gerven]
venue: Cerebral Cortex
doi: 10.1093/cercor/bhs324
url: https://doi.org/10.1093/cercor/bhs324
license: null
modalities: [fmri, spoken-words, written-words, photographs, natural-sounds]
tags: [label-validity, cross-modal-decoding, train-on-one-test-on-other, four-stimulus-modalities, searchlight, free-recall-control, abstract-only]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-available
pdf_path: null
md_path: source.md
md_quality: abstract-only
---

## TL;DR

The methodological answer to "is my classifier reading the stimulus or the concept": train the
decoder in one presentation modality and test it in another, and see what survives — which here
isolated left inferior temporal and frontal clusters that also discriminated categories during
free recall with no stimulus present at all.

## Summary

An fMRI study decoding semantic category with a searchlight method while participants performed a
semantic categorisation task across four stimulus modalities — spoken names, written names,
photographs and natural sounds. Classification was significant within all four. The contribution
is the cross-modal step: "Modality-independent decoding was implemented by training and testing
the searchlight method across modalities. This allowed the localization of those brain regions,
which correctly discriminated between the categories, independent of stimulus modality." That
analysis "revealed large clusters of voxels in the left inferior temporal cortex and in frontal
regions", and the authors add a further control — "these voxels also allowed category
discrimination in a free recall session where subjects recalled the objects in the absence of
external stimuli." The stated conclusion is that "semantic information can be decoded from the
fMRI signal independently of the input modality".

## Relevance to the review

This entry carries the design pattern the project needs, in a paper by the same group as
`simanova-2010-eeg-object-categories` and using the same four-category logic. Where the 2010 EEG
study found that a within-modality classifier failed to generalise to unseen exemplars, this study
shows what the positive version of the test looks like: train on one modality, test on another,
and report only what transfers.

For a project planning to label epochs spoken versus written, the implication runs in a specific
direction. This paper establishes that the *category* signal generalises across presentation
modality — which means that whatever distinguishes a spoken trial from a written trial is, by
construction, the part that does *not* generalise. A spoken-versus-written classifier is therefore
trained on precisely the modality-specific component that this literature separates out and
discards when it wants a cognitive claim. That is the strand's central concern stated the other
way round, and it comes from a paper whose own conclusion is about invariance rather than about
confounds.

The free-recall control is the other transferable idea: if the same voxels discriminate categories
with no stimulus present, the discrimination is not driven by the stimulus. An analogous
no-stimulus or post-stimulus control period is the cheapest available check on whether a
STRUM classifier is reading anything other than the sensory response.

## Notable details

- **Modalities**: four — spoken names, written names, photographs, natural sounds. This is a
  richer factorial than the three-modality EEG study, and it crosses sensory channel (auditory,
  visual) with symbolic status (linguistic, non-linguistic) rather than confounding them.
- **Method**: searchlight multivariate decoding of stimulus category from fMRI, with a semantic
  categorisation task.
- **Within-modality result**: "Significant classification performance was achieved in all 4
  modalities."
- **Cross-modal result**: training and testing across modalities localised "large clusters of
  voxels in the left inferior temporal cortex and in frontal regions".
- **Free-recall control**: the same voxels "allowed category discrimination in a free recall
  session where subjects recalled the objects in the absence of external stimuli".
- **What the authors concluded the classifier was separating**: semantic category, at the
  cross-modal clusters specifically; the abstract does not characterise what the within-modality
  classifiers were separating outside those clusters, which is where the modality-specific sensory
  response would live.

## Open questions / limitations

- **Abstract-only card.** Cerebral Cortex is paywalled with no repository copy; Europe PMC has no
  PMCID and the Oxford University Press PDF endpoint is blocked to automated retrieval. Participant
  count, scan parameters, category set, effect sizes, and the accuracy figures for each modality
  are all reported in the paper but were not accessible. See `meta.json` for what was attempted.
- This is fMRI, not EEG. The spatial cross-modal generalisation result does not transfer directly
  to a modality with no spatial resolution to speak of; the transferable content is the
  experimental logic, not the anatomy.
- The abstract makes no claim about how large the modality-specific component is relative to the
  modality-independent one. That ratio is what would determine how much of a spoken-versus-written
  EEG classifier's accuracy is sensory, and it is not recoverable from the abstract.
- Whether the cross-modal decoding was done in both directions, and whether accuracy was
  symmetric, is not stated in the abstract.

## Citations

Primary: `simanova-2012-modality-independent`

- `simanova-2010-eeg-object-categories` — the EEG predecessor from the same group, where the
  cross-modal analysis did *not* recover modality-independent patterns and the within-modality
  classifier failed on unseen exemplars.
- `deniz-2019-modality-invariant-semantics` — the same claim at much higher sensitivity, using
  voxelwise encoding models over hours of narrative rather than isolated words.
- `snoek-2019-confound-control` — the complementary approach: rather than testing generalisation
  across a nuisance factor, statistically remove it, and the ways that goes wrong.
- `ritchie-2019-decoding-limits` — the conceptual argument for why a successful decode does not by
  itself license a representational claim.
