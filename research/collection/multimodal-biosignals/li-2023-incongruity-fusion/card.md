---
slug: li-2023-incongruity-fusion
type: paper
strand: multimodal-biosignals
year: 2023
authors: [Li, Chen, Zhu, Li, Xu, Chen]
venue: Information Fusion 105:102220
doi: 10.1016/j.inffus.2023.102220
url: https://doi.org/10.1016/j.inffus.2023.102220
license: null
modalities: [eeg, eog, ecg, eda, resp]
tags: [incongruity, cross-modal-transformer, low-rank-fusion, self-attention, primary-auxiliary-modality, deap, wesad, redundancy, intermediate-fusion, retrieval-failure]
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

Treats disagreement between physiological modalities as something to be modelled rather than
averaged away — one signal is designated primary and the rest are corrected against it by a
cross-modal transformer before low-rank fusion removes the redundancy — but no numerical result
from the paper could be retrieved from any source.

## Summary

The method designates one physiological signal as the *primary* modality on the grounds that it
performs best alone for emotion recognition, and treats the remaining signals as *auxiliary*. A
Cross Modal Transformer (CMT) optimises the auxiliary-modality features by eliminating the
incongruity among them; Low Rank Fusion (LRF) then removes the information redundancy that fusion
introduces. A modified CMT (MCMT) enhances the primary-modality feature using each optimised
auxiliary feature in turn, and a Self-Attention Transformer (SAT) is applied to the concatenation
of all the enhanced primary-modality features to exploit their common and complementary
properties. Evaluation is on DEAP and WESAD. **This summary is assembled from web-search snippets
of the publisher's abstract page, not from the paper**; see the retrieval note below and in
`source.md`.

## Relevance to the review

The incongruity framing is the reason the brief made this a required seed, and it survives even
without the numbers. Most fusion architectures in this strand implicitly assume the modalities
agree and differ only in noise; concatenation, canonical-correlation methods and shared-code
autoencoders all reward the component the signals have in common. `liu-2022-multimodal-robustness`
is the extreme case — deep canonical correlation analysis maximises exactly the shared component.
If the peripheral channel is largely a downstream copy of the central state, as
`zeng-brain-heart-ccm`'s directional asymmetry suggests, then optimising for the shared component
guarantees the peripheral channel adds nothing new.

An architecture built around *disagreement* inverts that. Incongruity between an EEG feature and
an ECG feature at the same moment is, on this view, the part that could carry information the EEG
does not already have — which is precisely the quantity the project's third comparison is trying
to measure. The primary/auxiliary asymmetry is also the right shape for this project's
configuration: a strong pretrained EEG encoder as primary, weaker peripheral encoders as
auxiliary, with the auxiliaries used to correct rather than to vote.

Whether the paper's own ablation isolates the incongruity mechanism — the second thing the brief
asked for — is unknown. The architecture has four named components (CMT, MCMT, LRF, SAT), so a
component-removal ablation is likely to exist in the paper, but it could not be seen.

## Notable details

- **Datasets**: DEAP and WESAD. Note the asymmetry: DEAP carries EEG plus peripheral physiology,
  while WESAD carries no EEG at all, so the "primary modality" cannot be EEG on both. Which signal
  is designated primary on each dataset is not recoverable, and it is the design decision the whole
  method turns on.
- **EEG-only number**: **reported but not accessible.** The paper's method is explicitly built on
  a primary modality "chosen due to its prominent performance in emotion recognition", which
  implies unimodal results were computed, but no value could be retrieved.
- **Combined number**: reported but not accessible.
- **Split protocol**: not accessible.
- **Participant count**: not accessible beyond what the two public datasets carry (DEAP 32,
  WESAD 15); the paper's own subsetting is unknown.
- **Architecture components**: Cross Modal Transformer, modified Cross Modal Transformer, Low Rank
  Fusion, Self-Attention Transformer. LRF is present specifically to counteract the redundancy
  that fusing correlated physiological channels creates, which is an unusually explicit
  acknowledgement that redundancy is the default outcome.
- **Modality list on this card** is inferred from DEAP's channel set (EEG plus EOG, EMG, GSR,
  respiration, plethysmograph, temperature) and WESAD's (ECG, EDA, EMG, respiration, temperature,
  acceleration), mapped to the controlled vocabulary. It is *not* read from the paper. Phase 3
  should treat the modality tags for this entry as provisional.
- **Bibliographic note**: OpenAlex and Semantic Scholar record the year as 2023; Crossref gives the
  issue date as May 2024. The brief and this card use 2023.

## Open questions / limitations

- **This is the strand's worst retrieval.** No abstract is deposited by Elsevier in Crossref, none
  is recorded by OpenAlex or Semantic Scholar, and ScienceDirect returns an anti-bot challenge for
  both plausible PII values. The method description above is second-hand, reconstructed from two
  independent web searches, and one contaminating sentence attributing "UAGCFNet" to this paper was
  caught and removed after a follow-up search showed UAGCFNet is a different article (Neural
  Networks, 10.1016/j.neunet.2025.107363). The description should be verified by anyone with
  ScienceDirect access before it is cited.
- Not a single numerical result is on this card. The brief's requirement that every category 3
  entry record the EEG-only number, the combined number, the split protocol and the participant
  count is unmet on all four counts, and in every case because of access rather than because the
  paper omits them.
- How incongruity is *operationalised* — the specific fact the brief asked for — is described only
  at the level of "the CMT eliminates the incongruity among auxiliary modalities". Whether that
  means a learned residual, an alignment loss, an attention mask or something else is unknown.
- Whether the ablation isolates the incongruity mechanism, the brief's second requested fact, is
  unknown.
- WESAD contains no EEG, so on that dataset the method demonstrates peripheral-to-peripheral
  fusion only. Conclusions drawn from the two datasets pooled would not be about EEG-plus-periphery.
- The primary/auxiliary designation is made on the basis of unimodal performance, which means the
  architecture's structure depends on a measurement the paper presumably reports and this card
  cannot see.

## Citations

Primary: `li-2023-incongruity-fusion`

- `liu-2022-multimodal-robustness` — the correlation-maximising alternative, which optimises for
  precisely the shared component that incongruity-aware fusion sets aside.
- `ding-2025-cross-attention-fusion` — a dual-branch cross-attention design on the same DEAP and
  SEED-IV territory.
- `kumar-2026-attention-eeg-ecg-stress` — attention-weighted fusion of EEG and ECG with an explicit
  unimodal ablation.
- `zeng-brain-heart-ccm` — the physiological reason to expect redundancy between the cortical and
  cardiac channels in the first place.
- Li, Chen et al., "Uncertainty-Aware Graph Contrastive Fusion Network for multimodal
  physiological signal emotion recognition", Neural Networks, 10.1016/j.neunet.2025.107363 — a
  later, distinct paper from an overlapping group, recorded here specifically so that it is not
  confused with this entry again.
