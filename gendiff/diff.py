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
