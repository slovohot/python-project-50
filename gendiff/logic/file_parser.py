import yaml
import json
import os


# accept json/yaml and returns a dict
def get_data(file_path, default_directory='tests/fixtures/'):
    if os.path.isabs(file_path):
        full_file_path = file_path
    else: 
        full_file_path = os.path.join(default_directory, file_path)

    _, extension = os.path.splitext(full_file_path)

    if extension not in ['.json', '.yml', '.yaml']:
        raise Exception(f"Unsupported file format: {extension}. "
                        f"Please use .json, .yml, or .yaml files.")

    with open(full_file_path, 'r') as file:
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
