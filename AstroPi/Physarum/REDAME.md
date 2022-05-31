# Variables
Variables for **background** simulation(with cells) itself has prefix __SIM__
Variables for **visual** simulation(with colored squares) itself has prefix __VSIM__

# Background simulation
## Overall
Rotation of the cell is measured in **degrees** from the horizontal line **pointing right**
## Detection
Every cell has 3 sensors in front of it in the distance __SENSOR_DISTANCE__. First is in the **same direction as the rotation** of the cell. Other two sensors are (+) or (-) __SENSOR_ANGLE__. Every sensors asks the value of the square on its position and cell turns in the **direction of the ones with the highest value**(=brightest). If values of two squares are equal, then the direction is random in range (__-SENSOR_ANGLE__;__+SENSOR_ANGLE__). Simualtion has edge of 1 pixel where there can be no sensor.

# Visual simulation
Visual grid is defined as **list of rows** (in a from of lists) which has same number of elements as the number of columns in visual simulation.
Every single element shows the **brightness of the square** and it's value is between __0 and 1__
## Difuse
We have to find a way, how to add some value to specific squares according to their distance from another. You can do this by finding row and column index for each of them and then looking for this specific position in the list of squares and adding the value to it. But there is maybe some more effective way using the sum of matricies, but it takes more space in memory (because of creating another list) and I am not sure, if this will speed up the whole process.
## Decay
I am not sure, but I think, it is enough to just substract some value form every square after the difuse phase.

# Conclusion
5/19/2022 - 5 000 000 → 107s to generate rotation and update visual map one time
It look like linear realtion between the number of cells and time. Number of squares in visual map almost doesn't affect the simulation runtime.

# Posibilities
You can rewrite whole code in a form of matricies, which can possibly speed up the whole proces.