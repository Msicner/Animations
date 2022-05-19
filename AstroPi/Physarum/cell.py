from constants import *

class Cell:
    """ Workswith separate cells and does operations with it"""
    def __init__(
            self,
            position_x,
            position_y,
            rotation,
            speed
            ) -> object:
        self.position_x = position_x
        self.position_y = position_y
        # Rotation is measured from the direction right and it is increasing counterclockwise, measured in degrees
        self.rotation = rotation  
        self.speed = speed