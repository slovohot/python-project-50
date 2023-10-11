import pytest


@pytest.fixture
def open_result():
    with open('tests/result.txt', 'r') as file:
        content = file.read()
    return content
