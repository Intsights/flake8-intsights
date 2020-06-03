import astroid

from . import _checker


class Checker(
    _checker.BaseChecker,
):
    DEBUG_MODULES = {
        'pdb',
        'ipdb',
        'pudb',
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
            if isinstance(node, astroid.Call):
                if isinstance(node.func, astroid.Name) and node.func.name == 'breakpoint':
                    yield from cls.error_yielder.yield_error(
                        error_id='I092',
                        line_number=node.lineno,
                        column_offset=node.col_offset,
                    )
            elif isinstance(node, astroid.Import):
                for import_name, import_as in node.names:
                    if import_name in cls.DEBUG_MODULES:
                        yield from cls.error_yielder.yield_error(
                            error_id='I092',
                            line_number=node.lineno,
                            column_offset=node.col_offset,
                        )
