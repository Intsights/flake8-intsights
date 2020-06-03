import astroid
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
        for node in all_astroid_nodes:
            if isinstance(node, astroid.Call) and hasattr(node.func, 'attrname'):
                if node.func.attrname != 'format':
                    continue
                elif not isinstance(node.func.expr, astroid.Const):
                    continue
                elif node.func.expr.pytype() != 'builtins.str':
                    continue

                yield from cls.error_yielder.yield_error(
                    error_id='I098',
                    line_number=node.lineno,
                    column_offset=node.col_offset,
                )

        for index, token in enumerate(tokens):
            if token.type != tokenize.OP or token.string != '%':
                continue

            if index == 0:
                continue

            previous_token = tokens[index - 1]
            if previous_token.type == tokenize.STRING:
                yield from cls.error_yielder.yield_error(
                    error_id='I098',
                    line_number=token.start[0],
                    column_offset=token.start[1],
                )
