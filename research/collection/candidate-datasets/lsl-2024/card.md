---
slug: lsl-2024
type: tool
strand: candidate-datasets
year: 2024
authors: [Kothe, Shirazi, Stenner, Medine, Boulay, Grivich, Artoni, Mullen, Delorme, Makeig]
venue: bioRxiv preprint 2024.02.13.580071
doi: 10.1101/2024.02.13.580071
url: https://doi.org/10.1101/2024.02.13.580071
license: null
modalities: [multimodal-streaming, scalp-eeg, emg, motion-capture, eye-tracking, audio, event-markers]
tags: [synchronization, lab-streaming-layer, xdf, clock-offset-correction, jitter-handling, multi-machine, measured-precision, mobi, cites-strum]
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

The Lab Streaming Layer synchronises independently clocked acquisition devices in software rather
than in hardware, and this paper is the reference description of the framework together with its
authors' own timing measurements — sub-millisecond jitter between professional amplifiers, with a
fixed device offset that has to be measured and subtracted separately.

**Corrected 2026-08-01, Phase 4 audit.** This previously claimed the paper "is the first to publish
measured numbers for how well it does that". The paper explicitly disclaims priority, positioning
itself after prior validation work: "LSL has been extensively tested and validated by the biosignal
research community in several studies" (eight citations), and "Here, we provide some data
concerning LSL's performance on a local network". Its conclusion likewise credits others with the
headline result: "Recent benchmarks have demonstrated that LSL achieves sub-millisecond
synchronization accuracy [Blum et al., 2021], [Chuang et al., 2021], [Iwama et al., 2022]".

## Summary

An architecture-and-performance paper for the Lab Streaming Layer (LSL), the software framework
that has been the de facto standard for multimodal neurophysiological recording since 2012. LSL
publishes each device's data as a network *outlet* that any *inlet* on the local area network can
subscribe to; per-sample timestamps are taken from the most steady high-resolution clock available
on each machine, and the relative offset and drift between machines' clocks are measured
continuously and corrected. The paper describes the framework as "a freely available open-source
project" hosted at github.com/labstreaminglayer with core repositories from the Swartz Center for
Computational Neuroscience, and reports "a listing of over 150 known LSL-compatible device
classes". The performance section is the substantive contribution: single-machine and networked
tests against a National Instruments data-acquisition reference, plus a two-device EEG-and-EMG
test. The authors are explicit about the limitation that bounds all of it — LSL "does not have
access to any incoming data until the moment it is received by the microprocessor", so a fixed
device-dependent transport delay remains and must be characterised per device.

## Relevance to the review

This entry sits in category 1 because synchronisation precision is what bounds any
cross-participant analysis, and a two-person recording built on LSL inherits the numbers below
as its floor. It also matters as the tooling context for STRUM: the strand brief flags that STRUM
was plausibly recorded with this toolchain, and this paper is one of exactly two works that cite
STRUM. The link is established twice over, from both ends. This paper's own conclusion states that
LSL was used to make the recording: "In one multiperson, multiple touchscreen simulation [Kothe et
al., 2018], we successfully used LSL to record from over 40 LSL data streams in recording sessions
lasting multiple hours", with a footnote describing "Two concurrent subjects, each with instruments
including a 267-channel BioSemi, microphone, force plate, eye-tracking, three cameras, motion
capture, and event marker streams." And the STRUM methods, read in full on 2026-08-01, say the same
directly: "Time synchronization was done using the Lab Streaming Layer", with each two-participant
session written to a single time-synchronized XDF file. The relationship is recorded as confirmed
on `strum-2018`, and this card's numbers therefore apply to STRUM rather than merely resembling its
setup.

Two details worth carrying. First, the earlier version of this paragraph said the citation "on its
own would establish only that LSL's authors cite STRUM"; that understated it, since the citing
sentence asserts the recording use. Second, an **unreconciled channel-count discrepancy** between
the two sources: this paper's footnote says "267-channel BioSemi", while `strum-2018` gives 206 EEG
plus 43 EMG, 2 ECG, 2 EOG and 16 respiration, which totals 269. Both readings are recorded and
neither is picked.

The concrete value for this strand is that it supplies the reference numbers against which the
two multi-person EEG datasets found here can be judged. Both `boa-actors-2025` and
`livewire-2024` synchronise by trigger — hardware and manual respectively — and neither reports
any measured timing error. LSL's published figures are what "measured synchronisation precision"
looks like when it is actually reported, and their absence from the two dataset papers is
therefore a specification gap rather than an unanswerable question.

## Notable details

- **Measured single-machine performance**: comparing a BioSemi marker stream against a
  data-acquisition input marker showed a 12.20 ms fixed setup offset between the two markers, with
  jitter — reported as the standard deviation of the lag — of 156 microseconds, "below the
  ~500-microsecond Biosemi time resolution". The authors' conclusion is that the two streams "could
  be aligned by removing this (pre-measured) device setup offset, and time jitter should not affect
  this alignment".
- **Measured networked performance**: the same test with the BioSemi and data-acquisition machines
  separated gave a smaller setup offset, 6.26 ms against the local 12.20 ms, with offset jitter of
  145 microseconds — "similar to the results from the local network experiment". The authors
  attribute the offset decrease to the machine separation and possibly faster performance, and do
  not claim it as a general result.
- **Two-device biosignal test**: "the jitter-corrected latency between EEG and EMG streams showed a
  tight distribution centered around zero with standard deviation of approximately 0.5 ms,
  indicating excellent synchronization performance", for professional hardware with uniform
  sampling rates.
- **Jitter handling is not free, and its sign depends on the hardware**: "Disabling jitter handling
  (HandleJitter = false) increased jitter by at least one order of magnitude for professional-grade
  devices, as shown in the EEG-EMG comparison where the uncorrected jitter distribution was
  substantially broader. Interestingly, for consumer-grade hardware such as a webcam, disabling
  jitter handling sometimes improved synchronization. This occurs because highly irregular sampling
  rates violate the Gaussian delay distribution assumptions underlying the jitter correction
  algorithm." Performance "varied significantly with device type and parameter settings".

  **Corrected 2026-08-01, Phase 4 audit.** This bullet previously truncated the quotation at
  "increased jitter by at least" and stated that "the extracted sentence is truncated at that point
  in the retrievable text; the direction is unambiguous, the magnitude is not quoted here". The
  magnitude — "at least one order of magnitude for professional-grade devices" — is present in
  `source.md`; nothing was missing. The card also omitted the reversal for consumer-grade hardware,
  which is the operationally relevant half for anyone using a webcam or consumer sensor in the
  stack. The same false truncation claim appears in this entry's `meta.json` notes.
- **The offset is fixed, the jitter is small**: this is the operationally important shape of the
  result. LSL does not remove the constant transport delay of a device; it makes that delay stable
  enough that a single pre-measured constant can be subtracted. Any recording that did not measure
  its device offsets carries them uncorrected.
- **Mechanism**: "LSL's timestamping function returns the time of the most steady (i.e.,
  monotonically increasing) high-precision computer clock available that has a minimum resolution
  of 1 msec or better (typically the machine uptime). The time offset between multiple computers'
  clocks, as well as their relative drift, is continually measured" and corrected.
- **What it replaces**: the paper's own framing of the alternative is that "'start/stop' events"
  are insufficient because "such a setup may cause synchronization to drift by many milliseconds
  within mere minutes of data collection". On hardware alternatives the paper says: "Recent
  advances in hardware-managed synchronization can improve common clock accuracy for digitally
  triggered events to tens of microseconds, including solutions based on shared clocks and
  analog-to-digital (A/D) converters [Chuang et al., 2021] and radio-frequency trigger modules
  [Cerone et al., 2022]. However, the use of hardware data synchronization approaches is very often
  not feasible in laboratories without resources to engineer special-purpose solutions". The
  precision time protocol is named separately as an alternative that "requires dedicated hardware",
  with no precision figure attached.

  **Corrected 2026-08-01, Phase 4 audit.** This bullet previously attributed the tens-of-microseconds
  figure to "transistor-transistor logic pulse trains, dedicated clock channels, the precision time
  protocol", and the Citations block attributed it to Artoni et al. (2017). Neither matches the
  source. The tens-of-microseconds claim belongs to Chuang et al. (2021) and Cerone et al. (2022),
  for shared clocks / A-D converters and radio-frequency trigger modules. Artoni et al. (2017) is
  cited for a different and coarser figure: "A recent study of multimodal MoBI data collection
  methods concluded that frequent TTL pulses are needed to retain millisecond synchronization
  between data streams [Artoni et al., 2017]" — milliseconds, not microseconds.
- **Container format**: recordings are written by LabRecorder to XDF, which is the format most
  multi-stream MoBI datasets in this area are distributed in or converted from.
- **Citation position**: this is one of the 2 works citing `strum-2018`.

## Open questions / limitations

- The stated hard limit, from the authors: LSL timestamps a sample when the operating system
  receives it, not when the sensor acquired it. Every reported number is therefore a measure of
  transport-and-clock behaviour, not of end-to-end acquisition latency, and per-device offsets
  must be characterised separately by whoever builds the rig.
- The reported figures come from a small number of specific device pairings — BioSemi with a
  National Instruments card, and one EEG-plus-EMG combination. The paper is explicit that
  performance "varied significantly with device type and parameter settings", so these numbers do
  not transfer to an arbitrary rig.
- The single-machine and networked offsets differ by a factor of two (12.20 ms versus 6.26 ms) and
  the paper offers only a hypothesis for why. A reader should not treat either figure as the
  expected offset for a new setup.
- No multi-*participant* synchronisation test is reported. Everything measured is multi-*device*.
  Whether two separately capped participants on two amplifiers achieve the same sub-millisecond
  jitter is a reasonable extrapolation, not a published result.
- The preprint carries no open licence (see `meta.json`), so only the extraction is held here and
  the numbers above should be re-checked against the published version when one exists.

## Citations

Primary: `lsl-2024`

- `strum-2018` — cited by this paper; one of only two works that cite it.
- `boa-actors-2025` and `livewire-2024` — the two multi-person EEG datasets carded here, both of
  which synchronise by trigger rather than by LSL and neither of which reports a measured error.
- `hinss-2023-passive-bci` — a dataset in this strand that does use LSL, distributing its event
  markers as an "LSL trigger list".
- Chuang et al. (2021) and Cerone et al. (2022) — the hardware-synchronisation alternatives this
  paper positions LSL against, reaching tens of microseconds at the cost of dedicated hardware.
- Artoni et al. (2017) — cited by this paper for the weaker claim that frequent TTL pulses are
  needed to retain *millisecond* synchronisation in MoBI recordings. (Artoni is also a co-author of
  this paper; the 2017 work is a separate study.)
