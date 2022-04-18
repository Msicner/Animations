import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import random
from animations_matplotlib.constants import *

START_X = random.randint(0, WIDTH) # start position
x_points = START_X * np.ones((1, 1)) # creates array of 100 elements equal to 1 and it has got one row

#z = 50 * np.ones((100, 1)) # creates array of 100 elements equal to 1 * 50 and it has got one row
#x_points = np.concatenate((x_points, z)) # merges two arrays together
START_Y = random.randint(0, HEIGHT)
y_points = START_Y * np.ones((1, 1))

# generate 3 curves
#y_points = np.copy(x_points)
#y_points[:, 0] = np.cos(y_points[:, 0] )
#y_points[:, 1] = 5
#y_points[:, 2] = 5 #np.sin(y_points[:, 2] ) + np.cos(y_points[:, 2])

fig, ax = plt.subplots()
plt.axis("off")
ax = plt.axes(xlim=(0,WIDTH), ylim=(0, HEIGHT))
line1, = ax.plot([], [], lw=LINE_WIDTH)
#line2, = ax.plot([], [], lw=2)
#line3, = ax.plot([], [], lw=2)

def new_point(round):
    global x_points, y_points, START_X, START_Y

    """ for x_points """
    x_dir = random.randint(-2, 2)
    x_coord = START_X + (MOVE * x_dir)
    x_new = x_coord * np.ones((1, 1))

    x_points = np.concatenate((x_points, x_new))
    START_X = x_coord
    
    """ for y_points """
    y_dir = random.randint(-2, 2)
    y_coord = START_Y + (MOVE * y_dir)
    y_new = y_coord * np.ones((1, 1))

    y_points = np.concatenate((y_points, y_new))
    START_Y = y_coord


def animate(i):
    new_point(i)
    line1.set_data(x_points[:i, 0], y_points[:i, 0])
    #line2.set_data(x_points[:i, 1], y_points[:i, 1])
    #line3.set_data(x_points[:i, 2], y_points[:i, 2])
    #return line1#,line2,line3

anim = FuncAnimation(fig, animate, interval=SPEED)
plt.show()

"""I am doing some change"""
