---
slug: bendr-2021
type: paper
strand: eeg-models
year: 2021
authors: [Kostas, Aroca-Ouellette, Rudzicz]
venue: Frontiers in Human Neuroscience 15:653659
doi: 10.3389/fnhum.2021.653659
url: https://www.frontiersin.org/articles/10.3389/fnhum.2021.653659/full
license: CC BY 4.0
modalities: [scalp-eeg, clinical-eeg, 19-channel-10-20, fixed-channel-index-mapping, bipolar-mapped-to-single-site]
tags: [contrastive-objective, wav2vec2, transformer, convolutional-encoder, zero-padded-missing-channels, released-weights, motor-imagery, sleep-staging, p300, erp, transfer-ablation]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

The first transformer pretrained on EEG at corpus scale: wav2vec 2.0's contrastive objective
applied to raw clinical EEG, with the honest finding that the transformer stage is often
unnecessary downstream and that on the one large downstream dataset, fine-tuning the pretrained
model is only on par with training it from scratch.

## Summary

BENDR (BErt-inspired Neural Data Representations) adapts wav2vec 2.0 to EEG. A six-block strided
1D convolutional encoder reduces raw 256 Hz signal by a factor of 96 to a sequence of 512-length
vectors at an effective rate of about 2.67 Hz — these vectors are what the paper calls BENDR — and
an 8-layer transformer is then trained with a contrastive loss to reproduce masked BENDR vectors
against distractors sampled from elsewhere in the same sequence. Pretraining uses the Temple
University Hospital EEG corpus, and downstream evaluation covers five datasets spanning motor
imagery, error-related negativity, P300, and sleep staging, each under leave-one- or
leave-multiple-subjects-out cross-validation. The paper's design contribution is the six
fine-tuning configurations it compares, which separate the value of the convolutional stage from
the value of the transformer and from the value of pretraining at all. Its conclusions are
mixed by its own account: the configuration that discards the pretrained transformer and puts a
linear classifier on averaged BENDR vectors is the best of the six on four of five datasets,
frozen-feature configurations stay "marginally above chance", and pretraining's clearest benefit
is consistency rather than peak accuracy.

## Relevance to the review

BENDR is the convolutional-plus-contrastive predecessor that later masked-modelling papers in
this strand cite as the thing pretraining is measured against, so it sets the historical baseline
for the strand's category 2. For this project it is more useful than its age suggests, for three
reasons.

First, its handling of an unfamiliar channel set is the crudest in the strand and is stated
plainly: a fixed index mapping (Deep1010, from the DN3 library) assigns each named electrode to a
fixed position in a 20-channel tensor, surplus channels are ignored and *missing channels are set
to zero*. There is no mechanism that adapts to a layout; there is a slot per name and a zero when
the slot is empty. Second, the paper contains a montage approximation of exactly the kind this
strand has to watch: the sleep dataset SSC provides two bipolar derivations, FPz-Cz and Pz-Oz,
and the authors "simply mapped" them to FPz and Pz — the first electrode of each pair, not a
midpoint. A derivation is thereby recorded as though it were a single-site signal. Third, the
paper's own negative results are the kind Phase 4 needs: on the largest downstream dataset, the
pretrained model is only level with full supervision, and the authors attribute that to there
being enough labelled data for supervised learning to work.

## Notable details

- **Pretraining corpus and total hours**: TUEG versions 1.1 and 1.2, approximately 1.5 TB of EDF
  before preprocessing, over 10,000 subjects, some with sessions up to 8 months apart, 51 percent
  female, ages under 1 to over 90. **Total hours: `not reported`** — the paper gives corpus size
  in terabytes and in subjects, and never in hours. The string "hour" does not occur in the text.
- **Parameter count**: not given as a headline figure for the pretrained encoder. What the paper
  does state is that "the total number of parameters trained in configuration (1) is over one
  billion parameters", configuration (1) being full fine-tuning of convolutional stage plus
  transformer plus a new linear layer. The transformer is 8 layers, 8 heads, model dimension
  1536, internal feed-forward dimension printed as 3076 (see limitations). The convolutional
  stage is six blocks of 512 filters, receptive field 2 except the first at 3, strides equal to
  receptive field.
- **Input contract**: 256 Hz target, reached by whole-multiple over- or undersampling followed by
  nearest-neighbour interpolation. 19 EEG channels of the unambiguously-illustrated 10/20 set
  plus one relative-amplitude channel, so every sequence from every dataset is exactly 20
  channels; surplus channels ignored, missing channels zero-filled; reference electrodes, EOG and
  other auxiliary channels dropped. Pretraining sequences are 60 s (15,360 samples) taken every
  60 s. Downstream trials are shorter and vary per dataset (2 s for ERN and P300, 6 s for MMI and
  BCIC, 30 s for SSC), which the architecture tolerates. P300 was low-pass filtered below 120 Hz
  before resampling to avoid aliasing from its 2,048 Hz native rate.
- **Most informative transfer number, with baseline**: on the PhysioNet Motor Movement/Imagery
  dataset (MMI, 105 subjects, left/right, 5 folds), pretrained BENDR with a linear head reaches
  86.7 class-balanced accuracy. The matched baseline is the *same architecture without
  pretraining* (configuration 5, randomly initialized convolutional stage with the same linear
  head), and the paper reports that comparison **only as a figure**: Figure 5 plots all six
  configurations for all five datasets as bootstrap confidence intervals, with no numeric table.
  Its stated summary is that configuration 5 "also performed well, though less consistently,
  suggesting pre-training was needed for consistent performance". So the direction is reported
  and the magnitude is not, and this is a reporting choice by the authors rather than an access
  problem — the source does not report the paired number in extractable form.
- **The negative result on the largest dataset**: for SSC (sleep staging, 83 subjects), "for both
  the full and linear model architectures trained with the SSC data, fine-tuning the pre-trained
  model is mostly on par with the fully supervised counterpart", which the authors attribute to
  "the larger amount of data available for fully supervised learning".
- **Frozen features are not usable**: configurations 4 and 6, which keep pretrained weights fixed
  and train only later layers or the classifier, "often stayed marginally above chance,
  indicating that the pre-trained features were not sufficient without further training".
  Configuration 3 (full architecture, no pretraining) was also "generally ineffective", which the
  authors read as evidence that a transformer of this size needs pretraining or much more data.
- **Best results across the battery** (Table 2, each the best of six configurations): MMI 86.7
  balanced accuracy; BCIC 42.6 accuracy (4-class); ERN 0.65 AUROC; SSC 0.72 balanced accuracy;
  P300 0.72 AUROC. The linear-headed configuration (2) is the best-performing on four of five;
  P300 is the exception, where the transformer configuration (1) wins.
- **Contrastive-task diagnostics**: masked-position accuracy rises monotonically with evaluation
  context from 20 s to 60 s, and is nearly identical across the five downstream datasets and
  across subjects. The authors read the length dependence as evidence the contrastive task is
  being solved with signal-relevant features rather than interpolation or position recognition,
  and read the flatness across subjects as evidence of generalization — while noting that
  subject-wise variability returns as soon as the model is fine-tuned for classification.
- **Release**: source code and pretrained models at https://github.com/SPOClab-ca/BENDR;
  preprocessing built on the DN3 library at https://github.com/SPOClab-ca/dn3. No licence is
  stated for the released weights in the paper.

## Open questions / limitations

- The internal feed-forward dimension is printed as **3076**, verified against the published PDF
  rather than taken from the markdown conversion. For a model dimension of 1536 the conventional
  value would be 3072, so this is very likely a typographical error in the paper; the card
  records what the source says.
- The authors' own stated architectural limitation is that spatial information is handled poorly:
  they write that it is "presently unclear to what degree" BENDR leverages spatial information,
  and name "better isolating temporal and spatial operations" as future work. The zero-fill for
  missing channels means an absent electrode is indistinguishable from a flat one.
- Mapping the bipolar derivations FPz-Cz and Pz-Oz to FPz and Pz discards the second electrode of
  each pair entirely. The paper offers no ablation on this choice, and the SSC results — its one
  large-dataset result and its one null result — rest on it.
- Only 19 of MMI's 64 channels are used, which the authors flag when noting their MMI results are
  "reasonably competitive" rather than state of the art. The comparison to prior work on MMI and
  SSC is qualitative throughout; no table places BENDR next to a named prior method with numbers.
- The comparison to Banville and colleagues' self-supervised sleep-staging schemes is made in
  prose, and the authors explicitly say they "cannot speak to statistical significance of this
  comparison".
- Downstream results outside MMI and SSC are, in the authors' words, "not competitive with more
  targeted solutions". BCIC at 42.6 percent on a 4-class problem is barely above the 25 percent
  chance level, and ERN at 0.65 AUROC is weak.
- Sequence-length agnosticism is asserted "ostensibly" and the authors point to their own
  discussion for caveats. The contrastive-accuracy-versus-length result shows performance is in
  fact strongly length-dependent.

## Citations

Primary: `bendr-2021`

- Baevski et al., wav2vec 2.0 (2020) — the speech model whose contrastive objective, masking
  scheme, and regularization BENDR transplants to EEG.
- `banville-2021-self-supervised-eeg` — the relative-positioning and temporal-shuffling
  self-supervised schemes BENDR compares its SSC results against in prose.
- Kostas and Rudzicz, DN3 (2020) — the library supplying the Deep1010 channel mapping that fixes
  the 20-channel input tensor.
- Obeid and Picone, TUH EEG corpus (2016) — the pretraining corpus.
- Huang et al., T-Fixup (2020) — the initialization scheme that replaces the removed batch-norm
  layers in the transformer.
