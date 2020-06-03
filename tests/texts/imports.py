imports_test_text_001 = '''
import module1
'''
imports_test_text_002 = '''
import module1.submodule1
'''
imports_test_text_003 = '''
from . import module1
'''
imports_test_text_004 = '''
from .. import module1
'''
imports_test_text_005 = '''
import module1

from . import module2
'''
imports_test_text_006 = '''
import module1
import module2

from . import module3
'''
imports_test_text_007 = '''
import module1

from . import module2
from . import module3
'''
imports_test_text_008 = '''
import module1
import module2

from . import module3
from . import module4
'''
imports_test_text_009 = '''
import module1
import module2

from . import module3
from . import module4
'''
imports_test_text_010 = '''
import module1.submodule1 as alias1
'''
imports_test_text_011 = '''
import module1 as alias1
'''
imports_test_text_012 = '''
import module1, module2
'''
imports_test_text_013 = '''
import module1.submodule1, module2
'''
imports_test_text_014 = '''
from module1 import submodule1
'''
imports_test_text_015 = '''
from module1 import submodule1 as alias1
'''
imports_test_text_016 = '''
from module1 import *
'''
imports_test_text_017 = '''
from module1 import module1, module2
'''
imports_test_text_018 = '''
from .module1 import module1
'''
imports_test_text_019 = '''
from .module1 import module1, module2
'''
imports_test_text_020 = '''
from ..module1 import module1
'''
imports_test_text_021 = '''
from ..module1 import module1, module2
'''
imports_test_text_022 = '''
from . import module1 as alias1
'''
imports_test_text_023 = '''
from .module1 import *
'''
imports_test_text_024 = '''
import module1
from . import module2
'''
imports_test_text_025 = '''
from . import module2
import module1
'''
imports_test_text_026 = '''
import module
'''
imports_test_text_027 = '''
import module

'''
imports_test_text_028 = '''
import module


param = 1
'''
imports_test_text_029 = '''
import module

param = 1
'''
imports_test_text_030 = '''
import module
param = 1
'''
