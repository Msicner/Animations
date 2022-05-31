import csv

test_list = ['1', '56', '7']

with open('test.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(test_list)