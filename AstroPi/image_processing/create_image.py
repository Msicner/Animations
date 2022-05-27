import numpy as np
from PIL import Image
import csv
from typing import List



IMAGE_HEIGHT = 2
IMAGE_WIDTH = 2
FRAME_COUNT = 4
PATH_TO_DATA = '/home/martin/Documents/programování/astropi2021/postpro/Animations/AstroPi/image_processing/pixels.csv'


class Photo():
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.pixels = np.zeros([2, 2, 3], dtype=np.uint8)

    def save(self):
        """ Saves the image as a file """
        img = Image.fromarray(self.pixels)
        img.save(self.name)


def get_data() -> List[List[str]]:
    """ Extracts data from csv file """
    with open(PATH_TO_DATA, 'r') as file:
        reader = csv.reader(file)
        lines = []
        for row in reader:
            lines.append(row)
            print(row)
        return lines


def create_photos(data: List[List[str]]) -> None:
    """ Saves multiple photos from list """
    for photo_index in range(FRAME_COUNT):
        print(photo_index)
        photo = Photo(f'frame_{photo_index+1}.png')
        # ---- SETTING VALUES OF EACH PIXEL ----
        for row in lines[1:]:
            # - reformating string rgb values to List -
            values = row[photo_index+1]
            values = values[1:values.find(')')]
            values = values.split(', ')
            
            # - setting value of one pixel
            photo.pixels[int(row[0][1]), int(row[0][4])] = values
        
        # ---- SAVING THE IMAGE ----
        photo.save()
