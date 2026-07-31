# Strand D, Dyadic and team neuroergonomics (Phase 1 brief)

**Goal:** populate `research/collection/team-neuroergonomics/` with at least 18 paper-cards
covering what mental states are actually decodable when two or more people are recorded
together, the task designs that elicit those states, and how reliable the resulting labels are.

This strand establishes whether the project's decoding target is a sound one. The plan is to
label epochs by stimulus condition, initially spoken versus written language. That is a stimulus
label, not a cognitive state, and this strand must surface how the surrounding literature treats
that distinction before Phase 4 decides whether the planned label supports a research claim.

## Scope

Cover 5 categories.

### 1. Decodable constructs

- Mental workload, engagement, vigilance and fatigue, situation awareness, shared attention,
  and communication state.
- Operational definitions used per construct, and how much they vary across papers.
- Reported within-subject and cross-subject decoding accuracy per construct, with chance level.

### 2. Task and stimulus designs

- Paradigms used to elicit team states: shared control tasks, communication tasks, joint
  problem solving, and simulated operational settings.
- Stimulus modality manipulations, specifically spoken versus written or visual versus
  auditory presentation, and what the resulting contrast is understood to measure.
- Trial structure and timing, and whether epochs are stimulus-locked or response-locked.

Category 2 must be searched with the project's own design in mind. Find work that treats an
auditory versus visual language contrast as a decoding target and record what those papers
concluded the classifier was picking up, including the possibility that it separates low-level
sensory response rather than any team or cognitive state.

### 3. Inter-brain versus within-brain analysis

- Hyperscanning measures: phase locking, coherence, Granger causality, and their critiques.
- Whether inter-brain coupling adds predictive value over concatenated within-brain features.
- Spurious synchrony from shared stimulus, shared motion, and common reference, and the
  controls that address it.

### 4. Label provenance and reliability

- Where labels come from: stimulus condition, self-report scales, expert rating, behavioral
  performance, or physiological proxy.
- Agreement statistics between label sources, and cases where they disagree.
- Circularity risks, where the label is derived from a signal that the model also sees.

### 5. Applied and operational studies

- Aviation, driving, surgical teams, control rooms, and military or emergency-response settings.
- What constraints operational recording imposes on montage, session length, and artifact.
- Deployment claims and whether they were validated on held-out teams rather than held-out
  trials from the same teams.

## Per-entry deliverable

Create folder `research/collection/team-neuroergonomics/<slug>/` containing:

- `card.md` with `strand: team-neuroergonomics` and `type` usually paper.
- `source.md` always; `source.pdf` only when `meta.json.redistribution_ok` is true.
- `meta.json` with digital object identifier or uniform resource locator, `retrieved_at`,
  license, and `redistribution_ok`.
- BibTeX appended to `research/collection/team-neuroergonomics/team-neuroergonomics.bib`, with
  the citation key rewritten to equal the entry slug exactly. `opencite` generates keys such as
  `Xu2019ADT`; replace them, since the validator and the direction papers both key on the slug.
- One categorized line in `research/collection/team-neuroergonomics/INDEX.md`.

Every card must record, in "Notable details": the construct, its operational definition in that
paper, the label source, the number of participants and of dyads or teams, whether evaluation
held out participants, and the decoding result against chance. Write `not reported` where the
paper is silent, which is common in this literature and is itself evidence for Phase 4.

## Seed material

Provisional, pending the user's seed list of papers and authors. Team neuroergonomics is a
smaller and more scattered literature than the model strands, so the user's pointers matter more
here than anywhere else in the review.

Two anchors are already fixed:

- Mullen T, Kothe C, Makeig S. STRUM: A New Dataset for Neuroergonomics Research. IEEE SMC 2018,
  digital object identifier `10.1109/SMC.2018.00023`. The `datasets-benchmarks` strand cards the
  recording; this strand cards the task and stimulus design, what construct the authors intended
  the conditions to elicit, and how they justified the spoken and written contrast. Use the same
  extraction, and use slug `strum-2018-design` so the two cards do not collide.
- Kothe C and colleagues. Decoding Working-Memory Load During n-Back Task Performance from High
  Channel NIRS Data. arXiv `2312.07546`. An inferred lead rather than a given one: same author
  group, workload as the construct, a different modality. Bears on categories 1 and 4. Verify it
  earns a card rather than assuming it does, and mark it `relevance: low` if the construct
  definition does not transfer to EEG.

Until they arrive, anchor on hyperscanning review articles and on the operational workload
literature, and expand with `opencite cite --direction both`, which recovers this literature
better than keyword search because terminology is inconsistent across communities.

Imported entries must set `imported_from: <relative path>` in `card.md`.

## Search strategy

Sources: arXiv, OpenAlex, Crossref, PubMed. PubMed matters more for this strand than for the
model strands, since much of the work appears in psychophysiology and human factors venues.

Window: 2018 onward, wider than the other strands because the construct definitions and the
hyperscanning critiques predate the foundation-model era and are still the current references.

Representative queries:

- `opencite canonical "hyperscanning inter-brain synchrony" --max 15`
- `opencite search "team neuroergonomics EEG workload operational" --max 25`
- `opencite search "EEG decoding spoken versus written language comprehension" --max 25`
- `opencite search "inter-brain coupling spurious shared stimulus control" --max 20`
- `opencite search "cross-participant generalization mental workload classification" --max 20`
- `opencite cite "<seed DOI>" --direction both`

Inclusion: the work decodes or measures a cognitive or team state from EEG in a multi-person or
operational setting, defines such a construct, or critiques how it is measured.

Exclusion: single-participant laboratory cognitive neuroscience with no decoding and no team
component; functional near-infrared spectroscopy and functional magnetic resonance imaging
hyperscanning, except where the construct definition or the spurious-synchrony critique
transfers directly to EEG.

## Skills to use

- `opencite:opencite` for retrieval, conversion, and BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 18 entries across all 5 categories
- [ ] At least 3 entries per category
- [ ] At least 3 entries bearing directly on stimulus-modality contrasts as decoding targets
- [ ] At least 2 entries critiquing inter-brain measures or label validity
- [ ] Every card records the fixed field set, using `not reported` where the paper is silent
- [ ] Every entry folder has `card.md`, `source.md`, and `meta.json`
- [ ] Every entry has BibTeX in `team-neuroergonomics.bib`
- [ ] `INDEX.md` fully populated with categorized one-liners
- [ ] No more than 40 percent of entries marked `relevance: high`
- [ ] `python tools/validate_corpus.py` exits 0
- [ ] No prose synthesis; that is Phase 3

## Out of scope

- Model architectures, pretraining, and fusion methods. Those are the `eeg-models` and
  `multimodal-biosignals` strands.
- Dataset specifications. Card the construct and the design here; the recording is the
  `datasets-benchmarks` strand.
- Social neuroscience theory with no measurement or decoding component.
- Judging whether the project's spoken versus written label is defensible. Collect the evidence
  here; Phase 4 makes the call.
