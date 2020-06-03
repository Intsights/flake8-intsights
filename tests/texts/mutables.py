mutables_test_text_001 = '''
def function(
    param,
):
    pass
'''
mutables_test_text_002 = '''
def function(
    param=0,
):
    pass
'''
mutables_test_text_003 = '''
def function(
    param={},
):
    pass
'''
mutables_test_text_004 = '''
def function(
    param=[],
):
    pass
'''
mutables_test_text_005 = '''
def function(
    param=tuple(),
):
    pass
'''
mutables_test_text_006 = '''
def function(
    param=list(),
):
    pass
'''
mutables_test_text_007 = '''
def function(
    param_one,
    param_two,
):
    pass
'''
mutables_test_text_008 = '''
def function(
    param_one,
    param_two=0,
):
    pass
'''
mutables_test_text_009 = '''
def function(
    param_one,
    param_two={},
):
    pass
'''
mutables_test_text_010 = '''
def function(
    param_one,
    param_two=[],
):
    pass
'''
mutables_test_text_011 = '''
def function(
    param_one,
    param_two=list(),
):
    pass
'''
mutables_test_text_012 = '''
def function(
    param_one,
    param_two=tuple(),
):
    pass
'''
mutables_test_text_013 = '''
def function(
    param_one,
    param_two,
    param_three,
):
    pass
'''
mutables_test_text_014 = '''
def function(
    param_one,
    param_two,
    param_three=0,
):
    pass
'''
mutables_test_text_015 = '''
def function(
    param_one,
    param_two=0,
    param_three={},
):
    pass
'''
mutables_test_text_016 = '''
def function(
    param_one,
    param_two=[],
    param_three={},
):
    pass
'''
mutables_test_text_017 = '''
def function(
    param_one={},
    param_two=0,
    param_three={},
):
    pass
'''
mutables_test_text_018 = '''
def function(
    param_one=0,
    param_two=[],
    param_three=0,
):
    pass
'''
