#!/usr/bin/env python3
"""Validate agents, skills, hooks and plugin manifests. Exit 1 on any problem."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODELS = {"opus", "sonnet", "haiku", "fable", "inherit"}
COLORS = {"red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"}
WRITE_TOOLS = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
errors = []


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
        return {}, ""
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            v = v.strip()
            if v.startswith('"') and v.endswith('"') and len(v) >= 2:
                v = v[1:-1].replace('\\"', '"').replace("\\\\", "\\")
            elif ": " in v or v.startswith(("[", "{", "<", "*", "&", "!", "|", ">", "%", "@", "`")) and k.strip() in ("description", "argument-hint"):
                errors.append(f"{path.relative_to(ROOT)}: '{k.strip()}' must be double-quoted (YAML would fail to parse)")
            data[k.strip()] = v
    return data, m.group(2)


def tool_set(value):
    return {t.strip() for t in value.split(",") if t.strip()} if value else set()


# Agents
names = set()
for f in sorted((ROOT / "agents").glob("*.md")):
    fm, body = frontmatter(f)
    rel = f"agents/{f.name}"
    for key in ("name", "description", "tools", "model"):
        if not fm.get(key):
            errors.append(f"{rel}: missing '{key}'")
    name = fm.get("name", "")
    if name != f.stem:
        errors.append(f"{rel}: name '{name}' must match filename")
    if ":" in name:
        errors.append(f"{rel}: name must not contain ':'")
    if name in names:
        errors.append(f"{rel}: duplicate name")
    names.add(name)
    if len(fm.get("description", "")) < 40:
        errors.append(f"{rel}: description too short to route reliably")
    if fm.get("model") and fm["model"] not in MODELS:
        errors.append(f"{rel}: unknown model '{fm['model']}'")
    if fm.get("color") and fm["color"] not in COLORS:
        errors.append(f"{rel}: unknown color '{fm['color']}'")
    if "read-only" in fm.get("description", "").lower() and tool_set(fm.get("tools")) & WRITE_TOOLS:
        errors.append(f"{rel}: described as read-only but has write tools")
    if len(body.strip()) < 200:
        errors.append(f"{rel}: system prompt body looks empty")

# Skills
skill_names = set()
for d in sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir()):
    skill = d / "SKILL.md"
    if not skill.exists():
        errors.append(f"skills/{d.name}: missing SKILL.md")
        continue
    fm, _ = frontmatter(skill)
    if not fm.get("description"):
        errors.append(f"skills/{d.name}/SKILL.md: missing 'description'")
    if fm.get("name") and fm["name"] != d.name:
        errors.append(f"skills/{d.name}/SKILL.md: name must match folder")
    skill_names.add(d.name)
clash = names & skill_names
if clash:
    errors.append(f"agent and skill share a name: {sorted(clash)}")

# Manifests
for j in (".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"):
    try:
        json.loads((ROOT / j).read_text(encoding="utf-8"))
    except Exception as e:
        errors.append(f"{j}: {e}")

# Hooks
hooks_path = ROOT / "hooks" / "hooks.json"
if hooks_path.exists():
    try:
        hooks = json.loads(hooks_path.read_text(encoding="utf-8"))["hooks"]
        for event, groups in hooks.items():
            for g in groups:
                for h in g.get("hooks", []):
                    for script in re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([^\"\s]+)", h.get("command", "")):
                        if not (ROOT / script).exists():
                            errors.append(f"hooks/hooks.json: {event} references missing {script}")
    except Exception as e:
        errors.append(f"hooks/hooks.json: {e}")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"OK: {len(names)} agents, {len(skill_names)} skills validated")
