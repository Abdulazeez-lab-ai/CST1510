# 1. Ask the user for your three values.
label = input("Enter a label (e.g., name, hostname, IP): ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

# 2. Work out what you were NOT given.
difference = first - second
percent = (first / second) * 100

# 3. Print the report.
print()
print("-" * 34)
print(f" RECORD CHECK - {label}")
print("-" * 34)
print(f" First value: {first:>10.2f}")
print(f" Second value:{second:>10.2f}")
print(f" Difference:  {difference:>+10.2f}")
print(f" Percent:     {percent:>10.2f}%")

print("-" * 34)
