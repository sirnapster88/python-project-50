from gendiff.find_diff import generate_diff


def test_recursive_dif():
    result = generate_diff('tests/test_data/file1_tree.json', 
                           'tests/test_data/file2_tree.json')
    with open('tests/test_data/expected/expected_recursive.txt') as f:
        expected = f.read()
        assert result == expected
    
