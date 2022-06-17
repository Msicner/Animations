from load_measurements import load_images_names, load_data, get_average

""" Data constants """
CSV_FILE_PATH: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\Physarum\\vis_map.csv'
DATA_FOLDER: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\measurements_data\\'  # During final testing, change 'testing data' to 'cm_pi'
SAVE_DATA_FOLDER: str = 'C:\\Users\\Matej\\Documents\\Programming\\Projects_git\\Animations\\AstroPi\\csv_config_data'
IMAGES_NAMES: list = load_images_names(DATA_FOLDER)
PHOTO_WEIGHT: float = 0.004
PHOTO_DURATION: int = 20
BASED_ON_PHOTOS: bool = True

"""Measurements data"""
MEASUREMENTS_DATA: dict = load_data(str(DATA_FOLDER + "data.csv"))

""" Constants of cells """
CELLS: list = []
NUM_CELLS: int = 120000  # 3 - 15% of the image area

""" Simulation dimensions """
SIM_WIDTH: int = 1080
SIM_HEIGHT: int = 1080
SPEED: float = 1.0
sensor_distance: float = 1.0
SENSOR_ANGLE: float = 45.0
rotate_angle: int = 45

"""Visual simulation"""
VSIM_NUM_ROWS: int = SIM_HEIGHT
VSIM_NUM_COLUMNS: int = SIM_WIDTH
VSIM_CELL_WEIGHT: float = 0.1#0.03
VSIM_LIFETIME: float = 9.0  # Describes how many frames you can see the cell in vsim_grid
VSIM_DECAY: float = VSIM_CELL_WEIGHT / VSIM_LIFETIME
RGB_IN_CSV: bool = False

""" Visualization """
FRAMES_COUNT: int = 300