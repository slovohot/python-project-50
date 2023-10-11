from gendiff.logic.generate_diff import generate_diff
from gendiff.logic.logic_argparse import file_path1, file_path2


def main():
    diff = generate_diff(file_path1, file_path2)
    print(diff)


if __name__ == '__main__':
    main()
