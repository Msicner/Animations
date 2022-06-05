import PIL
import numpy
from numpy import asarray
from PIL import Image
from typing import List, Tuple
import csv
from os import listdir

from constants import *

np = numpy
table = {}
images_names: list = []  # List of all names of files ending with .png 

for image in listdir(DATA_FOLDER):
    # check if the image ends with jpg
    if (image.endswith(".jpg")):
        images_names.append(image)

def get_image_array(name: str):
    # load the image
    image = Image.open(DATA_FOLDER + name)
    data = asarray(image)
    return data


def add_image_to_table(data):
    for y_axis in range(len(data)):
        for x_axis in range(len(data[y_axis])):
            key = f"({y_axis}, {x_axis})"
            pixel = pixel_to_string(data[y_axis][x_axis])
            if key in table.keys():
                table[key].append(pixel)
            else:
                table[key] = [pixel]


def pixel_to_string(rbg_array):
    return f"({rbg_array[0]}, {rbg_array[1]}, {rbg_array[2]})"

def create_array(photo_names: list = images_names):
    for image_name in photo_names:
        data = get_image_array(image_name)
        image_name = image_name.replace(".jpg", "")
        write_data(data, image_name)

def write_data(data_to_write, frame_name):
    with open(f'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\data_for_simulation\\{frame_name}_data.csv', 'w', buffering=1, newline='') as file:
        writer = csv.writer(file)
        header = ['pixels y x', f'{frame_name}']
        writer.writerow(header)
        for row in range(len(data_to_write)):
            for column in range(len(data_to_write[row])):
                row_data = []
                row_data.append(f'({row}, {column})')
                row_data.append(f"({round(sum(data_to_write[row, column]) / 3, 2)})")
                writer.writerow(row_data)

create_array()
