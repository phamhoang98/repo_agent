#!/usr/bin/env python3
"""PreToolUse hook: block edits to secrets and signing files. Exit 2 = block."""
import json
import re
import sys

PROTECTED = [
    r"(^|/)\.env(\.[^/]*)?$",            # .env, .env.local, .env.production
    r"\.(pem|key|p8|p12|pfx|jks|keystore|mobileprovision)$",
    r"(^|/)id_(rsa|ed25519|ecdsa)$",
    r"(^|/)\.git/",
]
ALLOWED = [r"\.env\.(example|sample|template)$"]

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

path = (data.get("tool_input") or {}).get("file_path", "") or ""
if any(re.search(p, path) for p in ALLOWED):
    sys.exit(0)
for pattern in PROTECTED:
    if re.search(pattern, path):
        print(f"Blocked by multi-agent-kit: '{path}' looks like a secret or signing file. Ask the user to edit it manually.", file=sys.stderr)
        sys.exit(2)
sys.exit(0)
