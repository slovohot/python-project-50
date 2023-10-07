def generate_diff(f1, f2):
    res = []
    f1_keys = sorted(f1.keys())
    f2_keys = sorted(f2.keys())

    for key in f1_keys:
        value1 = f1[key]
        value2 = f2.get(key)
        if key not in f2:
            res.append(f'- {key}: {value1}')
        elif value1 == value2:
            res.append(f'  {key}: {value1}')
        else:
            res.append(f'- {key}: {value1}')
            res.append(f'+ {key}: {value2}')

    for key in f2_keys:
        if key not in f1:
            res.append(f'+ {key}: {f2[key]}')

    return '{\n' + '\n'.join(res) + '\n'
