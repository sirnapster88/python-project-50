def format_stylish(diff, depth=0):
    lines = []
    indent = '    ' * depth

    for node in diff:
        key = node['key']
        type_ = node['type']

        if type_ == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}    }}")
        
        if type_ == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")

        if type_ == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")

        if type_ == 'updated':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")

        if type_ == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        
    if depth == 0:
        return "{\n" + "\n".join(lines) + "\n}"
    else:
        return "\n".join(lines)
    
def format_value(value, depth):
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = ['{']
        for k,v in value.items():
            formatted_value = format_value(v, depth + 1)
            lines.append(f"{indent}    {k}: {formatted_value}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)
