from random import random
from time import time
import numpy as np

from constants import *
from cell import Cell
from visual_map import VisualMap
from cell_simulation import CellSimulation
from csv_writing import CSVFileWriter

"""Initializes whole simulation"""
start_time = time()
vsim_grid = np.zeros((VSIM_NUM_ROWS, VSIM_NUM_COLUMNS))
CSVFileWriter.initialize_csv()

"""Initialize cells/particles"""
for cell in range(NUM_CELLS):
    position_x = random() * SIM_WIDTH
    position_y = random() * SIM_HEIGHT
    rotation = random() * 360
    speed = SPEED
    CELLS.append(Cell(position_x, position_y, rotation, speed))

    VisualMap.update_square_value(position_x, position_y, vsim_grid)

for _ in range(FRAMES_COUNT):
    vsim_grid = CellSimulation.update_simulation(vsim_grid)
    CSVFileWriter.save_data_to_csv(vsim_grid)

print("Runtimetime with", NUM_CELLS, " cells and", VSIM_NUM_ROWS * VSIM_NUM_COLUMNS, "squares took", time() - start_time)
