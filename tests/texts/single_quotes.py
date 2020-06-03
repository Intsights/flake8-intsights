single_quotes_test_text_001 = '''
arg = 'test'
'''
single_quotes_test_text_002 = '''
arg = "test"
'''
single_quotes_test_text_003 = '''
function('test')
'''
single_quotes_test_text_004 = '''
function("test")
'''
single_quotes_test_text_005 = '''
function(
    arg='test',
)
'''
single_quotes_test_text_006 = '''
function(
    arg="test",
)
'''
single_quotes_test_text_007 = '''
def function(
    arg='test',
):
    pass
'''
single_quotes_test_text_008 = '''
def function(
    arg="test",
):
    pass
'''
single_quotes_test_text_009 = '''
def function(
    arg,
):
    \'\'\'
    \'\'\'
    pass
'''
single_quotes_test_text_010 = '''
def function(
    arg,
):
    """
    """
    pass
'''
single_quotes_test_text_011 = '''
tuple_arg = (
    'test',
)
'''
single_quotes_test_text_012 = '''
tuple_arg = (
    "test",
)
'''
single_quotes_test_text_013 = '''
dict_arg = {
    'key': 1,
}
'''
single_quotes_test_text_014 = '''
dict_arg = {
    "key": 1,
}
'''
single_quotes_test_text_015 = '''
dict_arg = {
    'key': '1',
}
'''
single_quotes_test_text_016 = '''
dict_arg = {
    "key": "1",
}
'''
