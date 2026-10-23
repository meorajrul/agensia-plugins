# Capability verification and onboarding

Use at G0/G8 and when preparing a client handoff. Resolve inputs from the user's approved documents and authorised non-production environment. No private source library, previous investigation, particular folder structure or environment URL is required.

**Production is prohibited:** never create, push, publish, execute or otherwise mutate Agensia production, including through connected production resources. Verify non-production status before every platform write or run. If status is unknown, continue local drafting only. G0–G8 approvals cannot waive this boundary.

## Discover the deployment context

Derive known facts before asking questions. Record target classification, workspace, visible build/version or Not exposed, person type, workspace role, source versions, resource scope and authorised actions. Keep personal identifiers in the user's project records, not reusable examples.

Differentiate:

- **Specified:** a design or requirement says what should happen.
- **Reported:** a source describes behavior without independent verification.
- **Verified within scope:** actual evidence supports the precise assertion in the tested context.
- **Blocked / unknown:** a prerequisite or result is missing.
- **Contradicted:** an observed result differs from the requirement; retain both.

Use the user's existing evidence log. Record requirement ID, source, expected behavior, exact test steps, actual result, evidence, scope, confidence and next check. A test script is not a test result. An absent control in one state does not establish global absence; inspect relevant supported triggers within authorised scope.

## Actors and access

| Responsibility | Establish before dependent work |
|---|---|
| Process and Pod owner | Outcome, scope, authority, acceptance goal and decision responsibility |
| Platform administrator | Actual ability to configure identities, workspaces and available assets |
| Builder / application owner | Permission to create and revise the selected non-production assets |
| Workspace administrator | Membership, assignment, resource scope and permitted integrations |
| User / collaborator | Intended use, access level and restricted actions |
| Reviewer / approver | Exact assignment, evidence presented, allowed decisions and durable receipt |
| Acceptance / operations owner | Completion criteria, training, support and revalidation ownership |

Person type, company/workspace/group membership, asset access, connector authority and commercial entitlement are different dimensions. Do not infer one from another. Where groups exist, verify membership/migration and cross-group access. A personal availability toggle must not be assumed to change a subscription or company entitlement; inspect the relevant policy separately.

## Handoff checklist

| Item | Required evidence |
|---|---|
| Target | Verified non-production platform and downstream resources; no production mutation path |
| People | Named responsible/accountable roles, assignments and tested access boundaries |
| Knowledge | Approved current sources, conflict policy, exact content retrieval and citation checks |
| Integrations | Permitted instance/resources/actions, authenticated identity and reconciled reads |
| Configuration | Saved/reopened outcomes, sources, Talents, hierarchy and exact selected version |
| Availability | Distinct review, publication, assignment and invocation evidence where applicable |
| Outputs | Correct content, rendering, persistence, download/open and native handoff as required |
| Decisions | Actor/case/revision-bound approval and non-approval receipts; enforced continuation |
| Acceptance | Owner goal, baseline, expected/negative cases and actual results |
| Operations | Support owner, limitations, failure/recovery procedure and revalidation triggers |

Mark each row specified, verified, blocked or not applicable with reason. Document preparation does not execute deployment. Supported non-production publication, runs and schedules each require their own scoped authorisation.

## Verify independent stages

1. Configuration is present and scoped correctly.
2. Generation answers the intended request using approved inputs.
3. Rendering produces the required artifact.
4. Persistence retains that artifact after reopening.
5. Recall retrieves known content in fresh context; preview alone is insufficient.
6. Execution has an actual run, output and resulting-state evidence.
7. Authority gates dependent actions and handles rejection, expiry and missing decisions.

Test only the stages the outcome needs. Do not demand automation for a read-only advisory deliverable. A platform account label does not prove the named human made a business decision; preserve actual actor attribution and its limits.

## Decision and memory checks

For a calculated decision, specify options, constraints, approved criteria, missing information, approver and permissible result. Do not invent weights to force a winner. Check effective parameters and displayed wording, actual solving, any required simulation, explicit acceptance and originating Workflow return separately. A solver's feasible result is not proof of an authorised external action.

For user Collections and personal memory, test the actual scopes. Use harmless markers to distinguish preview, extraction and fresh-context recall. If a memory switch is supported, verify on/off/on behavior rather than assuming it erases history or backfills the disabled interval. Verify derived-memory deletion separately from the source item and check restricted-collaborator access.

## Revalidation

Recheck after changes to release, source/version, connector, permissions, assignments, authority or ownership. Preserve failed and assisted runs; do not claim a clean run when manual intervention was required. Resolve the affected control rather than strengthening prompt prose alone. Keep evidence and customer-specific details in the user's own records; public examples should be fictional and self-contained.
