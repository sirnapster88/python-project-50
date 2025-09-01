import json
import yaml

def load_files(file_path):
    """Функция осуществляющая чтение и парсинг файлов"""
    with open(file_path) as f:
        data = f.read()
    
    if file_path.endswith('.json'):
        return parse_json(data)
    elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
        return parse_yaml(data)
    
def parse_json(data):
    return json.loads(data)

def parse_yaml(data):
    return yaml.safe_load(data)
