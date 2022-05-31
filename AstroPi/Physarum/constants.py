CSV_FILE_PATH: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Physarum\\vis_map.csv'

# Constants of cells
CELLS: list = []
NUM_CELLS: int = 1000

# Simulation dimensions
SIM_WIDTH: int = 200
SIM_HEIGHT: int = 200
SPEED: float = 5.0
SENSOR_DISTANCE: int = 10
SENSOR_ANGLE: int = 45

# Visual simulation
VSIM_GRID: list  = []
VSIM_NUM_ROWS: int = 200
VSIM_NUM_COLUMNS: int = 200
VSIM_CELL_WEIGHT: float = 0.05
RGB_IN_CSV: bool = False

# Visualization
FRAMES_COUNT: int = 2  # Don't try to increase it, it will freeze your computer completely