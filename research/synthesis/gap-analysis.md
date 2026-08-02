# Gap analysis

Phase 4. Its inputs are the seven Phase 3 documents in this directory — the four strand ontologies,
the cross-strand [science map](./science-map.md), the [dataset hierarchy](./dataset-hierarchy.md) and
the [scope diagram](./scope-diagram.md) — together with the 84 cards they organize.

**What changes here.** Phases 1 to 3 were forbidden from stating properties of the set. This document
states them. Absence, coverage, sufficiency, and whether the project's plan is sound are its subject.

**Why that freedom is dangerous, and what constrains it.** The corpus is 84 entries selected by briefs
written before anyone had read the literature. It is not exhaustive, it is not PRISMA, every
acceptance criterion is a floor, and its discovery route was the citation graph outward from a
user-supplied seed set ([scope-diagram](./scope-diagram.md) §5). A gap that is really a hole in our
collection, presented with the full apparatus of citation, would be a false finding dressed as a
result. Two guards run through the whole document.

*Guard one.* No absence is called a gap until it carries four things: **the evidence** (the set of
cards whose combined coverage leaves the space empty, not one card saying nobody has done it), **the
scope check** against [scope-diagram](./scope-diagram.md) classifying it as a genuine absence, a
partition, a scope judgment or a resource limit, **the falsifier** (one finding that would show it is
not real — "more evidence" is not a falsifier), and **the search record** where one exists. §3 holds
the candidates that failed the scope check, and that list is as informative as §2.

*Guard two.* §5 states what the corpus does **not** support, as its own section rather than a closing
caveat: claims blocked by inaccessible entries, questions where two entries point opposite ways with
no basis to choose, and the places where this document's own confidence outruns the number of entries
behind it.

**Structure.** §1 is column one, what prior work covers. §2 and §3 are column two, what is uncovered
and which of those absences are ours; §2.1 holds the four absences this document published and has
since withdrawn. §4 is column three, the actionable subset with a route for each. §5 is guard two. §6
assesses the project's three planned comparisons. §7 records what this document needed from the
synthesis layer and could not find.

**A third guard, added after the fact.** This document has been through an adversarial refutation pass
and did not survive it intact. Four of its eleven gaps are retracted, two are restated smaller, one is
relocated, and three sections of §6 are rebuilt. Every retraction was forced by evidence that was
already in the corpus when the gap was written, and in three cases by a card the gap itself cited. The
withdrawn claims are kept in place with what refuted them, because the pattern in the failures is a
finding about how this review checks itself — §2.1 and §5.3 — and because a gap analysis that quietly
deletes its errors is less trustworthy than one that shows them.

---

## 1. Column one: what prior work covers

Stated as what the corpus **does** support, so that §2's absences have a positive background. Each
line is a claim the corpus can carry; none is a claim about the whole field.

**The measurement layer is well covered and internally consistent about its own unreliability.** The
cost of moving the holdout boundary is measured four times, in three strands, by independent groups,
and every measurement exceeds the effect the study was trying to detect: 46.8 points segment-to-subject
([brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)), error
rises on all five replicated models with two at chance
([kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)),
7.74 and 13.1 points from 10-fold to leave-one-subject-out
([angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)),
12.7 points from a session change alone
([zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md)). The
null is covered ([combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)),
the interval is covered
([varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)),
and one entry implements inference to the standard both recommend
([moabb](../collection/datasets-benchmarks/moabb/card.md)). A project that gets its protocol wrong
cannot claim the literature failed to warn it.

**Identity confounding is covered at six levels of granularity by four strands.** Dataset, subject
(twice, independently), session, segment, trial and exemplar — the table is
[science-map](./science-map.md) §2. The mechanism is not in dispute anywhere in the corpus. Two
corrections to that table, both established in §2.1 and §6.0 below: its session row reads "not
measured anywhere", and [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md)
measures a session-or-trial boundary against a subject boundary on the same models and tasks; and
STRUM's design instantiates two further levels the table has no row for, the within-session block and
the co-recorded partner. Five remedies are enumerated, of which four are implemented on data and one
([ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md))
is a recommendation illustrated with somebody else's study.

**The spatial-identity contract of every carded checkpoint is known.** Five mutually exclusive
mechanisms, each entry in exactly one
([eeg-models-ontology](./eeg-models-ontology.md) §1): learned per-channel parameter
([labram-2024](../collection/eeg-models/labram-2024/card.md),
[biot-2023](../collection/eeg-models/biot-2023/card.md),
[bendr-2021](../collection/eeg-models/bendr-2021/card.md),
[femba-2025](../collection/eeg-models/femba-2025/card.md)), coordinate-driven
([reve-2025](../collection/eeg-models/reve-2025/card.md),
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md),
[luna-2025](../collection/eeg-models/luna-2025/card.md)), context-generated
([cbramod-2025](../collection/eeg-models/cbramod-2025/card.md)), learned remap onto a fixed superset
([eegpt-2024](../collection/eeg-models/eegpt-2024/card.md)), and position-blind
([brainwave](../collection/eeg-models/brainwave/card.md)). Whether a given recording can be ingested
at all is answerable in advance.

**That scale does not order the models is supported by six independent measurements.**
[eeg-models-ontology](./eeg-models-ontology.md) §2.5. Two entries dissent and both are qualitative.

**That a small supervised or classical model frequently matches or beats a checkpoint is supported by
six entries, four of them third-party.** [eeg-models-ontology](./eeg-models-ontology.md) §4.2.

**That the adaptation regime reorders the models is demonstrated rather than asserted**, inside two
suites, with opposite signs for different checkpoints
([omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md),
[adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md);
[datasets-benchmarks-ontology](./datasets-benchmarks-ontology.md) §2.2).

**The data layer is inventoried.** 154 distinct recordings, 14 carded in full, 140 named only, with
every carded recording's access route on record and the derivation, coordinate and peripheral fields
stated or explicitly marked absent ([dataset-hierarchy](./dataset-hierarchy.md) §1, §3).

**Label validity is covered as a procedure, not only as a caution.** One demonstrated failure with a
diagnostic attached
([simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)),
four tests that bound what a stimulus-condition label can mean
([candidate-datasets-ontology](./candidate-datasets-ontology.md) §1.8), and one dataset validating its
labels on three concurrent channels
([hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md)).

**The fusion literature's ablation structure is fully partitioned.** Every one of 25 entries has
exactly one value on "which arms exist"
([multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §1), and four entries supply
three arms on one split.

---

## 2. Column two: what the corpus reveals as uncovered

Eleven absences were named here. **Four have since been retracted**, against evidence that was already
inside the corpus when they were written: L1, L3, L7 and L11. They are kept, at the end of this
section, with what refuted each and what if anything survives, because a retracted gap is a finding
about this review's own method and deleting it would destroy the finding. Two of the four leave a
narrower residue behind them, which §4 still builds a route on. Seven gaps survive: two (L2, L10)
restated at the size the evidence supports rather than the size first claimed, and one (L5) relocated
from an instrumentation claim that was false to a comparison claim that holds.

Each survivor carries the four elements guard one requires. Where the scope check found a *bounded*
resource limit sitting behind an otherwise genuine absence, the bound is stated inside the gap rather
than hidden; **three of the seven** have one — L2, L6 and L8. The earlier text here said "three of the
eleven have one bound", which was an arithmetic error: the table marked four (L2, L3, L6, L8).

Ordering carries no ranking. Column three (§4) selects from these.

| # | the absence | scope class | recorded null search |
|---|---|---|---|
| L2 | two of the five *enumerated* remedies run on the same data | genuine, bounded | none |
| L4 | what ocular-artifact removal costs in task accuracy | genuine | none |
| L5 | decoders from EOG electrodes compared against decoders from eye tracking | genuine | none |
| L6 | a frozen EEG encoder paired with a frozen peripheral encoder | genuine, bounded | none |
| L8 | spoken versus written decoded from EEG within subject | genuine, bounded | none |
| L9 | a measured cross-participant synchronization precision | genuine | partial |
| L10 | an open EEG dyadic release from a second laboratory | genuine | **yes, seven queries** |
| L1 | **retracted** — AdaBrain-Bench measures it | — | — |
| L3 | **retracted as stated**; a narrower residue survives | — | — |
| L7 | **retracted as stated**; a narrower residue survives | — | — |
| L11 | **retracted** — the CBraMod delta is in the corpus | — | — |

**A note on the search-record column, before it is read as a defect.** Only one of the survivors is
backed by a recorded null search, and that is a real difference in evidential weight, not a formatting
gap. [scope-diagram](./scope-diagram.md) §5 states that the corpus has no screening log and that the
per-strand search records of §3.4 "cover category 1 of one strand and the STRUM citation search, and
nothing else". So L10 is the only absence in this document that rests on having looked and found
nothing. The rest rest on the combined coverage of entries collected for other reasons, plus, in
several cases, cards declaring the absence about themselves.

**And a second note, which the retractions force and which the first note was too mild to carry.**
[scope-diagram](./scope-diagram.md) §6 check 3 is a disjunction: an absence counts as a property of
the field if it is in §3.4's search record **or** if "a card states the absence about itself". The
second disjunct is unsound. A paper saying it did not run arm X is evidence about that paper; it is
evidence about the field only if the paper had reason to survey the field, and a primary study usually
does not. Seven of the original eleven cleared the check on that disjunct alone, and two of those
seven were wrong — L7, where two cards correctly declared the absence about themselves while two other
entries in the same corpus ran the comparison, and L5, where the card denied a fact its own source
stated. The rule is recorded as a defect in §5.3, and the survivors that still rest only on it (L4,
L6, L8) are marked at the point of use.

---

### L2. No entry runs two of the five enumerated identity-confound remedies

**The evidence.** The corpus holds five procedures for one problem, in three strands
([science-map](./science-map.md) §2): post-hoc linear erasure
([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)), confound
regression inside every cross-validation fold
([snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)),
a held-out generalization test across exemplars or modalities
([simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md),
[simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)),
training the decoder on a separate functional localizer
([mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)),
and tying decodability to behavioural read-out
([ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md)).
No entry runs two **of these five**.

**The headline was first written as "no entry runs two identity-confound remedies", and in that form
it is false.** Two entries run more than one procedure.
[snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
compares three confound-control procedures — post-hoc counterbalancing, plain confound regression and
confound regression inside every cross-validation fold — against a common simulation set and against
one empirical dataset, decoding gender from structural MRI while controlling for brain size; the
finding that the first two are biased in opposite directions *is* a head-to-head comparison, and it is
what makes the third recommendable. [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)
runs two interventions on the same 12 model-by-dataset pairs: closed-form LEACE erasure of the subject
axis, and ablation of the FOOOF aperiodic 1/f component, reporting both. So the corpus does contain
procedure-versus-procedure comparison. What it does not contain is a comparison that crosses the five
entries the science map enumerates — nobody has run LEACE erasure against cross-validated confound
regression, or either against a modality-generalization test, on one dataset and one set of folds.

**And the count of five was itself inflated.** One of the five,
[ritchie-2019-decoding-limits](../collection/candidate-datasets/ritchie-2019-decoding-limits/card.md),
is a philosophy-of-science analysis that runs no procedure on any data; its behavioural-read-out
criterion is a recommendation illustrated with somebody else's published study. "Five procedures, one
entry each, none compared" counted a non-runner as a runner. The defensible statement is four
implemented procedures plus one recommended one, and no comparison across them.

The consequence still holds and is the reason the gap matters: the enumerated remedies are not
ordered, so a project told to control for identity has several options and no evidence about which to
pick across the boundaries the science map draws.

**The scope check.** Genuine absence, with a bounded caveat. All five remedies live in strands the
corpus has, so this is not a partition error. No brief excludes confound methodology: strand A excludes
MEG, fNIRS and fMRI *models*, not confound-control methods, and strand D admits label-validity work
regardless of imaging modality — [mous-2019](../collection/candidate-datasets/mous-2019/card.md) is
MEG and admitted, [snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
is structural MRI and admitted ([scope-diagram](./scope-diagram.md) §2.1, §2.4, §7.2). **The bound:**
three of the five come from fMRI or MRI work, discovery ran outward from a seed set along the citation
graph, and [scope-diagram](./scope-diagram.md) §4 records that anything no post-2022 entry cites "was
outside the discovery route by construction". A head-to-head comparison of erasure against
cross-validated confound regression published in the neuroimaging methods literature and cited by no
EEG paper in this corpus would not have been reached. So: genuine for the EEG literature the corpus
reaches, undetermined for the methods literature beyond it.

**The falsifier.** One paper applying two of the five *enumerated* remedies to one dataset and
reporting both results — for instance LEACE erasure and cross-validated confound regression on the
same embeddings and the same folds. Note that the earlier, wider falsifier ("one paper applying two
confound-control procedures") has already fired twice, on Snoek and on Lin, which is what forced the
restatement above.

**The search record.** None.

### L4. What ocular-artifact removal costs in task accuracy is unmeasured

**The evidence.** Two cards on opposite sides of the artifact-versus-signal argument independently
name the same missing arm.
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
reports no "EEG with ocular components projected out" condition;
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
establishes that gaze carries the label and reports no neural decoding accuracy with the gaze
contribution regressed out, so "the residual cortical effect is undetermined". Around them,
[science-map](./science-map.md) §5 records the same discard with three different justifications and no
measurement anywhere: the models strand drops the channels as out of contract
([bendr-2021](../collection/eeg-models/bendr-2021/card.md)), the benchmark strand as protocol-prohibited
([bci-competition-iv-2a](../collection/datasets-benchmarks/bci-competition-iv-2a/card.md)'s EOG "must
not be used for classification", with no suite stating what it did), and the fusion strand argues both
sides. [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) relies
on ICA rather than a recorded ocular channel, which is exactly the case Mostert's authors call
"imperfect".

**The scope check.** Genuine absence, and one that rests **only** on the unsound disjunct of
[scope-diagram](./scope-diagram.md) §6 check 3: two cards state it about themselves and nothing else
supports it. After L7, that is a warning rather than a clearance. What keeps it standing is that the
two cards sit on *opposite* sides of the artifact-versus-signal argument, so the absence is not one
research programme's blind spot, and that [science-map](./science-map.md) §5 finds the discard
justified three different ways across three strands with no measurement attached to any of them. It
is still weaker than L10 and should be re-checked against a targeted search before Phase 5 builds on
it. One complication must also be recorded rather than smoothed: strand B's brief excluded
"camera-based or contactless physiology estimation" while six of its entries carry eye-tracking-derived
signal, a mismatch [scope-diagram](./scope-diagram.md) §7.1 filed as a defect and which was amended in
the same phase to record the exception actually in force, at eight entries. So the eye-tracking side of
this literature is present *by amendment*, not by original design, and its coverage was shaped by an
exclusion that was written and not honoured.

**The falsifier.** One study reporting decoding accuracy with and without ocular components projected
out, on the same data and the same split.

**The search record.** None.

### L5. No study compares a decoder built from EOG electrodes against a decoder built from eye tracking

**Restated.** This gap was first written as "no recording measures EOG electrodes and eye tracking on
the same trials", and in that form it is false about an entry already in the corpus.
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
records "Both vertical and horizontal electrooculogram (EOG) as well as electrocardiogram were obtained
to aid in the recognition of artifacts. All signals were sampled at 1200 Hz", alongside gaze position
and pupil dilation from an EyeLink 1000 at the same rate. Both instruments, the same trials, the same
sampling rate. The card previously denied this about its own source and was corrected during the
refutation pass. The gap is therefore not about instrumentation. It is about what nobody did with it.

**The evidence.** [multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §4.3 states
the fault line: every entry arguing that ocular activity is *signal* measures it with an eye tracker —
COLET ([wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md)),
eye-tracking glasses ([ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)),
an SMI tracker ([zheng-2018-emotionmeter](../collection/multimodal-biosignals/zheng-2018-emotionmeter/card.md)),
pupil size ([hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md))
— and the entries carrying electrooculography electrodes sit on the other side.
[rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
is the one entry that builds a decoder from EOG electrodes at all: four EOG channels on a BioSemi
ActiveTwo with placements on record, run through the same CSP pipeline as the EEG, and the weaker arm
in every condition. It has no eye tracker. Mostert has both instruments and builds a decoder from only
one of them: gaze x and y through a three-class classifier with 8-fold cross-validation, while the EOG
channels serve artifact recognition and never enter a decoding analysis. The cards state that an eye
tracker gives position and pupil diameter while EOG "gives a potential difference that mixes gaze angle
with blink and with the corneo-retinal standing potential", and that the two "overlap but are not
interchangeable". [science-map](./science-map.md) §13's `eog` row records "three levels of specificity,
one tag". **No entry reports a decoding result from both instruments on the same trials**, so the
corpus cannot say how much of a tracker-derived result an EOG derivation would recover.

**The scope check.** Genuine absence. Under the amended strand B brief both instruments are in scope
([scope-diagram](./scope-diagram.md) §7.1), and no card claims a two-instrument decoder comparison
exists anywhere. Not a partition: `channels.tsv`'s machine-readable channel type
([eeg-bids](../collection/datasets-benchmarks/eeg-bids/card.md)) records the electrode type and not the
instrument, so the format strand cannot hold the distinction either. Note that
[scope-diagram](./scope-diagram.md) §7.1 still lists Mostert as an entry whose "measurement here is
video eye tracking, not electrooculography"; that line is stale against the corrected card, and §7
below records it as a synthesis-layer item to close.

**The falsifier.** One study reporting an ocular-derived decoding result from electrooculography
electrodes and from a simultaneous eye tracker on the same trials.

**The search record.** None.

**Two substrates, and a note that belongs to §4.** Of the 14 carded recordings,
[strum-2018](../collection/candidate-datasets/strum-2018/card.md) carries both instruments — 2-channel
EOG on the amplifier and a custom head-mounted eye tracker with scene camera
([dataset-hierarchy](./dataset-hierarchy.md) §3.3). It is not the only object in the corpus that could
answer the question: Mostert's deposited recording carries both at 1200 Hz on the same trials, and the
data and analysis scripts are on record at the Donders repository. The head-mounting of STRUM's tracker
is a specification detail and does nothing to narrow the field; what narrows it is the modality, since
Mostert is MEG and STRUM is scalp EEG, where the corneo-retinal dipole projects more strongly.

### L6. No entry pairs a frozen EEG encoder with a frozen peripheral encoder

**The evidence.** [multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §7.5
enumerates four entries that speak to the configuration and states that none runs it:
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) is framed as "both a feature
extractor and an encoder for multimodal models" and "no multimodal experiment appears in the
evaluation"; [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md)
reports competitive linear probing whose figures did not survive extraction;
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
freezes pretrained backbones that are ImageNet-lineage image models rather than biosignal foundation
models; [ding-2025-cross-attention-fusion](../collection/multimodal-biosignals/ding-2025-cross-attention-fusion/card.md)
trains its branches. From the other side, the EEG checkpoints have no representation for a peripheral
channel at all: [bendr-2021](../collection/eeg-models/bendr-2021/card.md) drops "reference electrodes,
EOG and other auxiliary channels", and
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md)'s Sensor Encoder type vocabulary has
exactly three values, so "an ECG, EOG or respiration channel has no representation in the current
model". The one apparent exception is not one:
[biot-2023](../collection/eeg-models/biot-2023/card.md) pretrains across resting EEG, sleep EEG and
ECG and fine-tunes on any of them **one modality at a time**.

**The scope check.** Genuine absence, bounded. Fusion architectures are strand B's category 2 and
peripheral foundation models its category 1; both were collected, and both released peripheral
encoders are carded. **The bound:** [scope-diagram](./scope-diagram.md) §3.2 records that publisher
anti-bot barriers cost strand B's two review-shaped entries their reference lists, and that
"neither review produced a downstream entry in that strand" — a second-order incidental exclusion of
an unknown number of primary papers. One of those reviews,
[liu-eeg-multimodal-emotion-review](../collection/multimodal-biosignals/liu-eeg-multimodal-emotion-review/card.md),
has incomplete multimodal learning as an organising aspect and is called "the only pointer this strand
has into the literature that addresses it". The pointer could not be followed.

**The falsifier.** One paper bolting a head onto a frozen EEG checkpoint and a frozen ECG or PPG
checkpoint, reporting an EEG-only arm on the same split.

**The search record.** None, and one recorded discovery failure pointing the other way. This is a
second gap resting only on the unsound disjunct of §6 check 3 — four cards each declining the
configuration — and it has the same shape as L7, which that pattern got wrong. What distinguishes it
is that the blocking fact is on the *EEG* side and is structural rather than declarative: the
checkpoints have no channel type for a peripheral signal, which is a property of published input
contracts rather than an omission anyone reports.

### L8. Spoken versus written has never been decoded from EEG within subject

**The evidence.** Four entries bear on the contrast and none runs it.
[simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
presents spoken words, line drawings and written words to 20 participants at 60 electrodes, and its
card states the boundary explicitly: "the paper does *not* run a spoken-versus-written classifier",
its decoding target being semantic category within each modality.
[mous-2019](../collection/candidate-datasets/mous-2019/card.md) carries the exact contrast at scale
and manipulates it **between** subjects — 102 readers, 102 listeners — so its card records that "any
across-subject classifier trained on the contrast is separating two disjoint groups of people"; it is
also MEG, 275 axial gradiometers and no EEG at all.
[deniz-2019-modality-invariant-semantics](../collection/candidate-datasets/deniz-2019-modality-invariant-semantics/card.md)
and [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
are fMRI and abstract-only. The nearest published analogue in the benchmark layer is
[omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)'s two Broderick sets, named
by [dataset-hierarchy](./dataset-hierarchy.md) §2.7 as "the corpus's nearest published analogue to a
spoken-language contrast".

**The scope check.** Genuine absence, **bounded**. Strand D's category 3 and category 5 both target
exactly this contrast; the collection found the four entries above and no fifth.
**The bound:** forty-eight of OmniEEG-Bench's fifty-four datasets and eight of Brain4FMs's eighteen are
not named on their cards, because the per-dataset tables live in supplementary material and an
appendix ([scope-diagram](./scope-diagram.md) §3.1, [dataset-hierarchy](./dataset-hierarchy.md) §1).
A within-subject auditory-versus-visual language task could be sitting inside those 56 unnamed
recordings and this corpus would not see it. That is a resource limit with a named cause and a known
closing action.

**The falsifier.** One paper reporting within-subject EEG decoding of auditory versus visual language
presentation with a stated split. Recovering OmniEEG-Bench's supplementary tables 5 to 7 would either
close the gap or tighten it.

**The search record.** None ran on the contrast itself. This is the third survivor whose positive
support is a set of cards declining the contrast rather than a search for it, and the bound above is
what keeps that honest: the 56 unnamed recordings are the specific place a counterexample would hide.

### L9. No multi-person recording reports a measured cross-participant synchronization precision

**The evidence.** All four multi-person EEG recordings report none.
[boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) uses a custom hardware
trigger with post-hoc alignment against a filmed UTC clock and gives no numeric precision, which its
card flags as a real limit given that the dataset's own stated purpose includes quantifying
synchronization across participants;
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) uses manual triggers with no
measured offset or jitter; [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) reports
none for the four participants in a group; and
[strum-2018](../collection/candidate-datasets/strum-2018/card.md) reports none despite writing both
participants into one XDF file. The only measured numbers in the corpus are device-to-device, in
[lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) — 156 µs single-machine, 145 µs
networked, ~0.5 ms between jitter-corrected EEG and EMG streams — and that card declines the
extrapolation itself: "Whether two separately capped participants on two amplifiers achieve the same
sub-millisecond jitter is a reasonable extrapolation, not a published result."
[dataset-hierarchy](./dataset-hierarchy.md) §3.6 files all four under "never reported by the source".

**The scope check.** Genuine absence, and the strand's clearest *answerable* one — its own ontology
calls it "a specification gap that is answerable rather than unanswerable: the numbers exist for the
framework, they are absent from the datasets, and their absence is a reporting choice by the dataset
papers, not a property of the field"
([candidate-datasets-ontology](./candidate-datasets-ontology.md) §6.3). Not covered by the
hyperscanning exclusion: [scope-diagram](./scope-diagram.md) §1.1 excludes connectivity *methodology*
and states that "multi-person recordings remained in scope and are category 1", and the brief asked
for synchronization method and its measured precision by name.

**The falsifier.** One multi-person EEG data descriptor reporting a measured participant-to-participant
timing error as a number.

**The search record.** Partial. The seven category-1 queries ([scope-diagram](./scope-diagram.md) §3.4)
establish how few such datasets exist; none asked whether the existing ones report precision. The
absence is over a denominator of four, which is small, and that is a limit on the claim rather than a
strength of it.

### L10. The only open EEG dyadic releases are two small ones from one laboratory; every other-group multi-person release the sweeps returned is fNIRS or fMRI

**Restated, because the old headline contradicted its own evidence two paragraphs below itself.** The
gap was written as "no EEG dyadic dataset release", and the search record it cites names two.
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) is a two-person EEG recording
released on FigShare with the data under an explicit CC BY 4.0 grant, "no registration, no data use
agreement". [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md) is an open
FigShare download with no registration described, three simultaneously recorded participants per
session; its *article* is CC BY-NC-ND 4.0 and its **data licence is not stated in the paper**, which
is worth saying precisely because the two releases are not equally clean. Either way, open EEG dyadic
releases exist, and "none exists" was false on the corpus's own record.

What the search record actually supports is narrower and still worth stating: the open EEG dyadic
releases the sweeps found are **two small ones from a single laboratory** — Contreras-Vidal's mobile
brain-body imaging group at Houston, sharing a toolchain and a 28-EEG-plus-4-EOG configuration — at 2
and 10 participants, neither exceeding 28 channels; and every multi-person neuroimaging release from
any other group that the sweeps returned is fNIRS or fMRI. That is a claim about the composition and
concentration of what the field distributes, not about its emptiness, and it is the claim the queries
below can carry.

**The evidence.** Seven recorded queries, tabulated in [scope-diagram](./scope-diagram.md) §3.4 and
read in [candidate-datasets-ontology](./candidate-datasets-ontology.md) §6.4. Two `opencite` sweeps
returned 20 results each with zero dataset releases; PubMed `hyperscanning[Title] AND (dataset[Title]
OR data[Title])` returned 15 hits whose every dataset release is fNIRS or fMRI; PubMed
`EEG[Title] AND dataset[Title] AND (dyad*/dyadic/interpersonal/two-person)[Title]` returned **0 hits**;
a *Scientific Data*-restricted query returned exactly the two Contreras-Vidal group releases already
carded ([boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md),
[livewire-2024](../collection/candidate-datasets/livewire-2024/card.md)); OpenNeuro's GraphQL returned
0 edges for each of four keywords. The corpus's four multi-person EEG recordings are 2, 3, 4 and 2
simultaneous participants, two of them from one laboratory, and none of the three openly downloadable
ones exceeds 28 channels ([candidate-datasets-ontology](./candidate-datasets-ontology.md) §6.2).

**The scope check.** Genuine absence, and it is the corpus's only absence backed by a recorded null
search — but two of the seven returns must be discounted, and the index says so itself. First, the
OpenNeuro zeros mean "nothing tagged with that keyword", because
[openneuro-2021](../collection/candidate-datasets/openneuro-2021/card.md) records that
`DatasetSearchInput` has no free-text field, so whether the zero reflects the archive's holdings or its
tagging "cannot be distinguished from the interface". That is a resource limit inside an otherwise
genuine finding. Second, the `opencite` returns were not empty but the wrong kind of thing — reviews
and methods papers, most of which strand D's hyperscanning exclusion turns away
([scope-diagram](./scope-diagram.md) §1.1). What survives both discounts is the PubMed zero and the
fNIRS/fMRI composition of what does get released, which is a boundary of the field.

**The falsifier.** One published, downloadable EEG data descriptor with two or more simultaneously
recorded participants, more than ten pairs, and a stimulus-condition label, from a group other than
Contreras-Vidal's. The falsifier is stated at more than ten pairs and outside one laboratory precisely
because the unqualified version has already fired.

**The search record.** Yes — seven queries, two discounted, tabulated.

**And the sharpening.** [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is the
release the restated gap describes as missing: 56 participants as 28 pairs at 206 channels, from a
third group, an order of magnitude more people than any other multi-person recording in the corpus.
It is not in the search results because it is not distributed — `headit.ucsd.edu` no longer resolves,
the community index records "contact authors", and no registry sweep located a hosted copy. So what
the field is short of is not dyadic EEG data but *distributed, dense, other-group* dyadic EEG data,
and the corpus contains the object that would supply it.

---

## 2.1 The four retractions, and what they say about this review's method

Each of these was published above as a gap and is withdrawn. In every case the falsifier the gap
itself named was already satisfied by a card in the corpus, so nothing new had to be found; what was
missing was the check. That is the finding, and it is about the method rather than about the field.
The pattern is uniform: a card said the absence about itself, the scope check accepted that as
licensing a claim about the literature, and no one asked whether some *other* card ran the arm.

### L1 (retracted). What a session-wise holdout boundary is worth is measured

**What refuted it.** [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) runs
the same four foundation models and four supervised models on the same tasks under both its
multi-subject setting — trained on multiple subjects, tested on "distinct recording trials or
sessions of the same subject cohort" — and its cross-subject setting, and compares them directly:
"on SEED, the cross-subject performance of LaBraM, CBraMod, and EEGPT are lower than multi-subject
performance by 15%, 19%, and 7%, respectively. **Foundation models demonstrated superior
generalization when transferring across sessions than across subjects.**" That is the gap's own
weaker-but-decisive falsifier, verbatim: a suite publishing both rows for the same task and
attributing the difference to the boundary rather than pooling it into an average rank. L1 named the
falsifier and did not check whether the paper it cited had already fired it.

**What survives, and it is not a gap of the size claimed.** AdaBrain-Bench's held-out unit is
"sessions **or** trials", and the paper does not resolve which applies per dataset, so the 15/19/7
points cannot be attributed to the session boundary specifically rather than to the trial boundary.
And [moabb](../collection/datasets-benchmarks/moabb/card.md) genuinely implements no cross-session
evaluation: it runs within-session 5-fold cross-validation, averages across sessions where a dataset
has several, and names cross-session once as future work, "a task that is currently infeasible" given
how few multi-session datasets exist. So the field's most careful inference implementation does not
carry the boundary, and one suite that measures it does not disambiguate it. Those are real, and they
are a reporting-precision complaint, not an unmeasured quantity.

**Consequence elsewhere.** §4's treatment of L1 as "actionable but not on STRUM" is unaffected in its
substrate reasoning — STRUM is single-session and cannot test cross-session generalisation — but the
work it would do is now disambiguation on COG-BCI rather than a first measurement.

### L3 (retracted as stated). "Its downstream sets are not high-density" is false

**What refuted it.** [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) reports
downstream numbers on **269, 306 and 372 sensors** — MEG-MMI at 269 magnetometers, ASD74 at 306, and
SomatoMotor at 372 in the combined EEG-plus-MEG condition — in the same downstream table as its
19-to-64-channel EEG sets, and its appendix reports that latent-source models beat electrode-level
models on exactly those dense sets. The gap's own falsifier reads "one checkpoint reporting a
downstream number on a montage above 130 channels", and the card it cited two sentences earlier
contains three.

**A second error in the same gap, in the opposite direction.** The text described
[luna-2025](../collection/eeg-models/luna-2025/card.md) as evaluating on a high-density layout and
failing. SEED-V is **62 channels**. LUNA pretrains on recordings with 20, 22 and 29 channels, so
"vastly different, high-density layouts" in its discussion means denser than its own pretraining, not
dense in absolute terms. The quoted failure is real; the scale it is a failure at is roughly a third
of what the gap implied. LUNA's own authors say elsewhere that "research/clinical systems often employ
64–256 channels" and position that as future work, which is the honest reading.

**What survives, narrowed to a size the corpus supports.** No **scalp-EEG** checkpoint has a reported
downstream number above roughly 137 channels. BrainOmni's dense evaluations are MEG and EMEG; its
densest EEG downstream set is PhysioNet-MI at 64. The supported-channel inventory for the scalp-EEG
checkpoints is BIOT 18 fixed, EEGPT 58, LaBraM 137, CBraMod arbitrary via an input-conditioned channel
embedding ([adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md); LaBraM's figure
is contested at 136/137/128, [science-map](./science-map.md) §11), and
[reve-2025](../collection/eeg-models/reve-2025/card.md)'s corpus spans 396 unique electrode names on
mostly 10-5 layouts without a dense downstream number. On the data side, the densest recording any
carded checkpoint has been **evaluated on** is Grosse-Wentrup 2009 at 128 in
[moabb](../collection/datasets-benchmarks/moabb/card.md)'s table, followed by Chisco at 125 in
[brain4fms](../collection/datasets-benchmarks/brain4fms/card.md) and Things-EEG at 63
([dataset-hierarchy](./dataset-hierarchy.md) §7). STRUM at 206 is denser than all of them and is the
densest EEG layout in the corpus; the earlier text called Grosse-Wentrup "the densest recording
anywhere in the corpus", which contradicted STRUM eight sections later and is corrected here.

That residue keeps its **bound by §3 U5** — five of the six uncarded checkpoints are unknown on this
axis — and it is what A2 in §4 rests on. A2 is a smaller contribution than the retracted gap implied,
because dense evaluation is no longer unprecedented across modalities, only within scalp EEG.

### L7 (retracted as stated). Engineered peripheral features have been compared against learned ones

**What refuted it.** Two entries already in the corpus run the comparison.
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) benchmarks its frozen
pretrained encoder against "a random forest trained on statistical features extracted from the PPG
signal, including mean, median, maximum, minimum, and the 25th, 50th, and 75th percentiles", and
separately against a PPG-morphology feature baseline (sVRI, IPA, SQI, with and without demographics),
on the same subject-level splits and the same linear-probe protocol, reporting that PaPaGei "outperforms
the demographics + PPG baseline in 14 out of 18 tasks".
[angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
computes **53 ECG features via NeuroKit2** — the HRV vocabulary the Haque review enumerates, plus
statistical moments — and trains both classical classifiers on those features and VGG- and
ResNet-style encoders on the raw signals, under the identical 10-fold and leave-one-subject-out
schemes. The gap's falsifier asked for "a task metric from an engineered HRV or EDA feature set and
from a pretrained peripheral encoder's embeddings, on the same data and split"; PaPaGei satisfies it
on the pretrained side and Angkan on the cognitive-state side.

**Why the self-declarations were true and the gap was still false.** Both category-5 cards state the
absence accurately about themselves — Haque predates the peripheral-foundation-model literature,
NeuroKit2 is a library paper. Neither is in a position to know what PaPaGei did. This is the clearest
instance of the disjunct failure described in §2, and it is why that note exists.

**What survives.** No comparison of engineered peripheral features against a **pretrained** peripheral
encoder on a **cognitive-state** task **with an EEG arm on the same split**. PaPaGei is pretrained and
splits cleanly but its tasks are cardiovascular, sleep and wellbeing endpoints and it has no EEG arm;
Angkan has the cognitive-state task and the EEG arm but its learned side is trained from scratch on
the downstream data, not pretrained. The intersection is empty, and that intersection is what A6 in
§4 would occupy. **A6 keeps its experiment and loses its novelty claim**: it is a well-motivated arm
to run, no longer a first.

### L11 (retracted). The CBraMod held-out-corpus delta is in the corpus, and it is small

**What refuted it.** [cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) reports the
re-pretraining check twice, as matched pairs on identical evaluation data. Method, verbatim: "we
excluded TUEV from the pretraining process, re-pretrained a new instance of CBraMod, and subsequently
evaluated it on TUEV." The numbers are **TUEV 0.6659 ± 0.0124 excluded against 0.6671 ± 0.0107
included, a delta of +0.0012**, and **TUAB 0.8249 ± 0.0025 excluded against 0.8289 ± 0.0022 included,
a delta of +0.0040**. The gap's own falsifier named that quantity — "the magnitude of CBraMod's
re-pretraining delta" — and the card had it. An earlier version of the card mis-attributed 0.6671 to
the excluded run, which is what the original extraction propagated as "whether CBraMod's check reports
a delta is not on record".

**What the number means, stated carefully.** This is the corpus's only direct measurement of what
pretraining-corpus overlap with the evaluation set is worth, and it is 0.12 to 0.40 balanced-accuracy
points, inside one standard deviation in both cases. Both deltas favour the included run, so overlap
helps rather than harms, but by an amount neither experiment can resolve. Two limits on how far it
generalises: it is one architecture on two clinical corpora from the same hospital archive, and it
measures the *overlap* term only, not the broader distribution-shift term that a genuinely unlike
downstream dataset also carries.

**Consequence, carried into §6.2.** The observation that a suite has never partitioned its
leaderboard into "in the pretraining corpus" and "not in the pretraining corpus" remains true and is
worth a sentence somewhere; it is not a research gap, because the quantity that partition would
estimate has now been estimated directly and found near zero. More sharply for this project: §6.2
claimed STRUM's absence from every pretraining corpus as a genuine strength and named it a
contribution. On the only measurement of that quantity in the corpus, the strength is worth about a
third of a balanced-accuracy point. §6.2 is rewritten accordingly.

---

## 3. Rejected candidates: absences that the scope check showed are gaps in us

Each of these reads as a gap and is not one. Keeping them visible is the point of the exercise, and
each is labelled with the class [scope-diagram](./scope-diagram.md) §2 assigns.

**U1. "The corpus says nothing about how two simultaneously recorded brains are analysed together."**
— **Scope judgment**, and the single largest deliberate exclusion in the review. Hyperscanning
connectivity measures, inter-brain coupling and their critiques went out of scope when the
`team-neuroergonomics` strand was replaced by `candidate-datasets`
([scope-diagram](./scope-diagram.md) §1.1). The exclusion was encountered in practice and honoured:
the hyperscanning query returned 20 results and the works it turned away are named — Hamilton 2020,
Barraza et al. 2019, Hakim et al. 2023, Zamm et al. 2024, Carollo & Esposito 2024. The brief's remedy
is explicit and is a partition change: reopen it as a new strand, not by widening
`candidate-datasets`. **Any Phase 5 proposal to admit this material is a proposal to change the
partition**, and nothing in this document should be read as making that proposal.

**U2. "The corpus excludes social-neuroscience theory."** — **Neither.** No brief records such an
exclusion anywhere ([scope-diagram](./scope-diagram.md) §2.5). The nearest real boundaries are U1 and
strand A's two-entry cap on the theoretical-motivation line. Stating that the corpus excludes
social-neuroscience theory would be inventing a decision nobody recorded; stating that the corpus
covers it would be equally unsupported. This candidate is rejected because there is no basis in either
direction.

**U3. "No pretrained EEG model can ingest a non-EEG channel."** — **Partition, and false on the
facts.** Peripheral encoders and fusion are strand B's by design
([scope-diagram](./scope-diagram.md) §2.1), so looking for them in strand A is a filing error. And the
flat claim is wrong: [biot-2023](../collection/eeg-models/biot-2023/card.md) is pretrained on resting
EEG, sleep EEG **and** ECG, with an ECG lead owning a row in the same name vocabulary as an EEG
derivation. The supportable statement is the narrow one in L6 — no *combined input*, one modality at a
time.

**U4. "The corpus contains no cross-imaging-modality work, so nothing bears on transfer across
recording modalities."** — **Scope judgment, and false on the facts.** MEG, fNIRS and fMRI models are
excluded "except where a single paper covers EEG alongside them"
([scope-diagram](./scope-diagram.md) §2.1), and the exception did real work:
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) is EEG plus MEG with a
joint-pretraining ablation, [brainwave](../collection/eeg-models/brainwave/card.md) is EEG plus
intracranial EEG, [mous-2019](../collection/candidate-datasets/mous-2019/card.md) is MEG in strand D,
and [alexander-2019-cortical-waves](../collection/eeg-models/alexander-2019-cortical-waves/card.md) is
MEG and ECoG admitted by an authorized override ([scope-diagram](./scope-diagram.md) §7.2).

**U5. "No checkpoint does X" — in general.** — **Resource limit**, bounding every such claim in this
document. Six checkpoints that benchmark cards record as evaluated have no entry in `eeg-models`:
BFM, BrainBERT, MBrain, EEGMamba, NeuroGPT and NeuroLM
([scope-diagram](./scope-diagram.md) §3.3). Strand A's acceptance criteria wanted every one of them
carded. Two follow-on consequences are already on record: NeuroLM's parameter count is held at 169.60M
and 1.7B by two cards and cannot be adjudicated because no primary exists in the corpus, and NeuroGPT
is counted among the "12 distinct model families represented" while the strand holds no NeuroGPT
entry. **The L3 residue (§2.1) is stated over the carded set for this reason, and any Phase 5 sentence
of the form "no EEG foundation model does X" must carry the same bound or close it first.** L3's
retraction is a second, independent reason for the same caution: the sentence that failed there was
not blocked by an uncarded checkpoint at all, but by a carded one whose own table had already been
read into this corpus.

**U6. Facts absent because a retrieval failed.** — **Resource limit**, each with a named cause.
DEAP's distributed channel list and both DEAP's and AMIGOS's licence text, because `eecs.qmul.ac.uk`
returned HTTP 503 throughout retrieval over both protocols — and the DEAP case is the sharp one,
because the paper contradicts itself about whether an ECG channel exists and the object that would
settle it is the unreadable one ([deap-2012](../collection/candidate-datasets/deap-2012/card.md)).
TUAB's and TUEV's `_AAREADME` behind a registration wall, which is where patient-disjointness of the
field's most reported partition would be recorded. OmniEEG-Bench's 48 and Brain4FMs's 8 unnamed
datasets, in supplementary material. Both strand B reviews' reference lists, behind anti-bot barriers.
None of these is a fact about the field, and each is closable by re-retrieval.
[scope-diagram](./scope-diagram.md) §3.1, §3.2.

**U7. "Nobody estimates physiology from a camera without contact."** — **Scope judgment, vacuously
honoured.** Remote photoplethysmography and camera-based respiration remain excluded with no exception
under the amended strand B brief, and no entry in the corpus does it
([scope-diagram](./scope-diagram.md) §7.1). The absence is entirely ours.

**U8. "No released checkpoint of either modality carries a licence."** — **Genuine, but not a research
gap.** [science-map](./science-map.md) §10 establishes it across both model strands, with each card
recording the omission individually. It belongs in this section because it is a *project risk* rather
than an absence anyone could publish against: the terms under which the project may fine-tune and
redistribute any checkpoint it uses are unstated by every source in the corpus, and the one licence
stated for any released artefact in strand A
([adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md)'s MIT) covers benchmark
pipeline code rather than weights. Phase 5 should treat this as a legal precondition, not as a
direction.

---

## 4. Column three: the actionable subset, with a route for each

Seven routes are actionable by this project. Five of them close a surviving gap; two — A2 and A6 —
now rest on the narrowed residues of retracted gaps and are worth running for their own sake rather
than as firsts. The three surviving gaps that are not actionable here are recorded first, with why,
followed by what the retractions changed.

**L9 (cross-participant sync precision) is not actionable here.** The measurement matters for
cross-brain analysis, which is U1's excluded territory. STRUM's two participants sit in one
time-synchronized XDF file and its peripherals share the EEG amplifier, so no cross-participant
alignment is required for any of the three planned comparisons.

**L10 (open dyadic releases concentrated in one laboratory) is not actionable and does not need to
be.** STRUM is the dense, other-group release the restated gap describes as missing; what is missing
is its distribution, and that turns on the authors' response rather than on any research act.

**L4 (what ocular removal costs) is actionable and is A5** — with the warning of §2.1 attached, since
it is one of the three survivors resting only on self-declaration.

**What the retractions changed in this section.** L11 is withdrawn, and with it the claim that STRUM's
absence from every pretraining corpus is an advantage worth naming; the one measurement of that
quantity in the corpus puts it at 0.12 to 0.40 balanced-accuracy points (§2.1). L1 is withdrawn as a
first measurement and survives as a disambiguation task: AdaBrain-Bench's held-out unit is "sessions
or trials" and is not resolved per dataset, and MOABB implements no cross-session split at all. That
task is still not doable on STRUM, and for the reason originally given — STRUM is single-session by
design, "the overall experiment takes ca. 3.5 hours ... also to induce a moderate degree of fatigue",
so no cross-session generalisation is testable in it
([candidate-datasets-ontology](./candidate-datasets-ontology.md) §2.3). The substrate would be
[hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md): 29
participants, three sessions one week apart, open download from Zenodo with no registration, BIDS,
referential to a named Fpz, and the corpus's only recording with **measured** electrode coordinates —
a 3D head-and-cap scan at the start of each session, so between-session electrode displacement is
quantified rather than assumed. Two hazards to design around, both on the card: Cz is absent for
participants 1 through 9, so nine of 29 have a different channel set, and 29 participants is "still a
small subject pool for anything claiming subject-general transfer". STRUM does, however, carry a
*within*-session temporal boundary that the corpus's identity table has no row for and that STRUM's
own authors used — the 5-block structure and blockwise cross-validation (§6.0).

### The seven actionable routes

**A1 — L8, spoken versus written within subject.**
*Dataset:* STRUM, and no alternative. [mous-2019](../collection/candidate-datasets/mous-2019/card.md)
carries the contrast at four times the scale and cannot support it: the manipulation is between
subjects, so no holdout unit separates the label from subject identity, and it is MEG, which no EEG
checkpoint can ingest.
[simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)'s
recording is fully specified but is a study-own cohort with no released identity
([dataset-hierarchy](./dataset-hierarchy.md) §2.9).
*Method:* train the classifier on the auditory-verbal against visual-verbal cells and test it on the
auditory-non-verbal against visual-non-verbal cells. If it transfers, it is reading stimulus modality
rather than language — the diagnosis
[simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
reached by a different route and
[simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
proposes as the general procedure.
*What would have to be true:* the 2×2 must actually be balanced in the released data, which no source
states; the cells must be matched on stimulus duration, which the paper does not report and which
[mous-2019](../collection/candidate-datasets/mous-2019/card.md) shows costs an explicit per-word
formula to achieve; and the auditory-spread-in-time asymmetry must be handled, which is on record as
unaddressed ([candidate-datasets-ontology](./candidate-datasets-ontology.md) §3). None of the three is
established. Two further conditions were not visible before the full paper was read, and both are
developed in §6.3: the two visual cells sit on **different screens** — text comms left, satellite map
right — so the transfer test's ocular component changes sign between the training cells and the test
cells; and stimuli are presented over **loudspeakers** in a room seating both participants, so a
visual-verbal trial for one subject can co-occur with an audible auditory-verbal stimulus for the
other, which contaminates the visual cell of the label itself.

**A2 — the L3 residue, a scalp-EEG checkpoint above 137 channels.**
*What it is now worth:* dense downstream evaluation is not unprecedented —
[brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) reports numbers at 269, 306 and 372
sensors (§2.1). What has not been done is a scalp-EEG checkpoint above roughly 137 channels. A2 is
that, and it is a narrower claim than the retracted gap supported.
*Dataset:* STRUM at 206, the densest EEG layout in the corpus and 60% denser than the densest
recording any carded checkpoint has been evaluated on
([dataset-hierarchy](./dataset-hierarchy.md) §7).
*Method:* the checkpoint choice is forced and narrow.
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) is the **only** carded checkpoint whose
spatial mechanism admits 206 channels without a name lookup, a coordinate, or a selection step: its
asymmetric conditional positional encoding is a depthwise convolution over each patch's
channel-by-time neighbourhood, so an unfamiliar channel count needs no new positional parameters. The
coordinate-driven models could take an arbitrary layout but need a position per channel, and STRUM's
coordinates are **absent** — "the paper does not say whether individual electrode coordinates were
digitised per subject or whether a template layout is assumed", and "a template for a non-standard
high-density cap may not exist"
([candidate-datasets-ontology](./candidate-datasets-ontology.md) §4.4). The name-indexed models
require selection or interpolation down to their montage.
*What would have to be true:* CBraMod's flexibility must survive a **10.8-fold** increase over the 19
channels of the 10-20 system it was actually pretrained on (206 ÷ 19; the earlier text said nine-fold,
which was wrong), which its own card marks as "a property of
the encoding rather than something demonstrated at pretraining time"; and CBraMod must be fine-tuned
rather than frozen, because its own paper reports PhysioNet-MI falling 0.6417 → 0.3845 with the
backbone fixed and concludes the model "cannot currently serve as a fixed-parameter feature extractor".
*The fallback, and its cost:* STRUM's own section IV subsampled "the 205-channel EEG ... to a subset of
64 approximately equidistant channels", which is a precedent for selection and also discards the
property that makes A2 a contribution.

**A3 — L2, two of the five enumerated identity remedies on one dataset.**
*Dataset:* STRUM primarily, because the 2×2 makes the label vary **within** subject, which is exactly
the regime where [lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)
reports that erasing identity *improves* label decoding by 6 to 12 points. A cheaper first pass is
available on [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md), CC BY 4.0
and openly downloadable from Zenodo and OpenNeuro `ds003670`.
*Method:* run closed-form LEACE erasure of the subject axis and cross-validated confound regression on
the same embeddings and the same folds, and report both. That is the comparison no entry runs. Two
precedents exist for the *shape* of the experiment and neither crosses this pair:
[snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
compares three confound-control procedures on one dataset, and
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) runs LEACE and FOOOF
aperiodic ablation on the same 12 pairs (§2). Both are templates to copy rather than results to
duplicate.
*What would have to be true:* the subject axis must be linearly removable in the fine-tuned
representation, which Lin establishes in 12 of 12 model-by-dataset pairs but with one dataset per cell
of a 2×2 and three models differing along five design axes at once. And the confound-regression
procedure must be reconstructible, which the corpus cannot supply:
[snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md) is
abstract-only and "no implementation detail should be taken from this card". Closing that is a
re-retrieval, not research.

**A4 — L6, two frozen encoders.**
*Dataset:* STRUM is the only recording in the corpus carrying all three of the project's named
peripheral modalities, hardware-synchronous on one 24-bit BioSemi amplifier with the EEG, so no
cross-device alignment is required at all
([candidate-datasets-ontology](./candidate-datasets-ontology.md) §5.2).
[mous-2019](../collection/candidate-datasets/mous-2019/card.md) is "exactly the project's target set
minus respiration" but is MEG. [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md)
is the cheap open substrate: lead-I ECG and horizontal EOG on the same amplifier, ECG used as an
independent variable in the authors' own analysis, and a continuous behavioural label that "places it
outside the circularity trap this strand worries about".
*Method:* freeze an EEG checkpoint and freeze
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) or
[mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md), concatenate or
cross-attend, and report the EEG-only arm on the same split.
*What would have to be true:* the peripheral encoders' contracts must be satisfiable. PaPaGei is PPG
and STRUM has no PPG, so ECG-FM is the applicable one; it resamples to 500 Hz on 5-second segments,
which is "long relative to a stimulus-locked EEG epoch and short relative to reliable HRV estimation —
an awkward middle for either use". And the licence question of U8 applies to both.

**A5 — L4, what ocular removal costs.**
*Dataset:* STRUM's 2-channel EOG on the EEG amplifier.
*Method:* report the label decoding with and without ocular components projected out, on the same
split — the arm two cards on opposite sides both name as missing.
*Why the substrate is better than the corpus alone suggested:* STRUM's own authors already found the
effect on these data. Section V reports that "the highest-performing methods prominently depend on
artifactual EEG sources, specifically frontal patterns typical for eye activity for some subjects ...
and temporal-lobe patterns typical of muscle activity for some other subjects". So the removal cost
is not a speculative quantity on this recording; it is a quantity the dataset paper observed and did
not measure.
*What would have to be true, and the reason this is not a free win:* reading requires saccades and
listening does not, so a spoken-versus-written contrast produces systematic differential ocular
behaviour **by construction**
([mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)),
and the 2×2 does not subtract it, because gaze differs between reading and listening whether the
material is verbal or not ([candidate-datasets-ontology](./candidate-datasets-ontology.md) §3). So on
this label the removal cost and the confound magnitude are the same number. That makes the measurement
easier to obtain and harder to interpret, and the interpretation must be stated as a confound estimate
rather than as a cost. §6.3 adds the further complication that the 2×2's two visual cells sit on
different screens, which changes the sign of the horizontal-EOG component between them.

**A6 — the L7 residue, engineered against pretrained peripheral features on a cognitive-state task.**
*What it is now worth:* the comparison exists in two other forms already —
[papagei-2024](../collection/multimodal-biosignals/papagei-2024/card.md) against statistical and
morphology feature baselines on subject-level splits, and
[angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
with 53 NeuroKit2 ECG features against from-scratch raw encoders on identical splits (§2.1). **A6 keeps
its experiment and loses its novelty claim.** What is unoccupied is the intersection: engineered
features against a *pretrained* peripheral encoder, on a *cognitive-state* task, with an *EEG arm on
the same split*.
*Dataset:* [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) first, then
STRUM. GX is CC BY 4.0, openly downloadable, and its ECG is used as signal by its own authors; STRUM
adds respiration and is behind a request.
*Method:* the twelve recurring HRV indices
([haque-hrv-stress-review](../collection/multimodal-biosignals/haque-hrv-stress-review/card.md))
computed through [makowski-2021-neurokit2](../collection/multimodal-biosignals/makowski-2021-neurokit2/card.md),
against [mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md)
embeddings, one task, one split, with the EEG arm reported alongside. Angkan's 53-index list is the
precedent for how wide the engineered arm should be, and is wider than twelve.
*What would have to be true:* very little. This is the cheapest of the seven, the engineered space is
"small enough to compute exhaustively", and both sides are released. The binding risk is the window
mismatch of §6.3, which applies to whichever side wins.
*One hazard on the substrate:* GX's participant identifiers are not stable across repeats — one
participant appears as 22, 23 and 24 — so "a subject-wise split built naively on the identifier column
would leak".

**A7 — L5, decoders from EOG electrodes against decoders from eye tracking.**
*Dataset:* STRUM, and — this is new — not uniquely. Of the 14 carded recordings, STRUM is the one
carrying both electrooculography electrodes and an eye tracker
([dataset-hierarchy](./dataset-hierarchy.md) §3.3), but the tracker being head-mounted does no
narrowing work and should not be cited as though it did.
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
carries vertical and horizontal EOG electrodes and an EyeLink 1000 on the same trials at 1200 Hz, with
data and scripts deposited at the Donders repository, and could answer the same question — it simply
never built a decoder from the EOG side. Two reasons still favour STRUM: Mostert is MEG, where the
corneo-retinal dipole projects more weakly than onto scalp electrodes, and Mostert's task is
orientation working memory rather than a language contrast.
*Method:* run the same ocular decoder on the EOG derivation and on the tracker's gaze and pupil
channels, on the same trials, and report both. Mostert's deposit is the cheap open rehearsal for the
pipeline before STRUM arrives.
*What would have to be true:* the eye-tracker stream must be released and time-aligned with the
amplifier stream. STRUM records it, but the tracker is a separate device rather than an amplifier
channel, and no measured device offset is reported for it —
[lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) establishes that LSL "does not remove
the constant transport delay of a device; it makes that delay stable enough that a single pre-measured
constant can be subtracted. Any recording that did not measure its device offsets carries them
uncorrected."

### The dataset decision, stated against the alternatives

STRUM is the primary target for five of the seven routes (A1, A2, A4, A5, A7), the primary target with
an open fallback for A3, and the fallback rather than the first choice for A6. The case is not close
in either direction.

| candidate | why it can or cannot carry the project | source |
|---|---|---|
| **STRUM** | only recording with the 2×2, the three peripheral modalities hardware-synchronous, both ocular instruments, and 206 channels; and now the only one with a published modelling baseline and protocol on the same data (§6.1). Access by request with no published route, data licence unknown, coordinates absent, reference unstated, single-session, 28 pair-sessions with the exclusion arithmetic unresolved (§6.0) | [strum-2018](../collection/candidate-datasets/strum-2018/card.md) |
| MOUS | the exact contrast at 204 subjects, but between subjects and MEG-only — no EEG checkpoint can ingest it and no holdout unit separates label from identity | [mous-2019](../collection/candidate-datasets/mous-2019/card.md) |
| COG-BCI (Hinss) | the only measured coordinates and the only three-session design; open Zenodo, BIDS, named reference. No language contrast, no EOG, no respiration; 1 ECG channel bought by sacrificing TP9 | [hinss-2023-passive-bci](../collection/candidate-datasets/hinss-2023-passive-bci/card.md) |
| GX (TES) | CC BY 4.0, open, ECG and EOG on the amplifier and used as signal, continuous behavioural label, named CPz reference. 32 channels, 20 subjects, no language contrast, unstable participant IDs | [tes-eeg-ecg-2021](../collection/candidate-datasets/tes-eeg-ecg-2021/card.md) |
| Sleep-EDF | cheapest open substrate for probing the bipolar midpoint approximation; 2 channels, 100 Hz, no ECG, expert-scored labels with a stated circularity | [sleep-edfx](../collection/candidate-datasets/sleep-edfx/card.md) |
| DEAP / AMIGOS | printed-signed-scanned EULAs, host unreachable throughout retrieval, and DEAP's ECG presence contradictory in its own paper with the resolving document inaccessible — disqualifying for a peripheral comparison | [deap-2012](../collection/candidate-datasets/deap-2012/card.md), [amigos-2021](../collection/candidate-datasets/amigos-2021/card.md) |
| BOA / LiveWire | multi-person and open, but 10 and 2 participants, no ECG, no respiration; LiveWire's subject-wise split "has exactly two folds" | [boa-actors-2025](../collection/candidate-datasets/boa-actors-2025/card.md), [livewire-2024](../collection/candidate-datasets/livewire-2024/card.md) |
| TUH family | the field's substrate, but no cognitive, behavioural or stimulus label exists anywhere in it | [tuh-eeg-corpus](../collection/datasets-benchmarks/tuh-eeg-corpus/card.md) |

**The precondition nobody else can satisfy.** STRUM sits at the highest-friction rung of the access
ladder — request to the authors, no published route, `oa_status: closed`, no hosted copy found by any
registry sweep, and a data licence that is unknown rather than restrictive
([candidate-datasets-ontology](./candidate-datasets-ontology.md) §7.1). Every route above that depends
on STRUM depends first on that request succeeding, and on the cap layout or electrode coordinates
being obtainable in the same request, since A2 turns on them. Phase 5 should treat the data request
and the coordinate request as one action with a go/no-go outcome, and should have GX and COG-BCI as
the named fallback for A3 and A6.

---

## 5. What the corpus does not support

The protocol requires this as its own treatment, and it is the section most likely to be skipped, so
it is placed before the assessment that depends on it rather than after.

### 5.1 Claims this review cannot make, because the relevant entries are inaccessible

Each of these is a claim the review might be expected to make and must decline. The distinction
between "the source does not report it" and "the source reports it and we could not read it" is
preserved, because only the second is closable.

- **How much of a spoken-versus-written EEG classifier's accuracy is sensory.** The elimination
  argument — that if semantic representations are near-identical across modality then the classifier
  is separating the sensory channel — rests on two abstract-only cards.
  [deniz-2019-modality-invariant-semantics](../collection/candidate-datasets/deniz-2019-modality-invariant-semantics/card.md)
  records that "almost identical" is a qualitative abstract summary and that the residual difference
  "could be small and real, and this card cannot say how large it is".
  [simanova-2012-modality-independent](../collection/candidate-datasets/simanova-2012-modality-independent/card.md)
  records that the abstract does not say how large the modality-specific component is relative to the
  modality-independent one, "which is what would determine how much of a spoken-versus-written EEG
  classifier's accuracy is sensory". **The review can say the contrast is not semantic in the way its
  name suggests. It cannot say by how much, and any Phase 5 sentence that quantifies it is
  unsupported.**
- **What the empirical chance level is for any design in this project.**
  [combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
  is abstract-only and its tabulated levels as a function of sample size, class count,
  cross-validation parameters and classifier are "the part a user would actually apply" and are
  reported-but-unread. The corpus supports "the theoretical level is the wrong threshold at small n"
  and supports the remedy (a permutation null); it does not support any specific number.
- **How to implement the one unbiased confound-removal method.**
  [snoek-2019-confound-control](../collection/candidate-datasets/snoek-2019-confound-control/card.md)
  is abstract-only: "no implementation detail should be taken from this card". The recommendation is
  on record without a reproducible procedure attached.
- **Whether cardiac activity is downstream of the cortical state.** All three convergent-cross-mapping
  entries are inaccessible on their decisive quantity, and in all three the source reports it
  ([multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §5.3).
  [zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) reports no
  coefficients, no significance levels, and no control for the video stimulus driving both signals —
  which its card calls "the single most important control for a coupling claim of this kind" — and its
  detected direction may be biased by single-lead ECG reconstructing a cardiac attractor more cleanly
  than 32-channel EEG reconstructs a cortical one. **The mechanistic argument against comparison 3 is a
  prediction, not a measurement, and §6.3 treats it as such.**
- **How many fusion studies declined to run the physiology-only arm.** Four entries in strand B
  computed the comparison and the number did not reach the corpus
  ([multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §1.4); 18 of 25 entries have
  at least one decisive fact reported-but-unread. [scope-diagram](./scope-diagram.md) §3.1 states the
  rule directly: "A Phase 4 reader counting missing ablation arms must not count those four as evidence
  about the literature." This document does not.
- **Whether the field's most reported partition is patient-disjoint.**
  [tuab](../collection/datasets-benchmarks/tuab/card.md)'s naming thesis says the data "was divided
  into two sets" without asserting it, the parent archive averages 1.56 sessions per patient with one
  contributing 37, and the release's `_AAREADME` is behind a registration wall. Every foundation-model
  TUAB number in this corpus inherits that partition.
- **What most of the field's leaderboard rows were computed on.** Forty-eight of OmniEEG-Bench's 54
  and eight of Brain4FMs's 18 evaluation datasets have no identity in this corpus
  ([dataset-hierarchy](./dataset-hierarchy.md) §1, §5.2).

### 5.2 Questions where the corpus holds two entries pointing opposite ways and no basis to choose

- **Is ocular activity artifact or signal?** [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  and [rotaru-2024-auditory-attention-bias](../collection/multimodal-biosignals/rotaru-2024-auditory-attention-bias/card.md)
  against [wibirama-cognitive-load-eye-movement](../collection/multimodal-biosignals/wibirama-cognitive-load-eye-movement/card.md),
  [ahmad-2020-cognitive-load-framework](../collection/multimodal-biosignals/ahmad-2020-cognitive-load-framework/card.md)
  and [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md).
  This is not a live disagreement that will be settled by weighting, because **the instrument differs
  across the fault line**: every constructive entry builds its decoder from an eye tracker, and the
  only entry that builds one from EOG electrodes is on the other side. Mostert carries both
  instruments on the same trials and builds a decoder from only the tracker (L5, as restated), so even
  the one recording that could bridge the fault line does not. The corpus therefore cannot transfer
  the constructive result to an EOG derivation, and any project reasoning "eye tracking carries
  cognitive load, therefore EOG will help" is crossing a boundary the corpus does not license.
- **Does peripheral physiology add information beyond EEG?** Consistent with near-zero:
  [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  (+0.002), [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
  (not significant), and the EEG+ECG cell of
  [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  (+2.75, the smallest of its three pairings). Inconsistent:
  [salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) (+12.6) and
  [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
  (+11.6). Both inconsistent entries carry flags — three mutually inconsistent split descriptions in
  the first, an EEG stream attributed to two datasets that distribute no EEG in the second — and this
  document weights accordingly in §6.3. **That weighting is a judgment, not a finding.** The two
  entries have not been shown wrong; their denominators have been shown unverifiable, which is a
  different thing, and a reader who declines the weighting is left with five entries pointing two ways.
- **Does scale order the models?** Six measured observations say no; two say partly yes
  ([reve-2025](../collection/eeg-models/reve-2025/card.md) reports improvement with size while fitting
  no scaling law, [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) reports its tiny
  model beating its base model on MDD, which cuts against its own side). The six are better evidence,
  but one of the six rests on a parameter count the corpus holds at three orders of magnitude of
  spread ([science-map](./science-map.md) §11).
- **Which adaptation regime is primary?** Five suite positions, and no entry in the corpus converts
  between them ([datasets-benchmarks-ontology](./datasets-benchmarks-ontology.md) §2.2). Two suites
  demonstrate the reordering with *opposite signs* for different checkpoints. There is no basis in the
  corpus for choosing one regime as canonical, which is why §6.2 recommends reporting both rather than
  picking.
- **BENDR's parameter count**, at 0.39M, 3.97M, 157M, or unpublished by its own paper — load-bearing in
  two strands and unadjudicable.

### 5.3 Where this document's confidence outruns the entries behind it

Stated as self-criticism, because the previous two subsections are about the corpus and this one is
about the writing.

- **"The apparent value of peripheral physiology shrinks toward zero as evaluation gets stricter."**
  This is the load-bearing claim of §6.3 and it rests on **three** readable arms with stated splits:
  [azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)
  (n = 25, acoustic annoyance),
  [hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md)
  (n = 14, workload) and
  [angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
  (n = 21, driving load). Sixty participants across three studies, three different manipulations, none
  of them a stimulus-locked language contrast, and the strongest of the three (+0.002) is *gated* so
  that its headline is a mixture of the fused and EEG-only outputs rather than a fusion measurement.
  The direction is supported. The magnitude is not, and no quantity in §6.3 should be read as an
  effect-size estimate.
- **"A small supervised model frequently matches or beats a checkpoint."** Better supported — six
  entries, four of them third-party re-runs rather than quoted tables
  ([eeg-models-ontology](./eeg-models-ontology.md) §4.2) — but two qualifications hold. One of the six
  has its magnitude behind a paywall and only its sign on record
  ([sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md)),
  and the corpus's general caution applies to the rest: "there is always a concern that authors
  applying a method as a baseline may not be using it to its fullest potential", which
  [guetschel-2024-representation-learning-review](../collection/eeg-models/guetschel-2024-representation-learning-review/card.md)'s
  card marks as applying to every transfer number in that strand. Separately, LaBraM's twelve
  comparator appearances are a fact about the corpus's comparator graph, and several of them are one
  quoted number travelling along the copied-baseline chain rather than twelve measurements
  ([eeg-models-ontology](./eeg-models-ontology.md) §3.7).
- **"No checkpoint handles 206 channels."** Correctly, no *carded scalp-EEG* checkpoint has a reported
  downstream number above roughly 137. Five of the six uncarded ones are unknown on this axis (§3 U5),
  and BrainOmni does report 269, 306 and 372 in MEG and EMEG (§2.1). The strong form is not supported
  and is no longer used anywhere in this document.
- **"STRUM's 2×2 supplies the control."** This rests on one sentence of one paper, read once through
  institutional access, with no second reader and no released data to check it against. The paper
  contradicts itself on channel count (206 in section III, 205 in section IV) and on participants
  (56 as 28 pairs against a sex breakdown summing to 62), and does not restate the usable session
  count after "3 datasets were excluded"
  ([strum-2018](../collection/candidate-datasets/strum-2018/card.md)). §6.0 offers a reconciliation
  for the second and third of those, and it is a hypothesis, not a resolution. The 2×2 is a **design
  property as quoted**, not a validated one: whether its cells are balanced, and whether they are
  matched on stimulus duration, is unrecorded — and §6.3 now adds that two of its four cells differ in
  screen position and two in spatialisation, which is a design fact the 2×2's symmetry hides.
- **The pair-session argument in §6.0** is this document's own inference in its *unit* claim. No card
  treats the co-participant as a level of identity, and [science-map](./science-map.md) §2's table of
  six levels has no row for it. What is now quoted rather than inferred is the mechanism: stimuli are
  presented over loudspeakers in a room seating both participants and verbal responses are spoken
  aloud, so a cross-participant dependency exists in the recorded signal by design. The inference is
  the step from that to "therefore the split unit is the pair-session".
- **The scope-check rule this document inherited is unsound, and the retractions are its cost.**
  [scope-diagram](./scope-diagram.md) §6 check 3 licenses "property of the field" on the disjunct
  "a card states the absence about itself". A primary study reporting that it did not run arm X is
  evidence about that study. Seven of the original eleven gaps cleared on that disjunct; two of those
  seven were wrong (L5, L7), and a third (L1) was refuted by a paper the gap itself cited. The rule
  should be split: a self-declaration by a *review* whose scope is the field is field evidence; a
  self-declaration by a primary study is not, and needs a search or a survey of the other cards
  behind it. §7 records this as a synthesis-layer item. The three survivors still resting only on the
  weak disjunct are marked in place: L4, L6, L8.

---

## 6. The project's three planned comparisons, assessed

The review exists to test three comparisons. Each is assessed against the corpus, with what it would
and would not establish. Where the corpus says the plan is sound, that is said; where it says a
comparison would not establish what it appears to, that is said equally plainly.

### 6.0 One finding that conditions all three: the pair-session is the defensible holdout unit, and n=28 is not the reason to expect nothing

**This section previously argued that STRUM's n of about 28 puts every effect inside the confidence
interval, and that argument is withdrawn.** It was the most consequential conclusion in the document
and it was wrong in a way that would have discouraged the project from work its own dataset paper has
already shown to be feasible. What survives is the split-unit recommendation, which is a design
choice, not a power verdict. The two are separated below because conflating them was the original
error.

#### What survives: the pair-session as the defensible conservative unit

STRUM's 56 participants are 28 simultaneous pairs, each pair "recorded into a single time-synchronized
file in XDF format" ([strum-2018](../collection/candidate-datasets/strum-2018/card.md)). The original
argument for treating the pair as the unit was environmental — one room, one clock, one experimenter,
one time of day — which is the sort of reasoning that could be made about any two recordings made on
the same afternoon. Reading the full paper supplies a far better reason, and it is a dependency in the
recorded signal rather than in the ambient conditions.

**Stimuli are presented over loudspeakers in a room seating both participants, and verbal responses
are given by voice command.** The laboratory figure is captioned as showing "seats and associated
displays and loudspeakers for audio-visual stimulus presentation", the space "includes two identical
seats for the subjects", and the side tasks require subjects "to respond either via touch-screen
button press, or by voice command". So participant A's auditory stimuli are audible to participant B,
and A's spoken responses are audible to B. Half of the 2×2's stimulus deliveries and a self-paced
fraction of every response are physically shared between the two people in the room. That is a
cross-participant dependency in the data, not an inference about nuisance variables, and it is what
makes a subject-disjoint split that puts partner A in train and partner B in test something other than
disjoint.

The corpus's identity results then apply on top of it: segments of one subject resemble each other
([brookshire-2024-data-leakage](../collection/eeg-models/brookshire-2024-data-leakage/card.md)) and
dataset membership is decodable at AUROC 1.000 from frozen embeddings
([zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md)). **The
pair-session is therefore the defensible conservative unit — an arm to report, not a forced choice.**
A study reporting both a pair-disjoint and a subject-disjoint number, with the difference stated, is
strictly more informative than one that picks either, and the difference is itself the kind of
split-unit measurement L1's residue says the field under-reports.

#### A seventh and an eighth level of identity, one of which has a published precedent

[science-map](./science-map.md) §2's identity table has six rows: dataset, subject, session, segment,
trial, exemplar. STRUM's design instantiates two more.

- **The block.** The session "breaks down into a pseudo-random sequence of foreground activities ...
  organized into 5 blocks of 4-6 activities each, with 10-20 second long pauses between blocks", and
  STRUM's own authors cross-validated on it: "blockwise cross-validation (CV) matched to the 5-block
  structure of the session", with nested blockwise CV for hyperparameters. That is a within-session
  temporal boundary sitting between segment and session, it is the finest holdout unit in this design
  that is not a segment, and it is the only identity boundary in this project with a published
  protocol on this exact recording. It is the precedent to follow.
- **The co-recorded partner.** Coarser than subject, finer than dataset, with no row anywhere and no
  card treating it (§5.3).

#### What is dead: "n is 28, therefore the interval swallows every effect"

Three independent reasons, each checkable against the source, and then an empirical refutation that is
stronger than all three.

1. **Varoquaux exempts this design class by name.** The paper the argument leaned on says, in its own
   abstract: "The problems are particularly severe for methods development and inter-subject
   diagnostics studies. Conversely, **cognitive neuroscience studies are less impacted, as they often
   have access to higher sample sizes using multiple trials per subjects and multiple subjects**"
   ([varoquaux-2018-cross-validation-failure](../collection/datasets-benchmarks/varoquaux-2018-cross-validation-failure/card.md)).
   Its conclusion adds that "cognitive neuroscience MVPA studies often control these errors by
   performing a group-level statistical analysis", and its recommendations section spells out the
   design: cross-validate within subject, then "conclusions should be drawn from the group, and not at
   the subject level". STRUM is a multi-trial, multi-subject, within-subject cognitive design. It is
   the case the paper carves out, not the case it warns about.
2. **Which n the table refers to was never settled.** The document's own cited card records that for
   EEG, where one participant contributes thousands of epochs, which n Varoquaux's table indexes "is
   exactly the question ... and this paper does not settle it". Reading "n = 30" as "30 pair-sessions"
   rather than "30 observations" was a choice the source does not license.
3. **±15 bounds the wrong quantity.** Varoquaux's Table A1 gives the 5th-to-95th percentile of a
   binomial at 30 samples as 36.7–63.3 percent for a true accuracy of 50 percent, and 60.0–86.7 at 75
   percent — a bound on how far **one absolute accuracy** can sit from **its population value**. The
   project's question is a paired difference between two models evaluated on the same folds, where
   fold-sampling error is largely common to both arms and cancels in the difference. That is standard
   and it is why matched-pair testing exists; it is **not** something Varoquaux states, and the claim
   is marked here as this document's own reasoning rather than as a quotation. The nearest passage in
   the source runs the other way — his Kaggle example compares two scores on two *different* test sets
   and concludes the single-measurement error is smaller than the ±15 discrepancy by a factor of two —
   and his methods-development section does apply the absolute bar to method comparison, in the
   context of pipeline search across arbitrary choices. So reason 3 is the weakest of the three and is
   stated at that strength.

**And the empirical refutation, which is stronger than all three.** STRUM's own authors resolved a
12-point difference between methods on this exact recording. Section V reports response-error
detection with dual-spectral regularized logistic regression at **Az 0.75 ± 0.13**, HDCA at
**0.71 ± 0.10** and plain shrinkage LDA at **0.63 ± 0.07**, all significantly above the 0.5 chance
level, with "differences between DSLR the other two methods ... highly significant at p<0.01".
Task-performance estimation over 8-second windows reached 0.55 ± 0.06 to 0.61 ± 0.08, "above the
chance level of 0.5 at p<0.01", with the DLCSPcv-versus-CSP difference significant at p<0.05 — a
difference of about six points. The protocol was per-subject blockwise cross-validation matched to the
5-block session structure, with nested blockwise CV for hyperparameters and t-tests for significance.

One caveat, so this is not over-read. The authors' significance tests are across **subjects**, not
across pair-sessions, so their effective denominator is roughly 50 to 56 rather than 28, and a project
that adopts the pair-session unit of the previous subsection halves it. That weakens the argument by a
factor of two on n; it does not restore the retracted claim, because the retracted claim was that at
this scale "the interval swallows the effect" for differences of the size the corpus reports, and a
12-point difference at p<0.01 and a six-point difference at p<0.05 were both resolved here under
matched folds. **Model-versus-model differences of the size this project is looking for have been
detected on this recording.** The claim that they cannot be is refuted by the dataset paper.

#### The contradiction with §6.2, resolved

§6.2 argues that STRUM's within-subject label is precisely the regime where erasing subject identity
*improves* label decoding by 6 to 12 points
([lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md)). The retracted
version of this section argued that identity confounding is so severe here that the effective n
collapses to the number of pairs. Both cannot be right about how much identity confounding this design
carries, and the resolution is that they are about different things.

Identity variance in this design is **large in magnitude and orthogonal to the label in direction**.
Large: Lin measures frozen embeddings dominated by subject identity at 13–89× a random-Gaussian null
in 12 of 12 model-by-dataset pairs. Orthogonal: because every subject contributes trials in all four
cells of the 2×2, subject identity carries no information about the label, which is exactly why
erasing it helps rather than hurting — it removes variance that is pure nuisance. The original
argument slid from "identity is a large nuisance" to "the label is confounded with identity, so the
unit of analysis is the person". The second does not follow from the first in a within-subject design.
What the split unit governs is the **generalisation claim** — does this decoder work on a pair it has
never seen? — and not the effective sample size of the within-subject effect.

#### The exclusion arithmetic, and a reconciliation offered as a hypothesis

Two of STRUM's self-contradictions may be one contradiction. The paper reports "56 participants (28
pairs)" and "3 datasets were excluded due to interruptions in the experiment" in the same sentence,
and gives a sex breakdown of "13 f, 49 m" that sums to 62. Note that 62 − 56 = 6, which is exactly
three pairs. **If "datasets" means pair-sessions**, then 31 pairs were recruited and described
demographically, 3 pair-sessions were excluded, and the 56-participants-as-28-pairs figure is already
the post-exclusion count. Both apparent self-contradictions dissolve together, the usable n is 28
pair-sessions rather than "between 25 and 28", and the demographic line simply describes the recruited
cohort.

This is a hypothesis with an arithmetic coincidence behind it, not a finding. The paper does not say
what a "dataset" is, and the alternative — 28 pairs recorded, 3 excluded, 25 usable, with the sex
breakdown simply wrong — is equally consistent with the text. It is worth stating because it is
resolvable in the same author request that would obtain the data, and because the earlier "between 25
and 28" was presented with more confidence than the record supports in either direction.

#### What to do, stated positively

- **Report the pair-disjoint arm.** It is the conservative and defensible unit, justified by the
  loudspeaker and voice-response dependency rather than by ambient-condition reasoning. Report the
  subject-disjoint arm alongside it and state the difference.
- **Follow the authors' blockwise protocol.** Per-subject cross-validation matched to the 5-block
  structure, with nested blockwise CV for hyperparameters, is the precedent on this recording and
  makes any result directly comparable to Section V's numbers.
- **Do group-level inference on per-pair predictions.** Fit and evaluate within pair-session, then
  test the distribution of per-pair scores across pairs. That is Varoquaux's own recommendation for
  this design class, and it is strictly better than pooling trials across pairs into one accuracy.
- **Run a permutation null.** Not because n is fatal, but because it is cheap and correct.
  [combrisson-2015-chance-level](../collection/datasets-benchmarks/combrisson-2015-chance-level/card.md)
  establishes that classifying pure Gaussian noise reaches "decoding accuracies of up to 70% or higher
  in two-class decoding" at small sample sizes, and the corpus cannot supply the specific empirical
  chance level for any design here (§5.1).
- **Decide the generalisation claim in advance.**
  [kamrud-2021-data-partitioning](../collection/datasets-benchmarks/kamrud-2021-data-partitioning/card.md)
  permits the narrower protocol "if a cross-participant model is only intended to perform
  classification on the same population that it is training upon", provided the paper says so. A
  within-subject study on STRUM's 2×2 answers a narrower question and answers it better. That trade
  should be made deliberately at the start rather than discovered at the end.

### 6.1 Comparison 1 — a small supervised model trained from scratch on STRUM

**What it would establish, corrected.** This section previously said there is no published number on
STRUM, so the available claim is "we establish the first". That is false. **STRUM's dataset paper is
not only a descriptor: Section V reports a model comparison on these data.** Response-error detection
under per-subject blockwise cross-validation gives DSLR at Az 0.75 ± 0.13, HDCA at 0.71 ± 0.10 and
sLDA at 0.63 ± 0.07; task-performance estimation over 8-second windows gives 0.55 ± 0.06 (CSP) to
0.61 ± 0.08 (DLCSPcv), with Spec-CSP and FBCSP at 0.56 ± 0.07 and 0.59 ± 0.07. All are above chance at
p<0.01. The claim available is therefore a **comparison**, not an establishment, and that is better
for the project on two counts: there is an external sanity check on whether a number is reasonable,
and there is a published protocol to match.

Two qualifications keep this precise. The published baselines are on *different labels* — response
errors and high-versus-low task performance — so a first result on the modality-by-kind label is still
a first on that label. And Section IV's analyses ran on a 64-channel subsample at 128 Hz, so a
206-channel result is not directly comparable to them without reproducing the subsample. The absence
of a published number on the project's own label remains true; "no published number on STRUM" does
not.

**What it would not establish.** On its own, nothing about foundation-model transfer.

**The corpus's prediction, and the trap inside it.** The corpus expects this baseline to be strong.
[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) finds EEGNet's 72.29
beating every foundation model on Siena and Conformer's 73.84 doing so on HMC, with two of four
checkpoints level with or below the best supervised model in the macro-average;
[lee-2025-lbms-capable-yet](../collection/eeg-models/lee-2025-lbms-capable-yet/card.md) finds the best
fine-tuned foundation model at 0.745 against EEGNet's 0.731 with 2,394 trainable parameters;
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) finds classical
logistic regression at 0.847 against the best foundation-model tier at 0.755;
[zare-2026-stress-testing](../collection/eeg-models/zare-2026-stress-testing/card.md) finds classical
features beating frozen REVE by at least 12.7 points under every tested condition;
[sirca-2026-peft-motor-imagery](../collection/eeg-models/sirca-2026-peft-motor-imagery/card.md) finds
DeepConvNet highest at every calibration size.

**The Banville argument, which this section previously ran backwards.**
[banville-2021-self-supervised-eeg](../collection/eeg-models/banville-2021-self-supervised-eeg/card.md)
measured the self-supervised advantage as a curve: 22.8 points at one label per class, shrinking
monotonically, **inverting above roughly 10,000 examples per class**, after which full supervision
leads by 1.6 to 3.5 percent. The earlier text placed STRUM above that inversion point by reciting its
raw data volume — 269 channels per subject at 512 Hz over 3.5 hours, gigabytes per session hour — and
concluded that a null in comparison 2 would be uninterpretable. **Banville's axis is labelled examples
per class, not unlabelled data volume.** Gigabytes of recording say nothing about where a dataset sits
on it.

Counting the right quantity reverses the conclusion. STRUM's two verbal side tasks share a stimulus
set of "ca. 200 non-repeating statement sentences", so a subject sees on the order of **100 trials per
class** if the pool is divided between the auditory-verbal and visual-verbal tasks, or about 200 if
each task draws a set of that size. Pooled across 50 to 56 subjects, that is roughly **5,000 to 11,000
labelled examples per class** — straddling Banville's inversion point rather than sitting far above
it, and per subject two orders of magnitude below it, deep in the regime where pretraining helps most.
(The estimate is arithmetic on the card's sentence count and should be checked against the released
event stream; a lower figure is possible if some presentations are unusable.)

So the inference runs the other way. **A null in comparison 2 would be *more* informative, not less**:
STRUM is at or below the label volume where the corpus's own measurement says self-supervision should
still be winning, so a foundation model failing to beat a small supervised network here is a failure
in the regime most favourable to it. That is a result about transfer, not a result about dataset size.

One mapping detail matters for which arm the curve applies to. Banville's contrast is **frozen
features read out by a linear probe** against a fully trained supervised network — the card records
this explicitly as "not the like-for-like fine-tuning comparison that later work in this strand runs".
The inversion point therefore locates the **frozen probe** arm of comparison 2, not the fine-tuned
one. Since §6.2 already recommends reporting both, the curve gives the frozen arm a published
expectation to be measured against, and the fine-tuned arm has none.

[adabrain-bench-2025](../collection/eeg-models/adabrain-bench-2025/card.md) still reaches a related
explanation from the other direction, attributing its small margins to downstream datasets being large
enough that supervised learning suffices — but its datasets are TUAB, SHHS and Sleep-EDF-scale, and
STRUM is not.

**Verdict: sound, with one design change, and the change survives with its rationale reversed.** Report
comparison 1 as a **label-count curve** rather than at a single operating point, following Banville's
design. The reason is no longer "to check whether STRUM is above the inversion point and therefore
uninformative"; it is that the curve is the shape of the effect the project is testing, that STRUM's
label count sits in the interesting part of it, and that a curve locates the result on an axis the
corpus has already measured instead of leaving it as one point. It costs several training runs of a
small network and it remains the highest-value change to the plan in this document.

### 6.2 Comparison 2 — an off-the-shelf pretrained EEG model fine-tuned on STRUM

**One thing is genuinely in the project's favour. A second thing was claimed here and has to be
withdrawn.**

*Withdrawn: "STRUM is out of distribution for every checkpoint, and that is a contribution."* The
factual half is true — STRUM is in no archive the field pretrains from, has no hosted copy, and is
named in no pretraining corpus, against
[kuruppu-2025-critical-review](../collection/eeg-models/kuruppu-2025-critical-review/card.md)'s
finding that in four of ten reviewed studies the evaluation datasets were already used for
pretraining. What is withdrawn is the value placed on it. With L11 retracted, the corpus now contains
a direct measurement of what pretraining-corpus overlap is worth:
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) re-pretrained without TUEV and evaluated
on TUEV (0.6659 ± 0.0124 excluded against 0.6671 ± 0.0107 included, **+0.0012**), and did the same for
TUAB (0.8249 ± 0.0025 against 0.8289 ± 0.0022, **+0.0040**). Overlap is worth 0.12 to 0.40
balanced-accuracy points, inside one standard deviation in both cases. **A clean-overlap evaluation is
therefore worth about a third of a point, and naming it as a contribution would be overclaiming by
roughly the width of the noise.** It should be reported as a property of the design, in one sentence,
and not as a result.

Two limits on that retraction, so it is not over-applied. The CBraMod check is one architecture on two
corpora from the same hospital archive. And it bounds the *overlap* term only — how much a model gains
from having seen the evaluation corpus — not the *distribution-shift* term, which is how much a model
loses on data unlike anything it saw. STRUM carries both, and the second is large and unmeasured: 206
channels, a task battery, a dyadic room. Being unseen is worth nothing; being unlike is the risk.

*Retained: the label varies within subject.* That is the regime in which
[lin-2026-identity-trap](../collection/eeg-models/lin-2026-identity-trap/card.md) reports that erasing
subject identity *improves* label decoding by 6 to 12 points, so the identity remedy is both applicable
and predicted to help — which is not true of a between-subject design like
[mous-2019](../collection/candidate-datasets/mous-2019/card.md)'s.

**The ingestion problem is real, and its shape is precise.** At 206 channels STRUM sits far outside
every checkpoint's pretraining distribution. The name-indexed models cannot take it without selection
or interpolation. The coordinate-driven models can take an arbitrary layout **and need a coordinate per
channel** — which is exactly the field STRUM does not have, and for a non-standard high-density cap a
template may not exist. So the two properties compound in the one place they both matter
([dataset-hierarchy](./dataset-hierarchy.md) §7): *the checkpoints that could ingest 206 channels are
precisely the ones that need the field STRUM is missing.*
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) is the one way out, needing neither name
nor coordinate — and it pretrained on 19 channels, and its card marks the flexibility as a property of
the encoding rather than something demonstrated. That is a real risk and it is the substance of A2.

**What comparison 2 would establish.** That *this checkpoint, under this adaptation regime, on this
split* beats or does not beat comparison 1 on STRUM.

**What it would not establish, and this is the plain statement the brief asks for.** It would not
establish that pretrained EEG models transfer to this setting, for three reasons the corpus supplies
rather than this document inventing.

1. **The regime reorders the models.** [omnieeg-bench](../collection/datasets-benchmarks/omnieeg-bench/card.md)
   runs both regimes on ten checkpoints and 54 datasets and reports that "the model rankings change
   substantially"; [adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md) finds the
   same dependence with the *opposite* sign for a different checkpoint, EEGPT rising from 25.81 under
   full fine-tuning to 47.89 under linear probing on BCI-IV-2A while CBraMod falls from 47.71 to 32.32.
   A result at one regime is one point on an axis the corpus has demonstrated is not monotone.
2. **The checkpoint is not a proxy for the class.** Scale does not order the models
   ([eeg-models-ontology](./eeg-models-ontology.md) §2.5), the protocol reorders them, and
   [brainomni-2025](../collection/eeg-models/brainomni-2025/card.md) shows one model frozen beating
   another fine-tuned. One checkpoint's result generalizes to one checkpoint.
3. **The effect to be detected is small relative to the field's own margins, though not — per §6.0 —
   undetectable.** In AdaBrain-Bench's full cross-subject table the per-dataset margin between the
   best foundation model and the best supervised model, in balanced accuracy, runs from **−0.08**
   (Sleep-EDF: CBraMod 69.47 against ST-Transformer 69.55) to **+15.00** (EEGMAT: CBraMod 88.89
   against Conformer 73.89), with a median of a few points
   ([adabrain-bench](../collection/datasets-benchmarks/adabrain-bench/card.md), Table 2; the range is
   computed from that table rather than quoted from the text, and both endpoints are stated here so
   the derivation is checkable). A project designed to detect a few points needs the matched-pair
   protocol of §6.0 and cannot rely on eyeballing two absolute accuracies.

**What would have to change.** Report **both** the frozen probe and the fine-tuned number. Only eight
of 22 entries in strand A report both ([eeg-models-ontology](./eeg-models-ontology.md) §3.4), so doing
so costs one extra training configuration and puts the project above the field's median reporting
standard; and per §6.1, the frozen arm is the one Banville's label-count curve gives an expectation
for. Run at least two checkpoints with different spatial mechanisms, so that a null is attributable
to transfer rather than to one model's channel contract. Report the pair-session-disjoint arm and the
subject-disjoint arm, on the authors' blockwise protocol, with group-level inference over per-pair
scores and a permutation null (§6.0).

**Verdict: sound in premise, conditional in execution, and with one claimed strength withdrawn.** The
comparison is worth running. Its out-of-distribution property is now measured to be worth about a
third of a balanced-accuracy point and should not be sold as a contribution. What is genuinely in its
favour is the label geometry: within-subject variation, an identity remedy that is predicted to help
rather than hurt, and a label count that sits in the part of Banville's curve where pretraining is
supposed to win. Stated as "we fine-tuned checkpoint X and it beat a from-scratch baseline", it would
claim considerably more than it establishes.

### 6.3 Comparison 3 — the fine-tuned model plus peripheral physiology

This is the comparison the corpus says would not establish what it appears to. The case was rebuilt
after the refutation pass: one of its two legs — that the effect is too small to detect at this n —
is withdrawn with §6.0, and the other, that the channels most likely to show a gain would show it for
the wrong reason, is now much stronger, because STRUM's own authors observed the mechanism operating
on these data and because the 2×2 control has a design flaw the earlier reading did not see.

**The premise is sound at the specification level, and the card says so.** STRUM carries 2-channel
ECG, 2-channel EOG and a 16-channel respiration belt, all on the same 24-bit BioSemi amplifier as the
EEG — hardware-synchronous, so no cross-device alignment is required at all, which is a stronger
guarantee than anything the multi-device recordings in the corpus can offer. It is the only recording
in the corpus carrying all three of the project's named modalities. The card's own words:
"The third comparison's premise is sound."

**Four findings say the effect it would measure is close to zero, and the fourth — the temporal-scale
mismatch — is the one that is structural rather than statistical.**

*The gain shrinks toward zero as evaluation gets stricter.* The three entries whose split geometry is
stated and either subject-disjoint or designed against inflation report +5.84 / +6.21, +0.002, and a
difference their own authors call not significant. The two double-digit gains in the corpus are the two
whose denominators the cards flag as unverifiable:
[salam-eeg-ecg-stress](../collection/multimodal-biosignals/salam-eeg-ecg-stress/card.md) describes its
split three mutually inconsistent ways, and
[kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)
attributes its EEG stream to WESAD and CASE, neither of which distributes EEG at all — and since the
EEG-only arm is the denominator of the claimed gain, "the gain cannot be trusted either".
[multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §2.1. Per §5.3, this is a
direction, not a magnitude.

*The split protocol costs more than the modalities buy, measured on the same data.*
[angkan-2024-invehicle-cognitive-load](../collection/multimodal-biosignals/angkan-2024-invehicle-cognitive-load/card.md)
holds its four-modality input fixed and moves only the protocol: 7.74 and 13.1 points lost, each larger
than the entire EEG-to-all-four gain under the harder protocol. Its card states the consequence
directly: "any project reporting a fusion gain under record-wise folds is reporting a number smaller
than its own split-protocol artifact."

*The smallest gain in the corpus is not even a gain.*
[azad-2025-construction-noise](../collection/multimodal-biosignals/azad-2025-construction-noise/card.md)'s
+0.002 was produced under a per-fold gate: "fusion was used on the test set only if it outperformed EEG
in terms of both accuracy and F1 on the fusion-validation subset; otherwise, predictions defaulted to
EEG." The headline is a mixture of the fused and the EEG-only model's outputs and the paper does not
report how often the gate fired. Its card's reading is the one that matters: "a system that has to gate
its own fusion behind a per-fold check is a system whose designers observed that fusion sometimes
hurts." This is also the protocol the strand names as the one this project should copy.

*The time scales do not meet, and this one is structural rather than statistical.* The peripheral
integration window is 5 to 60 seconds; a stimulus-locked EEG epoch is 2 to 4. Eight entries state a
window and none reconciles the two
([multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §8.3).
[wang-2025-sedation-non-eeg](../collection/multimodal-biosignals/wang-2025-sedation-non-eeg/card.md) is
the only entry that sweeps it: 2 s to 20 s buys about 0.012 AUROC, and its card records that "a 20 s
window cannot resolve a stimulus-locked contrast at all".
[mckeen-2025-ecg-fm](../collection/multimodal-biosignals/mckeen-2025-ecg-fm/card.md)'s 5 s is "an
awkward middle for either use". STRUM's label is stimulus-locked: a stimulus sequence with a query
about the preceding, no-longer-displayed stimulus. **So HRV and the respiration belt are at the wrong
temporal scale for the planned label by construction**, and this is not a tuning problem.

**The respiration belt specifically — STRUM's most distinctive peripheral asset — has one readable arm
in the corpus and it is a null.** `eeg`+`resp` appears in 4 of 25 entries; three carry no accessible
EEG-versus-combined number
([multimodal-biosignals-ontology](./multimodal-biosignals-ontology.md) §6.1). The one that does is
[hogervorst-2014-workload-comparison](../collection/multimodal-biosignals/hogervorst-2014-workload-comparison/card.md),
where respiration frequency at 69% is one of only two non-EEG variables exceeding the chance level, in
the study that found no significant fusion gain, tried both feature-level and decision-level fusion,
and is the **one entry in the strand that held visual input constant** — which is to say, the one entry
that removed the confound is the one that found no gain.

**The ocular channel is the sharpest trap, and it must be stated without softening.** Reading requires
saccades and listening does not, so a spoken-versus-written contrast produces systematic differential
ocular behaviour by construction. **Adding EOG to a spoken-versus-written classifier and reporting the
gain would be measuring the confound and calling it a result.** The corpus cannot borrow the
constructive eye-tracking results to argue the other way either, because every constructive decoder in
it was built from a tracker and STRUM's channel is an EOG derivation (L5, §5.2).

**And on this recording the trap is not hypothetical. Its authors walked into it.** Section V of the
dataset paper reports, of the best response-error detectors: "Of note, the highest-performing methods
prominently depend on artifactual EEG sources, specifically frontal patterns typical for eye activity
for some subjects ... and temporal-lobe patterns typical of muscle activity for some other subjects."
The discussion generalises it: "the complexity of the STRUM task holds potential pitfalls, such as,
for instance, artifacts that may be correlated with user state, and which may be mistaken for brain
signatures". The contrast the same section draws is instructive — the task-performance models, which
are slow and oscillatory rather than stimulus-locked, rest instead on "spatial patterns localizable to
neocortical locations", occipital alpha and frontal beta. So on this dataset, the stimulus-locked
label class is the one that recruited eye activity and the slow label class is the one that did not.
That is an on-substrate observation, from the people who collected the data, and it is stronger
evidence for the ocular risk here than anything the fusion strand supplies.

**The verdict and the remedy contradicted each other; here is the position that holds.** This section
previously said "the 2×2 does not rescue it" and then prescribed the 2×2 transfer test as the remedy.
Both cannot stand. The defensible position: **the 2×2 diagnoses the ocular confound; it does not
subtract it.** Subtraction would require the non-verbal cells to carry the same ocular behaviour as
the verbal ones, so that the difference removed it, and they do not — gaze differs between reading and
listening whether the material is verbal or not
([candidate-datasets-ontology](./candidate-datasets-ontology.md) §3). What the transfer test does is
tell you *whether* a classifier trained on the verbal cells is reading sensory modality rather than
language. That is a diagnosis, it is worth having, and it is what A1 and A5 are for. It is not a
correction.

**A design fact that breaks the diagnostic as currently specified.** STRUM's two visual side tasks are
on **different screens**. The laboratory description places "a comm chatter task (large black text
message display to the left) on the left screen, and a satellite map task (right overhead view ...)"
on the right, across three vertically mounted 24-inch monitors per seat. So the visual-verbal cell is
a left-gaze task and the visual-non-verbal cell is a right-gaze task. A classifier trained on
auditory-verbal against visual-verbal learns, among other things, "gaze left". Tested on
auditory-non-verbal against visual-non-verbal, the visual cell now demands "gaze right", and the
horizontal-EOG component of the decision function **carries the opposite sign**. Such a classifier can
transfer at chance or below while being maximally ocular — and the protocol as written reads "does not
transfer" as "not ocular". **The diagnostic can return exactly the wrong answer, and it returns it in
the case the project most needs to detect.**

The auditory cells are asymmetric in a matching way. The auditory-non-verbal task presents sounds
"from one of three directions (left, right, back)" and queries the direction; the auditory-verbal task
presents pre-recorded sentences over the loudspeakers with no spatialisation reported. So one auditory
cell invites orienting behaviour and the other does not, and the two auditory cells are not
interchangeable as a control for each other any more than the two visual cells are.

**What a corrected design would need.** At minimum: (i) sign-invariant ocular features — magnitude of
horizontal deflection, saccade rate, blink rate — rather than signed horizontal EOG, so that a
left-gaze and a right-gaze task are not opposites; (ii) transfer evaluated in **both** directions, and
with the classifier's weights inspected, rather than accepting a chance-level transfer as evidence of
no ocular content; (iii) an explicit gaze-direction covariate per cell, which the head-mounted tracker
supplies directly and A7 would build; (iv) if a within-modality control is wanted, the natural-visual
"Curbside Items" task, which plays out in the *centre* viewport, as a third visual cell whose gaze
geometry differs from both side screens; and (v) reporting whether the ocular decoder is above chance
on each cell pair separately, since a single transfer number cannot distinguish "no ocular content"
from "ocular content with inverted sign".

**A second, unaddressed threat to the label itself, from the same paragraph of the paper.** Stimuli
are presented over loudspeakers in a room seating both participants. The paper's within-subject
concurrency rule prevents ambiguity between one subject's own side tasks — "a stimulus is not
presented when it falls into a time window during which an ambiguity with another task would arise" —
but no such rule exists across the two participants, whose side tasks run on independent pseudo-random
schedules. **So a labelled visual-verbal trial for subject A can co-occur with subject B's audible
auditory-verbal stimulus, and with B's spoken responses.** The "visual" cell of the label is therefore
not purely visual for an unknown fraction of trials, in a direction that specifically blurs the
auditory-versus-visual contrast the project intends to decode. This is checkable in the event stream
before any modelling, and it should be: the two participants' event timelines are in the same XDF
file, so the co-occurrence rate can be computed exactly and contaminated trials can be excluded or
modelled. No source in the corpus raises this, and it is a condition on A1 as much as on comparison 3.

**The mechanistic prediction, marked as a prediction.**
[zeng-brain-heart-ccm](../collection/multimodal-biosignals/zeng-brain-heart-ccm/card.md) reports
descending cortical-to-cardiac coupling as "stronger, more sustained, and spatially focused" than
ascending, which if true makes a cardiac channel closer to a noisy copy of what the encoder already has
than to a new source. Per §5.1 this entry reports no coefficients, no significance levels and no
shared-stimulus control, so it is consistent with the fusion nulls rather than evidence for them.

**Verdict: this comparison, as planned, would not establish what it appears to — but for reasons of
construct validity rather than of power.** The power argument this verdict previously rested on is
withdrawn with §6.0: an effect of a few points is detectable at this n under a matched-pair protocol,
and STRUM's own authors detected twelve. What stands is that the two channels most likely to produce a
visible gain would produce it for the wrong reason. EOG would produce it through the
reading-versus-listening confound, which the dataset's own authors already observed contaminating
their best models on these data, and which the 2×2 diagnoses rather than removes — and diagnoses
unreliably, because of the screen geometry above. HRV and the respiration belt would be read at a
5-to-60-second window against a stimulus-locked label they cannot resolve. A gain measured under those
conditions is not a measurement of what peripheral physiology adds.

**What would have to change, and it is a change of question rather than of method.** Run comparison 3
as a **falsification** rather than as a measurement of added value:

- Report the physiology-only arm. Only four entries in the whole corpus run three arms on one split,
  and in two of those the peripheral arm sits at or below a trivial baseline. A physiology-only floor
  on STRUM would be a contribution on its own and costs one extra model.
- Test the ocular gain against the non-verbal cells — **with the corrections above**, since the
  uncorrected version of this test can read a maximally ocular classifier as non-ocular. If a
  sign-invariant ocular decoder helps on both cell pairs, the gain is ocular behaviour tracking the
  sensory channel, not physiology informing a language contrast. That is A5 and A7, and it converts
  the trap into the finding.
- Audit the cross-participant audio contamination of the visual-verbal cell before anything else. It
  is a query over the event stream, it costs nothing, and if the rate is high it changes what the
  label means for every comparison in this document.
- Report engineered features alongside learned ones (A6), noting per §2.1 that this arm is
  well-motivated rather than novel. The engineered space is a dozen recurring indices, or
  fifty-three in Angkan's implementation, and omitting it is in the corpus's own words hard to
  justify.
- Do not run HRV or respiration against the stimulus-locked label. Run them against a label that lives
  at their time scale — STRUM's session was designed to induce "a moderate degree of fatigue" over
  3.5 hours, which is a slow within-session covariate no other entry in the candidate strand designs
  for, and which is the right temporal object for a 5-to-60-second peripheral window. The dataset's
  own task-performance analysis is exactly such a label, it is published with numbers to compare
  against, and it is the one label class Section V found resting on cortical rather than artifactual
  sources.

That last point is the one place where the corpus turns a defect of the plan into a better study, and
it is now stronger than when it was written: the slow label is not merely the right temporal object
for the peripheral window, it is the label STRUM's own authors found to be least ocular. The project's
peripheral inventory is genuinely exceptional; the planned label is the wrong thing to spend it on.

---

## 7. What this document needed from the synthesis layer and could not find

Recorded because the layer below keeps moving and these are the specific holes a Phase 5 reader or a
corpus revision should close.

- **Two levels of identity the table has no row for.** [science-map](./science-map.md) §2 lists six —
  dataset, subject, session, segment, trial, exemplar — and STRUM's design instantiates two more. The
  **block** is a within-session temporal boundary between segment and session; STRUM organises its
  session into "5 blocks of 4-6 activities each" and its authors cross-validated on exactly that
  boundary, so this level has a published protocol behind it and belongs in the table. The
  **co-recorded partner** sits between subject and dataset and has no card at all; §6.0's use of it is
  this document's inference, though the loudspeaker and voice-response dependency that motivates it is
  now quoted rather than inferred.
- **The scope check's self-declaration disjunct.** [scope-diagram](./scope-diagram.md) §6 check 3
  licenses "property of the field" on a card stating an absence about itself, without distinguishing a
  review that surveyed the field from a primary study reporting what it did not run. Four retractions
  in §2.1 are the cost. The check should be split, and any Phase 4 or 5 absence resting on the weak
  disjunct should be re-derived from a survey of the other cards or from a search.
- **A stale line in the scope diagram.** [scope-diagram](./scope-diagram.md) §7.1 lists
  [mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
  among the entries whose "measurement here is video eye tracking, not electrooculography". The
  corrected card records both instruments on the same trials at 1200 Hz. The camera-exclusion defect
  §7.1 files is unaffected in substance — the entry does carry video eye tracking — but the count and
  the framing should be revisited.
- **STRUM's usable session count.** "3 datasets were excluded due to interruptions" and the paper does
  not restate the surviving figure. §6.0 offers a reconciliation — 13 f + 49 m = 62, 62 − 56 = 6 =
  three pairs, so 28 may already be the post-exclusion count — and it is a hypothesis. No document in
  the corpus settles what a "dataset" is in that sentence, and the author request is the way to close
  it.
- **Whether the reference reader reads the project's target format.**
  [mne-python](../collection/datasets-benchmarks/mne-python/card.md) is recorded as reading BTI/4D,
  KIT, EDF, Biosemi BDF, BrainVision and FIF natively, reaching BIDS through MNE-BIDS, and explicitly
  *not* reading GDF. XDF appears on neither list, and
  [strum-2018](../collection/candidate-datasets/strum-2018/card.md) is XDF.
  [lsl-2024](../collection/candidate-datasets/lsl-2024/card.md) documents the toolchain that writes it.
  **The corpus does not record whether the field's reference reader can open the project's target
  file format**, which is a first-day blocker and a one-line check.
- **No expected effect size for a within-subject sensory-modality contrast in EEG.** A power
  calculation for §6.0 needs one and no entry supplies it.
  [simanova-2010-eeg-object-categories](../collection/candidate-datasets/simanova-2010-eeg-object-categories/card.md)
  gives 0.79 for semantic category within modality, which is a different contrast. STRUM's own Section
  V now supplies the nearest thing — Az 0.75 ± 0.13 for response errors and 0.55 to 0.61 for task
  performance on these data under blockwise CV — but on different labels, so it bounds what this
  recording yields rather than what this contrast yields.
- **The labelled-trial count per class.** §6.1's Banville argument needs it and derives it
  arithmetically from "ca. 200 non-repeating statement sentences". No document in the corpus states
  trials per condition per subject, and the released event stream is the only thing that would.
- **No compute or cost figure for fine-tuning any EEG checkpoint.** The corpus's only cost accounting
  is [kumar-2026-attention-eeg-ecg-stress](../collection/multimodal-biosignals/kumar-2026-attention-eeg-ecg-stress/card.md)'s
  fusion overhead, so whether comparison 2 is feasible on the project's hardware is unassessable from
  the corpus. Against the memory constraint the project already records, that is a real gap in the
  planning inputs.
- ~~**Whether CBraMod's held-out-corpus re-pretraining check reports a delta.**~~ **Closed.** The
  card reports it twice: TUEV +0.0012 and TUAB +0.0040 (§2.1).
  [dataset-hierarchy](./dataset-hierarchy.md) §4.1 still describes the check without its magnitude and
  should be updated.

---

## 8. Provenance

Every claim above is grounded in a card, a Phase 3 synthesis document, or a brief's recorded scope
decision. Where this document reasons beyond its sources — §6.0's pair-session *unit* claim and its
common-mode-cancellation argument, §6.1's per-class trial arithmetic, §6.3's screen-geometry and
cross-participant-audio inferences, §4's dataset recommendations, and the weighting of the two flagged
fusion entries in §5.2 — that is marked at the point of use and repeated in §5.3.

The scope check of guard one was applied to every candidate absence, including the eight in §3 that
failed it. Every surviving gap in §2 carries evidence, a scope classification, a falsifier, and a
statement of whether a null search backs it; the one gap with a recorded null search is L10 and the
difference is visible in §2's table rather than smoothed away.

**Revision, after an adversarial refutation pass.** Four gaps were retracted (L1, L3, L7, L11), two
restated at a smaller size (L2, L10), one restated at a different location (L5), and three sections
rebuilt (§6.0, §6.1, §6.3). Every retraction was forced by evidence already inside the corpus at the
time the gap was written, in three cases by a card the gap itself cited. Three cards were corrected in
the same pass and are the authority for four of the revisions:
[strum-2018](../collection/candidate-datasets/strum-2018/card.md) (Section V, the loudspeakers, the
screen positions and the sentence count, all missed by the original extraction),
[cbramod-2025](../collection/eeg-models/cbramod-2025/card.md) (the held-out-corpus deltas, previously
attributed to the wrong row) and
[mostert-2018-eye-movement-confounds](../collection/multimodal-biosignals/mostert-2018-eye-movement-confounds/card.md)
(the EOG electrodes, previously denied against its own source). Four arithmetic and consistency errors
were fixed: the bounded-gap count, the CBraMod channel-ratio, the AdaBrain margin range's derivation,
and the "densest recording in the corpus" claim that contradicted STRUM. The refutation is not
authoritative either, and two of its own claims did not survive checking; both are noted at the point
of use — the AdaBrain range **is** sourceable as a derivation from Table 2, and Varoquaux does not
himself invoke common-mode cancellation for same-fold paired comparisons.

`uv run python tools/validate_corpus.py` exits 0 at the time of writing, with 84 entries checked, 0
violations, six checkpoint-coverage warnings (§3 U5) and four shared-identifier warnings
([scope-diagram](./scope-diagram.md) §1).
