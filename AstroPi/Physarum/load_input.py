import os
import csv

def load_input():
    input_data = []
    file_path = os.path.realpath(__file__)
    file_path = file_path.replace("load_input.py", "App\\data.csv")

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            input = row[0].split(": ")
            input_data.append(input[1])
    return input_data
