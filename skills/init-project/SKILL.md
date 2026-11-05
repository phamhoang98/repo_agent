---
name: init-project
description: "Detect a project's stack and generate a filled-in CLAUDE.md that the kit's agents rely on."
disable-model-invocation: true
---

Create or update `CLAUDE.md` at the project root so every agent in this kit knows the stack, commands and conventions.

1. Detect the stack from project files, for example:
   - Web: `package.json` (next, react, vue, svelte, vite), `tsconfig.json`
   - React Native / Expo: `app.json` / `app.config.*` with `expo`, `react-native` in `package.json`
   - Flutter: `pubspec.yaml`
   - iOS: `*.xcodeproj`, `Package.swift`, `Podfile`
   - Android: `build.gradle(.kts)`, `settings.gradle(.kts)`
   - Backend: `requirements.txt`, `pyproject.toml`, `go.mod`, `pom.xml`, server frameworks in `package.json`
2. Read the scripts/tasks to find the real install, dev, build, lint, type-check and test commands. Do not invent commands.
3. Look at the folder layout and a few files to infer conventions (component/screen locations, state management, test location, naming).
4. Fill in the template. Keep the "Agent routing" table, but delete rows for agents that do not apply (for example drop `mobile-dev` for a web-only project, `web-frontend` for mobile-only). Keep it under ~120 lines. Mark anything you could not determine as `TODO`.
5. If `CLAUDE.md` already exists, propose a diff and keep the user's existing content.

Template: `${CLAUDE_SKILL_DIR}/template.md` (if not readable, use these sections: Overview, Stack, Commands, Conventions, Rules for agents).

Finish by listing the TODOs the user should fill in.
