---
slug: edf-plus
type: standard
strand: datasets-benchmarks
year: 2003
authors: [Kemp, Olivan]
venue: Clinical Neurophysiology 114(9):1755-1761 (specification also published at edfplus.info)
doi: 10.1016/S1388-2457(03)00123-8
url: https://www.edfplus.info/specs/edfplus.html
license: null (no licence statement on the specification page; journal article paywalled)
modalities: [scalp-eeg, polysomnography, ecg, emg, evoked-potentials]
tags: [file-format, standard, edf-annotations, tal, stimulus-markers, discontinuous-recording, backward-compatible, little-endian, no-electrode-coordinates, averaging-triggers]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: not-redistributable
pdf_path: null
md_path: source.md
md_quality: partial
---

## TL;DR

The format almost every corpus in this strand is distributed in, and the mechanism it uses for
stimulus markers is not a trigger channel but a reserved *signal* named `EDF Annotations` carrying
time-stamped text — which is also why identical stimuli must be annotated identically if automatic
averaging is to work.

## Summary

EDF+ extends the 1992 European Data Format with one incompatible change and several additive ones.
The structure is unchanged: "a standard EDF file consists of a header record followed by data
records", where the header identifies the patient and the technical characteristics of each signal
and the data records "contain consecutive fixed-duration epochs of the recorded signals" as
two-byte little-endian two's-complement integers. The single incompatibility is discontinuity:
"EDF+ allows storage of several NON-CONTIGUOUS recordings into one file. This is the only
incompatibility with EDF", flagged in the reserved header field as `EDF+C` for uninterrupted and
`EDF+D` for interrupted. Everything else is additive: standardized signal labels and polarity, data
records shorter than one second, a filename and companion-file convention for derived analysis
results, and the annotation mechanism. The version field is deliberately left reading `0` so that
"old EDF viewers will still work and display EDF+ files (be they continuous or discontinuous) as
continuous EDF files".

## Relevance to the review

Two things here matter for this project.

The first is where stimulus markers live and what shape they have. EDF+ stores events not as a
digital trigger line but as text in a reserved signal: "text, time-keeping, events and stimuli are
coded as text annotations in this 'EDF Annotations' signal", listed as Time-stamped Annotations Lists
with an onset in seconds relative to the file start, an optional duration, and one or more
UTF-8 text strings, delimited by the unprintable bytes 20 and 21. An EDF+ file must contain at least
one such signal even when there are no annotations, because the first annotation of each data record
carries that record's start time. So an EDF+ recording's labels are strings, and reading them is a
parsing problem rather than a thresholding problem. This is directly upstream of the `events.tsv`
requirement in `eeg-bids`: the Brain Imaging Data Structure asks for events to be made explicit
precisely because in the raw file they are either buried in a trigger channel or encoded as free text
in an annotation signal.

The second is a constraint the specification imposes that bears on label design: "in order to support
automatic averaging and superimposition, identical events or stimuli that occur several times in one
file must be coded each time by the same, unique annotation. Annotations ... of different
events/stimuli (or the same stimulus at a different location) must differ from this unique
annotation." If STRUM's spoken and written conditions are marked in EDF+, this rule is what makes
epoching by condition mechanical rather than manual — and where a lab has not followed it, the labels
have to be reconstructed.

One absence is worth recording. EDF+ stores channel *labels*, standardized as texts, and the
specification page carries no mechanism at all for electrode coordinates — the word "coordinate"
does not occur in it. The caveat is that the page's linked companion, the standard-texts list at
`edftexts.html`, is not in `source.md`, so the absence is established for the specification proper
and not for the standard-texts document it defers to. Re-derivation is described as label manipulation:
"because electrode locations are specified using standard texts, re-montaging (i.e. re-referencing)
EEG derivations can be done automatically". A coordinate-based checkpoint reading an EDF+ file must
therefore infer positions from the standard label, which is exactly what `reve-2025` does — it uses
the coordinate when available and otherwise infers it from the label, excluding channels with no
identifiable name or position. That gap is filled by `eeg-bids` with `electrodes.tsv` and
`coordsystem.json`, not by the file format.

## Notable details

- **Structure.** Header record then data records. Header fields, in order: 8 ASCII version, 80 local
  patient identification, 80 local recording identification, 8 startdate `dd.mm.yy`, 8 starttime
  `hh.mm.ss`, 8 header bytes, 44 reserved, 8 number of data records, 8 duration of a data record, 4
  number of signals; then per signal 16 label, 80 transducer type, 8 physical dimension, 8 physical
  minimum, 8 physical maximum, 8 digital minimum, 8 digital maximum, 80 prefiltering, 8 samples per
  data record, 32 reserved. "In the header, use only printable US-ASCII characters with byte values
  32..126."
- **Sample encoding.** "The ordinary signal samples (2-byte two's complement integers) must be stored
  in 'little-endian' format, that is the least significant byte first."
- **Annotation mechanism.** A signal labelled `EDF Annotations`. Each Time-stamped Annotations List
  begins `Onset[<21>Duration]<20>`, where 21 and 20 are single bytes; onset begins with `+` or `-`
  and is in seconds relative to the file start date and time; duration carries no sign; each
  annotation is terminated by byte 20 and the list by a byte 0. In each data record the first list
  must start at the first byte of the annotations signal; a list "may not overflow into another data
  record"; "each event is annotated only once, even if its duration makes it extend into the time
  period of other data records"; unused bytes are zero-filled; additional annotations signals may be
  defined. Annotation text may contain only Unicode characters encoded as UTF-8, with tab, line feed
  and carriage return permitted for multi-line text. Header constraints for the annotations signal:
  digital minimum and maximum forced to −32768 and 32767, physical minimum and maximum must differ,
  other fields blank.
- **Mandatory even when empty.** "Even if no annotations are to be kept, an EDF+ file must contain at
  least one 'EDF Annotations' signal in order to specify the starttime of each datarecord", the first
  annotation of which is empty and whose timestamp gives the record's offset from the file start.
- **Continuity flag.** Reserved field reads `EDF+C` or `EDF+D`; version stays `0` for backward
  compatibility. The specification recommends continuous files "if there are no good reasons for the
  opposite".
- **File-splitting rule.** "Signals, recorded using the same technique and constant amplifier
  settings, can be stored in one file. Different techniques, or identical techniques but with
  different amplifier settings, must be stored in separate files."
- **Derived-file convention.** An analysis of `R.edf` is stored as `RA.edf`, copying the
  80-character patient identification line and keeping the start date and time consistent, "in this
  way it is clear that both files refer to one and the same time period in the patient's life".
- **Where it is used in this strand.** Temple University Hospital corpora are distributed in EDF (the
  overview page says EDF+); Sleep-EDF polysomnograms are EDF and their hypnograms EDF+, with all
  headers EDF+ compliant; the PhysioNet motor-imagery dataset is EDF+ with annotation channels;
  `eeg-bids` names European Data Format one of its two official raw formats.
- Attribution on the specification page: the equivalent article is "Bob Kemp and Jesus Olivan.
  European data format 'plus' (EDF+), an EDF alike standard format for the exchange of physiological
  data. Clinical Neurophysiology, 114 (2003): 1755-1761." The page's acknowledgement names eight
  contributors from the Yahoo EDF users group and says the specification "was finalized in December
  2002".

## Open questions / limitations

- **No licence statement anywhere on the specification page.** No copyright line, no terms of use, no
  public-domain declaration. The format is universally treated as free to implement and the page
  offers downloads and a companies list, but nothing on it says so. The journal article is paywalled
  and was not retrieved.
- **No maintainership statement.** The page carries no byline and no "maintained by" line; the only
  named authors are Kemp and Olivan through the article citation, and the acknowledgement's "we" is
  never expanded.
- **"One session in one file" is promised twice and prohibited once.** The introduction says "all
  signals, annotations and events that are recorded in one session using one recording system can be
  kept safely together in one file", and section 2.3 repeats it as an ideal; but the filename
  convention states that "different techniques, or identical techniques but with different amplifier
  settings, must be stored in separate files", and the worked example duly splits one session across
  several files. For anyone reasoning about session-level grouping in a split, this means a session
  is not reliably one file.
- **"Epoch" is used in two incompatible senses.** A data record is described as a "fixed-duration
  epoch of the recorded signals"; in section 2.3, "Unscored epochs should be coded as the integer
  number 9" refers to sleep-scoring intervals. These are different objects and the
  specification never disambiguates them. *Correction, made during review: an earlier version of
  this bullet called the second sense "30-second sleep-scoring intervals" and placed it "three
  sections later". The specification states no scoring-epoch length anywhere; the section 3.3
  worked example's sleep-stage annotations run 660, 300, 180, 300, 210, 270 and 30 seconds. The
  30 seconds was an external convention, not this source.* "Window" appears as a third near-synonym for the data
  record duration in the electromyography and neurophysiology examples.
- **"Montage", "derivation" and "re-referencing" are used interchangeably** in one sentence, and the
  table of contents heading ("Montages in a routine EEG") does not match the section heading
  ("Routine EEG"). Strictly a montage is a set of derivations and re-referencing is one way to
  produce them; the specification collapses the three, which matters because the format stores
  labels only and cannot express a coordinate.
- **Sleep-stage nomenclature is inconsistent between sections**: section 2.3 gives "sleep stages
  W,1,2,3,4,R,M ... coded in the data records as the integer numbers 0,1,2,3,4,5,6 respectively",
  while the section 3.3 annotation example uses the names "Sleep stage N1", "N2", "N3". No mapping
  between the two is given, and there is no stage 4 in the example's scheme. *Correction, made
  during review: an earlier version of this bullet named the two schemes Rechtschaffen and Kales
  and American Academy of Sleep Medicine. Neither name — nor "AASM" — appears anywhere in the
  specification; the identification is external and has been removed, though the mismatch itself is
  real.* This is the same mismatch that appears between `sleep-edf-expanded`'s hypnograms
  and the five-class labels the benchmark suites report.
- **`md_quality` is `partial` for a specific reason**: the unprintable delimiter bytes 20 and 21 are
  the specification, and the HTML-to-text conversion silently dropped them, so every worked
  annotation example in `source.md` has lost its field boundaries and several definitional sentences
  are ungrammatical as extracted. The byte layout on this card was reconstructed from the surrounding
  prose, which names the byte values explicitly, and should be checked against the live page before
  any implementation. The sleep-scoring example table was also read column-wise and is out of
  chronological order in the extraction.
- The specification predates any machine-learning use of these files and says nothing about
  evaluation, splits or leakage. The one adjacent provision is the derived-file naming convention,
  which makes recording-level linkage recoverable — the precondition a leakage-aware split needs —
  though the specification does not frame it that way.

## Citations

Primary: `edf-plus`

- `eeg-bids` — names European Data Format one of two official raw formats, and supplies the
  `events.tsv`, `electrodes.tsv` and `coordsystem.json` layers this format has no mechanism for.
- `sleep-edf-expanded` — polysomnograms in EDF with EDF+-compliant headers and hypnograms in EDF+.
- `physionet-mi` — EDF+ with annotation channels carrying the T0/T1/T2 stimulus markers.
- `tuh-eeg-corpus` — distributed in EDF, converted from a proprietary format.
- `mne-python` — reads European Data Format among its supported raw formats.
