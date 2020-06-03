import astroid

from . import _checker


class Checker(
    _checker.BaseChecker,
):
    FUNCTION_DEF_PREFIXES = (
        'def ',
        'async def ',
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
            if type(node) in cls.LIST_TYPES:
                yield from cls.check_lists(
                    node=node,
                    lines=lines,
                    tokens=tokens,
                    start_position_to_token=start_position_to_token,
                    ast_tree=ast_tree,
                    astroid_tree=astroid_tree,
                )

            if isinstance(node, astroid.Dict):
                yield from cls.check_dicts(
                    node=node,
                    lines=lines,
                    tokens=tokens,
                    ast_tree=ast_tree,
                    astroid_tree=astroid_tree,
                )

            if isinstance(node, astroid.ClassDef):
                yield from cls.check_classes(
                    node=node,
                    lines=lines,
                    tokens=tokens,
                    ast_tree=ast_tree,
                    astroid_tree=astroid_tree,
                )

            if isinstance(node, astroid.FunctionDef):
                yield from cls.check_functions(
                    node=node,
                    lines=lines,
                    tokens=tokens,
                    ast_tree=ast_tree,
                    astroid_tree=astroid_tree,
                    start_position_to_token=start_position_to_token,
                )

            if isinstance(node, astroid.TryExcept):
                yield from cls.check_exception_handling(
                    node=node,
                    lines=lines,
                    tokens=tokens,
                    ast_tree=ast_tree,
                    astroid_tree=astroid_tree,
                )

    @classmethod
    def check_empty_list(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        list_decleration_line = lines[node.lineno - 1]
        if not list_decleration_line[node.col_offset:].startswith(
            (
                '[]',
                '()',
                '{}',
            )
        ):
            yield from cls.error_yielder.yield_error(
                error_id='I041',
                line_number=node.lineno,
                column_offset=node.col_offset,
            )

    @classmethod
    def check_empty_dict(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        list_decleration_line = lines[node.lineno - 1]
        if not list_decleration_line[node.col_offset:].startswith(
            (
                '{}',
            )
        ):
            yield from cls.error_yielder.yield_error(
                error_id='I041',
                line_number=node.lineno,
                column_offset=node.col_offset,
            )

    @classmethod
    def check_one_element_list(
        cls,
        node,
        lines,
        tokens,
        start_position_to_token,
        ast_tree,
        astroid_tree,
    ):
        if isinstance(node, astroid.List):
            list_entry_node = node.elts[0]
            if type(list_entry_node) in [
                astroid.Const,
                astroid.Name,
                astroid.Attribute,
                astroid.Subscript,
            ]:
                list_line = lines[node.lineno - 1]
                closer_token = cls.get_node_closer_token(
                    node=node,
                    tokens=tokens,
                    start_position_to_token=start_position_to_token,
                )
                list_block = list_line[node.col_offset:closer_token.start[1] + 1]
                good_format_string = f'[{list_entry_node.as_string()}]'

                if good_format_string == list_block:
                    return
                else:
                    yield from cls.ensure_sub_elements(
                        node=node,
                        lines=lines,
                        tokens=tokens,
                        start_position_to_token=start_position_to_token,
                        ast_tree=ast_tree,
                        astroid_tree=astroid_tree,
                    )
            else:
                yield from cls.ensure_sub_elements(
                    node=node,
                    lines=lines,
                    tokens=tokens,
                    start_position_to_token=start_position_to_token,
                    ast_tree=ast_tree,
                    astroid_tree=astroid_tree,
                )
        else:
            yield from cls.ensure_sub_elements(
                node=node,
                lines=lines,
                tokens=tokens,
                start_position_to_token=start_position_to_token,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )

    @classmethod
    def check_multiple_elements_list(
        cls,
        node,
        lines,
        tokens,
        start_position_to_token,
        ast_tree,
        astroid_tree,
    ):
        yield from cls.ensure_sub_elements(
            node=node,
            lines=lines,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            ast_tree=ast_tree,
            astroid_tree=astroid_tree,
        )

    @classmethod
    def ensure_sub_elements(
        cls,
        node,
        lines,
        tokens,
        start_position_to_token,
        ast_tree,
        astroid_tree,
    ):
        if isinstance(node, astroid.Tuple):
            if isinstance(node.parent, astroid.For) and node is node.parent.target:
                return

            if isinstance(node.parent, astroid.Comprehension) and node is node.parent.target:
                return

            if isinstance(node.parent, astroid.Assign) and node in node.parent.targets:
                return

            if isinstance(
                node.parent,
                (
                    astroid.Index,
                    astroid.Subscript,
                ),
            ):
                return

            tuple_first_line = lines[node.elts[0].lineno - 1]
            tuple_previous_line = lines[node.elts[0].lineno - 2]
            if not tuple_first_line.strip().startswith('(') and not tuple_previous_line.strip().endswith('('):
                yield from cls.error_yielder.yield_error(
                    error_id='I044',
                    line_number=node.lineno,
                    column_offset=node.col_offset,
                )
            else:
                node.lineno = node.lineno - 1

        previous_node = node
        for list_entry_node in node.elts:
            if type(list_entry_node) in cls.LIST_TYPES:
                if isinstance(list_entry_node, astroid.Tuple):
                    list_entry_previous_line = lines[list_entry_node.elts[0].lineno - 2]
                    if list_entry_previous_line.strip() != '(':
                        yield from cls.error_yielder.yield_error(
                            error_id='I045',
                            line_number=list_entry_node.lineno,
                            column_offset=node.col_offset,
                        )
                else:
                    list_entry_line = lines[list_entry_node.lineno - 1]
                    list_entry_line = list_entry_line.strip()
                    if len(list_entry_line) != 1 and list_entry_line != '[],':
                        yield from cls.error_yielder.yield_error(
                            error_id='I045',
                            line_number=list_entry_node.lineno,
                            column_offset=list_entry_node.col_offset,
                        )

                if list_entry_node == node.elts[-1]:
                    list_closer_token = cls.get_node_closer_token(
                        node=list_entry_node,
                        tokens=tokens,
                        start_position_to_token=start_position_to_token,
                    )
                    list_entry_line = lines[list_closer_token.start[0] - 1]
                    if not list_entry_line.strip().endswith(','):
                        yield from cls.error_yielder.yield_error(
                            error_id='I043',
                            line_number=list_closer_token.start[0],
                            column_offset=list_closer_token.start[1],
                        )
            elif isinstance(list_entry_node, astroid.Call):
                if list_entry_node == node.elts[-1]:
                    list_closer_token = cls.get_node_closer_token(
                        node=list_entry_node,
                        tokens=tokens,
                        start_position_to_token=start_position_to_token,
                    )
                    list_entry_line = lines[list_closer_token.start[0] - 1]
                    if not list_entry_line.strip().endswith(','):
                        yield from cls.error_yielder.yield_error(
                            error_id='I043',
                            line_number=list_closer_token.start[0],
                            column_offset=list_closer_token.start[1],
                        )
            else:
                if list_entry_node.lineno < len(lines):
                    number_of_separation_lines = cls.number_of_separation_lines(
                        lines=lines,
                        first_node=previous_node,
                        second_node=list_entry_node,
                    )
                    list_entry_next_line = lines[list_entry_node.lineno]
                    if (
                        previous_node.lineno == list_entry_node.lineno
                        or number_of_separation_lines > 0
                        or list_entry_next_line.strip() == ''
                    ):
                        yield from cls.error_yielder.yield_error(
                            error_id='I042',
                            line_number=list_entry_node.lineno,
                            column_offset=list_entry_node.col_offset,
                        )

                list_entry_line = lines[list_entry_node.lineno - 1]
                if list_entry_line.strip() in cls.OPENERS:
                    list_closer_token = cls.get_node_closer_token(
                        node=list_entry_node,
                        tokens=tokens,
                        start_position_to_token=start_position_to_token,
                    )
                    list_entry_line = lines[list_closer_token.start[0] - 1]
                    if not list_entry_line.strip().endswith(','):
                        yield from cls.error_yielder.yield_error(
                            error_id='I043',
                            line_number=list_closer_token.start[0],
                            column_offset=list_closer_token.start[1],
                        )
                else:
                    if not list_entry_line.strip().endswith(','):
                        yield from cls.error_yielder.yield_error(
                            error_id='I043',
                            line_number=list_entry_node.lineno,
                            column_offset=list_entry_node.col_offset,
                        )

            previous_node = list_entry_node

    @classmethod
    def check_lists(
        cls,
        node,
        lines,
        tokens,
        start_position_to_token,
        ast_tree,
        astroid_tree,
    ):
        if len(node.elts) == 0:
            yield from cls.check_empty_list(
                node=node,
                lines=lines,
                tokens=tokens,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )
        elif len(node.elts) == 1:
            yield from cls.check_one_element_list(
                node=node,
                lines=lines,
                tokens=tokens,
                start_position_to_token=start_position_to_token,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )
        else:
            yield from cls.check_multiple_elements_list(
                node=node,
                lines=lines,
                tokens=tokens,
                start_position_to_token=start_position_to_token,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )

    @classmethod
    def check_dicts(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        if len(node.items) == 0:
            yield from cls.check_empty_dict(
                node=node,
                lines=lines,
                tokens=tokens,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )
        else:
            for dict_key, dict_value in node.items:
                if not isinstance(
                    dict_key,
                    (
                        astroid.Const,
                        astroid.DictUnpack,
                        astroid.Name,
                        astroid.JoinedStr,
                        astroid.Subscript,
                        astroid.Attribute,
                    )
                ):
                    yield from cls.error_yielder.yield_error(
                        error_id='I049',
                        line_number=dict_key.lineno,
                        column_offset=dict_key.col_offset,
                    )

                    continue

                if dict_key.lineno == dict_value.lineno:
                    continue

                if lines[dict_key.lineno - 1].rstrip().endswith(':'):
                    yield from cls.error_yielder.yield_error(
                        error_id='I046',
                        line_number=dict_value.lineno,
                        column_offset=dict_value.col_offset,
                    )

            if len(node.items) > 1:
                for i in range(len(node.items) - 1):
                    first_element_key = node.items[i][0]
                    second_element_key = node.items[i + 1][0]

                    if first_element_key.lineno == second_element_key.lineno:
                        yield from cls.error_yielder.yield_error(
                            error_id='I047',
                            line_number=second_element_key.lineno,
                            column_offset=second_element_key.col_offset,
                        )

                        continue

                    if isinstance(first_element_key, astroid.DictUnpack):
                        first_element_key_col_offset = first_element_key.col_offset - 2
                    else:
                        first_element_key_col_offset = first_element_key.col_offset

                    if isinstance(second_element_key, astroid.DictUnpack):
                        second_element_key_col_offset = second_element_key.col_offset - 2
                    else:
                        second_element_key_col_offset = second_element_key.col_offset

                    if first_element_key_col_offset != second_element_key_col_offset:
                        yield from cls.error_yielder.yield_error(
                            error_id='I048',
                            line_number=second_element_key.lineno,
                            column_offset=second_element_key.col_offset,
                        )

    @classmethod
    def check_empty_class(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        empty_class_definition_format = f'class {node.name}:'

        class_definition_lineno = node.lineno
        class_definition_text = lines[node.lineno - 1]
        while not class_definition_text.lstrip().startswith('class '):
            class_definition_lineno += 1
            class_definition_text = lines[class_definition_lineno - 1]

        if class_definition_text.strip() != empty_class_definition_format:
            yield from cls.error_yielder.yield_error(
                error_id='I051',
                line_number=class_definition_lineno,
                column_offset=0,
            )

    @classmethod
    def check_inheritance_class(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        inheritance_class_definition_format = f'class {node.name}('

        class_definition_lineno = node.lineno
        class_definition_text = lines[node.lineno - 1]
        while not class_definition_text.lstrip().startswith('class '):
            class_definition_lineno += 1
            class_definition_text = lines[class_definition_lineno - 1]

        if not class_definition_text.strip().startswith(inheritance_class_definition_format):
            yield from cls.error_yielder.yield_error(
                error_id='I052',
                line_number=node.lineno,
                column_offset=node.col_offset,
            )

        main_class_indentation_level = cls.get_line_indentation_level(
            line=lines[node.lineno - 1],
        )
        last_base_class_definition_line_number = class_definition_lineno
        for base_class in node.bases:
            if isinstance(base_class, astroid.Name) and base_class.name == 'object':
                yield from cls.error_yielder.yield_error(
                    error_id='I056',
                    line_number=base_class.lineno,
                    column_offset=base_class.col_offset,
                )

            if base_class.lineno != last_base_class_definition_line_number + 1:
                yield from cls.error_yielder.yield_error(
                    error_id='I053',
                    line_number=base_class.lineno,
                    column_offset=base_class.col_offset,
                )

            base_class_line = lines[base_class.lineno - 1]
            base_class_indentation_level = cls.get_line_leading_indentations(
                line=base_class_line,
            )
            if base_class_indentation_level != main_class_indentation_level + 1:
                yield from cls.error_yielder.yield_error(
                    error_id='I054',
                    line_number=base_class.lineno,
                    column_offset=base_class.col_offset,
                )

            if not base_class_line.endswith(','):
                yield from cls.error_yielder.yield_error(
                    error_id='I055',
                    line_number=base_class.lineno,
                    column_offset=base_class.col_offset,
                )

            last_base_class_definition_line_number = base_class.lineno

    @classmethod
    def check_classes(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        if len(node.bases) == 0:
            yield from cls.check_empty_class(
                node=node,
                lines=lines,
                tokens=tokens,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )
        else:
            yield from cls.check_inheritance_class(
                node=node,
                lines=lines,
                tokens=tokens,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )

    @classmethod
    def check_no_args_function(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        function_definition_lineno = node.lineno
        function_definition_text = lines[node.lineno - 1]
        while not function_definition_text.lstrip().startswith(cls.FUNCTION_DEF_PREFIXES):
            function_definition_lineno += 1
            function_definition_text = lines[function_definition_lineno - 1]

        if node.args.vararg or node.args.kwarg:
            function_without_args_definition_format = (
                f'def {node.name}(',
                f'async def {node.name}(',
            )
            if not function_definition_text.strip().startswith(function_without_args_definition_format):
                yield from cls.error_yielder.yield_error(
                    error_id='I061',
                    line_number=function_definition_lineno,
                    column_offset=0,
                )
        else:
            function_without_args_definition_format = (
                f'def {node.name}()',
                f'async def {node.name}()',
                f'def {node.name}() -> ',
                f'async def {node.name}() -> ',
            )

            clean_definition = function_definition_text.strip().startswith(function_without_args_definition_format)
            clean_definition &= not function_definition_text.endswith(' :')
            clean_definition &= function_definition_text.endswith(':')
            if not clean_definition:
                yield from cls.error_yielder.yield_error(
                    error_id='I061',
                    line_number=function_definition_lineno,
                    column_offset=0,
                )

    @classmethod
    def check_args_function(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
        start_position_to_token,
    ):
        function_with_args_definition_format = (
            f'def {node.name}(',
            f'async def {node.name}(',
        )

        function_definition_lineno = node.lineno
        function_definition_text = lines[node.lineno - 1]
        while not function_definition_text.lstrip().startswith(cls.FUNCTION_DEF_PREFIXES):
            function_definition_lineno += 1
            function_definition_text = lines[function_definition_lineno - 1]

        last_argument_definition_lineno = function_definition_lineno

        if not function_definition_text.strip().startswith(function_with_args_definition_format):
            yield from cls.error_yielder.yield_error(
                error_id='I062',
                line_number=function_definition_lineno,
                column_offset=node.col_offset,
            )

        function_definition_indentation_level = cls.get_line_leading_indentations(
            line=function_definition_text,
        )

        for function_argument in node.args.args:
            if function_argument.lineno != last_argument_definition_lineno + 1:
                yield from cls.error_yielder.yield_error(
                    error_id='I063',
                    line_number=function_argument.lineno,
                    column_offset=function_argument.col_offset,
                )

            function_argument_line = lines[function_argument.lineno - 1]
            function_argument_indentation_level = cls.get_line_leading_indentations(
                line=function_argument_line,
            )
            if function_argument_indentation_level != function_definition_indentation_level + 1:
                yield from cls.error_yielder.yield_error(
                    error_id='I064',
                    line_number=function_argument.lineno,
                    column_offset=function_argument.col_offset,
                )

            if not function_argument_line.endswith(','):
                if function_argument_line.endswith(
                    (
                        '[',
                        '(',
                        '{',
                        '\'\'\'',
                    )
                ):
                    break

                yield from cls.error_yielder.yield_error(
                    error_id='I065',
                    line_number=function_argument.lineno,
                    column_offset=function_argument.col_offset,
                )

            function_argument_next_line = lines[function_argument.lineno]
            if function_argument_next_line.strip() == '':
                yield from cls.error_yielder.yield_error(
                    error_id='I066',
                    line_number=function_argument.lineno + 1,
                    column_offset=0,
                )

            last_argument_definition_lineno = function_argument.lineno

    @classmethod
    def check_functions(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
        start_position_to_token,
    ):
        if len(node.args.args) == 0:
            yield from cls.check_no_args_function(
                node=node,
                lines=lines,
                tokens=tokens,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
            )
        else:
            yield from cls.check_args_function(
                node=node,
                lines=lines,
                tokens=tokens,
                ast_tree=ast_tree,
                astroid_tree=astroid_tree,
                start_position_to_token=start_position_to_token,
            )

    @classmethod
    def check_exception_handling(
        cls,
        node,
        lines,
        tokens,
        ast_tree,
        astroid_tree,
    ):
        for exception_handler in node.handlers:
            if exception_handler.name is None:
                continue

            if exception_handler.name.as_string() != 'exception':
                yield from cls.error_yielder.yield_error(
                    error_id='I071',
                    line_number=exception_handler.lineno,
                    column_offset=exception_handler.col_offset,
                )
