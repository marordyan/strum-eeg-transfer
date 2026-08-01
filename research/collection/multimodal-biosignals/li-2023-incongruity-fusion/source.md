# Incongruity-aware multimodal physiology signals fusion for emotion recognition

**Authors:** Jing Li, Ning Chen, Hongqing Zhu, Guangqiang Li, Zhangyong Xu, Dingxin Chen
(author list confirmed identically by Crossref, OpenAlex and Semantic Scholar)

**Venue:** Information Fusion (Elsevier)

**Year:** OpenAlex and Semantic Scholar record 2023; Crossref records the issue date as May 2024.
The strand brief cites it as 2023, which is the online-first year. This card uses 2023 and notes
the discrepancy.

**DOI:** https://doi.org/10.1016/j.inffus.2023.102220

**Volume / article number / pages:** 105 / 102220 / 102220

**DBLP key:** journals/inffus/LiCZLXC24   **Semantic Scholar CorpusId:** 266659785

**OpenAlex open-access status:** closed. No licence recorded; Crossref lists only Elsevier
text-and-data-mining and STM-sharing policy links, i.e. no reader-facing reuse licence.

## Retrieval note

This is the one entry in the strand for which no abstract could be retrieved from any structured
source. Attempts, in order:

1. `curl` on the OpenAlex work record — the record exists and is complete for authors, venue,
   keywords and topics, but `abstract_inverted_index` is `null`.
2. Crossref work record — `abstract` field absent (Elsevier does not deposit abstracts for this
   title).
3. Semantic Scholar Graph API (`fields=abstract`) — `abstract` absent; `openAccessPdf.status`
   is `CLOSED`.
4. ScienceDirect landing page, both plausible PII values (`S1566253523005365`, which is the PII a
   web search associates with this title, and `S1566253523005043`) — both return an identical
   832 kB anti-bot challenge page with no `citation_title`, `citation_doi` or `description`
   metadata.
5. The `ouci.dntb.gov.ua` Crossref mirror — no abstract record.

## Method description recovered from web-search snippets of the publisher abstract

The text below is **not** a verbatim copy taken from the publisher. It is a paraphrase assembled
from two independent web searches that surfaced snippets of the ScienceDirect abstract page for
this exact title, and it is recorded here only so that the card can say something specific about
the method rather than nothing. It has one confirmed contamination risk, described after it.

- One physiological signal is designated the *primary* modality, on the grounds that it performs
  best alone for emotion recognition; the remaining signals are treated as *auxiliary*
  modalities.
- A **Cross Modal Transformer (CMT)** optimises the auxiliary-modality features by eliminating
  the incongruity among them.
- **Low Rank Fusion (LRF)** is then applied to remove the information redundancy that fusion
  introduces.
- A **modified CMT (MCMT)** enhances the primary-modality feature using each optimised auxiliary
  feature in turn.
- A **Self-Attention Transformer (SAT)** is applied to the concatenation of all the enhanced
  primary-modality features, to exploit the common and complementary properties among them.
- Evaluation is on the **DEAP** and **WESAD** datasets.

**Contamination risk, checked and resolved.** The first search summary that returned this
description opened by attributing an "Uncertainty-Aware Graph Contrastive Fusion Network
(UAGCFNet)" to this paper. A follow-up search established that UAGCFNet is a *different* paper —
"Uncertainty-Aware Graph Contrastive Fusion Network for multimodal physiological signal emotion
recognition", Neural Networks, DOI 10.1016/j.neunet.2025.107363, evaluated on DEAP, DREAMER and
MPED — so that sentence was discarded. The CMT / MCMT / LRF / SAT description and the DEAP +
WESAD dataset pair were returned again, independently, by the second search restricted to this
title's authors and venue, which is why they are retained here. They should still be treated as
second-hand until someone with ScienceDirect access reads the paper.

**No numerical result of any kind was recoverable** — no unimodal arm, no fused arm, no split
protocol, no participant count beyond what DEAP (32) and WESAD (15) themselves carry.

## Keywords and topics recorded by OpenAlex

Keywords: Concatenation (mathematics); Modality (human-computer interaction); Modalities;
Redundancy (engineering); Feature (linguistics); Fusion; Transformer.

Topics: Emotion and Mood Recognition; EEG and Brain-Computer Interfaces.

Cited-by count at retrieval: 40. Referenced works: 44.
