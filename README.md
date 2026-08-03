# EEG foundation-model transfer on the STRUM dataset

Do pretrained EEG foundation models transfer to a dyadic, team-neuroergonomics setting, and does
adding peripheral physiology on top of the EEG embedding improve that transfer?

The study is three comparisons on [STRUM](https://doi.org/10.1109/SMC.2018.00023), a 28-pair
neuroergonomics recording with 206-channel EEG plus ECG, EOG and respiration on the same amplifier:

1. A small supervised-from-scratch EEG model trained directly on STRUM.
2. An off-the-shelf pretrained EEG foundation model, fine-tuned on STRUM.
3. That fine-tuned model plus peripheral physiology, to measure the added value.

## What is in this repository right now

No modelling code yet. What exists is the literature review that decides how the three comparisons
should be run, and the toolchain that keeps it honest.

| Path | What it holds |
|---|---|
| `direction-papers/` | The argument, with every claim linked to the card that supports it |
| `research/synthesis/` | Four strand ontologies, a cross-strand theme map, a dataset hierarchy, a scope diagram, and the gap analysis |
| `research/collection/` | 84 paper cards, each with an archived source extraction and provenance |
| `_briefs/` | What each strand was asked to collect, and the shared collection and synthesis practice |
| `tools/`, `tests/` | The corpus validator and its test suite |

Start with `research/README.md` for the reading order, or go straight to
`direction-papers/eeg-transfer-strum-direction.md`.

## What the review concluded

**Report transfer as a located number, not a value.** A reported transfer number is one position on
three axes the corpus has measured to reorder results: the holdout unit, the adaptation regime, and
the checkpoint's identity. A single unlocated number is not checkable.

**But do not cross all three.** The paper concedes this against itself in section 9.3. Backing an
effect size out of the dataset paper's own dispersion puts the minimum detectable difference near
seven points at the full subject denominator, against target effects whose median is a few points. A
full crossing multiplies underpowered cells. What survives is stating the coordinates, reporting an
interval and a permutation null at each point, traversing the adaptation regime, and crossing the
holdout unit once.

Four findings that change the plan:

- **STRUM already has a published baseline.** The dataset paper's own Section V is a model
  comparison on this recording with a stated protocol. Its authors warn that their best models
  "prominently depend on artifactual EEG sources, specifically frontal patterns typical for eye
  activity", which is the strongest on-substrate evidence for the ocular confound.
- **The spoken-versus-written label survives, with a caveat.** The side tasks form a 2x2 of stimulus
  modality by stimulus kind. That structure diagnoses the ocular confound rather than subtracting
  it, and it is broken for signed horizontal EOG because the two visual tasks sit on different
  screens. Build the ocular arm from sign-invariant features.
- **Peripheral physiology is runnable but needs the right label.** HRV and respiration integrate over
  5 to 20 seconds and cannot resolve a short stimulus-locked label. Run them against the slow fatigue
  covariate the 3.5-hour session was designed to induce.
- **Adaptation regime dominates checkpoint choice.** Freezing costs 29.5 points on one dataset and
  1.9 on another, and partial fine-tuning beats full. Being unseen by every pretraining corpus is
  worth 0.12 to 0.40 points, so novelty of substrate is not the contribution.

## Reliability

Section 6 of the direction paper accounts for what the citation guarantee does and does not buy. A
corpus-wide card-versus-source audit corrected 57 of 84 entries. A first pass finding 57 defects
bounds nothing about what a second would find, and one correction made during review was itself
wrong and is documented as such rather than silently reversed. Traceability is not correctness; it
is the ability to check.

## Toolchain

Python, managed with [uv](https://docs.astral.sh/uv/). The corpus validator is standard library plus
PyYAML.

```bash
uv run python tools/validate_corpus.py   # structural + licence invariants over all 84 entries
uv run pytest -q                         # 69 tests
uv run pytest tests/test_validate_corpus.py::test_redistribution_violation -q   # a single test
uv run ruff check . && uv run ruff format --check .
```

CI runs all four on push and pull request. Use `uv run`, not bare `python`; PyYAML lives in the
`dev` dependency group, which `uv run` installs by default.

## Licence policy for archived sources

`meta.json.redistribution_ok` is the single source of truth for whether a `source.pdf` may exist in
an entry folder. Open-access papers and preprints are archived as PDFs; paywalled ones are not, and
only the markdown extraction is committed as research notes. When a licence is unclear the default
is deny, and an arXiv posting conveys no third-party redistribution right unless the paper states
one. Four invariants are enforced by the validator and by CI; `research/README.md` lists them.

## Next step

The roadmap is section 7 of the direction paper. It has one precondition that is not a research act:
STRUM is at the highest-friction rung of the access ladder, so the first move is a request to the
authors carrying the coordinate and cap-layout question, the EOG placement question, the
auditory-task screen assignment, and the usable session count, as one action with a go/no-go
outcome. Three of the seven routes have open-substrate rehearsals that can run without waiting.
