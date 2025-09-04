def format_plain(diff, path=''):
    lines = []

    for node in diff:
        current_path = f"{path}.{node['key']}" if path else node['key']

        if node['type'] == 'nested':
            nested_result = format_plain(node['children'], current_path)
            if nested_result:
                lines.append(nested_result)
        
        elif node['type'] == 'added':
            value = format_value_plain(node['value'])
            lines.append(f"Property {current_path} was added with value: {value}")

        elif node['type'] == 'removed':
            lines.append(f"Property {current_path} was removed")

        elif node['type'] == 'updated':
            old_value = format_value_plain(node['old_value'])
            new_value = format_value_plain(node['new_value'])
            lines.append(f"Property {current_path} was updated. From {old_value} to {new_value}")

    return "\n".join([line for line in lines if line])


def format_value_plain(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)
    

