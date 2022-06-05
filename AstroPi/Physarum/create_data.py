from os import listdir

from constants import *
from create_array import *

images_names: list = []  # List of all files ending with .png


for images in listdir(folder_dir = DATA_FOLDER):
    # check if the image ends with png
    if (images.endswith(".png")):
        images_names.append(images)

def get_array_from_photos():
    for image_name in images_names:
        data = get_image_array(image_name)
        add_image_to_table(data)
    write_data(len(images_names))