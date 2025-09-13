import pytest
from gendiff.find_diff import generate_diff


@pytest.mark.parametrize("file1,file2,expected",
                         [('tests/test_data/input/equal/file1.json',
                           'tests/test_data/input/equal/file2.json',
                           'tests/test_data/expected/expected_equal_files.txt'),
                            ('tests/test_data/input/diff_values/file1.json',
                            'tests/test_data/input/diff_values/file2.json',
                            'tests/test_data/expected/expected_diff_values.txt'),
                            ('tests/test_data/input/diff_keys/file1.json',
                            'tests/test_data/input/diff_keys/file2.json',
                            'tests/test_data/expected/expected_diff_keys.txt'),
                            ('tests/test_data/input/empty_noempty/file1.json',
                             'tests/test_data/input/empty_noempty/file2.json',
                             'tests/test_data/expected/exp_empty_noempty.txt'),
                            ('tests/test_data/input/empty/file1.json',
                             'tests/test_data/input/empty/file1.json',
                             'tests/test_data/expected/expected_empty.txt')])
def test_gendiff(file1, file2, expected):
    result = generate_diff(file1, file2)
    with open(expected) as f:
        exp = f.read()
        assert result == exp
