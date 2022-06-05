# how many ms does it take to update → higher means slower
SPEED: int = 10

# proportions of the window(only displayed values)
WIDTH: int = 5000 
HEIGHT: int = 5000

# how many pixels it can move in one step
MOVE: int = 5

# number of lines
NUM_LINES: int = 3

# starting positions of each line and then coordinates of the last point
START_X: list = []
START_Y: list = []

# list of the line elements 
LINES: list = []

# width of the lines
LINE_WIDTH: int = 2

# colour of the line
LINE_COLOR: str = "green" 

# directions in which the point can move
DIRECTION = [-1, 1]