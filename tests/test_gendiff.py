import os
import json
import yaml
import shutil
import tempfile
import pytest
from pathlib import Path
from gendiff.differ import generate_diff
from gendiff.load_files import load_files

@pytest.fixture
def temp_json_files():
    temp_dir =  tempfile.mkdtemp(dir='tests')
    test_file1_path = os.path.join(temp_dir,'test_file1.json')
    test_file2_path = os.path.join(temp_dir,'test_file2.json')
    yield test_file1_path, test_file2_path
    shutil.rmtree(temp_dir)


def create_json_test_file(test_file_path, data):
    with open(test_file_path, 'w') as f:
        json.dump(data, f)


def test_equal_files(temp_json_files):
    """Тестирование одинаковых файлов"""
    test_file1_path, test_file2_path = temp_json_files
    data = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }
    create_json_test_file(test_file1_path, data)
    create_json_test_file(test_file2_path, data)
    result = generate_diff(test_file1_path, test_file2_path)
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    assert result == expected

def test_diff_values(temp_json_files):
    """Тестирование файлов, где отличаются значения"""
    test_file1_path, test_file2_path = temp_json_files
    data1 = {"timeout": 50,
            "follow": False
        }
    data2 = {"timeout": 40,
            "follow": True
        }
    create_json_test_file(test_file1_path, data1)
    create_json_test_file(test_file2_path, data2)
    result = generate_diff(test_file1_path, test_file2_path)
    expected = """{
  - follow: false
  + follow: true
  - timeout: 50
  + timeout: 40
}"""
    assert result == expected

def test_diff_keys(temp_json_files):
    """Тестирование файлов, где отличаются ключи"""
    test_file1_path, test_file2_path = temp_json_files
    data1 = {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
    }
    data2 = {
        "host": "hexlet.io",
        "timeout": 30,
        "follow": False
    }
    create_json_test_file(test_file1_path, data1)
    create_json_test_file(test_file2_path, data2)
    result = generate_diff(test_file1_path, test_file2_path)
    expected = """{
  + follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 30
}"""
    assert result == expected

def test_empty_nonempty(temp_json_files):
    """Тестирование файлов, где один из файлов пустой"""
    test_file1_path, test_file2_path = temp_json_files
    data1 = {}
    data2 = {
        "host": "hexlet.io",
        "timeout": 30,
        "follow": False
    }
    create_json_test_file(test_file1_path, data1)
    create_json_test_file(test_file2_path, data2)
    result = generate_diff(test_file1_path, test_file2_path)
    expected = """{
  + follow: false
  + host: hexlet.io
  + timeout: 30
}"""
    assert result == expected

def test_empty_files(temp_json_files):
    """Тестирование файлов, где оба файла пустые"""
    test_file1_path, test_file2_path = temp_json_files
    data1 = {}
    data2 = {}
    create_json_test_file(test_file1_path, data1)
    create_json_test_file(test_file2_path, data2)
    result = generate_diff(test_file1_path, test_file2_path)
    expected = "{\n\n}"
    assert result == expected

def test_yaml_files():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f1:
        f1.write("""
        host: hexlet.io
        timeout: 50
        proxy: 123.234.53.22
        follow: false
        """)
        file1 = f1.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f2:
        f2.write("""
        host: hexlet.io
        timeout: 30
        follow: false
        """)
        file2 = f2.name
    
    try:
        result = generate_diff(file1, file2)
        assert 'timeout: 50' in result
        assert 'timeout: 30' in result
        assert 'proxy: 123.234.53.22' in result
        assert 'follow: false' in result
    finally:
        os.unlink(file1)
        os.unlink(file2)

def test_recursive_diff():

    result = generate_diff('file1.json', 'file2.json')

    assert "common: {" in result
    assert "group1: {" in result
    assert "group2: {" in result
    assert "setting1: Value 1" in result
    assert "setting2: 200" in result
    assert "setting3: true" in result
    assert "setting3: null" in result
    assert "doge: {" in result
    assert "wow: so much" in result