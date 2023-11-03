import argparse


def parse_args():
    # description
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    # positional arguments:
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # optional arguments:
    parser.add_argument('-f', '--format',
                        default="stylish",
                        choices=['stylish'],
                        help='set format of output')

    # assign an argument
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
