import numpy as np
from PIL import Image
import csv


IMAGE_HEIGHT = 2
IMAGE_WIDTH = 2
FRAME_COUNT = 4


class Photo():
    
    def __init__(self, name) -> None:
        self.name = name
        self.pixels = np.zeros([2, 2, 3], dtype=np.uint8)

    def save(self):
        img = Image.fromarray(self.pixels)
        img.save(self.name)



with open('/home/martin/Documents/programování/astropi2021/postpro/Animations/AstroPi/image_processing/pixels.csv', 'r') as file:
    reader = csv.reader(file)
    lines = []
    for row in reader:
        lines.append(row)
        print(row)

for photo_index in range(FRAME_COUNT):
    print(photo_index)
    photo = Photo(f'frame_{photo_index+1}.png')
    for row in lines[1:]:
        print(f'Entering row {row[0]} on frame {photo_index+1}')
        values = row[photo_index+1]
        print(f"This line contains: _{values}_ with lenght of {len(values)}")
        index = 0
        for letter in values:
            print(f"{index}: _{letter}_")
            index += 1
        values = values[1:values.find(')')]
        values = values.split(', ')
        print(values)
        photo.pixels[int(row[0][1]), int(row[0][4])] = values

    photo.save()

# array = np.zeros([100, 200, 3], dtype=np.uint8)
# array[:,:100] = [255, 128, 0] #Orange left side
# array[:,100:] = [0, 0, 255]   #Blue right side
# array[0,0] = [0, 0, 255]
