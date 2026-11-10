def status_of(percent):
    """Return status classification based on percentage threshold."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check_record(value, limit):
    """Return calculated difference, percent, and status for a record."""
    difference = limit - value
    percent = (value / limit) * 100
    status = status_of(percent)
    return difference, percent, status


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


def load_records(path):
    """Read record lines from a file and return a list of dictionaries."""
    records_list = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                records_list.append({
                    "label": parts[0].strip(),
                    "value": float(parts[1].strip()),
                    "limit": float(parts[2].strip())
                })
    return records_list


def save_results(path, output_lines):
    """Write processed record labels and their statuses to an output file."""
    with open(path, "w") as f:
        for line in output_lines:
            f.write(f"{line}\n")


with open("records.txt", "w") as f:
    f.write("srv-01, 87, 120\n")
    f.write("srv-02, 125, 120\n")
    f.write("srv-03, 110, 120\n")

records = load_records("records.txt")

over_limit_count = 0
results_to_save = []

for record in records:
    label = record["label"]
    value = record["value"]
    limit = record["limit"]

    difference, percent, status = check_record(value, limit)
    print_report(label, value, limit, difference, percent, status)

    results_to_save.append(f"{label}, {status}")

    if status == "OVER LIMIT":
        over_limit_count += 1

save_results("results.txt", results_to_save)

print(f"Total OVER LIMIT records: {over_limit_count}")