#!/usr/bin/env python3
"""PreToolUse hook: block clearly destructive shell commands. Exit 2 = block."""
import json
import re
import sys

BLOCKED = [
    (r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*f?[a-zA-Z]*\s+(/|~|\$HOME)(\s|/?$)", "recursive delete of / or home"),
    (r"\bgit\s+push\b.*(--force\b|-f\b)(?!-with-lease)", "force push (use --force-with-lease if really needed)"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard discards work"),
    (r"\bgit\s+clean\s+-[a-zA-Z]*f", "git clean -f deletes untracked files"),
    (r"\b(mkfs|dd\s+if=)", "disk-level write"),
    (r":\(\)\s*\{\s*:\|:&\s*\};:", "fork bomb"),
    (r"\bchmod\s+-R\s+777\b", "chmod -R 777"),
    (r"(curl|wget)[^|]*\|\s*(sudo\s+)?(ba|z)?sh\b", "piping a download into a shell"),
]

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

cmd = (data.get("tool_input") or {}).get("command", "")
for pattern, reason in BLOCKED:
    if re.search(pattern, cmd):
        print(f"Blocked by multi-agent-kit guard: {reason}. Ask the user to run it manually if intended.", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
