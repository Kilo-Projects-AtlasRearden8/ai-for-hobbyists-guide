# Local LLM Helper

A tiny, dependency-free Python utility for local AI hobbyists. It lists models available through Ollama (if installed) and helps you draft safe, privacy-first prompts. Nothing is sent over the network except what you explicitly ask Ollama to do.

**Remember:** Never paste personal info, passwords, or API keys into AI tools. See `docs/privacy.md`.

## Files

- `list_models.py` — prints installed Ollama models
- `prompt_template.py` — prints a safe prompt template for hobby projects

## Requirements

Python 3 only. No external packages. Ollama is optional (for `list_models.py`).

## Run it

```bash
python3 list_models.py
python3 prompt_template.py
```

## What it does

`list_models.py` calls `ollama list` and prints available local models. If Ollama is not installed or not running, it prints a friendly message.

`prompt_template.py` prints a fill-in-the-blanks prompt you can copy into any AI chat. It reminds you not to paste personal info.

## Safety

This tool runs entirely on your computer. It does not collect or transmit data. Review any code before running it.

---

Credit: Asdale Dynamics, LLC (Indiana, formed October 2026). Beginner-friendly AI education, plain English, step by step.
