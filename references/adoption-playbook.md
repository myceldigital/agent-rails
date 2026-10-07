# Adoption Playbook

Use this reference when introducing rails into a large existing codebase.

## Sequence

Follow:

`observe -> characterize -> introduce seam -> migrate -> prohibit -> verify`

Do not start with repository-wide prohibition.

## Phase 1: inventory

Pick a bounded surface with repeated future work. Gather concrete callsites and recent mistakes. Avoid speculative platform work.

## Phase 2: characterize

Lock current intended behavior with tests or executable examples. Separate accidental behavior from contractual behavior.

## Phase 3: introduce the seam

Add the approved primitive alongside the old path. Keep the first implementation narrow.

## Phase 4: migrate

Move scoped callsites. Watch for exceptions; use them to test whether the primitive is too narrow or the domain truly needs an escape hatch.

## Phase 5: prohibit

After migration, mechanically block reintroduction of the obsolete path in the scoped region.

If the old path remains required elsewhere, scope the rule precisely rather than weakening it globally.

## Phase 6: verify

Run positive, adversarial, and behavioral proof.

## Phase 7: document only the interface

Update `AGENTS.md` or equivalent with the minimum discoverability statement:

- what primitive to use;
- where it lives;
- which verification command to run.

Do not duplicate the implementation rationale unless future maintainers need it.

## Rollout strategy

Prefer repeated narrow passes over a whole-repository framework migration.

Good early targets:

- high-frequency feature work;
- dangerous low-level capabilities;
- repeated review comments;
- cross-cutting operations with obvious invariants;
- areas with reliable tests.

Bad early targets:

- unstable product domains;
- one-off legacy subsystems;
- broad style preferences;
- abstractions awaiting a second real use case.
