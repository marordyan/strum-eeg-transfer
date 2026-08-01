---
slug: ritchie-2019-decoding-limits
type: paper
strand: candidate-datasets
year: 2019
authors: [Ritchie, Kaplan, Klein]
venue: The British Journal for the Philosophy of Science
doi: 10.1093/bjps/axx023
url: https://doi.org/10.1093/bjps/axx023
license: CC BY 4.0
modalities: [conceptual-analysis, fmri, mvpa]
tags: [label-validity, decoders-dictum, decodability-vs-representation, implicit-vs-explicit-information, classifier-flexibility, behavioural-readout, linking-inference]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-available
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

The inference the authors name "the decoder's dictum" — if information can be decoded from neural
activity then that activity represents it — is argued to be false, because a sufficiently flexible
classifier can extract information that is present in the signal but that no downstream neural
process could use.

## Summary

A philosophy-of-science analysis of what multivariate pattern analysis licenses. The authors
isolate the inference underwriting most decoding papers and state it as "the decoder's dictum: If
information can be decoded from patterns of neural activity, then this provides strong evidence
about what information those patterns represent." They then argue "that it is false: decodability
is a poor guide for revealing the content of neural representations", while offering a constructive
replacement rather than only a critique — "we also suggest how the dictum can be improved on, in
order to better justify inferences about neural representation using MVPA." The argument runs
through the distinction between implicit and explicit information: information can be latent in a
signal without being in "a format that can be easily read-out by a downstream neuron in order to
guide action", and the notion of explicitness is defined "relative to some procedure for reading
out" the information. Their example is retinal ganglion cell firing, which carries all the
information the visual system acts on but not in a usable format. From this follows the
methodological corollary they endorse, citing Naselaris et al.: "non-linearity should be avoided
precisely because it is too powerful: it allows us to pull out information that is present in the
brain but could not be exploited by the brain itself", since "a sufficiently powerful nonlinear
classifier could decode almost any arbitrary feature". The constructive proposal is to tie
decodability to behavioural read-out, illustrated by a study where decodable shape-category
information existed in both retinotopic and lateral occipital cortex but only the latter showed
stronger patterns on correct than on incorrect trials.

## Relevance to the review

This is the conceptual backstop for category 3. The project's plan is to fit a classifier to a
stimulus-condition label and to read the resulting accuracy as evidence about a cognitive state.
That is the decoder's dictum applied to an EEG foundation model, and this paper is the direct
argument that the step is invalid on its own.

Two elements bear on the project concretely. The first is the flexibility warning. A pretrained
foundation-model embedding followed by a fine-tuned head is a far more powerful nonlinear extractor
than the linear classifiers this paper is arguing about, so the paper's objection applies to it
*more* strongly, not less. The `eeg-models` strand has already recorded that frozen embeddings of
several EEG checkpoints are dominated by subject identity; a model that can decode subject identity
from an embedding can very plausibly decode auditory-versus-visual stimulation from the same
embedding, and neither is evidence that the embedding represents a cognitive state.

The second is the constructive half, which gives this project something to actually do. The
behavioural read-out criterion — decodable information should discriminate correct from incorrect
trials if it is the information the participant is using — is implementable in any dataset that
logs behavioural responses. It is a stronger test than accuracy and cheaper than a new experiment.

## Notable details

- **The dictum, in the authors' own formulation**: "If information can be decoded from patterns of
  neural activity, then this provides strong evidence about what information those patterns
  represent."
- **The verdict**: false. "Decodability is a poor guide for revealing the content of neural
  representations."
- **The structure of the argument**, from the section headings: 3.1 "We don't know what information
  is decoded"; 3.2 "The theoretical basis for the dictum"; 3.3 "Undermining the theoretical basis";
  then objections 4.1 "Does anyone really believe the dictum?", 4.2 "Good decoding is not enough",
  4.3 "Predicting behaviour is not enough"; then 5 "Moving beyond the Dictum".
- **The implicit/explicit distinction**: information is explicit only "relative to some procedure
  for reading" it out. The retinal ganglion cell example makes the point that nonlinearity and noise
  "can only decrease (and never increase) the absolute amount of information present", so
  information being present says nothing about it being usable.
- **The classifier-flexibility corollary**: "it is important to restrict the flexibility of pattern
  analysis methods when measuring ensemble feature selectivity", because otherwise the result
  characterises "the analysis algorithm rather than the tuning properties of individual units within
  the brain".
- **The behavioural read-out criterion**: the illustrative study analysed spatial fMRI patterns
  during a shape-discrimination task and found that "although both retinotopic cortex and lateral
  occipital cortex (LOC) in humans contain decodable category information, only the LOC shows a
  difference in pattern strength for correct as compared to incorrect trials". Decodability was
  equal; behavioural relevance was not.
- **Scope declared by the authors**: the analysis focuses on fMRI studies of the visual system,
  for three stated reasons — that vision decoding popularised MVPA, drove its methodological
  innovation, and is the domain where functional organisation is best understood — with the
  argument that "if the dictum is viable at all, it should apply to decoding research on the visual
  system".

## Open questions / limitations

- This is a philosophical argument, not an empirical result. It supplies no numbers and no
  procedure that can be run; its contribution is a constraint on interpretation and a criterion
  (behavioural read-out) that has to be operationalised per study.
- The scope is fMRI and vision by the authors' own declaration. The extension to EEG is natural —
  the paper notes MVPA is "a unified approach for analysing data from cellular recordings, fMRI,
  EEG, and MEG" — but the specific arguments about spatial patterns and voxel selectivity do not
  map cleanly onto scalp-level time series, where the "units" whose tuning is at issue are not
  measured at all.
- The recommendation to restrict classifier flexibility sits in direct tension with the entire
  premise of transfer from a large pretrained model, which is that a high-capacity nonlinear
  representation transfers better than a hand-designed feature. The paper does not engage with that
  tension because it predates the foundation-model literature; recording it here rather than
  resolving it.
- The behavioural read-out criterion requires trials to have a correctness. A passive stimulus
  condition with no task response — which is what a spoken-versus-written listening paradigm often
  is — has no correct/incorrect split to condition on, so the criterion may not be available
  precisely where it is most needed.

## Citations

Primary: `ritchie-2019-decoding-limits`

- `snoek-2019-confound-control` — the methodological counterpart: even granting the dictum, which
  source of information drives the decode is ambiguous, and the standard remedies are biased.
- `simanova-2010-eeg-object-categories` — an empirical instance of the dictum failing in EEG: the
  classifier decoded, but not the category the label named.
- Naselaris et al. (2011) — cited here for the argument that nonlinearity in decoding "is too
  powerful" and should be avoided.
- Kriegeskorte & Kievit (2013), Haxby et al. (2014) — the representative statements of the
  decoding programme this paper is arguing against.
