import os
import yaml
import shutil
import tempfile
import pytest
from pathlib import Path
from gendiff.scripts.differ import generate_diff


def test_yaml_files():
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml') as f1:
        f1.write("""
        host: hexlet.io
        timeout: 50
        proxy: 123.234.53.22
        follow: False
        """)
        file1 = f1.name
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f2:
        f2.write("""
        host: hexlet.io
        timeout: 30
        follow: False
        """)
        file2 = f2.name
    
    try:
        result = generate_diff(file1, file2)
        assert 'timeout: 50' in result
        assert 'timeout: 30' in result
        assert 'proxy: 123.234.53.22' in result
        assert 'follow: False' in result
    finally:
        os.unlink(file1)
        os.unlink(file2)

