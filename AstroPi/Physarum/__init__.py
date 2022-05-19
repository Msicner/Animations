from random import random
from time import time

from constants import *
from cell import Cell
from visual_map import VisualMap
from cell_simulation import CellSimulation

start_time = time()
VisualMap.generate_map()

for cell in range(NUM_CELLS):
    position_x = random() * SIM_WIDTH
    position_y = random() * SIM_HEIGHT
    rotation = random() * 360
    speed = SPEED
    CELLS.append(Cell(position_x, position_y, rotation, speed))

    VisualMap.update_square_value(position_x, position_y)

CellSimulation.update_simulation()

print("Runtimetime with", NUM_CELLS, " cells and", VSIM_NUM_ROWS * VSIM_NUM_COLUMNS, "squares took", time() - start_time)
