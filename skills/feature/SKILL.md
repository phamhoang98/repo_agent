---
name: feature
description: "Build a feature end to end with planner, architect, implementer, tester, reviewer and security-auditor subagents."
argument-hint: "<feature description>"
disable-model-invocation: true
---

Implement this feature: $ARGUMENTS

Agent names below are short names. When this kit is installed as a plugin they are namespaced, e.g. `multi-agent-kit:planner`.

Run these stages in order. Pass results between stages through files, not by pasting long text.

1. **planner**: write `docs/plan.md`. If it lists open questions, stop and ask me before continuing.
2. **architect**: only if the plan adds new modules, schemas or APIs. Write `docs/design.md`.
3. **Implementation**: pick by work type, following `docs/plan.md`:
   - web UI -> `web-frontend`
   - mobile screens / native code -> `mobile-dev`
   - API, database, server logic -> `backend-api`
   - anything else -> `coder`
   Independent parts (for example web and mobile clients of the same API) may run in parallel once the API contract in `docs/design.md` is fixed.
4. **tester**: add and run tests for the changes.
5. **reviewer** and **security-auditor** in parallel on the final diff. Add **accessibility-auditor** if UI changed.
6. If any returns Blockers / Critical / High, send them back to the implementer and repeat steps 4-5 (max 2 rounds).
7. **doc-writer** if public behavior or setup changed.

Finish with a short summary: what changed, test results, remaining issues. Do not commit unless I ask.
