duplications_test_text_001 = '''
class ClassOne:
    pass

class ClassTwo:
    pass
'''
duplications_test_text_002 = '''
class ClassOne:
    pass

class ClassOne:
    pass
'''
duplications_test_text_003 = '''
def function_one():
    pass

def function_two():
    pass
'''
duplications_test_text_004 = '''
def function_one():
    pass

def function_one():
    pass
'''
duplications_test_text_005 = '''
class ClassOne:
    def method_one():
        pass

    def method_two():
        pass
'''
duplications_test_text_006 = '''
class ClassOne:
    def method_one():
        pass

    def method_one():
        pass
'''
duplications_test_text_007 = '''
class ClassOne:
    @property
    def method_one():
        pass

    @method_one.setter
    def method_one():
        pass
'''
duplications_test_text_008 = '''
class ClassOne:
    @property
    def method_one():
        pass

    @method_one.setter
    def method_one():
        pass

    def method_one():
        pass
'''
duplications_test_text_009 = '''
class ClassOne:
    class SubClassOne:
        pass

    class SubClassTwo:
        pass
'''
duplications_test_text_010 = '''
class ClassOne:
    class SubClassOne:
        pass

    class SubClassOne:
        pass
'''
duplications_test_text_011 = '''
def function_one():
    def sub_function_one():
        pass

    def sub_function_two():
        pass
'''
duplications_test_text_012 = '''
def function_one():
    def sub_function_one():
        pass

    def sub_function_one():
        pass
'''
duplications_test_text_013 = '''
dict_one = {
    'key_1': 'value_1',
    'key_2': 'value_2',
}
'''
duplications_test_text_014 = '''
dict_one = {
    'key_1': 'value_1',
    'key_1': 'value_2',
}
'''
duplications_test_text_015 = '''
new_dict = {
    **dict_one,
    **dict_two,
}
'''
