---
name: research
description: "Research a technical question by running several researcher subagents in parallel and synthesizing a sourced answer. Use for library comparisons and \"how does X work\" questions that need several sources."
argument-hint: "<question>"
---

Research: $ARGUMENTS

Split the question into 2-4 independent sub-questions. Launch one **researcher** subagent (`multi-agent-kit:researcher` as a plugin) per sub-question in parallel. Combine their findings into one answer with evidence, trade-offs and a recommendation. Flag any disagreement between sources. Do not modify files.
