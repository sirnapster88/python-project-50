import tempfile
import pytest
import shutil
import json
import os
from gendiff.gendiff import generate_diff


def test_recursive_dif():
    result = generate_diff('tests/file1.json', 'tests/file2.json')

    assert "common: {" in result
    assert "group1: {" in result
    assert "group2: {" in result
    assert "setting1: Value 1" in result
    assert "setting2: 200" in result
    assert "setting3: true" in result
    assert "setting3: null" in result
    assert "doge: {" in result
    assert "wow: so much" in result
