import json
import yaml


def serialize_value(value):
    if isinstance(value, dict):
        return yaml.dump(value)
    elif isinstance(value, str):
        return json.dumps(value)[1:-1]  # removed quotes here :( ???
    return json.dumps(value)


def get_diff(data1, data2):
    diff = []

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key not in data1:
            diff.append(f"  + {key}: {serialize_value(data2[key])}")
        elif key not in data2:
            diff.append(f"  - {key}: {serialize_value(data1[key])}")
        elif data1[key] == data2[key]:
            diff.append(f"    {key}: {serialize_value(data1[key])}")
        else:
            diff.append(f"  - {key}: {serialize_value(data1[key])}")
            diff.append(f"  + {key}: {serialize_value(data2[key])}")

    return '{\n' + '\n'.join(diff) + '\n}'
