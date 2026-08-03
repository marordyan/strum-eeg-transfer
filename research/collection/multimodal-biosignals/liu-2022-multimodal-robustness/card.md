---
slug: liu-2022-multimodal-robustness
type: paper
strand: multimodal-biosignals
year: 2022
authors: [Liu, Qiu, Zheng, Lu]
venue: IEEE Transactions on Cognitive and Developmental Systems 14(2)
doi: 10.1109/TCDS.2021.3071170
url: https://doi.org/10.1109/TCDS.2021.3071170
license: null
modalities: [eeg, eog, ecg]
tags: [deep-canonical-correlation-analysis, bimodal-deep-autoencoder, modality-noise-ablation, robustness, seed, seed-iv, seed-v, deap, dreamer, attention-fusion, weighted-sum-fusion]
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

Systematically compares two multimodal fusion families across five datasets and then does the
thing this strand most wants: replaces the EEG features with noise and measures what is left,
which is the cleanest available operationalisation of "how much of the fused result is the
peripheral channel".

## Summary

The paper compares deep canonical correlation analysis (DCCA) and the bimodal deep autoencoder
(BDAE) for multimodal emotion recognition, contributing three things. It extends the original DCCA
model with two fusion variants, weighted-sum fusion and attention-based fusion. It compares DCCA,
BDAE and traditional approaches on five multimodal datasets. And it investigates robustness on
SEED-V and DREAMER under two manipulations: adding noise of varying amounts to the multimodal
features, and replacing the electroencephalography features with noise entirely. DCCA reaches
94.6% on SEED, 87.5% on SEED-IV, 84.3% and 85.6% on DEAP, 85.3% on SEED-V, and 89.0%, 90.6% and
90.7% on DREAMER, which the authors describe as state of the art on all five. DCCA is also
reported to be more robust when noise is added on SEED-V and DREAMER. Visualising features before
and after the DCCA transformation, the authors report that transformed features are more
homogeneous and more discriminative across emotions.

## Relevance to the review

The EEG-replacement experiment is the reason this entry is here. Adding a peripheral channel and
measuring the gain tells you the joint performance went up; destroying the EEG channel and
measuring what survives tells you how much the peripheral channel was carrying on its own inside
the fused model. Those are different questions, and only the second one distinguishes "the
peripheral signal adds information" from "the fusion architecture regularises the EEG branch".
This is the only entry in the strand that runs the second experiment, and it runs it on two
datasets.

The fusion-model comparison is secondary but useful for the project's architecture choice. DCCA
maximises correlation between per-modality projections before classification, which is a
canonically *intermediate* fusion on embeddings — the configuration this project would actually
use, with a head bolted onto frozen per-modality encoders. BDAE reconstructs both modalities from
a shared code, which is closer to early fusion in effect. That the two are compared head to head on
five datasets makes this the strand's reference point for that design decision.

The peripheral modalities differ by dataset — SEED and SEED-IV/V pair EEG with eye tracking,
DEAP pairs EEG with peripheral physiology including EOG, EMG, GSR, respiration, plethysmograph and
temperature, and DREAMER pairs EEG with ECG — so the five results together span most of the
modality combinations this project might use. The card lists `eeg`, `eog` and `ecg` on that basis;
the exact per-dataset channel sets are a `datasets-benchmarks` question.

## Notable details

- **Combined numbers** (DCCA, from the abstract): SEED 94.6%; SEED-IV 87.5%; DEAP 84.3% and 85.6%
  (two label dimensions); SEED-V 85.3%; DREAMER 89.0%, 90.6% and 90.7% (three label dimensions).
- **EEG-only number**: **reported but not accessible.** The paper compares DCCA and BDAE against
  "traditional approaches" on all five datasets, which in this literature includes unimodal
  baselines, but the abstract lists only the fused figures. IEEE Xplore is paywalled (see
  `meta.json.notes`).
- **Peripheral-only number**: reported but not accessible, same reason.
- **The modality-ablation experiment**: robustness is investigated on SEED-V and DREAMER under
  (1) adding varying amounts of noise to the multimodal features and (2) **replacing the
  electroencephalography features with noise**. The abstract states DCCA "has greater robustness
  when adding various amounts of noises" but gives no numbers for either manipulation. The
  EEG-replacement result is the single most valuable missing fact in this entry.
- **Fusion variants introduced**: weighted-sum fusion and attention-based fusion, both extensions
  of the original DCCA model.
- **Representation claim**: t-SNE-style visualisation of SEED-V features before and after the DCCA
  transformation shows the transformed features to be "more homogeneous and discriminative across
  emotions".
- **Split protocol**: **not accessible** from the abstract. The SEED family conventionally uses a
  fixed within-subject session split; DEAP and DREAMER conventions vary. This matters because
  94.6% on SEED is a within-subject number in most of this literature.
- **Participant counts**: not accessible; they are properties of the five public datasets rather
  than of this study.

## Open questions / limitations

- The EEG-replacement numbers are absent from every accessible source. Without them the entry
  documents that the experiment exists rather than what it found, which is a weaker contribution
  than the design deserves.
- Reporting "state-of-the-art results on all five data sets" invites the usual concern that model
  selection and dataset selection were not independent; the abstract gives no held-out protocol
  statement.
- Noise robustness is not the same property as modality-dropout robustness. Adding Gaussian noise
  to a feature vector degrades it smoothly; losing a channel at deployment is a structural change.
  The abstract describes the former plus one instance of the latter.
- Five datasets with different peripheral modalities are aggregated into one comparison, so a
  claim that DCCA beats BDAE does not decompose into a claim about any particular modality pair.
- DCCA maximises canonical correlation between modalities, which by construction rewards the
  *shared* component of the two signals. That is the opposite of what a project looking for
  complementary information wants, and the abstract does not address the tension.
- No cross-subject or cross-session evaluation is named in the abstract, and SEED-family results
  at 94.6% are almost certainly within-subject.

## Citations

Primary: `liu-2022-multimodal-robustness`

- `zheng-2018-emotionmeter` — the same laboratory's earlier EEG-plus-eye-movement fusion, and the
  source of the SEED-IV pairing used here.
- `ding-2025-cross-attention-fusion` — a later cross-attention model benchmarked against DCCA on
  DEAP and SEED-IV.
- `li-2023-incongruity-fusion` — the same fusion problem approached by treating cross-modal
  disagreement as information rather than as noise to be correlated away.
- `liu-eeg-multimodal-emotion-review` — the review that maps this design space, including
  incomplete-modality learning.
- Andrew et al. (2013), "Deep canonical correlation analysis" — the base method this paper extends.
