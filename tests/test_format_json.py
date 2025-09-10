import json

from gendiff.scripts.gendiff import generate_diff


def test_format_json():
    test_file1 = 'tests/test_data/input/json/file1.json'
    test_file2 = 'tests/test_data/input/json/file2.json'
    result = generate_diff(test_file1, test_file2, 'json')
    with open('tests/test_data/expected/expected_json.txt', 'r') as f:
        expected = f.read()
        assert result == expected
