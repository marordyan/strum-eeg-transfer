---
slug: banville-2021-self-supervised-eeg
type: paper
strand: eeg-models
year: 2021
authors: [Banville, Chehab, Hyvärinen, Engemann, Gramfort]
venue: Journal of Neural Engineering 18(4):046020
doi: 10.1088/1741-2552/abca18
url: https://arxiv.org/abs/2007.16104
license: null
modalities: [scalp-eeg, clinical-eeg, polysomnography, 2-channel-frontal, 21-channel-10-20]
tags: [relative-positioning, temporal-shuffling, contrastive-predictive-coding, autoencoder-baseline, pretext-task-design, linear-probe, low-label-regime, sleep-staging, pathology-detection, handcrafted-feature-baseline]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: clean
---

## TL;DR

Three temporal-context pretext tasks — is this window near that one, are these three windows in
order, and does this window follow that context — turn out to be enough to make a linear probe on
frozen EEG features beat a fully supervised network by up to 22.8 points in the one-label-per-class
regime, while a reconstruction autoencoder on the same architecture barely beats random weights.

## Summary

This is the paper that established pretext-task design as the operative variable in EEG
self-supervision. Four objectives are compared on identical convolutional encoders: relative
positioning (RP), which classifies whether two windows fall within τ_pos of each other or beyond
τ_neg; temporal shuffling (TS), which classifies whether three windows are in temporal order;
contrastive predictive coding (CPC), which replaces the single anchor with an autoregressively
summarized context and asks which of N+1 candidate windows actually follows; and a plain
autoencoder. Feature extractors are then frozen and a linear logistic regression is trained on
labelled examples, with the number of labels per class swept from one to all. Evaluation covers
sleep staging on the PhysioNet Challenge 2018 dataset (994 recordings, 5 classes) and pathology
detection on TUH Abnormal (2,993 recordings, 2 classes), against three baselines: a fully
supervised deep network, a random forest on handcrafted features, and the same architecture with
random weights. The headline finding is regime-dependent — SSL features dominate when labels are
scarce, and full supervision catches up and passes them only above roughly 10,000 examples per
class, and then only by 1.6 to 3.5 percent.

## Relevance to the review

This is the strand's clearest statement of what a pretraining *objective* buys, isolated from
architecture, because every objective here is trained on the same encoder and read out by the
same linear probe. Two of its results bear directly on this project's design.

The first is the shape of the curve. STRUM is a small dataset, and this paper measures exactly
the axis that matters: at one labelled example per class the SSL advantage over full supervision
is 22.8 points, and it shrinks monotonically until it inverts around 10,000 examples per class.
That is the quantitative form of "pretraining helps when labels are scarce", measured rather than
asserted, and it is the evidence base for expecting comparison 2 to beat comparison 1 at all.

The second is the negative control. The autoencoder, trained with mean squared error on the same
data and architecture, "could not compete" and on TUHab never exceeded 53.0 percent against a
50 percent chance level. The authors' explanation is mechanistic and worth carrying: MSE
reconstruction is dominated by low frequencies, which carry the largest amplitudes under EEG's
1/f power law and the least neurobiological information. A masked-reconstruction objective on
raw signal is not automatically informative; the paper shows one that is not.

## Notable details

- **Pretraining corpus and total hours**: no separate pretraining corpus. Self-supervision runs
  on the *unlabelled* version of the same two datasets used downstream, which is what makes the
  comparison clean. PC18: 994 overnight recordings from 994 individuals with suspected sleep
  apnoea, mean age 55, 33 percent female. TUHab v2.0.0: 2,993 recordings of 15 minutes or more
  from 2,329 patients, mean age 49.3, 53.5 percent of recordings female. **Total hours: `not
  reported as an hour figure`, partly reconstructible (narrowed during the Phase 4 audit).** An
  earlier version of this bullet said the retained duration "cannot be reconstructed". That is
  true only of TUHab. The paper never states hours anywhere, but Table 1 gives PC18's window
  counts, and 891,668 non-overlapping 30 s windows is about 7,430 hours. For TUHab the
  reconstruction does fail, because the first minute of each recording is cropped and "Longer
  files were also cropped such that a maximum of 20 minutes was used from each recording", so the
  2,993 recordings of "15 minutes or more" have no recoverable total.
- **Parameter count: 62,307 and 170,860 (corrected during the Phase 4 audit).** An earlier version
  of this bullet recorded the parameter count as `not reported` and said the paper "gives no
  parameter total". The paper gives two, one per embedder, and it uses two embedders, not one.
  StagerNet, on PC18: a 3-layer convolutional network adapted from prior sleep-staging work with
  16 convolutional channels (twice the original 8) plus batch normalization, producing a
  100-dimensional embedding — "This yielded a total of 62,307 trainable parameters." ShallowNet,
  on TUHab, taken as-is from prior TUH Abnormal work with only the output dimensionality changed
  to D = 100 — "This yielded a total of 170,860 trainable parameters." CPC additionally uses a GRU
  with hidden size 100. The "relatively small" remark the earlier version leaned on is about model
  capacity in the discussion, not a substitute for the counts. What changes: this paper is now the
  strand's smallest measured encoder by a wide margin, and its low-label advantage can be put on a
  cost footing after all.
- **Input contract**: differs by dataset, and the paper does not impose a common one. PC18: 30 Hz
  FIR low-pass with a Hamming window, downsampled to 100 Hz, restricted to channels F3-M2 and
  F4-M1, non-overlapping 30 s windows of shape 3000 x 2, native rate 200 Hz, referenced to M1 or
  M2. TUHab: first minute cropped, at most 20 minutes retained per recording, 21 channels common
  to all recordings (Fp1, Fp2, F7, F8, F3, Fz, F4, A1, T3, C3, Cz, C4, T4, A2, T5, P3, Pz, P4,
  T6, O1, O2), downsampled to 100 Hz, clipped at ±800 µV, non-overlapping 6 s windows of shape
  600 x 21, native rates 250/256/512 Hz, common average reference. Both: windows with
  peak-to-peak amplitude below 1 µV rejected, then channel-wise z-scoring.
- **Most informative transfer number, with baseline**: on PC18 sleep staging, SSL features with a
  linear probe reach up to 72.3 percent balanced accuracy (5-class, chance 20 percent), and the
  gap over the fully supervised network "was as high as 22.8 points when only one example per
  class was available". The gap stays in SSL's favour up to roughly 10,000 examples per class, at
  which point full supervision overtakes it "by a 1.6-3.5% margin only". Against the handcrafted
  feature baseline, SSL wins above 100 examples per class by up to 5.6 points for CPC. On TUHab
  the best SSL result is 79.4 percent (2-class, chance 50 percent), CPC beats full supervision
  below 10,000 labelled examples per class and is within about 1 percent of it at full labels,
  and CPC beats handcrafted features by 3.8 to 4.8 points.
- **The autoencoder null**: AE features and random-weight features "obtained much lower
  performance"; on TUHab the AE "never exceeded 53.0%" against 50 percent chance. The authors
  attribute this to the MSE loss concentrating on low frequencies with the largest amplitudes
  under 1/f dynamics.
- **Negative-sampling strategy is dataset-dependent**: same-recording negatives were selected for
  PC18, across-recording negatives for TUHab, chosen by hyperparameter search. This is the single
  hyperparameter the paper flags as mattering most, and it differs in direction between the two
  datasets.
- **Pretext-task volume**: 2,000 RP pairs or TS triplets per PC18 recording (400 for TUHab, whose
  recordings are shorter), giving 1,986,000 RP/TS examples on PC18 and 1,196,000 on TUHab; CPC
  batches were set to 0.05 times the number of windows per recording, batch size 32.
- **Embedding structure**: UMAP projections of the 100-dimensional TS and CPC features on PC18
  arrange the five sleep stages sequentially along a trajectory W → N1 → N2 → N3, with R
  overlapping N1, without any labels having been used. This is the paper's evidence that the
  learned axes are physiological rather than arbitrary.
- The authors note explicitly that although the tasks were developed on clinical recordings, they
  "could be readily applied to event-related EEG protocols, such as those encountered in
  cognitive psychology or brain-computer interfaces" — which is STRUM's regime, and is stated as
  an expectation rather than a result.

## Open questions / limitations

- **Splits are record-wise, not subject-wise, and the distinction bites on one dataset.** The
  paper states that "the examples from each recording were only in one of the sets". For PC18
  that is equivalent to subject-wise, since there are 994 recordings from 994 individuals. For
  TUHab there are 2,993 recordings from 2,329 patients, so a patient with two recordings can
  appear in both training and validation under the 80-20 split of the development set. The test
  set is the TUHab-provided evaluation set, which limits the exposure, but the validation-set
  leakage is real and the paper does not discuss it.
- **Compute budget, corrected during the Phase 4 audit.** An earlier version of this bullet said
  "No parameter count and no compute budget are reported". Both are reported. The parameter counts
  are above; the compute budget is stated verbatim as "deep learning models were trained on 1 or 2
  Nvidia Tesla V100 GPUs for anywhere from a few minutes to 7h, depending on the amount of data,
  early stopping and GPU configuration." It is a range rather than a per-model figure, so a
  precise cost comparison between SSL and full supervision still cannot be made, but the claim
  that nothing was reported was wrong.
- The pretext-task hyperparameters τ_pos and τ_neg are swept over a wide grid per dataset and per
  task, and the best combination differs between datasets. The reported SSL numbers are therefore
  the best of a search, while the fully supervised baseline is a single configuration.
  **Corrected during the Phase 4 audit:** an earlier version added that "the paper does not say
  whether the baseline received comparable tuning". It says so explicitly, and lists it first among
  its three self-identified limitations: "Given the computational requirements of training neural
  networks on large EEG datasets, we fixed the training hyperparameters of the fully supervised
  models (i.e., learning rate, batch size, dropout, weight decay) and reused the same values across
  all data regimes. As a result, the fully supervised models typically stopped learning after only
  a few epochs, although they might have been able to train longer with different hyperparameters.
  We tested the impact of various training hyperparameter settings on a subset of the models and
  saw that even though training can be slightly improved by changing hyperparameters, this effect
  is not strong enough to change any of our conclusions (results not shown)." So the asymmetry is
  disclosed and partially tested, but the test is unreported ("results not shown"), which is the
  form the caveat should take.
- The paper's second self-identified limitation is that the architecture was never searched: "Sticking
  to a single fixed architecture for all models and data regimes means that these improvements -
  which could help bridge (or widen) the gap between SSL methods and the various baselines - were
  not taken into account in this work." Its third is that it does not attempt state-of-the-art
  performance on either downstream task, and on PC18 sleep staging it states there is no prior art
  to compare against at all.
- Only two frontal channels are used on PC18, out of six recorded, "to reduce the dimensionality
  of the input data". The sleep-staging result therefore says nothing about how the objectives
  behave with a full montage.
- The comparison is between a *linear probe* on frozen SSL features and a *fully trained*
  supervised network. This favours neither side unambiguously — the probe is handicapped, the
  encoder has seen more data — but it is not the like-for-like fine-tuning comparison that later
  work in this strand runs.
- The two downstream tasks are sleep staging and pathology detection, both of which the brief
  places out of scope as applications. They are admitted here because they are the substrate for
  the objective comparison, not because the applications matter.

## Citations

Primary: `banville-2021-self-supervised-eeg`

- Oord et al., Representation learning with contrastive predictive coding (2018) — the objective
  adapted here as CPC, and the one that performs best of the four.
- `bendr-2021` — compares its own sleep-staging results against the RP and TS schemes defined
  here.
- Chambon et al. (reference [42]) — the sleep-staging architecture adapted into StagerNet.
- Obeid and Picone, TUH EEG corpus (2016), and the TUH Abnormal subset (reference [40]) — the
  pathology-detection data.
- Ghassemi et al., PhysioNet/CinC Challenge 2018 (reference [1]) — the sleep dataset.
