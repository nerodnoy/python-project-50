import json


def load_json_data(filepath):
    with open(filepath) as file:
        data = json.load(file)
    return data


def generate_diff(filepath1, filepath2):
    data1 = load_json_data(filepath1)
    data2 = load_json_data(filepath2)

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
