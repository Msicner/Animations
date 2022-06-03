import numpy as np

from constants import *

class VisualMap:
    def generate_map(vsim_grid):
        """Initializes the visual grid of the simulation with zeroes for every square"""
        vsim_grid = np.zeros((VSIM_NUM_ROWS, VSIM_NUM_COLUMNS))
        return vsim_grid

    def decay(vsim_grid):
        """Decreases value of every single square in vsim_grid"""
        vsim_grid = vsim_grid - VSIM_DECAY
        vsim_grid = np.clip(vsim_grid, 0, 1)
        return vsim_grid

    def get_square(position_x, position_y):
        """Returns the coordinates of the square which contains the given position"""
        square_row = int(position_y // (SIM_HEIGHT/VSIM_NUM_ROWS))
        square_column = int(position_x // (SIM_WIDTH/VSIM_NUM_COLUMNS))
        return square_row, square_column

    def get_square_value(position_x, position_y, vsim_grid):
        """Returns the value(=brigtness) of the square"""
        square_row, square_column = VisualMap.get_square(position_x, position_y)
        brightness = vsim_grid[square_row, square_column]
        return brightness

    def update_square_value(position_x, position_y, vsim_grid):
        """Updates the value of the square with the input of the position of the cell"""
        square_row, square_column = VisualMap.get_square(position_x, position_y)
        vsim_grid[square_row, square_column] = min(vsim_grid[square_row, square_column] + VSIM_CELL_WEIGHT, 1)  # Maximum value is 1
    
    def update_map(vsim_grid, photo_index):
        """Updates the map based on actual positions of cells"""
        if photo_index == 0:
            vsim_grid = VisualMap.generate_map(vsim_grid)
        else:
            vsim_grid = VisualMap.decay(vsim_grid)
        for cell in CELLS:
            VisualMap.update_square_value(cell.position_x, cell.position_y, vsim_grid)
        return vsim_grid