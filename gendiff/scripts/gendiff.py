import argparse, json
from pathlib import Path


def load_files(file1_name, file2_name):
    project_root = Path(__file__).parent.parent
    file1_path = project_root / file1_name
    file2_path = project_root / file2_name
    with open(file1_path) as f1:
        data1 = json.load(f1)
    with open(file2_path) as f2:
        data2 = json.load(f2)
    return data1, data2


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
    
    

if __name__ == '__main__':
    main()