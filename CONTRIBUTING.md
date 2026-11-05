# Contributing

## Adding or changing an agent

1. One file per agent in `agents/`, `name` equal to the filename, no `:` in the name.
2. `description` says **when to use** the agent (and when not). Quote it if it contains `: `.
3. Grant the fewest tools needed. Review/audit agents are read-only (`disallowedTools: Edit, Write`).
4. Pick a model: `opus` for planning/architecture, `sonnet` for coding and review, `haiku` for simple, high-volume work.
5. Body: role, process, quality bar, rules, and a fixed output format.
6. Add or update a scenario in [docs/evals.md](docs/evals.md).

## Adding a skill

Create `skills/<name>/SKILL.md` with a `description`. Use `disable-model-invocation: true` for workflows that should only run when the user types them.

## Before opening a PR

```bash
python3 scripts/validate.py
python3 scripts/test_hooks.py
claude plugin validate .
claude plugin validate .claude-plugin/plugin.json
```

Bump `version` in `.claude-plugin/plugin.json` and add a `CHANGELOG.md` entry: plugin users only receive updates when the version changes.
