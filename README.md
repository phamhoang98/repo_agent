# multi-agent-kit

Reusable multi-agent toolkit for [Claude Code](https://claude.com/claude-code), built for **web and mobile** projects. Install once, use in every project.

[Tiếng Việt](README.vi.md)

## What's inside

**15 subagents**, each with one job, least-privilege tools, and a model matched to the task:

| Group | Agents |
|---|---|
| Plan | `planner` (opus), `architect` (opus) |
| Build | `coder`, `web-frontend`, `mobile-dev`, `backend-api`, `devops-release` |
| Verify | `tester`, `debugger`, `reviewer`, `security-auditor`, `accessibility-auditor`, `performance-optimizer` |
| Support | `doc-writer` (haiku), `researcher` |

Read-only agents (`reviewer`, `security-auditor`, `accessibility-auditor`, `researcher`) cannot edit files.

**9 skills** (invoke with `/name`, or Claude loads them when relevant):

| Skill | What it does |
|---|---|
| `/auto <task>` | Analyzes the request, picks the right workflow and agents, runs it. The only command you need to remember |
| `/feature <desc>` | planner -> architect -> implementer(s) -> tester -> reviewer + security in parallel -> fix loop -> docs |
| `/bugfix <desc>` | debugger -> tester -> reviewer |
| `/review` | reviewer + security-auditor (+ accessibility) in parallel, one merged report |
| `/research <q>` | parallel researchers, one sourced answer |
| `/init-project` | detects your stack and writes `CLAUDE.md` |
| `tdd` | red-green-refactor loop |
| `mobile-release` | App Store / Google Play pre-release checklist |
| `web-launch-check` | build, Core Web Vitals, SEO, a11y, security headers checklist |

**Safety hooks** (plugin install, or `--with-hooks` for manual install):
- Block destructive shell commands: `rm -rf /`, force push, `git reset --hard`, `curl | sh`.
- Block edits to secrets and signing files: `.env*`, `*.keystore`, `*.jks`, `*.p8`, `*.p12`, `*.pem`.
- Auto-format edited files with the project's own formatter (Prettier, dart format, gofmt, ruff/black, swiftformat, ktlint) when installed.

## Install

### Option 1: plugin (recommended)

```
/plugin marketplace add YOUR_GITHUB_USER/multi-agent-kit
/plugin install multi-agent-kit@multi-agent-kit
```

Update later with `/plugin marketplace update multi-agent-kit`. As a plugin, names are namespaced: `multi-agent-kit:reviewer`, `/multi-agent-kit:feature`.

### Option 2: install script

```bash
git clone https://github.com/YOUR_GITHUB_USER/multi-agent-kit.git
./multi-agent-kit/scripts/install.sh --profile web --with-hooks /path/to/project
```

| Flag | Meaning |
|---|---|
| `--profile core\|web\|mobile\|all` | Which agents (default `all`). `web` / `mobile` add the platform specialist plus backend, devops, a11y, performance |
| `--user` | Install into `~/.claude` for all projects |
| `--with-hooks` | Copy hook scripts and merge them into `settings.json` |
| `--uninstall` | Remove what the script installed |
| `--dry-run` | Show actions without changing anything |

Requires `python3` for hooks.

## Quick start

1. In your project, run `/init-project` and fill in the TODOs in the generated `CLAUDE.md`. Agents read it for stack, commands and conventions.
2. Just describe the work in plain language. Two things make agents run without you naming them:
   - The **Agent routing** table that `/init-project` writes into `CLAUDE.md` (loaded every session) tells Claude which agent handles which situation.
   - Each agent's `description` lets Claude pick it on its own.
3. Or be explicit. `/auto <task>` classifies the task and runs the right workflow; the others force a specific one:

```
/auto fix the crash when opening settings offline
/feature add a login screen with email and password, web and mobile
/bugfix app crashes when opening settings offline
/review
/research Zustand vs Redux Toolkit for a React Native app
/mobile-release
```

## How it works

```
/feature
  └─ planner ──> docs/plan.md
       └─ architect ──> docs/design.md        (only for new modules / APIs)
            ├─ web-frontend ─┐
            ├─ mobile-dev ───┼─ in parallel once the API contract is fixed
            └─ backend-api ──┘
                 └─ tester
                      └─ reviewer ‖ security-auditor ‖ accessibility-auditor
                           └─ blockers? back to implementer (max 2 rounds)
                                └─ doc-writer
```

- The main session orchestrates through skills. Agents hand over work through files (`docs/plan.md`, `docs/design.md`), which keeps context small and lets you review each step.
- Project-specific knowledge lives in your project's `CLAUDE.md`, not in the agents, so the same kit fits every project.

## Customize

- Edit any agent in `agents/`. Keep `name` equal to the filename and write a precise `description`: that is how Claude decides when to delegate.
- Quote frontmatter values that contain `: ` (the validator enforces this).
- Project-level agents with the same name override the kit's, so you can fork one agent per project.

## Development

```bash
python3 scripts/validate.py      # agents, skills, hooks, manifests
python3 scripts/test_hooks.py    # hook unit tests
claude plugin validate .         # official marketplace check
claude plugin validate .claude-plugin/plugin.json
```

CI runs all of these plus installer tests. See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/evals.md](docs/evals.md).

## License

MIT
