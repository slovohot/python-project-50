
def diff_creator(old_dict, new_dict):
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

    diff = []
    keys = sorted(set(old_dict.keys()).union(new_dict.keys()))

    for key in keys:
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

        else:  # key in new_dict
            edits = {
                'status': 'added',
                'new_value': new_value
            }

        diff.append({'name': key, **edits})

    return diff
