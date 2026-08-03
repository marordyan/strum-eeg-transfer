---
slug: makowski-2021-neurokit2
type: tool
strand: multimodal-biosignals
year: 2021
authors: [Makowski, Pham, Lau, Brammer, Lespinasse, Pham, Schölzel, Chen]
venue: Behavior Research Methods 53(4)
doi: 10.3758/s13428-020-01516-y
url: https://doi.org/10.3758/s13428-020-01516-y
license: null
modalities: [ecg, ppg, eda, resp]
tags: [tool, python, reference-implementation, feature-extraction, event-related, interval-related, algorithm-comparison, r-peak-detection, reproducibility, three-layer-api]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: rough
---

## TL;DR

The reference Python implementation for engineered peripheral-physiology features — ECG, PPG, EDA,
EMG and respiration in one uniform interface — and the reason a classical baseline for a peripheral
channel is cheap enough that there is no excuse for omitting it.

## Summary

NeuroKit2 is an open-source, community-driven Python package for neurophysiological signal
processing, covering ECG, PPG, EDA, EMG and respiration. Its stated motivation is that signal
processing algorithms are frequently published without usable packaged code, and that most existing
tools are limited to a single signal type, which forces researchers working with multimodal data to
assemble several packages. The design is a three-layer API: low-level base utilities for signal
processing, mid-level per-signal functions with fine-grained control over arguments, and high-level
convenience functions (such as `bio_process`) that run validated pipelines in a few lines. Method
selection is exposed through a `method` argument that propagates through the internal functions, so
alternative pipelines can be swapped and compared without rewriting analysis code. The paper
illustrates two typical scenarios — an event-related paradigm and an interval-related analysis —
and notes that the package supports algorithm comparison directly, for example by evaluating
different ECG R-peak detection algorithms against a suite of open-source databases.

## Relevance to the review

The brief's category 5 asks for reference implementations and their validation, and for the cases
where engineered features match or beat learned representations. This entry is the infrastructure
half of that question, and it matters for a specific practical reason.

The project's third comparison needs a peripheral baseline that is not a learned encoder.
Otherwise a gain from adding a pretrained peripheral model is uninterpretable: it could be the
peripheral *information*, or it could be the peripheral *encoder*. Several negative results in the
`eeg-models` strand turn on exactly this distinction, where classical features beat frozen
foundation-model embeddings. NeuroKit2 makes the classical arm a few lines of code across every
peripheral channel this project has — ECG, respiration, and EDA if present — under one interface,
which removes the usual reason that arm gets skipped.

Two design properties are worth carrying forward. The `method` argument means the same analysis can
be re-run under a different R-peak detector or a different EDA decomposition, so the sensitivity of
a result to preprocessing choices is measurable rather than assumed — the same concern
`schiecke-ccm-methods` raises for convergent cross mapping, in a more tractable setting. And the
split between event-related and interval-related analysis is the distinction this project has to
make explicitly: a stimulus-locked epoch is event-related, while HRV and tonic EDA are
interval-related and need windows longer than an epoch. NeuroKit2 treats these as separate
workflows rather than conflating them.

The card records `type: tool` because the article is a software description; the artifact is the
package.

## Notable details

- **Signals covered**: ECG, PPG, EDA, EMG, respiration (RSP). The card's modality tags omit EMG,
  which is not in this strand's controlled vocabulary.
- **API structure**: three layers — low-level base utilities; mid-level per-signal processing
  functions with fine-tuned control; high-level convenience functions (`bio_process` is named) that
  run validated pipelines in a few lines.
- **Method switching**: a `method` argument selects among alternative algorithms and propagates
  through internal functions, so "easily switching between processing pipelines allows for the
  comparison of different methods".
- **Two illustrated workflows**: an event-related paradigm and an interval-related analysis, which
  the paper presents as the two most typical scenarios.
- **Algorithm comparison**: the paper states that the package "allows for the comparison of
  different algorithms. For instance, using a suite of open-source databases, different algorithms
  for ECG R-peak detection have been compared for their robustness (number of errors encountered),
  efficiency (computation time) and accuracy (absolute distance from true R-peak location),
  documented in the 'Studies' section of the package's documentation."
- **Validation posture**: the abstract claims "validated pipelines" and the body says the library
  "aims at being reliable and trustworthy", backed by "a comprehensive test suite (using pytest)
  and continuous integration (using Travis-CI and GitHub actions)". Corrected in the Phase 4 audit:
  an earlier version of this card said the specific validation evidence "did not survive the
  extraction". It survives; what the source says is that the R-peak benchmark's *criteria* are the
  three named above and that its *results* live in the package documentation, not in the article.
  The gap is a deliberate pointer elsewhere by the paper, not an extraction failure — which matters,
  because a documentation page is a moving target and an article is not.
- **Provenance**: a re-forged successor to NeuroKit "1" (Makowski, 2020), retaining its most
  successful features.
- **Uptake**: 1,322 citations at retrieval, which for a tool paper is a proxy for the package being
  the field's default rather than for the paper's argument being influential.
- **Licensing**: the *article* is Springer bronze open access with no Creative Commons statement,
  so no PDF is committed here (see `meta.json.notes`). The *software* is separately licensed —
  the repository at github.com/neuropsychology/NeuroKit is MIT — and that licence, not the
  article's, governs use of the code.

## Open questions / limitations

- No EEG. NeuroKit2 covers peripheral signals; MNE-Python covers the EEG side. Any pipeline in
  this project spans two toolkits, with two sets of conventions for epoching, resampling and
  event handling, and nothing in this entry addresses the interface between them.
- "Validated pipelines" is a claim the article asserts more than it demonstrates. The R-peak
  benchmarking is named, with its three criteria, but its results are deferred to the package
  documentation rather than reported in the paper, so the article carries no number a reader can
  audit or cite. The paper also says pipelines "have been tested against established software such
  as BioSPPy … hrv …" without reporting the agreement.
- The package's convenience is also its risk: a high-level function that runs a full pipeline in
  one call makes it easy to produce features without recording which algorithm produced them. The
  `method` argument exists to counter this, but the default path does not require using it.
- The paper predates the peripheral-foundation-model literature entirely, so it offers no
  comparison between engineered features and learned representations. The strand has no entry that
  runs that comparison head to head for a peripheral channel, which is a genuine gap.
- Version drift: the article describes the package as of 2020–2021. Function names, defaults and
  available methods have changed since, so the article is a citation for the tool rather than
  documentation of the version anyone would run.
- This is the one entry in the strand whose `source.md` was not regenerated with pymupdf4llm, and it
  shows: the two-column Springer layout is shredded and inter-word spaces are stripped, so the text
  reads as run-together strings ("Webelievethat", "usingvalidatedpipelines") and the function names
  lose their underscores (`bio_process` appears as "bio process"). `md_quality: rough` is correct.
  Nothing quoted on this card depends on a table cell, but a re-extraction would be cheap.
- The paper contains no performance benchmark that could be quoted as a baseline number, so this
  entry supplies infrastructure rather than a figure to beat.

## Citations

Primary: `makowski-2021-neurokit2`

- `haque-hrv-stress-review` — the HRV-feature literature this package implements, and the closest
  thing the strand has to a performance baseline for those features.
- `wang-2025-sedation-non-eeg` — engineered HRV and vital-sign features reaching AUROC 0.825 with
  no learned encoder.
- `ahmad-2020-cognitive-load-framework` — engineered ocular and cardiac features for cognitive
  load.
- `azad-2025-construction-noise` — hand-rolls the tonic/phasic EDA decomposition this package
  provides, which is the situation the tool exists to prevent.
- Gomes et al., pyHRV, and van Gent et al., HeartPy — the single-signal alternatives NeuroKit2
  positions itself against; pyHRV is the one `kuttala-2023-hierarchical-fusion` uses.
