import pytest
from gendiff.formatters.plain import format_value_plain
from gendiff.scripts.gendiff import generate_diff


def test_format_value_plain():
    assert format_value_plain("text") == "'text'"
    assert format_value_plain(123) == "123"
    assert format_value_plain(True) == "true"
    assert format_value_plain({'a': 1}) == "[complex value]"


@pytest.mark.parametrize("file1,file2, expected",
                         [('tests/test_data/file1_tree.json',
                           'tests/test_data/file2_tree.json',
                           'tests/test_data/expected/expected_plain.txt')])
def test_format_plain(file1, file2, expected):
    result = generate_diff(file1, file2, 'plain')
    with open(expected) as f:
        exp = f.read()
        assert result == exp
