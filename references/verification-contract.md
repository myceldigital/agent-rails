# Verification Contract

A rail must prove both preservation and prohibition.

## 1. Characterization proof

Before migration, capture the behavior that must remain true using the cheapest reliable mechanism:

- existing tests;
- new characterization tests;
- stable fixture;
- CLI/smoke workflow.

Do not prohibit the old path before behavior is understood.

## 2. Positive proof

Show that the approved path:

- compiles/types;
- passes relevant static checks;
- passes relevant tests;
- completes the affected workflow when practical.

## 3. Adversarial proof

Construct an intentional violation representative of the old/bad path.

Require the intended enforcement layer to fail for the intended reason.

Examples:

- forbidden import fails dependency check;
- raw API call triggers lint rule;
- invalid state fails type checking;
- bypass fixture fails architecture test.

Do not count a failure caused by an unrelated syntax error or broken fixture.

## 4. Recovery proof

Confirm the error points to the approved path or is obvious enough that an agent can recover without repository archaeology.

## 5. Behavioral proof

When the change affects a runnable product surface, exercise it through that surface or its closest deterministic integration test.

Examples:

- API request succeeds end-to-end;
- UI flow completes in the test environment;
- background job consumes and emits expected state;
- CLI command creates the expected artifact.

## 6. Speed target

The architecture check used during editing should be fast enough to run repeatedly. Prefer seconds, not minutes, for local invariant checks.

Keep expensive end-to-end verification separate when necessary.

## Completion evidence

Record:

- positive command and exit result;
- adversarial command and expected non-zero result;
- behavioral command/result where relevant;
- files/rules responsible for enforcement.

`scripts/adversarial_verify.py` can validate an independent pass command and fail command.
