from os import listdir
# Data constants
CSV_FILE_PATH: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Physarum\\vis_map.csv'
DATA_FOLDER: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\testing_data\\'  # During final testing, change 'testing data' to 'cm_pi'
SAVE_DATA_FOLDER: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\data_for_simulation'
IMAGES_NAMES: list = []
for image in listdir(DATA_FOLDER):
    if (image.endswith(".jpg")):
        IMAGES_NAMES.append(image)
PHOTO_WEIGHT: float = 0.001
PHOTO_DURATION: int = 20

# Constants of cells
CELLS: list = []
NUM_CELLS: int = 300000  #6000 # 15% of the image area

# Simulation dimensions
SIM_WIDTH: int = 1920
SIM_HEIGHT: int = 1920
SPEED: float = 1.0
SENSOR_DISTANCE: float = 15
SENSOR_ANGLE: float = 45  # Smaller angle → doing dots more likely than streams
ROTATE_ANGLE: int = 15

# Visual simulation
VSIM_NUM_ROWS: int = 1920
VSIM_NUM_COLUMNS: int = 1920
VSIM_CELL_WEIGHT: float = 0.01
VSIM_LIFETIME: float = 5.0  # Describes how many frames you can see the cell in vsim_grid
VSIM_DECAY: float = VSIM_CELL_WEIGHT / VSIM_LIFETIME
RGB_IN_CSV: bool = False

# Visualization
FRAMES_COUNT: int = 100