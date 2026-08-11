# Northstar architecture example — partially completed

Use this as a time-boxed reference, not as a finished answer. Copy the separate ADR template into `C926-labs/` and complete the scenario-specific decisions there.

## Outcome and exclusions

- Outcome example: return cited device-support guidance and prepare a synthetic escalation draft that a person can approve.
- Exclusions example: live identity changes, entitlement overrides, financial commitments and direct customer notification.

## Starter service map

| Need | Candidate | Decision still required |
|---|---|---|
| Grounded policy answer | Foundry model + Azure AI Search | Choose evidence freshness and permission-filter controls. |
| Synthetic request action | Agent Framework typed tool | Define approval, idempotency and invocation caps. |
| Invoice evidence | Content Understanding | Define source evidence and human-review thresholds. |
| Call evidence | Speech/Translator or supplied rejoin | Define language, timing and identifier-preservation checks. |

## Starter trust-boundary flow

`Learner user → local app → Foundry project → model / search / bounded tools → trace view`

Complete the acting identity, minimum role/scope, data crossing the boundary and observable evidence at each arrow.

## Starter risk rows

| Risk | Example preventive control | Evidence still required |
|---|---|---|
| Unsupported answer | Retrieved-source allowlist and strict output schema | Supported, unsupported and conflict traces |
| Unauthorized evidence | Caller-scope filter before retrieval | Same-category restricted-source test |
| Excessive agency | Approval-required write tool and invocation cap | Approved/rejected before-after store hashes |
| Prompt injection | Extracted text remains untrusted data; tools disabled | Deterministic injection result |

Complete unsafe-content and sensitive-trace rows, assign owners, add capacity/cost controls and choose the release evidence.
