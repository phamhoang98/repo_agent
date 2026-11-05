# Changelog

## 0.2.0

- Repo flattened so `.claude-plugin/` and CI live at the root (required for marketplace install and GitHub Actions).
- Commands migrated to skills (`skills/<name>/SKILL.md`), as Claude Code now recommends.
- New agents: `backend-api`, `devops-release`, `performance-optimizer`, `accessibility-auditor`.
- New skill `/auto`: classifies a request and runs the matching workflow and agents.
- `/init-project` now writes an "Agent routing" table into `CLAUDE.md` so Claude delegates automatically.
- New skills: `/init-project`, `tdd`, `mobile-release`, `web-launch-check`.
- Safety hooks: destructive-command guard, secret/signing file protection, auto-format.
- Installer: profiles (`core`, `web`, `mobile`, `all`), `--with-hooks`, `--uninstall`, `--dry-run`.
- Agents: `color`, `effort`, and `disallowedTools` for read-only agents; frontmatter descriptions quoted (two agents previously failed YAML parsing).
- Validator checks skills, hooks and YAML quoting; hook unit tests; CI runs the official `claude plugin validate`.

## 0.1.0

- Initial 11 agents, 4 commands, installer, validator.
