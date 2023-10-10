from gendiff.logic.generate_diff import generate_diff
from gendiff.logic.logic_argparse import file_path1, file_path2
import json


# accept json and returns a dict
def get_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


# returns a dict for futher processing
data1 = get_data(file_path1)
data2 = get_data(file_path2)


def main():
    if file_path1[-4:] and file_path2[-4:] == 'json':
        diff = generate_diff(data1, data2)
        print(diff)


if __name__ == '__main__':
    main()
