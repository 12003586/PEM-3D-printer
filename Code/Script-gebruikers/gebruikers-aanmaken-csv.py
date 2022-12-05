import csv

with open("Studenten.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
print(header)
