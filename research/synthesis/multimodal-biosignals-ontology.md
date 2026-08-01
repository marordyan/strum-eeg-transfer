# Ontology of the `multimodal-biosignals` strand

Phase 3 synthesis, strand B. Input is the 25 entries in
`research/collection/multimodal-biosignals/`; where a fact is grounded in a sibling strand's card,
that card is linked instead.

This document says what the strand contains and how its pieces relate. It is not the gap analysis:
it does not enumerate what the field is missing, does not rank entries, and does not recommend a
fusion design. Where two cards disagree, both readings are recorded and neither is picked. Where a
claim is repeated by several cards but traces to one measurement, it is counted once and the
repetition is named as repetition. A small number of sentences sit on the Phase 3 / Phase 4 boundary
because the register would be dishonest without them; each is marked **[boundary]**.

Every leaf of every facet is a card link. All 25 entries appear; the coverage table at the end says
where each one sits.

---

## Why these facets, and not the brief's five categories

`_briefs/strand-multimodal-biosignals.md` scopes the strand into five categories: single-modality
peripheral foundation models, fusion architectures, ablations isolating the peripheral contribution,
artifact versus signal, and classical feature baselines. The collection was run against those
categories and the strand's `INDEX.md` is organized by them. This ontology departs from them, for a
reason visible in the index itself.

Category 3 is the strand's declared centre of gravity, and the index could not keep it as one
heading. It is subdivided by hand into four groups — "entries reporting a genuine EEG-only versus
combined comparison, with the numbers this corpus could actually read", "entries where the
comparison is reported by the paper but its magnitude was not accessible", "physiology-only arms",
and "coupling rather than classification". Those four are not four kinds of paper. They are four
values on one property: *which experimental arms exist, and which of them this corpus can read*.
Once that is stated as an axis rather than as four sub-lists, it partitions the whole strand and not
just one category, because a foundation-model paper and a tool paper also have a value on it (none).

Three further mismatches, each grounded:

- Categories 3 and 4 hold the same entry for the same reason.
  [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) is
  cross-listed under both, because "is the cardiac channel carrying its own information" and "is the
  apparent effect shared task structure" are one question asked of one measurement. Splitting them
  duplicates the entry and clarifies nothing.
- Category 4's own two sides are not two categories.
  [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)
  is filed under "artifact versus signal" while arguing that the ocular channel is signal, and
  [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  is filed there arguing it is artifact. What makes them legible is being placed against each other
  along the axis of *what was measured with what instrument*, which the category heading hides.
- The property that most changes how a fusion gain should be read is not which category the paper
  sits in but the split geometry, and split geometry is invisible in the index. It cuts across
  categories 2, 3 and 5 and it is the difference between
  [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)'s
  +0.002 and
  [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md)'s +12.6.

The facets below are nine questions a reader can ask of any entry:

1. **Which arms exist** — the ablation axis, and the strand's primary partition (§1).
2. **Where the reported gain comes from** — what else the number is a function of (§2).
3. **What the gain was measured against** — split geometry and chance (§3).
4. **Artifact versus signal** — the ocular channel argued from both sides, and its cardiac
   counterpart (§4).
5. **Coupling, which is a different question from fusion** (§5).
6. **Modality coverage, and what the controlled spellings hide** (§6).
7. **Fusion mechanism** — where the streams meet and what each objective rewards (§7).
8. **The peripheral branch's input contract** — encoders, engineered features, and the window
   mismatch (§8).
9. **Where the corpus disagrees with itself** — a register, not a resolution (§9).

§1 is the axis that reorders the corpus relative to the index, and it is a hard partition rather
than a matter of degree: an entry either has an EEG-only arm on the same split as its combined arm
or it does not, and if it does not, no reading of its headline number answers the project's
question. §3 is the axis that changes the size of every gain in §2 without changing a single model.

---

## 1. The ablation axis: which arms exist

The question this node answers: for each entry, which of {EEG-only, peripheral-only, combined} was
run on one split, and which of those the corpus can read. The seven nodes are mutually exclusive and
every entry sits in exactly one. The counts are 4, 1, 2, 4, 1, 6, 7.

### 1.1 Three arms on one split, all magnitudes readable

Four entries. These are the only entries from which a reader can compute both a
combined-minus-EEG-only gain and a peripheral-only floor.

- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — EEG
  (theta/alpha ratio) 80.0% versus ECG (heart rate, LF/HF) 66.65% versus fused 92.6% on the five-way
  rest-versus-AC1–AC4 problem, SVM, 66 participants; 75.2 / 71.3 / 85.7 on the three-way rest / low /
  high problem. Three engineered scalars in total. The card records that the ECG arm's Matthews
  correlation coefficient is 0.0 in the three-class table despite 71.3% accuracy, so that arm is at
  or near the majority-class baseline.
- [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
  — EEG around 86% (best single variable the ERP at Pz, 88%), peripheral physiology and eye measures
  70–75%, EEG plus eye-related variables "a little over 90%", which the authors describe as "a
  similar and not significantly different performance". Fourteen participants. The only non-EEG
  variables exceeding the p < 0.01 chance level were respiration frequency (69%) and pupil size
  (75%).
- [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  — EEG 0.794 (95% CI 0.768–0.820) versus EDA 0.557 (0.528–0.586) versus fused 0.796 (0.769–0.823),
  5-fold subject-independent GroupKFold, 25 participants. The EDA arm sits below the 67%
  majority-class rate, and the authors state the gap "is systematic and not due to high variance".
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — EEG-only 0.823 / 0.841 / 0.836 across three backbones, ECG-only 0.798 with HRV features and
  0.856 with raw signal plus a CNN, early fusion 0.892, late fusion 0.914, attention fusion 0.957,
  with the attention layer removed 0.905. A three-subject held-out test set.

Two structural features of this node, both stated by the cards rather than inferred. In two of the
four, the peripheral-only arm is at or below a trivial baseline
([salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md)'s
three-class ECG arm,
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)'s
EDA arm) — yet one of those two reports the strand's largest gain and the other its smallest. And in
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
the peripheral arm *beats every EEG arm*, so its result is not "peripheral physiology adds to EEG"
but "EEG adds to ECG", which is a different claim from the one the paper frames.

### 1.2 EEG-only and combined, no physiology-only arm

- [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  — the strand's only full modality *grid*: EEG alone, EEG with each of three peripheral channels,
  and every combination, crossed with two label granularities and two evaluation criteria. Averaged
  over thirteen models, leave-one-subject-out binary accuracy runs 61.20% (EEG) → 63.95% (EEG+ECG) →
  64.04% (EEG+EDA) → 64.25% (EEG+gaze) → 67.04% (all four); ternary LOSO 41.59% → 47.80%. Twenty-one
  participants. The card names the structural gap precisely: "every one of the eight modality
  subsets includes EEG, so there is no physiology-only arm".

This entry belongs in its own node rather than with §1.1 because the missing arm is the one that
distinguishes "the peripheral channels carry the signal independently" from "they only sharpen an
EEG-led decision", and it is the arm the fusion literature most often omits.

### 1.3 EEG-only and peripheral-only, no combined arm — the confound configuration

Two entries. They run the comparison in the opposite direction from the fusion literature: not to
show that adding the peripheral channel helps, but to show that the peripheral channel alone already
carries the label.

- [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  — common spatial pattern filters on four EOG channels alone against the same pipeline on 64-channel
  EEG, sixteen participants. The EOG arm is lower than EEG in every condition (Wilcoxon signed-rank
  p = 0.001, 0.15, 0.03 and 0.04 across the four visual conditions) but still exceeds the
  significance level in the audiovisually congruent condition, which is also the only condition where
  subject-independent EEG decoding is significant.
- [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  — a two-feature decoder on horizontal and vertical gaze position, run through the same three-class
  classifier and the same 8-fold cross-validation as the neural analysis, recovering the memorised
  grating orientation. The recording modality is MEG, not EEG, and the card states the substitution
  and its direction: the corneo-retinal dipole projects more strongly onto scalp electrodes than onto
  magnetometers, so the argument transfers to EEG a fortiori.

### 1.4 The comparison exists in the source, and its magnitude does not reach this corpus

Four entries. This node exists because the practice brief requires the inaccessible-versus-unreported
distinction to survive synthesis, and in this strand it is four entries rather than a footnote. In
every case the paper computed the comparison and the corpus could not read it; nothing here is a
paper that declined to run the arm.

- [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) —
  fusion 85.11% on four emotions within session and 72.39% across three sessions on different days,
  on a six-electrode above-the-ear montage. The abstract states that fusion "can significantly
  enhance the performance compared with a single modality" and that EEG is better at happy while eye
  movements are better at fear, but gives no single-modality accuracy; IEEE Xplore is paywalled. The
  complementarity *localisation* — which class each modality wins on — is the shape of evidence the
  strand most needs and the one number that came through.
- [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md)
  — the only entry in the strand running the inverse ablation, replacing the EEG features with noise
  and measuring what survives, on SEED-V and DREAMER. The abstract names the experiment and gives no
  numbers for it. The fused DCCA figures are on record (SEED 94.6%, SEED-IV 87.5%, DEAP 84.3% and
  85.6%, SEED-V 85.3%, DREAMER 89.0% / 90.6% / 90.7%); the unimodal arms are not.
- [li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md)
  — the strand's worst retrieval. The method designates a primary modality "due to its prominent
  performance in emotion recognition", which means unimodal results were computed, and not a single
  numerical result could be retrieved from Crossref, OpenAlex, Semantic Scholar or the publisher. The
  card records that its method description is reconstructed from web-search snippets and that one
  contaminating sentence, attributing a different paper's model name to this work, was caught and
  removed.
- [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) —
  "19% maximum improvement with multimodal monitoring" over single-domain monitoring, computed with
  canonical correlation analysis and temporal kernel CCA over neural, vascular and autonomic domains.
  A gain stated as an improvement implies a baseline, and the baseline, the task, the participant
  count and the split are all in the paywalled body.

### 1.5 Combined only

- [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
  — 94.88% valence and 95.26% arousal on DEAP, 89.12% four-class on SEED-IV, compared only against
  other multimodal methods (BDAE, DCCA, HC-MFB, MMResLSTM on DEAP; DCCA, EmotionMeter, MFFNN on
  SEED-IV). The card is explicit that this is "a gap in the source, not in this corpus's access": no
  unimodal arm of any kind appears in the paper, and no ablation of the cross-attention module itself
  is visible either, so even the architectural claim rests on comparison to other papers' models
  rather than to its own model with the module removed.

This is the single entry that the brief's own rule targets — an entry reporting only combined
performance cannot answer the project's question — and it is marked `relevance: low` on exactly that
basis while being kept for its architecture (§7.2).

### 1.6 Peripheral signal only, with no EEG in the study at all

Six entries. Two report the physiology-only arm the fusion literature omits; two are cognitive-state
decoders that happen to have no cortical channel; two are the peripheral foundation models.

- [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
  — the strand's cleanest physiology-only arm, and in the most informative configuration available:
  the *label* is EEG-derived (bispectral index above 60), so the experiment is how much of an
  EEG-derived state peripheral physiology recovers without the EEG. Twenty-seven demographic,
  vital-sign and HRV features reach AUROC 0.825 (95% CI 0.823–0.826) at a 2 s window and roughly
  0.837 at 20 s, on 1,022 patients after an exclusion cascade from 6,388, with a patient-ID-level
  split. The SHAP ranking puts mean blood pressure, end-tidal CO2 and systolic blood pressure ahead
  of heart rate, with a single HRV index sixth.
- [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
  — EDA plus ECG with no EEG anywhere, subject-independent across ASCERTAIN (58 subjects), CLAS, MAUS
  and WAUC (48, 45 after removing incomplete records). Improvements are reported only as ranges: 1–2%
  over existing models on frequency-band features, 2–4% for the three-level hierarchical feature set
  over other level combinations. Per-dataset accuracies did not survive the two-column extraction.
- [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
  — three-level cognitive load at 91.66% (random forest) and 85.83% (naive Bayes) from eye and heart
  measures on 40 participants, with mean pupil diameter change in both eyes dominant and blink rate a
  moderate contributor. The card states plainly that the absent EEG arm is "a property of the study,
  not an access gap".
- [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)
  — BiLSTM on eye-movement indices at 0.8780 for multiclass cognitive load and 0.8836 for multiclass
  activity-task classification on COLET, against LSTM and a temporal convolutional network. The paper
  positions eye tracking as an *alternative* to EEG, ECG and GSR on intrusiveness grounds, so it
  contains no fusion arm and no EEG comparison by design.
- [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) — the first open PPG
  foundation model, evaluated on 20 tasks across 10 datasets with out-of-domain holdouts. It is
  explicitly framed as "both a feature extractor and an encoder for multimodal models", and the card
  records that no multimodal experiment appears in the evaluation, so the framing is a claim the
  paper does not test.
- [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) — an
  open-weight wav2vec 2.0 ECG encoder evaluated on multi-label ECG interpretation and reduced
  ejection fraction, with data-scaling experiments. Its downstream endpoints are diagnostic; the card
  records that nothing in it evaluates a cognitive, affective or stimulus-locked contrast.

### 1.7 No decoding arm at all

Seven entries. These are the coupling analyses, the methods and tool entries, and the reviews. They
enter the strand as constraints on how the entries above should be read rather than as evidence
about fusion.

- [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md),
  [schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) and
  [schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md)
  — the convergent-cross-mapping line (§5).
- [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) —
  the reference Python implementation for engineered peripheral features; `type: tool`, and the paper
  "contains no performance benchmark that could be quoted as a baseline number".
- [haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md) —
  43 studies tabulated by sensor, preprocessing, feature and model.
- [liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md)
  and [lee-2025-biosignal-fm-review](../collection/multimodal-biosignals/lee-2025-biosignal-fm-review/card.md)
  — the two review-shaped entries, both paywalled or blocked, and both cards record that their
  reference lists could not be mined, so neither produced a downstream entry.

---

## 2. Where the reported gain comes from

This node takes the five entries with a readable EEG-only-to-combined delta (§1.1 and §1.2) and
decomposes what else each number is a function of. Every gain in the strand is attributable in part
to something other than the peripheral signal, and the cards say so themselves.

### 2.1 The magnitudes, side by side

| entry | EEG-only | peripheral-only | combined | delta | split | n |
|---|---|---|---|---|---|---|
| [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md), 5-class | 80.0% | 66.65% | 92.6% | +12.6 | described three inconsistent ways | 66 |
| [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md), 3-class | 75.2% | 71.3% | 85.7% | +10.5 | same | 66 |
| [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md) | 0.841 (best of 3) | 0.856 | 0.957 | +11.6 | 3-subject held-out test | 35 claimed |
| [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md), LOSO binary | 61.20% | not run | 67.04% | +5.84 | leave-one-subject-out | 21 |
| [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md), LOSO ternary | 41.59% | not run | 47.80% | +6.21 | leave-one-subject-out | 21 |
| [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md) | ~86% | 70–75% | "a little over 90%" | ~+4, not significant | within-subject, train early / test late | 14 |
| [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md) | 0.794 | 0.557 | 0.796 | +0.002 | 5-fold GroupKFold, subject-independent | 25 |
| [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) | not accessible | not accessible | not accessible | "19% maximum improvement" | not accessible | not accessible |

The relation between the two rightmost columns and the delta column is the structure this table
exists to make visible, and it is a relation between entries rather than a verdict about the field.
The three entries whose split geometry is stated and either subject-disjoint or otherwise designed
against inflation — the LOSO grid, the GroupKFold study, and a within-subject temporal split — report
+5.84 / +6.21, +0.002, and a difference their own authors call not significant. The third is not
subject-disjoint and its card says so explicitly, every model being personal; it earns its place here
because its temporal split is designed against time-dependence inflation, which is a different
protection rather than a weaker version of the same one. The two
entries reporting double-digit gains are the two whose denominators the cards flag as unverifiable:
one has three mutually inconsistent split descriptions, the other attributes its EEG stream to
datasets that contain no EEG.

### 2.2 The gain is gated, so the headline is a mixture

[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
is the sharpest instance in the strand and its own paper supplies the evidence. On each fold,
"fusion was used on the test set only if it outperformed EEG in terms of both accuracy and F1 on the
fusion-validation subset; otherwise, predictions defaulted to EEG." The card names the consequence
exactly: the reported 0.796 is on some folds the fused model's output and on others the EEG model's,
the paper does not report how often the gate fired, and so the number "cannot be read as 'the fused
model's accuracy'". A +0.002 headline over an EEG-only arm, produced by a rule that falls back to
that same arm per fold, is a mixture rather than a measurement of fusion.

The card also reads the gate as evidence in itself: "a system that has to gate its own fusion behind
a per-fold check is a system whose designers observed that fusion sometimes hurts."

### 2.3 The arms are not equal effort

[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
compares single backbones against an ensemble. The EEG-only arms are one backbone each (VGG16 14.7 M,
EfficientNetB0 5.3 M, ResNeXt50 25 M); the fused model concatenates all three into a 1536-dimensional
vector compressed to 512, adds an attention layer over two modality streams, and totals 42.7 M
parameters. The paper's own backbone-ablation table gives 0.928–0.934 with any two backbones, which
the card reads as the ensemble contributing 2–3 points on its own, before any modality is fused. The
attention layer's own removal costs 0.052 (0.905 against 0.957).

### 2.4 The gain is classifier-specific

[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) ran six
classifiers on the same three features. On combined-sex data the linear discriminant reaches 84.3%
and the random forest 65.7%, so "the SVM's 92.6% is an outlier among the six models rather than a
property of the feature set". The instability goes further: the best classifier differs between the
pooled and sex-stratified analyses, with the linear discriminant reaching 90% for males and 90.9%
for females where the SVM reaches 75% and 80.6%.

### 2.5 The split protocol costs more than the modalities buy

Two entries measure this directly on their own data, and the arithmetic is theirs.

- [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  — holding the four-modality input fixed, moving from 10-fold to LOSO drops binary accuracy 74.78%
  → 67.04% and ternary 60.90% → 47.80%. Those drops, 7.74 and 13.1 points, are each larger than the
  entire EEG-to-all-four gain under LOSO, 5.84 and 6.21 points. The card states the consequence:
  "any project reporting a fusion gain under record-wise folds is reporting a number smaller than its
  own split-protocol artifact."
- [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) —
  the same fused system falls from 85.11% within session to 72.39% across sessions on the same
  subjects, a 12.7-point cost from session change alone, "larger than most reported fusion gains in
  this strand".

### 2.6 The denominator is unverifiable

[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
states that WESAD "consists of synchronised, high-resolution EEG and ECG recordings for 14 channels"
at 700 Hz and that CASE "offers an EEG with a maximum of 32 EEG electrodes". The card records that
neither public dataset distributes EEG at all — WESAD's chest RespiBAN carries ECG, EDA, EMG,
respiration, temperature and acceleration, with 700 Hz being its sampling rate rather than an EEG
rate, and CASE carries ECG, blood volume pulse, EMG, galvanic skin response, respiration and skin
temperature. Since the EEG-only arm is the denominator of the claimed peripheral gain, the card's
conclusion is that "the gain cannot be trusted either". This is the reason a paper carrying the
strand's most complete ablation table is marked `relevance: low`.

The entry is nonetheless the strand's cleanest cautionary case of a well-formed ablation table
sitting on top of an unverifiable dataset claim — a failure mode invisible to a reading of the
tables alone.

### 2.7 The mechanism that makes the peripheral channel informative differs by study

The peripheral arms in §1.1 are not measuring the same thing, and the cards state the mechanism in
each case.

- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — heart
  rate and LF/HF against a Montreal Imaging Stress Task, an arousal manipulation by design. The card
  states the transfer limit: "a spoken-versus-written stimulus contrast has no comparable arousal
  manipulation, so the mechanism that makes ECG informative in this paper may not be present."
- [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  — electrodermal activity against an acoustic annoyance manipulation. The card records the reverse
  limit: EDA is "slow, tonic, and the least likely of the peripheral channels to track a
  stimulus-locked contrast", so its null "is weaker evidence about ECG or EOG than about autonomic
  arousal generally".
- [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  — cognitive load manipulated by driving-scenario complexity, which changes the visual scene, so the
  gaze channel's contribution "could reflect the scene rather than the load".
- [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
  — WAUC's manipulation is exercise intensity on a cycle or rowing machine, so decoding "cognitive
  load" from ECG and EDA there "is close to decoding the exercise level".

### 2.8 Subgroup composition entangled with accuracy

Two entries report a sex difference and neither separates it from cohort composition. In
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md), females
were 45 of 66 participants and were classified more accurately, and the card notes that a class-size
explanation is not excluded. In
[wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md),
female patients were more likely to be classified as inadequately sedated, and sex is itself among
the top SHAP predictors. The two run in different directions and neither is adjudicated here. The
same shape appears on a different variable in
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md), whose Fitzpatrick skin-tone
benchmark is the strand's only fairness evaluation and exists because PPG amplitude depends on
optical absorption.

---

## 3. What the gain was measured against: split geometry and chance

The single property that most changes how a number in §2 should be read, and the axis the index does
not carry. Five regimes appear.

### 3.1 Subject- or patient-disjoint, stated

- [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  — 5-fold GroupKFold with all windows from a participant confined to one fold; within each training
  fold, 15% held out and split 1:1 into a temperature-scaling calibration subset and a
  fusion/threshold subset, so the test folds are used for nothing but testing. The card names this
  "the protocol this project should copy", and it is the protocol under which the gain evaporates.
- [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  — leave-one-subject-out reported in full and separately from 10-fold, for both label
  granularities. The strand's only entry that reports both regimes side by side rather than choosing
  one.
- [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
  — patient-ID-level 80/20, explicitly motivated: "To avoid potential data leakage, train/test
  splitting was performed at the patient ID level."
- [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
  — subject IDs used to keep training and test subjects disjoint, but five-second segmentation
  "to increase the sample count" inflates the within-subject sample count, which the card notes
  protects against cross-subject leakage and not against the resulting optimism in the variance
  estimate.
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — a subject-wise held-out test set of three participants, with training and validation stratified
  by dataset and gender. Subject-disjoint in form; the card records that three subjects cannot
  support a 95.7% point estimate, with no confidence interval, repeated-split variance or per-subject
  breakdown reported.
- [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) — MIMIC-IV-ECG
  split by patient only, because acquisition dates are imprecise; UHN-ECG excluded from pretraining
  entirely to serve as a cross-dataset generalisation test.

### 3.2 Within-subject by design

- [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
  — individually tuned models, the first part of each participant's data for training and the last
  part for testing, explicitly to avoid inflation from time dependencies. This is closer to a
  deployment protocol than random cross-validation, and the card is equally explicit that "the
  numbers say nothing about cross-subject transfer". The strand's null therefore comes from the
  regime where a personalised model is strongest.
- [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) —
  the 72.39% is across three sessions within subject; whether the 85.11% is within- or cross-subject
  is not accessible.

### 3.3 A sample-level split that leaks participant identity

- [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
  — "stratified KFold to create five different splits in our dataset" stratifies by class, not by
  participant, so windows from the same participant appear on both sides. The card reads the
  consequence through the finding itself: the dominant features are *changes* in pupil diameter,
  "which is the right normalisation for a within-subject comparison and the wrong one for a
  cross-subject one", and 91.66% "should therefore be read as a within-subject-leakage-inclusive
  number".

### 3.4 Random cross-validation as the object of study

- [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  — the only entry in the strand where the split geometry is the finding rather than a caveat. Under
  random cross-validation, "different short-term windows within a trial are randomly divided between
  the test and train set", so a test segment usually has a training segment nearby in time carrying
  the same fingerprint. Trained to predict trial identity instead of attention, the same pipeline
  reaches median 100%, 99.9%, 99.7% and 99.6% across the four conditions, significantly above the
  attention accuracies themselves, and the authors conclude "trial fingerprints are even more
  dominant than spatial auditory attention patterns". Where a study has one attention label per
  trial, the attention label and the trial label are the same variable — which applies to any
  stimulus-blocked design.

### 3.5 The split is stated inconsistently, or not at all

- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — the
  paper states subject-wise grouping, an 80/20 split, *and* stratified 10-fold cross-validation. The
  card records that these three statements "are not mutually consistent as written" and that what was
  actually run cannot be determined. This is the most consequential single ambiguity in the strand,
  because it sits under its largest gain.
- Not accessible, in the corpus's sense rather than the source's:
  [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md),
  [li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md),
  [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md),
  [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md).
- Not stated by the source:
  [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md),
  whose card records that "no train/test description was recoverable" from an extraction it calls the
  worst in the strand, and that accuracies of 94.88% and 95.26% on DEAP "are far above typical
  cross-subject figures for that dataset and are only interpretable with the protocol named".

### 3.6 Chance level, class balance, and what is reported against nothing

Several entries report an accuracy with no chance level or class balance, and each card says so
rather than supplying one:
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) (five-class
problem, one rest condition against four arithmetic conditions, "unlikely to be balanced"),
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
(three-state problem),
[ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md),
[wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)
("multiclass" without a class count, which the card says "makes 0.8780 uninterpretable as an effect
size"), and
[wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
(accuracy 0.741 with AUROC 0.825 implies imbalance, and the class balance is not stated).
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
and [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
both record that no permutation test or chance-corrected metric was run.

The sibling strands supply the yardsticks these entries lack, and the connection is worth stating
because it changes how the numbers above should be read.
[datasets-benchmarks/combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
demonstrates that classifying pure Gaussian noise reaches "decoding accuracies of up to 70% or
higher in two-class decoding" at small sample sizes, so a theoretical chance level is not the
threshold. [datasets-benchmarks/varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)
puts a roughly ±10 percentage-point confidence interval on a cross-validated accuracy at the sample
sizes neuroimaging uses. And the split-geometry effect that §3.3 and §3.4 describe qualitatively is
quantified twice elsewhere:
[datasets-benchmarks/kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
replicates five cross-participant EEG models with and without participant holdout and finds error
rates rising between 35 percent and roughly 3,900 percent, and
[eeg-models/brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
measures 99.8 percent under segment-based holdout against 53.0 percent under subject-based holdout on
one dataset.

### 3.7 The comparator graph, which is structure and not evidence

No entry in this strand re-runs another entry's model. **[boundary]** The one measurement that
crosses entries is corroborative rather than comparative:
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)'s
Table 4 independently lists EmotionMeter at 85.11% on SEED-IV, which is the one number recoverable
from the paywalled
[zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md). The
strand's comparisons are otherwise quoted rather than measured, and
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)'s
card states the general hazard for itself: "the comparator numbers are quoted from other papers
rather than re-run, so the ranking inherits every difference in preprocessing and splits among them."
This is why the DCCA disagreement in §9.1 falls between a first-party report and a quoted comparator
table rather than randomly.

Three descent relations are on record:

- Same laboratory, one dataset family:
  [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) →
  [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md),
  the second being "the same laboratory's later systematic comparison of fusion models" and the first
  "the source of the SEED-IV pairing used here".
- Same group, one method:
  [schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) →
  [schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md),
  sharing authors, method and one cohort family. The card instructs that "the two should be read as
  one line of work, not two independent results".
- One re-run under matched labels:
  [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  re-runs its own models under an earlier study's annoyance cutoff, reaching 0.834 unimodal and 0.846
  fused against that study's 0.6383 and 0.6517 — so its late fusion beats the earlier early-fusion
  approach even though its own fusion gain over EEG is negligible.

One weighting note. Every one of the 25 entries is named in the Citations section of at least two
others, and the counts are led by
[haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md) (11),
[makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) (8),
and [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) (8).
That is a fact about how this corpus is wired — the engineered-feature reference points are the
strand's hubs — and it is not evidence about those entries' quality.

---

## 4. Artifact versus signal

The strand contains the same ocular activity described as nuisance and as signal, by different
entries, and the two sides are placed against each other here rather than in separate lists. The
cardiac version of the question follows in §4.4.

### 4.1 The channel carries the label without a cortical contribution

- [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  — the canonical demonstration, and unusual in publishing its own abandoned positive result on
  purpose: "we also present the original analyses to highlight how these might have readily led to
  invalid conclusions". The mechanism named by the authors is that "on perceiving and encoding the
  stimulus, subjects move their eyes in a way systematically related to the identity of the stimulus
  and keep that gaze position stable throughout the entire delay period". The remedy proposed is
  training the decoder on a separate functional localizer designed to elicit bottom-up sensory
  responses without inviting stimulus-specific eye movements.
- [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  — the same argument in EEG, with two independent confounds rather than one. Subject-independent
  CSP accuracies are significant only in the one audiovisually congruent condition "despite a
  comparable amount of training data for all conditions", which the authors read as decoding
  "predominantly driven by signal components that originate from the motion of the eyeballs (i.e.,
  EOG-related components), and therefore have no neurological component whatsoever". The
  trial-fingerprint result (§3.4) generalises past ocular artifact entirely.

Both cards bound their own claims, and the bounds belong here.
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
records decoding above the significance threshold in the three audiovisually *incongruent*
conditions too, which the authors take as evidence of genuine auditory-attention lateralisation:
"the paper does not claim all decoding is artifact".
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
establishes that gaze carries the label and does not report how much of the original neural decoding
was attributable to it, so "the residual cortical effect is undetermined"; the gaze effect is itself
described as significant "only marginally" at encoding, which the card flags as an uncomfortable
combination the paper does not resolve.

### 4.2 The same activity as a legitimate decoder of state

- [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)
  — 0.8780 multiclass cognitive load from eye-movement indices alone. The card states the
  consequence for this project in both directions: ocular artifact removal "is not a neutral cleaning
  step", and a measured gain from adding an ocular channel "may be ocular behaviour, and ocular
  behaviour differs between a spoken and a written stimulus by construction".
- [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
  — mean pupil diameter change in both eyes is the dominant feature and blink rate a moderate
  contributor, at 91.66% for three-level load.
- [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
  — pupil size at 75% is the strongest non-EEG variable in a study that also concludes fusion does
  not help. The card places the eye channel, "not the cardiac or electrodermal channel, as the
  plausible source of any peripheral gain".
- [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) —
  the complementarity localisation: EEG better at happy, eye movements better at fear. The card also
  supplies the counter-reading: "a class-specific advantage for eye movements on 'fear' could reflect
  stimulus properties (a fear clip may have different visual dynamics) rather than an affective
  mechanism."

### 4.3 Where the two sides do not meet

Three specific non-meetings, each grounded in the cards and none of them a matter of the two sides
disagreeing about a number.

**The instrument differs across the fault line.** Every entry in §4.2 measures with an eye tracker:
COLET is an eye-tracking dataset
([wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)),
eye-tracking glasses
([ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)),
an SMI tracker
([zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md)), an
EyeLink 1000 at 1200 Hz
([mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)),
and pupil size
([hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)).
The one entry using actual electrooculography electrodes with their placements on record is
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
— four channels, 1.5 cm above and below the right eye for vertical activity and approximately 1 cm
lateral to each eye for horizontal — and its EOG-only decoder is the weaker arm in every condition.
Several cards state the substitution problem in the same terms: an eye tracker gives position and
pupil diameter, while EOG "gives a potential difference that mixes gaze angle with blink and with the
corneo-retinal standing potential", and the two "overlap but are not interchangeable". **[boundary]**
The strand's constructive ocular results therefore rest on a measurement that an EOG derivation does
not straightforwardly recover.

**Neither side reports what removal costs.** Two cards name the same missing arm independently.
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
records that the paper reports no "EEG with ocular components projected out" arm, "that is the arm
this project would most want, because it is the one that says what ocular artifact removal costs".
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
records that no neural decoding accuracy with the gaze contribution regressed out is reported.

**The visual-input confound is controlled in exactly one place.**
[hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
held both body movement and visual input constant across workload levels, and states its own reason
for doing so: eye-related measures "have probably partly been found to covary with workload due to
the often occurring confound of the amount of visual information", and for pupil dilation "the reason
for its association with workload is unclear". By contrast
[ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)'s
three load levels use different stimuli — single words against sentences — so the display differs
between conditions, and
[angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
manipulates load by scenario complexity, which changes the scene. The one entry that removed the
confound is the one that found no fusion gain.

### 4.4 The cardiac version of the same question

- [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) — the
  directional claim (§5).
- [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
  — the redundancy scenario made concrete: peripheral physiology recovers an EEG-derived index at
  AUROC 0.825, which the card reads narrowly as showing that "peripheral physiology tracks *something
  an EEG-derived index also tracks*". The card supplies its own alternative explanation: anaesthetic
  agents directly manipulate both the EEG and the cardiovascular system, so the association "may be
  substantially mediated by drug concentration rather than by any central-peripheral coupling", and
  intraoperative dosing is unadjusted in the accessible text.
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — a design-level instance rather than an empirical one: ICA is applied to remove eye movement,
  muscle *and cardiac* interference from the EEG stream while ECG is the second modality, which the
  card flags as "the one preprocessing step that would suppress the shared component" the fusion is
  supposed to exploit.
- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — its EEG
  arm is a single scalar, the theta/alpha ratio, computed from a published feature table rather than
  raw signal, so "nothing can be said about artifact handling, and the possibility that the EEG
  theta/alpha ratio is itself contaminated by muscle or ocular activity during arithmetic is not
  addressed".

### 4.5 What preprocessing did, and what it did not do

The strand's artifact-removal practice, as reported:
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
cleaned "regular artifacts such as heartbeat, blinks and eye movements" and the authors state that
"the removal of eye movement-related artifacts was imperfect";
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
applies ICA, described twice in its own methods with different wording;
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
preprocesses in EEGLAB and "notes explicitly that scalp EEG is sensitive to ocular and muscular
contamination" while running no control of the kind §4.1 describes; and
[zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) reports no
artifact handling in its accessible text, which matters because its left-lateralised frontal-central
topography is "consistent with a genuine affective asymmetry and equally consistent with ocular and
muscular contamination of frontal channels during video viewing".

The methodological control the strand does not carry itself sits in the sibling strands:
[candidate-datasets/snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
establishes that of the two standard ways of removing a confound from a decoding analysis, post hoc
counterbalancing biases upward and confound regression biases downward far enough to produce
significant below-chance accuracy, and only confound regression performed inside every
cross-validation fold is unbiased.

---

## 5. Coupling, which is a different question from fusion

Three entries use convergent cross mapping and one uses canonical correlation. None of them
classifies anything, which is why §1.7 holds them apart from the ablation axis; the question they ask
is whether cardiac and cortical activity drive each other, not whether concatenating them helps.
That question bears on fusion because it predicts the answer: if the cardiac signal is largely
downstream of the central state the EEG already carries, adding it should buy little.

### 5.1 The application

- [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) —
  32-channel EEG and single-lead ECG during validated virtual-reality videos eliciting positive or
  negative affect, with CCM applied to heartbeat-evoked potentials and full cardiac waveforms treated
  as evolving dynamical systems rather than to band powers and HRV indices. The reported asymmetry is
  that descending, cortical-to-cardiac coupling is "stronger, more sustained, and spatially focused"
  than ascending, with preferential enhancement of the descending direction under emotional
  conditions, and a left-lateralised frontal-central topography.

The three facts the brief asked this entry for are all inaccessible: the strength of coupling (no
coefficients, no significance levels, no effect sizes), the time scales, and whether the analysis
controlled for the video stimulus driving both signals. That last is, in the card's words, "the
single most important control for a coupling claim of this kind", and without it "'descending
coupling' and 'the stimulus drives cortex first and heart second with a lag' are not distinguished".

### 5.2 The methods entries that condition it

- [schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) — the
  parameter-sensitivity reference. Its abstract states that "influence of estimation parameters could
  be demonstrated by means of simulated data", and the card is explicit that this "is what licenses
  Phase 3 to treat the direction claim in `zeng-brain-heart-ccm` as conditional on its parameter
  settings rather than as a fact about the nervous system". *Which* parameters, over what ranges, by
  how much, and what the paper recommends are all reported but not accessible: it is a four-page
  conference paper behind a paywall. The entry also supplies the interval-based CCM adaptation, which
  is the form a stimulus-locked analysis would need since standard CCM assumes a stationary system and
  a long observation.
- [schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md)
  — the processing-and-statistics companion, organising a brain-heart CCM analysis along four axes:
  time-variant, frequency-dependent, topographical and statistical. The card names what each axis
  guards against: "a CCM coefficient computed on a whole recording hides the time course; one
  computed on broadband signals hides the frequency dependence; one computed on a single electrode
  hides the topography; and one reported without a null distribution hides whether it is
  distinguishable from chance in a system where both signals are autocorrelated." Its statistical
  machinery is surrogate data, bootstrapping and linear mixed-effects models.

### 5.3 The relation between them, which is the structural point

Four things follow from placing the three entries together, and each is stated on a card.

The application reports none of the machinery the methods entries propose.
[schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md)'s
card puts it directly: "`zeng-brain-heart-ccm`, the application entry in this strand, reports no
comparable machinery in its abstract, which is a reason to weight the two differently."

The two methods entries are one position, not two.
[schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) and
[schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md)
share authors, method and one cohort family (children with temporal lobe epilepsy), and whether the
2019 paper supersedes the 2015 parameter analysis or complements it "cannot be determined without
both full texts". A reader counting them as two independent methodological cautions would be
double-counting one group.

The direction claim has an independent alternative explanation that is not a parameter-sensitivity
objection.
[zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md)'s own card
supplies it: CCM's ability to detect cross-mapping in one direction depends on how well each system's
attractor is reconstructed from its own observable, and "single-lead ECG reconstructs a cardiac
attractor far more cleanly than 32-channel scalp EEG reconstructs a cortical one, which could bias
the detected direction" — toward exactly the direction reported.

All three CCM entries are inaccessible on their decisive quantity, and in all three cases the source
reports it. **[boundary]** That is one property in the inaccessible-not-unreported register of §9.4
rather than three independent gaps: coupling strength and time scales in the application, parameter
identities and ranges in the 2015 methods paper, coupling values and cohort sizes in the 2019 one.

### 5.4 The earlier, symmetric instrument

- [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) —
  canonical correlation analysis and temporal kernel CCA over neural, vascular and autonomic domains,
  used "to find neural-vascular-autonomic coupling rather than to classify directly", with the 19%
  multimodal-improvement claim attached. Its own card names the succession: the directed-coupling
  framing "supersedes symmetric CCA for asking which system drives which". A symmetric measure cannot
  produce the asymmetry that §5.1 reports and §5.3 conditions, which is why this entry sits alongside
  the CCM line rather than inside it.

### 5.5 What the coupling literature predicts, and which fusion entries match

Stated as a relation between two facets, not as a verdict. If descending coupling dominates, adding
a cardiac channel to an EEG embedding is closer to a noisy copy of information the encoder already
has than to a new source, and a measured gain "would then need another explanation: better
signal-to-noise on a slow component, a different temporal integration window, or artifact".

Consistent with that prediction:
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
(+0.002, though on EDA rather than ECG),
[hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
(not significant), and the EEG+ECG cell of
[angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)'s
grid specifically (61.20% → 63.95%, the smallest of its three pairings). Inconsistent with it:
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) (+12.6 from
heart rate and LF/HF) and
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
(+11.6, denominator unverifiable per §2.6). Both of the inconsistent entries carry the split or
provenance flags of §2.1; neither the prediction nor the exception is adjudicated here.

The same prediction shows up as a design decision rather than a result in two architectures.
[li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md)
includes Low Rank Fusion specifically to remove "the information redundancy that fusion introduces",
which its card calls "an unusually explicit acknowledgement that redundancy is the default outcome".
And [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md)'s
deep canonical correlation analysis "maximises canonical correlation between modalities, which by
construction rewards the *shared* component of the two signals" — the component the coupling result
says is dominant. See §7.4.

---

## 6. Modality coverage, and what the controlled spellings hide

The brief fixed the spellings `eeg`, `ecg`, `ppg`, `eog`, `eda`, `resp` so a modality-by-task matrix
could be built mechanically. It can be, and the matrix below is read from the 25 frontmatter blocks.
The rest of this node is what the matrix does not carry.

### 6.1 The matrix

| entry | eeg | ecg | ppg | eog | eda | resp |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md) | | • | | • | | |
| [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md) | • | • | | • | • | |
| [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md) | • | | | | • | |
| [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md) | • | | • | • | • | • |
| [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) | • | • | | | | |
| [haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md) | | • | • | | • | |
| [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md) | • | • | | • | • | • |
| [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md) | • | • | | | | |
| [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md) | | • | | | • | |
| [lee-2025-biosignal-fm-review](../collection/multimodal-biosignals/lee-2025-biosignal-fm-review/card.md) | • | • | • | • | | |
| [li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md) | • | • | | • | • | • |
| [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md) | • | • | | • | | |
| [liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md) | • | • | | • | • | • |
| [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) | | • | • | | • | • |
| [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) | | • | | | | |
| [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md) | | | | • | | |
| [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) | | | • | | | |
| [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md) | • | | | • | | |
| [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) | • | • | | | | |
| [schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md) | • | • | | | | |
| [schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) | • | • | | | | |
| [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md) | | • | • | | | |
| [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md) | | | | • | | |
| [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) | • | • | | | | |
| [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) | • | | | • | | |
| **total** | **16** | **18** | **6** | **12** | **9** | **5** |

Pairings with EEG, which is the axis the project's third comparison runs along: `eeg`+`ecg` in 11
entries, `eeg`+`eog` in 9, `eeg`+`eda` in 6, `eeg`+`resp` in 4, `eeg`+`ppg` in 2.

Of the four `eeg`+`resp` entries, three carry no accessible EEG-versus-combined number —
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
has no unimodal arm,
[li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md)
has no accessible numbers, and
[liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md)
is a review — leaving
[hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md),
where respiration frequency at 69% is one of only two non-EEG variables exceeding chance and the
combined arm is not significantly better. **[boundary]** This matters because
[candidate-datasets/strum-2018](../collection/candidate-datasets/strum-2018/card.md) records that the
project's target recording carries a 16-channel respiration belt alongside 2-channel ECG and
2-channel EOG.

### 6.2 The tag is not always the measurement

The controlled vocabulary was fixed for mechanical matrix-building and it is doing that job, but six
entries carry a tag whose instrument differs from what the spelling names. Every one of those cards
states the substitution itself, so this is a property of the vocabulary rather than a carding error.

- `eog` where the instrument is an eye tracker, not electrooculography electrodes:
  [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) (SMI
  tracker; "the card records `eog` per the controlled vocabulary, but the measurement is eye
  tracking"),
  [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
  (eye-tracking glasses; "the actual instruments are an eye tracker and a heart-rate sensor, not
  electrooculography electrodes and a clinical ECG"),
  [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)
  (COLET, an eye-tracking dataset),
  [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  (EyeLink 1000; "a deliberate abstraction"), and
  [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  (gaze as an eye-movement proxy; "an eye tracker gives position, EOG gives a potential difference
  that mixes gaze angle with blink and with the corneo-retinal offset").
- `ecg` where the derivation is optical:
  [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md)'s
  HRV comes from an earplug PPG sensor, and the card records that "beat-interval estimates from PPG
  carry pulse-transit-time variability that ECG-derived intervals do not, so HRV features are not
  interchangeable between the two".

The same conflation is a property of the literature and not only of this corpus:
[haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md)
records that its 43 studies pool ECG-derived and PPG-derived HRV under one name, drawing intervals
from clinical ECG, wrist PPG, a Polar chest strap, ballistocardiography and in one case Fitbit
activity summaries, and that "a review that pools them is pooling different measurements under one
name".

### 6.3 Tags that are provisional, and channels the vocabulary cannot express

Two entries have modality lists inferred from their datasets rather than read from the paper, and
both cards say so.
[li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md)'s
list is mapped from DEAP's and WESAD's channel sets — "It is *not* read from the paper. Phase 3
should treat the modality tags for this entry as provisional" — and
[liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md)'s
is inferred from an abstract that says only "EEG and other physiological signals".

Three entries carry a channel the vocabulary has no spelling for, and the matrix under-reports them
by one each: EMG in
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
(DEAP's two EMG channels; the card states the matrix "will therefore under-report this entry by one
channel"),
[makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) and
[lee-2025-biosignal-fm-review](../collection/multimodal-biosignals/lee-2025-biosignal-fm-review/card.md).
Separately,
[wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
is correctly *not* tagged `resp` even though a respiratory quantity carries much of its decoding:
"respiration enters only as end-tidal CO2, a capnograph-derived vital sign, not as a respiratory
waveform."

One further distinction the tag flattens.
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md)'s `ecg` and
`eeg` are a published feature table of three scalars, not waveforms, which is why its card can say
nothing about artifact handling (§4.4).

---

## 7. Fusion mechanism: where the streams meet, and what the objective rewards

### 7.1 Feature concatenation before one classifier

- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — three
  engineered scalars, screened with Shapiro-Wilk and Kruskal-Wallis, reduced with principal component
  analysis, fed to six classifiers in unimodal and concatenated configurations. Kruskal-Wallis effect
  sizes on the three features: theta/alpha ratio epsilon-squared 0.154, LF/HF 0.094, heart rate 0.030.
- [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  — per-modality hand-crafted feature sets concatenated across the eight modality subsets, with EEG
  contributing 40 features (band powers, spectral entropy, Hjorth mobility and complexity), plus deep
  models on raw signals as a parallel track.

### 7.2 Intermediate fusion, on embeddings

The configuration this project would use, and the strand's densest node.

- [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md)
  — deep canonical correlation analysis against the bimodal deep autoencoder, head to head on five
  datasets, with two new DCCA fusion variants (weighted-sum and attention-based). The card frames the
  design contrast: DCCA "maximises correlation between per-modality projections before
  classification, which is a canonically *intermediate* fusion on embeddings", while BDAE
  "reconstructs both modalities from a shared code, which is closer to early fusion in effect".
- [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
  — the Multimodal Transfer Module recalibrating each modality's features conditional on the other's,
  applied to low-, mid- and high-level CNN activations concatenated within each modality, then late
  fusion for the decision. The card calls MMTM "one of the few mechanisms in this strand that operates
  at exactly that interface", and records the transferable empirical claim: taking three levels rather
  than the last layer alone is worth 2–4%. MMTM is adopted without an ablation against simpler
  recalibration, so its contribution is not isolated from the hierarchical-feature contribution.
- [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
  — dual-branch encoders producing full feature *sequences* rather than static vectors, then
  multi-head cross attention with the EEG representation as Query over the peripheral sequence. The
  sequence-preserving detail is the card's point: "most fusion work reduces each modality to a static
  vector before combining, which discards exactly the temporal offset between a cortical response and
  its peripheral consequence."
- [li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md)
  — a four-component pipeline: a Cross Modal Transformer eliminating incongruity among auxiliary
  modalities, Low Rank Fusion removing the redundancy fusion introduces, a modified CMT enhancing the
  primary modality with each optimised auxiliary in turn, and a Self-Attention Transformer over the
  concatenated enhanced features. The primary/auxiliary asymmetry is designated by unimodal
  performance, which the card notes means "the architecture's structure depends on a measurement the
  paper presumably reports and this card cannot see". How incongruity is operationalised — a learned
  residual, an alignment loss, an attention mask, something else — is unknown.
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — an attention layer weighting two streams, over three frozen pretrained image backbones applied to
  Morlet scalograms stacked into a 128 × 128 × 3 image. The strand's only entry reporting cost
  alongside accuracy: 42.7 M parameters, 3.2 min per training epoch, 18.5 ms inference per sample,
  against 14.7 M / 1.8 min / 12.3 ms for EEG-only VGG16 and 8.3 M / 1.2 min / 8.7 ms for ECG-only raw
  CNN, framed by the authors as "a 5–10% increase in accuracy from multimodal fusion against a 2–3x
  increase in computational cost".

### 7.3 Decision-level fusion

- [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  — each branch's logits temperature-scaled on a held-out calibration subset and then combined by
  stacked late fusion, with the validation gate of §2.2 on top.
- [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
  — a decision-level model combining single-feature model outputs, tried *alongside* feature-level
  fusion. This is what makes its null harder to dismiss, and the authors say so: they used both levels
  and still saw no reliable advantage, and "giving more weight to lower-performing variables hurts".
  Both explanations "cut against the idea that a better fusion architecture would have rescued the
  result".
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — late (average) fusion at 0.914 as one of its two naive baselines, against early fusion at 0.892.

### 7.4 What each objective rewards, which is the axis that matters

The mechanisms above are not interchangeable, because they optimise for opposite properties of the
two signals, and the corpus contains both poles.

At one pole, methods that reward the *shared* component.
[liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md)'s
DCCA maximises canonical correlation between modalities, and its own card names the tension: "that is
the opposite of what a project looking for complementary information wants, and the abstract does not
address the tension". BDAE reconstructs both modalities from a shared code.

At the other, methods built around disagreement.
[li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md)
is the strand's only architecture designed on that principle, and its card states the argument for
why the pole matters: "Most fusion architectures in this strand implicitly assume the modalities agree
and differ only in noise; concatenation, canonical-correlation methods and shared-code autoencoders
all reward the component the signals have in common. If the peripheral channel is largely a downstream
copy of the central state, as `zeng-brain-heart-ccm`'s directional asymmetry suggests, then optimising
for the shared component guarantees the peripheral channel adds nothing new."

In between, mechanisms that reweight rather than align:
[kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)'s
MMTM recalibrates each modality conditional on the other, and
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)'s
cross attention weights the peripheral sequence by relevance to the current EEG feature.

**[boundary]** The strand's one disagreement-based architecture is also its one entry with no
retrievable numbers, so the two poles are not represented by comparable evidence.

### 7.5 Frozen encoders versus end to end

The brief singles out "whether the fusion model is trained end to end or bolts a head onto frozen
encoders, which is the configuration this project would actually use". Four entries speak to it and
none runs it.

- [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) — explicitly framed as
  "both a feature extractor and an encoder for multimodal models"; the card records that "no
  multimodal experiment appears in the evaluation", so the framing is untested.
- [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) — reports
  "competitive linear probing performance, with functionally discriminative embeddings", which is the
  claim a frozen peripheral branch depends on; the linear-probing table "did not survive the
  two-column extraction cleanly, so no frozen-encoder figure is quoted".
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — the closest instance: frozen pretrained backbones over a time-frequency representation with a
  learned attention weighting and a head on top. The backbones are ImageNet-lineage image models, not
  biosignal foundation models.
- [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
  — the dual-branch justification, that separate streams "respect the heterogeneity of the different
  modalities", is the card's reading of "the argument for bolting a head onto frozen encoders rather
  than training end to end", but the paper trains its branches rather than freezing pretrained ones.

Removed during review: this paragraph previously asserted that no entry pairs two frozen pretrained
encoders, and tied that to the project's third comparison. It was marked `[boundary]` and kept, but
`_briefs/synthesis-practice.md` gives that exact sentence as its illustration of what belongs to
Phase 4, so the mark was functioning as a permission slip rather than a flag. The Phase 3 statement
is the enumeration above: four entries speak to the configuration, each declaring its own limit, and
none runs it.

### 7.6 Missing and corrupted channels

- [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) — Random Lead
  Masking, which stochastically masks leads during pretraining so the model can be fine-tuned on
  arbitrary reduced lead sets. Its card calls this "the closest thing in this strand to a principled
  answer to the brief's 'missing or corrupted channels' question", and also records that no result in
  the paper evaluates a single-lead configuration.
- [liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md)
  — its third organising aspect is incomplete multimodal learning, which its card calls "the only
  pointer this strand has into the literature that addresses it". The pointer could not be followed:
  the reference list is paywalled.
- [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md)
  — its card draws the distinction that keeps the two apart: "Adding Gaussian noise to a feature
  vector degrades it smoothly; losing a channel at deployment is a structural change." The paper does
  the former plus one instance of the latter (EEG replacement).
- [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  — no modality-dropout experiment at inference time, "so robustness to a missing channel — the
  scenario a deployed system actually faces — is not evaluated".

### 7.7 Representational budget between the branches

An asymmetry that is invisible in a fusion diagram and is stated numerically on two cards.
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
gives DEAP's eight peripheral channels three summary statistics each, for 24 dimensions, against 310
EEG dimensions on SEED-IV — "a 13:1 imbalance in representational budget before any learning
happens" — and its card notes that whatever cross attention does, "it is attending over a very coarse
peripheral description". The inversion also occurs:
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) gives EEG a
single scalar against ECG's two, with "no other band, no spatial feature, no per-channel information".

---

## 8. The peripheral branch's input contract

### 8.1 The two released peripheral encoders

- [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) — an 18-block ResNet-style
  CNN projecting to 512 dimensions (a PaPaGei-S variant adds an expert block giving 128), pretrained
  on 13,517 participants, 20,751,206 segments and 57,641 hours from VitalDB, the MIMIC-III waveform
  matched subset and the MESA sleep sub-study, with a morphology-based supervision signal in place of
  instance-contrastive learning. Reported gains are 6.3% on classification and 2.9% on regression
  metrics in at least 14 of 20 tasks, while "outperforming models 70 times larger" — a
  parameter-efficiency result the card reads as suggesting "the useful capacity for a single-channel
  peripheral signal is small".
- [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) — 90.9 million
  parameters, wav2vec 2.0 architecture, 1.4 million 5-second 12-lead segments, hybrid masked
  reconstruction plus contrastive objective. Poor-quality records were deliberately *retained* "to
  produce a model more tolerant of real-world artifacts", which the card notes means the corpus size
  is not a curated-hours figure.

Both release weights and neither states a licence for them, which the cards flag individually. That
is the same omission the sibling strand records for every EEG checkpoint it holds — see
[eeg-models/adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md), whose MIT
pipeline licence is the only licence stated for any released artefact in that strand and covers
benchmark code rather than a checkpoint.
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md)'s card makes the connection
explicit: "the licence attached to the released weights is not stated in the extracted text, which is
the same gap the `eeg-models` strand records for its checkpoints."

### 8.2 The engineered alternative

- [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) — a
  three-layer API over ECG, PPG, EDA, EMG and respiration, whose `method` argument propagates through
  the internal functions so that "the sensitivity of a result to preprocessing choices is measurable
  rather than assumed". The card records the licensing split: the article is Springer bronze open
  access with no Creative Commons statement, while the software repository is MIT, "and that licence,
  not the article's, governs use of the code".
- [haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md) —
  establishes the size of the engineered cardiac feature space. Across 43 studies the same dozen
  indices recur: RMSSD, SDNN, SDANN, AVNN, NN50, PNN50, SD1, SD2, LF, HF, LF/HF and mean heart rate.
  The card's reading is that this "is small enough to compute exhaustively — which is what makes the
  classical arm cheap and makes omitting it hard to justify".

What the strand's studies actually computed, which is a narrower set than the vocabulary allows:
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) two indices
(heart rate, LF/HF);
[kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
51 frequency-domain HRV measures per band from pyHRV over Welch spectra, plus 40 EDA statistics;
[wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
27 features reduced to 12 by recursive feature elimination, of which only one HRV index reaches the
top eight by SHAP;
[ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
pupil diameter change, blink rate, heart rate and HRV;
[hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
band powers, an ERP amplitude, HRV bands, respiration rate, pupil size and blink counts. And
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
hand-rolls the tonic/phasic EDA decomposition with a 10 s centred moving average, which
[makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md)'s card
names as "the situation the tool exists to prevent".

**[boundary]** No entry in the strand compares an engineered peripheral feature set against a learned
peripheral representation on the same task. Both category-5 cards say so of their own accord:
[haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md)
"predates the peripheral-foundation-model literature and therefore cannot say whether learned
representations beat these engineered features", and
[makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md)
records the same absence.

### 8.3 The window mismatch, which every entry that names both windows names as a mismatch

The strongest cross-card regularity in this facet. The peripheral branch's natural integration window
is five to sixty seconds; a stimulus-locked EEG epoch is two to four. Eight entries state a window and
none reconciles the two scales.

- [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  — EEG non-overlapping 2 s at 128 Hz against EDA non-overlapping 20 s at 4 Hz. Its card names the
  consequence for the EDA arm's weakness: "the two branches are not decoding the same temporal object.
  Some of the EDA arm's weakness is a resolution mismatch rather than an absence of information, and
  the paper does not separate the two." The ablation finds 6 s EEG and 5–10 s EDA windows most stable.
- [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
  — the only entry that sweeps the window: 2, 6, 10 and 20 s, with 2 s to 20 s buying about 0.012
  AUROC. The card reads it as "small, monotone and not free, since a 20 s window cannot resolve a
  stimulus-locked contrast. The peripheral channel's information here is slow and mostly not improved
  by looking longer."
- [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) — 5 s
  non-overlapping segments, "long relative to a stimulus-locked EEG epoch and short relative to
  reliable HRV estimation — an awkward middle for either use".
- [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) — 60 s segments.
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — 10 s non-overlapping epochs, each "treated as an independent sample".
- [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
  — 5 s segments, chosen "to increase the sample count".
- [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
  — a 4 s non-overlapping Hanning window for the EEG differential-entropy features.
- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — the HRV
  window is unspecified, "so the temporal resolution of the fused decision is unstated. This matters
  for STRUM, where stimulus-locked epochs are short relative to HRV estimation windows."

[makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) is the
toolkit-level recognition of the same fact: it "treats these as separate workflows rather than
conflating them", with event-related and interval-related analyses as distinct pipelines, because "a
stimulus-locked epoch is event-related, while HRV and tonic EDA are interval-related and need windows
longer than an epoch".

### 8.4 Sampling rates

No two peripheral contracts in the strand share a rate, and none matches an EEG one.
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) resamples everything to
125 Hz, the lowest rate among its three sources (500, 125 and 256 Hz), with no ablation reporting the
cost. [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) resamples
to 500 Hz by linear interpolation.
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
runs EEG at 128 Hz and EDA at 4 Hz after a 1.9 Hz low-pass.
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
records at 8192 Hz.
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
misattributes 700 Hz to an EEG stream when it is a peripheral sampling rate (§2.6). Two cards name
this as the concrete form of the brief's sampling-rate question:
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) ("any peripheral encoder
bolted onto an EEG pipeline inherits a resampling and filtering stage of its own, at a rate unrelated
to the EEG rate") and
[mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) ("both the rate
and the window differ from anything an EEG encoder wants").

### 8.5 Acquisition, as the constraint under all of the above

- [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) —
  the strand's only hardware entry, and its contribution is at the synchronisation layer: a sub-200 g
  headband and earplug system with a multi-loop low-noise amplifier achieving over 130 dB common-mode
  rejection on the EEG front end, which is "the specification that makes it possible: the EEG channel
  has to reject the stimulation and the optical driver currents sharing the same head". Two EEG
  channels, which the card notes "would not satisfy the input contract of any of the pretrained EEG
  encoders in the `eeg-models` strand".

---

## 9. Where the corpus disagrees with itself

A register. Nothing here is resolved, because resolving it would require the sources, and in several
cases the sources contradict themselves so there is nothing to resolve to.

No paper in this strand is carded twice, in this strand or across strands. `tools/validate_corpus.py`
reports four identifiers carded in two strands each across the corpus's 84 entries — three dataset or
standard entries shared between `datasets-benchmarks` and `candidate-datasets`, and AdaBrain-Bench
shared between `datasets-benchmarks` and `eeg-models`, which is the deliberate cross-listing whose
divergence the `eeg-models` ontology files. None of the four is a `multimodal-biosignals` paper.
**There are therefore no same-paper card divergences to file as corpus defects from this strand.** The
one card-level defect the strand does contain is recorded in §9.2.

### 9.1 Cards disagreeing about the same quantity

**DCCA's accuracy on SEED-IV — 87.5% or 78.74%.**

| value | card |
|---|---|
| 87.5% on SEED-IV, first-party, reported by the authors of the DCCA extension | [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md) |
| 78.74 on SEED-IV, in a comparator table | [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md) |

An 8.8-point spread on the same method and the same dataset. It is not adjudicable inside the corpus:
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)'s
card records that its comparator numbers are quoted from other papers rather than re-run, so the
lower value may be an older DCCA configuration or a different split rather than a re-measurement, and
[liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md)'s
own split protocol is not accessible. The disagreement is load-bearing in one direction only: it sits
under
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)'s
claim to beat DCCA on SEED-IV (89.12 against 78.74), a 10.4-point margin that becomes 1.6 points under
the first-party figure.

**Whether DEAP carries an ECG channel — three cards, two strands, three positions.**

| position | card |
|---|---|
| DEAP's peripheral set includes `ecg`, as an inferred modality tag | [li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md) |
| DEAP's eight peripheral channels enumerated as 2 EOG, 2 EMG, 1 GSR, 1 skin temperature, 1 respiration, 1 blood volume pressure — no ECG | [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md) |
| the source paper contradicts itself; one enumeration includes "electrocardiogram" and the sensor-placement figure does not; the card "does not assert that DEAP carries ECG" | [candidate-datasets/deap-2012](../collection/candidate-datasets/deap-2012/card.md) |

This one is traceable to its origin, which makes it kind 1 with a kind 2 underneath: the underlying
disagreement is inside the DEAP paper, and the three cards took three different positions on it. The
`li-2023-incongruity-fusion` tag is the weakest of the three by its own admission — its modality list
is "inferred from DEAP's channel set... It is *not* read from the paper" and is marked provisional. A
Phase 4 modality matrix keying on `ecg` will otherwise count that entry as an EEG-plus-ECG study on
the strength of a channel that may not exist.

**A corroboration, recorded so it is not mistaken for the pattern above.** EmotionMeter's 85.11% on
SEED-IV appears in
[zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) from
the paper's own abstract and in
[ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)'s
Table 4 as a quoted comparator. The two agree. This is the strand's only independently corroborated
number, and it is the only accessible number from a paywalled entry.

**A card contradicting its source's factual claim, rather than another card.**
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
records the paper's participant arithmetic (35 = WESAD 15 + CASE 20) alongside the fact that "CASE as
published has 30 participants, so the 20 is unexplained", and records that WESAD and CASE distribute
no EEG at all against the paper's claim that both do. These are the card checking the source against
the public record, not two records of one work disagreeing.

### 9.2 Sources contradicting themselves, carded faithfully

Distinct from §9.1: here one paper disagrees with itself and the card records both readings rather
than silently picking.

- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — three
  separate self-contradictions, and they are the reason its headline cannot be quoted. (i) The abstract
  claims 94.7% "in the combined-gender classification of cognitive stress" *and* "a peak average
  accuracy of 92.6%"; in Table 8, 94.7% is the SVM's accuracy for rest-versus-low-stress only, one cell
  of a three-condition row whose average is 85.7%. The card takes the table values per the
  tables-over-prose rule. (ii) The abstract attributes 90.9% to sex-specific classification generally
  while the body attributes 90% to males and 90.9% to females and Table 7's linear-discriminant row
  shows 86.6% and 87.4%. (iii) The split is described three mutually inconsistent ways (§3.5).
- [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  — the three noise conditions are labelled "40, 60, and 80 dB" in the abstract and class-distribution
  prose and "40 Hz", "60 Hz", "80 Hz" in Table 3 and its surrounding text, "repeated often enough that
  it is not a single typographic slip". Separately, the annoyance cutoff is justified by a citation
  rendered in the published text as the literal word "(reference)", an unresolved placeholder.
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — the dataset claim of §2.6 and §9.1, plus ICA described twice in its own EEG pipeline with different
  wording and one sentence referring to "the undetectable model".
- [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
  — the eight EDA statistical features list "min" twice, "which is either a typographic error or an
  undocumented distinction".
- [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) — the
  strand brief names six authors where the published record has seven, and renders the title with
  "transcranial Electrical Stimulation" spelled out where the published title abbreviates to "tES".
  These are brief-versus-record differences rather than source self-contradictions and are filed here
  only so they are not later read as two different papers.
- [liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md)
  — same shape: the brief's "and colleagues" resolves to two named authors, giving seven in total,
  identical across OpenAlex and Crossref.

**The one defect in this corpus's own record.**
[wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
records that an earlier version of its own card gave 0.753 as the accuracy paired with the 20 s AUROC,
a value that "appears nowhere in the source and is contradicted by this card's own quoted caption
list", most likely misread off a plotted bar. The card lists the fourteen values the re-extracted
figure text does contain, none of which is 0.753, and leaves the value unstated rather than replacing
it with a guess. This is the only place in the strand where the corpus carried a number the source
does not contain, and the card filed the correction itself.

### 9.3 Differences that look like disagreements and are not

Recorded so they are not promoted into §9.1.

**Publication years split between online posting and issue of record, in four entries.**
[zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) — 2018
by DOI and OpenAlex (early access), issue of record IEEE TCYB 49(3), 1110–1122, 2019.
[ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
— online 2020, print issue Personal and Ubiquitous Computing 27(6), 2027–2041, 2023.
[li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md) —
2023 in OpenAlex and Semantic Scholar, May 2024 in Crossref.
[ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) —
December 2015 issue per PubMed, 2016 in Crossref and OpenAlex (the online year), with the DOI suffix
agreeing with 2015. In each case the card states which value it uses and why.

**Pre- and post-curation corpus counts.**
[mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) — "a study using
1.5 million 12-lead ECGs" in the abstract against "pretrained on 1.4 million ECG segments" in the
introduction. The card records these as "consistent only if curation removed roughly 100,000 records,
which Figure 1 apparently documents", and notes that neither place says so.

**A truncated page range.**
[schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) — pages
7418–7421, recorded by OpenAlex in the truncated PubMed style "7418-21".

**Not a rounding, filed here only to keep it out of this node.**
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md)'s 94.7
against 92.6 is a single table cell against a row average, not two roundings of one figure; it belongs
in §9.2.

### 9.4 Inaccessible versus unreported

The distinction the practice brief requires be carried into synthesis. In this strand it is large
enough to need a node: nineteen of the 25 entries have at least one decisive fact in one column or the
other, and the two columns have opposite implications for whether re-retrieval is worth doing.

**Reported by the source, and not accessible to this corpus.** Re-retrieval would recover these.

| entry | what is missing |
|---|---|
| [li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md) | every number; no abstract deposited in Crossref, none in OpenAlex or Semantic Scholar, ScienceDirect returns an anti-bot challenge for both plausible PII values |
| [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) | coupling strength, time scales, shared-input control, participant count; IOP anti-bot barrier |
| [schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) | which estimation parameters matter, over what ranges, and the recommendations |
| [schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md) | coupling values, cohort sizes, the preprocessing schemes themselves; recorded CC-BY upstream, publisher PDF unretrievable |
| [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) | both unimodal accuracies, split protocol, participant count |
| [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md) | the EEG-replacement result, the unimodal arms, the split |
| [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) | the baseline behind the 19% claim, the arms, task, n and split |
| [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md) | class count, chance level, split, participant count, which indices carry the classification |
| [lee-2025-biosignal-fm-review](../collection/multimodal-biosignals/lee-2025-biosignal-fm-review/card.md) | contents, model coverage, any comparison table, reference list; Cloudflare challenge, HTTP 403 |
| [liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md) | reference list, taxonomies, tabulated datasets |
| [haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md) | per-study accuracy figures; the landscape tables collapse in two-column extraction |
| [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md) | per-dataset accuracies; Tables 2 and 3 collapse entirely |
| [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md) | per-condition accuracies across the four comparisons; Figure 3 is an image and did not convert |
| [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) | the skin-tone stratified results; Figure 26 converts to character soup |
| [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) | the linear-probing figures |
| [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md) | the accuracy paired with the 20 s AUROC; needs the figure itself |
| [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) | the validation evidence behind "validated pipelines" |
| [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md) | the exact analysed n; the exclusion sentence is mangled in extraction |

**Not reported by the source.** Re-retrieval would recover nothing.

- [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
  — no unimodal arm of any kind, and no ablation of its own cross-attention module. Its card marks the
  distinction explicitly: "This is a gap in the source, not in this corpus's access."
- [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  — no physiology-only arm, no permutation test, no chance-corrected metric, no modality-dropout
  experiment, no standard deviations in the modality tables.
- [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
  and [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md)
  — no EEG arm, by study design in both cases.
- [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  — no confidence interval, no repeated-split variance, no per-subject breakdown, no chance level or
  class balance.
- [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) — no chance
  level or class-balance figure for the five-class problem, and no HRV window specification.
- [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  — no permutation test, and no count of how often its fusion gate fired.
- [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md)
  — no variance and no significance test behind the 1–2% and 2–4% ranges.
- [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) — no
  test statistic or multiple-comparison correction accompanies "significantly enhance" in the abstract.
- [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  — no "EEG with ocular components projected out" arm (§4.3).

**[boundary]** Both review-shaped entries fall in the first column for the same reason, and the
consequence is recorded on both cards: neither reference list could be mined, so neither review
produced a downstream entry in this strand.

---

## Coverage: all 25 entries and where each sits

The "primary" column is §1, which partitions the strand exhaustively and without overlap; every entry
therefore has exactly one primary node. Every entry also appears in §6's matrix, which is omitted from
the "also appears in" column since it is universal.

| entry | primary node (§1) | also appears in |
|---|---|---|
| [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md) | §1.6 peripheral only, no EEG | §3.3, §4.2, §4.3, §8.2, §9.3, §9.4 |
| [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md) | §1.2 EEG-only and combined, no physiology-only | §2.1, §2.5, §2.7, §3.1, §3.6, §4.3, §5.5, §7.1, §7.6, §9.4 |
| [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md) | §1.1 three arms readable | §2.1, §2.2, §2.7, §3.1, §3.6, §3.7, §4.5, §5.5, §7.3, §8.2, §8.3, §8.4, §9.2, §9.4 |
| [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md) | §1.5 combined only | §3.5, §3.7, §7.2, §7.4, §7.5, §7.7, §8.3, §9.1, §9.4 |
| [ha-wearable-eeg-heg-hrv](../collection/multimodal-biosignals/ha-wearable-eeg-heg-hrv/card.md) | §1.4 comparison inaccessible | §2.1, §5.4, §6.2, §8.5, §9.2, §9.3, §9.4 |
| [haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md) | §1.7 no decoding arm | §3.7, §6.2, §8.2, §9.4 |
| [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md) | §1.1 three arms readable | §2.1, §3.2, §4.2, §4.3, §5.5, §6.1, §7.3, §8.2, §9.4 |
| [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md) | §1.1 three arms readable | §2.1, §2.3, §2.6, §3.1, §3.6, §4.4, §4.5, §5.5, §7.2, §7.3, §7.5, §8.4, §9.1, §9.2, §9.4 |
| [kuttala-2023-hierarchical-fusion](../collection/multimodal-biosignals/kuttala-2023-hierarchical-fusion/card.md) | §1.6 peripheral only, no EEG | §2.7, §3.1, §7.2, §8.2, §8.3, §9.2, §9.4 |
| [lee-2025-biosignal-fm-review](../collection/multimodal-biosignals/lee-2025-biosignal-fm-review/card.md) | §1.7 no decoding arm | §6.3, §9.4 |
| [li-2023-incongruity-fusion](../collection/multimodal-biosignals/li-2023-incongruity-fusion/card.md) | §1.4 comparison inaccessible | §5.5, §6.3, §7.2, §7.4, §9.1, §9.3, §9.4 |
| [liu-2022-multimodal-robustness](../collection/multimodal-biosignals/liu-2022-multimodal-robustness/card.md) | §1.4 comparison inaccessible | §3.5, §3.7, §5.5, §7.2, §7.4, §7.6, §9.1, §9.4 |
| [liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md) | §1.7 no decoding arm | §6.3, §7.6, §9.2, §9.4 |
| [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md) | §1.7 no decoding arm | §3.7, §6.3, §8.2, §8.3, §9.4 |
| [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md) | §1.6 peripheral only, no EEG | §3.1, §7.5, §7.6, §8.1, §8.3, §8.4, §9.3, §9.4 |
| [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md) | §1.3 EEG-only and peripheral-only, no combined | §4.1, §4.3, §4.5, §9.4 |
| [papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) | §1.6 peripheral only, no EEG | §2.8, §7.5, §8.1, §8.3, §8.4, §9.4 |
| [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md) | §1.3 EEG-only and peripheral-only, no combined | §3.4, §4.1, §4.3, §4.5, §8.4, §9.4 |
| [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) | §1.1 three arms readable | §2.1, §2.4, §2.7, §2.8, §3.5, §3.6, §3.7, §4.4, §5.5, §6.2, §7.1, §7.7, §8.2, §8.3, §9.2, §9.3, §9.4 |
| [schiecke-2019-brain-heart-ccm](../collection/multimodal-biosignals/schiecke-2019-brain-heart-ccm/card.md) | §1.7 no decoding arm | §3.7, §5.2, §5.3, §9.4 |
| [schiecke-ccm-methods](../collection/multimodal-biosignals/schiecke-ccm-methods/card.md) | §1.7 no decoding arm | §3.7, §5.2, §5.3, §9.3, §9.4 |
| [wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md) | §1.6 peripheral only, no EEG | §2.8, §3.1, §3.6, §4.4, §6.3, §8.2, §8.3, §9.2, §9.4 |
| [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md) | §1.6 peripheral only, no EEG | §3.5, §3.6, §4.2, §4.3, §9.4 |
| [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) | §1.7 no decoding arm | §4.4, §4.5, §5.1, §5.3, §5.5, §7.4, §9.4 |
| [zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md) | §1.4 comparison inaccessible | §2.5, §3.2, §3.7, §4.2, §9.1, §9.3, §9.4 |

Every entry appears in at least four nodes except
[lee-2025-biosignal-fm-review](../collection/multimodal-biosignals/lee-2025-biosignal-fm-review/card.md),
which appears in three. That is the intended shape rather than a placement failure: it is a review
whose contents could not be read, so it has no arms to place on §1's axis beyond the null value, no
split, no window and no mechanism — which is precisely the property §9.4's first column exists to make
legible. No entry failed to fit a node.
