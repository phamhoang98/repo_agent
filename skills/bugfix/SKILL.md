---
name: bugfix
description: "Diagnose and fix a bug with debugger, tester and reviewer subagents."
argument-hint: "<bug description, error message or failing test>"
disable-model-invocation: true
---

Fix this bug: $ARGUMENTS

Agent names are short names; as a plugin they are `multi-agent-kit:<name>`.

1. **debugger**: reproduce, find the root cause, apply the minimal fix.
2. **tester**: confirm a regression test exists and the related suite passes.
3. **reviewer**: review the diff. If there are Blockers, return to step 1 (max 2 rounds).

Summarize: root cause, fix, verification. Do not commit unless I ask.
