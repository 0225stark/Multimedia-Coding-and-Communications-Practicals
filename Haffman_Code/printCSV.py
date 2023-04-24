import csv

with open('symbol_code_table.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
