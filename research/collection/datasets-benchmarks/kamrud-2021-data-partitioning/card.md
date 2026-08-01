---
slug: kamrud-2021-data-partitioning
type: paper
strand: datasets-benchmarks
year: 2021
authors: [Kamrud, Borghetti, Schubert Kabban]
venue: Sensors 21(9):3225
doi: 10.3390/s21093225
url: https://doi.org/10.3390/s21093225
license: CC BY 4.0
modalities: [scalp-eeg, driver-fatigue-eeg, clinical-eeg, single-channel-eeg, resting-state-eeg]
tags: [data-partitioning, leave-one-participant-out, covariate-shift, cross-participant-models, individual-differences, non-stationarity, protocol-critique, replication, confidence-intervals, reporting-standards]
relevance: high
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

Five published cross-participant EEG models are replicated twice each, once with participants
shuffled across the split as the original papers did and once with participants held out, and the
error rate rises by between 35 percent and roughly 3,900 percent — on two of the five datasets the
participant-disjoint model is at chance.

## Summary

The paper argues that a cross-participant EEG model — one intended to work on people it has not
seen — is invalidated by any split that puts a participant's data on both sides, because individual
differences and non-stationarity make the training and test input distributions differ, which is
covariate shift, which breaks the independent-and-identically-distributed assumption the split
relies on. It tests this by replicating five published models on five public datasets under two
partitioning schemes with the data volume held constant: improper, "all participant data were
shuffled together and one-twelfth of the data were randomly selected for the test set", and proper,
"one participant was selected for the test set, and the remaining 11 participants were selected for
the training set", realized as leave-one-participant-out or leave-N-participants-out cross-validation.
The rule stated is absolute: "if participant A is used for training, then not even a single
observation from participant A should be used for validation or testing". Error rates rise on every
dataset. The paper then shows a mechanism: two transformations that artificially reduce
inter-participant variability raise proper-protocol accuracy substantially (entropy features from
0.50 to 0.80, spectral from 0.50 to 0.72 under shift-to-median) while doing nothing under the
improper protocol, "because the model has seen each participant's input distribution".

## Relevance to the review

This is the entry that quantifies the leakage penalty in the *cognitive-state* setting rather than
the clinical one, which is the setting this project is in. Two of its five datasets are
cognitive-state tasks with stimulus-driven or self-reported labels — driver fatigue and confused
students — and both show the effect: driver fatigue error rises from 0.09 to 0.466, and confused
students from 0.31 to 0.416.

The driver-fatigue result is the most transferable to STRUM. It is a 12-participant study, which is
the order of magnitude a dyadic corpus reaches, and a model that looks like 91% accuracy under a
shuffled split is 54% under leave-one-participant-out — "over five times" the error rate. If this
project reports a spoken-versus-written accuracy from a small participant pool, that is the size of
error a shuffled split would introduce.

The paper also supplies the reporting requirement this strand needs to state: de-identified
participant labels must ship with any released EEG so that a downstream user *can* partition
properly, and where a repository pre-partitions data for a competition, "proper dataset partitioning
guidelines should be followed". It proposes these as "a minimal reporting requirement for
performance evaluation of EEG cross-participant models" to the IEEE Standards Association
Neurotechnologies for Brain–Machine Interfacing group.

One qualification worth carrying: the paper explicitly permits the improper protocol when the
inference is narrower — "if a cross-participant model is only intended to perform classification on
the same population that it is training upon ... then ensuring the model is tested with unseen
individuals is not necessary" — provided the paper says so. That distinction matters if this
project's claim is about a fixed cohort rather than about new people.

## Notable details

- **Split rule compared.** Only two schemes, and the axis is the participant. Improper: random
  shuffle of observations pooled across all participants. Proper: participant-disjoint, realized as
  12-fold leave-one-participant-out (driver fatigue, PTSD), 30-fold leave-one-participant-out
  (schizophrenia), 5-fold leave-two-participants-out (confused students), and "5-fold
  Leave-N-Participants-Out CV, with N equal to 24 or 25 depending on the fold" (alcoholism). Data
  volume for training and testing is held constant across the two schemes.
- **Metric and uncertainty.** Accuracy and error rate with 95% confidence intervals on every value.
  Comparisons are made by interval dominance; no p-values, t-tests, permutation tests or Wilcoxon
  tests appear anywhere in the paper, though Table 3's caption nonetheless says the proper method
  "always reveals a significantly greater error rate".
- **Measured effect, per dataset** (improper error → proper error, with 95% CI on the proper value):
  driver fatigue, MLP, 0.09 → 0.466 (0.448, 0.472), "over five times"; confused students, Bi-LSTM,
  0.31 → 0.416 (0.372, 0.448), "over 33% greater"; alcoholism, LSTM, 0.16 → 0.31 (0.29, 0.33),
  against a chance error of 0.36; PTSD, MLP, 0.005 → 0.197 (0.1811, 0.2129), "over 39 times larger";
  schizophrenia, MLP, 0.008 → 0.50 (0.44, 0.56) and RFC 0.059 → 0.50, where "no model was able to
  perform better than random chance (50%)".
- **Originally published accuracies being replicated**, and the protocol each used: Min et al. 0.968
  under leave-one-out with a 50/50 random split; Ni et al. 0.733 under 5-fold shuffled; Farsi et al.
  0.93 under an 80/20 random split "mixing the participants data".
- **Datasets** (participants / channels / sampling rate / labels): driver fatigue 12 / 32-channel cap
  of which two are mastoid references, so 30 usable / rate not stated, only a 50 Hz notch and a
  0.15–45 Hz band-pass / normal versus fatigued in a driving simulator. Confused students 10 /
  single-channel NeuroSky MindSet / 512 Hz with features at 2 Hz / confused versus not while
  watching lecture videos. Alcoholism 122, being 45 male controls and 77 male alcoholics / 64 scalp
  plus 2 EOG / 256 Hz referenced to Cz / alcoholic versus not during visual object matching. PTSD 12,
  six healthy and six combat-related PTSD / 33 channels of which two are ground and reference, so 31
  EEG / 5000 Hz downsampled to 250 Hz / pre- versus post-treatment resting state. Schizophrenia 30
  used, 15 healthy subsampled from 25 and 15 with schizophrenia / BioSemi ActiveTwo 64 plus 2 mastoid
  / 1024 Hz, epoched at 3 s per trial, 300 trials per participant / schizophrenia versus control.
  Chance accuracy is 0.64 for alcoholism and 0.50 for the rest.
- **Mechanism.** Covariate shift, formalized with the Shimodaira loss-rescaling weight, evidenced by
  principal-component histogram weight-ratio heat maps and by t-SNE embeddings that cluster by
  participant. Non-stationarity sources listed: "continual changes in states of neuronal assemblies
  ... user attention levels, user fatigue, sensor equipment used, and scalp placement of electrodes".
  The claim about why the improper protocol looks good: "the higher measured performance is due to
  the reduced inter-participant variability between the training dataset and the validation or
  testing dataset — essentially masking the true differences".
- **Prevalence.** Citing Roy et al. 2019, "only 23 out of 108 cross-participant models utilized some
  method of proper dataset partitioning", with cross-participant studies outnumbering
  within-participant ones by over 5:1.
- The paper does not reject cross-validation: "CV merely needs to be modified so that for each fold,
  participants used in training are not also used for validation."

## Open questions / limitations

- **There is no session-level or record-level condition.** The word "session" appears only
  descriptively, never as a partitioning unit. The paper's dichotomy is proper versus improper,
  which collapses record-wise random splitting, window-overlap leakage and every other
  non-participant-disjoint scheme into one category. For a project deciding whether a session-wise
  or run-wise split is adequate, this paper does not answer the question — `brookshire-2024-data-leakage`
  splits at the segment level and is equally silent on the intermediate cases.
- **The confidence intervals are almost certainly too narrow and their construction is not stated.**
  An error rate of 0.09 is given as (0.083, 0.097), which implies pooling over observations rather
  than over participants or folds. Under participant-disjoint evaluation the sampling unit is the
  participant, and n is 10 to 122. The paper never says how the intervals were computed. Taking
  them at face value would understate the uncertainty on exactly the comparison the paper is making.
- **The 3,900 percent figure is attributed to the wrong dataset.** The abstract, discussion and
  conclusion attribute it to schizophrenia, but 0.197/0.005 ≈ 39× is the PTSD ratio, and the paper's
  own section 4.4 calls PTSD "the 2nd largest difference". The schizophrenia MLP ratio is 0.008 →
  0.50, roughly 62×. Following the standing rule, the per-dataset table values are carded above and
  the discrepancy recorded here; the range in the abstract, "between 35% and 3900%", should be
  quoted as the paper's own summary rather than as a per-dataset fact.
- Further internal inconsistencies: driver-fatigue proper error is 0.46 in the body and 0.466 in
  Table 3, while the stated interval (0.448, 0.472) is centred on 0.46; driver-fatigue proper
  accuracy is 0.540 in the body and 0.50 in Table 1; PTSD observations per participant are 200 in
  one sentence and 260 three sentences later; alcoholism channels are 64 in the body and 62 in
  Appendix A.3; confused-students participants are 10 in Table 2 but "all nine participants" in the
  replication text, against a leave-two-out design that implies 10; the confused-students effect is
  "over 33%" in the body and 35% in the abstract.
- **An undiscussed second leakage source.** For confused students the data were "segmented using a
  sliding sequence window of 15 samples in length and slides by 12 samples", i.e. overlapping
  windows, then shuffled under the improper protocol. Overlapping windows on both sides of a split
  is a distinct leak from participant overlap, and the paper's improper condition therefore mixes
  two mechanisms without separating them.
- The demonstration is on models replicated by the authors, not on the original authors' code, so
  the improper baselines are reconstructions rather than the published numbers (which are reported
  separately and are higher still).
- The two variability-reducing transformations are presented as evidence for the covariate-shift
  mechanism, not as a recommended method; shifted-Heaviside "reduced clustering but did not help",
  and the paper draws the right conclusion, that reducing inter-participant variability "does not
  necessarily imply an improvement in cross-participant model accuracy".

## Citations

Primary: `kamrud-2021-data-partitioning`

- `brookshire-2024-data-leakage` — the clinical-domain counterpart, splitting at the segment rather
  than the participant level and adding a survey of published practice.
- `varoquaux-2018-cross-validation-failure` — supplies the error-bar magnitudes this paper's narrow
  confidence intervals would need to be checked against.
- Roy et al. (2019), *J. Neural Eng.* — the systematic review this paper draws its 23-of-108
  prevalence figure from.
- Shimodaira (2000) — the covariate-shift loss reweighting the paper formalizes its argument with.
- `lin-2026-identity-trap` (strand `eeg-models`) — shows the residual problem after the fix this
  paper recommends is applied.
