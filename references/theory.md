# Design-Space Compression Theory

## Purpose

Use this reference to decide whether a proposed rail removes harmful entropy or merely moves complexity.

## Model

Let:

- `S` be the set of implementations an agent could generate.
- `V` be the subset accepted mechanically by the repository.
- `D` be the subset aligned with intended architecture.

A prompt-heavy repository often has `D` much smaller than `V`. The agent must infer the preferred path from prose and local examples.

The goal of Agent Rails is to reshape the repository so `V` approaches `D` while preserving legitimate flexibility.

## Design-Space Compression Principle

Remove invalid implementation paths when the repository can express the invariant more reliably than prose.

Prefer:

- one domain operation over repeated orchestration;
- a forbidden import over a warning not to import it;
- a type that makes an invalid state unrepresentable over a comment describing the state;
- a deterministic verification command over reviewer intuition.

## Minimum Necessary Constraint Principle

Not every difference is entropy. Preserve choices that encode meaningful product, performance, compatibility, deployment, or domain tradeoffs.

Before constraining a choice, ask:

1. Do multiple valid outcomes genuinely need this freedom?
2. Has the freedom caused repeated mistakes or review burden?
3. Can the invariant be expressed locally and mechanically?
4. Can a future exception be handled through a clear escape hatch?
5. Will the rail remove more concepts than it introduces?

If the answer to 1 is yes and the others are weak, do not add the rail.

## Repository as policy model

Treat knowledge layers as progressively stronger forms of repository memory:

1. Prompt instruction
2. Documentation
3. Verification command
4. Test or static analysis
5. Framework/domain primitive
6. Dependency boundary
7. Type or language impossibility

Moving an invariant downward reduces context that future agents must load and reason about. Move it only when the lower layer stays simpler than the behavior it replaces.

## Optimization target

Do not optimize for architectural elegance in isolation. Optimize for:

- probability of correct agent completion;
- reduced number of implementation decisions;
- lower context and exploration burden;
- fast, local failure feedback;
- preserved behavior;
- low maintenance cost of the rail itself.

A rail that looks clean but does not change agent behavior is decorative.
