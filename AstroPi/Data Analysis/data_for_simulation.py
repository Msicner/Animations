import csv

filename = "C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Sample Data\\sample_data_izzy.csv"

fields = []
rows = []

with open(filename, "r") as csvfile:
    cvsreader = csv.reader(csvfile)

    fields = next(cvsreader)

    for row in cvsreader:
        rows.append(row)

def get_avg(column_number: int) -> float:
    global rows
    
    sum = float(0)
    num_rows = len(rows)
    for row in rows:
        sum = sum + float(row[column_number])

    avg = sum / num_rows

    return avg

print(fields)
print(len(rows))

averages = {}
for column in range(1, len(fields) - 2):
    avg_value = get_avg(column)
    averages.update([(fields[column], avg_value)])

print(averages)