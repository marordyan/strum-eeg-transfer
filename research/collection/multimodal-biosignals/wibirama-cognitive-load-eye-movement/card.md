---
slug: wibirama-cognitive-load-eye-movement
type: paper
strand: multimodal-biosignals
year: 2025
authors: [Wibirama, Alfarozi, Suhari, Fristiana, Nurlatifa, Santosa]
venue: IEEE Access 13
doi: 10.1109/ACCESS.2025.3613292
url: https://doi.org/10.1109/ACCESS.2025.3613292
license: null
modalities: [eog]
tags: [eye-movement-indices, cognitive-load, colet, lstm, bilstm, tcn, temporal-windows, artifact-versus-signal, eye-tracking, multiclass]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-available
pdf_path: null
md_path: source.md
md_quality: abstract-only
---

## TL;DR

Time-series deep models on eye-movement indices alone classify multiclass cognitive load at 0.8780
accuracy, which is the strand's most concrete reason to worry that the ocular activity EEG
pipelines routinely delete is carrying task information rather than nuisance.

## Summary

The paper argues that eye tracking is a less intrusive route to cognitive-load classification than
EEG, ECG or galvanic skin response, and that prior eye-tracking work was limited by weak multiclass
accuracy and by dependence on proprietary feature extraction that blocks reproduction with
non-commercial software. It implements three time-series deep architectures — long short-term
memory (LSTM), bidirectional LSTM (BiLSTM) and a temporal convolutional network (TCN) —
benchmarked against traditional machine-learning methods on the public COLET dataset, and
introduces novel features computed over several temporal window lengths together with
hyperparameter optimisation. BiLSTM performs best, reaching 0.8780 accuracy for multiclass
cognitive-load classification and 0.8836 for multiclass activity-task classification, both
described as significantly above the conventional machine-learning comparators. The authors frame
the contribution as making accurate cognitive-load assessment feasible on low-cost eye-tracking
devices.

## Relevance to the review

This entry sits on the fault line the brief identified, and it does so from the side that is
usually ignored. Standard EEG preprocessing treats ocular activity as an artifact to be removed by
independent component analysis, regression or artifact subspace reconstruction. This paper shows
that the same ocular activity, measured directly, supports 0.8780 four-way-or-more classification
of cognitive load. Two consequences follow for the project.

If ocular activity carries decodable state information, then ocular artifact removal is not a
neutral cleaning step — it deletes a channel that is informative about at least one cognitive
construct. The cost of that deletion has never been quantified for this project's task, and this
paper is the reason to think the cost may not be zero.

Symmetrically, if the project adds an electrooculography channel to the EEG embedding and observes
a gain, this paper is the reason the gain cannot be attributed to "peripheral physiology
complementing cortical activity" without further work. The gain may be ocular behaviour, and
ocular behaviour differs between a spoken and a written stimulus by construction: reading produces
saccade sequences and fixations that listening does not. In that case, the added channel is
decoding the stimulus modality through its motor consequences, which is a trivial result dressed
as a physiological one.

The measurement distinction matters and the paper is on the eye-tracking side of it. Its indices
are derived from eye tracking (COLET is an eye-tracking dataset), not from electrooculography.
Eye tracking gives gaze position and pupil diameter; EOG gives a potential difference that mixes
gaze angle with blink and with the corneo-retinal standing potential. The two overlap but are not
interchangeable, and a claim carried from this paper into an EOG argument should say so.

## Notable details

- **Best reported number**: BiLSTM, 0.8780 accuracy for multiclass cognitive-load classification
  and 0.8836 for multiclass activity-task classification.
- **Models compared**: LSTM, BiLSTM and TCN against unspecified "traditional machine learning
  techniques".
- **Dataset**: COLET, a public eye-tracking cognitive-load dataset. Participant count, class count,
  chance level and split protocol are all *reported but not accessible*: the abstract states the
  benchmark and the accuracies but not the design, and the full text could not be retrieved (see
  `meta.json.notes`).
- **Method contributions named in the abstract**: novel features computed over "various temporal
  windows", and hyperparameter optimisation during training.
- **Signals**: eye-movement indices derived from eye tracking. Whether pupil diameter is among the
  indices, and whether blinks are treated as signal or removed, is not recoverable from the
  abstract.
- The paper's own framing positions eye tracking as an *alternative* to EEG, ECG and GSR on
  intrusiveness grounds, not as a complement to them, so it contains no fusion arm and no
  EEG comparison of its own.
- Author group context: the same group published a related 2026 paper, "Cognitive load
  classification during online shopping using deep learning on time series eye movement indices"
  (Array, 10.1016/j.array.2025.100669), reporting an attention-based LSTM-FCN at 97.70% accuracy
  on a different dataset. That is a distinct work and is not this entry.

## Open questions / limitations

- **Performance against chance is not recorded on this card** because the number of classes and
  their balance are not in the abstract. "Multiclass" without a class count makes 0.8780
  uninterpretable as an effect size. This is a reported-but-not-accessible gap, not a gap in the
  literature.
- **The split protocol is not recorded on this card** for the same reason. Whether COLET is
  evaluated subject-wise or record-wise determines whether the result speaks to a new participant
  at all, and eye-movement indices are strongly idiosyncratic, so record-wise folds would inflate
  heavily.
- **Participant count is not recorded on this card**, again from the abstract's silence. COLET's
  own cohort size is a `datasets-benchmarks` question.
- Which indices carry the classification — the fact the brief specifically asked for — is not
  stated in the abstract. The abstract advertises "novel features" over multiple temporal windows
  but names none.
- The comparison is against "traditional machine learning" on the same dataset, not against an EEG
  model, so nothing here licenses a claim that eye movement matches or beats EEG on cognitive load.
- Because the indices come from an eye tracker, the paper says nothing about whether the same
  information survives in an EOG derivation at the sampling rate and electrode positions an EEG
  montage would provide.

## Citations

Primary: `wibirama-cognitive-load-eye-movement`

- `rotaru-2024-auditory-attention-bias` — the same ocular information seen as a confound, with an
  explicit EOG-only decoder.
- `mostert-2018-eye-movement-confounds` — gaze position alone decoding a stimulus label that was
  supposed to be neural.
- `ahmad-2020-cognitive-load-framework` — cognitive load from eye and cardiac features, with pupil
  diameter as the dominant predictor.
- `hogervorst-2014-workload-comparison` — pupil size at 75% is the only non-EEG variable besides
  respiration to exceed chance on n-back workload.
- Ktistakis et al., COLET — the eye-tracking cognitive-load dataset benchmarked here; dataset
  characterization belongs to the `datasets-benchmarks` strand.
