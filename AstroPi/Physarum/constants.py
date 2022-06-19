from load_measurements import load_images_names, load_data, get_average

""" Data constants """
CSV_FILE_PATH: str = #SYSTEM PATH TO YOUR CSV FILE, WHERE THE PROGRAM SHOULD WRITE VISUAL MAP AT THE END
DATA_FOLDER: str = #SYSTEM PATH TO THE FOLDER WITH MEASUREMENTS DATA AND IMAGES
SAVE_DATA_FOLDER: str = #SYSTEM PAT TO THE FOLER, WHERE YOU WANT TO STORE CSV DATA FROM IMAGES
IMAGES_NAMES: list = load_images_names(DATA_FOLDER)
PHOTO_WEIGHT: float = 0.004
PHOTO_DURATION: int = 20
BASED_ON_PHOTOS: bool = True

"""Measurements data"""
MEASUREMENTS_DATA: dict = load_data(str(DATA_FOLDER + "data.csv"))

""" Constants of cells """
CELLS: list = []
NUM_CELLS: int = 120000

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
VSIM_CELL_WEIGHT: float = 0.1
VSIM_LIFETIME: float = 9.0
VSIM_DECAY: float = VSIM_CELL_WEIGHT / VSIM_LIFETIME
RGB_IN_CSV: bool = False

""" Visualization """
FRAMES_COUNT: int = 300
