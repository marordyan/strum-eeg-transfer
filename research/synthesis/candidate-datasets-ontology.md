# Ontology of the `candidate-datasets` strand

Phase 3 synthesis, strand D. Input is the 19 entries in
`research/collection/candidate-datasets/` and nothing else; where a fact is grounded in a sibling
strand's card, that card is linked instead.

This strand asks what data the project could fine-tune on and whether the resulting labels support
a claim. This document says what the strand contains and how its pieces relate. It is not the gap
analysis: it does not rank datasets, does not recommend one, and does not say whether any absence
in the corpus is a gap. Where two cards disagree, both readings are recorded and neither is picked.
Where a fact is repeated by several cards but traces to one source, it is counted once and the
repetition is named as repetition.

Every leaf below is a card link. All 19 entries appear; the coverage table at the end says where
each one sits.

---

## Why these facets, and not the brief's five categories

`_briefs/strand-candidate-datasets.md` scopes the strand into five collection categories:
multi-person recordings, synchronized EEG and peripheral physiology, label provenance and validity,
access and feasibility, and STRUM with its comparators. The collection was run against them and
`INDEX.md` is organized by them. This ontology departs, for reasons the index itself makes visible.

Four of the five categories leak, and always in the same direction:

- **Category 2 cannot hold its own property.** Its three members are followed by a paragraph
  beginning "Also carrying EEG alongside at least one peripheral modality, carded in other
  categories", which then names five more entries. Peripheral coverage is a property every dataset
  has a value on, not a bin that some datasets fall into.
- **Category 3 cannot hold its own property either.** Its seven members are followed by "Also
  relevant", which pulls in [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md)
  — the strand's only case of three label sources agreeing on the same trials — and
  [mous-2019](../collection/candidate-datasets/mous-2019/card.md), which carries the project's exact
  manipulation. Both are filed elsewhere, and both are more consequential for label validity than
  several of the entries filed under it.
- **Category 4's actual content is not a membership list.** It is a friction ordering that spans
  every category, written in the index as a prose ladder from CC0 through to request-to-authors,
  naming seven entries drawn from four different categories.
- **Category 1's boundary excludes the strand's own target dataset.** The index records "three
  dataset entries ... where two or more people wearing EEG were recorded at the same time". But
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is 56 participants recorded as
  28 simultaneous pairs into a single time-synchronized XDF file per session, which is exactly that
  property. STRUM is absent from category 1 because it is filed under category 5. The corpus holds
  four multi-person EEG recordings, not three, and the scarcity claim has to be stated against the
  right denominator.

The deeper mismatch is that the brief's categories classify entries by *what kind of thing they
are*, which is what a collector needs. Phase 4 needs to know *what value each entry takes on a few
independent properties* — where its label came from, whether its manipulation is within or between
subject, what a checkpoint would have to do to ingest it, what peripheral channels it carries and
whether they are usable, and what it costs to get. Every dataset has a value on all five. Papers
have none of them, and instead bear on one.

The facets below are eight questions a reader can ask, plus a register:

1. **Label provenance** — where the label came from, and what one of them was demonstrated to mean
   (§1).
2. **Manipulation geometry** — within subject or between subject, and across how many sessions (§2).
3. **STRUM's factorial design** — the point where §1 and §2 cross, and the most consequential
   relation in the strand (§3).
4. **Ingestion contract** — channels, rate, derivation scheme, coordinates, format (§4).
5. **Peripheral coverage** — present or not, and signal or artifact reference (§5).
6. **Multi-person recordings** — what exists and how it is distributed (§6).
7. **Access** — friction, and the inaccessible-versus-unreported distinction (§7).
8. **The four entries that specify no recording** — what they constrain rather than supply (§8).
9. **Where the corpus disagrees with itself** — a register, not a resolution (§9).

Nodes 1, 2 and 3 are the ones that reorder the corpus relative to the index. §1 is the strand's
sharpest axis because label validity is an admissibility condition rather than a matter of degree: a
dataset whose label does not mean what it appears to cannot support the study however good the
recording is. §2 is the axis that the index has no representation for at all, and it is the axis on
which the strand's two closest analogues to the project's plan — MOUS and STRUM — fall on opposite
sides.

---

## 1. Label provenance, and what a label was demonstrated to mean

The question this node answers: for each entry, what generated the value the model would be trained
to predict, and what evidence exists that the value means what its name says. §1.1 to §1.6 sort the
entries by provenance; §1.7 to §1.9 are the validity work, which is what makes the sort matter.

### 1.1 Stimulus condition or experimental parameter, set by the experimenter

The class the project plans to use. The label is a property of the design, known exactly, balanced
by construction, and available without a rating or a scorer.

- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — task, stimulus modality,
  stimulus kind, query type, response modality and correctness, all recorded per trial. The events
  are not bare trigger codes: they are "recorded in great detail and described using an ontology
  extended from the HED 1.0 event marker specification", so the condition structure is carried in
  Hierarchical Event Descriptor tags. See §3 for what the design does with these.
- [mous-2019](../collection/candidate-datasets/mous-2019/card.md) — two crossed factors, sentence
  versus word list within subject and auditory versus visual presentation between subject, plus
  probe-question responses. The card records a specific gap: the behavioural responses are "not
  represented as such in the `events.tsv` files" and have to be recovered from the original
  Presentation logs in `sourcedata`, so the only per-trial measure of whether a participant
  comprehended anything is not exposed at the level the BIDS release advertises.
- [kothe-2023-nback-nirs](../collection/candidate-datasets/kothe-2023-nback-nirs/card.md) — the
  purest instance: the class *is* the value of *n* the experimenter set, at 0, 1 or 2, "balanced and
  pseudo-randomized across blocks, sets, and participants", with the 0-back case handled by
  reserving a target letter so the motor response rate stays comparable. No validation of any kind
  is reported against it — no subjective scale, no behavioural analysis — so its construct validity
  rests entirely on the n-back paradigm's standing.
- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — the stimulation
  condition per trial, nine types crossing three cortical targets with three waveforms, alongside
  two other label classes (§1.4, §1.2).
- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) — task
  identity and difficulty level, set by the experimenter, and the card quotes the design's own
  framing: "as the ground truth about the task difficulty is known by the experimenter, the results
  of the classification can then be evaluated in terms of their accuracy". This entry also appears
  in §1.6, which is what distinguishes it.

The relation that makes this node non-trivial:
[kothe-2023-nback-nirs](../collection/candidate-datasets/kothe-2023-nback-nirs/card.md) has the same
*formal* label structure as the project's plan — a stimulus-regime parameter rather than a measured
mental state — and its card states precisely why the two are not equally supportable. The n-back
manipulation equates everything but working-memory load: "the letters, timing, target rate, motor
response and screen appearance are identical across *n*". Spoken versus written equates nothing:
"changing presentation modality changes the sensory channel, the stimulus timing profile ... and the
sensory cortex responding, all at once". So an experimenter-set label supports a cognitive reading
in proportion to what the design holds constant, not in virtue of being experimenter-set. That is
the axis, and it is the reason §1.1 is a starting point rather than a verdict.

### 1.2 Self-report

- [deap-2012](../collection/candidate-datasets/deap-2012/card.md) — arousal, valence, like/dislike,
  dominance and familiarity on nine-point scales, thresholded at the midpoint into binary classes
  for the baseline experiments ("the threshold was simply placed in the middle"). The authors state
  that "the participants' ratings during the experiment are used as the ground truth". DEAP has no
  stimulus-condition label at all, so it cannot serve as a label-validity case; its value to the
  strand is §5.
- [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) — self-assessed valence,
  arousal, dominance, liking, familiarity and basic-emotion selection, plus Big Five personality and
  PANAS mood. Every label except the individual-versus-group social context is a rating. Its card
  names the consequence in the form specific to ratings: "the risk is not that the label leaks into
  the signal, it is that the label may not correspond to any state the signal contains" — which is
  the inverse of the circularity risk in §1.9.
- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) —
  Karolinska Sleepiness Scale and Rating Scale Mental Effort, administered systematically after every
  task, as one of three concurrent sources (§1.6).
- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — pre- and
  post-session wellness questionnaires, the weakest of its three label sources.

### 1.3 Expert rating

- [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) — the strand's only instance.
  Sleep stage per 30-second epoch, "manually scored by well-trained technicians ... according to the
  1968 Rechtschaffen and Kales manual", with the scoring technician identifiable from the eighth
  letter of each hypnogram filename. That last property is unusual and load-bearing: it makes
  inter-rater agreement addressable in principle, though the landing page reports none. See §1.9 for
  the circularity that comes with it.

### 1.4 Behavioural performance, measured continuously

- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — the compensatory
  tracking task's deviation score, which "allowed for the assessment of vigilance/attention on the
  scale of milliseconds, facilitating its acquisition concurrency with dynamic EEG, ECG, and EOG".
  This is the only continuous behavioural label in the strand, and its card names the trade exactly:
  it "places it outside the circularity trap this strand worries about, at the cost of not being a
  discrete classification target".
- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) —
  per-task accuracy and reaction time, as the third of its three sources (§1.6).

### 1.5 Human annotation of observed behaviour

A class that exists only because two entries record naturalistic tasks with no stimulus timeline to
label against.

- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) — continuous event
  annotation from video by the research team, "instant-by-instant into a spreadsheet giving the
  sample-level start and end of each observed activity", so the release ships a behavioural timeline
  rather than a stimulus log. Its card is explicit that this "places this dataset in a different
  label-provenance class from every screen-paradigm dataset in this strand".
- [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) — session type
  (rehearsal versus performance) from the protocol, plus video-derived tagging of choreography
  sections. The release is explicitly raw, with no epoch-level label files described, so what exists
  at trial resolution is not established by the paper.

### 1.6 More than one source on the same trials

The strand's only case of label-source agreement being addressed rather than assumed, and the
property the brief asks for under "agreement between label sources where more than one exists".

- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) — the
  paper validates its experimenter-set difficulty labels "on a subjective, behavioral and
  physiological level": subjective through the Karolinska and Rating Scale Mental Effort scales,
  behavioural through per-task accuracy and reaction time, physiological through cardiac and
  cerebral activity. Four channels of evidence on one set of recordings.
- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — three provenances
  in one dataset by construction (behavioural tracking, experimental stimulation condition,
  self-reported wellness), though the card does not report the authors testing agreement *between*
  them the way Hinss does.
- [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) — self-report and external
  annotation of the same twenty-second segments, which is two sources but both of them ratings. The
  authors do run one between-source comparison, though not the one that would validate a label: they
  report that the distribution of personality and PANAS ratings does not differ significantly
  between the individual and group settings (p > 0.1 on every dimension by two-sample t-test).

### 1.7 The one demonstrated failure, and what it was demonstrated with

- [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  is the entry the rest of this node exists to position. Eight concepts — four animals and four
  tools, all monosyllabic Dutch, matched for lemma frequency — were presented in three stimulus
  modalities: spoken words, line drawings and written words, eighty repetitions each, to twenty
  analysed participants on 60 equidistant scalp electrodes at 500 Hz.

  Single-trial decoding of semantic category succeeded within modality. **The group result for
  pictures is a mean of 0.79 (SD 0.07), significant in all twenty subjects.** The figure 0.89 that
  appears in the strand's `INDEX.md` line for this entry is the best single subject, and the card
  states directly that "quoting it alone overstates the paper, and the mean is the number synthesis
  should carry". This document carries 0.79. Written words were significant in only two of twenty
  subjects.

  What makes the entry decisive is not the accuracy but the generalization test. Trained on some
  exemplars and tested on a concept it had never seen, the classifier "failed to predict the semantic
  category of a previously unseen item", and the authors' own conclusion is that it "could not
  distinguish the semantic classes, but only the exemplars, possibly through the use of perceptual
  differences between the exemplars". Above-chance accuracy on the intended label did not license the
  intended interpretation, and only a held-out generalization test revealed it.

  Three further facts on the card bear directly on the project's contrast, and they are about the
  spoken-versus-written difference specifically rather than about the category label:

  - The discriminating features are early and sensory, and the card locates them. Pictures: P1 at
    ~110 ms and a visual N1 at ~160 ms, largest at infero-temporal and occipital sites. Spoken words:
    a centro-posterior N1 peaking at 130 ms. Written words: a posterior P1-N1 with a left-lateralised
    N1. An early posterior visual complex against an early centro-posterior auditory complex is
    exactly what a spoken-versus-written classifier would separate.
  - The cross-modal transfer analysis did not recover modality-independent structure (pictures 0.83,
    spoken 0.66, written 0.61), and the authors attribute this to picture trials biasing feature
    selection toward occipital sites rather than to amodal semantics being absent.
  - The authors name a structural asymmetry that any spoken-versus-written epoching scheme inherits:
    "Auditory stimuli are spread out in time, whereas the others are presented instantaneously."

  One boundary the card sets and this document preserves: the paper does *not* run a
  spoken-versus-written classifier. Its decoding target is semantic category within each modality. It
  supplies the diagnostic procedure and the ERP evidence, not a number for the contrast the project
  plans.

### 1.8 The four tests that bound what a stimulus-condition label can mean

Four entries, each supplying a different check, and they compose into a sequence rather than
repeating one point. Two of the four are abstract-only cards (§7.2) and nothing quantitative should
be taken from them.

- **Is there anything cognitive left to decode in this contrast?**
  [deniz-2019-modality-invariant-semantics](../collection/candidate-datasets/deniz-2019-modality-invariant-semantics/card.md)
  — hours of the *same* narratives listened to and read, with voxelwise encoding models fitted per
  voxel per participant. Semantic tuning is "highly correlated in most semantically selective regions
  of cortex", models fitted in one modality "accurately predict voxel responses in the other", and
  the significance statement is that the representations "are almost identical". The card draws the
  consequence and marks it as the card's inference rather than the paper's claim: if the semantic
  representations are near-identical, a classifier separating spoken from written epochs is by
  elimination separating something other than semantics. That does not void the label; it fixes its
  meaning as *the sensory channel through which language arrived*.
- **What is the test that isolates what survives?**
  [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
  — train the decoder in one presentation modality and test it in another. Across four modalities
  (spoken names, written names, photographs, natural sounds) this localised clusters in left inferior
  temporal and frontal cortex, and the same voxels discriminated categories in a free-recall session
  with no stimulus present at all. The direction the card draws is the one that matters here: if the
  category signal is what generalises across modality, then whatever distinguishes a spoken trial
  from a written trial is by construction the part that does *not* generalise. A
  spoken-versus-written classifier is trained on exactly the component this literature separates out
  and discards.
- **Does a successful decode establish a representation at all?**
  [ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md)
  — the "decoder's dictum" stated and rejected. Information can be latent in a signal without being
  in "a format that can be easily read-out by a downstream neuron in order to guide action", so "a
  sufficiently powerful nonlinear classifier could decode almost any arbitrary feature". The
  constructive half is a criterion rather than a prohibition: tie decodability to behavioural
  read-out, as in the illustrative study where retinotopic and lateral occipital cortex both carried
  decodable shape-category information but only the latter showed stronger patterns on correct than
  on incorrect trials.
- **If the confound is identified, can it be removed?**
  [snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
  — not by the two obvious methods. Post hoc counterbalancing biases accuracy *upward*, because "the
  subsampling process ... tends to remove samples that are hard to classify or would be wrongly
  classified". Confound regression biases it *downward*, "even resulting in significant below chance
  performance in some realistic scenarios". Only confound regression performed inside every
  cross-validation fold is unbiased. The card adds a diagnostic reading: significant below-chance
  accuracy should be read as a symptom of the analysis before it is read as a finding.

Two limits that the four cards state about themselves, and that must travel with them. Three of the
four are fMRI or structural MRI, and
[ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md)
declares its scope as fMRI and vision. And the same card records a tension it does not resolve: its
recommendation to restrict classifier flexibility "sits in direct tension with the entire premise of
transfer from a large pretrained model". The paper predates that literature, so the tension is
recorded rather than adjudicated.

Two sibling-strand entries extend this node in the specific direction the project's contrast runs,
and they are not repetitions of the four above because they measure rather than argue:

- [multimodal-biosignals/mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  — a planned working-memory decoding study published as a cautionary result because the memorised
  item was decodable from two numbers, horizontal and vertical gaze position. Two properties transfer
  exactly: the data had already been cleaned of "regular artifacts such as heartbeat, blinks and eye
  movements" and the authors state that removal "was imperfect", so an ICA pass does not close the
  question; and the confound is a stimulus-locked micro-behaviour rather than gross artifact. That
  card draws the consequence for this project explicitly — reading requires saccades and listening
  does not, so a spoken-versus-written contrast produces systematic differential ocular behaviour by
  construction.
- [multimodal-biosignals/rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  — four EOG channels alone decode spatial auditory attention above chance when gaze and attention
  are congruent, and a classifier asked to predict *which trial* a segment came from reaches median
  99.6 to 100 percent. The trial-fingerprint result generalises past ocular artifact entirely: where a
  design gives one label per trial, the label and the trial identity are the same variable, which any
  stimulus-blocked design inherits. The card also records the authors' scaling claim, that non-linear
  deep models "are even more vulnerable to such biases".

The `eeg-models` strand supplies the same shape of failure at the level of the representation rather
than the label:
[eeg-models/lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) finds
frozen foundation-model embeddings dominated by subject identity in 12 of 12 model-by-dataset pairs.
That is a different claim from anything in this strand — it is about the embedding, not the label —
but it is the reason §2 is a separate facet rather than a remark.

### 1.9 Circularity, where the label derives from the signal the model sees

The brief asks for this explicitly. The strand contains one clean instance and one non-instance
worth naming so they are not conflated.

- [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) — the hypnograms were scored
  "based on Fpz-Cz/Pz-Oz EEGs instead of C4-A1/C3-A2 EEGs", which is to say from the same two
  channels a model would be given. The card names it as "a mild circularity worth naming, though it
  is intrinsic to all expert-scored sleep data", and draws the consequence: a high sleep-staging
  score is not evidence that a model learned anything beyond the scoring rules. The scoring is also
  non-conformant to the manual it cites — a point recorded on the sibling card
  ([datasets-benchmarks/sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md))
  rather than this one, so a model trained on these labels is learning a variant scoring.
- The non-instance:
  [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md)'s card explains why a
  self-report label is not circular in this sense. The label does not derive from the signal, so
  nothing leaks; the risk runs the other way, that the label corresponds to no state the signal
  contains. Both are label-validity failures and they are opposite failures. Filing them under one
  heading would lose the distinction.

Nothing in the strand records a stimulus-condition label deriving from the recorded signal, which is
the form of circularity the brief names first.

---

## 2. Manipulation geometry: within subject, between subject, and how many sessions

The question this node answers: for each dataset, is the contrast the project cares about
manipulated inside a participant or across two disjoint groups of them, and how many sittings does
each participant contribute. The index has no representation for this axis at all, and it is the
axis on which the strand's two closest analogues to the project's plan fall on opposite sides.

The principle, stated once so it is not restated per entry: a factor manipulated between subjects is
perfectly collinear with subject identity by construction. A classifier separating the two levels is
separating two groups of people, and no amount of accuracy distinguishes the two explanations,
because within that design there is no condition in which they come apart. A factor manipulated
within subject is not free of subject identity — the subject is still a nuisance variable — but the
label and the identity are no longer the same variable, so the ordinary machinery of
subject-disjoint splits applies.

### 2.1 Between subjects: the manipulation and the subject are the same variable

- [mous-2019](../collection/candidate-datasets/mous-2019/card.md) — the only entry in this class,
  and the strand's specification of what the project's exact contrast looks like at scale. 204 native
  Dutch speakers, 102 reading the sentences and 102 listening to the same ones. The card states the
  consequence flatly: "in MOUS there is no such thing as a within-subject spoken-versus-written
  classifier, and any across-subject classifier trained on the contrast is separating two disjoint
  groups of people, so its accuracy is confounded with subject identity at the maximum possible
  strength".

  Two elements of MOUS are transferable regardless, and they are the reason it belongs in the corpus
  rather than being excluded:

  - **The stimulus-duration control.** Each word's visual presentation duration is computed from the
    duration of the audio recording of the spoken version of the same sentence, by the formula
    `(nletters/sumnletters) * (audiodur + 2000 - 150*nwords)` with a 300 ms floor. Without such a
    control, a spoken-versus-written contrast is also a contrast in trial length, and epoch length is
    trivially decodable. This is the sentence-level form of the timing asymmetry that
    [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
    names at the word level, and MOUS shows what controlling it costs.
  - **A residual that the control does not remove.** The card records a trigger-to-auditory-onset
    delay "on the order of slightly more than 60 milliseconds", which applies only to the auditory
    half of the sample. That is a systematic timing difference between the two modality groups *on
    top of* the group difference itself, larger than most early evoked components. It is correctable
    from the recorded audio traces, but only for the subjects who have them.

### 2.2 Within subject

Every other dataset in the strand manipulates its conditions within participant, which makes §2.1 a
node of one. The distinctions that matter inside this class are about what varies alongside the
condition.

- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — the side tasks run
  concurrently for every participant as a 2×2 (§3). This is the property MOUS lacks.
- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) — four
  tasks and three N-back difficulty levels, all within participant, each task presented twice per
  session in pseudorandom order.
- [kothe-2023-nback-nirs](../collection/candidate-datasets/kothe-2023-nback-nirs/card.md) — *n*
  balanced and pseudo-randomised across blocks, sets and participants.
- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — a
  repeated-measures crossover: nine stimulation conditions within participant, with four participants
  repeating an entire experiment for within-participant reliability.
- [deap-2012](../collection/candidate-datasets/deap-2012/card.md) and
  [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) — all stimuli seen by all
  participants. AMIGOS is a partial exception: its individual-versus-group social context is between
  subjects (17 individual against 20 in groups), and it is the only stimulus-independent label the
  dataset has.
- [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  and [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
  — all stimulus modalities presented to all participants, which is what makes their cross-modal
  train-test designs possible in the first place. The design property in §2.2 is the precondition for
  the diagnostic in §1.8.
- [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) — the sleep-telemetry subset is a
  within-participant temazepam-versus-placebo crossover; the sleep-cassette subset has no
  manipulation at all.

### 2.3 Sessions per participant, and what multiple sittings buy

- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) — three
  sessions spaced one week apart, which the card calls the dataset's headline feature. Each session
  opens with a fresh 3D head-and-cap scan, so between-session electrode displacement is *measured*
  rather than assumed away (§4.4).
- [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) — ten sessions over four
  months, seven rehearsals and three performances. The longest span in the strand, over two
  participants.
- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) — six rehearsals and
  three performances within a single week, which the card characterises as "longitudinal within a
  single week rather than cross-sectional".
- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — 62 sessions over
  20 participants, three or two per participant depending on experiment.
- [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) — two nights per subject in both
  subsets, with three cassette nights lost to equipment failure.
- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — one session of about 3.5
  hours, deliberately long, "to maximize the amount of data collected per subject, and also to induce
  a moderate degree of fatigue". Single-session, so no cross-session generalisation is testable in
  it; but fatigue is an intended within-session covariate, which no other entry in the strand
  designs for.

### 2.4 Where the subject pool is too small for the distinction to be actionable

Recorded because these entries' cards say so themselves, and because a within-subject design over
two people does not deliver what a within-subject design normally delivers.

- [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) — two participants total.
  "Any model fitted to this dataset is fitted to two people, so nothing subject-general can be
  established from it, and a subject-wise split has exactly two folds."
- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) — ten participants, of
  whom three were recorded for about seven minutes each, and the third instrumented person differs by
  session so the simultaneously recorded triad is not stable across sessions.
- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) — 29
  participants across three sessions is, on its own card's assessment, "still a small subject pool for
  anything claiming subject-general transfer".

### 2.5 Split hazards the cards record, which are properties of the data rather than of a protocol

These belong here because they are consequences of the manipulation geometry, and because each is an
identifier-level trap that a naive pipeline would fall into silently.

- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — participant
  identifiers are not stable across repeats; one participant appears as 22, 23 and 24 across three
  runs. "A subject-wise split built naively on the identifier column would leak."
- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) — Cz is
  missing for participants 1 through 9, so nine of 29 participants have a different channel set. "A
  pipeline that assumes a fixed channel order across subjects will break or, worse, silently
  misalign."
- [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) — two nights per subject across
  197 files, and the sibling card
  ([datasets-benchmarks/sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md))
  adds that the file split "does not map cleanly onto a subject count", so a recording-level split is
  not a subject-level split here.
- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) — P01 on all three
  dyads has 31 channels rather than 32, electrode CP6 having been removed.

The measurement of what these hazards cost lives in the sibling strands rather than here, and is
linked rather than restated:
[datasets-benchmarks/kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
replicates five published cross-participant EEG models under shuffled and participant-held-out splits
and reports error-rate increases between 35 percent and roughly 3,900 percent, with two of five at
chance under the proper split;
[eeg-models/brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)
measures a 46.8-point inflation from segment-based to subject-based holdout on one clinical task. And
[datasets-benchmarks/combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
bears on how the per-subject figures in
[simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
should be read at all: classifying pure Gaussian noise at small sample size reaches "70% or higher in
two-class decoding", so a theoretical chance level is not the threshold. Simanova's twenty
participants at eighty repetitions per item is squarely in that regime.

---

## 3. STRUM's factorial design, and where §1 meets §2

This is the most consequential relation in the strand, and it is the one thing the full paper
contributed that changes the project's position rather than merely specifying it.

[strum-2018](../collection/candidate-datasets/strum-2018/card.md)'s side tasks are not a list. They
are an explicit factorial, quoted from section III: "broken down by stimulus modality
(auditory/visual) and stimulus kind (verbal/non-verbal), yielding a matrix of four tasks, plus one
additional task with natural visual stimuli". Each task presents a stimulus sequence, a fraction of
which is followed by a query about the preceding, no-longer-displayed stimulus; queries match their
task's modality and kind. Responses alternate between touchscreen and voice, self-paced, with a
penalty for more than 15 successive uses of one modality.

**The relation.** The project's planned label, spoken versus written, is in STRUM's own terms
auditory-verbal versus visual-verbal. That is one cell pair of a 2×2 whose other cell pair is
auditory-non-verbal versus visual-non-verbal. The two axes of this ontology meet exactly here:

- On the §1 axis, the label is a stimulus-condition label, and §1.7 and §1.8 establish that such a
  label can be decoded for a reason other than the one it names — in
  [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)'s
  case, exemplar-level perceptual differences rather than semantic class; in the
  spoken-versus-written case, the auditory-versus-visual sensory response that
  [deniz-2019-modality-invariant-semantics](../collection/candidate-datasets/deniz-2019-modality-invariant-semantics/card.md)
  leaves as the only thing available once semantics is ruled out.
- On the §2 axis, the manipulation is within subject, which
  [mous-2019](../collection/candidate-datasets/mous-2019/card.md) is not.
- The 2×2 is what turns the first of these from a caveat into an experiment. Because the same
  factorial contains non-verbal tasks in *both* modalities, the sensory factor is instantiated
  independently of the verbal one. A classifier trained on the verbal cells can be tested on the
  non-verbal ones. If it transfers, it is reading stimulus modality rather than language, which is
  precisely the diagnosis
  [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  arrived at by a different route and
  [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
  proposes as the general procedure. The card puts it plainly: the confound "is not merely a risk to
  acknowledge, it is a factor the dataset lets you subtract".

**What the relation does not settle.** Four limits, each on the card:

- The design supplies the control; it does not supply the result. Nothing in the corpus reports the
  test having been run, on STRUM or on anything else. STRUM's citation count is 2 and neither citing
  work trains or evaluates a model on it (§7.1).
- The factorial crosses sensory channel with symbolic status, which is the same crossing that
  [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
  identifies as the improvement its four-modality design makes over the three-modality EEG study —
  spoken names, written names, photographs and natural sounds "crosses sensory channel (auditory,
  visual) with symbolic status (linguistic, non-linguistic) rather than confounding them". STRUM's
  2×2 has the same structure. What the corpus does not record is whether STRUM's cells are matched on
  stimulus duration the way
  [mous-2019](../collection/candidate-datasets/mous-2019/card.md)'s are; the card does not report a
  duration-matching formula, and the auditory-spread-in-time asymmetry named in §1.7 is therefore
  unaddressed on the record.
- The ocular confound named in
  [multimodal-biosignals/mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  is not subtracted by the 2×2, because reading and listening differ in gaze behaviour whether the
  material is verbal or not. STRUM does carry 2-channel EOG on the same amplifier (§5.1), which makes
  the confound measurable rather than merely present.
- The design is one cell of a 2×2 *plus* a fifth task with natural visual stimuli, which has no
  auditory counterpart. The factorial is complete over the four cells and the fifth task sits outside
  it.

**One further consequence of the same design.** Response modality alternates between touchscreen and
voice and is recorded per trial, and correctness is recorded per trial. That makes the behavioural
read-out criterion of
[ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md)
available in STRUM — the criterion that card flags as possibly unavailable "precisely where it is
most needed", since "a passive stimulus condition with no task response ... has no correct/incorrect
split to condition on". STRUM has one. That is a relation between two cards that neither states.

---

## 4. Ingestion contract: channels, rate, derivation, coordinates, format

The question this node answers: what would a checkpoint have to be given, and what would it have to
approximate. The `eeg-models` strand established that spatial identity is the hard admissibility
condition and that a derivation is not a position; this node sorts the strand's datasets on those
terms. Only the nine `type: dataset` entries have values here.

### 4.1 Derivation scheme

Five classes, and they are not equivalent for a coordinate-driven model.

**Referential to a named reference** — each channel is a potential at one named site, so a
coordinate can be assigned directly and no approximation is required:

- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) —
  reference at Fpz, ground unstated, distributed raw. The card notes the authors' own preprocessing
  example applies full-rank average referencing before ICA, but that is a suggestion, not the
  distributed form.
- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — online reference
  CPz, ground AFz, both named explicitly, which its card flags as "unusual among the datasets in this
  strand".
- [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) — referential to linked
  earlobes.
- [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  — right-mastoid reference converted offline to linked mastoids. Not a candidate fine-tuning corpus,
  but its acquisition is fully specified and is the only label-validity paper in the strand for which
  that is true.

**Average reference** — a potential relative to the mean of the montage, which is not a per-electrode
potential and is not what a checkpoint pretrained on referential data saw:

- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) — the released EEGLAB
  structure carries `EEG.ref` as "Channel referencing to the common average", and preprocessing
  applies "robust re-referencing though the PREP pipeline". Its card names the consequence: "An
  average reference is not a per-electrode potential, which matters for any checkpoint that assumes
  one."

**Bipolar** — a difference between two sites, with no single position:

- [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) — Fpz-Cz and Pz-Oz, and its card
  calls this "the distinguishing feature of the dataset for this strand". It is the exact case
  [eeg-models/reve-2025](../collection/eeg-models/reve-2025/card.md) handles by substituting the
  midpoint of the pair, an approximation the `eeg-models` ontology records as untested by any
  ablation. Sleep-EDF is the cheapest open substrate on which it could be probed.
- [mous-2019](../collection/candidate-datasets/mous-2019/card.md) — bipolar only on its three
  peripheral pairs (EEG057, EEG058, EEG059); the 275 MEG channels are axial gradiometers and the
  question does not arise.

**Referential but with the reference unstated** — the class that matters most, because it looks like
the first class and is not:

- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — the paper says only "a
  206-channel EEG montage (24-bit BioSemi amplifier)", using "montage" in the loose cap-layout sense.
  The card reasons from the hardware rather than from the text: BioSemi acquires referentially against
  the CMS/DRL driven-feedback pair and does not record bipolar derivations, so STRUM is not bipolar as
  recorded and the midpoint approximation does not apply. But "the paper does not name the reference
  used for any released version of the data, so what re-referencing has already been applied is
  unknown". The derivation *class* is constrained; the derivation is not stated.
- [deap-2012](../collection/candidate-datasets/deap-2012/card.md) — the same situation and the same
  discipline. BioSemi ActiveTwo, "but the paper does not describe the derivation of the distributed
  data, so it is recorded as unknown rather than assumed from the hardware".

**Unknown** — neither stated nor constrained:

- [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) — the Emotiv EPOC uses a fixed
  proprietary reference pair, but the paper does not describe the derivation and the card declines to
  infer it.

That two of the eleven datasets are "constrained by hardware but unstated in text" and one is
outright unknown is a property of this corpus worth carrying forward as a class, because a reader
scanning for "referential" would otherwise merge them with the four datasets that name a reference
electrode.

### 4.2 Channel count and layout

The spread is two orders of magnitude, and the two ends are the two entries the project cares most
about.

| entry | EEG channels | layout |
|---|---|---|
| [strum-2018](../collection/candidate-datasets/strum-2018/card.md) | 206 (205 in its own section IV; see §9.2) | not stated; non-standard high-density cap |
| [mous-2019](../collection/candidate-datasets/mous-2019/card.md) | 275 MEG axial gradiometers, not EEG | CTF |
| [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) | 63 EEG + 1 ECG on TP9 | extended 10-20 |
| [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md) | 60 scalp of a 64-channel cap | equidistant |
| [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | 32 | international 10-20 |
| [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) | 32 | 10/10, with 9 stimulation electrodes interleaved |
| [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) | 28 EEG + 4 EOG of a 32-channel cap | 10-20, four electrodes moved to periocular sites |
| [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) | 28 EEG + 4 EOG | 10-20 |
| [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) | 14 | fixed consumer set, named in the paper |
| [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) | 2 bipolar derivations | Fpz-Cz, Pz-Oz |

The ingestion consequences are stated by the cards, not inferred here.
[strum-2018](../collection/candidate-datasets/strum-2018/card.md)'s card records that at 206 channels
STRUM "sits far outside every checkpoint's pretraining distribution", and that the models indexing
spatial identity by channel name — LaBraM, BIOT, CBraMod — "cannot ingest a 206-channel set without
channel selection or interpolation down to their expected montage", while the coordinate-driven
models can take an arbitrary layout given coordinates. That maps onto §1.1 and §1.2 of the
[`eeg-models` ontology](./eeg-models-ontology.md) directly. At the other end,
[amigos-2021](../collection/candidate-datasets/amigos-2021/card.md)'s card records that 14 channels
"would leave most of the model's spatial capacity unused", and
[sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)'s that on two channels "most of a
spatial encoder's capacity is unused" and "whether transfer to such a sparse layout is meaningful is
untested by any paper read here".

One special case that is neither a layout nor a count problem:
[hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) buys its
single ECG channel by sacrificing electrode TP9. The card names it as "a real trade: the electrode is
missing from the scalp layout, which matters for any model that expects a symmetric montage or that
interpolates across the temporal chain". It is the only entry in the strand where the peripheral
inventory and the EEG layout are in direct competition.

### 4.3 Sampling rate

Every rate in the strand requires resampling for at least one checkpoint in `eeg-models`, and the
spread is 20-fold.

- 2000 Hz — [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md), amplifier
  bandwidth 0–520 Hz.
- 1200 Hz — [mous-2019](../collection/candidate-datasets/mous-2019/card.md), MEG and all peripheral
  channels together, 300 Hz analogue anti-aliasing cutoff, audio channel synchronous at the same rate.
- 1000 Hz — [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md), EEG and EOG.
- 512 Hz — [strum-2018](../collection/candidate-datasets/strum-2018/card.md) (acquired at 2048 Hz and
  resampled) and [deap-2012](../collection/candidate-datasets/deap-2012/card.md) (the widely
  distributed preprocessed version is downsampled to 128 Hz).
- 500 Hz — [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md),
  [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) (24-bit,
  0.05 µV resolution, no acquisition filtering),
  [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  (0.2–200 Hz).
- 128 Hz — [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md), 14-bit.
- 100 Hz — [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md).

Two structural points rather than a list. First, the peripheral channels are frequently sampled at
*different* rates from the EEG, and that is a per-dataset fact rather than a convention: on the same
amplifier and therefore at the same rate for
[strum-2018](../collection/candidate-datasets/strum-2018/card.md),
[tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md),
[hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) and
[mous-2019](../collection/candidate-datasets/mous-2019/card.md); on separate devices at 64, 32, 4 and
1 Hz for [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md); at 256 Hz
against 128 Hz EEG for [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md); at 1 Hz
against 100 Hz EEG for [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md)'s
respiration, temperature and EMG envelope. Any fusion architecture has to resolve that ratio, and it
ranges from 1:1 to 100:1 within this corpus.

Second, the memory constraint recorded in the project's `CLAUDE.md` is a function of this table
crossed with §4.2, and three cards say so independently.
[strum-2018](../collection/candidate-datasets/strum-2018/card.md): 269 channels per subject at 512 Hz
with two subjects in one XDF file is "on the order of gigabytes per session hour", so kernel
exhaustion "is the expected behaviour of this format, not a configuration problem".
[tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md): 32 channels at 2 kHz
over continuous 70-minute sessions, where the constraint "applies here with force".
[sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md): whole-night recordings of about 20
hours each.

### 4.4 Electrode coordinates: measured, template, or absent

This is the sub-axis the `eeg-models` strand's coordinate-driven mechanisms depend on, and the strand
splits three ways.

- **Measured per participant per session** —
  [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) alone. A
  Structure 3D scanning camera and the `get_chanlocs` pipeline, run at the start of each of three
  sessions. Its card names why this is more than a nicety: "this is the difference between real
  coordinates and inferred ones — and it is measured three times per participant, so between-session
  electrode displacement is quantifiable rather than a hidden nuisance".
- **Template positions in the released structure** —
  [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md), whose `EEG.chanlocs`
  carries "the spatial location of each channel N according to the international 10-20 system"; and
  the several datasets whose channels are named 10-20 or 10/10 sites from which a template coordinate
  is derivable ([tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md),
  [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md),
  [deap-2012](../collection/candidate-datasets/deap-2012/card.md),
  [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md)).
- **Absent, and consequentially so** —
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md). The paper "does not say whether
  individual electrode coordinates were digitised per subject or whether a template layout is
  assumed", and the card names why this bites harder here than elsewhere: "for a 206-channel cap this
  matters more than usual, since a coordinate-driven model needs a position per channel and a template
  for a non-standard high-density cap may not exist". This is the one place where §4.2 and §4.4
  compound: the checkpoints that could ingest 206 channels are exactly the ones that need a coordinate
  per channel, and that is exactly what is unrecorded.

[eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md) is the entry that makes this
axis machine-checkable rather than a matter of reading methods sections, and also the entry that
records why compliance does not settle it (§8.1).

### 4.5 Format, and what reads it

- **BIDS** — [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) (OpenNeuro
  `ds003670`), [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md)
  (Zenodo, raw, with a notebook of task order and interruptions and an explicit Lab Streaming Layer
  trigger list), [mous-2019](../collection/candidate-datasets/mous-2019/card.md) (Donders, MEG in CTF
  format, MRI defaced, conversion scripts in a `code` folder).
- **EDF and EDF+** — [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md), polysomnograms
  in EDF and hypnograms in EDF+, readable by EDFbrowser, Polyman, LightWAVE and WFDB, with the caveat
  recorded on the card that WFDB "does not decode annotations in EDF+ files" — which is where the
  labels live.
- **EEGLAB `.set`** — [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md), and
  [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) recommends MATLAB and EEGLAB
  for its raw release.
- **XDF** — [strum-2018](../collection/candidate-datasets/strum-2018/card.md), one time-synchronized
  file per two-participant session, written by the Lab Streaming Layer toolchain that
  [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) documents. This is the only container
  in the strand that holds two participants' data in one file.
- **Bespoke or unstated** — [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md)
  also distributes raw `.cnt` and derived `.mat`; [deap-2012](../collection/candidate-datasets/deap-2012/card.md)
  and [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) have no format stated on
  their cards, in both cases because the distribution host was unreachable at retrieval (§7.3).

---

## 5. Peripheral coverage, and signal versus artifact reference

The brief asks for this distinction specifically because it "decides whether a dataset can support
the project's third comparison at all". The strand sorts three ways, and the sort is by *what the
source's own analysis did with the channel*, not by what a channel could in principle be used for.

**The corpus holds eight datasets carrying EEG alongside at least one peripheral modality.** The
strand's `INDEX.md` states six. The discrepancy has two components and both are recorded here rather
than resolved: STRUM is not counted, because it is filed under category 5 rather than category 2; and
the index's own enumeration in that paragraph lists seven EEG datasets while the sentence following it
says six. Counting the nine `type: dataset` cards, the eight are
[strum-2018](../collection/candidate-datasets/strum-2018/card.md),
[deap-2012](../collection/candidate-datasets/deap-2012/card.md),
[tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md),
[sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md),
[boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md),
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md),
[amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) and
[hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md), plus
[mous-2019](../collection/candidate-datasets/mous-2019/card.md) carrying the same channels alongside
MEG rather than EEG.

### 5.1 Used as signal in the source's own analysis

The strongest class, because the source itself demonstrates the channel carries usable information.

- [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) — bipolar lead-I ECG
  (electrodes below each clavicle, ground at the left hip) and bipolar horizontal EOG (outer canthi),
  on the same amplifier as the EEG. Its card calls it "the cleanest specimen in the strand" and gives
  the reason: the authors' stated purpose includes testing "how variations in brain state (e.g.
  baseline vigilance) or physiology impact sensitivity to tES", so the ECG is an independent variable
  in their own analysis rather than a nuisance regressor. One limit on the card: it is a single lead,
  supporting heart rate and heart-rate variability but not morphological analysis.
- [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) — one ECG
  channel on TP9, at the left fifth intercostal space, used as one of the dataset's own four
  validation channels (§1.6). No EOG and no respiration; the authors' ocular artifact removal relies
  on ICA rather than on a recorded ocular channel, which is the case
  [multimodal-biosignals/mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  reports as insufficient.
- [deap-2012](../collection/candidate-datasets/deap-2012/card.md) — the richest inventory in the
  strand and the only entry whose original paper "already separates the contribution of the peripheral
  modality from that of the EEG", reporting baseline classification separately for EEG, peripheral
  signals and multimedia content. The card also names a dual character worth preserving: the four EOG
  and four EMG electrodes (zygomaticus major, trapezius) are simultaneously the standard artifact
  references and, in an affect paradigm, the measure of interest.
- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) — four EOG channels
  "used as signal for H-infinity ocular filtering rather than only discarded", plus Empatica E4 blood
  volume pulse (64 Hz), derived heart rate (1 Hz), electrodermal activity (4 Hz), skin temperature
  (4 Hz), triaxial wrist acceleration (32 Hz) and two APDM Opal inertial units (128 Hz). No ECG and no
  respiration.
- [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) — four EOG channels, "usable
  as signal — the paper illustrates ocular activity taken from them", plus a head inertial unit.
  Nothing autonomic.
- [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) — a three-electrode ECG at
  256 Hz that the authors describe as allowing "precise identification of heart beats as well as the
  full ECG QRS complex", plus galvanic skin response. Its card marks it as "the kind of peripheral
  channel the project's third comparison would need — usable as signal, not recorded for artefact
  rejection".
- [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) — horizontal EOG and submental
  chin EMG, which are "diagnostic signals here rather than artefact references — sleep staging depends
  on them — so they are usable as signal by construction". Oro-nasal respiration and rectal body
  temperature in the sleep-cassette records only.
- [mous-2019](../collection/candidate-datasets/mous-2019/card.md) — bipolar vertical EOG, horizontal
  EOG and ECG on named channels at 1200 Hz, the same rate as the neural data, marked "usable as
  signal" on the card. This is "exactly the project's target set minus respiration", and it is the
  only entry other than STRUM for which that is true.

### 5.2 Present and hardware-synchronous, with no analysis on record either way

- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is the strand's richest peripheral
  inventory and the one for which no first-party analysis of those channels is on record, because the
  paper's own analysis is "an exemplary analysis of a slice" of the data. What is established, from
  section III: 2-channel ECG, 2-channel EOG and a 16-channel respiration belt, together with a
  43-channel EMG neckband, all on the *same 24-bit BioSemi amplifier as the EEG* — 269 channels per
  subject, 538 across the pair. Also present and outside the project's plan: force plate, head-mounted
  eye tracker with scene camera, two video cameras, desk microphone, an instrumented Xbox 360
  controller, and a room-scale PhaseSpace motion-capture system at 480 Hz.

  Two properties make this the strand's strongest peripheral specification and they should not be
  merged. The channels are *hardware-synchronous*, on one amplifier, so no cross-device alignment is
  required at all — which is a stronger guarantee than anything §6.3 can offer for a multi-device rig.
  And the inventory covers all three of the project's named peripheral modalities plus two it did not
  plan for. The card states the finding in exactly those terms: "The third comparison's premise is
  sound."

### 5.3 Present, standardized, and discarded by the field

Recorded because it is a fact about practice that no card in *this* strand states, and because it is
the direct comparator for whatever the project's third comparison would show.

- [datasets-benchmarks/sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)
  — the sibling card of [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md), written to
  the benchmark question rather than the candidate-dataset one, records that every recording carries
  EOG and chin EMG and the cassette subset adds airflow and temperature, and that "no checkpoint or
  benchmark suite in this corpus uses any of those channels": AdaBrain-Bench tabulates Sleep-EDF as
  two channels at 100 Hz, meaning the two EEG derivations only. Its own phrasing is the useful one —
  "The peripheral channels are present, standardized, and universally discarded."

The measured counterpart, from the fusion strand rather than this one:
[multimodal-biosignals/hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
holds body movement and visual input constant across workload levels and reports EEG at about 86
percent against 70 to 75 percent for peripheral physiology and eye measures, with no statistically
significant improvement from combining sensor groups. That is a negative result on fusion from a
study designed to test it, and it is the reference point against which "adding peripheral physiology
helps" would have to be argued.

### 5.4 No peripheral channels

- [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  records bipolar EOG computed from periocular electrodes, used for artifact handling rather than as
  signal, and nothing else. It is a paper rather than a candidate corpus, so this is a specification
  note rather than a coverage entry.

No `type: dataset` entry in the strand carries EEG with zero peripheral channels. Every one of the
eleven has at least EOG or ECG or a wristband channel. The variation is entirely in *which* modality
and in whether the source used it.

---

## 6. Multi-person recordings, and the shape of their scarcity

The brief anticipated that this category might come back thin, asked for the queries to be recorded,
and stated that whether the scarcity constitutes a gap is not this phase's call. This node records
what exists and how it is distributed. It does not say whether the distribution is a gap.

### 6.1 What exists

Four entries in the corpus record two or more people wearing EEG simultaneously. Ordered by the
number of participants instrumented at once:

- **Four simultaneous** — [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md). Five
  groups of four watching long videos together, all four wearing EEG, ECG and galvanic skin response
  sensors, driven from a single PC that both "present[ed] the stimuli" and "get[s] and synchronize[s]
  signals". 14-channel consumer headset at 128 Hz. The only four-way simultaneous physiological
  recording in the corpus.
- **Three simultaneous** — [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md).
  Each recording covers one actor dyad plus either the director or an audience member, all
  instrumented at once, across six rehearsals and three public performances in one week. 28 EEG plus
  4 EOG at 500 Hz per person, plus wristband autonomic channels.
- **Two simultaneous** — [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md). Two
  professional dancers, recordings "obtained simultaneously and in synchrony for the two
  participants", across ten sessions in four months. 28 EEG plus 4 EOG at 1000 Hz.
- **Two simultaneous, at high density** —
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md). 28 pairs, "the data for each
  two-participant session were recorded into a single time-synchronized file in XDF format", at 206
  EEG channels plus 63 peripheral channels per person.

### 6.2 How the four are distributed

Five properties of the distribution, each grounded, and stated as description:

- **Two of the four come from one laboratory.**
  [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) and
  [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) share the
  Contreras-Vidal mobile brain-body imaging group at the University of Houston, the same toolchain and
  the same 28-EEG-plus-4-EOG configuration; the strand's `INDEX.md` records that a targeted PubMed
  query restricted to *Scientific Data* returned exactly these two.
- **Participant counts are small in three of four.** Two people
  ([livewire-2024](../collection/candidate-datasets/livewire-2024/card.md)), ten people of whom three
  were recorded for about seven minutes
  ([boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md)), twenty people in five
  groups ([amigos-2021](../collection/candidate-datasets/amigos-2021/card.md)). STRUM's 56 is an order
  of magnitude larger than any of them.
- **Density and access trade against each other across the four.** The three open ones are 14, 28 and
  28 channels; the 206-channel one is available only by request to the authors (§7.1). No entry in the
  corpus is both dense and openly downloadable and multi-person.
- **The tasks are heterogeneous.** A screen paradigm
  ([amigos-2021](../collection/candidate-datasets/amigos-2021/card.md)), two naturalistic performance
  settings ([boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md),
  [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md)), and one operational task
  battery ([strum-2018](../collection/candidate-datasets/strum-2018/card.md)). Their label provenances
  differ correspondingly, spanning §1.1, §1.2 and §1.5, so the four are not interchangeable on any
  axis but simultaneity.
- **The stable-group property is not uniform.**
  [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md)'s card records that the
  third instrumented person differs by session, "so the three simultaneously recorded participants are
  not a stable triad across sessions", which its own card flags as making the self-described
  "hyperscanning" framing looser than the recording warrants.

### 6.3 Synchronization precision, which bounds any cross-participant analysis

The brief asks for synchronization method and its *measured* precision. The corpus's answer is
asymmetric, and the asymmetry is the finding.

- **No dataset in the strand reports a measured cross-participant timing error.**
  [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) uses a custom hardware
  trigger with post-hoc alignment against a filmed UTC clock and reports no numeric precision, which
  its card flags as "a real limit on what inter-participant analyses it can support" given that the
  dataset's own stated purpose includes quantifying synchronization "within and across all
  participating individuals". [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md)
  uses manual triggers with no measured offset or jitter, which its card notes is "a weaker mechanism
  than the hardware triggers used by the same laboratory".
  [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) reports none for the four
  participants in a group relative to one another.
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md) reports none either, though it
  writes both participants into one Lab Streaming Layer XDF file.
- **The only measured numbers in the strand are device-to-device, not participant-to-participant.**
  [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) reports 156 microseconds of offset
  jitter in a single-machine test against a National Instruments reference (on top of a *fixed* 12.20
  ms setup offset), 145 microseconds networked (on a 6.26 ms offset), and approximately 0.5 ms
  standard deviation between jitter-corrected EEG and EMG streams. Its card is explicit about the
  shape of the result: LSL "does not remove the constant transport delay of a device; it makes that
  delay stable enough that a single pre-measured constant can be subtracted. Any recording that did
  not measure its device offsets carries them uncorrected."
- **And the LSL paper itself declines the extrapolation.** Its card records: "No multi-*participant*
  synchronisation test is reported. Everything measured is multi-*device*. Whether two separately
  capped participants on two amplifiers achieve the same sub-millisecond jitter is a reasonable
  extrapolation, not a published result." It also records that the single-machine and networked
  offsets differ by a factor of two with only a hypothesis offered for why, so neither figure is an
  expected value for a new rig.

This is the strand's clearest instance of a specification gap that is answerable rather than
unanswerable: the numbers exist for the framework, they are absent from the datasets, and their
absence is a reporting choice by the dataset papers, not a property of the field.

### 6.4 What the search record establishes, and what it does not

The strand's `INDEX.md` records six queries and their returns. Two properties of that record are
worth carrying forward, because they bound what a later reader may conclude from it:

- **The returns were not empty; they were the wrong kind of thing.** The hyperscanning query returned
  20 results of which zero were dataset releases — reviews and methods papers (Hamilton 2020; Barraza
  et al. 2019; Hakim et al. 2023; Zamm et al. 2024; Carollo & Esposito 2024), most of them out of
  scope for this strand under the brief's exclusion of hyperscanning methodology. The PubMed sweep
  found multi-person neuroimaging *datasets* being released in fNIRS and fMRI rather than EEG, with
  three specific fNIRS and fMRI hyperscanning data descriptors named. One PubMed query
  (`EEG[Title] AND dataset[Title] AND (dyad*|dyadic|interpersonal|two-person)[Title]`) returned zero
  hits.
- **One of the zero results is not evidence of absence, and the index says so.** OpenNeuro's GraphQL
  `advancedSearch` returned zero edges for `hyperscanning`, `dyadic`, `conversation` and `joint
  action` under `modality: "EEG"`, but
  [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md)'s card records that
  `DatasetSearchInput` has no free-text field and rejects Elasticsearch-style query inputs, so a zero
  means "nothing tagged with that keyword", not "nothing exists". Its card generalises the point:
  whether the zero reflects the archive's holdings or its tagging "cannot be distinguished from the
  interface, which is itself a finding about registry coverage".
  [nemar-2022](../collection/candidate-datasets/nemar-2022/card.md) is the entry that exists partly
  because of this: it is the EEG-scoped browsable layer over the same archive, and its card notes the
  difference between "600 datasets, mostly MRI" and a browsable EEG inventory.

---

## 7. Access, and the inaccessible-versus-unreported distinction

### 7.1 The friction ladder

Recorded in `INDEX.md` as prose; restated here as an ordering because it is a property every entry
has a value on, and because the ordering is what a reader would otherwise reconstruct by hand.

| friction | entries |
|---|---|
| CC0, no account | [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) default — "places no restrictions on who can use the data or what can be done with them" |
| Open Data Commons Attribution, no account | [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md), 8.1 GB by browser, `wget`, or `aws s3 sync --no-sign-request` |
| CC BY, open download | [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) (Zenodo and OpenNeuro `ds003670`), [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) (FigShare, licence stated in the paper itself) |
| Open download, data licence unstated | [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md), [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) |
| Click-through data use agreement with registration | [mous-2019](../collection/candidate-datasets/mous-2019/card.md) |
| Printed, signed, scanned end-user licence agreement | [deap-2012](../collection/candidate-datasets/deap-2012/card.md), [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) |
| Request to the authors, no published route | [strum-2018](../collection/candidate-datasets/strum-2018/card.md) |

Three refinements the cards add that the ladder alone loses:

- **The article licence and the data licence are different objects and diverge often.**
  [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) and
  [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) are both CC BY-NC-ND as
  articles; LiveWire's *data* are CC BY 4.0, stated in Data Records, while BOA's data licence "is not
  stated in the paper text". [mous-2019](../collection/candidate-datasets/mous-2019/card.md) is CC BY
  4.0 as an article and governed by a data use agreement as data.
- **CC0 by default is not CC0 guaranteed.**
  [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md)'s card records that the
  licence of any specific dataset must be read from its own `dataset_description.json`, and that CC0
  "removes legal restrictions but not ethical ones" — a dataset being CC0 "does not certify that its
  consent covers model pretraining".
- **STRUM's access route contradicts its own paper.** The abstract calls it "a new open dataset" and a
  footnote gives a distribution point, `http://headit.ucsd.edu/`. The community index
  `meagmohit/EEG-Datasets` records the route verbatim as "Strum dataset is not available on
  headit.ucsd .. contact authors". The card's reading, which this document carries: the data were
  published and the host has since gone away, so "what remains open is whether the authors will supply
  it now, not whether it was ever public". No registry sweep (PhysioNet, OpenNeuro, NEMAR, Zenodo,
  figshare) located a hosted copy; Unpaywall reports `oa_status: closed` with an empty `oa_locations`
  array; and `intheon.io/projects` "lists LSL, XDF, ASR, BCILAB and SIFT and does not mention STRUM at
  all".

One access-adjacent fact that belongs with the ladder rather than in a footnote:
[strum-2018](../collection/candidate-datasets/strum-2018/card.md) has 2 citations, agreeing across
Semantic Scholar and OpenAlex, and neither citing work trains or evaluates a model on STRUM data.
[lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) is one of the two. The 21 referenced
works are a pre-2017 passive-BCI methods lineage — Farwell & Donchin 1988, Ramoser et al. 2000, Ang
et al. 2008, Zander & Kothe 2011, Kothe & Makeig 2013, Bigdely-Shamlo et al. 2013 — with no dataset
descriptor among them. The card's own reading of what this figure supports is the careful one: it is
"a fact about visibility, not about quality", and it is consistent both with a dataset nobody modelled
and with one nobody could obtain.

### 7.2 Entries whose decisive facts are inaccessible rather than unreported

`_briefs/synthesis-practice.md` requires this distinction to survive into synthesis, and requires a
node rather than a footnote where a strand has more than one or two such entries. This strand has
five, in two different senses, and the senses have opposite implications for whether re-retrieval is
worthwhile.

**Abstract-only: the paper reports the numbers and we could not read them.** Three entries, all three
in §1.8, which is to say the label-validity axis is the part of the strand most affected.

- [deniz-2019-modality-invariant-semantics](../collection/candidate-datasets/deniz-2019-modality-invariant-semantics/card.md)
  — "Participant count, story durations, model specification, the exact correlation values behind
  'highly correlated', and the cross-modality prediction accuracies are all reported in the paper and
  are all unread. Nothing quantitative should be attributed to this entry." The card also notes that
  "almost identical" is a qualitative abstract summary and that the residual difference "could be
  small and real, and this card cannot say how large it is". This matters because the elimination
  argument in §1.8 is only as tight as that residual.
- [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
  — participant count, scan parameters, category set, effect sizes and per-modality accuracies all
  reported and all unread; and the abstract does not say how large the modality-specific component is
  relative to the modality-independent one, "which is what would determine how much of a
  spoken-versus-written EEG classifier's accuracy is sensory".
- [snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
  — simulation parameters, empirical accuracies, the exact cross-validated procedure and any released
  code all unread, "so no implementation detail should be taken from this card". The card's
  recommendation (cross-validated confound regression) is therefore on record as a conclusion without
  a reproducible procedure attached.

**Read but not redistributable, or read only in part.**

- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — the opposite case, and the
  strand's most important one. The complete six-page paper *was* obtained through institutional access
  on 2026-08-01 and every fixed field is read from section III; the PDF is cached locally, gitignored
  and uncommitted because the paper is under IEEE copyright. So STRUM's specification is not
  inaccessible; it is inaccessible *to redistribution*. What remains genuinely unreported by the paper
  is a short list: the reference used for any released version, the electrode coordinates, and the
  usable session count after "3 datasets were excluded due to interruptions".
- [deap-2012](../collection/candidate-datasets/deap-2012/card.md) — a mixed case that must not be
  filed as "unreported". The peripheral channel enumeration is contradictory *in the paper* (§9.2),
  and the object that would resolve it — the distributed channel list — is *inaccessible*, because the
  host was returning HTTP 503 throughout retrieval. Re-retrieval is worthwhile here in a way it is not
  for a genuinely silent source.
- [nemar-2022](../collection/candidate-datasets/nemar-2022/card.md) — CC BY-NC per Europe PMC, but
  both the Oxford University Press PDF endpoint and the Europe PMC full-text endpoint refused
  automated download, so the card is written from a rough extraction and carries no scale numbers at
  all.

### 7.3 Retrieval failures that are properties of the record

Three, recorded so they are not mistaken for properties of the datasets:

- `eecs.qmul.ac.uk`, the host serving both the DEAP and AMIGOS project pages, returned HTTP 503
  throughout retrieval over both HTTP and HTTPS, so neither end-user licence text nor DEAP's
  distributed channel list could be read.
- IEEE Xplore blocks automated retrieval, which is why
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md)'s author-order discrepancy had to
  be settled from the PDF title block rather than from the publisher page (§9.2).
- OpenNeuro's search interface has no free-text field, so the category-1 sweep could not be run as a
  free-text query at all (§6.4).

---

## 8. The four entries that specify no recording

Four of the 19 entries have no label, no manipulation geometry, no channels and no peripheral
inventory. They are not datasets and they are not label-validity papers; they constrain or describe
the other entries. This node exists so that the coverage table does not have to pretend otherwise.

### 8.1 The format specification

- [eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md) — the extension that makes
  §4.4 machine-checkable. `channels.tsv` "must be specified"; `electrodes.tsv` and `coordsystem.json`
  "should be specified if the positions of the electrodes are known". Its card draws the consequence
  for this project precisely: a dataset with those two files "hands the checkpoint measured
  coordinates in a named frame; a dataset without them forces the fallback", so BIDS compliance is "a
  concrete predictor of whether a checkpoint can ingest it without approximation" — with the caveat
  that "compliance is a floor, not a guarantee", since the two coordinate files are recommended rather
  than required and a fully valid BIDS-EEG dataset can carry no electrode coordinates.

  `channels.tsv` also carries the §5 distinction in machine-readable form: it is where channel type
  (EEG, EOG, ECG, EMG, MISC) and status live, rather than in a methods paragraph. Two candidate
  datasets expose their peripheral inventory that way
  ([tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md),
  [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md)), and one
  more in MEG form ([mous-2019](../collection/candidate-datasets/mous-2019/card.md)).

  Two limits the card names that matter for this strand specifically. Neither recommended format
  expresses a derivation scheme as a first-class concept — a bipolar channel appears as a channel
  named `Fpz-Cz`, and whether tooling parses that as a difference is left to convention, which is §4.1
  restated as a format problem. And the specification standardises where metadata lives, not whether
  it is correct: "a `channels.tsv` can name a reference that does not match what was recorded, and
  nothing in the format detects that".

### 8.2 The registries

- [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) — the access-route
  reference point (§7.1) and the negative search result (§6.4). Its "long tail" framing is the
  property the card marks as relevant beyond licensing: the archive is built for "datasets of tens of
  participants collected for a specific question", which is the size regime this project sits in.
- [nemar-2022](../collection/candidate-datasets/nemar-2022/card.md) — the EEG/MEG/iEEG-scoped gateway
  over OpenNeuro with per-dataset quality assessment and a handoff to San Diego Supercomputer Center
  compute. Two facts on its card connect to other nodes. It is the entry that argues for Hierarchical
  Event Descriptors, on the grounds that "BIDS standards in themselves do not constitute a system for
  adequately describing the timeline of the recording" — which is the standard
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md) already uses, in an extended form
  of HED 1.0, and which the card identifies as "precisely the gap in which a label like 'spoken' versus
  'written' gets defined inconsistently across datasets". And it is a Swartz Center product, one of the
  two institutional homes the brief named for a STRUM author copy; STRUM is not in it.

### 8.3 The synchronization framework

- [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) — the measured numbers in §6.3, the
  XDF container in §4.5, and one of the two works citing STRUM. Its card also records a limit that
  applies to every number it publishes: LSL timestamps a sample "when the operating system receives
  it, not when the sensor acquired it", so all reported figures measure transport and clock behaviour
  rather than end-to-end acquisition latency, and per-device offsets must be characterised separately
  by whoever builds the rig.

---

## 9. Where the corpus disagrees with itself

A register. Nothing here is resolved. The three kinds are kept apart deliberately, because conflating
them would let a later reader promote a rounding into a substantive disagreement or treat a defect in
our records as a fact about the field.

### 9.1 Kind 1: cards disagreeing about the same quantity

**STRUM's use of the Lab Streaming Layer — confirmed on one card, unresolved on another.** This is
the strand's one clean kind-1 disagreement and it is a staleness rather than a difference of reading.
[strum-2018](../collection/candidate-datasets/strum-2018/card.md), rewritten against the full paper on
2026-08-01, states: "Lab Streaming Layer, with each two-participant session written to a single
time-synchronized XDF file. The Lab Streaming Layer lead recorded in this strand's brief as an
inference is therefore confirmed by the primary source."
[lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) still states the pre-retrieval position:
"That citation establishes only that LSL's authors cite STRUM — it does not establish that STRUM used
LSL, and the STRUM methods could not be read to confirm it. The relationship is recorded as unresolved
on `strum-2018`." The second sentence is a claim about the first card that the first card no longer
supports. Both are recorded; neither is picked. **This is a defect in the corpus rather than a fact
about the field, and a synthesis document cannot fix a card. It should be filed against
`lsl-2024`.**

**Simanova's headline accuracy — 0.79 or 0.89, and the strand's own index takes the higher one.**
[simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
records both figures and instructs which to carry: "the highest classification accuracy reached over
all subjects was 0.89", with "a mean value of 0.79 (SD = 0.07)", and "0.89 is the best single subject,
not the group result; quoting it alone overstates the paper, and the mean is the number synthesis
should carry". The strand's `INDEX.md` line for the entry states "single-trial EEG decoding reached
89% for pictures" without the mean. The card and the index are the same record at two levels of
detail, and the index takes the reading the card warns against. **Recorded as a corpus defect against
`INDEX.md`, not against the card, which is correct.** This document carries 0.79.

**The count of EEG datasets carrying a peripheral modality — six, seven, or eight.** §5 above. The
index states six in its category-2 paragraph and again in its acceptance-criteria table; the
enumeration inside that same paragraph names seven EEG datasets; and the union of the cards is eight
once [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is counted. The card set and
the index disagree, and the index disagrees with itself.

**Whether the strand contains three or four multi-person EEG recordings.** §6.1. `INDEX.md` states
three; [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is the fourth and is filed
under a different category. The number three is correct for category 1 as a filing decision and
incorrect as a statement about the corpus.

### 9.1a Kind 1 between two cards of the same paper — corpus defects

Three works are deliberately carded in both this strand and `datasets-benchmarks`. Each pair diverges,
and each divergence is a defect in our records rather than a disagreement in the literature. All three
should be filed.

**EEG-BIDS: the requirement level of `electrodes.tsv`, and the number of permitted formats.**

| reading | card |
|---|---|
| `electrodes.tsv` and `coordsystem.json` are "recommended, not required", stated once and used as the basis for the card's central argument | [eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md) |
| the paper states the requirement level *two ways* — a conditional "should be specified if the positions of the electrodes are known" in the summary against an unconditional researchers "may in addition specify an 'electrodes.tsv' file" in the specific-considerations section — and the card flags the difference as deciding "whether a coordinate-based checkpoint can rely on positions being present in a conformant dataset" | [datasets-benchmarks/eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) |

The two cards are not asserting different facts; one flags an internal inconsistency in the source and
the other does not, and the one that does not is the one this strand's §4.4 and §8.1 arguments rest
on. The same pair diverges twice more. On formats:
[eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md) says the specification "names
only two recommended official data formats" (EDF and BrainVision), while
[datasets-benchmarks/eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) records four
permitted formats — the two official plus "unofficial but allowed" EEGLAB `.set`/`.fdt` and Biosemi
`.bdf` — and flags "'Only two' official formats, then four are permitted" as a source inconsistency.
That difference is load-bearing in this strand specifically, since
[boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) and
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) distribute `.set` and
[strum-2018](../collection/candidate-datasets/strum-2018/card.md) is BioSemi-acquired. On
`events.tsv`: the `datasets-benchmarks` card lists it among the required files in the `eeg/`
directory; the `candidate-datasets` card describes what it does without stating a requirement level.

**OpenNeuro: rounded figures against exact ones, and one card flags the source's internal gap while
the other does not.**

| figures | card |
|---|---|
| "more than 600 datasets and 20,000 participants at time of publication", "more than 150 publications" | [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) |
| 604 datasets, 20,989 participants, 165 reuse publications, 81 scalp-EEG datasets and 8 iEEG, 406 TB distributed — and three flagged internal inconsistencies: 604 against "the 502 OpenNeuro datasets available via DataLad" for the same 9 October 2021 cutoff, Table 1's modality counts summing to 1,124 against 604 total, and the abstract rounding where the results are precise | [datasets-benchmarks/openneuro](../collection/datasets-benchmarks/openneuro/card.md) |

The values are the same source's abstract and body respectively, so at the level of numbers this is
kind 3 (see §9.3). What makes it a kind-1 defect is that one card of the same paper flags the 604/502
gap and the modality double-counting and the other reproduces the abstract's rounding with neither
flagged. A reader using only the `candidate-datasets` card would not know that "more than 600" has a
502 sitting behind it.

**Sleep-EDF: one card computes a total-hours figure the other card explicitly declines to compute.**
[sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) gives "roughly 3,450 hours by
arithmetic from the reported figures".
[datasets-benchmarks/sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)
states the same inputs and then: "the landing page gives no total and the durations are approximate,
so this card does not compute one." Neither is wrong; they applied opposite conventions to the same
non-figure, and a downstream table that pulls "3,450 h" from one card and "not stated" from the other
would read them as a disagreement about the data. The same pair diverges on completeness in two
smaller ways: the `candidate-datasets` card records that submental EMG is sampled at 100 Hz in the
telemetry study against a 1 Hz envelope in the cassette study, which the sibling omits; and the
sibling records a widely used 78-subject figure sourced from AdaBrain-Bench's preparation rather than
from the landing page, plus a Rechtschaffen-and-Kales-versus-AASM label-space mismatch, neither of
which appears on the `candidate-datasets` card.

### 9.2 Kind 2: sources that contradict themselves, carded faithfully

The disagreement is in the literature, not in our corpus. Seven of the 19 entries carry at least one.

- [strum-2018](../collection/candidate-datasets/strum-2018/card.md) — four, which is the most of any
  entry in the strand and all four in the one paper the project most depends on. **Channel count**:
  section III says "206channel EEG montage", section IV says "the 205-channel EEG was subsampled to a
  subset of 64 approximately equidistant channels"; the card takes 206 under the standing rule
  preferring the section describing the recording, and quotes both. **Participants**: 56 as 28 pairs
  against a sex breakdown of "13 f, 49 m" summing to 62. **Openness**: the abstract says "open
  dataset" and a footnote gives `http://headit.ucsd.edu/`, against a practical route of
  request-to-authors. **Author order**: dblp and Semantic Scholar give Mullen, Kothe, Makeig; Crossref
  and OpenAlex give Kothe, Mullen, Makeig; the PDF title block settles it as Kothe, Mullen, Makeig,
  and the card notes the `.bib` entry still carried the dblp order and was corrected. Separately, the
  reference list is 21 works in OpenAlex against 24 in the printed bibliography, with three years
  disagreeing between the indexes and the printed list.
- [deap-2012](../collection/candidate-datasets/deap-2012/card.md) — two enumerations of the peripheral
  channels that disagree about whether ECG is present. One lists "electrocardiogram" among the
  recorded signals; the sensor-placement figure and channel inventory list a plethysmograph for blood
  volume and no cardiac electrode. The card applies the standing rule preferring figure and count over
  body prose and therefore "does not assert that DEAP carries ECG", and names why this is not
  pedantic: "blood volume pulse and ECG support different heart-rate-variability measures, and the
  third comparison would be built on whichever one is actually there". Separately, "thirteen
  peripheral physiological signals" does not reconcile with the eight signal types enumerated; the
  card carries the paper's figure and flags that it could not be reconciled (four EOG plus four EMG
  plus GSR, respiration, plethysmograph and temperature is twelve).
- [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) — publication year ambiguous
  across indexes: Crossref and IEEE date the issue to 2021, Semantic Scholar reports 2017, and the
  arXiv preprint used for extraction is from 2017. The card uses 2021 and the `.bib` entry records the
  discrepancy.
- [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  — the transfer-learning table reports significance values with a second value in parentheses
  (spoken 1.7×10⁻⁵ (0.001), written 0.02 (0.32)) whose meaning is defined in a table footnote the
  extraction did not preserve legibly. The card quotes them as printed and declines the natural
  uncorrected/corrected reading rather than asserting it.
- [datasets-benchmarks/eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md) — the
  should/may and two/four inconsistencies of §9.1a are *source* self-contradictions; they become a
  corpus defect only because one of our two cards records them and the other does not.
- [datasets-benchmarks/openneuro](../collection/datasets-benchmarks/openneuro/card.md) — 604 against
  502 for one cutoff date, Table 1 summing to 1,124 against 604, CC0 called "a dedication, a licence
  and an agreement in three places", and "session" used in two senses in one paper.
- [datasets-benchmarks/sleep-edf-expanded](../collection/datasets-benchmarks/sleep-edf-expanded/card.md)
  — the PhysioNet page dated "Published: Oct. 24, 2013. Version: 1.0.0" while describing a March 2018
  expansion, so the version string does not track the content; and hypnograms scored under
  Rechtschaffen and Kales from Fpz-Cz/Pz-Oz rather than the C4-A1/C3-A2 the manual specifies, so "the
  labels are not strictly manual-conformant and a model learning them is learning a variant scoring".
- [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) — the four eye
  electrodes described as part of the "32-channel EEG head cap" in one place and as EOG in another.
  The card resolves it as a labelling choice rather than a contradiction of fact — the ocular channels
  share the EEG amplifier and sampling rate — and warns that "a reader treating them as an independent
  peripheral modality should know they come from the same cap".

### 9.3 Kind 3: differences that look like disagreements and are not

Recorded precisely so they are not promoted into §9.1.

- **OpenNeuro's scale.** "More than 600 / 604 datasets", "more than 20,000 / 20,989 participants",
  "more than 150 / 165 publications". These are the same paper's abstract and results sections, and
  the two cards of it each took a different side. The values are roundings; the *defect* is the
  unflagged flagging asymmetry recorded in §9.1a, not the numbers.
- **Sleep-EDF's total hours.** 3,450 h computed against no total computed. One arithmetic convention
  against another over the same two approximate durations, not two measurements.
- **Hinss's channel count.** "64 active Ag-AgCl electrodes ... of which one (TP9) is used for ECG" on
  the card against "63 EEG channels plus 1 ECG" in the index. Same fact, two framings, and the second
  is the correct reading of the first.
- **BOA's channel count.** 32 channels per participant as the nominal configuration, 31 for P01 on all
  three dyads because electrode CP6 was removed. A documented per-subject exception, not an
  inconsistency.
- **DEAP's sampling rate.** 512 Hz as acquired against 128 Hz in the widely distributed preprocessed
  version. The card states both and identifies which is which.
- **STRUM's sampling rate.** Acquired at 2048 Hz, resampled to 512 Hz. Two rates for one recording.
- **STRUM's session hours.** "About 3.5 hours" per session is reported; "on the order of 98
  session-hours" for 28 pairs is arithmetic the card performs and explicitly marks as "arithmetic
  rather than a reported figure". The distinction should survive: no corpus total is reported by the
  paper.
- **TES/GX and DEAP totals.** Roughly 72 hours and roughly 21 hours respectively, both computed by
  their cards from session counts and durations and both marked as arithmetic rather than reported.

---

## Coverage: all 19 entries and where each sits

The "primary" column names the node where the entry is most distinguishing. Entries appear in several
nodes because the facets are orthogonal by construction: every dataset has a label provenance (§1), a
manipulation geometry (§2), an ingestion contract (§4), a peripheral profile (§5) and an access route
(§7).

| entry | primary node | also appears in |
|---|---|---|
| [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) | §6.1 four simultaneous participants | §1.2, §1.6, §1.9, §2.2, §4.1, §4.2, §4.3, §5.1, §6.2, §6.3, §7.1, §9.2 |
| [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) | §6.1 three simultaneous participants | §1.5, §2.3, §2.4, §2.5, §4.1, §4.2, §4.3, §4.4, §4.5, §5.1, §6.2, §6.3, §7.1, §9.2 |
| [deap-2012](../collection/candidate-datasets/deap-2012/card.md) | §5.1 peripheral channels as signal | §1.2, §2.2, §4.1, §4.2, §4.3, §4.4, §4.5, §7.1, §7.2, §9.2, §9.3 |
| [deniz-2019-modality-invariant-semantics](../collection/candidate-datasets/deniz-2019-modality-invariant-semantics/card.md) | §1.8 what the contrast can be about | §3, §7.2 |
| [eeg-bids-2019](../collection/candidate-datasets/eeg-bids-2019/card.md) | §8.1 the format specification | §4.4, §4.5, §5, §9.1a |
| [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) | §1.6 three label sources on the same trials | §1.1, §1.2, §1.4, §2.2, §2.3, §2.4, §2.5, §4.1, §4.2, §4.3, §4.4, §4.5, §5.1, §7.1, §9.3 |
| [kothe-2023-nback-nirs](../collection/candidate-datasets/kothe-2023-nback-nirs/card.md) | §1.1 the experimental-parameter label, unvalidated | §2.2 |
| [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) | §6.1 two simultaneous participants | §1.5, §2.3, §2.4, §4.1, §4.2, §4.3, §4.4, §4.5, §5.1, §6.2, §6.3, §7.1, §9.1a |
| [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) | §6.3 measured synchronization precision | §4.5, §7.1, §8.3, §9.1 |
| [mous-2019](../collection/candidate-datasets/mous-2019/card.md) | §2.1 between-subjects manipulation | §1.1, §3, §4.1, §4.2, §4.3, §4.5, §5.1, §7.1, §8.1 |
| [nemar-2022](../collection/candidate-datasets/nemar-2022/card.md) | §8.2 the registries | §6.4, §7.2 |
| [openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) | §8.2 the registries | §6.4, §7.1, §9.1a, §9.3 |
| [ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md) | §1.8 does a decode establish a representation | §3 |
| [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md) | §1.7 the one demonstrated failure | §2.2, §2.5, §3, §4.1, §4.2, §4.3, §5.4, §9.1, §9.2 |
| [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md) | §1.8 the test that isolates what survives | §2.2, §3, §7.2 |
| [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) | §4.1 bipolar derivation | §1.3, §1.9, §2.2, §2.3, §2.5, §4.2, §4.3, §4.5, §5.1, §5.3, §7.1, §9.1a, §9.3 |
| [snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md) | §1.8 can an identified confound be removed | §7.2 |
| [strum-2018](../collection/candidate-datasets/strum-2018/card.md) | §3 the factorial design | §1.1, §2.2, §2.3, §4.1, §4.2, §4.3, §4.4, §4.5, §5.2, §6.1, §6.2, §6.3, §7.1, §7.2, §9.1, §9.2, §9.3 |
| [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) | §5.1 peripheral channels as signal | §1.1, §1.2, §1.4, §1.6, §2.2, §2.3, §2.5, §4.1, §4.2, §4.3, §4.4, §4.5, §7.1, §9.3 |

Every entry appears in at least two nodes.
[kothe-2023-nback-nirs](../collection/candidate-datasets/kothe-2023-nback-nirs/card.md) is the
narrowest, at two, which is the intended shape: it is NIRS rather than EEG, admitted by the brief for
its label reasoning alone, and it has no ingestion contract, no peripheral inventory and no access
route this project would use.
[snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
and [nemar-2022](../collection/candidate-datasets/nemar-2022/card.md) are next, also at two, for the
same reason in different directions — one is a methods paper with no recording, the other a gateway
with no holdings. No entry failed to fit a node.
