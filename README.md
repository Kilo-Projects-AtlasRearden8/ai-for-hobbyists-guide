# AI for Hobbyists

A beginner-friendly manual and static HTML site on using **free AI models** for hobbies &mdash; crafting, collecting, gaming, DIY projects, and more &mdash; written in plain English, step by step, with printable project planners.

## Who this is for

You do not need to be technical. You do not need to pay for AI. This guide is for anyone who wants to use free AI for fun projects at home, whether you knit, collect trading cards, play games, or tinker around the house.

## Privacy rule (read first)

**Never paste personal info into an AI tool.** No names, addresses, phone numbers, emails, passwords, bank details, health information, or anything that identifies you or someone else. Treat every AI conversation as public. See `docs/privacy.md`.

## What's inside

### Beginner manuals (`docs/`)

| Guide | What's inside |
|---|---|
| `getting-started.md` | Picking and using free AI models, writing prompts |
| `privacy.md` | Privacy and safety rules |
| `crafting.md` | Knitting, sewing, scrapbooking, cards, Cricut |
| `collecting.md` | Tracking, researching, selling collections |
| `gaming.md` | Tabletop, video games, online games including FFXIV |
| `diy.md` | Home repair, woodworking, gardening, with safety rules |
| `project-planner.md` | Printable AI project planner |
| `local-ai.md` | Running free models on your own computer |
| `agents-mcp.md` | AI agents and Model Context Protocol in plain English |
| `free-ai-coding.md` | Free AI coding for beginners |
| `github.md` | Using GitHub to save and share projects |
| `automation.md` | Small, safe AI automations |
| `kdp-publishing.md` | KDP and book publishing for authors |
| `book-marketing.md` | Free book marketing ideas |
| `reselling.md` | Reselling on eBay/Amazon with AI |
| `bookkeeping.md` | Small-business and hobby bookkeeping basics |
| `paperwork-organizer.md` | Organizing household paperwork safely |
| `budgeting.md` | Building a simple monthly budget |
| `adhd-productivity.md` | Low-energy, ADHD-friendly productivity |
| `healthcare-worker-ai.md` | AI for healthcare workers (education only, never medical advice) |
| `chess-tools.md` | Learning and enjoying chess with AI |

### Static HTML site (`site/`)

The same manuals as HTML pages. Open `site/index.html` in any web browser &mdash; nothing to install, build, or host.

### Open-source apps and templates (`apps/`)

- `apps/prompt-builder/` &mdash; browser-based prompt builder (private, runs locally)
- `apps/local-llm-util/` &mdash; list local Ollama models and prompt templates (Python)
- `apps/mcp-server/` &mdash; minimal read-only Model Context Protocol server (Python)
- `apps/agent-skill/` &mdash; simple project-cost estimator agent skill (Python)

## How to use

1. Read `docs/privacy.md` first.
2. Read `docs/getting-started.md` to pick a free AI tool and write your first prompts.
3. Pick a hobby guide and start with one small project.
4. Print `docs/project-planner.md` (or `site/project-planner.html`) and use it for each project.

## About

Created by **Asdale Dynamics, LLC** (Indiana, formed October 2026), publisher of beginner-friendly AI education &mdash; including Dylan Asdale's *The Massive AI Manual* and dylanasdale.github.io &mdash; which explains AI "like a friend would": plain English, step by step, never condescending.

Asdale Dynamics, LLC focuses on approachable AI guides, open-source templates, small-business and author tools, accessible life-admin helpers, healthcare-worker AI aids (education only, never medical advice), and fun extras like gaming and chess tools.

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See `LICENSE`.

## Verification

Run `python3 scripts/validate.py` to check HTML structure, internal links, the LICENSE copyright line, README credit, and scan for secrets or personal data.
