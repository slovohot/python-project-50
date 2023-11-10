import yaml
import json
import os


# accept json/yaml and returns a dict
def get_data(file_path: str) -> dict:
    extension = file_path.split('.')[-1]

    if extension not in ['json', 'yml', 'yaml']:
        raise Exception(f"Unsupported file format: {extension}. "
                        f"Please use .json, .yml, or .yaml files.")

    with open(file_path, 'r') as file:
        if extension == 'json':
            return json.load(file)

        elif extension == 'yml' or extension == 'yaml':
            return yaml.safe_load(file)
