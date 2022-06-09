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

"""Initializes whole simulation"""
print("Initializing grid")
start_time = time()
vsim_grid = np.zeros((VSIM_NUM_ROWS, VSIM_NUM_COLUMNS))
CSVFileWriter.initialize_csv()

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
    vsim_grid = CellSimulation.update_simulation(vsim_grid, photo_index)
    if photo_index == 0:  # photo_index % PHOTO_DURATION == 0:  # Every 10th frame, set the simulation according to photo
        print(f"Setting vsim_grid for frame {photo_index + 1}")
        vsim_grid = create_array(IMAGES_NAMES[int(photo_index / PHOTO_DURATION)]) * PHOTO_WEIGHT
        print("vsim_grid has been set")
    else:
        vsim_grid = VisualMap.update_map(vsim_grid, photo_index)
    create_photo(vsim_grid, photo_index)

"""Writing vsim_grid of the last frame into csv"""
CSVFileWriter.save_data_to_csv(vsim_grid, (True, FRAMES_COUNT))
print(f"Data of frame {FRAMES_COUNT} saved succesfully")

print("Runtimetime with", NUM_CELLS, " cells and", VSIM_NUM_ROWS * VSIM_NUM_COLUMNS, "squares took", time() - start_time)
