naming_test_text_001 = '''
def function_one():
    pass

def function_two(arg):
    pass

def function_three(self):
    pass

def function_four(cls):
    pass

class Test:
    def method_1():
        pass

    def method_2(arg):
        pass

    def method_3(self):
        pass

    def method_4(cls):
        pass

    @classmethod
    def method_5():
        pass

    @classmethod
    def method_6(arg):
        pass

    @classmethod
    def method_7(cls):
        pass

    @classmethod
    def method_8(self):
        pass

    @staticmethod
    def method_9():
        pass

    @staticmethod
    def method_10(arg):
        pass

    @staticmethod
    def method_11(cls):
        pass

    @staticmethod
    def method_12(self):
        pass

def function_five(Argumemnt):
    pass
'''
naming_test_text_002 = '''
class Some:
    pass

class some:
    pass

class Some_class:
    pass

class ModuleTestCase(
    unittest.TestCase,
):
    pass

class TestCase(
    unittest.TestCase,
):
    pass

class Module(
    unittest.TestCase,
):
    pass
'''
