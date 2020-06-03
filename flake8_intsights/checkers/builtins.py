import ast
import inspect
import builtins

from . import _checker


class Checker(
    _checker.BaseChecker,
):
    BUILTINS = [
        member[0]
        for member in inspect.getmembers(builtins)
        if member[0] not in [
            '__name__',
            '__doc__',
            'credits',
            '_',
        ]
    ]

    FUNCTION_NODES = (
        ast.FunctionDef,
        ast.AsyncFunctionDef,
    )

    FOR_NODES = (
        ast.For,
        ast.AsyncFor,
    )

    WITH_NODES = (
        ast.With,
        ast.AsyncWith,
    )

    IMPORT_NODES = (
        ast.Import,
        ast.ImportFrom,
    )

    ITERATOR_NODES = (
        ast.Tuple,
        ast.List,
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
        for node in ast.walk(ast_tree):
            if isinstance(node, ast.Assign):
                yield from cls.check_assignment(
                    node=node,
                )
            elif isinstance(node, cls.FUNCTION_NODES):
                yield from cls.check_function_definition(
                    node=node,
                )
            elif isinstance(node, cls.FOR_NODES):
                yield from cls.check_for_loop(
                    node=node,
                )
            elif isinstance(node, cls.WITH_NODES):
                yield from cls.check_with(
                    node=node,
                )
            elif isinstance(node, ast.ListComp):
                yield from cls.check_list_comprehension(
                    node=node,
                )
            elif isinstance(node, ast.ClassDef):
                yield from cls.check_class(
                    node=node,
                )

    @classmethod
    def check_assignment(
        cls,
        node,
    ):
        stack = list(node.targets)
        while stack:
            item = stack.pop()
            if isinstance(item, cls.ITERATOR_NODES):
                stack.extend(list(item.elts))
            elif isinstance(item, ast.Name) and item.id in cls.BUILTINS:
                yield from cls.error_yielder.yield_error(
                    error_id='I091',
                    line_number=item.lineno,
                    column_offset=item.col_offset,
                )
            elif isinstance(item, ast.Starred) and item.value.id in cls.BUILTINS:
                yield from cls.error_yielder.yield_error(
                    error_id='I091',
                    line_number=item.lineno,
                    column_offset=item.col_offset,
                )

    @classmethod
    def check_function_definition(
        cls,
        node,
    ):
        if node.name in cls.BUILTINS:
            yield from cls.error_yielder.yield_error(
                error_id='I091',
                line_number=node.lineno,
                column_offset=node.col_offset,
            )

        for arg in node.args.args:
            if arg.arg in cls.BUILTINS:
                yield from cls.error_yielder.yield_error(
                    error_id='I091',
                    line_number=arg.lineno,
                    column_offset=arg.col_offset,
                )

    @classmethod
    def check_for_loop(
        cls,
        node,
    ):
        stack = [
            node.target,
        ]
        while stack:
            item = stack.pop()
            if isinstance(item, cls.ITERATOR_NODES):
                stack.extend(list(item.elts))
            elif isinstance(item, ast.Name) and item.id in cls.BUILTINS:
                yield from cls.error_yielder.yield_error(
                    error_id='I091',
                    line_number=item.lineno,
                    column_offset=item.col_offset,
                )
            elif isinstance(item, ast.Starred) and item.value.id in cls.BUILTINS:
                yield from cls.error_yielder.yield_error(
                    error_id='I091',
                    line_number=item.lineno,
                    column_offset=item.col_offset,
                )

    @classmethod
    def check_with(
        cls,
        node,
    ):
        for item in node.items:
            var = item.optional_vars
            if isinstance(var, cls.ITERATOR_NODES):
                for element in var.elts:
                    if isinstance(element, ast.Name) and element.id in cls.BUILTINS:
                        yield from cls.error_yielder.yield_error(
                            error_id='I091',
                            line_number=element.lineno,
                            column_offset=element.col_offset,
                        )
                    elif isinstance(element, ast.Starred) and element.value.id in cls.BUILTINS:
                        yield from cls.error_yielder.yield_error(
                            error_id='I091',
                            line_number=element.lineno,
                            column_offset=element.col_offset,
                        )
            elif isinstance(var, ast.Name) and var.id in cls.BUILTINS:
                yield from cls.error_yielder.yield_error(
                    error_id='I091',
                    line_number=var.lineno,
                    column_offset=var.col_offset,
                )

    @classmethod
    def check_list_comprehension(
        cls,
        node,
    ):
        for generator in node.generators:
            if isinstance(generator.target, ast.Name) and generator.target.id in cls.BUILTINS:
                yield from cls.error_yielder.yield_error(
                    error_id='I091',
                    line_number=generator.target.lineno,
                    column_offset=generator.target.col_offset,
                )
            elif isinstance(generator.target, cls.ITERATOR_NODES):
                for tuple_element in generator.target.elts:
                    if isinstance(tuple_element, ast.Name) and tuple_element.id in cls.BUILTINS:
                        yield from cls.error_yielder.yield_error(
                            error_id='I091',
                            line_number=tuple_element.lineno,
                            column_offset=tuple_element.col_offset,
                        )

    @classmethod
    def check_class(
        cls,
        node,
    ):
        if node.name in cls.BUILTINS:
            yield from cls.error_yielder.yield_error(
                error_id='I091',
                line_number=node.lineno,
                column_offset=node.col_offset,
            )
