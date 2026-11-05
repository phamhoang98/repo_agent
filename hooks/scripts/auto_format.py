#!/usr/bin/env python3
"""PostToolUse hook: format the edited file with the project's own formatter, if one is available.
Never fails the tool call: always exits 0."""
import json
import os
import shutil
import subprocess
import sys


def run(cmd, cwd):
    try:
        subprocess.run(cmd, cwd=cwd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=25)
    except Exception:
        pass


try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

path = (data.get("tool_input") or {}).get("file_path", "")
if not path or not os.path.isfile(path):
    sys.exit(0)

project = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
ext = os.path.splitext(path)[1].lower()

prettier = os.path.join(project, "node_modules", ".bin", "prettier")
if ext in {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".css", ".scss", ".json", ".md", ".html", ".vue", ".svelte", ".yml", ".yaml"}:
    if os.path.exists(prettier):
        run([prettier, "--write", "--ignore-unknown", path], project)
elif ext == ".dart" and shutil.which("dart"):
    run(["dart", "format", path], project)
elif ext == ".go" and shutil.which("gofmt"):
    run(["gofmt", "-w", path], project)
elif ext == ".py":
    if shutil.which("ruff"):
        run(["ruff", "format", path], project)
    elif shutil.which("black"):
        run(["black", "-q", path], project)
elif ext == ".swift" and shutil.which("swiftformat"):
    run(["swiftformat", path], project)
elif ext in {".kt", ".kts"} and shutil.which("ktlint"):
    run(["ktlint", "-F", path], project)

sys.exit(0)
