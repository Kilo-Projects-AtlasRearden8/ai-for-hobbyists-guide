# STATUS

## What was built

`/workspace/kilo-lab/ai-for-hobbyists-guide` — a beginner manual and static HTML site on using free AI models for hobbies (crafting, collecting, gaming, DIY projects) plus related beginner topics, written in plain English, step by step, with printable project planners.

**Markdown manuals (`docs/`):**
- `index.md` — manual overview and how to use
- `privacy.md` — privacy and safety rule (never paste personal info)
- `getting-started.md` — picking and using free AI models, prompt writing
- `crafting.md` — knitting, sewing, scrapbooking, cards, Cricut
- `collecting.md` — tracking, researching, selling collections
- `gaming.md` — tabletop, video games, online games including FFXIV
- `diy.md` — home repair, woodworking, gardening, with safety rules
- `local-ai.md` — running free models on your own computer (most private)
- `agents-mcp.md` — AI agents and Model Context Protocol in plain English
- `free-ai-coding.md` — free AI coding for beginners
- `github.md` — using GitHub to save and share projects
- `automation.md` — small, safe AI automations
- `kdp-publishing.md` — KDP and book publishing for authors
- `book-marketing.md` — free book marketing ideas
- `reselling.md` — reselling on eBay/Amazon with AI
- `bookkeeping.md` — small-business and hobby bookkeeping basics
- `paperwork-organizer.md` — organizing household paperwork safely
- `budgeting.md` — building a simple monthly budget
- `adhd-productivity.md` — low-energy, ADHD-friendly productivity
- `healthcare-worker-ai.md` — AI for healthcare workers (education only, never medical advice)
- `chess-tools.md` — learning and enjoying chess with AI
- `project-planner.md` — printable one-page AI project planner

**Static HTML site (`site/`):**
- HTML mirror of every doc above (27 pages), plus `apps/prompt-builder/index.html` browser-based prompt builder
- `css/style.css`, `js/script.js` (mobile nav menu)
- No build step — open any `.html` file in a browser

**Open-source apps and templates (`apps/`):**
- `apps/prompt-builder/` — browser-based prompt builder (private, runs locally)
- `apps/local-llm-util/` — list local Ollama models and prompt templates (Python)
- `apps/mcp-server/` — minimal read-only Model Context Protocol server (Python)
- `apps/agent-skill/` — simple project-cost estimator agent skill (Python)

**Other:**
- `LICENSE` — MIT License, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project landing page with feature table and Asdale Dynamics, LLC credit
- `scripts/validate.py` — validation script (HTML structure, internal links, LICENSE line, README credit, secrets scan)
- `STATUS.md` — this file

## How to run

Open `site/index.html` in any web browser. All pages are static HTML; no installation, server, or API key needed.

Run validation: `python3 scripts/validate.py`

Run Python apps: `python3 apps/local-llm-util/prompt_template.py`, `python3 apps/local-llm-util/list_models.py`, `python3 apps/mcp-server/mcp_server.py --notes-folder <folder>`, `python3 apps/agent-skill/project_cost.py`

## Verification results

- `python3 scripts/validate.py` — VALIDATION PASSED (HTML structure, 0 broken internal links, LICENSE copyright line, README credit, secrets/personal-data scan clean)
- Served via `python3 -m http.server` on port 18081: all 25 HTML pages + CSS return HTTP 200
- Python apps run without errors (`prompt_template.py`, `list_models.py` graceful when Ollama absent, `mcp_server.py`, `project_cost.py`)
- No `.github/workflows` present; no remote repo created; nothing pushed
- No secrets, API keys, or real personal data in files (only required credits and a fictional example address used in privacy teaching)

## Known gaps

- No full-text search or dark mode on the static site
- Print planner is a static template; no form interactivity
- Free model links point to official sites; availability/pricing may change over time
- Ollama not installed in this environment, so `list_models.py` degrades gracefully
