# Strand D, Candidate datasets and label validity (Phase 1 brief)

**Goal:** populate `research/collection/candidate-datasets/` with at least 18 cards covering
datasets this project could actually fine-tune or evaluate on, STRUM included, specified in enough
detail that Phase 4 can map identified gaps onto data by table lookup rather than by re-reading
sources.

This strand answers "what data could we use", including whether STRUM is the right choice. Strand C
answers the separate question of how the field measures transfer and whether that measurement is
sound. The two are kept apart because a dataset can be ideal on paper and unusable under the
evaluation protocol the field expects, and the review has to be able to say so.

A sequencing note, since the strand's purpose invites the mistake: this strand does not decide which
dataset closes a gap. The gap analysis does not exist until Phase 4. What this strand produces is a
specified inventory. Collect broadly, specify precisely, and leave the matching alone.

## Scope

Cover 5 categories.

### 1. Multi-person and dyadic recordings

- Public datasets with two or more simultaneously recorded participants.
- Synchronization method and its measured precision, which bounds any cross-participant analysis.
- Whether labels are per-participant, per-dyad, or per-trial.

If this category comes back thin after a genuine search, that absence is a finding rather than a
failure. Record in `INDEX.md` which queries were run and what they returned, so Phase 4 can state the
scarcity as evidence instead of as an impression.

### 2. Synchronized EEG and peripheral physiology

- Datasets carrying electroencephalography (EEG) alongside electrocardiography, electrooculography,
  respiration, or electrodermal activity.
- Which peripheral channels are usable as signal versus recorded only for artifact rejection. This
  distinction decides whether a dataset can support the project's third comparison at all.
- Sampling rate per modality, and how the modalities are aligned.

### 3. Label provenance and validity

- Where labels come from: stimulus condition, self-report, expert rating, behavioral performance, or
  physiological proxy.
- Whether a stimulus-condition label supports a cognitive claim. This project's initial plan is to
  label epochs spoken versus written, which is a property of the stimulus rather than of a mental
  state, and a classifier can score well on it by separating low-level auditory from visual response.
  Find work that treats such a contrast as a decoding target and record what the authors concluded
  the classifier was actually picking up.
- Circularity risks, where the label derives from a signal the model also sees.
- Agreement between label sources where more than one exists.

This category inherits the question that the retired team-neuroergonomics strand owned, and it is the
most consequential thing in this strand. A dataset with an invalid label cannot support the study no
matter how good the recording is.

### 4. Access, licensing, and practical feasibility

- Access route: open download, registration, data use agreement, or request to authors.
- Size on disk and total hours, weighed against the memory constraint recorded in `CLAUDE.md`, which
  is that one subject's full recording exhausts a Jupyter kernel.
- Montage and channel count, weighed against the input contracts recorded by strand A. A dataset a
  checkpoint cannot ingest without resampling or channel interpolation should say so on its card.
- Format: Brain Imaging Data Structure for EEG, European Data Format, or bespoke, and what reads it.

### 5. STRUM and its closest comparators

- STRUM itself, carded once, in full detail.
- Datasets resembling STRUM on the dimensions that matter to the research question, whether or not
  they are dyadic: language stimulus manipulations, operational or team settings, or EEG plus
  physiology in a task context.
- What each comparator offers that STRUM does not, written as specification rather than as judgment.

## Per-entry deliverable

Create folder `research/collection/candidate-datasets/<slug>/` containing:

- `card.md` with `strand: candidate-datasets`, and `type: dataset` for datasets, `type: paper` for
  label-validity and methods papers, `type: standard` for format specifications.
- `source.md` always. For a dataset with no paper, snapshot the canonical documentation or landing
  page and set `pdf_status: not-applicable`.
- `source.pdf` only when `meta.json.redistribution_ok` is true, `pdf_status` is `archived`, and
  `pdf_license` is in the redistributable set listed in the card schema addendum.
- `meta.json` with the access uniform resource locator, `retrieved_at`, license, and
  `redistribution_ok`. Record the data license separately from the paper license in `notes`; the two
  differ more often than not.
- BibTeX appended to `research/collection/candidate-datasets/candidate-datasets.bib`, with the
  citation key rewritten to equal the entry slug exactly. `opencite` generates keys such as
  `Xu2019ADT`; replace them, since the validator and the direction papers both key on the slug.
- One categorized line in `research/collection/candidate-datasets/INDEX.md`.

Every `type: dataset` card must record this fixed field set in "Notable details", so Phase 4 can
build a comparison table mechanically: participants, simultaneous participants per recording,
channels, sampling rate, peripheral channels present, total hours, task, label type, label source,
license, access route. Write `unknown` where the source is silent. Do not infer, and do not omit the
line.

Imported entries must set `imported_from: <relative path>` in `card.md`.

## Seed material

### Required entry: the STRUM dataset

Mullen T, Kothe C, Makeig S. STRUM: A New Dataset for Neuroergonomics Research. 2018 IEEE
International Conference on Systems, Man, and Cybernetics (SMC), pages 77 to 82. Digital object
identifier `10.1109/SMC.2018.00023`. Slug `strum-2018`.

One card, covering the recording, the task and stimulus design, and the label scheme together. An
earlier draft of these briefs split STRUM across two strands; the repartition removed the reason to,
and one card avoids two bibliography entries for a single identifier.

Retrieval notes: IEEE proceedings are paywalled, so expect `redistribution_ok: false` and a markdown
extraction only, unless an author copy exists. Check the Swartz Center for Computational Neuroscience
and Intheon publication pages for an author accepted manuscript first.

Record the citation count and test the claim that follows. At retrieval time Semantic Scholar and
OpenAlex both reported 2 citations. If that holds it is a substantive finding rather than trivia,
because it means there is almost no published modeling work on STRUM to baseline against, which
changes what this project can claim. Run
`opencite cite "10.1109/SMC.2018.00023" --direction backward` and card whatever it returns.

### Inferred leads, not given

Verify relevance before carding; drop any that does not bear on this strand.

- Kothe C and colleagues. The Lab Streaming Layer for Synchronized Multimodal Recording. bioRxiv,
  digital object identifier `10.1101/2024.02.13.580071`. Category 1, since synchronization precision
  bounds cross-participant analysis, and STRUM was plausibly recorded with this toolchain. Confirm
  from the STRUM methods rather than assuming it.
- Kothe C and colleagues. Decoding Working-Memory Load During n-Back Task Performance from High
  Channel NIRS Data. arXiv `2312.07546`. Category 3 only, and only for how the workload label was
  defined and validated. Different modality, so mark `relevance: low` unless the label reasoning
  transfers.
- The registries PhysioNet, OpenNeuro, and the Brain Imaging Data Structure example collection, swept
  for categories 1, 2, and 5. Citation search covers registries poorly, so browse them directly and
  record the registry landing page as `source_url`.

## Search strategy

Sources: arXiv, OpenAlex, Crossref, PubMed, plus direct registry browsing. PubMed matters here
because label-validity work often appears in psychophysiology and human factors venues.

Window: no lower bound for datasets, which stay current long after publication. For label-validity
papers, 2015 onward.

Representative queries:

- `opencite search "EEG dataset data descriptor multimodal physiological" --max 25`
- `opencite search "hyperscanning dataset two participants simultaneous EEG" --max 25`
- `opencite search "EEG decoding spoken versus written language comprehension" --max 25`
- `opencite search "stimulus condition label validity EEG decoding confound" --max 20`
- `opencite search "auditory versus visual presentation EEG classification sensory response" --max 20`
- `opencite lookup "10.1109/SMC.2018.00023"`

Inclusion: the work releases data this project could plausibly use, specifies such a dataset, or
establishes whether a label type supports a cognitive claim.

Exclusion: private clinical datasets with no access route; datasets under 8 participants with no
peripheral channels and no multi-person structure, unless a checkpoint in strand A reports on them.

## Collection practice

Read `_briefs/collection-practice.md` before starting. It carries the working tool invocations, the
BibTeX verification requirement, the search trap that silently reports zero matches on converted
sources, and the rules for missing facts, self-contradicting sources, and strand-level fields. Every
item in it cost real time or nearly corrupted a card during the Phase 2 pilot.

## Skills to use

- `opencite:opencite` for lookup, retrieval, conversion, and BibTeX export.
- `manuscript:manuscript-writing` for prose discipline in card sections.

## Acceptance criteria

- [ ] At least 18 entries across all 5 categories
- [ ] At least 3 entries per category
- [ ] STRUM carded once from its primary source, with the full fixed field set
- [ ] A backward citation search from the STRUM identifier has been run, and `INDEX.md` records what
      it returned, including the case where it returns nothing usable
- [ ] At least 4 datasets carrying EEG and at least one peripheral modality
- [ ] At least 3 entries in category 3 bearing directly on whether a stimulus-condition label
      supports a cognitive claim
- [ ] Category 1 either reaches 3 entries or `INDEX.md` records the queries run and what they
      returned
- [ ] Every `type: dataset` card records the full fixed field set, with `unknown` where the source is
      silent
- [ ] Every entry folder has `card.md`, `source.md`, and `meta.json`
- [ ] Every entry has BibTeX in `candidate-datasets.bib`, keyed to the slug
- [ ] `INDEX.md` fully populated with categorized one-liners
- [ ] No more than 40 percent of entries marked `relevance: high`
- [ ] `uv run python tools/validate_corpus.py` exits 0
- [ ] No prose synthesis, no dataset ranking, and no gap matching; those are Phases 3 and 4

## Out of scope

- Architectures, pretraining objectives, and checkpoints. That is strand A, `eeg-models`.
- Fusion methods and peripheral signal modeling. That is strand B, `multimodal-biosignals`.
- Large pretraining corpora, benchmark protocols, and split conventions. That is strand C,
  `datasets-benchmarks`. The dividing line: strand C cards a dataset when it is what a model was
  pretrained on or benchmarked against; this strand cards it when the project could fine-tune on it.
  A dataset that is both gets carded in both, with each card written to its own strand's question.
- Hyperscanning connectivity measures, inter-brain coupling, and their critiques, except where a
  paper bears directly on label validity. This strand replaced an earlier team-neuroergonomics
  strand, and that methodological literature went out of scope with it. If Phase 3 finds the omission
  load-bearing, reopen it as a new strand rather than smuggling it in here.
- Deciding which dataset the project should use. Phase 4 decides that from this inventory.
