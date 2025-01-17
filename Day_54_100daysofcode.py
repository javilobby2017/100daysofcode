# csv comma seperated values.
# join function combines lists

import csv 

total = 0.0

with open("Day54totals.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += float(row["Quantity"]) * float(row["Cost"])

print(f"Total: ${round(total,2)}")
