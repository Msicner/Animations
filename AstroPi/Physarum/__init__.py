from random import random
from time import time
import numpy as np

from constants import *
from cell import Cell
from visual_map import VisualMap
from cell_simulation import CellSimulation
from csv_writing import CSVFileWriter
from create_image import create_photo
from create_array import create_array

for frame in IMAGES_NAMES:
    speed = SPEED
    sensor_distance = SENSOR_ANGLE
    rotate_angle = rotate_angle
    CELLS.clear()

    """Initializes whole simulation"""
    print(f"Initializing grid for {frame}")
    start_time = time()
    vsim_grid = np.zeros((VSIM_NUM_ROWS, VSIM_NUM_COLUMNS))
    #CSVFileWriter.initialize_csv()

    """Initialize cells/particles"""
    print("Initializing cells")
    for cell in range(NUM_CELLS):
        position_x = random() * SIM_WIDTH
        position_y = random() * SIM_HEIGHT
        rotation = random() * 360
        speed = SPEED
        CELLS.append(Cell(position_x, position_y, rotation, speed))

        VisualMap.update_square_value(position_x, position_y, vsim_grid)

    """Saving photo of each frame without writing it into csv"""
    for photo_index in range(FRAMES_COUNT):
        print(f"Building frame {photo_index + 1} of {FRAMES_COUNT}")
        vsim_grid = CellSimulation.update_simulation(vsim_grid, speed, sensor_distance, rotate_angle)
        if photo_index == 0 and BASED_ON_PHOTOS == True:  # photo_index % PHOTO_DURATION == 0:  # Every 10th frame, set the simulation according to photo
            print(f"Setting vsim_grid for frame {photo_index + 1}")
            vsim_grid = create_array(frame) * PHOTO_WEIGHT  # You need to change it if you want to generate multiple photos
            print("vsim_grid has been set")
            photo_number = int(frame.replace("image", "").replace(".jpg", ""))
            speed = MEASUREMENTS_DATA[photo_number][0]
            sensor_distance = MEASUREMENTS_DATA[photo_number][1]
            rotate_angle = MEASUREMENTS_DATA[photo_number][2]
            print(speed, sensor_distance, rotate_angle)
        else:
            vsim_grid = VisualMap.update_map(vsim_grid, photo_index)

        create_photo(vsim_grid, photo_index, frame.replace(".jpg", ""))

    """Writing vsim_grid of the last frame into csv"""
    #CSVFileWriter.save_data_to_csv(vsim_grid, (True, FRAMES_COUNT))
    #print(f"Data of frame {FRAMES_COUNT} saved succesfully")

    print("Runtimetime with", NUM_CELLS, " cells and", VSIM_NUM_ROWS * VSIM_NUM_COLUMNS, "squares took", time() - start_time)
