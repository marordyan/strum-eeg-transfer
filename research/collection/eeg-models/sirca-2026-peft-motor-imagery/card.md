---
slug: sirca-2026-peft-motor-imagery
type: paper
strand: eeg-models
year: 2026
authors: [Širca, Brulec, Alimardani]
venue: 2026 14th International Conference on Brain-Computer Interface (BCI), IEEE
doi: 10.1109/BCI69045.2026.11435102
url: https://doi.org/10.1109/BCI69045.2026.11435102
license: null
modalities: [scalp-eeg, motor-imagery-eeg]
tags: [lora, parameter-efficient-fine-tuning, partial-fine-tuning, few-shot, calibration, leave-one-subject-out, cnn-baseline, deepconvnet, motor-imagery, negative-results]
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

A small supervised CNN (DeepConvNet) beat both partially fine-tuned and LoRA-adapted LaBraM on
overall motor-imagery accuracy at every calibration size, but LoRA adaptation produced reliably
positive per-subject calibration gains where the CNN was more variable — so the pretrained model's
advantage in this study is adaptation robustness and cost, not accuracy.

## Summary

*This card is written from the publisher abstract and bibliographic record only; the full text is
paywalled and no open copy exists. Claims below are limited to what the abstract states.*

The study asks whether the pretrained EEG foundation model LaBraM can support minimal-calibration
motor-imagery decoding, and whether parameter-efficient fine-tuning via LoRA is an effective and
computationally cheaper adaptation route than partial fine-tuning. Using a 54-subject motor-imagery
dataset under leave-one-subject-out evaluation, the authors compare three conditions under
controlled few-shot calibration: a CNN baseline (DeepConvNet), partial fine-tuning of LaBraM, and
LaBraM with LoRA. The headline result is negative for pretraining on the accuracy axis —
DeepConvNet achieved the highest overall accuracy across all calibration sizes — and positive on
two other axes: LoRA-tuned LaBraM showed more consistent subject-wise improvements and a steeper
adaptation trajectory despite lower overall accuracy, and yielded reliably positive calibration
gains across subjects where the CNN was more variable and partial fine-tuning was unstable. On
cost, LoRA reduced trainable parameters by over two orders of magnitude and cut training time per
epoch by 35% relative to partial fine-tuning. The authors' own conclusion is that foundation models
"currently fall short of specialized CNNs in MI decoding accuracy" while parameter-efficient
fine-tuning can still deliver fast, robust personalization from limited data.

## Relevance to the review

This is the closest published analogue in the strand to the project's own comparison 1 versus
comparison 2, run under conditions this project will share: a small supervised model trained
directly on the task, versus an off-the-shelf pretrained checkpoint adapted to it, in a few-shot
regime with subject-wise (leave-one-subject-out) evaluation. Its answer is that the small supervised
model wins on accuracy. That is the outcome this project must be prepared to report, and it means a
STRUM result in which the from-scratch baseline beats the fine-tuned checkpoint would be consistent
with existing evidence rather than a sign of implementation error.

It also separates three things this project should not conflate. Accuracy, per-subject consistency
of the calibration gain, and adaptation cost came apart here: the checkpoint lost on the first and
won on the second and third. If STRUM's fine-tuned model underperforms the baseline on balanced
accuracy, "does adaptation behave more predictably across subjects" remains a separate, answerable
question rather than a consolation.

Methodologically, the LoRA-versus-partial-fine-tuning contrast is directly portable. `reve-2025`
applies LoRA to the QKVO projections as part of its own recipe, and this paper supplies independent
evidence that on a small dataset LoRA is not merely cheaper than partial fine-tuning but more
*stable* — partial fine-tuning is described as unstable. For a dataset the size of STRUM's, that
stability difference is the more consequential finding.

## Notable details

*Every line below is constrained by the abstract-only extraction. Where the paper certainly reports
a fact that is not in the abstract, this is recorded as inaccessible rather than as unreported —
those are different failures and Phase 3 should not confuse them.*

- **Pretraining corpus and its total hours**: not stated in the accessible abstract. The paper does
  not pretrain anything; it adapts a released LaBraM checkpoint, whose corpus is over 2,500 hours
  from about 20 datasets per `labram-2024`. That figure comes from the LaBraM paper, not from this
  one, and this paper does not confirm which LaBraM release it loaded.
- **Parameter count**: not stated in the accessible abstract in absolute terms. The abstract reports
  only a *ratio*: LoRA "reduced trainable parameters by over two orders of magnitude" relative to
  partial fine-tuning. Neither the LaBraM size used (Base 5.8M / Large 46M / Huge 369M per
  `labram-2024`), nor the LoRA rank, nor the DeepConvNet parameter count is accessible.
- **Input contract**: not stated in the accessible abstract. Sampling rate, window length, channel
  count and ordering, referencing, and filtering are all in the paywalled methods section. The only
  input-side facts available are that the data is scalp motor-imagery EEG from 54 subjects and that
  calibration was varied in size under a few-shot protocol. Because the model is LaBraM, its release
  contract (200 Hz, 1-second non-overlapping patches, 0.1–75 Hz band-pass, 50 Hz notch, 256-patch
  sequence cap, channel identity resolved against the 10-20 universal set) presumably applies, but
  this paper does not state it and no claim here rests on that presumption.
- **Most informative transfer number, with baseline**: **the paper reports this and the number is
  not accessible.** The abstract states the direction and the comparator without values:
  "DeepConvNet achieved the highest overall accuracy across all calibration sizes", against partial
  fine-tuning of LaBraM and LaBraM with LoRA, under leave-one-subject-out on 54 subjects. So the
  baseline is identified (DeepConvNet, a supervised-from-scratch CNN) and the sign of the effect is
  known (baseline wins), but the magnitude is behind the paywall. This card therefore satisfies the
  brief's "transfer number with its baseline" requirement only in sign and comparator, not in
  magnitude — see Open questions.
- **The one accessible quantitative result**: LoRA reduced trainable parameters by over two orders
  of magnitude and shortened training time per epoch by 35%, both relative to partial fine-tuning of
  the same model. This is an efficiency comparison between two adaptation strategies for the same
  checkpoint, not a comparison against the CNN baseline.
- **Evaluation protocol**: leave-one-subject-out, i.e. subject-wise splits with no subject appearing
  in both training and test. Combined with "controlled few-shot conditions", this makes the study a
  cross-subject transfer evaluation with a calibration-size sweep rather than a within-subject one.
- Qualitative results the abstract asserts without numbers: LoRA-tuned LaBraM had "a steeper
  adaptation trajectory"; its calibration gains were "reliably positive ... across subjects"; the
  CNN's behaviour was "more variable"; partial fine-tuning of LaBraM was "unstab[le]".
- Venue and provenance: IEEE BCI 2026, Gangwon Province, Korea, 23–25 February 2026; 7 pages;
  16 referenced works; 0 citations as of retrieval, so it has had no external scrutiny yet.

## Open questions / limitations

- **The decisive number is inaccessible.** The brief requires every category 4 card to record a
  transfer number with its baseline. This card records the baseline (DeepConvNet), the protocol
  (leave-one-subject-out, 54 subjects), and the sign (baseline higher at every calibration size),
  but not the magnitude, because the paper is paywalled with no preprint. A Phase 3 claim that
  "a supervised CNN beat LaBraM on motor imagery" is supportable from this card; a claim about *how
  much* is not, and would need the publisher version. This is a limitation of the corpus entry, not
  of the paper.
- Because only the abstract is available, none of the paper's own stated limitations are known. The
  Open questions here are consequences of the extraction, plus what the abstract itself leaves
  underdetermined — they are not the authors' caveats, and the absence of an authors' limitations
  section in this card should not be read as the paper having none.
- The 54-subject dataset is unnamed in the abstract, so overlap between it and LaBraM's pretraining
  corpus cannot be checked. If the dataset is one of the ~20 in LaBraM's pretraining set, the
  comparison is contaminated in LaBraM's favour and the CNN's win is a stronger result than it
  appears; if it is held out, the comparison is clean. This is unresolvable from accessible sources
  and matters for how much weight the result carries.
- "Partial fine-tuning" is undefined in the abstract — which layers were unfrozen is a design choice
  that plausibly drives the reported instability, so the finding that partial fine-tuning is
  unstable may be specific to one unfreezing schedule rather than general.
- Neither a frozen linear probe nor full fine-tuning appears in the abstract's condition list. The
  study compares a CNN, partial fine-tuning, and LoRA, so it does not bound what a cheaper probe or
  a fuller fine-tune would have achieved on the same data.
- Motor imagery is a within-subject motor contrast with a strong, well-localized neural correlate.
  Whether the DeepConvNet-beats-LaBraM ordering holds for a stimulus-modality contrast like STRUM's
  spoken-versus-written label is not addressed and cannot be extrapolated from one task.
- The efficiency claims (two orders of magnitude fewer trainable parameters, 35% faster per epoch)
  are measured against partial fine-tuning of LaBraM, not against training DeepConvNet from scratch.
  Since DeepConvNet is a small CNN, the total compute comparison against the winning baseline is not
  established by these figures.

## Citations

Primary: `sirca-2026-peft-motor-imagery`

- `labram-2024` — Jiang et al., ICLR 2024. The pretrained checkpoint this study adapts; the paper
  does not state which of its three sizes was used.
- Schirrmeister et al. (2017) — origin of DeepConvNet, the supervised CNN baseline that wins on
  accuracy here. Named in the brief's category 2 as a convolutional predecessor that pretraining is
  measured against, and also used as a from-scratch baseline in `lin-2026-identity-trap`.
- Hu et al., LoRA (2022) — the low-rank adaptation method whose parameter and time savings this
  paper quantifies for EEG; the same technique `reve-2025` applies to its QKVO projections.
- `reve-2025` — El Ouahidi et al., NeurIPS 2025. Independently adopts LoRA plus a two-stage
  frozen-then-unfrozen schedule as its own small-dataset fine-tuning recipe.
- `zare-2026-stress-testing` — Zare 2026. Reaches a compatible conclusion by a different route,
  reporting classical and randomly-initialised comparators that match or beat pretrained checkpoints
  on several clinical tasks.
