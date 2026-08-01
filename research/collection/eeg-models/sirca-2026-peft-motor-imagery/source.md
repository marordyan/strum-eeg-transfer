# Parameter-Efficient Fine-Tuning of EEG Foundation Models for Plug-and-Play Motor Imagery BCIs

**Extraction status: ABSTRACT-ONLY.** The full text of this paper is behind the IEEE Xplore
paywall. No open-access copy exists (see `meta.json.notes` for the searches run). What follows is
the publisher-supplied bibliographic record and abstract, retrieved from OpenAlex and from the
Vrije Universiteit Amsterdam institutional research portal record on 2026-07-31. No figures,
tables, methods detail, or numeric results from the paper body are reproduced here, because none
were obtained. Section and figure content referenced elsewhere in this corpus must be cited by
number against the publisher version, never quoted from here.

## Bibliographic record

| Field | Value |
| --- | --- |
| Title | Parameter-Efficient Fine-Tuning of EEG Foundation Models for Plug-and-Play Motor Imagery BCIs |
| Authors | Urban Širca (Vrije Universiteit Amsterdam, Department of Computer Science); Lovro Brulec (Technical University of Munich, Department of Mathematics); Maryam Alimardani (Vrije Universiteit Amsterdam, Department of Computer Science, corresponding author) |
| Host publication | 2026 14th International Conference on Brain-Computer Interface (BCI) [Proceedings] |
| Publication series | International Winter Conference on Brain-Computer Interface, BCI (ISSN print 2572-7672) |
| Publisher | Institute of Electrical and Electronics Engineers Inc. (IEEE) |
| Type | Conference contribution, academic, peer-reviewed |
| Pages | 1–7 (7 pages) |
| Event | 14th International Conference on Brain-Computer Interface, BCI 2026, Gangwon Province, Korea (Republic of), 23–25 February 2026 |
| Published | 2026-02-23 |
| DOI | 10.1109/BCI69045.2026.11435102 |
| ISBN (electronic) | 9798331579272 |
| ISBN (print) | 9798331579289 |
| Copyright | Publisher Copyright: © 2026 IEEE |
| Referenced works | 16 (per OpenAlex) |
| Cited by | 0 (per OpenAlex, as of 2026-07-31) |
| Open access status | Closed. OpenAlex `is_oa: false`, `oa_status: "closed"`, `best_oa_location: null` |

## Abstract

> Calibration remains a major barrier for practical motor imagery (MI) brain–computer interfaces
> (BCIs). This study investigates whether the pretrained EEG foundation model LaBraM can support
> minimal-calibration MI decoding and whether parameter-efficient fine-tuning via LoRA offers an
> effective and computationally efficient adaptation strategy. Using a 54-subject MI dataset and a
> leave-one-subject-out evaluation, we compared a CNN baseline (DeepConvNet), partial fine-tuning of
> LaBraM, and LaBraM with LoRA under controlled few-shot conditions. DeepConvNet achieved the highest
> overall accuracy across all calibration sizes, while LaBraM with LoRA showed more consistent
> subject-wise improvements and a steeper adaptation trajectory despite lower overall accuracy.
> LoRA-tuned LaBraM yielded reliably positive calibration gains across subjects, in contrast to the
> more variable behavior of the CNN and the instability of LaBraM with partial fine-tuning. In terms
> of efficiency, LoRA reduced trainable parameters by over two orders of magnitude and shortened the
> training time per epoch by 35% compared to partial fine-tuning. These findings suggest that,
> although foundation models currently fall short of specialized CNNs in MI decoding accuracy,
> parameter-efficient fine-tuning can still deliver fast and robust personalization from limited
> data, making them a promising solution for scalable plug-and-play MI-BCIs.

Source of abstract text: reconstructed from the OpenAlex `abstract_inverted_index` for work
`https://doi.org/10.1109/bci69045.2026.11435102`, and independently confirmed word-for-word against
the abstract displayed on the Vrije Universiteit Amsterdam research portal record
(`https://research.vu.nl/en/publications/a55beab3-6c6b-4e72-9078-1354866e1329`). The two sources
agree, which is the basis for treating the text above as the publisher abstract rather than a
paraphrase.

## Publisher-supplied keywords

Brain-Computer Interface (BCI); Calibration; EEG; Few-shot learning; Foundation models; Motor
Imagery

## What is NOT available in this extraction

The following are stated by the abstract to exist in the paper but are not present in any
accessible source, and must not be inferred:

- The numeric accuracies for DeepConvNet, partial-fine-tuned LaBraM, and LoRA-tuned LaBraM. The
  abstract gives the *ordering* ("DeepConvNet achieved the highest overall accuracy across all
  calibration sizes") but no values.
- The identity of the 54-subject motor-imagery dataset. The abstract says only "a 54-subject MI
  dataset".
- The calibration sizes swept, the number of MI classes, the LoRA rank and which projection matrices
  it was applied to, the channel montage, sampling rate, epoch length, and which LaBraM size
  (Base/Large/Huge) was used.
- The definition of "partial fine-tuning" — which layers were unfrozen.
- Any statistical test or variance estimate behind "more consistent subject-wise improvements" and
  "reliably positive calibration gains".
