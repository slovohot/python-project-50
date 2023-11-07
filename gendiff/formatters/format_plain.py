from gendiff.logic.lower_bool import lower_bool


def create_string(value):
    if isinstance(value, str):
        return f"'{value}'"

    elif isinstance(value, dict):
        return '[complex value]'

    return lower_bool(value)


def generate_plain_diff(difference, parent=''):
    lines = []

    for item in difference:
        name = f"{parent}.{item['name']}" if parent else item['name']
        status = item['status']

        if status == 'nested':
            lines.extend(generate_plain_diff(item['nested'], name))

        elif status == 'removed':
            lines.append(f"Property '{name}' was {status}")

        elif status == 'added':
            new_value = create_string(item['new_value'])
            lines.append(
                f"Property '{name}' was {status} with value: {new_value}"
            )

        elif status == 'updated':
            old_value = create_string(item['old_value'])
            new_value = create_string(item['new_value'])
            lines.append(
                f"Property '{name}' was {status}. From {old_value} "
                f"to {new_value}"
            )

    return lines


def format_plain(diff):
    return '\n'.join(generate_plain_diff(diff))
