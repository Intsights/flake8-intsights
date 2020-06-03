builtins_test_text_001 = '''
arg = 10
int = 10
'''
builtins_test_text_002 = '''
def function_one():
    pass

def function_two(
    arg,
):
    pass

def function_three(
    int,
):
    pass

async def function_four():
    pass

async def function_five(
    arg,
):
    pass

async def function_six(
    int,
):
    pass

def int():
    pass
'''
builtins_test_text_003 = '''
for i in range(10):
    pass

for int in range(10):
    pass

for a, b in range(10):
    pass

for a, int in range(10):
    pass

for *a, b in [[1,2,3]]:
    pass

for *int, b in [[1,2,3]]:
    pass
'''
builtins_test_text_004 = '''
with func():
    pass

with func() as var:
    pass

with func() as int:
    pass

with func_one() as var_one, func_two() as var_two:
    pass

with func_one() as int, func_two() as var_two:
    pass

with func_one() as var_one, func_two() as int:
    pass

with func() as (var_one, var_two):
    pass

with func() as (var_one, int):
    pass

with func() as (*var_one, *var_two):
    pass

with func() as (*var_one, *int):
    pass
'''
builtins_test_text_005 = '''
var = [
    var_one
    for var_one in var_list
]
var = [
    int
    for int in var_list
]
var = [
    (var_one, var_two)
    for (var_one, var_two) in var_list
]
var = [
    (var_one, int)
    for (var_one, int) in var_list
]
'''
builtins_test_text_006 = '''
class ClassName:
    pass

class dict:
    pass
'''
