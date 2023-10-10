import argparse


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
file_path1 = f'source_file/{args.first_file}'
file_path2 = f'source_file/{args.second_file}'
