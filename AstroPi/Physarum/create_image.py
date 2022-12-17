from importlib.resources import path
import numpy as np
from PIL import Image
import csv
from typing import List
import os

from constants import *

class Photo():
    def __init__(self, name: str) -> None:
        self.name = name
        self.pixels = np.zeros([VSIM_NUM_ROWS, VSIM_NUM_COLUMNS, 3], dtype=np.uint8)

    def save(self, folder_name):
        """ Saves the image as a file """
        img = Image.fromarray(self.pixels)
        dir = os.path.join("H:\\Sdílené disky\\AstroPi Hackatrons\\2021 2022\\data\\sequences\\Photos - Physarum", folder_name)
        if not os.path.exists(dir):
            os.mkdir(dir)
        img.save(f"H:\\Sdílené disky\\AstroPi Hackatrons\\2021 2022\\data\\sequences\\Photos - Physarum\\{folder_name}\\{self.name}")
        print(f"{self.name} saved\n")
        print("-------------------------------------")


def get_data() -> List[List[str]]:
    """ Extracts data from csv file """
    with open(CSV_FILE_PATH, 'r') as file:
        reader = csv.reader(file)
        lines = []
        for row in reader:
            lines.append(row)
        return lines


def create_photos_from_csv(data: List[List[str]]) -> None:
    """ Saves multiple photos from list """
    for photo_index in range(FRAMES_COUNT + 1):
        photo = Photo(f'frame_{photo_index+1}.png')
        print(f"Creating image {photo_index}") 
        # ---- SETTING VALUES OF EACH PIXEL ----
        for row in data[1:]:
            # - reformating string rgb values to List -
            position = row[0]
            position = position[1:position.find(')')]
            position = position.split(', ')
            position[0] = int(position[0])
            position[1] = int(position[1])
            values = row[photo_index+1]
            values = values[1:values.find(')')]
            if RGB_IN_CSV == True:  # If you want to colorize pixels
                values = values.split(', ')
                values[0] = float(values[0])
                values[1] = float(values[1])
                values[2] = float(values[2])
            else:
                values = [float(values), float(values), float(values)]
            
            # - setting value of one pixel
            photo.pixels[position[0], position[1]] = values
        
        # ---- SAVING THE IMAGE ----
        print(f"Saving photo {photo_index + 2}")
        photo.save()

def create_photo(data, photo_index, folder: str = "1"):
    """Creates single photo based on values of pixels, not from csv"""
    photo = Photo(f'frame_{photo_index+1}.png')
    values = []
    for row in range(VSIM_NUM_ROWS):
        for column in range(VSIM_NUM_COLUMNS):
            value = float(data[row, column]) * 255
            values = [value, value, value]
            # Setting the value of one pixel
            photo.pixels[row, column] = values

    # ---- SAVING THE IMAGE ----
    print(f"Saving photo {photo_index + 1}")
    photo.save(folder)
    
