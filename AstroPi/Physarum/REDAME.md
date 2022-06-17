# Variables
Variables for **background** simulation(with cells) itself has prefix __SIM__
Variables for **visual** simulation(with colored squares) itself has prefix __VSIM__

# Background simulation
## Overall
Rotation of the cell is measured in **degrees** from the horizontal line **pointing right**
## Detection
Every cell has 3 sensors in front of it in the distance __SENSOR_DISTANCE__. First is in the **same direction as the rotation** of the cell. Other two sensors are (+) or (-) __SENSOR_ANGLE__. Every sensors asks the value of the square on its position and cell turns in the **direction of the ones with the highest value**(=brightest). If values of two squares are equal, then the direction is random in range (__-SENSOR_ANGLE__;__+SENSOR_ANGLE__).

# Visual simulation
Visual grid is defined as **numpy array** in a shape of (__VSIM_NUM_ROWS__, __VSIM_NUM_COLUMNS__).
Every single element shows the **brightness of the square** and it's value is between __0 and 1__
## Decay
It is done by simply substracting __VSIM_DECAY__ from the array and restricting max value to 1 and min value to 0.
## Difuse
Not implemented yet.
Possible way to implement it is to set value for every square individually depending on its neighbours.

# CSV writing
For saving memory, defaulty only the last state of visual map is written into cvs file. Constant __RGB_IN_CVS__ is defaultly set to false, which means, data in csv are stored just for chromatic photo. If you want to operate with colors of the pixels. Then you need to set value of this variable to true.
# Creating image
Image is defaultly created for every state. Every pixel of the photo is set to the value of corresponding square in __vsim_grid__. Pixels has RGB value, so you can also create data with different RGB data to change colors of individual pixels in the photo. Colorization is not implemented yet. 
# AstroPi implementation
We want to simulate some kind of real particle system. So we will use following measurements for following variables in the simulation. But first you need to create some file with measured data and input this file to the simulation. There should be value of every constant for every individual frame.
## Temperature
Changes the energy of particles → speed of the particles
Higher temperature means higher speed
## Photos
Sets the initial state of the __vsim_grid__ of the simulation. First you need to create grayscale of the photo, then convert it into csv_file and then use this csv file to set value of vsim_grid
## Acceleration
Causes the movement of the camera → synchronized movement of the particles and vsim_grid
## Pressure
Not implemented yet, but it should press particles together.

# Constants
## Num cells(NuC)
Affects the brightness of the simulation
It should be in a range of 3 - 15% of the area of the simulation
Higher NuC means brighter the simulation 
## Speed(S)
For resolution 200x200 it should be around 1
To high speed creates dots instead of lines
## Sensor distance(SD)
Narrows the lines
For bigger resolution, when you increase it, you get "lower resolution" or density of the lines → faster change
## Sensor angle(SA)
## Rotate angle(RA)
## Lifetime(LF)
## Cell weight(CeW)
Affects the brightness of the simulation
