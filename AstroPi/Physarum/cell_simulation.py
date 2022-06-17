from math import sin, cos, tan
from random import randrange, choice

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

    def rotate_cell(self: Cell, vsim_grid, sensor_distance, rotate_angle):
        """Checks values of squares on sensors positions and updates the rotation of the cell"""
        # Front sensor
        front_sensor_position_x, front_sensor_position_y = CellSimulation.add_polar_vector(
            self.position_x, 
            self.position_y, 
            self.rotation, 
            sensor_distance)
        front_sensor_value = VisualMap.get_square_value(front_sensor_position_x, front_sensor_position_y, vsim_grid)
        # Left sensor
        angle = CellSimulation.check_angle_value(self.rotation + SENSOR_ANGLE)
        left_sensor_position_x, left_sensor_position_y = CellSimulation.add_polar_vector(
            self.position_x, 
            self.position_y, 
            angle, 
            sensor_distance)
        left_sensor_value = VisualMap.get_square_value(left_sensor_position_x, left_sensor_position_y, vsim_grid)
        # Right sensor
        angle = CellSimulation.check_angle_value(self.rotation - SENSOR_ANGLE)
        right_sensor_position_x, right_sensor_position_y = CellSimulation.add_polar_vector(
            self.position_x, 
            self.position_y, 
            angle, 
            sensor_distance)
        right_sensor_value = VisualMap.get_square_value(right_sensor_position_x, right_sensor_position_y, vsim_grid)

        if front_sensor_value > left_sensor_value and front_sensor_value > right_sensor_value:
            self.rotation += 0  # continue with the same rotation
        elif front_sensor_value < left_sensor_value and front_sensor_value < right_sensor_value:
            self.rotation = CellSimulation.check_angle_value(self.rotation + choice([-1, 1]) * rotate_angle)  # self.rotation + randrange(-rotate_angle, rotate_angle)  |  continue with random rotation
        elif left_sensor_value < right_sensor_value:
            self.rotation = CellSimulation.check_angle_value(self.rotation - rotate_angle)  # right sensor has greatest value → turns right
        elif left_sensor_value > right_sensor_value:
            self.rotation = CellSimulation.check_angle_value(self.rotation + rotate_angle)  # left sensor has greates value → turns left

    def update_simulation(vsim_grid, speed, sensor_distance, rotate_angle):
        for cell in CELLS:
            cell.position_x, cell.position_y = CellSimulation.add_polar_vector(cell.position_x, cell.position_y, cell.rotation, speed)  # Moving the cell
        for cell in CELLS:
            CellSimulation.rotate_cell(cell, vsim_grid, sensor_distance, rotate_angle)  # Rotating the cell
        return vsim_grid
        