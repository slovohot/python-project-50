from gendiff.logic.file_parser import get_data
from gendiff.logic.diff_creator import diff_creator
from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_json import format_json


def generate_diff(file_path1, file_path2, format='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)
    diff = diff_creator(data1, data2)

    if format == 'stylish':
        return format_stylish(diff)
    elif format == 'plain':
        return format_plain(diff)
    else:  # format == 'json':
        return format_json(diff)
