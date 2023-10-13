from gendiff.logic.generate_diff import generate_diff
from fixtures.fixtures import open_result


file_json1 = 'source_file/file1.json'
file_json2 = 'source_file/file2.json'
file_yaml1 = 'source_file/file1.yaml'
file_yaml2 = 'source_file/file2.yaml'


def test_generate_diff_json(open_result):
    result_json = generate_diff(file_json1, file_json2)
    assert result_json == open_result


def test_generate_diff_yaml(open_result):
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_yaml == open_result


def test_generate_diff_yaml_json(open_result):
    result_json = generate_diff(file_json1, file_json2)
    result_yaml = generate_diff(file_yaml1, file_yaml2)
    assert result_json == result_yaml == open_result
