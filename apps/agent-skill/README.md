# Simple Agent Skill Template

A minimal template for an AI "agent skill" — a small, single-purpose function an AI assistant can call with your permission. This example calculates the estimated cost of a hobby project from a materials list.

**Remember:** Never paste personal info, prices tied to your real accounts, or payment details into an agent. See `docs/privacy.md`.

## What an agent skill is

A skill is a small, well-defined task an AI can perform for you — for example, adding up a shopping list, converting units, or formatting a checklist. You control when it runs and what data it sees.

## Files

- `project_cost.py` — calculates total cost from a simple materials list
- `SKILL.md` — plain-English description of what the skill does and how to use it safely

## Use it

```bash
python3 project_cost.py
```

Enter material names and prices one per line, or use the built-in example. The script prints a total. Nothing is sent over a network.

## Safety

- Run skills locally. Do not give an agent access to your bank or payment accounts.
- AI-suggested prices are estimates. Verify real costs before buying.
- Review any agent skill code before letting an AI call it.

---

Credit: Asdale Dynamics, LLC (Indiana, formed October 2026). Beginner-friendly AI education, plain English, step by step.
