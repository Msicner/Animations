import numpy as np

from constants import *

class VisualMap:
    def generate_map():
        """Initializes the visual grid of the simulation with zeroes for every square"""
        for rows in range(VSIM_NUM_ROWS):
            row = []
            for columns in range(VSIM_NUM_COLUMNS):
                row.append(0)
            VSIM_GRID.append(row)

    def get_square(position_x, position_y):
        """Returns the coordinates of the square which contains the given position"""
        square_row = int(position_y // (SIM_HEIGHT/VSIM_NUM_ROWS))
        square_column = int(position_x // (SIM_WIDTH/VSIM_NUM_COLUMNS))
        return square_row, square_column

    def get_square_value(position_x, position_y):
        """Returns the value(=brigtness) of the square"""
        square_row, square_column = VisualMap.get_square(position_x, position_y)
        brightness = VSIM_GRID[square_row][square_column]
        return brightness

    def update_square_value(position_x, position_y):
        """Updates the value of the square with the input of the position of the cell"""
        square_row, square_column = VisualMap.get_square(position_x, position_y)
        VSIM_GRID[square_row][square_column] = min(VSIM_GRID[square_row][square_column] + VSIM_CELL_WEIGHT, 1)  # Maximum value is 1
    
    def update_map():
        """Updates the map based on actual positions of cells"""
        for cell in CELLS:
            VisualMap.update_square_value(cell.position_x, cell.position_y)