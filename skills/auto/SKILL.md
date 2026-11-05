---
name: auto
description: "Analyze a request and automatically run the right workflow and subagents (feature, bugfix, review, research, release check). Use when the user gives a task without naming a workflow, or types /auto."
argument-hint: "<what you want done>"
---

Task: $ARGUMENTS

Agent names are short names; as a plugin they are `multi-agent-kit:<name>`.

## Step 1: Classify

Read the request, `CLAUDE.md`, and (if needed) a quick look at the repo. Choose exactly one:

| If the request is about... | Workflow |
|---|---|
| Building or changing behavior across several files | **feature**: follow the `feature` skill |
| An error, crash, regression, or failing test | **bugfix**: follow the `bugfix` skill |
| Checking existing changes or a PR | **review**: follow the `review` skill |
| Understanding code or comparing options | **research**: follow the `research` skill |
| Shipping a build or deploying | **release**: run `mobile-release` and/or `web-launch-check`, plus `devops-release` for pipeline work |
| Slowness | `performance-optimizer`, then `reviewer` |
| A tiny change (one file, one obvious edit) | Do it directly, then `reviewer` if code changed |

## Step 2: Announce

Before running, state in 2-3 lines: the workflow chosen, the agents that will run, and any assumption. If the request is ambiguous or risky (data deletion, auth, payments, production), ask one clarifying question first and wait.

## Step 3: Run

Execute the chosen workflow exactly as its skill describes. Pick implementers by platform: `web-frontend` for web UI, `mobile-dev` for mobile, `backend-api` for server code, `coder` otherwise. Run independent agents in parallel.

## Rules

- Do not commit, push, deploy, or submit to stores unless the user asked.
- If no `CLAUDE.md` exists, suggest running `/init-project` once, then continue.
- End with a short summary: workflow used, agents run, result, what remains.
