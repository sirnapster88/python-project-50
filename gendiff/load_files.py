import json
import yaml
from pathlib import Path

def load_files(file_path):
    """Функция осуществляющая чтение и парсинг файлов"""
    file_path = Path(file_path) 
    with open(file_path, 'r') as f:
        data = f.read()
    
    if file_path.suffix == '.json':
        return parse_json(data)
    elif file_path.suffix == '.yaml' or file_path.suffix == '.yml':
        return parse_yaml(data)
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")
    
def parse_json(data):
    return json.loads(data)

def parse_yaml(data):
    return yaml.safe_load(data)
