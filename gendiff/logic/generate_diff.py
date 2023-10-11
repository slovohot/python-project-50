import json


# accept json and returns a dict
def get_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data


def generate_diff(file_path1, file_path2):
    res = []

    # returns a dict for futher processing
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    # saves dict keys
    data1_keys = sorted(data1.keys())
    data2_keys = sorted(data2.keys())

    for key in data1_keys:
        value1 = data1[key]
        value2 = data2.get(key)
        if key not in data2:
            res.append(f'- {key}: {value1}'.lower())

        elif value1 == value2:
            res.append(f'  {key}: {value1}'.lower())

        else:
            res.append(f'- {key}: {value1}'.lower())
            res.append(f'+ {key}: {value2}'.lower())

    for key in data2_keys:
        if key not in data1:
            res.append(f'+ {key}: {data2[key]}'.lower())

    return '{\n' + '\n'.join(res) + '\n}'
