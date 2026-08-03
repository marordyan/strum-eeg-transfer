---
slug: bci-competition-iv-2a
type: dataset
strand: datasets-benchmarks
year: 2012
authors: [Tangermann, Müller, Aertsen, Birbaumer, Braun, Brunner, Leeb, Mehring, Miller, Müller-Putz, Nolte, Pfurtscheller, Preissl, Schalk, Schlögl, Vidaurre, Waldert, Blankertz]
venue: Frontiers in Neuroscience 6:55 (Review)
doi: 10.3389/fnins.2012.00055
url: https://doi.org/10.3389/fnins.2012.00055
license: CC BY (article); dataset free with citation requirement, no formal licence
modalities: [scalp-eeg, motor-imagery, eog, 22-channel, monopolar-mastoid-reference]
tags: [benchmark-dataset, four-class-motor-imagery, competition-protocol, held-out-test-labels, kappa, overfitting-warning, gdf, eog-artifact-removal-required, checkpoint-mapping, session-to-session-transfer]
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

Nine subjects, 288 four-class motor-imagery trials per session over two sessions on different days —
and the review that published it warns, about its own now-released test labels, that "the test data
should not be touched at all during the algorithm design process ... as this can lead to a
substantial amount of overfitting".

## Summary

Data set 2a of BCI Competition IV, "provided by C. Brunner, R. Leeb, G. R. Müller-Putz,
G. Pfurtscheller, and A. Schlögl from Graz (Austria)", is a cued four-class
motor-imagery paradigm: imagined movement of the left hand, right hand, both feet, and tongue. Nine
subjects each contributed two sessions on different days, six runs per session, 48 trials per run,
288 trials per session. Twenty-two silver/silver-chloride electrodes at 3.5 cm spacing were recorded
monopolarly with the left mastoid as reference and the right as ground, sampled at 250 Hz and
band-pass filtered 0.5–100 Hz with a 50 Hz notch, at 100 µV amplifier sensitivity. Three additional
monopolar electrooculography channels were recorded at the same rate and 1 mV sensitivity, and are
provided for artifact processing: "The EOG channels are provided for the subsequent application of
artifact processing methods (Fatourechi et al.,2007)" — the review's data-set-2a section stops
there, and its prohibition on using them to classify is stated only for data set 2b, and is itself
cut off mid-sentence in this extraction (see the correction under Open questions). Each session
opens with an
approximately five-minute electrooculography calibration block. Data are stored in the General Data
Format for biomedical signals, one file per subject per session, with labels released for the
training session only during the competition. The competition metric was the kappa coefficient, and
the winning submission, a filter-bank common spatial pattern extension with one-versus-rest naive
Bayes Parzen window classifiers, reached kappa 0.57 averaged over the nine subjects, against 0.52,
0.31, 0.30 and 0.29 for the other four submissions.

## Relevance to the review

BCI-IV-2a is in this strand because it is a benchmark the checkpoints report on, and because its
competition design is the strand's clearest historical example of an evaluation protocol built to
resist the failures category 4 documents.

The protocol is worth stating in full because nothing in the modern foundation-model suites matches
it. Test labels were withheld, so "software had to be submitted" rather than predicted
labels; "All algorithms had to be causal", and "in order to check whether the causality criterion and
the artifact processing requirements were fulfilled, all submissions had to be open source"; and the
organizers explicitly forbade non-causal exploitation of the unlabelled test block, noting they were
"aware of the problem, that this use of data is non-causal and unrealistic". Held-out labels,
submitted executables, enforced causality, and mandatory open source is a stronger anti-overfitting
regime than any of `adabrain-bench`, `omnieeg-bench`, `brain4fms` or `neuralbench` operates under.

And the review is explicit that the regime expired when the labels were released. It states three
cautions: that any post-competition improvement "should be reported with a note of caution, as it
could merely reflect random fluctuations"; that "any post-competition work on the same data has been
performed under the advantage of knowing the competition outcome, knowing the specific shortcomings
of the submitted algorithms"; and that the test labels' "use should be restricted to finally
determine the performance of a method". Every foundation-model result on BCI-IV-2a in this corpus is
post-competition work on released test labels, and the review's own authors said in advance what
that means.

The concrete number to carry: in `adabrain-bench`'s cross-subject setting, LaBraM reaches 54.98
balanced accuracy on BCI-IV-2a and CBraMod 47.71, against EEGNet at 47.83 and Conformer at 44.88 —
so the best pretrained model beats the best supervised one by 7.15 points, but the second-best
pretrained model is beaten by EEGNet. On 5,184 trials from 9 subjects, and against Varoquaux's
±10-point bound at n = 100, neither ordering is safely interpretable from a single run.

## Notable details

Fixed field set required of every `type: dataset` card in this strand:

- **Participants**: 9. "This data set comprises electroencephalographic (EEG) data from 9 subjects."
  *Correction, made during review: an earlier version of this card quoted "This data set consists of
  EEG data from 9 subjects", which is the opening sentence of the review's section 6.2, describing
  data set 2b. The count is the same; the sentence is not this data set's.*
- **Channels**: 22 EEG, "Twenty-two Ag/AgCl electrodes (with inter-electrode distances of 3.5cm)",
  plus 3 monopolar electrooculography channels; 25 channels total in the file, "the first 22 are EEG
  and the last 3 are EOG signals". The electrode layout is described as "corresponding to the
  international 10-20 system"; the 22 positions are never enumerated in text and the figure showing
  them did not survive extraction. The derivation is monopolar-referential, left mastoid reference
  and right mastoid ground — not a bipolar montage, despite the source using the word "montage" in
  its figure caption for what is an electrode layout.
- **Sampling rate**: 250 Hz for both EEG and electrooculography.
- **Total hours**: not stated. `brain4fms` records "130 min" for its preparation of BCI-2a with
  3-second windows at 250 Hz.
- **Task**: cued four-class motor imagery. Trial structure: fixation cross and acoustic warning at
  t = 0; arrow cue left, right, down or up at t = 2 s, on screen for 1.25 s; imagery sustained until
  the cross disappears at t = 6 s; then a break. "No feedback was provided." Two sessions per subject
  on different days, six runs per session, 48 trials per run (12 per class), 288 trials per session.
  Each session opens with about five minutes of electrooculography calibration in three blocks: two
  minutes eyes open on a fixation cross, one minute eyes closed, one minute of eye movements.
- **Label type**: stimulus-condition labels from the cue, encoded as GDF event types 769 to 772 for
  classes 1 to 4. Trials containing artifacts were marked by expert visual inspection (event type
  1023, plus an `h.ArtifactSelection` field). Labels are provided for the training session only in
  the original release; "the class labels ... are only provided for the training data and not for the
  testing data".
- **Licence**: none formally stated. "It can be freely assessed via
  http://www.bbci.de/competition/iv/ with the only restriction that the present article is referenced
  upon any publication of results." The Frontiers review itself is CC BY.
- **Access route**: free download from bbci.de/competition/iv/ with the citation condition above. No
  registration reported.
- **Checkpoints pretrained on or evaluated against it**:
  *Pretrained on it* — LaBraM lists BCI-IV-1 (not 2a) among its pretraining datasets per
  `adabrain-bench` Table 7; no checkpoint in this corpus reports pretraining on 2a specifically.
  *Evaluated on it* — BIOT 42.53, EEGPT 25.81 (47.89 under linear probing), LaBraM 54.98, CBraMod
  47.71 balanced accuracy under `adabrain-bench`'s cross-subject setting, against EEGNet 47.83, LDMA
  36.20, ST-Tran 31.42, Conformer 44.88; under the multi-subject setting the same four reach 50.67,
  54.01, 60.75, 59.03. `brain4fms` includes BCI-2a in its communication and affective computing
  family. `moabb` includes it as BNCI2014-001 (22 channels, 144 trials, 2 sessions, 9 subjects, 2–6 s
  epoch), though MOABB restricts to two-class.

Other details:

- **Filtering and sensitivity**: 0.5–100 Hz band-pass with a 50 Hz notch on both EEG and
  electrooculography; amplifier sensitivity 100 µV for EEG and 1 mV for electrooculography.
- **Format**: General Data Format for biomedical signals, one file per subject per session, readable
  with BioSig. Runs within a file are separated by 100 not-a-number samples.
- **Electrooculography is required to be removed**, of the submitted software: "Since three EOG
  channels were provided, the software was required to remove EOG artifacts before the subsequent
  data processing using artifact removal techniques such as high pass filtering or linear regression
  (Schlögl et al., 2007a)." *Correction, made during review: an earlier version of this card gave
  this as "it is required to remove EOG artifacts ... such as highpass filtering", which is not the
  source's wording and drops the fact that the requirement is on the competition submission.*
- **Metric**: kappa. Continuous per-sample classifier output was converted to confusion matrices from
  which "the time course of the accuracy as well as the kappa coefficient was obtained ... The chance
  level was at κ=0", and "the algorithm achieving the largest kappa value was declared the winner".
- **Competition outcome**: winner Ang, Chin, Wang, Guan, Zhang, Phua, Hamadicharef and Tee, Institute
  for Infocomm Research, Singapore, kappa 0.57, using filter-bank common spatial patterns extended to
  multiclass with one-versus-rest classifiers and a 2-second output delay. It "performed best in
  seven out of nine subjects; in two subjects, the algorithm that overall ranked second best reached
  even slightly higher kappa values". Other submissions: 0.52, 0.31, 0.30, 0.29.
- **The competition is not a systematic evaluation**, by its own account: "the competitions are by no
  means a systematic evaluation of all available algorithms".
- One subject's electrooculography calibration block is short: "due to technical problems the EOG
  block is shorter for subject A04T and contains only the eye movement condition".

## Open questions / limitations

- **The appended official description is no longer in `source.md`.** `meta.json` records that
  `source.md` holds two documents, the Frontiers review and, after a delimiter banner, the official
  BCI Competition IV data set 2a description `desc_2a.pdf` by Brunner, Leeb, Müller-Putz, Schlögl and
  Pfurtscheller. It does not: the 2026-08-01 pymupdf4llm regeneration was run over `source.pdf`
  alone and the appended document was lost with it. The present `source.md` runs from the review's
  title page to Appendix A.2, Table A4, and contains no delimiter banner, no `desc_2a`, and no "Graz
  data set A" text. Everything on this card that was attributed to "the official description" is
  therefore **not verifiable from this card's own source** until the document is re-appended, and the
  bullets below have been rewritten to say only what the review supports. Note also that the
  regeneration's stated rationale is wrong on its face: the review does carry the per-dataset
  recording parameters, in sections 5.2.1, 5.3 and Appendix A.1.
- **The review contradicts itself on the number of classes.** Section 5.1 says the data set
  "challenges the session-to-session transfer of a three class motor imagery task"; section 5.2.1 and
  Table 1 both say four. Four is correct; the three-class statement is an error in the review.
  *Correction: an earlier version of this bullet also cited the official Brunner description for
  four, which is not in this source.*
- **The review pluralizes the test sessions**: "only one session contains the class labels for all
  trials, whereas the other sessions are used to test the classifier". With exactly two sessions per
  subject the plural is wrong, and the sentence appears to be copied from the data set 2b text.
  *Correction: an earlier version of this bullet contrasted the plural against the official
  description's singular "the other session". That string does not occur in this source.*
- **Every modern result on this dataset is post-hoc on released test labels**, which the review's own
  authors flagged in advance as a source of substantial overfitting and of improvements that "could
  merely reflect random fluctuations". No suite carded here acknowledges this.
- **"Test" and "evaluation" name the same files** in different places — the review's own Table A1
  columns are headed Training and Test while its section 5.4 speaks of "evaluation data sets" — and
  the review reconciles them only in passing as "This data set (also called evaluation data)".
  *Correction: an earlier version of this bullet located the clash between the review's Table A1 and
  the official description's Table 1; the latter is not in this source.*
- **The per-subject kappa breakdown for 2a is not in the review**; only per-contributor means. The
  per-subject table exists for data set 2b, not 2a. So subject-level variability on the competition's
  own metric is not recoverable from this source.
- **The electrooculography prohibition cannot be sourced to data set 2a from this document, and is
  routinely ignored downstream.** *Correction, made during review: an earlier version of this card
  said "The official description says the electrooculography channels 'must not be used for
  classification'", and carried a frontmatter tag `eog-prohibited`, now replaced by
  `eog-artifact-removal-required`. The string "must not be
  used for classification" does not occur in `source.md`. The one occurrence of "must not be used"
  is in section 6.2.2, describing data set **2b**, and even there the extraction breaks off at "and
  must not be used for". The review's section 5.2.1, on 2a, ends the corresponding sentence at
  "(Fatourechi et al.,2007)". What this source does establish for 2a is section 5.4's requirement
  that the submitted software remove electrooculography artifacts before further processing.* The
  downstream observation stands on that weaker footing: benchmark preparations that feed all 25
  channels, or that skip
  artifact removal, are not running the protocol the dataset specifies, and none of the suites carded
  here states what it did. For this project, which will have electrooculography available, the
  distinction between a peripheral channel as signal and as an artifact reference is the same
  distinction, and it is decided per dataset rather than in general.
- **The total trial count of 5,184 that appears in `adabrain-bench` is arithmetic** (9 × 2 × 288),
  not a figure stated by either source.
- Nine subjects is far below the roughly 40 training subjects at which `adabrain-bench` reports
  cross-subject performance plateauing, so cross-subject numbers on this dataset are produced in the
  steep part of that curve.

## Citations

Primary: `bci-competition-iv-2a`

- Brunner C, Leeb R, Müller-Putz GR, Schlögl A, Pfurtscheller G, "BCI Competition 2008 – Graz data
  set A" — the official dataset description, retrieved from bbci.de. It was appended to `source.md`
  when this card was written but is **not in the current `source.md`**; the 2026-08-01 extraction
  regeneration dropped it. Nothing on this card is now sourced to it.
- `adabrain-bench` — the source of the four-checkpoint balanced-accuracy comparison quoted above.
- `moabb` — includes this recording as BNCI2014-001 and argues that the field's reliance on the BCI
  Competition datasets is itself a problem.
- `varoquaux-2018-cross-validation-failure` — the error-bar argument that bears on the small margins
  reported on this dataset.
- `physionet-mi` — the other standard motor-imagery benchmark, with 109 subjects rather than 9.
