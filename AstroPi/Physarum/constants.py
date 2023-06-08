from load_measurements import load_images_names, load_data
from load_input import load_input
import os

INPUT = load_input()

""" Data constants """
CSV_FILE_PATH: str = "" #SYSTEM PATH TO YOUR CSV FILE, WHERE THE PROGRAM SHOULD WRITE VISUAL MAP AT THE END
if INPUT[1] != "NOT SET":
    DATA_FOLDER = str(INPUT[1]) + "\\"
else:
    DATA_FOLDER: str = os.path.realpath(__file__).replace("constants.py", "data") + "\\"  #SYSTEM PATH TO THE FOLDER WITH MEASUREMENTS DATA AND IMAGES

SAVE_DATA_FOLDER: str = ""#SYSTEM PATH TO THE FOLER, WHERE YOU WANT TO STORE CSV DATA FROM IMAGES

if INPUT[2] != "NOT SET":
    SAVE_PHOTOS_FOLDER = str(INPUT[2]) + "\\"
else:
    SAVE_PHOTOS_FOLDER: str = os.path.realpath(__file__).replace("constants.py", "export") + "\\" #SYSTEM PATH TO THE FOLDER WHERE YOU WANT TO SAVE YOUR GENERATED IMAGES

IMAGES_NAMES: list = load_images_names(DATA_FOLDER)
PHOTO_WEIGHT: float = 0.004
PHOTO_DURATION: int = 20
BASED_ON_PHOTOS: bool = True

"""Measurements data"""
#MEASUREMENTS_DATA: dict = load_data(str(DATA_FOLDER + "data.csv"))

""" Constants of cells """
CELLS: list = []
if INPUT[3] != "NOT SET":
    NUM_CELLS = int(INPUT[3])
else:
    NUM_CELLS: int = 120000

""" Simulation dimensions """
if INPUT[5] != "NOT SET":
    SIM_WIDTH = int(INPUT[5])
else:
    SIM_WIDTH: int = 1080

if INPUT[6] != "NOT SET":
    SIM_HEIGHT = int(INPUT[6])
else:
    SIM_HEIGHT: int = 1080

if INPUT[10] != "NOT SET":
    SPEED = float(INPUT[10])
else:
    SPEED: float = 1.0

if INPUT[11] != "NOT SET":
    sensor_distance = float(INPUT[11])
else:
    sensor_distance: float = 1.0

if INPUT[12] != "NOT SET":
    SENSOR_ANGLE = float(INPUT[12])
else:
    SENSOR_ANGLE: float = 45.0

if INPUT[13] != "NOT SET":
    rotate_angle = int(INPUT[13])
else:
    rotate_angle: int = 45

"""Visual simulation"""
VSIM_NUM_ROWS: int = SIM_HEIGHT
VSIM_NUM_COLUMNS: int = SIM_WIDTH

if INPUT[14] != "NOT SET":
    VSIM_CELL_WEIGHT = float(INPUT[14])
else:
    VSIM_CELL_WEIGHT: float = 0.1

if INPUT[15] != "NOT SET":
    VSIM_LIFETIME = float(INPUT[15])
else:
    VSIM_LIFETIME: float = 9.0

VSIM_DECAY: float = VSIM_CELL_WEIGHT / VSIM_LIFETIME
RGB_IN_CSV: bool = False

""" Visualization """
if INPUT[4] != "NOT SET":
    FRAMES_COUNT = int(INPUT[4])
else:
    FRAMES_COUNT: int = 100
