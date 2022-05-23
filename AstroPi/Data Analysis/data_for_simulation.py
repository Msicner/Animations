import csv

sensors_file = "C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Sample Data\\sample_data_izzy.csv"
photos_file = "C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Sample Data\\LUT_cmpi_1.csv"

measurements = []

class Measurement:
    def __init__(self,data: list):
        self.index = data[0]
        self.temperature = data[2]
        self.humidity = data[4]
        self.pressure = data[5]

        measurements.append(self)

with open(sensors_file, "r") as csvfile:
    fields = []

    cvsreader = csv.reader(csvfile)

    fields = next(cvsreader)

    for row in cvsreader:
        Measurement(row)
    
    print(len(measurements))

def get_avg(column_number: int) -> float:
    global rows
    
    sum = float(0)
    num_rows = len(rows)
    for row in rows:
        sum = sum + float(row[column_number])

    avg = sum / num_rows

    return avg

""" print(fields)

averages = {}
for column in range(1, len(fields) - 2):
    avg_value = get_avg(column)
    averages.update([(fields[column], avg_value)])

print(averages) """