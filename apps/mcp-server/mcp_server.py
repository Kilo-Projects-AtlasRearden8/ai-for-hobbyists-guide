"""Minimal educational MCP server: lists markdown notes from a local folder.

This is a stdio-based example that demonstrates the MCP idea: an AI client can
ask the server to list notes in a chosen folder. It is read-only and runs
entirely on your machine. No external packages required.

Usage:
    python3 mcp_server.py --notes-folder /path/to/notes

Output is a JSON capability description on stdout.
"""
import argparse
import json
import os
import sys


def list_notes(folder):
    notes = []
    try:
        for name in sorted(os.listdir(folder)):
            path = os.path.join(folder, name)
            if os.path.isfile(path) and name.lower().endswith((".md", ".txt", ".markdown")):
                notes.append(name)
    except FileNotFoundError:
        return {"error": f"folder not found: {folder}"}
    except PermissionError:
        return {"error": f"permission denied: {folder}"}
    return {"notes": notes, "count": len(notes)}


def main():
    parser = argparse.ArgumentParser(description="Minimal MCP note-listing server")
    parser.add_argument("--notes-folder", required=True, help="Folder to list notes from")
    args = parser.parse_args()

    capability = {
        "name": "example-notes-server",
        "version": "0.1.0",
        "tools": [
            {
                "name": "list_notes",
                "description": "List markdown and text notes in the configured folder (read-only)",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False,
                },
            }
        ],
    }
    print(json.dumps(capability, indent=2))
    print("---")
    print(json.dumps(list_notes(args.notes_folder), indent=2))
    print("Remember: never put personal info in notes an AI can read.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
