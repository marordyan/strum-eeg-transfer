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
classifier could decode almost any arbitrary feature". The constructive proposal, in section 5, is
to connect behaviour to **the structure of the activation space** via a psychologically plausible
model: "if behaviour can be connected to the structure of activation space in a psychologically
plausible manner, then this may warrant the sort of inference researchers have had in mind."

**Corrected 2026-08-01, Phase 4 audit.** This passage previously read: "The constructive proposal
is to tie decodability to behavioural read-out, illustrated by a study where decodable
shape-category information existed in both retinotopic and lateral occipital cortex but only the
latter showed stronger patterns on correct than on incorrect trials." That is the option the paper
**rejects**, not the one it proposes. Section 4.3 — whose heading this card itself reproduces as
"Predicting behaviour is not enough" — closes: "In summary, merely predicting behaviour using
decodable information is not enough to revive the dictum." Section 5 opens by naming it as the
discarded alternative: "In the previous section, we considered one form of augmentation-linking
decoding results to behavioural outcomes-and argued that it was insufficient. The problem was that
linkages to behaviour do not show that the information is actually formatted in a useable way."
The Williams et al. correct-versus-incorrect study is introduced at 4.3 as "one of the earliest
indications that not all decodable information is 'read-out' in behaviour" — an illustration of the
problem, not of the remedy.

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

The second is the constructive half, which gives this project something to actually do — but it is
*not* the correct-versus-incorrect-trial test, and an earlier version of this card recommended that
test on the strength of a misreading (see the correction in the Summary). The paper argues that
linking decoding to behavioural outcomes is **insufficient**, because "linkages to behaviour do not
show that the information is actually formatted in a useable way". What it proposes instead is to
model observer behaviour from the *geometry* of the activation space — representational similarity
against psychological spaces, and predicting response latency from distance to the decision
boundary — an approach "importantly different from the dictum, as it does not rely on using linear
classifiers as a surrogate".

For this project that is a higher bar than a correct/incorrect split. Demonstrating that a
spoken-versus-written distinction is *represented* would mean showing that the embedding's
similarity structure predicts behaviour, not merely that decodable information tracks accuracy.
The correct/incorrect test remains worth running as a cheap first filter — a label that fails it is
in trouble — but passing it does not license the representational claim, which is precisely the
paper's point.

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
- **The classifier-flexibility corollary**, quoted by these authors from **Kamitani and Tong
  ([2005], p. 684)**, whom they introduce as "the first to caution against the use of non-linear
  classifiers": "nonlinear methods may spuriously reflect the feature-tuning properties of the
  pattern analysis algorithm rather than the tuning properties of individual units within the brain.
  For these reasons, it is important to restrict the flexibility of pattern analysis methods when
  measuring ensemble feature selectivity." (This bullet previously presented both strings as
  Ritchie et al.'s own words, and dropped "pattern" from "the pattern analysis algorithm".)
- **The behavioural read-out criterion, presented by the authors as insufficient** (section 4.3):
  the illustrative study analysed spatial fMRI patterns during a shape-discrimination task and found
  that "although both retinotopic cortex and lateral occipital cortex (LOC) in humans contain
  decodable category information, only the LOC shows a difference in pattern strength for correct as
  compared to incorrect trials". Both regions carry decodable information; only one tracks
  behaviour. (The source does **not** say the two regions' decodability was equal in magnitude; this
  bullet previously asserted "Decodability was equal", which is not in the paper.)
- **Scope declared by the authors**: the analysis focuses on fMRI studies of the visual system,
  for three stated reasons — that vision decoding popularised MVPA, drove its methodological
  innovation, and is the domain where functional organisation is best understood — with the
  argument that "if the dictum is viable at all, it should apply to decoding research on the visual
  system".

## Open questions / limitations

- This is a philosophical argument, not an empirical result. It reports no results of its own and
  no procedure that can be run off the shelf; its contribution is a constraint on interpretation
  plus a research programme (behaviour predicted from activation-space structure) that has to be
  operationalised per study. Note that the paper does contain accuracy figures — 86% in V1 and 65%
  in V5/+MT — but these are **Seymour et al. ([2009], p. 178)'s**, quoted as an example, not
  results of this paper. (This bullet previously said the paper "supplies no numbers", which those
  figures contradict, and previously named behavioural read-out as its criterion.)
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
