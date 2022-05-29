import PIL
import numpy
from numpy import asarray
from PIL import Image
from typing import List, Tuple
import csv

np = numpy
table = {}
FOLDER = '/home/martin/Documents/programování/astropi2021/postpro/Animations/AstroPi/image_processing/' #REPLACE PATH TO HOME FOLDER
PHOTO_NUMBERS = ['1', '2', '3', '4'] # REPLACE WITH NUMBERS OF PHOTOS
FILE_NAME = 'frame_xxxx.png' # REPLACE WITH NAME OF THE FILE. LEAVE THE "xxxx" AT THE PLACE WHERE IS CHANGED NUBERS OF FILES.
FRAME_COUNT = 4





def get_image_array(name: str):
    # load the image
    image = Image.open(FOLDER + name)
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


for image_index in PHOTO_NUMBERS:
    data = get_image_array(FILE_NAME.replace('xxxx', image_index))
    add_image_to_table(data)


with open(FOLDER + 'pixels_for_matýsek.csv', 'w', buffering=1) as file:
    writer = csv.writer(file)
    header = ['pixels y x']
    for frame in range(1, FRAME_COUNT + 1):
        header.append(f"f{frame}")
    writer.writerow(header)
    for key in table.keys():
        row = [key]
        for frame in table[key]:
            row.append(frame)
        writer.writerow(row)



# print(table)
