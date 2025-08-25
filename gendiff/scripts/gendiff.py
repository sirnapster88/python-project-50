import argparse, json
from pathlib import Path


def load_files(file1_path, file2_path):
    """Функция осуществляющая чтение и парсинг файлов"""
    file1_path = 'file1.json'
    file2_path = 'file2.json'
    with open(file1_path) as f1:
        data1 = json.load(f1)
    with open(file2_path) as f2:
        data2 = json.load(f2)
    return data1, data2

def generate_diff(dict1, dict2):
    """Функция осуществляющая поиск различий в двух плоских файлах"""
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    result = []

    for key in all_keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if key not in dict2:
            result.append(f"    - {key}: {value1}")
        elif key not in dict2:
            result.append(f"    + {key}: {value2}")
        elif value1 != value2:
            result.append(f"    - {key}: {value1}")
            result.append(f"    + {key}: {value2}")
        else:
            result.append(f"      {key}: {value1}")

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

    file1_data, file2_data= load_files(args.first_file, args.second_file)
    print(f"{args.first_file}:")
    print(json.dumps(file1_data))
    print(f"{args.second_file}:")
    print(json.dumps(file2_data))

    diff = generate_diff(file1_data, file2_data)
    print('Difference:')
    print(diff)
    

if __name__ == '__main__':
    main()