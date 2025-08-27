import argparse
import json


def load_files(file_path):
    """Функция осуществляющая чтение и парсинг файлов"""
    with open(file_path) as f:
        data = json.load(f)
    return data


def generate_diff(file1_path, file2_path):
    """Функция выполняющая сравнение"""
    data1 = load_files(file1_path)
    data2 = load_files(file2_path)
    
    # print(f"file1_data:")
    # print(json.dumps(data1))
    # print(f"file2_data:")
    # print(json.dumps(data2))
    
    diff = find_difference(data1, data2)
    return diff


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

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] [-f FORMAT] first_file second_file')

    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(f"Comparing {args.first_file} with {args.second_file}")
    if args.format:
        print(f"Output format{args.format}")

    result = generate_diff(args.first_file, args.second_file)
    print(result)
    

if __name__ == '__main__':
    main()