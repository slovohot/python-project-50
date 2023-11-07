
def diff_creator(old_dict, new_dict):
    diff = []
    keys = sorted(list(set(old_dict.keys()).union(new_dict.keys())))

    for key in keys:
        res = {'name': key}
        res.update(create_edits(old_dict, new_dict, key))
        diff.append(res)

    return diff


def create_edits(old_dict, new_dict, key):
    old_value = old_dict.get(key)
    new_value = new_dict.get(key)

    if old_value == new_value:
        edits = {
            'status': 'equal',
            'old_value': old_value
        }

    elif key in old_dict and key in new_dict:
        edits = create_nested_updated(old_value, new_value)

    elif key in old_dict:
        edits = {
            'status': 'removed',
            'old_value': old_value
        }

    else:  # key in new_dict:
        edits = {
            'status': 'added',
            'new_value': new_value
        }

    return edits


def create_nested_updated(old_value, new_value):
    if isinstance(old_value, dict) and isinstance(new_value, dict):
        return {
            'status': 'nested',
            'nested': diff_creator(old_value, new_value)
        }
    else:
        return {
            'status': 'updated',
            'old_value': old_value,
            'new_value': new_value
        }
