from random import random, uniform
from math import sin, cos

from constants import *
from body import Body

def set_bodies():
    """Sets the initial positions and motion_vectors for bodies on the screen"""
    angle = 360 / NUM_BODIES
    for i in range(NUM_BODIES):
        
        # From the center 
        x = sin(angle * i) * RADIUS + 0.5 * WIDTH
        y = cos(angle * i) * RADIUS + 0.5 * HEIGHT
        x_velocity = sin(angle * i) * SPEED
        y_velocity = cos(angle * i) * SPEED 
        
        
        """ # Random
        x = random() * WIDTH
        y = random() * HEIGHT
        x_velocity = uniform(-SPEED, SPEED)
        y_velocity = uniform(-SPEED, SPEED) """

        BODIES.append(Body(x_pos = x, 
                           y_pos = y, 
                           motion_vector = [x_velocity, y_velocity]
                           ))