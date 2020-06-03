import astroid

from . import _checker


class Checker(
    _checker.BaseChecker,
):
    MUTABLE_LITERALS = (
        astroid.Dict,
        astroid.List,
        astroid.Set,
        astroid.Tuple,
    )
    MUTABLE_CALLS = {
        'Counter',
        'OrderedDict',
        'collections.Counter',
        'collections.OrderedDict',
        'collections.defaultdict',
        'collections.deque',
        'defaultdict',
        'deque',
        'dict',
        'list',
        'set',
        'tuple',
    }

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
            if not isinstance(node, astroid.FunctionDef):
                continue

            for default in node.args.defaults + node.args.kw_defaults:
                if isinstance(default, cls.MUTABLE_LITERALS):
                    yield from cls.error_yielder.yield_error(
                        error_id='I081',
                        line_number=default.lineno,
                        column_offset=default.col_offset,
                    )
                elif isinstance(default, astroid.Call):
                    if default.func.as_string() in cls.MUTABLE_CALLS:
                        yield from cls.error_yielder.yield_error(
                            error_id='I081',
                            line_number=default.lineno,
                            column_offset=default.col_offset,
                        )
