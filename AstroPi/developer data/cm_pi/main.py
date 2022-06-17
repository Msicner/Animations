from sense_hat import SenseHat
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
from logzero import logger, logfile
import csv
from orbit import ISS
from skyfield.api import load
from picamera import PiCamera
from gpiozero import CPUTemperature



# define some constants
sense = SenseHat()
base_folder = Path(__file__).parent.resolve()
csv_file = base_folder/'data.csv'
logfile(base_folder/"cmpi.log")
start_time = datetime.now()
now_time = datetime.now()
cam = PiCamera()
cam.resolution = (1920,1920)
cpu = CPUTemperature()



def convert(angle):
    """
    Convert a `skyfield` Angle to an EXIF-appropriate
    representation (rationals)
    e.g. 98° 34' 58.7 to "98/1,34/1,587/10"

    Return a tuple containing a boolean and the converted angle,
    with the boolean indicating if the angle is negative.
    """
    try:
        sign, degrees, minutes, seconds = angle.signed_dms()
        exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
        return sign < 0, exif_angle
    except Exception as e:
        logger.error(f'Error has occured in "convert". Message:{e}')

def capture(camera, image, measurement):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    try:
        point = measurement[6]
        # Convert the latitude and longitude to EXIF-appropriate representations
        south, exif_latitude = convert(point.latitude)
        west, exif_longitude = convert(point.longitude)

        # Set the EXIF tags specifying the current location
        camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
        camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
        camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
        camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"



        # Capture the image
        camera.capture(image)
    except Exception as e:
        logger.error(f'Error has occured in "capture". Message:{e}')

def save_output(output):
    """ Saves data to csv file. """
    try:
        # write data to csv file
        with open(csv_file, mode='a', encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(output)
    except Exception as e:
        logger.error(f'Error has occured in "save_output". Message:{e}')




def take_single_measurement(meassure_index):
    """ Meassures values and each 30th measurement takes photo """
    try:
        # meassure data
        measurement = (meassure_index, datetime.now(), sense.temperature, sense.humidity, sense.get_accelerometer(), sense.pressure, ISS.coordinates(), cpu.temperature)
        logger.info('Meassurement was taken')
        save_output(measurement)
        if meassure_index % 30 == 0:
            logger.info(f'Image gps{meassure_index} was taken.')
            capture(cam, f"{base_folder}/image{meassure_index}.jpg", measurement)
        
    except Exception as e:
        logger.error(f'Error has occured in "take_single_meassurement". Message:{e}')


# write hearer
with open(csv_file, mode='w', encoding="utf-8") as f:
    writer = csv.writer(f)
    header = ("Id", "Time", "Temperature", "Humidity", "Orientation", "Pressure", "Location", "CPUTemperature")
    writer.writerow(header)

logger.info('start')
 # collecting data
meassure_index = 0
while now_time < start_time + timedelta(minutes=180):
    take_single_measurement(meassure_index)
    meassure_index += 1
    sleep(1)
    now_time = datetime.now()
