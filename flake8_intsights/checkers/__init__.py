from . import backslashes
from . import blank_lines
from . import builtins
from . import comments
from . import debugging
from . import declerations
from . import duplications
from . import imports
from . import indents
from . import mutables
from . import naming
from . import raise_exception
from . import single_quotes
from . import spacing
from . import string_interpolation

from . import _checker
from . import _errors


__checkers__ = [
    backslashes.Checker,
    blank_lines.Checker,
    builtins.Checker,
    comments.Checker,
    debugging.Checker,
    declerations.Checker,
    duplications.Checker,
    imports.Checker,
    indents.Checker,
    mutables.Checker,
    naming.Checker,
    raise_exception.Checker,
    single_quotes.Checker,
    spacing.Checker,
    string_interpolation.Checker,
]
