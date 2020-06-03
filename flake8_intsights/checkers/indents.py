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
        yield from cls.check_only_spaces_indents(
            tokens=tokens,
        )

        yield from cls.check_indentations_gradually(
            lines=lines,
            tokens=tokens,
        )

    @classmethod
    def check_only_spaces_indents(
        cls,
        tokens,
    ):
        for token in tokens:
            token_type_is_indent = token.type == tokenize.INDENT
            if not token_type_is_indent:
                continue

            number_of_tabs = token.string.count('\t')
            if number_of_tabs > 0:
                yield from cls.error_yielder.yield_error(
                    error_id='I003',
                    line_number=token.start[0],
                    column_offset=0,
                )

            number_of_spaces = token.string.count(' ')
            spaces_are_not_in_four = number_of_spaces % 4 != 0
            if spaces_are_not_in_four:
                yield from cls.error_yielder.yield_error(
                    error_id='I004',
                    line_number=token.start[0],
                    column_offset=0,
                )

    @classmethod
    def check_indentations_gradually(
        cls,
        lines,
        tokens,
    ):
        previous_indenation_level = 0

        for line_number, line in enumerate(lines, 1):
            if line.strip() == '':
                continue

            current_indenation_level = cls.get_line_indentation_level(
                line=line,
            )
            tokens_indented_ungradually = (current_indenation_level - previous_indenation_level) > 1
            if tokens_indented_ungradually:
                col_offset = len(line) - len(line.lstrip())
                current_token = cls.get_token_by_position(
                    lineno=line_number,
                    col_offset=col_offset,
                    tokens=tokens,
                )
                current_token_is_string = current_token.type == tokenize.STRING

                if not current_token_is_string:
                    yield from cls.error_yielder.yield_error(
                        error_id='I006',
                        line_number=line_number,
                        column_offset=0,
                    )

            previous_indenation_level = current_indenation_level
