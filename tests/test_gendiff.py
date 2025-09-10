from gendiff.find_diff import generate_diff


def test_equal_files():
    """Тестирование одинаковых файлов"""
    test_file1 = 'tests/test_data/input/equal/file1.json'
    test_file2 = 'tests/test_data/input/equal/file1.json'
    result = generate_diff(test_file1, test_file2)
    with open('tests/test_data/expected/expected_equal_files.txt', 'r') as f:
        expected = f.read()
        assert result == expected
    

def test_diff_values():
    """Тестирование файлов, где отличаются значения"""
    test_file1 = 'tests/test_data/input/diff_values/file1.json'
    test_file2 = 'tests/test_data/input/diff_values/file2.json'
    result = generate_diff(test_file1, test_file2)
    with open('tests/test_data/expected/expected_diff_values.txt', 'r') as f:
        expected = f.read()
        assert result == expected


def test_diff_keys():
    """Тестирование файлов, где отличаются ключи"""
    test_file1 = 'tests/test_data/input/diff_keys/file1.json'
    test_file2 = 'tests/test_data/input/diff_keys/file2.json'
    result = generate_diff(test_file1, test_file2)
    with open('tests/test_data/expected/expected_diff_keys.txt', 'r') as f:
        expected = f.read()
        assert result == expected


def test_empty_nonempty():
    """Тестирование файлов, где один из файлов пустой"""
    test_file1 = 'tests/test_data/input/empty_noempty/file1.json'
    test_file2 = 'tests/test_data/input/empty_noempty/file2.json'
    result = generate_diff(test_file1, test_file2)
    with open('tests/test_data/expected/expected_empty_noempty.txt', 'r') as f:
        expected = f.read()
        assert result == expected


def test_empty_files():
    """Тестирование файлов, где оба файла пустые"""
    test_file1 = 'tests/test_data/input/empty/file1.json'
    test_file2 = 'tests/test_data/input/empty/file2.json'
    result = generate_diff(test_file1, test_file2)
    with open('tests/test_data/expected/expected_empty.txt', 'r') as f:
        expected = f.read()
        assert result == expected

