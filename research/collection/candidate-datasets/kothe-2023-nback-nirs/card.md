---
slug: kothe-2023-nback-nirs
type: paper
strand: candidate-datasets
year: 2023
authors: [Kothe, Hanada, Mullen S, Mullen T]
venue: arXiv preprint 2312.07546
doi: 10.48550/arXiv.2312.07546
url: https://arxiv.org/abs/2312.07546
license: CC BY 4.0 (arXiv)
modalities: [nirs, high-channel-nirs]
tags: [label-provenance, task-difficulty-label, n-back, workload, intheon, leave-one-subject-out, transfer-learning, high-channel-count, not-eeg]
relevance: low
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

A working-memory-load decoder on 43 participants wearing a 3,198 dual-channel NIRS device, carded
here only for how its label was defined: the class is the experimental parameter *n* in the n-back
task, balanced and pseudo-randomised by design, with no self-report or behavioural component in the
label at all.

## Summary

The paper's own contribution is methodological — a spatio-temporal regularisation plus
cross-subject transfer strategy for the high-channel NIRS regime, interpretable as an end-to-end
generalised linear model — and it reports that replicated state-of-the-art approaches "struggle in
the high-channel regime and are largely outperformed by the proposed method". The experimental
design is what this strand cards. Forty-three participants completed four task sets, each of three
3-minute n-back blocks interleaved with two 2-minute Montreal Imaging Stress Task blocks (only the
n-back is analysed). Each n-back block held *n* constant and contained three successive 55-second
trials, each with 20 letter presentations (6 targets) drawn from 18 consonants, 0.5 s stimulus and
1.5 s inter-stimulus interval, 40 s of task performance per trial. "Conditions for n were limited
to 0, 1, 2 and were balanced and pseudo-randomized across blocks, sets, and participants, yielding
36 total trials per session." Classification was binary between any two levels — 0 versus 1,
0 versus 2, 1 versus 2 — with subject-independent methods evaluated leave-one-subject-out and
subject-specific methods evaluated with 4-fold blockwise cross-validation whose test partitions are
the four experimental task sets. Best reported setup: 0 versus 2 on the quality-filtered session
subset, 71.5 ± 9.2 %.

## Relevance to the review

The strand brief admits this entry for one narrow purpose — how the workload label was defined and
validated — and marks it low relevance unless the label reasoning transfers. It partly does, in a
way that is instructive by contrast with the project's plan.

The label here is a pure experimental-parameter label: the class *is* the value of *n* the
experimenter set. That has the same formal structure as the project's spoken-versus-written plan —
the label is a property of the stimulus regime, not of a measured mental state — but it differs in
one decisive respect. The n-back manipulation is designed so that the only systematic difference
between conditions is how much has to be held in working memory: the letters, timing, target rate,
motor response and screen appearance are identical across *n*. Spoken versus written has no such
property. Changing presentation modality changes the sensory channel, the stimulus timing profile
(auditory stimuli are extended in time, visual ones are not), and the sensory cortex responding,
all at once. So the n-back label supports a cognitive reading because the design equates everything
else, and the spoken-versus-written label does not inherit that support.

The second transferable element is the split protocol. The subject-specific evaluation uses
blockwise cross-validation with the four experimental task sets as the folds, so temporally
adjacent trials never straddle a fold boundary — a discipline directly applicable to a small
within-subject EEG dataset, where random trial-level splits leak through temporal autocorrelation.

There is also a provenance note: three of the four authors are at Intheon, and two of them
(Christian Kothe and Tim Mullen) are STRUM authors. This is the closest visible published work by
that group to a decoding study on a workload-style label.

## Notable details

- **Label type**: task difficulty as an experimental parameter, *n* ∈ {0, 1, 2}. Not self-report,
  not behavioural performance, not physiological proxy.
- **Label validation**: none reported beyond the design itself. The paper reports no subjective
  workload scale (no NASA-TLX, no Karolinska scale) and no analysis relating behavioural accuracy
  to the label, so the label's construct validity rests entirely on the n-back paradigm's
  established status. Contrast `hinss-2023-passive-bci`, which validates its task-difficulty labels
  against subjective scales and behavioural performance.
- **Design equating**: "Conditions for n were limited to 0, 1, 2 and were balanced and
  pseudo-randomized across blocks, sets, and participants". The 0-back case is handled by reserving
  a fixed target letter (X, excluded from the stimulus set for the other conditions) so the motor
  response rate is comparable.
- **Trial structure**: 36 trials per session; 55 s per trial of which 40 s is task performance; 20
  stimulus presentations per trial with 6 targets.
- **Participants and device**: 43 participants; a 3,198 dual-channel NIRS device. The paper frames
  the high channel count as the source of the "severely under-determined estimation problems" its
  method addresses — NIRS "is typically limited by few training trials".
- **Split protocol**: leave-one-subject-out for the two subject-independent methods, "using no data
  from the target subject"; 4-fold blockwise cross-validation for subject-specific methods, folds
  aligned to the four experimental task sets.
- **Headline number**: 71.5 ± 9.2 % for 0-back versus 2-back on the quality-filtered ("OK") session
  subset, used as the starting point for an ablation in which "each model aspect contributes to the
  overall performance".
- **Session exclusion**: results are reported both on an "ALL" subset of 43 sessions with no
  exclusion and on a filtered "OK" subset, so a data-quality exclusion is applied and reported
  rather than hidden.

## Open questions / limitations

- Different modality. This is near-infrared spectroscopy, a haemodynamic measure at a timescale
  of seconds; nothing about signal properties, preprocessing or model architecture transfers to
  EEG. Only the label logic and the split protocol do, which is why relevance is low.
- The label is never validated against anything external. If the question is whether a
  task-parameter label supports a cognitive claim, this paper assumes the answer rather than
  testing it.
- Binary classification between pairs of *n* levels at around 71 % is modest, and the paper does
  not report what a within-subject chance-level permutation distribution looks like, so how far
  above chance that is under the blockwise split is not stated in what was read.
- The "ALL" versus "OK" session subsets mean two numbers exist for every result; the card quotes
  the OK-subset figure because it is the one the paper uses as its ablation baseline, and this is
  flagged so a later reader does not treat 71.5 % as the headline for all 43 sessions.
- No peer-reviewed version was located; this is an arXiv preprint.

## Citations

Primary: `kothe-2023-nback-nirs`

- `strum-2018` — same group; two of this paper's authors are STRUM authors.
- `hinss-2023-passive-bci` — the EEG counterpart with an n-back among its four tasks, and with the
  label validation this paper lacks.
- `lsl-2024` — also from the Intheon/SCCN orbit; the recording toolchain context.
- Kirchner (1958) — the origin of the n-back paradigm whose established status the label leans on.
- Dedovic et al. (2005), Montreal Imaging Stress Task — the interleaved task in the same sessions,
  not analysed in this paper, which means additional unanalysed data exist in the same recordings.
