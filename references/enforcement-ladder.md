# Enforcement Ladder

Choose the simplest mechanism that makes the invariant reliably fail fast.

## Strength order

1. Language/type impossibility
2. Visibility or dependency/import boundary
3. Capability-restricted API
4. Domain/framework primitive
5. Code-generation template
6. Static analysis or AST lint
7. Runtime assertion
8. Automated test
9. Verification CLI
10. Documentation
11. Prompt instruction

Strength is not a command to choose the highest item. Complexity matters.

## Selection rules

Prefer an existing mechanism before inventing a custom one.

Examples:

- Make a symbol private before writing a lint plugin.
- Use package/module boundaries before a repository-wide regex checker.
- Use the type system when the rule is naturally structural.
- Use AST linting when the forbidden pattern is syntactic and types cannot express it cleanly.
- Use runtime assertions for invariants dependent on runtime state.
- Use tests for behavior, not as the only guard against an easily detectable forbidden import.

## Failure quality

A good violation fails near the edit and tells the agent how to recover.

Target message shape:

`<path>: <violation>. <reason>. Use <approved primitive/path> instead.`

Avoid opaque policy IDs as the only explanation.

## Enforcement anti-patterns

Reject:

- slow global checks for a local invariant;
- regex checks that produce predictable false positives when AST/type information is available;
- custom frameworks when a build-system boundary is enough;
- lint rules with broad disable comments and no rationale;
- duplicate enforcement layers with inconsistent semantics;
- a rule that blocks the old path before callsites are migrated.
