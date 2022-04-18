import pyglet
from pyglet import gl
from time import process_time

from constants import *
from animation import Animation
from initial_states import set_bodies

"""Draws rectangle on specific position

Diagram:

         y2 - +-----+
              |/////|
         y1 - +-----+
              :     :
             x1    x2
"""

# SEts initial states of the 'bodies'
set_bodies()

# Drives the window itself
window = pyglet.window.Window(width = WIDTH, height = HEIGHT)
pyglet.clock.schedule(Animation.refresh_state)
window.push_handlers(
    on_draw=Animation.redraw
)
pyglet.app.run()