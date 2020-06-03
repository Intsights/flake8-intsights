import tokenize

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
        for token in tokens:
            if token.type != tokenize.STRING:
                continue

            if token.string.startswith('"') or token.string.endswith('"'):
                yield from cls.error_yielder.yield_error(
                    error_id='I011',
                    line_number=token.start[0],
                    column_offset=token.start[1],
                )
