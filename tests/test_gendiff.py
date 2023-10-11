from gendiff.logic.generate_diff import generate_diff


file_path1 = 'source_file/file1.json'
file_path2 = 'source_file/file2.json'


def open_result():
    with open('tests/result_json.txt', 'r') as file:
        content = file.read()
    return content


def test_generate_diff():
    assert generate_diff(file_path1, file_path2) == open_result()
