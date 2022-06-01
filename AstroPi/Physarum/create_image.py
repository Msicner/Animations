import numpy as np
from PIL import Image
import csv
from typing import List

from constants import *

PATH_TO_DATA = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Physarum\\vis_map.csv'


class Photo():
    def __init__(self, name: str) -> None:
        self.name = name
        self.pixels = np.zeros([VSIM_NUM_ROWS, VSIM_NUM_COLUMNS, 3], dtype=np.uint8)

    def save(self):
        """ Saves the image as a file """
        img = Image.fromarray(self.pixels)
        img.save(self.name)
        print(f"Image {self.name} saved")


def get_data() -> List[List[str]]:
    """ Extracts data from csv file """
    with open(PATH_TO_DATA, 'r') as file:
        reader = csv.reader(file)
        lines = []
        for row in reader:
            lines.append(row)
        return lines


def create_photos(data: List[List[str]]) -> None:
    """ Saves multiple photos from list """
    for photo_index in range(FRAMES_COUNT + 1):
        photo = Photo(f'frame_{photo_index+1}.png')
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
        print(f"Saving photo {photo_index}")
        photo.save()

data = get_data()
create_photos(data)
