---
slug: guetschel-2024-representation-learning-review
type: paper
strand: eeg-models
year: 2024
authors: [Guetschel, Ahmadi, Tangermann]
venue: Journal of Neural Engineering 21(6):061002
doi: 10.1088/1741-2552/ad8962
url: https://arxiv.org/abs/2405.19345
license: CC BY 4.0
modalities: [scalp-eeg, bci-eeg, sleep-eeg]
tags: [review, pretext-task-taxonomy, autoencoder, gan, self-supervised-learning, metric-learning, embedding-introspection, linear-probing, benchmark-gap, transfer-learning-motivation]
relevance: medium
imported_from: null
added: 2026-07-31

# Archival fields
pdf_status: archived
pdf_path: source.pdf
md_path: source.md
md_quality: clean
---

## TL;DR

A survey of 81 BCI representation-learning articles finds that half use autoencoders, only 13 use
self-supervised learning (ten of them from 2022 onward), and none has produced a foundation model
the BCI community actually adopted — with most authors treating the learned embedding as a side
product they never inspect.

## Summary

Guetschel, Ahmadi and Tangermann review deep representation learning for EEG decoding along three
axes: which technique is used, why the authors wanted an embedding, and how (or whether) they
characterized what was learned. The technique taxonomy covers autoencoders and their variants,
self-supervised learning with pseudo-labels, generative adversarial networks, and metric learning,
with pretext-task-versus-downstream-task framing throughout. The motivation taxonomy is the
review's more distinctive contribution: it separates transfer learning (the dominant reason) from
learning robustness or invariance, from using an embedding as an algorithmic bridge between
components, from uncovering the structure of the data. The third axis is introspection — the
review catalogues the available techniques (downstream score, pretext score, low-dimensional
projections with various colourings) and finds most articles use none of them. It closes with four
recommendations: introspect learned embeddings; build EEG-specific foundation models with SSL;
assemble large unlabelled EEG datasets to train them on; and build benchmarks beyond BEETL with
fixed fine-tuning procedures.

## Relevance to the review

Carded under category 1 because what it supplies is a map of pretraining objectives and the
reasons for choosing between them, rather than evidence that any of them work. Its most useful
content for this project is methodological.

The review states the trade-off the project's first two comparisons instantiate: supervised
training "produces representations that are very targeted, which means they are typically not
transferable to other tasks and sometimes not to other distributions as well", against pretext
training, whose value depends on "how similar a particular pretext task is compared to actual BCI
tasks... whether a given pretext task is general enough". That is the question this project asks
of a checkpoint, phrased as a property of the objective rather than of the checkpoint.

It also argues specifically for linear probing as the evaluation protocol, on a ground that is not
about accuracy: training a linear classifier on frozen representations "produces reproducible
results, and its simplicity favours methods able to extract representations which are easy to
classify... It thus may not obtain the best classification scores, but this is not crucial for
benchmarking purposes." It adds the caveat that linear probing "is not always possible... depending
on the SSL strategy used".

Finally, the review names the trap in reading any baseline comparison in this literature: "there is
always a concern that authors applying a method as a baseline may not be using it to its fullest
potential, whether intentionally or not. For instance, a baseline method may be poorly optimized or
implemented, leading to sub-optimal results." That caution applies to every transfer number this
strand has collected.

## Notable details

- **Pretraining corpus and total hours**: not applicable. The review trains nothing. On corpora it
  observes that foundation models will need "extremely large, but not necessarily labelled
  datasets", that in other domains those came from very diverse sources, and that the Temple
  University Hospital EEG corpus "might be such a resource and has already been explored by Kostas
  et al. to train a SSL model, but we still lack hindsight on whether this corpus is a good
  dataset for training foundation models".
- **Parameter count**: not applicable. No model is proposed and the review does not tabulate model
  sizes for the articles it surveys.
- **Input contract**: not applicable. The review does not compile input contracts, which is itself
  a gap given that its own recommendation is to build benchmarks with "a deterministic fine-tuning
  procedure".
- **Most informative transfer number, with baseline**: `not reported`. This is a survey with no
  experiments of its own, and it does not aggregate the surveyed articles' accuracies into any
  comparable quantity — there is no results table anywhere in it (the word "Table" does not occur
  in `source.md`; the only two matches are inside "unstable" and "interpretable"). Its quantitative
  content is entirely bibliometric: 81 articles reviewed in depth; autoencoders reported three
  different ways (see limitations); and 13 using SSL of which ten were published in 2022 or later
  — "We identified 13 studies employing self-supervised learning (SSL) techniques, among which ten
  were published in 2022 or later".
- **GANs, corrected during the Phase 4 audit.** An earlier version of the bullet above said
  "approximately a quarter using GANs though 'none of the surveyed articles employed GANs for the
  purpose of EEG representation learning'". Both halves are wrong. No proportion of articles using
  GANs is stated anywhere; the word "quarter" does not appear in the source. And the quoted string
  is not in the paper. What the paper says, verbatim, is: "In the context of BCIs, we did not find
  any article using them for that purpose, but it could be worth investigating this further" —
  i.e. *zero*, not a quarter, and phrased as a research gap rather than a count. The paper's
  reason: "GANs are known to be difficult to train (long and unstable) such that their use as
  unsupervised feature extractors remains marginal in general." What changes: GANs are in the
  review's taxonomy as an unexplored option for BCI, not as a used technique, which strengthens
  rather than weakens the review's gap-finding.
- **The negative headline**: "none of these have led to standard foundation models that are picked
  up by the BCI community", and "there currently is no such model that has been widely adopted by
  the BCI community". As of the review's cutoff, adoption rather than publication is the missing
  step.
- **Embeddings as a side product**: "the authors often learned an embedding as a side product of
  the method they use rather than as an explicit objective. In most cases, they ignore the obtained
  embedding and continue with their primary task despite the large panel of introspection
  techniques available." Where introspection does happen, the review reports it is "shallow and
  limited to simple score comparisons with a few baselines".
- **Benchmark gap**: "To our knowledge there currently is only one standard benchmark for
  cross-dataset transfer in BCI", BEETL, which "still leaves room for improvement". The review
  argues a single downstream task is insufficient for a generality claim and calls for a GLUE-like
  set of tasks with a fixed fine-tuning procedure.
- **Two fine-tuning strategies compared as protocols, not as results**: full fine-tuning on the
  target distribution, which "can be computationally heavy and may easily overfit depending on the
  amount of fine-tuning data"; and linear probing on frozen representations, which is reproducible
  but not score-maximizing.
- **Introspection techniques catalogued**: downstream-task score; pretext-task score (noted as
  poor for cross-method comparison because each pretext task has its own intrinsic metric);
  low-dimensional projection plots coloured by downstream label, age, gender, date, pathology,
  continuous behavioural labels, subject identity, or train-versus-test membership — the last
  offered as a way to inspect non-stationarity between splits.
- Motivations for learning an embedding, in the review's taxonomy: transfer learning (dominant),
  learning robustness or invariances, use as an algorithmic bridge, and uncovering the structure of
  the data. Multi-task learning is described as the standard route to invariance, with subject
  invariance the worked example.

## Open questions / limitations

- **It predates the models this strand is built on.** The arXiv version is May 2024 and the
  version of record October 2024; LaBraM appeared in 2024 and CBraMod, EEGPT, REVE and the
  benchmark papers later. The claim that no EEG foundation model has been adopted by the BCI
  community is therefore a statement about the field before the models this project would actually
  use existed. It should be cited for its taxonomy and its methodological cautions, not for its
  verdict on adoption.
- No quantitative synthesis is attempted. The review counts articles by technique but never
  compares the techniques on any outcome, so it cannot support a claim that one pretext task
  transfers better than another — only that the field has tried each.
- The autoencoder count is given **three** ways, not two as an earlier version of this bullet said.
  The abstract states "a predominance of 31 articles using autoencoders" out of 81, which is
  38 percent. Section 2 states "Among the resulting 56+25 articles, many use similar techniques, in
  particular, 34 articles employed autoencoders to learn a representation." The discussion says
  autoencoder-based approaches account for "approximately half of the articles surveyed", which is
  about 40. The card records all three and adopts none; 31 and 34 are both specific and both stated
  by the authors, which is the self-contradicting-source case.
- **Selection reproducibility, corrected during the Phase 4 audit.** An earlier version said
  "no PRISMA-style flow, inter-rater agreement, or search-date cutoff is reported". One of those
  three is right. The search date *is* reported — "This search was conducted on April 1<sup>st</sup>
  2024" — along with a publication-year floor ("We restricted our search to articles published
  after 2014"), the two databases used and why Google Scholar was dropped, the 65-term query
  structure, and a title-only restriction. A selection flow *is* reported, with counts at every
  stage: 87 from Web of Science plus 43 from PubMed, 101 after deduplication, 76 after title
  screening, 67 after removing five paywalled, three non-English and one unavailable, 56 after
  abstract screening, plus 25 added post-search from reference sections and prior knowledge — and
  "A flow diagram summarizing the selection process is provided by Figure 1." What remains true is
  the absence of inter-rater agreement, and the fact that 25 of the 81 articles (31 percent) were
  added by author judgement outside the search protocol, which is the real reproducibility limit
  here rather than a missing flow diagram.
- The recommendations are unconditioned: they say what should be built, not what would count as
  evidence that it worked. The benchmark recommendation is the exception, specifying a fixed
  fine-tuning procedure and multiple tasks.
- The arXiv title block prints the first author's surname as "Gueschel"; the correspondence address
  (pierre.guetschel@donders.ru.nl), Crossref and OpenAlex all give "Guetschel", which is the form
  used here.

## Citations

Primary: `guetschel-2024-representation-learning-review`

- `bendr-2021` — cited (as Kostas et al.) as the one attempt the review knows of to train an SSL
  model on the Temple University Hospital corpus, in support of its dataset recommendation.
- `banville-2021-self-supervised-eeg` — among the SSL articles surveyed, and the closest prior
  work on pretext-task choice for EEG.
- Wei et al., BEETL (reference [121]) — the only standard cross-dataset transfer benchmark in BCI
  at the time of the review, and the baseline its benchmark recommendation is written against.
- Wang et al., GLUE (reference [119]) — the multi-task benchmark model the review asks the BCI
  field to imitate.
- Obeid and Picone, TUH EEG corpus (reference [78]) — the candidate pretraining corpus the review
  identifies while withholding judgement on its suitability.
