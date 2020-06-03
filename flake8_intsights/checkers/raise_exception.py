import astroid
import builtins

from . import _checker


class Checker(
    _checker.BaseChecker,
):
    @classmethod
    def check(
        cls,
        filename,
        lines,
        tokens,
        start_position_to_token,
        ast_tree,
        astroid_tree,
        all_astroid_nodes,
    ):
        for node in all_astroid_nodes:
            if not isinstance(node, astroid.Raise):
                continue

            if not node.exc or isinstance(node.exc, astroid.Call):
                continue

            if isinstance(node.exc, astroid.Name):
                builtin_exception_object = hasattr(builtins, node.exc.name)
                if builtin_exception_object:
                    yield from cls.error_yielder.yield_error(
                        error_id='I099',
                        line_number=node.exc.lineno,
                        column_offset=node.exc.col_offset,
                    )
