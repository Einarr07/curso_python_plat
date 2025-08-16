import statistics
import csv
import os 

cwd = os.getcwd()
file_path = os.path.join(cwd, "biblioteca_estandar")

monthly_sales = {}
with open(os.path.join(file_path, "monthly_sales.csv"), mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        month = row["month"]
        sales = int(row["sales"])
        monthly_sales[month] = sales
        
sales = list(monthly_sales.values())
print(sales)

# the mean
mean_sales = statistics.mean(sales)
print(f"Mean sales: {mean_sales:.2f}")

# Mode
mode_sales = statistics.mode(sales)
print(f"Mode Sales: {mode_sales:.2f}")

# Standard deviation
standard_deviation = statistics.stdev(sales)
print(f"Standard Deviation: {standard_deviation:.2f}")

# Max
max_sales = max(sales)
print(f"Max Sales: {max_sales:.2f}")

# Min
min_sales = min(sales)
print(f"Min Sales: {min_sales:.2f}")

range_sales = max_sales - min_sales
print(f"Range Sales: {range_sales:.2f}")
