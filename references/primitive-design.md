# Primitive Design

## Primitive test

Approve a primitive only when it hides several coherent decisions behind a smaller, stable interface.

A good primitive:

- represents a domain action or infrastructure policy;
- owns validation/invariants that every caller should share;
- reduces caller decisions;
- is easy to discover from nearby code;
- produces obvious errors;
- can be verified independently;
- does not absorb unrelated responsibilities.

## Compression ratio

Estimate:

`compression = decisions removed / concepts introduced`

Do not treat this as precise mathematics. Use it as a forcing function.

Prefer primitives where the numerator is clearly larger than the denominator.

Example:

`createAssessment(input)` may remove repeated decisions about validation, identifiers, persistence, auditing, event publication, and error mapping while introducing one domain operation.

## Deep module vs god abstraction

A deep module has a small interface over substantial coherent behavior.

A god abstraction has a small-looking interface that entangles unrelated domains or changes for many unrelated reasons.

Reject a primitive when:

- its parameters expose most hidden implementation choices anyway;
- callers frequently need escape flags;
- unrelated features cause it to change;
- it centralizes code without centralizing an invariant;
- it merely renames one or two existing calls;
- understanding it requires learning more concepts than the raw path.

## Correct path as shortcut

The approved path should be the path an uninstructed competent agent is most likely to discover and choose.

Improve discoverability through:

- domain naming;
- colocated interfaces;
- examples at the boundary;
- compiler/lint messages that name the replacement;
- fewer parameters and setup steps than the low-level path.

Do not rely on an agent remembering a distant standards document.

## Escape hatches

Allow an escape hatch only when legitimate exceptions exist.

Make it:

- explicit in its name;
- narrow in capability;
- searchable;
- locally documented with allowed reasons;
- optionally guarded by a lint suppression requiring rationale.

Prefer `unsafeRawDatabaseAccessForMigration(...)` to re-exporting the unrestricted database client.

## Framework emergence rule

Do not build an internal framework because several helpers exist.

Require at least one shared property such as:

- lifecycle;
- state model;
- registration/discovery mechanism;
- cross-cutting invariant that cannot stay local;
- common verification/runtime contract.

If independent primitives remain simpler, keep them independent.
