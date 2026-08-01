---
slug: cbramod-2025
type: paper
strand: eeg-models
year: 2025
authors: [Wang, Zhao, Luo, Zhou, Jiang, Li, Li, Pan]
venue: ICLR 2025 (arXiv preprint 2412.07236)
doi: 10.48550/arXiv.2412.07236
url: https://arxiv.org/abs/2412.07236
license: null
modalities: [scalp-eeg, clinical-eeg, 19-channel-10-20, variable-channel-count]
tags: [masked-reconstruction, criss-cross-attention, factorized-spatial-temporal-attention, conditional-positional-encoding, depthwise-cnn, released-weights, motor-imagery, emotion-recognition, sleep-staging, small-model]
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

Splitting attention into parallel spatial and temporal streams, and generating positional
information with an asymmetric depthwise convolution over the channel-by-time patch grid rather
than a fixed table, gives a 4M-parameter masked-reconstruction model that accepts arbitrary
channel counts and window lengths — but which its own ablation shows collapses when its weights
are frozen.

## Summary

CBraMod is a 12-layer transformer pretrained by patch-based masked EEG reconstruction on the
Temple University Hospital EEG corpus. Its two design claims are architectural. First,
*criss-cross attention*: each block splits its 8 heads into a spatial stream attending across
channels within one time interval and a temporal stream attending across time within one channel,
running in parallel rather than as full attention over the flattened patch grid, on the argument
that spatial and temporal dependencies in EEG are heterogeneous. Second, *asymmetric conditional
positional encoding*: position is produced by a one-layer depthwise 2D convolution over the
channel-by-time neighbourhood of each patch, with a kernel longer in the channel dimension than
the time dimension, so the positional signal is generated from local context instead of looked up
by index. Because nothing is indexed, a downstream dataset with an unfamiliar channel count or
recording length needs no new positional parameters. Evaluation covers 10 downstream tasks over
12 public datasets, against seven supervised baselines and two pretrained ones (BIOT, LaBraM).
The paper reports state-of-the-art results across that range and an ablation isolating the
contribution of pretraining, of pretraining-data cleaning, and of freezing the backbone.

## Relevance to the review

CBraMod is a lead named in the strand brief and one of the checkpoints this project would have
to consider. Its input contract is unusually permissive in the two dimensions STRUM will
exercise: channel count is not fixed by the positional encoding, and the model is pretrained on
30-second samples specifically because "30 seconds generally covers the length of EEG sample
segments for all the downstream tasks", with downstream windows from 1 s to 30 s used without
architectural change. Against that, the pretraining preprocessing fixes 19 channels from the
10-20 system, so the flexibility is a property of the encoding, not something demonstrated at
pretraining time.

Two of its own results bear directly on how this project should design comparison 1 versus
comparison 2. The pretraining ablation is clean and small: on PhysioNet-MI, CBraMod with clean
pretraining reaches 0.6417 balanced accuracy against 0.6196 for the identical architecture
trained only on the downstream data, so pretraining is worth about 2.2 points while the
architecture accounts for the rest of the gap over EEGNet. And the frozen-backbone ablation is
a negative result the authors state plainly: fixing the pretrained parameters "will lead to a
very large performance decline", and they conclude that CBraMod "cannot currently serve as a
fixed-parameter feature extractor like CLIP and SAM, and fine-tuning is still necessary". Any
plan that assumed frozen CBraMod embeddings could be fed to a downstream classifier — which is
the cheapest way to add peripheral physiology on top of an EEG embedding — has to reckon with
that.

## Notable details

- **Pretraining corpus and total hours**: TUEG (Temple University Hospital EEG corpus), described
  as 69,652 recordings from 14,987 subjects across 26,846 sessions totalling 27,062 hours. After
  preprocessing, 1,109,545 samples of 30 s are retained, which the paper states is "longer than
  9000 hours in total"; it contrasts this with 2,534.78 hours for LaBraM. The retained figure is
  therefore roughly a third of the raw corpus.
- **Parameter count**: 4.0M for the criss-cross variant (4.1M for the full-attention variant),
  measured on CHB-MIT with 16 channels and 10-second windows; 318.9M FLOPs. The backbone is 12
  layers, hidden dimension 200, feed-forward inner dimension 800, 8 heads. A scaling study spans
  0.1M to 4M parameters. The paper's own comparison table lists EEGNet at 0.003M, BIOT at 3.2M,
  LaBraM-Base at 5.8M, LaBraM-Large at 46M and LaBraM-Huge at 369M; the baseline counts are
  taken from LaBraM rather than recomputed, and CBraMod's own are computed with Thop.
- **Input contract**: 200 Hz after resampling, applied to every downstream dataset as well as to
  pretraining. Band-pass 0.3–75 Hz, 60 Hz notch. 19 channels selected from the 10-20 system
  (Fp1, Fp2, F7, F3, Fz, F4, F8, T3, C3, Cz, C4, T4, T5, P3, Pz, P4, T6, O1, O2) for pretraining.
  Patches are 1 s = 200 samples, non-overlapping; a 30 s pretraining sample becomes 19 x 30 = 570
  patches. Amplitude normalization sets the unit to 100 µV so values fall mainly in [-1, 1],
  following LaBraM. Samples containing any point exceeding 100 µV in absolute amplitude are
  discarded as bad. Recordings under 5 minutes are dropped, and the first and last minute of each
  recording are discarded.
- **Most informative transfer number, with baseline**: on PhysioNet-MI 4-class motor imagery,
  CBraMod reaches 0.6417 ± 0.0091 balanced accuracy against EEGNet at 0.5814 ± 0.0125 — a 6.0
  point margin over a 0.003M-parameter supervised convolutional baseline, at roughly 1,300 times
  the parameter count. The paper's own pretraining ablation places 0.6196 of that on the
  architecture and only the remaining 2.2 points on pretraining. Against the strongest pretrained
  comparator on the same task, LaBraM-Base reaches 0.6173.
- **Frozen-backbone result**: with the backbone fixed and only a classifier trained, PhysioNet-MI
  balanced accuracy falls from 0.6417 to 0.3845, and FACED from 0.5509 to 0.3146. Frozen CBraMod
  still beats frozen BIOT (0.3698 on PhysioNet-MI) and frozen LaBraM (0.3715), so the ordering
  among pretrained models is preserved while all three are far below their fine-tuned selves.
- **Data-cleaning ablation**: pretraining on TUEG without bad-sample removal ("dirty
  pretraining") gives 0.6245 on PhysioNet-MI against 0.6417 with cleaning and 0.6196 with no
  pretraining. Dirty pretraining is therefore worth only about half a point over no pretraining
  at all on this task, which the authors read as dirty data weakening the effectiveness of
  pretraining.
- **Held-out-corpus check**: for TUEV, the authors re-pretrained a fresh instance of CBraMod with
  TUEV excluded from pretraining, and it still reached 0.6671 balanced accuracy against
  LaBraM-Huge (369M parameters) at 0.6616. This is the one place the paper controls for overlap
  between pretraining corpus and evaluation set.
- **Objective**: mean squared error between reconstructed and original masked patches, at a 50
  percent mask ratio, on the raw normalized signal rather than on a discrete codebook. Mask token
  type (full-zero versus learnable) made no significant difference.
- **Release**: source code at https://github.com/wjq-learning/CBraMod. The paper states the code
  is publicly available; it makes no statement about the licence of the released weights, which
  is a gap for category 3.
- Pretraining cost: about 5 days on four NVIDIA RTX A5000 GPUs, 40 epochs, batch 128, AdamW at
  learning rate 5e-4.

## Open questions / limitations

- **Naming inconsistency inside the paper.** The pretraining-settings paragraph describes the
  8-head split as "4 heads for S-Attention and 4 heads for V-Attention", while Section 2, Figure 3
  and the eight other mentions all call the second stream T-Attention (temporal attention). The
  card uses T-Attention, following the tables and the method section per the standing rule; the
  single "V-Attention" appears to be a leftover. Nothing numerical depends on it, but a reader
  grepping the source for one name will miss the other.
- The channel-flexibility claim is structural, not demonstrated at pretraining scale. All
  pretraining uses the same 19 channels, and the paper does not report an experiment holding out
  an electrode layout. Downstream datasets do vary from 6 to 64 channels, which is real evidence,
  but each is fine-tuned rather than evaluated zero-shot.
- The 9,000-hour figure is stated only as "longer than 9000 hours" and is never given exactly,
  while the corpus figure it is derived from (27,062 hours) is exact. The retained fraction
  therefore cannot be computed precisely from the paper.
- Bad-sample removal discards any 30-second sample containing a single point above 100 µV. This
  is an amplitude criterion applied to a corpus of clinical recordings, and the authors note in
  their limitations that it "resulted in a significant reduction in the amount of available
  pre-training data". Whether it also removes genuine high-amplitude neural events is not
  examined.
- Downstream splits are subject-wise for some datasets (FACED subjects 1–80/81–100/101–123,
  PhysioNet-MI subjects 1–70/71–89/90–109, SHU-MI subjects 1–15/16–20/21–25) but trial-wise for
  others (SEED-V divides the fifteen trials of each session 5:5:5, so the same subject appears in
  train, validation and test). The paper does not flag this difference, and the SEED-V numbers
  are therefore not cross-subject.
- The authors' own stated limitation is that parameter count and computational complexity remain
  far above non-foundation models, raising the deployment threshold. At 4M parameters against
  EEGNet's 0.003M for 6 points of balanced accuracy, the efficiency question is left open.
- No licence is stated for the released weights, and none of the reported comparisons is to a
  third-party reproduction.

## Citations

Primary: `cbramod-2025`

- `labram-2024` — the vector-quantized model CBraMod treats as its strongest pretrained baseline
  and whose 100 µV normalization convention it adopts.
- `biot-2023` — the second pretrained baseline, and the source of the public baseline
  implementations CBraMod re-ran.
- `bendr-2021` — cited (as "BENDER") as the precedent for choosing longer pretraining segments to
  capture longer-range dependencies.
- Obeid and Picone, TUH EEG corpus (2016) — the pretraining corpus.
- Huang et al., CCNet criss-cross attention — the attention pattern CBraMod adapts, and one of
  the ablation comparators against its own variant.
