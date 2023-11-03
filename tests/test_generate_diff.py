import pytest
from gendiff.logic.generate_diff import generate_diff


@pytest.mark.parametrize('file_path1, file_path2, result, format', [
    ('file1.json',
     'file2.yaml',
     'tests/fixtures/result_flat.txt',
     'stylish'),

     ('file11.json',
     'file22.json',
     'tests/fixtures/result_stylish.txt',
     'stylish'),
])
def test_generate_diff(file_path1, file_path2, result, format):
    with open(result, 'r') as res:
        assert generate_diff(file_path1, file_path2, format) == res.read()
