#!/usr/bin/env python3
"""Merge the kit's hooks/hooks.json into a settings.json for manual installs.
Usage: merge_hooks.py <hooks.json> <settings.json> <installed-scripts-dir>"""
import json
import sys
from pathlib import Path

hooks_file, settings_file, scripts_dir = map(Path, sys.argv[1:4])
kit = json.loads(hooks_file.read_text())["hooks"]
settings = json.loads(settings_file.read_text()) if settings_file.exists() else {}
target = settings.setdefault("hooks", {})

added = 0
for event, groups in kit.items():
    existing = target.setdefault(event, [])
    existing_cmds = {h.get("command") for g in existing for h in g.get("hooks", [])}
    for group in groups:
        new_group = json.loads(json.dumps(group))
        for h in new_group["hooks"]:
            h["command"] = h["command"].replace("${CLAUDE_PLUGIN_ROOT}/hooks/scripts", str(scripts_dir))
        if all(h["command"] in existing_cmds for h in new_group["hooks"]):
            continue
        existing.append(new_group)
        added += 1

settings_file.parent.mkdir(parents=True, exist_ok=True)
settings_file.write_text(json.dumps(settings, indent=2) + "\n")
print(f"Hooks merged into {settings_file} ({added} new groups)")
