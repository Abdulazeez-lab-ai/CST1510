def status_of(percent):
    """Return status classification based on percentage threshold."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Calculate and return difference and percentage as a tuple."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print formatted record check report."""
    print()
    print("-" * 34)
    print(f"RECORD CHECK  - {label}")
    print("-" * 34)
    print(f"Value:       {value:>10.2f}")
    print(f"Limit:       {limit:>10.2f}")
    print(f"Difference:  {difference:>+10.2f}")
    print(f"Percent:     {percent:>10.2f}%")
    print(f"Status:      {status:>10}")
    print("-" * 34)
    print()


over_limit_count = 0

while True:
    label = input("Enter label (or type 'quit' to stop): ").strip()
    if label.lower() == "quit":
        break

    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(label, value, limit, difference, percent, status)

print(f"Total OVER LIMIT records: {over_limit_count}")