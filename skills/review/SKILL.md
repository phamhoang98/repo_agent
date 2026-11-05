---
name: review
description: "Review the current uncommitted or branch changes with reviewer, security-auditor and (for UI changes) accessibility-auditor in parallel. Use when asked to review changes before a commit or PR."
argument-hint: "[optional focus, e.g. a path or base branch]"
---

Review the current changes. Focus: $ARGUMENTS

Agent names are short names; as a plugin they are `multi-agent-kit:<name>`.

1. Determine the diff: uncommitted changes, or the branch against its base if the working tree is clean.
2. Run **reviewer** and **security-auditor** in parallel. Add **accessibility-auditor** if UI files changed, and **performance-optimizer** if the focus mentions performance.
3. Merge their results into one report ordered by severity, remove duplicates, and give a final verdict (APPROVE / REQUEST CHANGES).

Do not modify any files.
