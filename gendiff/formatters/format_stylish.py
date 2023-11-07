from gendiff.logic.lower_bool import lower_bool


START_DEPTH = 0
STEP_DEPTH = 1
INDENT = '  '
INDENT_TO_DEPTH = '    '


def get_stepdepth_or_vallower(value, depth):
    if isinstance(value, dict) or isinstance(value, list):
        return create_format(value, depth + STEP_DEPTH)

    else:
        return lower_bool(value)


def create_line(diff, depth):
    key = diff.get('name')
    status = diff.get('status')
    indent = f'{INDENT}{INDENT_TO_DEPTH * depth}'

    if status == 'equal':
        value = get_stepdepth_or_vallower(diff.get('old_value'), depth)
        line = f'{indent}  {key}: {value}'

    elif status == 'nested':
        value = get_stepdepth_or_vallower(diff.get('nested'), depth)
        line = f'{indent}  {key}: {value}'

    elif status == 'added':
        value = get_stepdepth_or_vallower(diff.get('new_value'), depth)
        line = f'{indent}+ {key}: {value}'

    elif status == 'removed':
        value = get_stepdepth_or_vallower(diff.get('old_value'), depth)
        line = f'{indent}- {key}: {value}'

    else:  # status == 'updated':
        value_old = get_stepdepth_or_vallower(diff.get('old_value'), depth)
        value_new = get_stepdepth_or_vallower(diff.get('new_value'), depth)
        line = f'{indent}- {key}: {value_old}\n' \
               f'{indent}+ {key}: {value_new}'
    return line


def create_format(diff, depth):
    lines = ['{']

    for item in diff:
        if isinstance(item, dict):
            lines.append(create_line(item, depth))

        else:
            lines.append(create_line(
                {
                    'name': item,
                    'old_value': diff.get(item),
                    'status': 'equal'
                }, depth))

    lines.append(f"{INDENT_TO_DEPTH * depth}" + '}')

    return '\n'.join(lines)


def format_stylish(diff):
    return create_format(diff, START_DEPTH)
