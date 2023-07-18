import argparse
import json


def generate_diff(filepath1, filepath2):
    with open(filepath1) as file1:
        data1 = json.load(file1)
    with open(filepath2) as file2:
        data2 = json.load(file2)

    diff = []

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff.append(f'    {key}: {data1[key]}')
            else:
                diff.append(f'  - {key}: {data1[key]}')
                diff.append(f'  + {key}: {data2[key]}')
        elif key in data1:
            diff.append(f'  - {key}: {data1[key]}')
        elif key in data2:
            diff.append(f'  + {key}: {data2[key]}')

    return '{\n' + '\n'.join(diff) + '\n}'


def main():
    parser = argparse.ArgumentParser(description='Generate diff between two JSON files.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)

    parser.add_argument('-f', '--format', help="set format of output")

    args = parser.parse_args()
    file1_path = args.first_file
    file2_path = args.second_file

    diff = generate_diff(file1_path, file2_path)
    print(diff)


if __name__ == '__main__':
    main()

