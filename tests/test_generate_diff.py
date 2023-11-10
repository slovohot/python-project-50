import pytest
from gendiff.logic.generate_diff import generate_diff


@pytest.mark.parametrize('file_path1, file_path2, result, format', [
    ('tests/fixtures/file1.json',
     'tests/fixtures/file2.yaml',
     'tests/fixtures/result_flat.txt',
     'stylish'),

    ('tests/fixtures/file11.json',
     'tests/fixtures/file22.json',
     'tests/fixtures/result_stylish.txt',
     'stylish'),

    ('tests/fixtures/file11.json',
     'tests/fixtures/file22.json',
     'tests/fixtures/result_plain.txt',
     'plain'),

    ('tests/fixtures/file11.json',
     'tests/fixtures/file22.json',
     'tests/fixtures/result_json.txt',
     'json')
])
def test_generate_diff(file_path1, file_path2, result, format):
    with open(result, 'r') as res:
        assert generate_diff(file_path1, file_path2, format) == res.read()
