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
        yield from cls.check_no_inline_comments(
            tokens=tokens,
        )

    @classmethod
    def check_no_inline_comments(
        cls,
        tokens,
    ):
        for token in tokens:
            token_type_is_comment = token.type == tokenize.COMMENT
            if token_type_is_comment:
                yield from cls.error_yielder.yield_error(
                    error_id='I005',
                    line_number=token.start[0],
                    column_offset=token.start[1],
                )
