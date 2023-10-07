from gendiff.logic.generate_diff import generate_diff
from gendiff.logic.logic_argparse import data1, data2


def main():
    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == '__main__':
    main()
