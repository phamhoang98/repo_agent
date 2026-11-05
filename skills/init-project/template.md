# Project guide for Claude

## Overview
<One or two sentences: what this project is.>

## Stack
- Platform: <web | mobile | both>
- Language/framework: <e.g. Next.js + TypeScript, Expo, Flutter>
- Package manager: <npm | pnpm | yarn | pub>

## Commands
- Install: `<command>`
- Dev: `<command>`
- Build: `<command>`
- Lint: `<command>`
- Type-check: `<command>`
- Test: `<command>`

## Conventions
- Folder structure: <where components, screens, services, tests live>
- Naming and style: <rules>
- Architecture: <e.g. MVVM, feature folders>

## Agent routing (multi-agent-kit)
Delegate to the matching subagent instead of doing the work inline. Names are `multi-agent-kit:<name>` when installed as a plugin.

| Situation | Agent |
|---|---|
| Task touches more than ~2 files or is ambiguous | `planner` first |
| New module, schema, or API contract | `architect` |
| Web UI (components, pages, styling) | `web-frontend` |
| Mobile screens, navigation, native modules | `mobile-dev` |
| API, database, auth, migrations | `backend-api` |
| CI/CD, Docker, build or release pipeline | `devops-release` |
| Other code changes | `coder` |
| Error, crash, or failing test | `debugger` |
| After any code change | `tester`, then `reviewer` |
| Auth, payments, user data, network, secrets | `security-auditor` |
| UI changed | `accessibility-auditor` |
| Something is slow | `performance-optimizer` |
| Public behavior or setup changed | `doc-writer` |
| "How does X work" / library comparison | `researcher` |

Run independent agents in parallel. Small one-line fixes need no agent.

## Rules for agents
- NEVER commit, push, merge, rebase, tag or open a PR on your own. Leave changes uncommitted and let the user do it, unless they explicitly ask in the current message. This applies to all subagents.
- Ask before adding dependencies.
- Never touch: <paths, e.g. generated code, signing config>
