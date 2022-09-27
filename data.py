import csv

file = []
with open("features.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        file.append(row)

#delete first column and add character labels
with open("features.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    for row in file:
        row.append(row[0][0])
        row.pop(0)
    writer.writerows(file)
