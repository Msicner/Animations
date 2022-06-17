import csv
from os import listdir

def load_data(filename: str, header: bool = True) -> list[list[int]]:
    """Returns data from csv as list"""
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        lines = {}
        i = 0
        for row in reader:
            if header == True and i == 0:
                i += 1
                continue
            """Index: [Temperature, Pressure, CPU Temperature] → [speed, sensor_distance, rotate_angle]"""
            speed = (float(row[1]) - 44.13038635) / 2.16918183 * 0.9 + 0.1  # 0.1 → 1
            sensor_distance = (float(row[1]) - 44.13038635) / 2.16918183 * 3 + 1  # 1 → 4
            rotate_angle = (997.4885254 - float(row[2])) / 0.3762207 * 5 + 45  # 50 → 45
            lines.update({int(row[0]):[speed, sensor_distance, rotate_angle]})
            i += 1
    return lines

def load_images_names(data_folder):
    images_names = []
    for image in listdir(data_folder):
        if (image.endswith(".jpg")):
            images_names.append(image)
    return images_names

def get_average(data: dict, quantity_index: int):
    quantity_list = []
    for row in data:
        quantity_list.append(data[row][quantity_index])
    avg = sum(quantity_list) / len(quantity_list)
    maximum = max(quantity_list)
    minimum = min(quantity_list)
    return (avg, maximum, minimum)