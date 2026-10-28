"""Simple agent skill: estimate hobby project cost from a materials list.

Run:
    python3 project_cost.py

Enter one material per line as: name, price
Example: yarn, 12.50
Blank line to finish. Nothing is sent over a network.
"""


def parse_line(line):
    """Return (name, price) or None if the line is invalid."""
    parts = [p.strip() for p in line.split(",")]
    if len(parts) != 2:
        return None
    name, price_str = parts
    if not name:
        return None
    try:
        price = float(price_str)
    except ValueError:
        return None
    if price < 0:
        return None
    return name, price


def main():
    print("Hobby Project Cost Estimator")
    print("Enter materials as: name, price")
    print("Blank line to finish.")
    print()

    total = 0.0
    count = 0
    while True:
        line = input("Material: ").strip()
        if line == "":
            break
        parsed = parse_line(line)
        if parsed is None:
            print("  (skip) Use format: name, price")
            continue
        name, price = parsed
        total += price
        count += 1
        print(f"  added {name}: ${price:.2f}")

    print()
    print(f"Items: {count}")
    print(f"Estimated total: ${total:.2f}")
    print("Tip: AI price suggestions are estimates — check real store prices.")


if __name__ == "__main__":
    main()
