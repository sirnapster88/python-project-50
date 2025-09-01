from gendiff.scripts.load_files import load_files

def find_difference(dict1,dict2):
    """Функция осуществляющая поиск различий в двух плоских файлах"""
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = []

    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict2:
            result.append(f"  - {key}: {value1}")
        elif key not in dict1:
            result.append(f"  + {key}: {value2}")
        elif value1 != value2:
            result.append(f"  - {key}: {value1}")
            result.append(f"  + {key}: {value2}")
        else:
            result.append(f"    {key}: {value1}")

    return "{\n" + "\n".join(result) + "\n}"

def generate_diff(file1_path, file2_path):
    """Функция выполняющая загрузку данных из файлов и выполняет сравнение"""
    data1 = load_files(file1_path)
    data2 = load_files(file2_path)
    diff = find_difference(data1, data2)
    return diff