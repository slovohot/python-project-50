import yaml
import json
import os
from gendiff.logic.create_diff import create_diff
from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_json import format_json


# accept json/yaml and returns a dict
def get_data(file_path):
    directory_path = 'tests/fixtures/'
    _, extension = os.path.splitext(file_path)
    file_path = os.path.join(directory_path, file_path)

    with open(file_path, 'r') as file:
        if extension == '.json':
            return json.load(file)

        elif extension == '.yml' or extension == '.yaml':
            yaml_data = yaml.safe_load(file)
            formatted_data = {}

            for key, value in yaml_data.items():
                if isinstance(value, list) and len(value) == 1:
                    formatted_data[key] = value[0]

                else:
                    formatted_data[key] = value
            return formatted_data


def generate_diff(file_path1, file_path2, format='stylish'):

    print(f"Loading data from {file_path1}")
    data1 = get_data(file_path1)
    # print(f"Data from {file_path1}: {data1}")

    print(f"Loading data from {file_path2}")
    data2 = get_data(file_path2)
    # print(f"Data from {file_path2}: {data2}")

    diff = create_diff(data1, data2)

    if format == 'stylish':
        return format_stylish(diff)
    elif format == 'plain':
        return format_plain(diff)
    else:  # format == 'json':
        return format_json(diff)
