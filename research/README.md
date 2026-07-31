# Literature review corpus

This directory holds the corpus for the epic tracked in issue #3: a citation-traceable review of
electroencephalography (EEG) and multimodal biosignal modeling, the gaps that review exposes,
and the datasets that could close them. It follows the `manuscript:lit-review` full protocol.

## Reading order

A reader who has never seen this project should be able to reconstruct the argument by reading,
in order:

1. `_briefs/strand-*.md` at the repository root. What each strand was asked to collect, and on
   what criteria it was declared complete.
2. `research/collection/<strand>/INDEX.md`. What was collected, grouped by scope category.
3. `research/synthesis/`. Ontologies, the theme map, the dataset hierarchy, the scope diagram,
   and the gap analysis.
4. `direction-papers/`. The argument, with every claim linked back to a card.

Nothing load-bearing lives outside this layout. If a claim exists only in a conversation or a
scratch note, it is not yet part of the review.

## Layout

```
_briefs/                                   strand dispatch documents
research/
  collection/
    _schema/paper-card.md                  the card schema all entries follow
    <strand>/
      INDEX.md                             categorized one-line index
      <strand>.bib                         BibTeX for every entry in the strand
      <slug>/
        card.md                            structured summary, YAML frontmatter
        source.md                          markdown extraction or canonical README
        source.pdf                         only when redistribution is permitted
        meta.json                          provenance, license, redistribution flag
  synthesis/                               Phase 3 and Phase 4 outputs
direction-papers/                          Phase 5 outputs
```

Strands: `eeg-models`, `multimodal-biosignals`, `datasets-benchmarks`, `team-neuroergonomics`.
They partition the topic into methods, fusion, data, and application. The partition is chosen so
that no strand can be merged into another without losing a distinction the gap analysis needs.

## Traceability rule

A claim in synthesis or in a direction paper cites a specific card path, of the form
`[<slug>](../research/collection/<strand>/<slug>/card.md)`. A claim with no card link is a claim
that has not been grounded: either ground it by adding the card, or remove it. Frequency of
mention across the corpus is not evidence weight.

## License policy

`meta.json.redistribution_ok` is the single source of truth for whether `source.pdf` may exist
in an entry folder. Open-access papers, preprints, and author accepted manuscripts are archived
as PDFs. Paywalled papers are not: the markdown extraction is committed as research notes, the
PDF is not, and `notes` records where the text came from. Figures from paywalled papers are
referenced by number, never reproduced. When a license is unclear, the default is deny.

The full policy is `license-rules.md` in the `manuscript:lit-review` skill; the invariant that
no `source.pdf` exists where `redistribution_ok` is false is enforced by
`tools/validate_corpus.py` and by continuous integration.

## Validating the corpus

```bash
uv run python tools/validate_corpus.py
```

The validator checks structure, not judgment: required files, frontmatter fields and their
vocabularies, slug and strand agreement with the directory names, BibTeX coverage, index links,
and the license invariant. It also warns when more than 40 percent of a strand's entries are
marked `relevance: high`, which means the field has stopped discriminating. Whether a card is
any good is a reviewer's call, not the validator's.
