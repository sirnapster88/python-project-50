import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.mark.parametrize("file1,file2,expected",
                         [('tests/test_data/file1_tree.json',
                           'tests/test_data/file2_tree.json',
                           'tests/test_data/expected/expected_json.txt')])
def test_format_json(file1, file2, expected):
    result = generate_diff(file1, file2, 'json')
    with open(expected) as f:
        exp = f.read()
        assert result == exp
