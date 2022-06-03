CSV_FILE_PATH: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Physarum\\vis_map.csv'

# Constants of cells
CELLS: list = []
NUM_CELLS: int = 6000

# Simulation dimensions
SIM_WIDTH: int = 200
SIM_HEIGHT: int = 200
SPEED: float = 1.0
SENSOR_DISTANCE: float = 9
SENSOR_ANGLE: float = 22.5  # Smaller angle → doing dots more likely than streams
ROTATE_ANGLE: int = 30

# Visual simulation
VSIM_NUM_ROWS: int = 200
VSIM_NUM_COLUMNS: int = 200
VSIM_CELL_WEIGHT: float = 0.1
VSIM_LIFETIME: float = 5.0  # Describes how many frames you can see the cell in vsim_grid
VSIM_DECAY: float = VSIM_CELL_WEIGHT / VSIM_LIFETIME
RGB_IN_CSV: bool = False

# Visualization
FRAMES_COUNT: int = 500