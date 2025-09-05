from gendiff.scripts.formatters.plain import format_value_plain, format_plain


def test_format_value_plain():
    assert format_value_plain("text") == "'text'"
    assert format_value_plain(123) == "123"
    assert format_value_plain(True) == "true"
    assert format_value_plain({'a':1}) == "[complex value]"


def test_format_plain():
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
    result = format_plain(diff)
    assert "Property 'common.setting2' was removed" in result
    assert "Property 'common.setting3' was updated. From true to null" in result