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
        for lineno, line in enumerate(lines, 1):
            if line.endswith('\\') and not line.endswith('\\\\'):
                yield from cls.error_yielder.yield_error(
                    error_id='I093',
                    line_number=lineno,
                    column_offset=len(line),
                )
