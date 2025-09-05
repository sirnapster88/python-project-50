from gendiff.load_files import load_files
from gendiff.scripts.formatters.stylish import format_stylish
from gendiff.scripts.formatters.plain import format_plain
from gendiff.scripts.formatters.json import format_json

def find_difference(dict1,dict2):
    """Функция осуществляющая логику сравнения"""
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = []

    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict2:
            result.append({'key': key, 
                           'type': 'removed', 
                           'value': value1})
        elif key not in dict1:
            result.append({'key': key,
                           'type': 'added',
                           'value': value2})
        elif isinstance(value1, dict) and isinstance(value2, dict):
            children = find_difference(value1, value2)
            result.append({
                'key': key,
                'type': 'nested',
                'children': children})
        elif value1 != value2:
            result.append({'key': key,
                           'type': 'updated',
                           'old_value': value1,
                           'new_value': value2})
        else:
            result.append({'key': key,
                           'type': 'unchanged',
                           'value': value1})
    return result

def generate_diff(file1_path, file2_path, format_name = 'stylish'):
    """Функция выполняющая основное сравнение"""
    data1 = load_files(file1_path)
    data2 = load_files(file2_path)
    diff = find_difference(data1, data2)
    
    if format_name == 'stylish':
        return format_stylish(diff)
    if format_name == 'plain':
        return format_plain(diff)
    if format_name == 'json':
        return format_json(diff)