---
name: agent-rails
description: Convert recurring coding-agent mistakes, duplicated architectural decisions, unsafe low-level access, and inconsistent implementation paths into durable repository constraints. Use when hardening an existing codebase for AI coding agents; designing agent-native architecture; replacing free-form implementation choices with approved primitives, factories, helpers, module boundaries, lint rules, type constraints, tests, or verification commands; reducing agent context/token needs; or turning repeated review feedback and AGENTS.md/CODING_STANDARDS.md instructions into mechanically enforced invariants.
---

# Agent Rails

## Mission

Reduce the implementation design space available to future coding agents by compiling recurring engineering judgment into repository primitives and mechanically enforced invariants.

Treat the repository as the durable policy model. Treat prose as the weakest enforcement layer.

## Constitution

MUST obey all rules below.

1. Never fix a repeatable mechanically enforceable mistake with documentation alone.
2. Never add an abstraction unless it removes more implementation decisions than concepts it introduces.
3. Never add a rail without proving an intentional bypass fails.
4. Never leave two blessed implementation paths unless coexistence is explicitly required.
5. Never refactor unrelated code while installing a rail.
6. Never weaken existing tests, types, linting, or verification to make a rail pass.
7. Prefer native language, type-system, dependency, and build-system mechanisms over custom frameworks.
8. Keep the approved path easier to discover and cheaper to use than the bypass path.
9. Preserve escape hatches only when they are explicit, rare, searchable, and reviewable.
10. Harden one seam at a time unless multiple seams are inseparable.
11. Characterize existing behavior before prohibiting the old path.
12. Do not create a framework merely because several primitives exist. Require a real shared lifecycle or invariant.

## Core model

Model three sets:

- `S`: implementations an agent could generate.
- `V`: implementations mechanically valid in the repository.
- `D`: implementations consistent with intended design.

Drive `V` toward `D` without eliminating legitimate product or engineering flexibility.

Use two governing principles:

- **Design-space compression:** remove an invalid path instead of repeatedly teaching agents to avoid it.
- **Minimum necessary constraint:** remove a degree of freedom only when that freedom has no meaningful engineering value.

Read `references/theory.md` when reasoning about whether a proposed constraint is justified.

## Operating loop

Execute this loop in order:

`OBSERVE -> CLASSIFY -> COMPRESS -> PROVE -> VERIFY -> RETRO`

### 1. OBSERVE

Inspect only the requested repository area or the smallest relevant dependency neighborhood.

Find entropy hotspots such as:

- repeated low-level calls;
- duplicated validation, error translation, persistence, event publication, or state transitions;
- multiple implementations of the same concept;
- bypasses around an intended domain boundary;
- recurring review comments or agent mistakes;
- large prompt/documentation rules that could be executable;
- workflows future agents cannot verify deterministically.

Describe each hotspot as **freedom exposed**, not merely bad code.

Example:

`Assessment creation exposes six repeated decisions across fourteen callsites: validation, ID generation, persistence, audit logging, event publication, and error translation.`

Do not patch during OBSERVE.

Read `references/entropy-taxonomy.md` for classification cues.

### 2. CLASSIFY

Assign each hotspot exactly one primary class:

- `A Knowledge problem`
- `B Repeated decision`
- `C Unsafe capability`
- `D Architectural divergence`
- `E Verification gap`

Rank candidates by frequency, blast radius, future-agent likelihood, enforcement feasibility, and expected design-space reduction.

Select one seam unless the user explicitly requests a broader program.

### 3. COMPRESS

For the selected seam, produce two candidate constrained designs unless one mechanism is overwhelmingly dominant.

For each candidate specify:

- invariant;
- approved primitive/interface;
- decisions hidden by the primitive;
- old path to prohibit;
- enforcement mechanism;
- migration plan;
- escape hatch, if any;
- positive verification;
- adversarial bypass verification;
- expected decisions removed;
- concepts introduced.

Reject any candidate where concepts introduced are not clearly lower than decisions removed.

Choose the strongest simple enforcement available. Consult `references/enforcement-ladder.md` and `references/primitive-design.md`.

Score competing candidates with `scripts/score_candidate.py` when the tradeoff is non-trivial. Read `references/scoring-rubric.md` before scoring.

If the user asked only for analysis or a proposal, stop after recommending a design. If the user explicitly asked to implement or install rails, treat that as permission to modify the scoped area. Pause for a choice only when two candidates have materially different product/architecture consequences that cannot be inferred safely.

### 4. INSTALL

When implementation is authorized:

1. Characterize current behavior with tests or executable examples.
2. Add the smallest approved primitive or boundary.
3. Migrate existing callsites in scope.
4. Add mechanical enforcement against the obsolete path.
5. Add or update concise repository guidance (`AGENTS.md`, `CODING_STANDARDS.md`, or equivalent) to point to the primitive and verification command; do not duplicate implementation detail there.
6. Add a rail record under `.agent-rails/manifest.json` when the repository accepts project metadata.
7. Keep the diff local and reviewable.

Use `assets/manifest.example.json` as the manifest shape. Validate a manifest with `scripts/check_manifest.py`.

### 5. PROVE

A rail is incomplete until an intentional bypass fails.

Create a temporary or fixture-level invalid implementation that violates the invariant. Run the enforcement mechanism and require failure. Remove or isolate the violation. Run the approved implementation and require success.

The failure message SHOULD state:

- what violated the invariant;
- why the path is forbidden;
- which primitive or path to use instead.

Use `scripts/adversarial_verify.py` when a pass command and a deliberate-failure command can be expressed independently.

Read `references/verification-contract.md` before claiming a rail is complete.

### 6. VERIFY

Run both structural and behavioral verification.

Structural verification includes relevant combinations of:

- compiler/type checks;
- import/dependency checks;
- lints/static analysis;
- unit/integration tests;
- architecture checks.

Behavioral verification proves the actual user/developer workflow still works through the public surface where practical.

Do not claim success from lint/types/tests alone when the affected workflow can be exercised directly.

### 7. RETRO

For every correction discovered during implementation or review, ask:

`Can the environment prevent this class of mistake permanently?`

If yes, record the next candidate rail. If no, document only the irreducible judgment.

Move knowledge down this compilation path whenever justified:

`prompt -> documentation -> verification -> lint/static check -> primitive/API -> dependency boundary -> type/language impossibility`

Do not move downward when doing so creates more complexity than it removes.

## Output contract

For an assessment-only run, return:

1. **Selected seam** - one sentence.
2. **Evidence** - concrete callsites/patterns.
3. **Freedom exposed** - decisions the current code repeatedly asks agents to make.
4. **Candidate designs** - two when useful.
5. **Score and recommendation** - explain the decisive tradeoff.
6. **Exact rail** - primitive + prohibition + enforcement + verification.
7. **Expected compression** - what future agents no longer need to decide or remember.
8. **Risks / escape hatch** - only material risks.

For an implementation run, additionally report:

- files changed;
- old path removed or blocked;
- positive proof result;
- adversarial bypass result;
- behavioral verification result;
- next highest-value candidate, if one emerged.

## Progressive references

Load only what the current step requires:

- Theory and decision-space model: `references/theory.md`
- Entropy classification: `references/entropy-taxonomy.md`
- Primitive quality and anti-framework checks: `references/primitive-design.md`
- Enforcement selection: `references/enforcement-ladder.md`
- Candidate scoring: `references/scoring-rubric.md`
- Proof and verification requirements: `references/verification-contract.md`
- Incremental adoption in existing repositories: `references/adoption-playbook.md`

## Completion gate

Do not mark an implemented rail complete unless all are true:

- the intended behavior is characterized;
- the approved path exists and is easier to use;
- scoped callsites are migrated;
- the bypass is mechanically blocked or intentionally documented as unpreventable;
- an adversarial bypass was tested;
- structural verification passes;
- behavioral verification passes when practical;
- repository guidance points to the approved path;
- no unrelated architecture was rewritten.
