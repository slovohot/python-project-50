import argparse
import json


# description
parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')


# positional arguments:
parser.add_argument('first_file')
parser.add_argument('second_file')


# optional arguments:
parser.add_argument('-f', '--format', help='set format of output')


# assign an argument
args = parser.parse_args()


# file path
file_path1 = f'test/source_file/{args.first_file}'
file_path2 = f'test/source_file/{args.second_file}'


# accept json and returns a dict
def get_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


# returns a dict for futher processing
data1 = get_data(file_path1)
data2 = get_data(file_path2)
