from gendiff.find_diff import generate_diff


def test_yaml_files():
    result = generate_diff('tests/test_data/file1.yml',
                           'tests/test_data/file2.yml')
    with open('tests/test_data/expected/expected_yaml.txt') as f:
        expected = f.read()
        assert result == expected
