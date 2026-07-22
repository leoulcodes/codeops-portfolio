
# telebirr_report.py

totals = {}

try:
    # Step 1: Read file
    with open("transactions.txt") as f:
        for line in f:
            name, amount = line.strip().split(",")
            amount = float(amount)

            # Step 2: Build dictionary (sum per customer)
            totals[name] = totals.get(name, 0) + amount

except FileNotFoundError:
    print("transactions.txt not found. Please add the file.")
    exit()

# Step 3: Sort customers by total spend (highest first)
sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)

# Step 4: Print results
print("CUSTOMER SPENDING REPORT")
print("-" * 35)

for name, total in sorted_totals:
    print(f"{name:<10} : {total:.2f} ETB")

# Step 5: Write to report.txt
with open("report.txt", "w") as report:
    report.write("CUSTOMER SPENDING REPORT\n")
    report.write("-" * 35 + "\n")

    for name, total in sorted_totals:
        report.write(f"{name:<10} : {total:.2f} ETB\n")

print("\nReport saved to report.txt")