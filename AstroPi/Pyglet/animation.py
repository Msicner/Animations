import pyglet
from pyglet import gl
from time import process_time

from constants import *

"""Focuses on the animation and redrawing the animation itself"""

class Animation:
    """Class used during animating points in the main window"""
    
    def draw_rectangle(self):
        """Draws a rectangle with the given size on given position."""
        # Sets variables for the drawing
        x1 = self.x - (self.size / 2)
        x2 = self.x + (self.size / 2)
        y1 = self.y - (self.size / 2)
        y2 = self.y + (self.size / 2)
        # Draws the triangles
        gl.glColor3f(self.color[0], self.color[1], self.color[2])
        gl.glBegin(gl.GL_TRIANGLE_FAN)
        gl.glVertex2f(int(x1), int(y1))
        gl.glVertex2f(int(x1), int(y2))
        gl.glVertex2f(int(x2), int(y2))
        gl.glVertex2f(int(x2), int(y1))
        gl.glEnd()

    def change_motion_dir(self, velocity_component):
        self.motion_vector[velocity_component] = -1 * self.motion_vector[velocity_component]
    
    def redraw():
        """Redraws every body on the screen in the list of BODIES"""
        gl.glClear(gl.GL_COLOR_BUFFER_BIT)  # paints with black the whole window
        for body in BODIES:
            Animation.check_walls(body)
            # Animation.check_neighbours(body)
            # STILL DOESN'T WORK AND I DON'T KNOW WHY. IT STOPS ENTIRE ANIMATION
            Animation.draw_rectangle(body)            
        
        #Force.calculate_forces(body)

    def refresh_state(self):
        """Called every time by the pyglet-window to refresh the window itself"""
        for body in BODIES:  # Updates the positions of the bodies on the screen
            body.x += body.motion_vector[0]
            body.y += body.motion_vector[1]

    def check_walls(self):
        """Checks wheteher the body is in the contact with a wall"""
        if self.x <= REC_SIZE / 2 or self.x >= WIDTH:  # Checks whether there is a wall in x-direction
            Animation.change_motion_dir(self, 0)

        elif self.y <= REC_SIZE / 2 or self.y >= HEIGHT:  # Checks whether there is a wall in y-direction
            Animation.change_motion_dir(self, 1)
    
    def check_neighbours(self):
        """Checks whether the body is in the contact with somenone else"""
        # Setting the surroundings of the particle
        max_x = self.x + REC_SIZE
        min_x = self.x - REC_SIZE
        max_y = self.y + REC_SIZE
        min_y = self.y - REC_SIZE
        
        for neighbour in BODIES:
            if neighbour.x > min_x and neighbour.x < max_x:
                if neighbour.y > min_y and neighbour.y < max_y:
                    if abs(neighbour.x - self.x) < abs(neighbour.y - self.y):  # Neighbour is closer to right or left → it will repel in x-direction
                        Animation.change_motion_dir(self, 0)
                    elif abs(neighbour.x - self.x) > abs(neighbour.y - self.y):  # Neighbour is closer to top or bottom → it will repel in y-direction
                        Animation.change_motion_dir(self, 1)
                    else:  # Neighbour is going tovards the corner of 'self' → it will repel in both x and y directions
                        Animation.change_motion_dir(self, 0)
                        Animation.change_motion_dir(self, 1)


class Force:
    """Works with the internal forces between objects"""

    def get_distance(self, object2) -> tuple:
        dif_x = object2.x - self.x
        dif_y = object2.y - self.y
        return [dif_x, dif_y]

    def calculate_forces(self):
        for body in BODIES:
            for body2 in BODIES:
                if body == body2:
                    continue
                else:
                    Force.get_distance(body, body2)