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
        yield from cls.check_blank_lines_from_bottom(
            lines=lines,
        )

        yield from cls.check_blank_lines_from_top(
            lines=lines,
        )

    @classmethod
    def check_blank_lines_from_bottom(
        cls,
        lines,
    ):
        if not lines:
            return
        elif len(lines) == 1:
            if lines[0] != '':
                yield from cls.error_yielder.yield_error(
                    error_id='I001',
                    line_number=len(lines),
                    column_offset=0,
                )
        else:
            last_line_is_blank = lines[-1].strip() == ''
            previous_to_last_line_is_not_blank = lines[-2].strip() != ''
            one_blank_line_at_the_end = last_line_is_blank and previous_to_last_line_is_not_blank

            if not one_blank_line_at_the_end:
                yield from cls.error_yielder.yield_error(
                    error_id='I001',
                    line_number=len(lines),
                    column_offset=0,
                )

    @classmethod
    def check_blank_lines_from_top(
        cls,
        lines,
    ):
        if len(lines) > 1:
            first_line_is_blank = lines[0].strip() == ''
            if first_line_is_blank:
                yield from cls.error_yielder.yield_error(
                    error_id='I002',
                    line_number=1,
                    column_offset=0,
                )
