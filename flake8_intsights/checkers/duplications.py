import astroid

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
        yield from cls.check_no_duplicate_classes(
            all_astroid_nodes=all_astroid_nodes,
        )

        yield from cls.check_no_duplicate_functions(
            all_astroid_nodes=all_astroid_nodes,
        )

        for node in all_astroid_nodes:
            if isinstance(node, astroid.Dict):
                yield from cls.check_no_duplicate_dict_keys(
                    node=node,
                )
            elif isinstance(node, astroid.ClassDef):
                yield from cls.check_no_duplicate_methods(
                    node=node,
                )

    @classmethod
    def check_no_duplicate_dict_keys(
        cls,
        node,
    ):
        dict_keys = set()

        for dict_item in node.items:
            item_key, item_value = dict_item

            if isinstance(item_key, astroid.DictUnpack):
                item_repr = item_value
            else:
                item_repr = getattr(item_key, 'value', item_key.as_string())

            if item_repr not in dict_keys:
                dict_keys.add(item_repr)
            else:
                yield from cls.error_yielder.yield_error(
                    error_id='I012',
                    line_number=item_key.lineno,
                    column_offset=item_key.col_offset,
                )

    @classmethod
    def check_no_duplicate_classes(
        cls,
        all_astroid_nodes,
    ):
        class_tuples = set()

        for node in all_astroid_nodes:
            if not isinstance(node, astroid.ClassDef):
                continue
            else:
                class_node = node

            class_tuple = (
                class_node.parent,
                class_node.name,
            )
            if class_tuple not in class_tuples:
                class_tuples.add(class_tuple)
            else:
                yield from cls.error_yielder.yield_error(
                    error_id='I012',
                    line_number=class_node.lineno,
                    column_offset=class_node.col_offset,
                )

    @classmethod
    def check_no_duplicate_functions(
        cls,
        all_astroid_nodes,
    ):
        function_tuples = set()

        for node in all_astroid_nodes:
            if not isinstance(node, astroid.FunctionDef):
                continue
            elif isinstance(node.parent, astroid.ClassDef):
                continue
            else:
                function_node = node

            function_tuple = (
                function_node.parent,
                function_node.name,
            )
            if function_tuple not in function_tuples:
                function_tuples.add(function_tuple)
            else:
                yield from cls.error_yielder.yield_error(
                    error_id='I012',
                    line_number=function_node.lineno,
                    column_offset=function_node.col_offset,
                )

    @classmethod
    def check_no_duplicate_methods(
        cls,
        node,
    ):
        method_names = set()
        for node in node.body:
            if not isinstance(node, astroid.FunctionDef):
                continue
            else:
                method_node = node

            if method_node.decorators is not None:
                for decorator in method_node.decorators.nodes:
                    is_setter_attribute = isinstance(decorator, astroid.Attribute) and decorator.attrname == 'setter'
                    is_getter_property = isinstance(decorator, astroid.Name) and decorator.name == 'property'

                    if is_setter_attribute:
                        current_method_names = [
                            f'{method_node.name}.setter',
                        ]
                    elif is_getter_property:
                        current_method_names = [
                            f'{method_node.name}.getter',
                        ]
                    else:
                        current_method_names = [
                            f'{method_node.name}.setter',
                            f'{method_node.name}.getter',
                            method_node.name,
                        ]
            else:
                current_method_names = [
                    f'{method_node.name}.setter',
                    f'{method_node.name}.getter',
                    method_node.name,
                ]

            for method_name in current_method_names:
                if method_name not in method_names:
                    method_names.add(method_name)
                else:
                    yield from cls.error_yielder.yield_error(
                        error_id='I012',
                        line_number=method_node.lineno,
                        column_offset=method_node.col_offset,
                    )

                    break
