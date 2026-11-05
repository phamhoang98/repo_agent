# Evals

Manual scenarios to re-run whenever an agent prompt changes. Run the agent on a small sample project and check the pass criteria.

| Agent / skill | Scenario | Pass criteria |
|---|---|---|
| planner | "Add dark mode toggle" on a sample web app | `docs/plan.md` has steps with "done when", lists files, no source edits |
| reviewer | Diff with an off-by-one and a missing null check | Both found with `file:line`; verdict REQUEST CHANGES |
| security-auditor | Hardcoded API key and SQL string concatenation | Both flagged Critical/High |
| debugger | Failing unit test caused by a wrong condition | Root cause named, minimal fix, test passes |
| web-frontend | "Add a signup form" | Labels, error states, keyboard accessible, type-check passes |
| mobile-dev | "Add a settings screen" on an Expo app | Uses existing navigation, handles safe area, runs type-check |
| backend-api | "Add GET /orders with pagination" | Validation, auth check, pagination, tests for 200/400/401 |
| devops-release | "Add CI for an Expo app" | lint -> test -> build steps, caching, no secrets in file |
| accessibility-auditor | Icon-only button without label | Flagged with fix |
| performance-optimizer | Long list rendered with `map` in React Native | Suggests/uses FlatList or FlashList with measurement or "unverified" label |
| `/feature` | Small full-stack feature | All stages run in order; stops on open questions |
| `/init-project` | Sample Next.js and Flutter repos | Correct stack and real commands; unknowns marked TODO |

Add a scenario every time an agent fails in a real project.
