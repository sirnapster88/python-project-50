import pytest
from gendiff.find_diff import generate_diff
from pathlib import Path

TEST_DATA = Path('tests/test_data')
INPUT = TEST_DATA / 'input'
EXPECTED = TEST_DATA / 'expected'

EQUAL = INPUT / 'equal'
DIFF_VALUES = INPUT / 'diff_values'
DIFF_KEYS = INPUT / 'diff_keys'
EMPTY_NOEMPTY = INPUT / 'empty_noempty'
EMPTY = INPUT / 'empty'


@pytest.mark.parametrize("file1,file2,expected",
                         [(EQUAL / 'file1.json',
                           EQUAL / 'file2.json',
                           EXPECTED / 'expected_equal_files.txt'),
                           (DIFF_VALUES / 'file1.json',
                            DIFF_VALUES / 'file2.json',
                            EXPECTED / 'expected_diff_values.txt'),
                           (DIFF_KEYS / 'file1.json',
                            DIFF_KEYS / 'file2.json',
                            EXPECTED / 'expected_diff_keys.txt'),
                           (EMPTY_NOEMPTY / 'file1.json',
                            EMPTY_NOEMPTY / 'file2.json',
                            EXPECTED / 'exp_empty_noempty.txt'),
                           (EMPTY / 'file1.json',
                            INPUT / 'empty/file1.json',
                            EXPECTED / 'expected_empty.txt'),
                           (TEST_DATA / 'file1_tree.json',
                            TEST_DATA / 'file2_tree.json',
                            EXPECTED / 'expected_recursive.txt')])
def test_gendiff(file1, file2, expected):
    result = generate_diff(file1, file2)
    with open(expected) as f:
        exp = f.read()
        assert result == exp
