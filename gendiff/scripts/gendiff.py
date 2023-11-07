from gendiff.logic.generate_diff import generate_diff
from gendiff.logic.argparser import parse_args


def main():
    first_file, second_file, format = parse_args()
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
