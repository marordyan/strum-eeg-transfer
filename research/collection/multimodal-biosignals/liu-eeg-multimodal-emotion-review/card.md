---
slug: liu-eeg-multimodal-emotion-review
type: paper
strand: multimodal-biosignals
year: 2024
authors: [Liu, Lou, Zhang, Wu, Xiao, Jensen, Zhang]
venue: IEEE Transactions on Instrumentation and Measurement 73
doi: 10.1109/TIM.2024.3369130
url: https://doi.org/10.1109/TIM.2024.3369130
license: null
modalities: [eeg, ecg, eog, eda, resp]
tags: [review, eeg-centred-fusion, representation-learning, incomplete-multimodal-learning, missing-modality, taxonomy, emotion-recognition, methodology-focused]
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

A methodology-first review of EEG-based multimodal emotion recognition organised around three
axes — multimodal feature representation learning, physiological signal fusion, and incomplete
multimodal learning — the third of which is the one this strand has almost no other coverage of.

## Summary

The review's stated gap is that existing surveys of emotion recognition from multimodal
physiological signals focus on general combinations of modalities without treating EEG as the
fundamental modality, and that they take a methodology-agnostic perspective concentrating on the
biomedical basis or the experimental paradigm rather than on the methodological characteristics
specific to the field. It therefore structures its coverage of what it calls EEG-based multimodal
emotion recognition (EMER) around three aspects: multimodal feature representation learning,
multimodal physiological signal fusion, and incomplete multimodal learning models. The framing
argument is that EEG's advantages — non-invasiveness, speed, high temporal resolution — combine
with a complementarity between EEG and other physiological signals to make EEG-centred fusion a
distinct problem rather than a special case of multimodal learning. The paper is 29 pages in IEEE
Transactions on Instrumentation and Measurement and had 93 citations at retrieval.

## Relevance to the review

Three things make this the right review for this strand rather than one of the several more-cited
general surveys of physiological emotion recognition.

It is EEG-centred by construction. The project's third comparison is not "fuse some physiological
signals"; it is "add peripheral channels to an EEG model". A review organised with EEG as the
fundamental modality and everything else as an addition has the same asymmetry the project has,
and the same asymmetry `li-2023-incongruity-fusion` builds into its primary/auxiliary split.

It is methodology-first. The alternative reviews in this space are organised by emotion model, by
dataset or by application; this one is organised by what the fusion machinery does, which is the
axis a design decision is made along.

Its third aspect, incomplete multimodal learning, is the one topic the brief asks about —
"handling of modality-specific sampling rates and of missing or corrupted channels" — that almost
nothing else in this strand covers. Every primary entry here assumes all channels are present at
train and test time. In a dyadic recording where one participant's ECG electrode fails, or where
respiration is unusable for part of a session, that assumption breaks, and this review is the only
pointer this strand has into the literature that addresses it.

The brief also asked that this review be mined for further entries in categories 2 and 3. That was
not possible: the paper is paywalled, its reference list is not in any accessible record, and no
entry in this strand was sourced from it. That is a real gap in the strand's coverage and is
recorded as such rather than papered over.

## Notable details

- **Type**: literature review, not primary evidence. Per the brief, its aggregate numbers are not
  to be treated as findings.
- **Three organising aspects**: (1) multimodal feature representation learning, (2) multimodal
  physiological signal fusion, (3) incomplete multimodal learning models.
- **Stated gap in prior reviews**: they cover "general combinations of modalities" without
  centring EEG, and they are "methodology-agnostic", concentrating on the biomedical basis or the
  experimental paradigms.
- **Extent**: volume 73, pages 1–29. 93 citations at retrieval.
- **Reference list**: **not accessible.** IEEE Xplore is paywalled and no repository or preprint
  copy was located (see `meta.json.notes`). The brief's instruction to mine it for further entries
  could not be carried out.
- **Which fusion taxonomies it uses, which datasets it tabulates, and which numbers it aggregates**
  are all reported but not accessible.
- **Modality list on this card** is inferred from the scope described in the abstract ("EEG and
  other physiological signals") mapped to the controlled vocabulary; the paper's actual coverage
  per modality is unknown. Treat these tags as provisional.
- **Author list**: the brief gives "Liu H, Lou T, Zhang Y, Wu Y, Xiao Y, and colleagues". The
  "and colleagues" resolves to two further authors, Christian S. Jensen and Dalin Zhang, giving
  seven in total: Huan Liu, Tianyu Lou, Yuzhe Zhang, Yixiao Wu, Yang Xiao, Christian S. Jensen,
  Dalin Zhang. That list is identical in the OpenAlex and the Crossref records, which is why it is
  carded despite the PDF being unavailable to check the title block against.

## Open questions / limitations

- Nothing in this card is evidence about the field's findings, only about how the field is
  organised, because only the abstract was accessible.
- Reviews published in instrumentation journals tend to weight sensing and measurement over
  evaluation methodology; whether this one interrogates split protocols and subject-wise
  generalisation — the failure mode that dominates the primary entries in this strand — is unknown.
- The scope is emotion recognition. The project's construct is a stimulus-modality contrast, and
  the fusion machinery may or may not transfer; the review offers no guidance visible from here.
- Coverage of the artifact-versus-signal question (category 4) is unknown. A methodology review
  that omits it would be a notable omission, and one that includes it would be a valuable pointer.
- 93 citations in roughly two years indicates the review is being used, which raises rather than
  lowers the cost of not being able to read it: whatever taxonomy it established is now the
  field's shared vocabulary and this corpus does not have it.

## Citations

Primary: `liu-eeg-multimodal-emotion-review`

- `li-2023-incongruity-fusion` — an EMER method with the same EEG-as-primary asymmetry the review
  is organised around.
- `liu-2022-multimodal-robustness` — representation learning (DCCA, BDAE) plus a modality-noise
  ablation, covering the review's first and second aspects.
- `ding-2025-cross-attention-fusion` — a recent instance of the dual-branch representation plus
  cross-attention pattern.
- `lee-2025-biosignal-fm-review` — the complementary map, organised by foundation model and
  pretraining rather than by fusion mechanism.
- `haque-hrv-stress-review` — the single-modality review counterpart for the cardiac channel.
