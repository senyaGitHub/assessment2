import csv


def load_data(path):
    with open(path, newline='') as csvfile:
        record = list(csv.reader(csvfile))
    return record
