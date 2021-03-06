import csv
import numpy as np

from constants import CSV_FILE_PATH, VSIM_NUM_ROWS, VSIM_NUM_COLUMNS, RGB_IN_CSV

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
    
    def save_data_to_csv(vsim_grid, photo_index):  # photo_index expects to get data in a form of (bool, int)
        """Saves data to csv file"""
        data_table = []
        num_rows = np.shape(vsim_grid)[0]
        num_columns = np.shape(vsim_grid)[1]
        with open(CSV_FILE_PATH) as csvfile:
            """Reading the data from the CSV file"""
            reader = csv.reader(csvfile)
            for row in reader:
                data_table.append(row)      
            """Updating the lines"""
            # Updating header
            string = data_table[0][-1]
            if photo_index[0] == False:  # If you don't specify the frame number
                time = int(string[1:]) + 1
            elif photo_index[0] == True:  # If you do specify the frame number
                time = photo_index[1]
            string = string[0] + str(time)
            data_table[0].append(string)
            # Updating data representing visual map
            position = 1
            for row in range(num_rows):
                for column in range(num_columns):   
                    pixel_value = round(vsim_grid[row, column] * 255, 2)
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
