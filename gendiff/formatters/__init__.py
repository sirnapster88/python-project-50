from .json import format_json
from .plain import format_plain
from .stylish import format_stylish

def get_formatter(format_name):
    formatters = {
        'stylish': format_stylish,
        'plain': format_plain,
        'json': format_json
    }
    return formatters[format_name]


__all__ = ['get_formatter','format_stylish', 'format_plain', 'format_json']
