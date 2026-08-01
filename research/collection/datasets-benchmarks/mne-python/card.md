---
slug: mne-python
type: tool
strand: datasets-benchmarks
year: 2013
authors: [Gramfort, Luessi, Larson, Engemann, Strohmeier, Brodbeck, Goj, Jas, Brooks, Parkkonen, Hämäläinen]
venue: Frontiers in Neuroscience 7:267
doi: 10.3389/fnins.2013.00267
url: https://doi.org/10.3389/fnins.2013.00267
license: BSD 3-clause (software); CC BY (article)
modalities: [scalp-eeg, meg]
tags: [reference-implementation, format-reader, lazy-loading, preload-false, epoching, artifact-rejection, decoding, scikit-learn-interface, bsd-licence, memory-constraint]
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

The reference implementation that reads every format in this strand and, more importantly for this
project, the one whose access-on-demand design is inherited by its epoching and averaging containers
— "which offers the possibility to process data with a very limited memory usage".

## Summary

MNE-Python is an open-source Python package for magnetoencephalography and electroencephalography
analysis, part of the wider MNE suite and interoperating with it through the Neuromag FIF format. It
reimplements standard M/EEG algorithms in pure Python on NumPy, SciPy, matplotlib and Mayavi, and
adds methods contributed by its own authors. Coverage spans the full pipeline: raw input and output,
band-pass, low-pass, high-pass, band-stop and notch filtering with finite and infinite impulse
response options, artifact suppression by signal-space projection and independent component
analysis, epoching with baseline correction and peak-to-peak rejection, averaging, forward and
inverse modelling (minimum-norm estimate, dSPM, sLORETA, LCMV, DICS, MxNE, TF-MxNE, γ-MAP),
time-frequency analysis, non-parametric cluster statistics, spectral connectivity, and decoding
through the scikit-learn interface. At the time of writing it comprised "more than 44,000 lines of
Python code with around 22,000 lines of comments, contributed by a total of 35 persons", with about
86% test coverage. It is distributed under the new BSD licence, "allowing code reuse, even in
commercial products".

## Relevance to the review

This project has a stated hard constraint — loading one subject's full recording into a Jupyter
kernel exhausts memory and kills it — and this paper is where the mechanism that solves it is
documented. MNE-Python's `Raw` class "offers for example the ability to read data from disk only when
needed", and the design point that matters is what follows: "this access-on-demand principle can also
be inherited by other classes that build upon Raw (such as Epochs and Evoked, below), which offers
the possibility to process data with a very limited memory usage". Two further lazy-evaluation
mechanisms are documented: projections are applied on demand rather than by rewriting the data, and
source estimates can be generated so that "the data is read on-demand from the raw file and projected
to source-space during the connectivity computation, therefore requiring only a single
SourceEstimate instance to be kept in memory". Epoching early with `preload` controlled, rather than
concatenating raw arrays, is the documented pattern, not folklore.

Second, it is the format reader for every corpus in this strand: it "supports reading raw data from
various file formats e.g., BTI/4D, KIT, EDF, Biosemi BDF and BrainVision EEG", plus Neuromag FIF
natively, and reaches Brain Imaging Data Structure datasets through MNE-BIDS as named in `eeg-bids`.
European Data Format covers Temple University Hospital, Sleep-EDF and PhysioNet motor imagery; the
BCI Competition data set 2a is in the General Data Format and is *not* on that list, which is a
concrete gap this project would hit if it used that benchmark.

Third, it is infrastructure for two other entries here: `moabb` is built on MNE-Python for
preprocessing and channel selection, and `neuralbench`'s smoke-test task uses MNE's own sample
dataset.

One caution the paper itself supplies by example rather than by warning. Its decoding demonstration
uses `ShuffleSplit(len(X), 10, test_size=0.2)` over epochs pooled from two conditions in a single
subject, with no grouping key. As a single-subject illustration that is fine, but it is a random
split over epochs from one continuous recording — the configuration that
`brookshire-2024-data-leakage` and `kamrud-2021-data-partitioning` show inflates accuracy, and the
one a new user is most likely to copy.

## Notable details

- **Formats read.** "MNE-Python supports reading raw data from various file formats e.g., BTI/4D,
  KIT, EDF, Biosemi BDF and BrainVision EEG", plus Neuromag FIF as the native format. eXimia and CTF
  are not read directly — they "can be converted to FIF files using tools available in the MNE-C
  package". Micromed and Elan are reachable through the Neo project. Nibabel is an optional
  dependency "for reading and writing volume data (MRI, fMRI)".
- **Formats written.** FIF for `Raw`, `Epochs`, `Evoked` and `ICA`; `.stc` for `SourceEstimate`; NIfTI
  via `stc.save_as_volume`.
- **Containers.** `Raw`, `Epochs`, `Evoked`. Epoching is parameterized as in the paper's own listing:
  `mne.Epochs(raw, events, event_id=1, tmin=-0.2, tmax=0.5, proj=True, picks=picks,
  baseline=(None, 0), preload=True, reject=dict(grad=4000e-13, mag=4e-12, eog=150e-6))`. Epochs
  support baseline correction, detrending, temporal decimation, and peak-to-peak and flat-signal
  rejection thresholds.
- **Filtering.** Band-pass, low-pass, high-pass, band-stop and notch; finite impulse response by fast
  Fourier transform with overlap-add, optionally on GPU through CUDA and PyCUDA; infinite impulse
  response through SciPy's Butterworth.
- **Epoch length guidance.** "Depending on the experimental paradigm and the analysis employed, an
  epoch is typically 500ms to 2s long."
- **Statistics.** Non-parametric cluster-level permutation testing, with the paper noting that
  "Bonferroni or false discovery rate corrections ... are generally overly conservative" for M/EEG
  and citing Maris and Oostenveld.
- **Decoding.** Multivariate pattern analysis through scikit-learn estimators; the worked example is
  a per-timepoint linear support vector machine with a cross-validation loop.
- **Licence.** New BSD, three-clause, for the software; the article is CC BY. The paper makes the
  reuse argument explicitly: the permissive licence allows "code reuse, even in commercial products".
- **Sample data.** A shipped sample dataset that doubles as the test-suite fixture and as a proposed
  "standard validation dataset for M/EEG methods".

## Open questions / limitations

- **No version number anywhere in the paper.** The word "version" appears only in "version control
  system". No release number, no Python version requirement, no dependency pins. The paper is from
  2013 and MNE-Python has changed substantially; nothing on this card should be read as describing
  the current application programming interface. The epoching call quoted above is the 2013 signature.
- **The General Data Format is not in the supported-format list.** BCI Competition IV data set 2a is
  distributed in that format and is read with BioSig, not MNE. Any pipeline built on MNE alone cannot
  ingest that benchmark without a conversion step.
- **"Epoch" and "trial" are used as synonyms** — "these can be segmented into pieces often called
  epochs or trials, which generally correspond to segments of data after each repetition of a
  stimulus" — and "epoch" also does duty as a training hyperparameter in the decoding section. The
  package's own operational definition is the segment, and that is what the container implements.
- **The decoding example's split has no grouping key**, as described above. The paper does not warn
  about it, and does not state a multiple-comparison correction for the per-timepoint significance
  claim in that section, though it discusses correction properly in the cluster-statistics section.
- **Memory behaviour is asserted, not measured.** The paper states the access-on-demand design and
  its consequence but reports no benchmark, no memory profile, and no guidance on when preloading is
  required. For a project operating against a hard memory ceiling, the mechanism is documented but
  its limits are not.
- Two typographical errors in the source itself: "scientific comptutation" in the abstract, and a
  duplicated "can" in the epochs section.
- The paper covers no evaluation protocol, benchmark or split convention beyond the single decoding
  illustration.

## Citations

Primary: `mne-python`

- `eeg-bids` — names MNE-Python and MNE-BIDS among the readers and converters for the standard.
- `moabb` — built on MNE-Python for preprocessing and channel selection.
- `edf-plus` — one of the raw formats read.
- `neuralbench` — uses MNE's sample dataset as its low-data smoke-test task.
- Maris and Oostenveld (2007) — the cluster-based permutation framework the statistics module
  implements.
