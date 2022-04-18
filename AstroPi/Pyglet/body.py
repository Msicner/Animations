from constants import *

class Body:
    """Operates with rectangles"""

    def __init__(self,
                 x_pos: int = 0,
                 y_pos: int = 0,
                 size: int = REC_SIZE,
                 motion_vector: tuple = [0, 0],
                 color: tuple = [1, 1, 1]):
        """Sets the initial states of the rectangle"""
        self.x = x_pos
        self.y = y_pos
        self.size = size
        self.motion_vector = motion_vector
        self.color = color
