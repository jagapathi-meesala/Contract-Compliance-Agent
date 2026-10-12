from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    "agent.yaml", "SOUL.md", "README.md", "RULES.md", "DUTIES.md",
    "AGENTS.md", "EXPLAINABILITY.md", "requirements.txt", "pytest.ini",
    "tools/review-contract-obligations.yaml", "tools/map-compliance-evidence.yaml",
    "tools/prepare-compliance-action-plan.yaml",
    "skills/clause-review/SKILL.md", "skills/obligation-tracking/SKILL.md",
    "skills/compliance-gap-analysis/SKILL.md",
]
missing = [name for name in required if not (ROOT / name).is_file()]
if missing:
    print("READINESS AUDIT: FAIL")
    for name in missing:
        print("MISSING:", name)
    raise SystemExit(1)
for path in (ROOT / "skills").rglob("SKILL.md"):
    if not path.read_text(encoding="utf-8").startswith("---\n"):
        print("READINESS AUDIT: FAIL")
        print("Missing YAML frontmatter:", path)
        raise SystemExit(1)
print("READINESS AUDIT: PASS")
print(f"Checked {len(required)} required files.")
