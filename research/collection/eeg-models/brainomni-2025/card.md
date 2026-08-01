---
slug: brainomni-2025
type: paper
strand: eeg-models
year: 2025
authors: [Xiao, Cui, Zhang, Chen, Wu, Thwaites, Woolgar, Zhou, Zhang]
venue: NeurIPS 2025 (arXiv preprint 2505.18185)
doi: 10.48550/arXiv.2505.18185
url: https://arxiv.org/abs/2505.18185
license: CC BY 4.0 (arXiv posting)
modalities: [scalp-eeg, meg, clinical-eeg, sensor-coordinates-and-orientation, arbitrary-electrode-layout, joint-eeg-meg]
tags: [residual-vector-quantization, masked-token-prediction, criss-cross-transformer, sensor-encoder, latent-source-variables, channel-compression, cross-device-generalisation, released-weights, cross-subject-split, balanced-accuracy]
relevance: high
imported_from: null
added: 2026-08-01

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

Compressing a variable number of sensors into a fixed set of 16 "latent source variables" by
cross-attention — with keys carrying each sensor's 3D position, orientation and type rather than its
name — lets one tokenizer quantise EEG and MEG from devices with 19 to 306 channels into a single
discrete vocabulary, which is what makes a single masked-token model trainable across both
modalities at once.

## Summary

BrainOmni is a two-stage model: BrainTokenizer, a masked autoencoder that quantises multichannel
signal into discrete tokens, and BrainOmni proper, a Criss-Cross Transformer trained with masked
token prediction over those tokens. Stage 1 encodes each channel's waveform with a SEANet
convolutional encoder, adds a Sensor Encoder embedding of the sensor's 6-dimensional position and
orientation vector plus its type (0 EEG, 1 gradiometer, 2 magnetometer), and then uses a
cross-attention block whose learnable queries compress the C input channels to C′ = 16 latent
variables before 4-layer residual vector quantisation. The authors frame this explicitly as a
learned analogue of source-current estimation: the tokenizer is the backward solution, the
reconstructor the forward solution, and the cross-attention weights a data-dependent inverse
operator in place of a fixed leadfield-derived one. Stage 2 masks 50% of positions in the
(C′, T) token grid and predicts all four residual-vector-quantisation layers non-autoregressively.
Pretraining uses 1,997 hours of EEG and 656 hours of MEG from 22 public datasets. On eight EEG,
two MEG and one joint dataset under 5-fold cross-subject cross-validation, BrainOmni_base reports
the best balanced accuracy on every task except PhysioNet-MI, and an ablation shows joint EEG-MEG
pretraining beating either single-modality variant on all four datasets tested.

## Relevance to the review

Two mechanisms here bear directly on whether a checkpoint can be fed STRUM data. The first is that
spatial identity is carried by physical sensor metadata rather than by a channel-name lookup, so an
electrode set absent from pretraining costs no new parameters — the same property `reve-2025`
provides, reached by a different route (a learned Sensor Encoder over position, orientation and
type, rather than a Fourier basis over coordinates). The second is channel compression: because
cross-attention maps any C to a fixed C′ = 16, the downstream feature dimension is constant
regardless of how many electrodes a recording has. That is the property that decides whether one
downstream head can be reused across recordings with different channel counts.

The paper's frozen-backbone table (Appendix F.2) is the part most relevant to this project's third
comparison, where a frozen embedding would be concatenated with peripheral physiology. It is
narrower than the strand's other frozen-feature evidence — three datasets, and the "frozen" head is
the same two-layer MLP used everywhere else rather than a single linear layer — but it is the
paper's own measurement of what survives freezing.

Keep the paper's own claims separate from the suite's. **BrainOmni's own paper** reports
cross-subject 5-fold results on eleven datasets it selected, against four non-pretrained EEG
models, one non-pretrained MEG model, and two pretrained EEG models (LaBraM, CBraMod), and claims
best-or-second-best on all of them. **`datasets-benchmarks/omnieeg-bench`** is a third party that
re-ran ten checkpoints on 54 datasets and found BrainOmni takes the best average rank under its
primary cross-subject linear-probing protocol, followed by CBraMod and REVE, and separately that
BrainOmni "exhibits steeper performance scaling with sample size" under few-shot linear probing.
Those are different evidence: the paper's is self-run on a chosen benchmark set under full
fine-tuning with a two-layer MLP head; the suite's is third-party, under a frozen backbone with a
linear head, on datasets the authors did not choose. Neither substitutes for the other, and only
the suite's number is a like-for-like ranking against the other checkpoints in this strand.

## Notable details

- **Pretraining corpus and total hours**: 1,997 hours of EEG plus 656 hours of MEG, 2,653 hours
  total, from 22 public datasets named in Appendix H (TUEG is not among them; the EEG sources are
  HBN-EEG, HBN EO/EC, SRM, RestCog, PEARL-Neuro, Features-EEG, MusicEEG, HFO, Go-Nogo, Awakening
  and the EEG half of Kymata-SOTO; the MEG sources include OMEGA, CC700, THINGS-MEG, SMN4Lang,
  MEG-MASC and others). Split 85/10/5 train/validation/test. EEG devices range from 19 to 128
  channels, MEG devices from 157 to 306. Two datasets recorded on device systems absent from the
  corpus (PerceiveImagine, Gloups-MEG) were held out entirely for the cross-device test. The paper
  states its own scale limit: "the scale of EEG and MEG data used for pretraining is still
  relatively limited", and attributes the MEG shortfall to dataset availability.
- **Parameter count**: BrainOmni_tiny 8.4M (hidden dim 256, 8 heads, depth 12); BrainOmni_base 33M
  (hidden dim 512, 16 heads, depth 12). Both sit on top of a separately trained BrainTokenizer
  (hidden dim 256, codebook dim 256, codebook size 512, 4 quantizers, 16 latent source variables,
  4 attention heads), whose parameter count is not reported separately. `datasets-benchmarks/brain4fms`
  independently tabulates BrainOmni at 32.71M, consistent with the base model.
- **Input contract**: 256 Hz after resampling; band-pass 0.1–96 Hz; 50/60 Hz notch; MEG recordings
  with head-position-indicator coils additionally filtered in their HPI bands. Bad channels are
  detected by a power-spectral-density outlier rule (Algorithm 1, IQR threshold 10) and
  interpolated. A global average across all channels of each sensor type is subtracted, applied at
  the recording level and per signal type, "regardless of whether a reference channel is
  unavailable or the signals have already been referenced"; then each channel is z-scored at the
  sample level. Each channel requires a 6-vector of Cartesian position and orientation plus a type
  label, taken "from either the dataset-provided positions or the device's standard montage".
  Channel count and ordering are unconstrained. BrainTokenizer operates on 2-second segments
  (window length 512 samples); BrainOmni is trained on 30-second segments with a 25% window overlap
  ratio.
- **Most informative transfer number, with baseline**: on TUEV (6-class event classification),
  BrainOmni_base reaches 0.622 balanced accuracy against 0.392 for ST-Transformer, the best of the
  four non-pretrained EEG baselines run under the same pipeline — a 23.0-point gain. The gap is
  strongly task-dependent: on MDD the same model reaches 0.877 against 0.863 for ContraWR, a
  1.4-point gain, and BrainOmni_tiny (0.886) beats BrainOmni_base there. On PhysioNet-MI it is
  second to CBraMod (0.590 vs 0.595).
- **Frozen backbone versus full fine-tuning** (Appendix F.2, Table 9, three datasets):
  BrainOmni_base frozen reaches 0.809 / 0.480 / 0.771 on TUAB / TUEV / AD65 against 0.819 / 0.622 /
  0.828 fully fine-tuned. Freezing costs 14.2 points on TUEV and 5.7 on AD65 but only 1.0 on TUAB.
  On AD65 the frozen BrainOmni_base (0.771) exceeds fully fine-tuned LaBraM (0.711) and CBraMod
  (0.681). Note the head: for every model in this table the classifier is a two-layer MLP over
  time-average-pooled, flattened embeddings, so "freeze" here is not a linear probe.
- **Cross-device evidence is reconstruction, not classification.** The unseen-device result
  (Table 4) compares BrainTokenizer's zero-shot reconstruction error on held-out device systems
  against its own test set: on the unseen EEG system PerceiveImagine it is *better* on every metric
  (PCC 0.802 against 0.748), on the unseen MEG system Gloups-MEG slightly worse (0.695 against
  0.711). No downstream classification accuracy is reported on either held-out system.
- **Sensor Encoder ablation**: removing the sensor embedding costs 3.5 points on TUAB, 6.5 on AD65,
  5.3 on ASD74 and 11.9 on SomatoMotor — but *gains* 0.4 points on TUEV, which the paper's text does
  not address. Treating channels as uncorrelated single-channel data ("pure temporal") is worse than
  the full model everywhere.
- **Joint EMEG pretraining**: EEG-only and MEG-only variants of the tiny model are beaten by the
  joint model on all four datasets tested; the largest effect is on MEG ASD74, a reported 12%
  relative balanced-accuracy improvement over the MEG-only model.
- **Evaluation protocol**: 5-fold cross-validation with a strict cross-subject split (three folds
  train, one validation, one test), two seeds, mean and standard deviation over 10 runs, balanced
  accuracy as the primary metric, 30 epochs, best-validation checkpoint. TUAB and TUEV use their
  official evaluation sets. All eleven downstream datasets were excluded from pretraining. Learning
  rate was selected per model from three values by best result, for baselines as well as for
  BrainOmni.
- Code and checkpoints are released at `https://github.com/OpenTSLab/BrainOmni`. The paper states
  no licence for the released weights.

## Open questions / limitations

- The pretraining corpus is not clinical: no TUEG, and the largest EEG contributions are
  developmental and resting-state cohorts. Four of the eleven downstream tasks are nonetheless
  clinical. The paper does not analyse the domain gap this implies.
- The four non-pretrained EEG baselines are reported with "-" in the "# Param" column of Tables 2
  and 3, so the parameter cost of the pretrained advantage cannot be read off the paper. That
  matters here: this project's comparison 1 is a *small* supervised model, and the paper gives no
  way to see how small its baselines were.
- Channel compression to 16 latent variables is a fixed bottleneck justified only by a
  reconstruction-loss curve (Fig. 3a) showing diminishing returns beyond 16. Whether 16 suffices for
  a task whose discriminative information is spatially fine-grained is untested; the ablation
  compares 16 against an electrode-level model on five datasets, not against other values of C′ on
  a downstream task.
- The unseen-device claim rests on reconstruction quality alone (see above). Better reconstruction
  on an unseen device is consistent with that device's signal simply being easier to reconstruct,
  and the paper does not control for that.
- The frozen-backbone table covers three datasets, none of them a cognitive or naturalistic-stimulus
  task, so it says little about the regime this project's third comparison would operate in.
- No dyadic or two-person recording appears anywhere in pretraining or evaluation, and no peripheral
  physiology is modelled. The Sensor Encoder's type vocabulary has exactly three values (EEG,
  gradiometer, magnetometer), so an ECG, EOG or respiration channel has no representation in the
  current model.
- The sensor-embedding ablation improving TUEV while degrading every other dataset is reported in
  Table 6 but described in the text as uniformly harmful ("the exclusion of sensor embedding
  significantly undermines the downstream performance"). The table is carded here; the prose
  overstates it.
- Bipolar derivations are not discussed. Every downstream EEG dataset is used in referential form,
  so the question of what position to assign a differential channel — which `reve-2025` answers with
  a midpoint — does not arise in this paper and is unanswered for it.

## Citations

Primary: `brainomni-2025`

- `cbramod-2025` — Wang et al. The Criss-Cross Transformer block BrainOmni's stage-2 model is built
  from, and one of its two pretrained baselines.
- `labram-2024` — Jiang et al., ICLR 2024. The vector-quantised tokenisation lineage BrainOmni
  extends from patch-level to spatiotemporal quantisation, and its other pretrained baseline.
- `biot-2023` — Yang et al. Cited as the prior approach to mismatched channels via a "biosignal
  sentence".
- `brainwave` — Yuan et al. The prior joint-modality brain foundation model (EEG plus intracranial
  EEG), cited as the closest precedent for training one model across two recording modalities.
- `datasets-benchmarks/omnieeg-bench` — Lu et al. 2026. Third-party evaluation that ranks BrainOmni
  first under its primary cross-subject linear-probing protocol.
