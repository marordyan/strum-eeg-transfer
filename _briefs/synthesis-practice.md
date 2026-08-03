# Synthesis practice (read before writing any Phase 3 document)

Rules for the synthesis phase, in one place. Everything here comes from the Phase 3 pilot, which
wrote the `eeg-models` ontology first specifically to find these before three more documents were
written against a method that had never been used.

Collection practice governs how entries are made. This governs how they are organized.

## The test that shapes the document, applied first and not last

**Does this tell a Phase 4 reader anything the strand's `INDEX.md` does not?** If the answer is no,
the document is a table of contents with extra steps.

Apply it while choosing the structure, not as a final check. In the pilot it is what forced the
ontology away from the brief's collection categories, and discovering that at the end would have
meant a rewrite. A strand brief's categories are a *collection* instrument: they tell a collector
what to go and find, and they discriminate well on the provenance of a paper. They often
discriminate badly on the properties that distinguish entries from each other once collected. Depart
from them when that is true, and say why in the document.

## Facets, not one tree

A strict single-home hierarchy fights a corpus where every entry has a value on several independent
properties. Forced into one, it either duplicates entries or lies about them.

Use a small set of orthogonal facets, each a shallow tree, and make the **coverage table mandatory**:
every entry, its primary node, and everywhere else it appears. That table is what proves nothing was
dropped, and it replaces the pretence of a single home.

## The phase boundary, as a test rather than a prohibition

Phase 3 states **properties of entries and relations between them**. Phase 4 states **properties of
the set as a whole**: absence, coverage, sufficiency, whether the project should proceed.

So "these four checkpoints bind spatial identity to a learned per-channel parameter, and these three
compute it from coordinates" is synthesis. "No checkpoint handles a 206-channel montage" is gap
analysis, even though it follows from the same cards. When a sentence is genuinely borderline, keep
it if the register would be dishonest without it, and mark it.

## Citations

Cite at **claim level**, not per numeric fact. A link may be omitted inside a bullet whose leading
link already scopes it. The pilot cited every number and landed at one link per four lines, which is
auditable and hard to read; the point is that a reader can check any claim, not that every clause
carries its own footnote.

Every leaf of every facet is still a card link, and every entry in the strand still appears.

**Contradiction work reaches across strands, and cross-strand links are expected.** A disagreement
about a checkpoint's parameter count frequently sits between a model card and a benchmark card in
another strand. Reading only your own strand's directory is not sufficient to satisfy "name the
contradictions". Link `../collection/<other-strand>/<slug>/card.md` freely.

## Contradictions come in three kinds, and conflating them is a defect

1. **Cards disagreeing about the same quantity.** Record both, attribute both, pick neither.
2. **A source contradicting itself**, carded faithfully by its own card. Different thing: the
   disagreement is in the literature, not in our corpus.
3. **Roundings and unit conversions that only look like disagreements.** Record these too, precisely
   so a later reader does not promote one into kind 1.

Where a kind-1 disagreement turns out to be between two cards of the *same* paper, that is a defect
in the corpus rather than a fact about the field. A synthesis document cannot fix a card; say so and
name the entry, so it can be filed.

## Repetition is not evidence, but the comparator graph is structure

"Frequency of mention is not evidence weight" is a real rule: three cards repeating one vendor claim
is one claim. But the prohibition has a positive counterpart that Phase 4 needs.

**Who measures whom, and who copies whose baseline table, is genuine structure.** Record it as a
graph, and label it non-evidential. In the pilot it explained why two cards disagree about
ST-Transformer's parameter count: the split follows a copied-baseline chain rather than being
random.

## Carry the inaccessible-versus-unreported distinction into synthesis

Cards distinguish "the source does not report it" from "the source reports it and we could not read
it". That distinction must survive. A node keyed on a number will otherwise silently mix entries
whose value is genuinely absent with entries whose value we simply could not see, and those two have
opposite implications for whether re-retrieval is worthwhile.

Where a strand has more than one or two such entries, give them a node rather than a footnote.

## Clarifications from the three strand ontologies

Added after the pilot's method was used three more times. Each of these was a real ambiguity someone
had to resolve by judgment.

### A single exclusive partition is not the thing the facet rule forbids

"Facets, not one tree" reads as discouraging exclusive partitions, and it should not. Where a
property is genuinely exclusive, a strict partition over it is often the strongest structure in the
document: the `multimodal-biosignals` ablation axis assigns every one of 25 entries exactly one of
seven values, and that partition is what makes the strand answerable. What fails is making one
partition the *only* structure. Partition where the property is exclusive, facet where it is not.

### Registers may be dense; prose should not be

"Cite at claim level" governs prose. In a contradiction register the claim *is* the numeric fact, and
in a checkpoint-to-corpus mapping the value to Phase 4 is precisely that every cell is attributable.
Those sections run near one link per two lines and should. Do not thin a register to satisfy a rule
aimed at readability of argument.

### The phase boundary, sharpened by the case that was actually hard

The clean example, "no checkpoint handles 206 channels", is not the difficult shape. The difficult
shape is an absence that the cards state about themselves.

Use this test: **when the cards state the absence about themselves, quoting them is a property
statement and belongs to Phase 3. When only the synthesis can see the absence, it is coverage and
belongs to Phase 4.** Three critique cards each declaring that they do not measure the session-level
boundary is Phase 3; "no entry in the corpus pairs two frozen encoders" is Phase 4.

### Three patterns of repetition, not one

The pilot named copied baselines. Two more turned up, and they have different hazards.

1. **Copied baselines**: one measurement travelling through several papers' comparison tables. Record
   the chain; it explains disagreements that otherwise look random.
2. **Single-sourced descriptions**: several cards independently failing to obtain a fact from primary
   documentation and each falling back to the same secondary table, saying so honestly. The hazard is
   that a reader counts them as corroboration. Name the shared source, especially when that source is
   itself internally inconsistent about the fields being propagated.
3. **Genuine corroboration**: two first-party measurements agreeing. Log it as corroboration
   explicitly, so it is not mistaken for either of the above.

The comparator-graph rule is not universal. A dataset strand has no copied-baseline chain, because
datasets do not re-report each other's numbers. Do not manufacture a node to satisfy the rule.

## What the cross-cutting documents changed

The second pilot was the science map, and two rules above turned out to be within-strand
instruments rather than universal ones.

**The mandatory coverage table does not transfer.** A cross-cutting document has no strand whose
entries it must exhaust, and an entry participating in no cross-strand theme is correctly absent
rather than dropped. Substitute a matrix over whatever the document does have to exhaust: the
science map uses theme by strand, the scope diagram exhausts the briefs' out-of-scope sections.

**The value test needs its comparand swapped.** For an ontology it is "does this say anything the
strand's `INDEX.md` does not". For a cross-cutting document it is "anything the four *ontologies* do
not", which is a much harder bar and the reason several candidate themes were correctly rejected.

**A fourth kind of contradiction exists at cross-strand level**, which the three kinds above do not
name: one entry's method assessed against another entry's standard. Two ontologies hit it
independently and had no slot for it. It is neither a disagreement about a quantity nor a source
contradicting itself; record it separately so it is not promoted into kind 1.

## The `[boundary]` mark, and how it fails

Documents in this phase mark borderline phase-boundary sentences inline with `[boundary]`. Two
things about it, both learned from review.

It is a **flag, not a permission slip**. Review found the mark being used to keep a sentence that
`synthesis-practice.md` itself gives as the illustration of Phase 4 work. If a marked sentence would
survive deletion because the Phase 3 version is already on the page, delete it; the mark is for
sentences the register genuinely needs, not for conclusions that want to sneak past.

It is also **applied unevenly**: nine uses in one document, two in two others, none in the remaining
four, and several of the unmarked documents contain the breaches. An inconsistent convention gives
false assurance, since a reader takes the absence of marks for the absence of borderline cases.
Either mark everywhere or nowhere.

## The layer below keeps moving

Every wave of this phase found defects in the layer beneath it, and every fix to that layer left the
citing text stale. The synthesis documents quote cards verbatim; when a card is corrected, the
quotation becomes a claim about a file that no longer says it.

`tools/validate_corpus.py` now fails on any unresolvable link from `research/synthesis/`, which
catches renames and removals. It does **not** catch a quotation that no longer matches its source.
After correcting any card, grep the synthesis directory for the entry's slug and re-read every hit.

## Reviewing for correctness and attacking for refutation find different things

The strongest evidence this review produced about its own method came from Phase 4, where the gap
analysis was written and then handed to a second agent whose only instruction was to break it.

Before that pass, the corpus had been through collection with a pilot, four strand ontologies, a
cross-strand map, a scope diagram, and two full pull-request reviews. Every one of those layers read
the STRUM card. None noticed that its extraction stopped at Section IV, so the dataset paper's own
model comparison, its significance tests, and its authors' warning that the best models depend on eye
activity were invisible to the entire review. Four conclusions rested on the omission, including a
headline claim repeated to the user several times.

The refutation pass found it in one run. It also retracted four of eleven gaps, reversed both
headline arguments, and located three cards that contradicted their own sources.

The difference is in the question. A reviewer asks "is this well-supported?", which is answered by
checking that each claim has a citation and that the citation says what the text says. An attacker
asks "can I break this?", which sends them looking for the counterexample the author did not cite,
the source section the author did not read, and the step in the argument that does not follow. Those
searches go to different places. A well-cited claim built on an incomplete reading passes the first
test and fails the second.

So, as standing practice for any phase that produces a claim someone will act on:

- **Write and attack as separate jobs, by separate agents.** An author checking their own conclusions
  is grading their own homework, and will re-read the passages that supported the claim rather than
  the ones that might undermine it.
- **Instruct the attacker to default to refuted.** A claim survives only if an attempt to break it
  failed. "I could not find a counterexample" is a result; "this looks well-supported" is not.
- **Name the claims that matter most and say why**, so the attack is spent on the load-bearing ones
  rather than spread evenly.
- **Attack the attacker.** The refutation here contained four errors of its own, one of which
  attributed an inference to a paper that does not make it. Adversarial output is not authoritative
  merely because it is adversarial, and the revision pass should verify it the same way.
- **When a claim is refuted, keep it with what refuted it.** A retracted finding is evidence about the
  review's own error rate, and deleting it hides the one measurement of reliability the process
  produces.
