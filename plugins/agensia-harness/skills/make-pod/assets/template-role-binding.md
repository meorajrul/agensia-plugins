---
artifact: ontology-source
framework: p2a
version: "0.1"
status: draft
owner: <accountable process owner role>
updated: <YYYY-MM-DD>
authority_rank: <n>
effective_from: <YYYY-MM-DD>
effective_to: open
review_due: <YYYY-MM-DD>
---

# <Pod name> role binding

Use this file to resolve every role named in this Pod's sources, Talents and Workflow tasks.
Sources name roles, not people. A person changes; a role stays.

| Role name in sources | Lane | Accountable for | Cover role when absent | Current holder (role title) | Confirmed (tag, date) |
| --- | --- | --- | --- | --- | --- |
| <Role> | <lane> | <decisions / approvals> | <role> | <title> | <OWN YYYY-MM-DD> |

## Rules

1. Send each escalation to the named role. When it is absent, send it to the cover role.
2. Do not name a person as approver unless the case record names that person.
3. When this file and a case record disagree, report the conflict. Use the case record.
4. When older records name a person instead of a role, map the name to the role listed here. If no mapping exists, stop and ask.
5. When a holder changes, update this file, re-run the playback for affected rows, and re-upload it. Do not edit other sources for a holder change.
