import os


def parse_line(raw_line):
    """Clean and parse a raw text line into a record dictionary."""
    parts = [p.strip() for p in raw_line.strip().split(",") if p.strip()]
    if len(parts) < 3:
        raise ValueError(f"Invalid record line format: '{raw_line}'")

    label = parts[0].strip()

    # Extract key-value pairs for used and total
    record_dict = {"label": label}
    for part in parts[1:]:
        if "=" in part:
            k, v = part.split("=", 1)
            record_dict[k.strip().lower()] = float(v.strip())

    return {
        "label": record_dict["label"],
        "used": record_dict["used"],
        "total": record_dict["total"],
    }


def status_of(used, total):
    """Return the status classification based on usage percentage."""
    if total == 0:
        return "OK"
    percent = (used / total) * 100
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


# 2. INPUT (Excellent: Write messy records to file and read them back)
sample_data = """  srv-01  ,  used=87 , total=100  
SRV-02,used=125,TOTAL=100
 srv-03 , Used=95 , Total=100 
SRV-04, used=45 , total=100
  srv-05  ,  used=105 , total=100 
"""

filename = "raw_records.txt"
with open(filename, "w") as f:
    f.write(sample_data)

raw_records = []
with open(filename, "r") as f:
    for line in f:
        cleaned_line = line.strip()
        if cleaned_line:
            raw_records.append(cleaned_line)

# 3. PROCESS + OUTPUT
total_records = 0
flagged_records = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record["used"], record["total"])
        print(f"Record: {record} | Status: {status}")

        total_records += 1
        if status in ["OVER LIMIT", "WARNING"]:
            flagged_records += 1

    except ValueError as e:
        print(f"Error parsing record '{raw_record}': {e}")

print("-" * 50)
print(f"Summary: Processed {total_records} records, {flagged_records} flagged.")
