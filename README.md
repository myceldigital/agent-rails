# Agent Rails

Agent Rails is a ChatGPT Skill for turning recurring coding-agent mistakes and repeated architectural decisions into durable repository constraints.

The central idea is simple:

> Do not keep teaching an agent to avoid the wrong path when the repository can remove that path.

Instead of relying on large prompt files, Agent Rails progressively compiles engineering judgment into primitives, type constraints, dependency boundaries, lint/static checks, tests, and verification commands. The target is a codebase where the mechanically valid implementation space is close to the intended design space.

## What it does

Agent Rails runs a six-stage loop:

1. **Observe** - find places where agents are forced to make repeated or unsafe decisions.
2. **Classify** - distinguish knowledge problems, repeated decisions, unsafe capabilities, architectural divergence, and verification gaps.
3. **Compress** - design a smaller approved path and the simplest reliable enforcement.
4. **Prove** - deliberately attempt the forbidden path and require it to fail.
5. **Verify** - prove both structural correctness and the affected workflow.
6. **Retro** - turn new recurring mistakes into the next rail.

## Skill structure

```text
agent-rails/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── adoption-playbook.md
│   ├── enforcement-ladder.md
│   ├── entropy-taxonomy.md
│   ├── primitive-design.md
│   ├── scoring-rubric.md
│   ├── theory.md
│   └── verification-contract.md
├── scripts/
│   ├── adversarial_verify.py
│   ├── check_manifest.py
│   └── score_candidate.py
└── assets/
    ├── agents-section.md
    └── manifest.example.json
```

## Core rules

- No documentation-only fix for a mechanically enforceable recurring mistake.
- No abstraction unless it removes more decisions than concepts it introduces.
- No rail without an adversarial bypass test.
- No competing blessed paths without explicit justification.
- No unrelated refactors while hardening a seam.
- Prefer native language/build-system mechanisms over custom frameworks.
- Make the correct path easier to discover and cheaper to use than the bypass.

## Example prompts

- "Audit this repository for the highest-leverage Agent Rails opportunity. Do not modify anything yet."
- "Agents keep importing the raw DB client from feature code. Harden this so the wrong path fails mechanically."
- "Turn the repeated review feedback in this PR history into primitives and lint/type constraints."
- "Reduce the design space for adding new API endpoints without building a giant internal framework."
- "Evaluate whether this helper is a real deep primitive or just another abstraction layer."

## Deterministic helpers

Score a candidate design:

```bash
python scripts/score_candidate.py candidate.json
```

Validate an Agent Rails manifest:

```bash
python scripts/check_manifest.py .agent-rails/manifest.json
```

Verify that the approved path passes and a deliberate bypass fails:

```bash
python scripts/adversarial_verify.py \
  --pass-cmd "pnpm check:architecture" \
  --fail-cmd "pnpm test:architecture-bypass-fixture"
```

## Philosophy

Agent Rails treats the repository itself as an externalized policy model. Prompt instructions and standards files remain useful for irreducible context, but recurring mechanical rules should migrate toward executable enforcement.

The goal is not maximum restriction. It is **minimum necessary constraint**: remove only degrees of freedom that create entropy without carrying meaningful engineering value.
