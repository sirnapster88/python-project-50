from gendiff.find_diff import generate_diff


def test_recursive_dif():
    result = generate_diff('tests/test_data/file1.json', 
                           'tests/test_data/file2.json')

    assert "common: {" in result
    assert "group1: {" in result
    assert "group2: {" in result
    assert "setting1: Value 1" in result
    assert "setting2: 200" in result
    assert "setting3: true" in result
    assert "setting3: null" in result
    assert "doge: {" in result
    assert "wow: so much" in result
