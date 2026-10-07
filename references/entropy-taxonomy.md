# Entropy Taxonomy

Classify each hotspot by its primary failure mode. Use the class to select a remedy; do not answer every problem with a wrapper.

## A. Knowledge problem

The implementation is structurally safe, but agents repeatedly lack a fact that cannot reasonably be encoded mechanically.

Examples:

- a business term has a non-obvious meaning;
- a migration must preserve a legacy external contract;
- a vendor has an operational quirk not represented in code.

Preferred remedies:

- concise repository documentation;
- named examples or fixtures;
- discoverable comments at the relevant interface.

Do not create code abstractions solely to hide domain knowledge that developers still need to understand.

## B. Repeated decision

Many callsites independently decide the same orchestration or policy.

Examples:

- validation + persistence + event publication repeated in routes;
- repeated pagination normalization;
- repeated auth and audit setup.

Preferred remedies:

- deep domain primitive;
- factory/helper with a small interface;
- template or generator only when variation is mechanical.

## C. Unsafe capability

A low-level capability is widely available where most callers should not possess it.

Examples:

- UI/features import a raw database client;
- arbitrary network client use bypasses policy;
- direct writes bypass audit or validation.

Preferred remedies:

- import/dependency boundary;
- capability-scoped interface;
- visibility/package restriction;
- explicit searchable escape hatch.

## D. Architectural divergence

Multiple patterns solve the same conceptual problem and force agents to choose among competing conventions.

Examples:

- three state-management patterns in one product surface;
- several ways to define jobs/events;
- old and new service layers both considered acceptable.

Preferred remedies:

- select one canonical path;
- migrate callsites;
- prohibit reintroduction of the obsolete path;
- document migration exceptions with sunset criteria.

## E. Verification gap

The repository cannot cheaply prove that a change works.

Examples:

- no stable command exercises a workflow;
- setup requires tribal knowledge;
- integration behavior is checked manually after review.

Preferred remedies:

- stable CLI/dev command;
- deterministic fixture/environment;
- smoke/integration test;
- fast reset/bootstrap path.

## Ranking candidates

Prioritize hotspots with:

- high recurrence;
- broad future-agent exposure;
- expensive review/rework;
- high blast radius when wrong;
- simple local enforcement;
- strong expected reduction in decisions.

Deprioritize one-off stylistic preferences, speculative abstractions, and areas with unresolved product semantics.
