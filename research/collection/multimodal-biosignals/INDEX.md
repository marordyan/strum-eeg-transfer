# Peripheral Biosignals and Multimodal Fusion — Collection Index

Strand B. Scope categories are those defined in `_briefs/strand-multimodal-biosignals.md`. One line
per entry; each entry's full record is its `card.md`. Entries appear under every category they
serve, so the per-category lines below total more than 25.

**Collection status: 25 of 25 entries.** Nothing here is a synthesis, a ranking or a gap analysis;
that is Phase 3.

## 1. Single-modality foundation models for peripheral signals

- [papagei-2024](./papagei-2024/card.md): the first open PPG foundation model — 20 M unlabelled
  segments, 57,641 h, morphology-based supervision instead of instance contrast, beats models 70x
  larger, and ships a Fitzpatrick skin-tone bias benchmark; input contract is single-channel PPG
  resampled to 125 Hz (`relevance: medium`, 2024)
- [mckeen-2025-ecg-fm](./mckeen-2025-ecg-fm/card.md): open-weight wav2vec 2.0 ECG encoder, 90.9 M
  parameters, 1.4 M 5-second 12-lead segments, hybrid masked-reconstruction plus contrastive
  objective; Random Lead Masking makes it fine-tunable on arbitrary reduced lead sets, which is the
  strand's only principled answer to missing channels (`relevance: medium`, 2025)
- [lee-2025-biosignal-fm-review](./lee-2025-biosignal-fm-review/card.md): survey of foundation
  models across EEG, ECG, EMG, EOG and PPG organised by data processing, architecture, pretraining
  paradigm and evaluation; a map of the field, on a server with no peer review, and its full text
  could not be retrieved (`relevance: medium`, 2025)
- [ha-wearable-eeg-heg-hrv](./ha-wearable-eeg-heg-hrv/card.md): the strand's only hardware entry —
  a sub-200 g headband and earplug ASIC acquiring EEG, hemoencephalography and HRV alongside
  transcranial electrical stimulation, with 130 dB CMRR on the EEG front end; two EEG channels and
  a modality set that barely overlaps STRUM's (`relevance: low`, 2015)

## 2. Fusion architectures

- [li-2023-incongruity-fusion](./li-2023-incongruity-fusion/card.md): designates one modality
  primary and corrects the auxiliaries against it with a cross-modal transformer before low-rank
  fusion removes redundancy — the one architecture in the strand built around modality
  *disagreement* rather than shared variance; no numerical result was retrievable from any source
  (`relevance: medium`, 2023)
- [liu-eeg-multimodal-emotion-review](./liu-eeg-multimodal-emotion-review/card.md): review
  organised around multimodal representation learning, physiological fusion, and incomplete
  multimodal learning — the last being the only pointer this strand has into the missing-channel
  literature; paywalled, so its reference list could not be mined (`relevance: medium`, 2024)
- [ding-2025-cross-attention-fusion](./ding-2025-cross-attention-fusion/card.md): dual-branch
  encoders producing full feature *sequences*, then multi-head cross attention where the EEG
  representation queries the peripheral sequence; 94.88 / 95.26 on DEAP and 89.12 on SEED-IV, but
  compared only against other multimodal methods with no unimodal arm (`relevance: low`, 2025)
- [kuttala-2023-hierarchical-fusion](./kuttala-2023-hierarchical-fusion/card.md): concatenates low,
  mid and high-level CNN features within each modality and recalibrates across modalities with a
  Multimodal Transfer Module; subject-independent on four benchmarks, but EDA and ECG only, with no
  EEG anywhere (`relevance: low`, 2023)

Also bearing on this category from other groups: the decision-level fusion with temperature scaling
and a validation-gated fallback to EEG in
[azad-2025-construction-noise](./azad-2025-construction-noise/card.md); the three-backbone
attention fusion with parameter counts and latency in
[kumar-2026-attention-eeg-ecg-stress](./kumar-2026-attention-eeg-ecg-stress/card.md); and the DCCA
versus bimodal-deep-autoencoder comparison across five datasets in
[liu-2022-multimodal-robustness](./liu-2022-multimodal-robustness/card.md).

## 3. Ablations that isolate the peripheral contribution

Entries reporting a genuine EEG-only versus combined comparison, with the numbers this corpus could
actually read:

- [salam-eeg-ecg-stress](./salam-eeg-ecg-stress/card.md): EEG (theta/alpha ratio) 80.0% vs ECG (HR,
  LF/HF) 66.65% vs fused 92.6%, SVM, 66 participants; the split is described three mutually
  inconsistent ways, and the abstract's headline 94.7% is one cell of a table whose average is
  85.7% (`relevance: high`, 2026)
- [hogervorst-2014-workload-comparison](./hogervorst-2014-workload-comparison/card.md): EEG ~86%,
  peripheral physiology and eye measures 70–75%, and combining sensor groups gives no significant
  improvement over the best single sensor — a null from a study designed to find the gain, with
  body movement and visual input held constant, 14 participants (`relevance: high`, 2014)
- [angkan-2024-invehicle-cognitive-load](./angkan-2024-invehicle-cognitive-load/card.md): the full
  modality grid — EEG alone 61.20% to all four modalities 67.04% under leave-one-subject-out
  binary, 21 participants; the 10-fold-to-LOSO drop is larger than the entire fusion gain
  (`relevance: high`, 2024)
- [azad-2025-construction-noise](./azad-2025-construction-noise/card.md): EEG 0.794 vs EDA 0.557 vs
  fused 0.796 under 5-fold subject-independent GroupKFold, 25 participants; the fusion rule falls
  back to EEG whenever fusion fails to beat it on a validation subset (`relevance: high`, 2025)
- [kumar-2026-attention-eeg-ecg-stress](./kumar-2026-attention-eeg-ecg-stress/card.md): EEG-only
  82.3%, ECG-only 85.6%, early fusion 89.2%, late fusion 91.4%, attention fusion 95.7%, with a
  three-subject held-out test set — and an EEG stream attributed to two public datasets that
  contain no EEG (`relevance: low`, 2026)

Entries where the comparison is reported by the paper but its magnitude was not accessible:

- [zheng-2018-emotionmeter](./zheng-2018-emotionmeter/card.md): fusion 85.11% on four emotions and
  72.39% across sessions, with EEG better at happy and eye movements better at fear — the
  complementarity result the strand needs, on a six-electrode montage; single-modality numbers are
  behind the paywall (`relevance: medium`, 2018)
- [liu-2022-multimodal-robustness](./liu-2022-multimodal-robustness/card.md): the only entry that
  runs the inverse ablation — replacing the EEG features with noise and measuring what survives —
  on SEED-V and DREAMER; the experiment is named in the abstract and its numbers are not
  (`relevance: medium`, 2022)
- [li-2023-incongruity-fusion](./li-2023-incongruity-fusion/card.md): cross-listed from category 2;
  the method designates a primary modality by unimodal performance, so unimodal arms exist, but no
  abstract could be retrieved from OpenAlex, Crossref, Semantic Scholar or the publisher
  (`relevance: medium`, 2023)

Physiology-only arms, the arm the fusion literature most often omits:

- [wang-2025-sedation-non-eeg](./wang-2025-sedation-non-eeg/card.md): predicts an EEG-derived label
  (bispectral index above 60) from 27 peripheral and demographic features at AUROC 0.825, 1,022
  patients, patient-wise split; the top predictors are blood pressure and end-tidal CO2, not HRV
  (`relevance: medium`, 2025)
- [kuttala-2023-hierarchical-fusion](./kuttala-2023-hierarchical-fusion/card.md): cross-listed from
  category 2 — EDA plus ECG only, subject-independent across ASCERTAIN, CLAS, MAUS and WAUC
  (`relevance: low`, 2023)
- [ahmad-2020-cognitive-load-framework](./ahmad-2020-cognitive-load-framework/card.md):
  cross-listed from category 5 — three-level cognitive load at 91.66% from eye and heart measures
  on 40 participants, but the 5-fold split is stratified over samples, not participants
  (`relevance: medium`, 2020)

Coupling rather than classification:

- [zeng-brain-heart-ccm](./zeng-brain-heart-ccm/card.md): convergent cross mapping between
  32-channel EEG and single-lead ECG finds descending cortex-to-heart coupling stronger and more
  sustained than ascending — the direction that predicts a peripheral channel adds little beyond a
  good EEG model (`relevance: high`, 2026)

## 4. Artifact versus signal

- [mostert-2018-eye-movement-confounds](./mostert-2018-eye-movement-confounds/card.md): the
  memorised item was decodable from two numbers — horizontal and vertical gaze position — so a
  planned working-memory decoding result was published as a cautionary one instead; ICA cleaning
  had not been sufficient (`relevance: high`, 2018)
- [rotaru-2024-auditory-attention-bias](./rotaru-2024-auditory-attention-bias/card.md): four EOG
  channels alone decode spatial auditory attention above chance when gaze and attention are
  congruent, and a classifier asked which *trial* a 5 s window came from reaches 99.6–100%; random
  cross-validation is the leak (`relevance: high`, 2024)
- [wibirama-cognitive-load-eye-movement](./wibirama-cognitive-load-eye-movement/card.md): the same
  fault line from the other side — BiLSTM on eye-movement indices classifies multiclass cognitive
  load at 0.8780, so ocular artifact removal is discarding task-relevant information
  (`relevance: high`, 2025)
- [zeng-brain-heart-ccm](./zeng-brain-heart-ccm/card.md): cross-listed from category 3 — whether
  cardiac and cortical activity drive each other or both follow the stimulus is the cardiac-channel
  version of the same question, and the shared-input control is not visible in the accessible text
  (`relevance: high`, 2026)

Also relevant: [hogervorst-2014-workload-comparison](./hogervorst-2014-workload-comparison/card.md)
states that eye-related measures "have probably partly been found to covary with workload due to
the often occurring confound of the amount of visual information", and controls body movement and
visual input for exactly that reason;
[kumar-2026-attention-eeg-ecg-stress](./kumar-2026-attention-eeg-ecg-stress/card.md) removes
cardiac interference from its EEG stream with ICA while using ECG as its second modality, which
suppresses the shared component the fusion is supposed to exploit.

## 5. Classical physiology feature baselines

- [makowski-2021-neurokit2](./makowski-2021-neurokit2/card.md): the reference Python implementation
  for ECG, PPG, EDA, EMG and respiration under one three-layer API, with a `method` argument that
  makes preprocessing sensitivity measurable and separate event-related and interval-related
  workflows (`relevance: medium`, 2021, `type: tool`)
- [haque-hrv-stress-review](./haque-hrv-stress-review/card.md): 43 studies predicting stress from
  HRV, tabulated by sensor, preprocessing, feature and model; establishes that the engineered
  cardiac feature space is about a dozen recurring indices, and that the literature pools
  ECG-derived and PPG-derived HRV under one name (`relevance: medium`, 2023)
- [ahmad-2020-cognitive-load-framework](./ahmad-2020-cognitive-load-framework/card.md): eye and
  heart features for three-level cognitive load on 40 participants, with mean pupil diameter change
  dominant and blink rate a moderate contributor; validated with a stratified sample-wise split
  rather than a participant-wise one (`relevance: medium`, 2020)
- [schiecke-ccm-methods](./schiecke-ccm-methods/card.md): the methods reference for convergent
  cross mapping — demonstrates on simulated data that CCM outcomes depend on estimation parameters,
  which is what conditions every coupling claim in this strand; four-page conference paper,
  paywalled, so which parameters and by how much is not recorded (`relevance: medium`, 2015)
- [schiecke-2019-brain-heart-ccm](./schiecke-2019-brain-heart-ccm/card.md): generalised processing
  schemes for CCM brain-heart interaction along four axes — time-variant, frequency-dependent,
  topographical, statistical — with surrogate data, bootstrapping and linear mixed-effects models;
  recorded as CC-BY upstream but the publisher PDF could not be retrieved (`relevance: medium`,
  2019)

Also in this category from other groups:
[wang-2025-sedation-non-eeg](./wang-2025-sedation-non-eeg/card.md) is an engineered-feature decoder
with a SHAP ranking that puts a single HRV index sixth behind three haemodynamic vital signs;
[ha-wearable-eeg-heg-hrv](./ha-wearable-eeg-heg-hrv/card.md) is the acquisition-side constraint on
where those features can be computed at all.
