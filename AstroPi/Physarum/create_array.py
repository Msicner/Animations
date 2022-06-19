import PIL
import numpy
from numpy import asarray
from PIL import Image
import csv
import os

from constants import *

np = numpy
table = {}
def get_image_array(name: str):
    # load the image
    path = str(DATA_FOLDER + name)
    image = Image.open(path)
    grayscale_image = image.convert('L')
    data = asarray(grayscale_image)
    return data

def rgb_list_to_value(element:list):
    return round(sum(element) / 3, 2)

def create_array(image_name: str, write_data_to_csv: bool = False):
    """Creates simple array according to the photos in the folder"""
    data = get_image_array(image_name)
    image_name = image_name.replace(".jpg", "")
    if write_data_to_csv == True:  # Only if you want to write data to csv file
        print("Writing data to csv")
        write_data(data, image_name)
    return data

def write_data(data_to_write, frame_name):
    with open(os.path.join(SAVE_DATA_FOLDER, f'{frame_name}_data.csv'), 'w', buffering=1, newline='') as file:
        writer = csv.writer(file)
        header = ['pixels y x', f'{frame_name}']
        writer.writerow(header)
        for row in range(len(data_to_write)):
            for column in range(len(data_to_write[row])):
                row_data = []
                row_data.append(f'({row}, {column})')
                row_data.append(f"({data_to_write[row, column]})")
                writer.writerow(row_data)
