"""List installed Ollama models on the local machine.

Runs `ollama list` and prints a friendly table. If Ollama is not available,
prints a helpful message instead. Nothing is sent over the network.
"""
import subprocess
import sys


def main():
    try:
        result = subprocess.run(
            ["ollama", "list"],
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError:
        print("Ollama is not installed or not on your PATH.")
        print("Install it from https://ollama.com to run models locally.")
        return 0
    except subprocess.CalledProcessError as exc:
        print("Could not talk to Ollama. Is it running?")
        print(exc.stderr.strip())
        return 1

    lines = result.stdout.strip().splitlines()
    if not lines:
        print("No Ollama output.")
        return 0

    print("Local Ollama models:")
    print("=" * 40)
    for line in lines:
        print(line)
    print("=" * 40)
    print("Tip: run `ollama run <model>` to start chatting with a model.")
    print("Remember: never paste personal info into an AI tool.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
