import collections
import astroid
import tokenize

from . import _errors


class BaseChecker:
    LIST_TYPES = [
        astroid.List,
        astroid.Tuple,
        astroid.Set,
    ]
    LATE_OPENERS_TYPES = [
        astroid.Call,
    ]
    LATE_CLOSERS_TYPES = [
        astroid.Tuple,
    ]
    OPENERS = [
        '[',
        '(',
        '{',
    ]
    CLOSERES = [
        ']',
        ')',
        '}',
    ]

    error_yielder = _errors.ErrorYielder

    @classmethod
    def walk(
        cls,
        node,
    ):
        nodes = set()

        nodes_to_go_through = collections.deque(
            iterable=[
                node,
            ],
        )
        while nodes_to_go_through:
            node = nodes_to_go_through.popleft()

            for name in node._astroid_fields:
                field = getattr(node, name, None)
                if isinstance(field, astroid.node_classes.NodeNG):
                    nodes_to_go_through.append(field)
                elif isinstance(field, list):
                    for item in field:
                        if isinstance(item, tuple):
                            for sub_item in item:
                                if isinstance(sub_item, astroid.node_classes.NodeNG):
                                    nodes_to_go_through.append(sub_item)
                        elif isinstance(item, astroid.node_classes.NodeNG):
                            nodes_to_go_through.append(item)

            if node not in nodes:
                yield node

                nodes.add(node)

    @classmethod
    def get_line_above(
        cls,
        lines,
        node,
    ):
        node_line_number = node.lineno

        if node_line_number > 1:
            return lines[node_line_number - 2]
        else:
            return None

    @classmethod
    def number_of_blank_lines_above(
        cls,
        lines,
        node,
    ):
        node_line_number = node.lineno

        number_of_blank_lines = 0
        for line in reversed(lines[:node_line_number - 1]):
            if line.strip() != '':
                break

            number_of_blank_lines += 1

        return number_of_blank_lines

    @classmethod
    def number_of_separation_lines(
        cls,
        lines,
        first_node,
        second_node,
    ):
        first_node_index = first_node.lineno - 1
        second_node_index = second_node.lineno - 1

        number_of_lines = 0
        for line_index in range(
            second_node_index - 1,
            first_node_index,
            -1,
        ):
            if lines[line_index].strip() == '':
                number_of_lines += 1
            else:
                break

        return number_of_lines

    @classmethod
    def get_previous_token_from_position(
        cls,
        lineno,
        col_offset,
        tokens,
        start_position_to_token,
        token_type,
        token_string,
    ):
        from_token_position = (
            lineno,
            col_offset,
        )

        current_token_index = start_position_to_token[from_token_position]['index']
        for token in reversed(tokens[:current_token_index]):
            if token.type == token_type and token.string == token_string:
                token_index = start_position_to_token[token.start]['index']

                return {
                    'token': token,
                    'index': token_index,
                }

    @classmethod
    def get_next_token_from_position(
        cls,
        lineno,
        col_offset,
        tokens,
        start_position_to_token,
        token_type,
        token_string,
    ):
        from_token_position = (
            lineno,
            col_offset,
        )

        current_token_index = start_position_to_token[from_token_position]['index']

        for token in tokens[current_token_index:]:
            if token.type == token_type and token.string == token_string:
                token_index = start_position_to_token[token.start]['index']

                return {
                    'token': token,
                    'index': token_index,
                }

    @classmethod
    def get_token_by_position(
        cls,
        lineno,
        col_offset,
        tokens,
    ):
        for token in tokens:
            token_start_lineno = token.start[0]
            token_start_col_offset = token.start[1]
            token_end_lineno = token.end[0]
            token_end_col_offset = token.end[1]

            same_lines = token_start_lineno <= lineno and lineno <= token_end_lineno

            same_cols = True
            if token_start_lineno == lineno:
                if token_start_col_offset > col_offset:
                    same_cols = False

            if token_end_lineno == lineno:
                if token_end_col_offset < col_offset:
                    same_cols = False

            if same_lines and same_cols:
                return token

        return None

    @classmethod
    def get_node_opener_token(
        cls,
        node,
        tokens,
        start_position_to_token,
    ):
        node_start_lineno = node.lineno
        node_start_offset = node.col_offset
        node_opener_position = (
            node_start_lineno,
            node_start_offset,
        )

        if isinstance(
            node,
            (
                astroid.List,
                astroid.Dict,
                astroid.Set,
            )
        ):
            return start_position_to_token[node_opener_position]
        elif isinstance(node, astroid.Tuple):
            current_node_token_string = start_position_to_token[node_opener_position]['token'].string
            if current_node_token_string == '(':
                return start_position_to_token[node_opener_position]

            return cls.get_previous_token_from_position(
                lineno=node_start_lineno,
                col_offset=node_start_offset,
                tokens=tokens,
                start_position_to_token=start_position_to_token,
                token_type=tokenize.OP,
                token_string='(',
            )
        elif isinstance(
            node,
            (
                astroid.Call,
                astroid.FunctionDef,
                astroid.AsyncFunctionDef,
            )
        ):
            return cls.get_next_token_from_position(
                lineno=node_start_lineno,
                col_offset=node_start_offset,
                tokens=tokens,
                start_position_to_token=start_position_to_token,
                token_type=tokenize.OP,
                token_string='(',
            )

    @classmethod
    def get_node_closer_token(
        cls,
        node,
        tokens,
        start_position_to_token,
    ):
        opener_token = cls.get_node_opener_token(
            node=node,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        current_open_token_index = opener_token['index']

        current_nesting_counter = 0
        for token in tokens[current_open_token_index:]:
            if token.type == tokenize.OP and token.string in cls.OPENERS:
                current_nesting_counter += 1

            if token.type == tokenize.OP and token.string in cls.CLOSERES:
                current_nesting_counter -= 1

            if current_nesting_counter == 0:
                return token
        else:
            return None

    @classmethod
    def get_line_leading_indentations(
        cls,
        line,
    ):
        number_of_leading_spaces = len(line) - len(line.lstrip(' '))

        return number_of_leading_spaces / 4

    @classmethod
    def get_line_indentation_level(
        cls,
        line,
    ):
        spaces_from_start = 0

        for char in line:
            if char != ' ':
                break

            spaces_from_start += 1

        return spaces_from_start / 4

    @classmethod
    def get_node_last_sub_node(
        cls,
        node,
    ):
        node_children = list(node.get_children())
        if not node_children:
            return node

        child_node = node_children[-1]
        child_node_children = list(child_node.get_children())
        if child_node_children:
            return cls.get_node_last_sub_node(
                node=child_node,
            )
        else:
            return child_node

    @classmethod
    def get_next_node_in_tree(
        cls,
        all_astroid_nodes,
        node,
    ):
        closest_node = None
        shortest_distance_between_nodes = None
        node_position_in_tree = getattr(node, 'lineno', 0) * 10000 + getattr(node, 'col_offset', 0)
        if node_position_in_tree == 0:
            return None

        for candidate_node in all_astroid_nodes:
            distance_between_nodes = candidate_node.position_in_tree - node_position_in_tree
            if distance_between_nodes <= 0:
                continue

            if shortest_distance_between_nodes is None or distance_between_nodes < shortest_distance_between_nodes:
                shortest_distance_between_nodes = distance_between_nodes
                closest_node = candidate_node

        return closest_node
