---
slug: mckeen-2025-ecg-fm
type: paper
strand: multimodal-biosignals
year: 2025
authors: [McKeen, Masood, Toma, Rubin, Wang]
venue: JAMIA Open 8(5):ooaf122
doi: 10.1093/jamiaopen/ooaf122
url: https://doi.org/10.1093/jamiaopen/ooaf122
license: CC BY 4.0
modalities: [ecg]
tags: [foundation-model, electrocardiography, wav2vec2, hybrid-self-supervision, masked-reconstruction, contrastive, random-lead-masking, open-weights, linear-probing, label-efficiency, mimic-iv-ecg-benchmark]
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

An open-weight wav2vec 2.0-style ECG encoder (90.9 M parameters) pretrained on 1.4 million 5-second
12-lead segments with a hybrid masked-reconstruction plus contrastive objective, released with
weights, code and a public MIMIC-IV-ECG benchmark, and reported to beat task-specific baselines
specifically in the small-to-medium data regime.

## Summary

ECG-FM is a transformer-based foundation model for electrocardiogram analysis, built on the
wav2vec 2.0 architecture — a multi-layer CNN feature extractor producing latent representations,
feeding a BERT-like transformer encoder producing contextualised representations — with 90.9
million parameters and a 4-block feature encoder. Pretraining uses 1.4 million ECG segments drawn
from a study set of 1.5 million 12-lead ECGs, with a hybrid self-supervised objective combining
masked reconstruction and contrastive learning plus ECG-specific augmentation including Random
Lead Masking, which exposes the model to varied lead subsets so that it can later be fine-tuned on
arbitrary reduced lead sets. Waveforms are resampled to 500 Hz by linear interpolation, z-score
normalised and cut into non-overlapping 5 s segments. Downstream evaluation covers multi-label ECG
interpretation and prediction of reduced left ventricular ejection fraction, with data-scaling
experiments, latent-space structure analysis and attention-based saliency. Fine-tuned models beat
task-specific baselines in the small-to-medium data regime, and reach AUROC 0.996 for atrial
fibrillation and 0.929 for LVEF at or below 40%. The pretrained encoder is reported to show
competitive linear-probing performance. Weights, code, tutorials and a MIMIC-IV-ECG benchmark are
released at github.com/bowang-lab/ECG-FM/.

## Relevance to the review

This is the cardiac-channel counterpart to the EEG foundation models in the `eeg-models` strand,
and three of its properties map onto decisions this project has to make.

The label-efficiency claim is the one that transfers most directly. ECG-FM's advantage over
task-specific baselines is reported specifically "in the small-to-medium-scale data regime", which
is where STRUM sits. That is the same argument the EEG foundation-model literature makes, and it
means the case for a pretrained peripheral encoder rests on the same premise as the case for a
pretrained EEG encoder — with the same exposure if the premise fails, as the negative results in
the `eeg-models` strand show it sometimes does.

The linear-probing result matters because this project would use a frozen peripheral encoder with
a head on top, not a fine-tuned one. "Competitive linear probing performance, with functionally
discriminative embeddings" is the claim that configuration depends on. The paper describes the
encoder as "a robust feature-set generator", which is exactly the role a peripheral branch would
play in a fusion model.

Random Lead Masking is the closest thing in this strand to a principled answer to the brief's
"missing or corrupted channels" question. Stochastically masking leads during pretraining
produces a model that accepts arbitrary reduced lead sets at fine-tuning time. STRUM's ECG is
unlikely to be 12-lead; a model trained to tolerate lead subsets is usable where a model expecting
all twelve is not.

The input contract is 500 Hz, z-scored, 5 s non-overlapping segments. Both the rate and the window
differ from anything an EEG encoder wants, which is the concrete form of the sampling-rate
mismatch a fusion architecture has to resolve.

The endpoints are cardiological and therefore out of this project's scope as clinical claims; the
brief admits the entry because it is the primary reference for a peripheral foundation model, and
the card treats it that way.

## Notable details

- **Parameter count**: 90.9 million. Architecture is wav2vec 2.0: a 4-block multi-layer CNN
  feature extractor embedding raw signal portions into latents z_t, feeding a BERT-like
  transformer encoder producing contextualised representations c_t.
- **Pretraining scale**: 1.4 million ECG segments — the Experiments section gives the exact figure,
  "The ECG-FM model was pretrained on 1 405 625 samples using 3 A100 80GB GPUs" — from a study using
  1.5 million 12-lead ECGs.
  Note the paper states both numbers in different places (abstract: "a study using 1.5 million
  12-lead ECGs"; introduction: "pretrained on 1.4 million ECG segments") — these are consistent
  only if curation removed roughly 100,000 records, which Figure 1 apparently documents.
- **Objective**: hybrid self-supervision combining masked reconstruction and contrastive learning,
  with ECG-specific augmentation. Random Lead Masking (following Oh et al.) stochastically masks
  leads so the model can be fine-tuned on arbitrary reduced lead sets.
- **Input contract**: raw waveforms resampled to 500 Hz by linear interpolation, z-score
  normalised, segmented into non-overlapping 5 s windows.
- **Data-quality policy**: records flagged for poor data quality were deliberately *retained*, on
  the reasoning that interpretation is attempted on them in practice, "to produce a model more
  tolerant of real-world artifacts". ECGs with null values or constant-valued leads were removed.
- **Splits**: MIMIC-IV-ECG was split by patient only, because acquisition dates are imprecise;
  PhysioNet 2021 was randomly split with its evaluative sets unused; UHN-ECG was excluded from
  pretraining entirely, both for patient privacy and to serve as a cross-dataset generalisation
  test.
- **Headline downstream numbers**: AUROC 0.996 for atrial fibrillation, 0.929 for LVEF at or below
  40%.
- **Release**: weights, code, tutorials and an openly available MIMIC-IV-ECG benchmark task. The
  licence attached to the released weights is not stated in the extracted text.
- The introduction frames the field's barrier as having shifted "from data access to responsible
  model development and evaluation", which is the same framing the EEG foundation-model literature
  has adopted.

## Open questions / limitations

- Everything is 12-lead clinical ECG. A research-grade single-lead or three-lead recording
  synchronised with EEG is a different acquisition, and although Random Lead Masking is designed
  for reduced lead sets, no result in the paper evaluates a single-lead configuration.
- The tasks are diagnostic labels and an ejection-fraction threshold. Nothing evaluates a
  cognitive, affective or stimulus-locked contrast, so this card cannot say whether the embeddings
  carry state information on the timescale this project needs.
- The 5 s non-overlapping segmentation sets a floor on temporal resolution that is long relative
  to a stimulus-locked EEG epoch and short relative to reliable HRV estimation — an awkward middle
  for either use.
- Linear probing is described as "competitive" without a number anywhere in the article body. The
  frozen-encoder evidence is a data-scaling curve (Figure 3, "Label-averaged AUPRC across experiment
  suites and training dataset sizes for all tasks") and a set of supplementary tables (S6-S9); the
  Results describe it only qualitatively — "At the smallest training set sizes, Linear outperforms
  the baselines and performs comparably to Full in the MIMIC-IV-ECG machine reads and UHN-ECG
  reduced LVEF tasks; however, its performance plateaus because it lacks the representational
  capacity necessary to exploit additional downstream data." Corrected in the Phase 4 audit: an
  earlier version of this card said "the linear-probing table did not survive the two-column
  extraction cleanly". There is no such table in the article. Every per-label result is in the
  supplement, which is not part of the archived source, so the right statement is that the numbers
  are outside the archived document rather than lost in conversion.
- **Frozen-versus-fine-tuned, qualitatively**: linear probing matches full fine-tuning only in the
  smallest-data regime and plateaus thereafter. For a project intending to bolt a head onto a frozen
  peripheral encoder, that is the relevant shape and it is a warning as much as an endorsement.
- The 1.5 million versus 1.4 million discrepancy between abstract and introduction is
  reconcilable as pre- versus post-curation but is not stated as such in either place.
- Deliberately retaining poor-quality records is defensible for clinical robustness but means the
  pretraining corpus size is not a curated-hours figure, the same caveat the `eeg-models` strand
  records for large EEG corpora.
- Weight licence unrecorded, so whether the checkpoint is usable in this project is unresolved.

## Citations

Primary: `mckeen-2025-ecg-fm`

- `papagei-2024` — the optical-channel counterpart, with the same open-release posture and a
  smaller encoder.
- `lee-2025-biosignal-fm-review` — the survey placing both among biosignal foundation models.
- `haque-hrv-stress-review` — the engineered-HRV alternative to a learned cardiac encoder.
- `kumar-2026-attention-eeg-ecg-stress` — an example of using pretrained backbones over
  time-frequency ECG representations inside a fusion model.
- Oh et al., Random Lead Masking — the ECG-specific augmentation ECG-FM adopts for reduced-lead
  flexibility.
