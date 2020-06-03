string_interpolation_test_text_001 = '''
var_one = ''
var_one = 'string'.format()
var_one = 'string{}'.format(1)
var_one = 'string{arg}'.format(arg=1)
var_one = f'string{arg}'
var_one = f'string'

def function():
    return 'string{arg}'.format(arg=1)

def function():
    return f'string{arg}'

var_one = 'string' % ()
var_one = 'string %s' % (1,)
'''
