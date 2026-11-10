class Record:
    """Represent a system record with usage values and limits."""

    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initialize a Record instance with label, value, and limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Return the status of the record based on percentage used."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"


def load_records(path):
    """Read lines from a data file and return a list of Record objects."""
    records_list = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(",")
                records_list.append(
                    Record(parts[0].strip(), parts[1].strip(), parts[2].strip())
                )
    return records_list


with open("records.txt", "w") as f:
    f.write("srv-01, 87, 120\n")
    f.write("srv-02, 125, 120\n")
    f.write("srv-03, 110, 120\n")

records = load_records("records.txt")

over_limit_count = 0

for record in records:
    difference = record.limit - record.value
    percent = (record.value / record.limit) * 100
    rec_status = record.status()

    if rec_status == "OVER LIMIT":
        over_limit_count += 1
        Record.over_limit_count += 1

    print()
    print("-" * 34)
    print(f"RECORD CHECK  - {record.label}")
    print("-" * 34)
    print(f"Value:       {record.value:>10.2f}")
    print(f"Limit:       {record.limit:>10.2f}")
    print(f"Difference:  {difference:>+10.2f}")
    print(f"Percent:     {percent:>10.2f}%")
    print(f"Status:      {rec_status:>10}")
    print("-" * 34)
    print()

print(f"Total OVER LIMIT records: {over_limit_count}")