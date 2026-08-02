---
slug: muller-2024-transformers-cortical-waves
type: paper
strand: eeg-models
year: 2024
authors: [Muller, Churchland, Sejnowski]
venue: Trends in Neurosciences 47(10):788-802
doi: 10.1016/j.tins.2024.08.006
url: https://pmc.ncbi.nlm.nih.gov/articles/PMC11936488/
license: null
modalities: [cortical-lfp, multielectrode-array, voltage-sensitive-dye-imaging, ecog, meg, scalp-eeg]
tags: [theoretical-motivation, self-attention, traveling-waves, spacetime-coding, state-space-models, sequence-models, no-transfer-evidence, opinion-piece]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

An opinion piece arguing that cortical traveling waves and transformer self-attention may
implement the same computational principle — folding a sequence of past inputs into one
structured spatial pattern that can be read out in parallel — and therefore that sequence
models are not obviously foreign to neural time series. It offers no model, no dataset, and no
measurement of its own.

## Summary

Muller, Churchland and Sejnowski propose an analogy: a transformer converts a whole input
sequence into a long encoding vector over which self-attention computes pairwise associations,
and a cortical traveling wave converts a sequence of stimuli into a spatiotemporal interference
pattern over a topographic map from which both *where* and *when* a stimulus occurred can be
decoded. The core formal claim is that population activity is not separable as P(x,t) = F(x)G(t)
but takes the wave form P(x − vt), so a snapshot of cortical activity carries the recent past
rather than only the present. The paper assembles supporting evidence from other groups: waves
in awake monkey V1 propagate at the speed of unmyelinated long-range horizontal fibres and are
sparse (fewer than 1 percent of neurons in a local patch spike as a wave passes); a recurrent
network with local connectivity and distance-dependent delays produces short-term predictions
that vanish when its connections are shuffled and are not recovered by retraining; and
wave-generating locally-connected recurrent networks trained on sequence tasks converge almost
two orders of magnitude faster than randomly connected ones. It closes by connecting state-space
models to waves through the structure of Toeplitz and circulant weight matrices, of which
Mexican-hat connectivity is one instance. Every result cited is someone else's; this article
contributes the framing.

## Relevance to the review

Carded strictly as motivation, under the theoretical-motivation line of category 1, which the
brief caps at two entries. Its use to this project is to answer, at the level of plausibility
only, why a transformer pretrained on EEG might be capturing something real rather than
overfitting: if cortical dynamics already encode temporal context as spatial structure, then an
architecture whose primitive is a parallel readout over a spatial pattern is at least not
mismatched to the substrate.

Two specifics matter for how far that can be carried. First, the mechanism the authors describe
operates over a *topographic map* at the scale of a cortical area, resolved by multielectrode
arrays and voltage-sensitive dye imaging. STRUM records scalp EEG, and the paper itself says of
non-invasive recording that "signal blurring poses a significant challenge to quantifying
spatiotemporal dynamics with these noninvasive techniques". The analogy is therefore weakest at
exactly the measurement modality this project uses. Second, the authors' own prediction is about
neural recordings, not about models: they predict that reconstructing previous sensory inputs
from current population activity should succeed, and that membrane potentials and relative spike
timing should carry more information about the past than firing rates do. Neither prediction
concerns whether a pretrained EEG checkpoint transfers.

## Notable details

- **Pretraining corpus and total hours**: not applicable. No model is trained in this work.
- **Parameter count**: not applicable. No model is trained in this work.
- **Input contract**: not applicable. No checkpoint or implementation accompanies the article.
- **Most informative transfer number, with baseline**: `not reported`. The article reports no
  quantitative result of its own and no downstream task, so there is no transfer number to
  record. The nearest quantitative claim is second-hand: locally connected recurrent networks
  that generate waves train "almost two orders of magnitude faster" on complex sequence-learning
  tasks than randomly connected networks that do not, attributed to reference [53]. That is a
  comparison between two recurrent-network connectivity schemes, not between a pretrained model
  and a supervised baseline, and it is not this paper's measurement.
- **Central formal statement**: population activity is claimed to be spacetime *non-separable*,
  P(x,t) ≠ F(x)G(t), and instead of the form P(x − vt) with v the wave velocity. This is the
  precise version of the "waves carry the recent past" claim and is what a later citation should
  quote.
- **Sparseness of the waves**: in both recordings and models, fewer than 1 percent of neurons in
  a local patch spike as a wave passes, which the authors contrast with the dense waves of
  epileptic seizure. Verbatim: "when a wave passes over a local patch of cortex, only a tiny
  fraction (<1%) of the neurons spike. This profile contrasts with the dense waves that occur, for
  example, during epileptic seizures. Unlike dense waves, sparse waves propagate across single
  cortical regions along long-range horizontal fibers, modulating but not completely overwhelming
  the feedforward input." (An earlier version of this bullet quoted the last clause as "modulate
  but do not completely overwhelm", which is a re-inflection rather than the source's wording.)
- **Wave-vs-shuffle control**: the recurrent model that produces short-term predictions loses
  them when its connections are randomly shuffled, and retraining does not restore them. This is
  the article's strongest cited evidence that wave-supporting architecture, not capacity, is what
  matters.
- **Self-attention analogue**: the authors route the analogy through state-space models rather
  than through attention matrices directly, on the grounds that an SSM with a Toeplitz (and in
  particular circulant) transition matrix supports waves, and that Mexican-hat connectivity is a
  Toeplitz matrix. This is the mechanistic link they actually claim; the transformer comparison
  in the title is the looser framing.
- Scales at which waves are said to be observed: single cortical areas via arrays and optical
  imaging, whole brain via EEG, MEG and intracranial recording, in wake and in sleep.

## Open questions / limitations

- **This article cannot support any claim about whether a pretrained model transfers.** It
  reports no model, no dataset, no baseline and no evaluation. A direction paper that cites it
  as evidence that EEG foundation models work would be making an argument the source does not
  make. It supports, at most, that a sequence model is an architecturally plausible choice for
  neural time series.
- The analogy is asserted, not tested. The authors write that waves and transformers "may be
  tapping into the same computational principle", and no formal correspondence between
  self-attention and wave propagation is derived. The nearest thing to a derivation is the
  Toeplitz/circulant argument for state-space models, which relates connectivity structure to
  wave solutions but does not establish that either computes attention.
- The evidence is overwhelmingly invasive and animal: monkey V1 arrays, bat hippocampus,
  salamander and rabbit retina, rodent whole-cortex imaging. The article acknowledges that EEG
  and MEG blur the spatial structure that the argument depends on, which is a direct limitation
  on transferring the motivation to scalp recordings.
- Published as an opinion-format review in Trends in Neurosciences. Every empirical result is
  drawn from cited work, several of which are the authors' own, so the article's selectivity
  cannot be checked from the article itself.
- No open questions are raised about the analogy's failure modes. **Corrected during the Phase 4
  audit:** an earlier version described the "Outstanding questions" box as asking "how waves
  interact with spontaneous activity and across regions". It contains four questions and none is
  about spontaneous activity; three of the four are explicitly framed in transformer terms, which
  is the opposite of the earlier characterisation. Verbatim: "In the framework of transformer-like
  encoding, what would be the 'context length' of a traveling wave, and could multiple cycles of
  waves implement longer context lengths?"; "How do the properties of traveling waves change in
  different regions of cortex, or at the whole-brain scale? Could these changes be related to
  changing 'context length' in terms of transformers?"; "How can recurrent architectures, where
  nodes have dense interconnections as in the cortex, provide advantages in sequence-to-sequence
  prediction in transformer-type networks?"; "What role do feedback connections play in shaping
  traveling waves in cortex, and how could they play a role in these artificial neural network
  architectures?" The narrower original point survives: all four take the analogy as given and ask
  how to extend it, and none asks under what conditions it would be false.

## Citations

Primary: `muller-2024-transformers-cortical-waves`

- `alexander-2019-cortical-waves` — the second and final entry on this strand's
  theoretical-motivation line; supplies an empirical demonstration that large-scale wave
  structure predicts future localized signal, which is the measurable version of this article's
  premise.
- Vaswani et al., Attention is all you need (2017) — the architecture whose encoding vector the
  analogy is built on.
- Muller et al., Cortical travelling waves: mechanisms and computational principles, Nat. Rev.
  Neurosci. 19 (2018) — the authors' earlier review supplying the wave mechanism assumed here.
- Muller et al., Nat. Commun. 5:3675 (2014) — the awake-monkey V1 recording establishing that a
  small visual stimulus evokes a propagating wave.
- Gu and Dao, Mamba (2024) — the state-space-model line through which the article routes its
  proposed cortical implementation of self-attention.
