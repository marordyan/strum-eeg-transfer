---
slug: lee-2025-biosignal-fm-review
type: paper
strand: multimodal-biosignals
year: 2025
authors: [Lee, Koliousis, Barmpas, Panagakis, Adamos, Laskaris, Zafeiriou]
venue: TechRxiv (preprint, not peer reviewed)
doi: 10.36227/techrxiv.176369849.97173246/v1
url: https://doi.org/10.36227/techrxiv.176369849.97173246/v1
license: null
modalities: [eeg, ecg, eog, ppg]
tags: [review, preprint, foundation-models, biosignals, pretraining-paradigms, unimodal, multimodal, benchmarking, interpretability, data-availability, not-peer-reviewed]
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

A survey of foundation models across biosignals — EEG, ECG, EMG, EOG and PPG — organised by data
processing, feature extraction, architecture, pretraining paradigm and evaluation, and covering
both unimodal and multimodal settings; a map of the field rather than evidence, and posted on a
server that does not peer review.

## Summary

The survey's premise is that foundation models are a promising response to the recurring
difficulties of biosignal analysis — high variability, noise, limited annotation. It introduces
the commonly used biosignals (electroencephalography, electrocardiography, electromyography,
electrooculography and photoplethysmography) and discusses their defining characteristics with
respect to training large models, which is the axis most modality-specific reviews omit. It then
surveys existing work across unimodal and multimodal settings, structured around data processing,
feature extraction, model architectures, pretraining paradigms and evaluation methods. It closes
by identifying open challenges — benchmarking, interpretability and data availability — and
possible directions. The stated aim is to guide development of robust and universal biosignal
foundation models.

## Relevance to the review

The brief surfaced this as a lead while resolving the seeds and flagged the right caution: weigh
it as a map of the field, not as evidence. Two things make the map worth having.

First, it is the only source in this strand that treats the *per-modality* question the project's
category 1 asks — what a foundation model for a peripheral signal has to contend with that an EEG
foundation model does not. Sampling rates, morphological stereotypy, artifact structure and
annotation availability all differ sharply between EEG, ECG and PPG, and a survey organised around
"their defining characteristics with respect to training large models" is organised around exactly
that difference.

Second, it explicitly covers multimodal settings alongside unimodal ones, which places it at the
junction of this strand's categories 1 and 2. The named open challenges — benchmarking,
interpretability, data availability — are the same three the `eeg-models` strand's negative
results keep running into, so a cross-modality restatement of them is useful for Phase 3's framing
even without the survey's contents.

The reasons it is not `relevance: high` are three. It is a preprint on TechRxiv, which does not
peer review. It is a secondary source in a strand whose value comes from primary ablations. And
its full text could not be retrieved, so this card records the survey's stated scope and nothing
about its contents.

## Notable details

- **Modalities surveyed**: EEG, ECG, EMG, EOG, PPG. Note EMG is named in the survey and is not in
  this strand's controlled vocabulary; the frontmatter therefore lists the four that are.
- **Organising axes**: data processing, feature extraction, model architectures, pretraining
  paradigms, evaluation methods; covered for both unimodal and multimodal settings.
- **Named open challenges**: benchmarking, interpretability, data availability.
- **Distinctive framing**: the survey discusses each biosignal's "defining characteristics with
  respect to training large models" rather than with respect to physiology or clinical use, which
  is what makes it a category 1 rather than a general-background entry.
- **Which models it covers, and any comparison table**: **reported but not accessible.** TechRxiv
  is behind a Cloudflare challenge and neither the landing page, the full-text view nor either PDF
  route returned the document (see `meta.json.notes`). WebFetch returned HTTP 403.
- **Peer-review status**: none. TechRxiv is a preprint server operated by IEEE that does not peer
  review submissions. Version 1, 2025.
- **Author affiliations** (from the OpenAlex record's author list): the group includes authors
  associated with EEG foundation-model work — Barmpas, Adamos, Laskaris and Zafeiriou appear on
  Imperial College and Cogitat-affiliated EEG deep-learning papers — so the survey's EEG coverage
  is likely to be its strongest section and its PPG and EMG coverage its weakest. That is an
  inference from the author list, not a statement about the text.
- **Licence**: OpenAlex records cc-by, but the posting's own licence statement could not be read,
  so the entry is `unknown` and no PDF is committed. If the cc-by is later confirmed on the
  posting this becomes archivable.

## Open questions / limitations

- Nothing in this card is a finding. Only the abstract was retrievable and it describes structure,
  not results.
- No peer review. Any claim taken from this survey needs its primary source checked, which is the
  normal standard for a review but is more pressing here.
- A survey listing five modalities in one paper will necessarily be uneven in depth. Which
  modalities are covered well is unknown, and the author-affiliation inference above suggests it
  will not be uniform.
- The survey is dated 2025 in a field where the EEG foundation-model literature turned over
  substantially in 2025 and 2026 (see the `eeg-models` strand), so its currency for the EEG portion
  is limited even if its framing holds.
- It is a lead for further entries and could not be used as one: no entry in this strand was
  sourced from its reference list, because the reference list is not accessible. That is the same
  failure as `liu-eeg-multimodal-emotion-review` and it means both of this strand's review-shaped
  entries contributed zero downstream entries.
- Whether it addresses the artifact-versus-signal question at all is unknown.

## Citations

Primary: `lee-2025-biosignal-fm-review`

- `papagei-2024` — an open PPG foundation model of the kind this survey maps.
- `mckeen-2025-ecg-fm` — the ECG equivalent.
- `liu-eeg-multimodal-emotion-review` — the complementary review, organised by fusion mechanism
  and centred on EEG rather than by foundation-model architecture across modalities.
- `haque-hrv-stress-review` — a single-modality, feature-engineering-era review of the cardiac
  channel, showing what the pre-foundation-model baseline looks like.
- `ha-wearable-eeg-heg-hrv` — the acquisition-hardware constraints that bound what any biosignal
  foundation model can be deployed on.
