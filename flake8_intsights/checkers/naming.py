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
        for node in all_astroid_nodes:
            if isinstance(node, astroid.FunctionDef):
                yield from cls.check_functions(
                    node=node,
                )
            elif isinstance(node, astroid.ClassDef):
                yield from cls.check_classes(
                    node=node,
                )

    @classmethod
    def check_functions(
        cls,
        node,
    ):
        for arg in node.args.args:
            if not arg.name.islower():
                yield from cls.error_yielder.yield_error(
                    error_id='I097',
                    line_number=arg.fromlineno,
                    column_offset=arg.col_offset,
                )

        if isinstance(node.parent, astroid.ClassDef):
            function_is_classmethod = False
            function_is_staticmethod = False

            if node.name == '__new__':
                function_is_classmethod = True

            for decorator_name in node.decoratornames():
                if decorator_name == 'builtins.classmethod':
                    function_is_classmethod = True

                    break
                elif decorator_name == 'builtins.staticmethod':
                    function_is_staticmethod = True

                    break

            if function_is_staticmethod:
                return

            if not node.args.args:
                yield from cls.error_yielder.yield_error(
                    error_id='I094',
                    line_number=node.fromlineno,
                    column_offset=node.col_offset,
                )

                return

            first_arg = node.args.args[0]
            if function_is_classmethod:
                if first_arg.name != 'cls':
                    yield from cls.error_yielder.yield_error(
                        error_id='I094',
                        line_number=first_arg.fromlineno,
                        column_offset=first_arg.col_offset,
                    )
            else:
                if first_arg.name != 'self':
                    yield from cls.error_yielder.yield_error(
                        error_id='I094',
                        line_number=first_arg.fromlineno,
                        column_offset=first_arg.col_offset,
                    )

    @classmethod
    def check_classes(
        cls,
        node,
    ):
        if not node.name[0].isupper() or '_' in node.name:
            yield from cls.error_yielder.yield_error(
                error_id='I095',
                line_number=node.lineno,
                column_offset=node.col_offset,
            )

        if 'unittest.TestCase' in node.basenames:
            if node.name == 'TestCase' or not node.name.endswith('TestCase'):
                yield from cls.error_yielder.yield_error(
                    error_id='I096',
                    line_number=node.lineno,
                    column_offset=node.col_offset,
                )
