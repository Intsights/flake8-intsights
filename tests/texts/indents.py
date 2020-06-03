indents_test_text_001 = '''
def func():
    pass
'''
indents_test_text_002 = '''
def func():
  pass
'''
indents_test_text_003 = '''
def func():
\tpass
'''
indents_test_text_004 = '''
if True:
    pass
'''
indents_test_text_005 = '''
if True:
        pass
'''
indents_test_text_006 = '''
if True:
            pass
'''
indents_test_text_007 = '''
if True:
    if True:
        if True:
                pass
'''
indents_test_text_008 = '''
if True:
    if True:
            if True:
                pass
'''
indents_test_text_009 = '''
[
    1,
    2,
]
'''
indents_test_text_010 = '''
[
    1,
        2,
]
'''
indents_test_text_011 = '''
[
    1,
            2,
]
'''
indents_test_text_012 = '''
if True:
    if True:
        if True:
            pass

param = 1
'''
indents_test_text_013 = '''
long_string = \'\'\'
    good line
\'\'\'
'''
indents_test_text_014 = '''
long_string = \'\'\'
    good line
            good line
\'\'\'
'''
indents_test_text_015 = '''
raise Exception(
    'a'.join(
        lines,
    )
)
'''
