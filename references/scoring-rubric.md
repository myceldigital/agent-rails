# Candidate Scoring Rubric

Use this rubric when two or more plausible rails have non-obvious tradeoffs.

Score every dimension from 0 to 5, where 5 is best.

| Dimension | Weight | 5 means |
| --- | ---: | --- |
| decisions_removed | 25 | Removes many recurring implementation choices |
| bad_paths_eliminated | 20 | Makes the known failure modes mechanically impossible or immediately failing |
| simplicity | 15 | Small mechanism with low conceptual/maintenance overhead |
| discoverability | 10 | An uninstructed agent is likely to find and choose the approved path |
| enforcement_strength | 10 | Violation fails early, locally, and reliably |
| verification_quality | 10 | Positive and adversarial proof are deterministic and fast |
| migration_safety | 5 | Can be introduced incrementally with low behavioral risk |
| escape_hatch_quality | 5 | Legitimate exceptions stay explicit and controlled |

Weighted score is out of 100.

## Hard rejection gates

Reject regardless of score if any is true:

- abstraction introduces at least as many concepts as decisions it removes;
- enforcement cannot be tested adversarially;
- design requires unrelated refactors;
- approved path is harder to use than the bypass path without a compelling safety reason;
- migration changes product semantics without explicit authorization;
- rule encodes an unresolved product decision as architecture.

## Interpretation

- 85-100: strong rail; implementation is usually justified.
- 70-84: useful but inspect complexity/escape hatch carefully.
- 55-69: weak compression; redesign before installing.
- below 55: do not install.

Use `scripts/score_candidate.py <candidate.json>` for deterministic calculation.
