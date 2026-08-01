---
slug: tuh-eeg-corpus
type: dataset
strand: datasets-benchmarks
year: 2016
authors: [Obeid, Picone]
venue: Frontiers in Neuroscience 10:196 (Data Report)
doi: 10.3389/fnins.2016.00196
url: https://doi.org/10.3389/fnins.2016.00196
license: CC BY (article); data access by registration, no data licence stated
modalities: [scalp-eeg, clinical-eeg]
tags: [pretraining-corpus, clinical-archive, temple-university-hospital, edf, registration-required, hipaa-deidentified, physician-reports, event-annotations, largest-public-clinical-eeg]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: rough
---

## TL;DR

The clinical EEG archive that most EEG foundation models are pretrained on, released as 16,986
recording sessions from 10,874 patients with the physician's report attached to each — and it is
distributed by registration and rsync rather than under any stated data licence.

## Summary

Obeid and Picone describe the Temple University Hospital EEG Corpus, assembled by the Neural
Engineering Data Consortium from archival clinical records at Temple University Hospital. Its stated
motivation is that machine learning in EEG had been limited by data scale, with typical studies
"involving 100 or less EEG studies". The released corpus comprises 16,986 sessions from 10,874
unique subjects, converted from Nicolet NicVue to European Data Format, de-identified to the
HIPAA Privacy Rule by removing 18 identifiers, and paired with the neurologist's report for each
session. What distinguishes it from a laboratory corpus is exactly what makes it hard: the authors
are explicit that "'clinical-grade' data is inherently more variable with respect to parameters such
as electrode location, clinical environment, equipment, and noise". A separately downloadable
annotation set labels channel-specific events in six classes: spike and sharp wave, periodic
lateralized epileptiform discharges, generalized periodic epileptiform discharges, artifact, eye
movement, and background.

## Relevance to the review

This is the substrate under most of the pretrained weights this project might use, and its
properties propagate into them. LaBraM, CBraMod, BIOT and REVE all draw on Temple University Hospital
data — CBraMod's pretraining corpus is described by `adabrain-bench` as TUAB, TUAR, TUEP, TUEV, TUSE
and TUSL, all derived from this archive, and `reve-2025` records 26,847 of its 61,415 pretraining
hours as coming from Temple University Hospital. Three consequences.

First, the pretraining distribution is clinical resting and routine EEG from patients, at 250 Hz on
24 to 36 channels, not task-evoked laboratory EEG from healthy participants under experimental
control. A stimulus-condition contrast recorded in a laboratory is a different distribution from the
one these checkpoints saw, and the size of that gap is one of the things this project's first two
comparisons will measure.

Second, the label structure is clinical. The corpus's own annotations are epileptiform and artifact
events plus a background class, and the corpus's downstream derivatives (`tuab`, `tuev`) inherit
that. Nothing here supplies a cognitive or stimulus label, which is why the checkpoints' reported
strengths cluster on pathology and seizure detection — the two task families `neuralbench` reports as
close to saturation.

Third, the access route decides whether this project could continue pretraining rather than only
fine-tune. It can, in principle: the data are free. But there is no licence, only a signed form and
an institutional email address, and as of January 2026 distribution moved to ssh keys and rsync.
That is a slower and more administratively involved path than a Creative Commons download, and it
has to be started early if it is on the plan at all.

## Notable details

Fixed field set required of every `type: dataset` card in this strand:

- **Participants**: 10,874 unique subjects. "The average number of sessions per patient was 1.56,
  although as many as 37 EEGs were recorded for a single patient over an 8-month period." Subjects
  were 51% female, ranging in age from under 1 year to over 90.
- **Channels**: "The most common number of EEG-only channels per EDF file was 31, although there
  were cases with as few as 20." The overview page states EEGs "consist of 24 to 36 channels of
  signal data and an annotation channel". Files typically also carry supplementary channels such as
  detected bursts, electrocardiography, electromyography and photic stimuli. **The montage — the
  derivation scheme — is not stated in the paper**, which reports channel counts only; the word
  montage does not appear. Downstream work on Temple University Hospital data commonly applies the
  transverse central parietal montage, but that is a choice made by those users, not a property of
  the corpus.
- **Sampling rate**: "A majority of the EEG data was sampled at 250 Hz (87%) with the remaining data
  being sampled at 256 Hz (8.3%), 400 Hz (3.8%), and 512 Hz (1%)." The overview page adds 16 bits
  per sample; the paper itself does not state bit depth.
- **Total hours**: not given in hours. The paper reports "a grand total of 29.1 years (total duration
  summed over all EEG channels) of EEG data" — a channel-summed figure, which is not convertible to
  recording hours without the per-file channel count. `reve-2025` records 26,847 hours from Temple
  University Hospital in its own accounting.
- **Task**: none. This is archival clinical recording — routine and long-term monitoring EEG ordered
  for diagnostic purposes, not an experimental paradigm. Approximately 87% of the accompanying
  reports contain the string "epilep" and about 12% "stroke".
- **Label type**: two kinds. Per session, the neurologist's free-text clinical report, generated as
  part of the patient's medical record and optically character-recognized from scanned printouts.
  Separately, an optional downloadable annotation set giving per-channel start and stop times with
  one of six event labels (SPSW, PLED, GPED, ARTF, EYEM, BCKG). No cognitive, behavioural or
  stimulus label exists.
- **Licence**: **no data licence is stated**, in either the paper or the downloads page. The article
  itself is CC BY. Access is governed by a signed form rather than a licence.
- **Access route**: free after registration. A form must be completed and emailed to
  help@nedcdata.org with a valid institutional email address; approval typically takes 24 to 48
  hours; as of January 2026 the corpora are distributed by ssh key and rsync (`rsync -auvxL`, with
  the `-L` option required because all subsets are symlinked back to the parent corpus). An 8 TB USB
  drive mailed to the maintainers is offered as an alternative where connectivity is a problem. The
  most current release path at retrieval time was `data/tuh_eeg/tuh_eeg/v2.0.2`.
- **Checkpoints pretrained on or evaluated against it**: pretrained on Temple University Hospital
  data — CBraMod (on TUAB, TUAR, TUEP, TUEV, TUSE, TUSL per `adabrain-bench` Table 7), BIOT (on TUAB
  and TUEV among six corpora), LaBraM (on TUEP and TUSZ among ~20 datasets), REVE (26,847 h of its
  61,415 h). Evaluated against derived subsets — see `tuab` and `tuev`, which between them are
  reported on by BIOT, EEGPT, LaBraM, CBraMod, REVE, BENDR, BrainOmni, FEMBA, Neuro-GPT, NeuroLM,
  EEGMamba and LUNA across the four benchmark suites carded in this strand.

Other details:

- **Size on disk**: 572 GB uncompressed for EDF files and reports together; 330 GB as per-patient
  gzip archives, median 4.1 MB per patient.
- **Years**: the paper says "14 years of clinical EEG data" and notes gaps — "with the exception of
  years 2000–2002, and 2005, in which limited numbers of complete reports were found" — but the
  explicit date range appears only in a lost figure. The downloads page says 2002 to 2017; the
  overview page says 2002 to 2013 "(and beyond)". Sessions per year vary "from ∼1000 to 2500", with
  the corpus growing "at a rate of ∼2500 new sessions per year".
- **Format and structure**: EDF (the overview page specifies EDF+). Directory hierarchy is patient
  then session, with patients grouped roughly 100 per folder under 109 numbered top-level folders.
  Each session folder holds one or more `.edf` files plus the report as `.txt`.
- **De-identification**: 18 HIPAA identifiers removed including names and dates of birth; medical
  record numbers randomized; "all storage and manipulation of source files was conducted on dedicated
  non-network connected computers". Work performed under Temple University institutional review
  board approval and in accordance with the Declaration of Helsinki.
- **Only sessions with both an EEG and a corresponding clinician report were included.**
- **No train/development/evaluation partition is defined by the corpus.** The partitions used in the
  literature come from the derived subsets and from individual benchmark suites.

## Open questions / limitations

- **No data licence.** Registration and a signed form are not a licence grant, and neither the paper
  nor the downloads page states redistribution or derivative terms. Any plan that involves
  republishing derived data or model weights trained on this corpus needs the form's actual text
  read, which was not retrieved.
- **The corpus version is internally inconsistent in the paper**: the body says "The TUH-EEG corpus
  v0.6.0 has been released" while the reference list cites v0.6.3. The downloads page as retrieved in
  2026 lists v2.0.2, so the paper describes a much earlier release than the one now distributed, and
  none of the counts above should be assumed current.
- **The 29.1-year figure is channel-summed and is routinely misquoted as recording duration.** It is
  not comparable to any hours figure reported by a pretraining paper without knowing the channel
  count assumption.
- **The reported age statistics are not internally coherent**: "average 51.6, stdev 55.9" for a
  distribution bounded between under 1 and over 90 years. A standard deviation exceeding the mean is
  not attainable there. Treat the standard deviation as unreliable; the paper offers no correction.
- **The annotation-class enumeration is broken in the paper**: it announces six classes and then
  enumerates three (SPSW, PLED, GPED), introducing the other three a paragraph later as "three events
  ... used to model background noise" before reconciling them as "these six classes (three signal
  classes and three noise classes)". The six are recoverable but the local enumeration does not
  match its own count.
- **"Record", "session", "EEG" and "scan" are used interchangeably**, and a session may contain
  multiple EDF files where long-term monitoring was split. So a count of records is not a count of
  sessions and not a count of files, and the max-per-patient statistic switches unit mid-sentence
  ("as many as 37 EEGs" inside a sessions-per-patient discussion). Any downstream count taken from
  this paper must say which unit it means.
- **No montage information at all.** For a project deciding whether a checkpoint's input contract can
  ingest its own recordings, the absence is material: the corpus specifies channel counts and labels
  but not the derivation scheme, and the checkpoints pretrained on it inherit whatever their authors
  chose in preprocessing.
- The corpus is single-site and single-country, and the population is a hospital population, 75% of
  whose records were classified as abnormal in the reports according to the Lopez thesis appended to
  the `tuab` source. That is a strong selection effect for any model pretrained on it.

## Citations

Primary: `tuh-eeg-corpus`

- `tuab` — the normal-versus-abnormal subset derived from this corpus, and one of the two most
  reported benchmarks in the foundation-model literature.
- `tuev` — the six-class event subset derived from this corpus.
- `labram-2024`, `reve-2025` (strand `eeg-models`) — two of the checkpoints pretrained partly on this
  archive.
- `edf-plus` — the file format the corpus is distributed in.
- Harati et al. (2014) — the earlier description of the archive the paper cites for the
  30,000-record, 18,000-patient figures quoted in the Lopez thesis.
