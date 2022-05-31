import csv
from email import header

from constants import CSV_FILE_PATH, VSIM_NUM_ROWS, VSIM_NUM_COLUMNS, RGB_IN_CSV

data_table = []

sample_visual_map = [[0.76, 0.56], [0.24, 0.29]]

class CSVFileWriter:
    def initialize_csv():
        """Setting initial values in the csv file."""
        with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            header = ['pixels', 't0']
            writer.writerow(header)
            for rows in range(VSIM_NUM_ROWS):
                for columns in range(VSIM_NUM_COLUMNS):
                    row_data = [f'({rows}, {columns})']
                    if RGB_IN_CSV == True:  # If you want to colorize pixels
                        row_data.append('(255, 255, 255)')
                    else:
                        row_data.append('(255)')
                    writer.writerow(row_data)
    
    def save_data_to_csv(visual_map_data):
        with open(CSV_FILE_PATH) as csvfile:
            """Reading the data from the CSV file"""
            reader = csv.reader(csvfile)
            for row in reader:
                data_table.append(row)      
            """Updating the lines"""
            string = data_table[0][-1]
            time = int(string[1:]) + 1
            string = string[0] + str(time)
            data_table[0].append(string)
            position = 1
            for row in range(len(visual_map_data)):
                for column in range(len(visual_map_data[row])):   
                    pixel_value = round(visual_map_data[row][column] * 255, 2)
                    if RGB_IN_CSV == True:  # If you want to colorize pixels
                        append_value = f'({pixel_value}, {pixel_value}, {pixel_value})'
                    else:
                        append_value = str(f'({pixel_value})')
                    data_table[position].append(append_value)
                    position += 1
        CSVFileWriter.write_data(data_table)

    def write_data(data_to_write):
        """Writing data to csv file"""
        with open(CSV_FILE_PATH, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in range(len(data_to_write)):
                writer.writerow(data_to_write[row])
