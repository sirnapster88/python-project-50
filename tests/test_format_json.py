import json
from gendiff.scripts.formatters.json import format_json


def test_format_json():
    diff = [
        {
            'key': 'common',
            'type': 'nested',
            'children':[
                {'key': 'setting1', 'type': 'unchanged', 'value': 'Value1'},
                {'key': 'setting2', 'type':'removed', 'value': '200'},
                {'key': 'setting3', 'type':'updated', 'old_value': True, 'new_value': None}
            ]
        }
    ]
    result = format_json(diff)

    parsed_result= json.loads(result)

    assert isinstance(parsed_result, list)
    assert len(parsed_result) == 1
    assert parsed_result[0]['key'] == 'common'
    assert parsed_result[0]['type'] == 'nested'