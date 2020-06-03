raise_exception_test_text_001 = '''
raise Exception
raise Exception()
raise Exception('exception message')
raise Exception from exc
raise Exception() from exc

try:
    raise Exception
    raise Exception()
except Exception as exception:
    raise Exception
    raise Exception()

    raise exception
    raise Exception from exception
    raise Exception() from exception

try:
    exception = Exception()
except:
    raise
    raise exception
    raise self.exception
'''
