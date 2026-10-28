# Minimal MCP Server Example

A tiny, educational Model Context Protocol (MCP) server written in Python. It exposes one read-only tool (`list_notes`) that lists markdown notes from a local folder you choose. Nothing leaves your machine.

**Remember:** Never put personal info, patient data, or secrets in notes an AI can read. See `docs/privacy.md`.

## What MCP is (in one sentence)

MCP lets an AI assistant connect to local tools and data through a standard, open protocol — like a USB port for AI.

## Requirements

Python 3. No external packages. This is a minimal example demonstrating the idea; real MCP clients use the official MCP SDK.

## Run it

```bash
python3 mcp_server.py --notes-folder ~/Documents/hobby-notes
```

It prints a JSON capability description to stdout. An MCP-compatible client can connect to it using stdio.

## Safety

- Read-only: it only lists files, never writes or deletes.
- Choose a folder that contains no personal or sensitive notes.
- Review code before running.

---

Credit: Asdale Dynamics, LLC (Indiana, formed October 2026). Beginner-friendly AI education, plain English, step by step.
