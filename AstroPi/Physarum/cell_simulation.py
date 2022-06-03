from math import sin, cos, tan
from random import randrange

from visual_map import VisualMap
from cell import Cell
from constants import *

class CellSimulation:
    def add_polar_vector(position_x, position_y, angle, distance):
        position_x = position_x + cos(angle) * distance
        position_y = position_y + sin(angle) * distance
        if position_x > SIM_WIDTH:
            position_x = position_x - SIM_WIDTH
        elif position_x < 0:
            position_x = position_x + SIM_WIDTH
        if position_y > SIM_HEIGHT:
            position_y = position_y - SIM_HEIGHT
        elif position_y < 0:
            position_y = position_y + SIM_HEIGHT
        return position_x, position_y
    
    def check_angle_value(angle):
        """Check whether the angle value is in the interval (0; 360)"""
        if angle < 0:
            angle = 360 + angle
        return angle

    def rotate_cell(self: Cell, vsim_grid):
        """Checks values of squares on sensors positions and updates the rotation of the cell"""
        # Front sensor
        front_sensor_position_x, front_sensor_position_y = CellSimulation.add_polar_vector(
            self.position_x, 
            self.position_y, 
            self.rotation, 
            SENSOR_DISTANCE)
        front_sensor_value = VisualMap.get_square_value(front_sensor_position_x, front_sensor_position_y, vsim_grid)
        # Left sensor
        angle = CellSimulation.check_angle_value(self.rotation + SENSOR_ANGLE)
        left_sensor_position_x, left_sensor_position_y = CellSimulation.add_polar_vector(
            self.position_x, 
            self.position_y, 
            angle, 
            SENSOR_DISTANCE)
        left_sensor_value = VisualMap.get_square_value(left_sensor_position_x, left_sensor_position_y, vsim_grid)
        # Right sensor
        angle = CellSimulation.check_angle_value(self.rotation - SENSOR_ANGLE)
        right_sensor_position_x, right_sensor_position_y = CellSimulation.add_polar_vector(
            self.position_x, 
            self.position_y, 
            angle, 
            SENSOR_DISTANCE)
        right_sensor_value = VisualMap.get_square_value(right_sensor_position_x, right_sensor_position_y, vsim_grid)

        if right_sensor_value == left_sensor_value:
            self.rotation = CellSimulation.check_angle_value(self.rotation + randrange(-ROTATE_ANGLE, ROTATE_ANGLE))  # Some sensors has the same value
        elif front_sensor_value > right_sensor_value:
            if front_sensor_value > left_sensor_value:
                self.rotation += 0  # Front sensor has greatest value
            elif front_sensor_value < left_sensor_value:    
                self.rotation = CellSimulation.check_angle_value(self.rotation + ROTATE_ANGLE) # Left sensor has greatest value
        elif right_sensor_value > left_sensor_value:
            self.rotation = CellSimulation.check_angle_value(self.rotation - ROTATE_ANGLE) # Right sensor has the greatest value
        elif left_sensor_value > front_sensor_value:
            self.rotation = CellSimulation.check_angle_value(self.rotation + ROTATE_ANGLE)  # Left sensor has greatest value

    def update_simulation(vsim_grid, photo_index):
        for cell in CELLS:
            cell.position_x, cell.position_y = CellSimulation.add_polar_vector(cell.position_x, cell.position_y, cell.rotation, SPEED)  # Moving the cell
        for cell in CELLS:
            CellSimulation.rotate_cell(cell, vsim_grid)  # Rotating the cell
        vsim_grid = VisualMap.update_map(vsim_grid, photo_index)
        return vsim_grid
        