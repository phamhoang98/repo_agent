#!/usr/bin/env bash
# Manual installer for multi-agent-kit (use the plugin marketplace if you can).
#
# Usage:
#   ./scripts/install.sh [options] [target-project-dir]
#
# Options:
#   --profile core|web|mobile|all   Which agents to install (default: all)
#   --user                          Install into ~/.claude for every project
#   --with-hooks                    Also install safety/format hooks into settings.json
#   --uninstall                     Remove files previously installed by this script
#   --dry-run                       Print what would happen, change nothing
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROFILE="all"; USER_SCOPE=0; WITH_HOOKS=0; UNINSTALL=0; DRY=0; TARGET="."

while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile) PROFILE="${2:?missing profile}"; shift 2 ;;
    --user) USER_SCOPE=1; shift ;;
    --with-hooks) WITH_HOOKS=1; shift ;;
    --uninstall) UNINSTALL=1; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    *) TARGET="$1"; shift ;;
  esac
done

CORE="planner architect coder reviewer tester debugger security-auditor doc-writer researcher"
SHARED="backend-api accessibility-auditor performance-optimizer devops-release"
case "$PROFILE" in
  core)   AGENTS="$CORE" ;;
  web)    AGENTS="$CORE web-frontend $SHARED" ;;
  mobile) AGENTS="$CORE mobile-dev $SHARED" ;;
  all)    AGENTS="$CORE web-frontend mobile-dev $SHARED" ;;
  *) echo "Unknown profile: $PROFILE" >&2; exit 1 ;;
esac

if [[ $USER_SCOPE -eq 1 ]]; then
  DEST="$HOME/.claude"; PROJECT=""
else
  PROJECT="$(cd "$TARGET" && pwd)"; DEST="$PROJECT/.claude"
fi
MANIFEST="$DEST/.multi-agent-kit-manifest"

do_cmd() { if [[ $DRY -eq 1 ]]; then echo "[dry-run] $*"; else "$@"; fi; }

if [[ $UNINSTALL -eq 1 ]]; then
  [[ -f "$MANIFEST" ]] || { echo "Nothing installed by multi-agent-kit in $DEST"; exit 0; }
  while IFS= read -r f; do [[ -n "$f" ]] && do_cmd rm -rf "$DEST/$f"; done < "$MANIFEST"
  do_cmd rm -f "$MANIFEST"
  echo "Uninstalled from $DEST (hooks in settings.json, if any, must be removed by hand)."
  exit 0
fi

do_cmd mkdir -p "$DEST/agents" "$DEST/skills"
INSTALLED=()
for a in $AGENTS; do
  do_cmd cp "$SRC/agents/$a.md" "$DEST/agents/"; INSTALLED+=("agents/$a.md")
done
for s in "$SRC"/skills/*/; do
  name="$(basename "$s")"
  do_cmd rm -rf "$DEST/skills/$name"
  do_cmd cp -R "$s" "$DEST/skills/$name"; INSTALLED+=("skills/$name")
done

if [[ $WITH_HOOKS -eq 1 ]]; then
  do_cmd mkdir -p "$DEST/hooks"
  do_cmd rm -rf "$DEST/hooks/multi-agent-kit"
  do_cmd cp -R "$SRC/hooks/scripts" "$DEST/hooks/multi-agent-kit"; INSTALLED+=("hooks/multi-agent-kit")
  if [[ $DRY -eq 0 ]]; then
    python3 -I "$SRC/scripts/merge_hooks.py" "$SRC/hooks/hooks.json" "$DEST/settings.json" "$DEST/hooks/multi-agent-kit"
  else
    echo "[dry-run] merge hooks into $DEST/settings.json"
  fi
fi

if [[ $DRY -eq 0 ]]; then printf '%s\n' "${INSTALLED[@]}" > "$MANIFEST"; fi

if [[ -n "$PROJECT" && ! -f "$PROJECT/CLAUDE.md" ]]; then
  echo "Tip: open Claude Code in $PROJECT and run /init-project to generate CLAUDE.md."
fi
echo "Installed profile '$PROFILE' (${#INSTALLED[@]} items) to $DEST"
