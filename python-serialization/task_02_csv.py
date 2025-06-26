#!/usr/bin/python3
"""Convert CSV data to JSON format and save it to data.json."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert CSV data to JSON and save to data.json."""
    try:
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except (FileNotFoundError, IOError, csv.Error, json.JSONDecodeError):
        return False
