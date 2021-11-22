import os
import csv
from datetime import datetime
from csvsort import csvsort

if __name__ == '__main__':
    # Do efficient external sorting of a large csv by department name
    csvsort('data.csv', [0], max_size=100, output_filename='sorted_by_name.csv', has_header=True)
    current_state_name = ""
    current_sales_sum = 0
    # Open sorted csv
    with open('sorted_by_name.csv') as read_file:
        reader = csv.reader(read_file)
        # skip header
        next(reader)
        # Open output file
        with open(f'output_{datetime.now()}.csv', 'w') as write_file:
            writer = csv.writer(write_file)
            # Read row by row sorted csv file and calculate sales sum for each department along the way.
            # Once we encounter new department we can write down sum of sales of previous department into the output file and continue counting
            for row in reader:
                state_name = row[0]
                if current_state_name and state_name != current_state_name:
                    writer.writerow([current_state_name, current_sales_sum])
                    current_state_name = state_name
                    current_sales_sum = int(row[2])
                else:
                    if not current_state_name:
                        current_state_name = state_name
                    current_sales_sum += int(row[2])

            if current_state_name:
                writer.writerow([current_state_name, current_sales_sum])

    os.remove("sorted_by_name.csv")
