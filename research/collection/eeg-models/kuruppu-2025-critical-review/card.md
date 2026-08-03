---
slug: kuruppu-2025-critical-review
type: paper
strand: eeg-models
year: 2025
authors: [Kuruppu, Wagh, Kremen, Pati, Worrell, Varatharajah]
venue: arXiv preprint 2507.11783
doi: null
url: https://arxiv.org/abs/2507.11783
license: CC BY-NC-SA 4.0 (arXiv posting)
modalities: [scalp-eeg, intracranial-eeg, clinical-eeg, sleep-eeg, bci-eeg]
tags: [critical-review, negative-result, evaluation-critique, in-distribution-evaluation, weak-scaling, channel-hours, linear-probing, benchmark-heterogeneity, time-series-foundation-models]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

A structured comparison of ten EEG foundation models finds that four of them evaluated on data
they were pretrained on, only four can be ranked against each other at all, linear probing is
"relatively worse" than fine-tuning and in several instances worse than the fully supervised
baselines it is meant to beat, and the evidence for data or model scaling is "weak, if any".
**Corrected during the Phase 4 audit:** an earlier version of this line said linear probing is
"consistently worse than the fully supervised baselines". The review does not say that, and its
own per-model summaries contradict it. What it says is "linear probing results, however, were
relatively worse", and, in the discussion, that such evaluations "have performed significantly
worse than fine-tuned versions and other baselines *in several instances*". Two of the five models
that reported linear probing go the other way: for BrainBERT, "Linear probing also achieved Area
Under the Receiver Operating Characteristic Curve (AUC) values similar to those of the fully
supervised models"; for Brant, "In the seizure detection and pathology detection tasks, both the
fine-tuned and linear probed versions of Brant outperformed other supervised and EEG-FM baselines".
Neuro-GPT is the clear negative case ("linear probing performed worse than fully-supervised
baselines"). The finding is a tendency with named exceptions, not a uniform result.

## Summary

Kuruppu and colleagues review ten early EEG foundation models — BrainBERT, Neuro-GPT, Brant, BIOT,
EEGFormer, LaBraM, Mentality, NeuroLM, FoME and BrainWave — along three axes: how the input signal
is represented, what the self-supervised objective is, and how the model was evaluated. The review
introduces *channel-hours* (recording duration multiplied by channel count) as a common unit for
pretraining volume, which makes corpora across scalp and intracranial studies comparable for the
first time in this literature. Its findings are largely negative and mostly about evaluation
rather than about architecture. Downstream comparisons are heterogeneous enough that only four of
the ten can be ranked even on the two most common tasks; four models were evaluated on datasets
that were also in their pretraining corpora; and only two, BrainWave and Brant, performed genuinely
out-of-distribution evaluation on unseen datasets. The paper closes with a list of research gaps
covering scaling evidence, preprocessing, ablations, context length, pretraining quality,
practically relevant metrics and standardized benchmarks.

## Relevance to the review

This is the strand's most systematic account of why transfer numbers from this literature should
not be taken at face value, and it supplies several specific cautions this project should apply
when choosing a checkpoint.

The most consequential for the project is the pretraining-quality gap the authors name directly:
"EEG-FM linear probing evaluations reported by some studies have performed significantly worse
than fine-tuned versions and other baselines in several instances... This contrasting observation
casts doubt on the quality of the representations learned via self-supervision in EEG-FMs." The
project's third comparison assumes an EEG embedding that peripheral physiology can be added on top
of; this review says the embeddings, as measured by the only protocol that isolates them, are not
established to be good.

Second, the review's data-scaling finding — that LaBraM's returns on TUAB and TUEV are "sharpest
under ~1000 hours of data and begin to plateau thereafter" — bears on whether a larger pretraining
corpus is a reason to prefer one checkpoint over another.

Third, the observation that general time-series foundation models sometimes beat EEG-specific ones
(TimesNet on sleep staging in FoME's evaluation, MOMENT on seizure and pathology detection in
BrainWave's) suggests a comparison this project could make cheaply and that would strengthen its
baseline set.

## Notable details

- **Pretraining corpus and total hours**: not applicable to this paper, which pretrains nothing.
  It contributes the *unit*: channel-hours, defined as total recording duration multiplied by
  number of EEG channels, tabulated for all ten models with the reviewed corpora. BrainBERT is
  listed at 4.5k channel-hours. The authors note that channel-hours or model size "could not be
  determined" for some entries, which is itself a reporting finding.
- **Parameter count**: across the ten models, "the number of trainable parameters... varied
  significantly... ranging from 3.3M in BIOT to 1.7B in NeuroLM, although most models fall within
  the 200-500M parameter range". BrainBERT is listed at 43.18M. FoME, LaBraM and NeuroLM ship
  multiple scales of the same architecture.
- **Input contract**: not applicable per se; the review's finding about input contracts is that
  "most EEG-FMs perform minimal and simple data preprocessing steps, namely filtering and
  resampling", that outlier removal, artifact suppression and site harmonization "were not
  explicitly pursued", and that normalization strategies "were not sufficiently described in most
  studies". Context length across all ten models does not exceed 90 seconds (FoME's maximum).
- **Most informative transfer number, with baseline**: `not reported`. This is a review and runs
  no experiment of its own; its comparative figures aggregate numbers whose tasks and metrics
  differ across the source papers, and the authors say so explicitly ("downstream tasks and the
  metrics differ across models"). The nearest quotable quantities are second-hand and are recorded
  as such: TUAB, the most common benchmark, "may already have saturated (85-87% accuracy) with
  traditional approaches", which sets a ceiling any pretrained model must clear; and LaBraM's
  pretraining-data scaling on TUAB/TUEV plateaus above roughly 1,000 hours.
- **In-distribution evaluation**: "in four of the ten reviewed studies (BrainBERT, Mentality,
  NeuroLM, and FoME), the downstream evaluation datasets were already used for pretraining, i.e.,
  the evaluations were in-distribution". Only BrainWave and Brant performed out-of-distribution
  evaluation on unseen datasets.
- **Rankability**: "Direct model rankings beyond the TUAB and TUEV tasks are difficult to
  determine due to heterogeneous selections of downstream tasks", and "Even when considering the
  TUAB and TUEV tasks, only four out of the ten EEG-FMs can be ranked". The number of meaningful
  classification tasks per study ranges from 1 (Mentality) to 12 (BrainWave), with most evaluating
  at most 5.
- **Linear probing versus fine-tuning**: five of ten (Brant, BrainBERT, LaBraM, EEGFormer,
  Neuro-GPT) reported linear probing at all, and "linear probing results, however, were relatively
  worse". For Neuro-GPT specifically the review records that "linear probing performed worse than
  fully-supervised baselines", while fine-tuning helped in certain configurations, and that the
  same model "performed similarly to other supervised baselines" when trained supervised without
  pretraining.
- **Scaling**: "it is unclear whether a clear and strong trend exists with model scaling,
  especially within the current EEG-FM parameter regime ranging from 3.3M (BIOT) to 1.7B
  (NeuroLM)". On data, "the evidence for data scaling is weak, if any". NeuroLM's TUAB and TUEV
  performance "was not sensitive to model size", and its HMC and Workload performance *decreased*
  with larger variants.
- **General time-series models as a live comparator**: TimesNet "performed reasonably well on
  several EEG tasks after fine-tuning and sometimes outperformed EEG-FMs (e.g., sleep-stage
  classification in FoME)"; MOMENT "outperformed EEG-FMs in specific tasks, such as seizure
  detection and pathology detection" in BrainWave's own experiments; PatchTST and CoST beat
  EEG-specific architectures on forecasting and imputation in Brant's.
- **Where pretraining does look good**: "In a majority of tasks, proposed EEG-FMs provided at
  least some improvement after fine-tuning, if not drastic, over previous DL and self-supervised
  baselines", and "Fine-tuned EEG-FMs showed substantial improvements over classical machine
  learning models with expert features — although such assessments were reported in only four
  studies".
- **Spatial modelling is neglected**: "the modeling of spatial EEG relationships was either
  ignored or limited to the positional encoding step", with BrainWave the exception for having a
  spatial attention mechanism; Brant's own ablation found its temporal encoder contributed more
  than its spatial encoder or frequency encoding.
- Pretraining objective: masked reconstruction of temporal sequences predominates; three models
  (LaBraM, NeuroLM, EEGFormer) add a learned discrete codebook. Mentality is the only non-
  transformer, using a Mamba architecture.

## Open questions / limitations

- The set of ten models is not the current field. CBraMod, EEGPT and REVE are not reviewed — the
  strings "CBraMod", "EEGPT" and "NeuroGPT" (as opposed to "Neuro-GPT") do not appear — so the
  claim that only four models can be ranked is a claim about this set, made at the v1 cutoff of
  July 2025 (this card reads v3, December 2025).
- The review's comparative figures place numbers from different papers on shared axes while
  stating that the tasks and metrics differ across them. The authors flag this, but the figures
  are still the visual basis for the scaling and paradigm conclusions, and no statistical
  aggregation is performed.
- Channel-hours is introduced as a normalizing unit but conflates a long single-channel recording
  with a short high-density one, and the review does not test whether it predicts anything. It is
  a bookkeeping convenience, not a validated measure of pretraining volume.
- BrainBERT is included even though it did not meet the search criteria, "because of its common
  presence as a baseline in other EEG-FM evaluations". This is a defensible choice but means the
  ten are not a clean sample of any defined population.
- Most of the review's negative conclusions are about *reporting* rather than about model
  capability: heterogeneous evaluation, undescribed normalization, missing ablations. Whether
  EEG-FMs actually fail to transfer, as opposed to not having been measured properly, is left
  open — which is precisely the question this strand's other category 5 entries attack directly.
- No reproduction is attempted. Every number is taken from the reviewed papers, so the review
  inherits any error in them.

## Citations

Primary: `kuruppu-2025-critical-review`

- `biot-2023` — the smallest of the ten reviewed models at 3.3M parameters as this review counts
  them, and one of the four that can be ranked on TUAB/TUEV.
- `labram-2024` — the review's leading model on TUAB and TUEV, and the source of the ~1,000-hour
  data-scaling plateau the review highlights.
- `brainwave` — named as the notable exception on evaluation breadth (12 tasks) and the only model
  with both out-of-distribution evaluation and a spatial attention mechanism.
- `bendr-2021` — recurring fully-supervised or self-supervised baseline in the reviewed
  evaluations (Neuro-GPT's and Brant's).
- Goswami et al., MOMENT, and Wu et al., TimesNet — general time-series foundation models that
  beat EEG-specific models on some EEG tasks in the reviewed papers' own experiments.
