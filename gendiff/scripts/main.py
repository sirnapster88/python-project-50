import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        usage='gendiff [-h] first_file second_file')

    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')

    args = parser.parse_args()
    print(f"Comparing {args.first_file} with {args.second_file}")

if __name__ == '__main__':
    main()