import astroid
import tokenize
import collections.abc

from . import _checker


class Checker(
    _checker.BaseChecker,
):
    NO_SPACE_CHILD_TYPES = (
        astroid.ClassDef,
        astroid.FunctionDef,
        astroid.AsyncFunctionDef,
        astroid.For,
        astroid.AsyncFor,
        astroid.While,
        astroid.If,
        astroid.With,
        astroid.AsyncWith,
        astroid.TryExcept,
        astroid.TryFinally,
        astroid.ExceptHandler,
    )

    NO_SPACE_BEFORE_TYPES = (
        astroid.TryExcept,
        astroid.TryFinally,
        astroid.ExceptHandler,
    )

    NO_SPACE_NEIGHBOUR_TYPES = (
        astroid.Expr,
    )

    NO_SPACE_NEIGHBOUR_TYPES_VALUES = (
        astroid.Const,
    )

    CONTROL_KEYWORDS = (
        astroid.Return,
        astroid.Break,
        astroid.Continue,
        astroid.Yield,
        astroid.YieldFrom,
        astroid.Pass,
        astroid.Raise,
    )

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
            if isinstance(node, astroid.Arguments):
                continue

            yield from cls.check_no_space_below(
                node=node,
                lines=lines,
            )

            yield from cls.check_right_after_else(
                node=node,
                lines=lines,
            )

            yield from cls.check_one_separation_above(
                node=node,
                lines=lines,
            )

            yield from cls.check_one_separation_below(
                all_astroid_nodes=all_astroid_nodes,
                node=node,
                lines=lines,
            )

        yield from cls.check_no_space_above(
            lines=lines,
            tokens=tokens,
        )

    @classmethod
    def check_no_space_below(
        cls,
        node,
        lines,
    ):
        if not isinstance(node, cls.NO_SPACE_CHILD_TYPES):
            return

        if not hasattr(node, 'body'):
            return

        if not isinstance(node.body, collections.abc.Iterable):
            return

        if getattr(node, 'doc', None) is not None:
            for current_line_number in range(node.lineno - 1, len(lines)):
                current_line = lines[current_line_number]
                if current_line.strip().endswith(':'):
                    next_line = lines[current_line_number + 1]
                    if next_line.strip() == '':
                        yield from cls.error_yielder.yield_error(
                            error_id='I031',
                            line_number=current_line_number + 2,
                            column_offset=0,
                        )

                        return

                    break

        if isinstance(node, astroid.TryFinally):
            first_child_node = node.finalbody[0]
            number_of_blank_lines_above = cls.number_of_blank_lines_above(
                lines=lines,
                node=first_child_node,
            )
            if number_of_blank_lines_above != 0:
                yield from cls.error_yielder.yield_error(
                    error_id='I031',
                    line_number=first_child_node.lineno,
                    column_offset=first_child_node.col_offset,
                )
        else:
            first_child_node = None
            for child_node in cls.walk(
                node=node,
            ):
                if not hasattr(child_node, 'lineno'):
                    continue

                if child_node in node.body:
                    if isinstance(child_node, astroid.Expr):
                        first_child_node = child_node.value
                    else:
                        first_child_node = child_node

                    break

            if first_child_node:
                number_of_blank_lines_above = cls.number_of_blank_lines_above(
                    lines=lines,
                    node=first_child_node,
                )
                if number_of_blank_lines_above != 0:
                    yield from cls.error_yielder.yield_error(
                        error_id='I031',
                        line_number=first_child_node.lineno,
                        column_offset=first_child_node.col_offset,
                    )

    @classmethod
    def check_no_space_above(
        cls,
        lines,
        tokens,
    ):
        no_space_above_keywords = [
            'else',
            'except',
            'finally',
        ]

        for token in tokens:
            if token.type == tokenize.NAME and token.string in no_space_above_keywords:
                token.lineno = token.start[0]
                number_of_blank_lines_above = cls.number_of_blank_lines_above(
                    lines=lines,
                    node=token,
                )
                if number_of_blank_lines_above != 0:
                    yield from cls.error_yielder.yield_error(
                        error_id='I034',
                        line_number=token.start[0],
                        column_offset=token.start[1],
                    )

    @classmethod
    def check_right_after_else(
        cls,
        node,
        lines,
    ):
        if not isinstance(node, astroid.If):
            return

        if not node.orelse:
            return

        if lines[node.orelse[0].lineno - 1].strip().startswith('elif '):
            else_nodes = node.orelse[0].orelse
        else:
            else_nodes = node.orelse

        child_nodes = []
        for child_node in else_nodes:
            if not hasattr(child_node, 'lineno'):
                continue

            if isinstance(child_node, astroid.Expr):
                child_nodes.append(child_node.value)
            else:
                child_nodes.append(child_node)

        if child_nodes:
            number_of_blank_lines_above = cls.number_of_blank_lines_above(
                lines=lines,
                node=child_nodes[0],
            )
            if number_of_blank_lines_above != 0:
                yield from cls.error_yielder.yield_error(
                    error_id='I031',
                    line_number=child_nodes[0].lineno,
                    column_offset=child_nodes[0].col_offset,
                )

    @classmethod
    def check_one_separation_above(
        cls,
        node,
        lines,
    ):
        if not isinstance(node, cls.CONTROL_KEYWORDS):
            return

        node_previous_sibling = node.previous_sibling()
        if node_previous_sibling is None:
            return

        if hasattr(node_previous_sibling, 'body'):
            node_previous_sibling = node_previous_sibling.last_child()

        if isinstance(node_previous_sibling, cls.NO_SPACE_CHILD_TYPES):
            return

        number_of_separation_lines = cls.number_of_separation_lines(
            lines=lines,
            first_node=node_previous_sibling,
            second_node=node,
        )
        if number_of_separation_lines != 1:
            yield from cls.error_yielder.yield_error(
                error_id='I032',
                line_number=node.lineno,
                column_offset=node.col_offset,
            )

    @classmethod
    def check_one_separation_below(
        cls,
        all_astroid_nodes,
        node,
        lines,
    ):
        if not isinstance(node, cls.CONTROL_KEYWORDS):
            return

        node_next_sibling = node.next_sibling()
        if node_next_sibling is None:
            node_next_sibling = cls.get_node_last_sub_node(
                node=node,
            )
            next_node_in_tree = cls.get_next_node_in_tree(
                all_astroid_nodes=all_astroid_nodes,
                node=node_next_sibling,
            )
            if not next_node_in_tree:
                return
        else:
            next_node_in_tree = node_next_sibling

        if next_node_in_tree.lineno == node.lineno:
            return

        if isinstance(next_node_in_tree, cls.NO_SPACE_BEFORE_TYPES):
            return

        line_above_next_sibiling = cls.get_line_above(
            lines=lines,
            node=next_node_in_tree,
        )
        if line_above_next_sibiling.strip() in [
            'try:',
            'except:',
            'finally:',
            'else:',
        ]:
            return

        number_of_blank_lines_above = cls.number_of_blank_lines_above(
            lines=lines,
            node=next_node_in_tree,
        )

        next_node_line = lines[next_node_in_tree.lineno - 1]
        if next_node_line.strip().startswith('elif '):
            if number_of_blank_lines_above != 0:
                yield from cls.error_yielder.yield_error(
                    error_id='I032',
                    line_number=next_node_in_tree.lineno - 1,
                    column_offset=0,
                )
        else:
            if number_of_blank_lines_above == 0:
                yield from cls.error_yielder.yield_error(
                    error_id='I032',
                    line_number=next_node_in_tree.lineno,
                    column_offset=next_node_in_tree.col_offset,
                )
