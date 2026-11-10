import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD
df = pd.read_csv("records.csv")

# 2. PROCESS
df["percent"] = (df["value"] / df["limit"]) * 100
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
)

# 3. OUTPUT
# Threshold: Print DataFrame as-is
print("--- All Records ---")
print(df)
print()

# Typical: Filter for non-OK records using boolean indexing
not_ok_df = df[df["status"] != "OK"]
print("--- Attention Needed (Not OK) ---")
print(not_ok_df)
print()

# Excellent: Group by status counts, export CSV, and output bar chart
status_counts = df.groupby("status")["label"].count()
print("--- Status Counts ---")
print(status_counts)

df.to_csv("processed_records.csv", index=False)

status_counts.plot(kind="bar")
plt.title("Record Counts by Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("status_counts.png")