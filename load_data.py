import os
import csv
import chardet

def load_data():
    data = {}
    files = {
        'games': os.getenv('GAMES_FILE_PATH'), 
        'venues': os.getenv('VENUES_FILE_PATH'),
    }

    # Check if environment variable is set for required file paths
    if None in files.values():
        raise ValueError('Error: Environment variable not set for required file path.')

    # Read data from multiple CSV files
    for key, path in files.items():

        #Check if file exists
        if not os.path.exists(path):
            print(f"The file '{path}' does not exist.")
            continue

        # Detect encoding
        with open(path, 'rb') as rawdata:
            result = chardet.detect(rawdata.read(10000))['encoding']

        # Read file and store data
        with open(path, mode='r', encoding=result) as file:
            csv_reader = csv.DictReader(file)
            if key not in data:
                data[key] = []
            for row in csv_reader:
                data[key].append(row)

    return data