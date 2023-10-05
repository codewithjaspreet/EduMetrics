

import csv


def make_csv(file_name, headers, *lists):
    csv_filename = file_name + ".csv"

    transposed_lists = list(zip(*lists))

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(headers)

        for row in transposed_lists:
            writer.writerow(row)

    print(f"CSV file '{csv_filename}' has been created.")

