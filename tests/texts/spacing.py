spacing_test_text_001 = '''
def function():
    return 1
'''
spacing_test_text_002 = '''
def function():

    return 1
'''
spacing_test_text_003 = '''
def function():
    arg = 1

    return 1
'''
spacing_test_text_004 = '''
def function():
    arg = 1
    return 1
'''
spacing_test_text_005 = '''
def function():
    arr = [
        1,
    ]

    return 1
'''
spacing_test_text_006 = '''
def function():
    arr = [
        1,
    ]
    return 1
'''
spacing_test_text_007 = '''
def function():
    if True:
        return 1
'''
spacing_test_text_008 = '''
def function():
    if True:

        return 1
'''
spacing_test_text_009 = '''
def function():
    while True:
        return 1
'''
spacing_test_text_010 = '''
def function():
    while True:

        return 1
'''
spacing_test_text_011 = '''
def function():
    if True:
        return 1
    else:
        return 2
'''
spacing_test_text_012 = '''
def function():
    if True:
        return 1
    else:

        return 2
'''
spacing_test_text_013 = '''
def function():
    if True:
        arg = 1

        return 1
'''
spacing_test_text_014 = '''
def function():
    if True:
        arg = 1
        return 1
'''
spacing_test_text_015 = '''
def function():
    try:
        arg = 10

        return 3
    except:
        return 4
'''
spacing_test_text_016 = '''
def function():
    try:
        arg = 10
        return 3
    except:
        return 4
'''
spacing_test_text_017 = '''
def function():
    try:
        return 3
    except:
        return 4
'''
spacing_test_text_018 = '''
def function():
    try:

        return 3
    except:
        return 4
'''
spacing_test_text_019 = '''
def function():
    try:
        return 3
    except:
        arg = 1

        return 4
'''
spacing_test_text_020 = '''
def function():
    try:
        return 3
    except:
        arg = 1
        return 4
'''
spacing_test_text_021 = '''
def function():
    try:
        return 3
    except:
        return 4
    finally:
        return 3
'''
spacing_test_text_022 = '''
def function():
    try:
        return 3
    except:

        return 4
'''
spacing_test_text_023 = '''
def function():
    if True:
        pass

    return 1
'''
spacing_test_text_024 = '''
def function():
    if True:
        pass
    return 1
'''
spacing_test_text_025 = '''
def function():
    """
    """
    return 1
'''
spacing_test_text_026 = '''
def function():
    """
    """

    return 1
'''
spacing_test_text_027 = '''
def function():
    """
    """
    arg = 1

    return 1
'''
spacing_test_text_028 = '''
def function():
    """
    """
    arg = 1
    return 1
'''
spacing_test_text_029 = '''
def function():
    arg = func(
        1,
    )

    return 1
'''
spacing_test_text_030 = '''
def function():
    arg = func(
        1,
    )
    return 1
'''
spacing_test_text_031 = '''
def function():
    arg = (
        1,
    )

    return 1
'''
spacing_test_text_032 = '''
def function():
    arg = (
        1,
    )
    return 1
'''
spacing_test_text_033 = '''
def function():
    yield (
        1,
    )

    return 1
'''
spacing_test_text_034 = '''
def function():
    yield (
        1,
    )
    return 1
'''
spacing_test_text_035 = '''
def function():
    arg = 1

    yield 1
'''
spacing_test_text_036 = '''
def function():
    arg = 1
    yield 1
'''
spacing_test_text_037 = '''
def function():
    arg = 1

    yield from test()
'''
spacing_test_text_038 = '''
def function():
    arg = 1
    yield from test()
'''
spacing_test_text_039 = '''
def function():
    yield from test()
'''
spacing_test_text_040 = '''
def function():

    yield from test()
'''
spacing_test_text_041 = '''
def function():
    yield 1
'''
spacing_test_text_042 = '''
def function():

    yield 1
'''
spacing_test_text_043 = '''
def function():
    if True:
        yield 1
'''
spacing_test_text_044 = '''
def function():
    if True:

        yield 1
'''
spacing_test_text_045 = '''
def function():
    if True:
        yield from 1
'''
spacing_test_text_046 = '''
def function():
    if True:

        yield from 1
'''
spacing_test_text_047 = '''
def function():
    if True:
        yield 1
    else:
        yield 1
'''
spacing_test_text_048 = '''
def function():
    if True:
        yield 1
    else:

        yield 1
'''
spacing_test_text_049 = '''
def function():
    if True:
        yield from 1
    else:
        yield from 1
'''
spacing_test_text_050 = '''
def function():
    if True:
        yield from 1
    else:

        yield from 1
'''
spacing_test_text_051 = '''
def function(
    a,
    b,
):
    yield from 1
'''
spacing_test_text_052 = '''
def function(
    a,
    b,
):

    yield from 1
'''
spacing_test_text_053 = '''
def function(
    a,
    b,
):
    """
    """
    yield from 1
'''
spacing_test_text_054 = '''
def function(
    a,
    b,
):
    """
    """

    yield from 1
'''
spacing_test_text_055 = '''
def function():
    if (
        a == 2
    ):
        yield from 1
'''
spacing_test_text_056 = '''
def function():
    if (
        a == 2
    ):

        yield from 1
'''
spacing_test_text_057 = '''
def function():
    if a == 2:
        yield 1

        a = 2
'''
spacing_test_text_058 = '''
def function():
    if a == 2:
        yield 1
        a = 2
'''
spacing_test_text_059 = '''
def function():
    if (
        a == 2
    ):
        yield 1

        a = 2
'''
spacing_test_text_060 = '''
def function():
    if (
        a == 2
    ):
        yield 1
        a = 2
'''
spacing_test_text_061 = '''
def function():
    if a == 2:
        yield 1

    a = 2
'''
spacing_test_text_062 = '''
def function():
    if a == 2:
        yield 1
    a = 2
'''
spacing_test_text_063 = '''
def function():
    if (
        a == 2
    ):
        yield 1

    a = 2
'''
spacing_test_text_064 = '''
def function():
    if (
        a == 2
    ):
        yield 1
    a = 2
'''
spacing_test_text_065 = '''
def function():
    if a == 2:
        yield from (
            1,
            2,
        )

        a = 2
'''
spacing_test_text_066 = '''
def function():
    if a == 2:
        yield from (
            1,
            2,
        )
        a = 2
'''
spacing_test_text_067 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )

        a = 2
'''
spacing_test_text_068 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )
        a = 2
'''
spacing_test_text_069 = '''
def function():
    if a == 2:
        yield from (
            1,
            2,
        )

    a = 2
'''
spacing_test_text_070 = '''
def function():
    if a == 2:
        yield from (
            1,
            2,
        )
    a = 2
'''
spacing_test_text_071 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )

    a = 2
'''
spacing_test_text_072 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )
    a = 2
'''
spacing_test_text_073 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )
    elif a == 1:
        return 3
'''
spacing_test_text_074 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )

    elif a == 1:
        return 3
'''
spacing_test_text_075 = '''
def function():
    if (
        a == 2
    ):
        yield 1
    elif a == 1:
        return 3
'''
spacing_test_text_076 = '''
def function():
    if (
        a == 2
    ):
        yield 1

    elif a == 1:
        return 3
'''
spacing_test_text_077 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )
    elif (
        a == 1
    ):
        return 3
'''
spacing_test_text_078 = '''
def function():
    if (
        a == 2
    ):
        yield from (
            1,
            2,
        )

    elif (
        a == 1
    ):
        return 3
'''
spacing_test_text_079 = '''
def function():
    if (
        a == 2
    ):
        yield 1
    elif (
        a == 1
    ):
        return 3
'''
spacing_test_text_080 = '''
def function():
    if (
        a == 2
    ):
        yield 1

    elif (
        a == 1
    ):
        return 3
'''
spacing_test_text_081 = '''
def function():
    return 3


def function_2():
    pass
'''
spacing_test_text_081 = '''
def function():
    return 3


def function_2():
    pass
'''
spacing_test_text_082 = '''
def function():
    if True:
        return

    try:
        pass
    except:
        pass
    finally:
        pass
'''
spacing_test_text_083 = '''
def function():
    if True:
        return

    try:
        pass
    except:
        pass
    finally:

        pass
'''
spacing_test_text_084 = '''
if True:
    pass

else:
    pass
'''
spacing_test_text_085 = '''
try:
    pass

except:
    pass
'''
spacing_test_text_086 = '''
try:
    pass

finally:
    pass
'''
spacing_test_text_087 = '''
class A:
    pass
'''
spacing_test_text_088 = '''
class A:

    pass
'''
spacing_test_text_089 = '''
class A(
    B,
):
    pass
'''
spacing_test_text_090 = '''
class A(
    B,
):

    pass
'''
spacing_test_text_091 = '''
class A:
    """
    """
    pass
'''
spacing_test_text_092 = '''
class A:

    """
    """
    pass
'''
spacing_test_text_093 = '''
class A(
    B,
):
    """
    """
    pass
'''
spacing_test_text_094 = '''
class A(
    B,
):

    """
    """
    pass
'''
spacing_test_text_095 = '''
def function():
    \'\'\'
        Example:

        test
    \'\'\'
    return value
'''
spacing_test_text_096 = '''
raise Exception(
    msg=f'({10})',
)

return SomeObject(
    param=f'\\'{object.attr}\\'',
)
'''
