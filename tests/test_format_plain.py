from gendiff.formatters.plain import format_value_plain
from gendiff.scripts.gendiff import generate_diff


def test_format_value_plain():
    assert format_value_plain("text") == "'text'"
    assert format_value_plain(123) == "123"
    assert format_value_plain(True) == "true"
    assert format_value_plain({'a': 1}) == "[complex value]"


def test_format_plain():
    test_file1 = 'tests/test_data/input/plain/file1.json'
    test_file2 = 'tests/test_data/input/plain/file2.json'
    result = generate_diff(test_file1, test_file2, 'plain')
    with open('tests/test_data/expected/expected_plain.txt', 'r') as f:
        expected = f.read()
        assert result == expected
