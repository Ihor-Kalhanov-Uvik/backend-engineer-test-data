import os
import csv
from datetime import datetime
from csvsort import csvsort


def save_to_csv(data):
    with open(f'output_{datetime.now()}.csv', 'w') as write_file:
        writer = csv.writer(write_file)
        for key, value in data.items():
            writer.writerow([key, value])


if __name__ == '__main__':
    csvsort('data.csv', [0], max_size=100, output_filename='sorted_by_name.csv', has_header=True)
    sorted_data = {}
    with open('sorted_by_name.csv') as read_file:
        reader = csv.reader(read_file)
        next(reader)

        for row in reader:
            state_name = row[0]
            if state_name not in sorted_data:
                sorted_data[f'{state_name}'] = int(row[2])

            elif state_name in sorted_data:
                sorted_data[f'{state_name}'] += int(row[2])

    save_to_csv(sorted_data)
    os.remove("sorted_by_name.csv")

