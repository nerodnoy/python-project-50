import json
import yaml


def get_json_or_yaml(value):
    if isinstance(value, dict):
        return yaml.dump(value)
    elif isinstance(value, str):
        return json.dumps(value)[1:-1]
    return json.dumps(value)


def get_diff(data1, data2):
    diff = []

    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key not in data1:
            diff.append(f"  + {key}: {get_json_or_yaml(data2[key])}")
        elif key not in data2:
            diff.append(f"  - {key}: {get_json_or_yaml(data1[key])}")
        elif data1[key] == data2[key]:
            diff.append(f"    {key}: {get_json_or_yaml(data1[key])}")
        else:
            diff.append(f"  - {key}: {get_json_or_yaml(data1[key])}")
            diff.append(f"  + {key}: {get_json_or_yaml(data2[key])}")

    return "{\n" + "\n".join(diff) + "\n}"
