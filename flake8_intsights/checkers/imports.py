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
        import_nodes = [
            node
            for node in astroid_tree.body
            if isinstance(node, astroid.Import)
        ]
        from_import_nodes = [
            node
            for node in astroid_tree.body
            if isinstance(node, astroid.ImportFrom)
        ]

        yield from cls.ensure_imports(
            imports=import_nodes,
        )

        yield from cls.ensure_from_imports(
            from_imports=from_import_nodes,
        )

        yield from cls.ensure_imports_order(
            imports=import_nodes,
            from_imports=from_import_nodes,
        )

        yield from cls.ensure_last_import_spaced(
            lines=lines,
            imports=import_nodes,
            from_imports=from_import_nodes,
        )

    @classmethod
    def ensure_imports_order(
        cls,
        imports,
        from_imports,
    ):
        imports_line_numbers = [
            import_node.lineno
            for import_node in imports
        ]
        from_imports_line_numbers = [
            from_import_node.lineno
            for from_import_node in from_imports
        ]

        if imports_line_numbers and from_imports_line_numbers:
            max_import_line_number = max(imports_line_numbers)
            min_from_import_line_number = min(from_imports_line_numbers)

            imports_correct_order = max_import_line_number < min_from_import_line_number
            imports_correct_separation = max_import_line_number + 2 == min_from_import_line_number

            if not imports_correct_order:
                yield from cls.error_yielder.yield_error(
                    error_id='I026',
                    line_number=min_from_import_line_number,
                    column_offset=0,
                )

            if imports_correct_order and not imports_correct_separation:
                yield from cls.error_yielder.yield_error(
                    error_id='I027',
                    line_number=min_from_import_line_number,
                    column_offset=0,
                )

    @classmethod
    def ensure_last_import_spaced(
        cls,
        lines,
        imports,
        from_imports,
    ):
        imports_line_numbers = [
            import_node.lineno
            for import_node in imports
        ]
        from_imports_line_numbers = [
            from_import_node.lineno
            for from_import_node in from_imports
        ]

        if imports_line_numbers or from_imports_line_numbers:
            max_import_line_number = max(imports_line_numbers + from_imports_line_numbers)
            next_two_lines = lines[max_import_line_number:max_import_line_number + 2]

            for line in next_two_lines:
                if line.strip():
                    yield from cls.error_yielder.yield_error(
                        error_id='I028',
                        line_number=max_import_line_number,
                        column_offset=0,
                    )

    @classmethod
    def ensure_imports(
        cls,
        imports,
    ):
        for import_node in imports:
            if len(import_node.names) > 1:
                yield from cls.error_yielder.yield_error(
                    error_id='I021',
                    line_number=import_node.lineno,
                    column_offset=import_node.col_offset,
                )

            if import_node.names[0][1] is not None:
                yield from cls.error_yielder.yield_error(
                    error_id='I025',
                    line_number=import_node.lineno,
                    column_offset=import_node.col_offset,
                )

    @classmethod
    def ensure_from_imports(
        cls,
        from_imports,
    ):
        for from_import_node in from_imports:
            if len(from_import_node.names) > 1:
                yield from cls.error_yielder.yield_error(
                    error_id='I021',
                    line_number=from_import_node.lineno,
                    column_offset=from_import_node.col_offset,
                )

            if len(from_import_node.names) == 1 and from_import_node.names[0][0] == '*':
                yield from cls.error_yielder.yield_error(
                    error_id='I022',
                    line_number=from_import_node.lineno,
                    column_offset=from_import_node.col_offset,
                )

            if from_import_node.modname != '':
                yield from cls.error_yielder.yield_error(
                    error_id='I023',
                    line_number=from_import_node.lineno,
                    column_offset=from_import_node.col_offset,
                )

            if from_import_node.level and from_import_node.modname != '':
                yield from cls.error_yielder.yield_error(
                    error_id='I024',
                    line_number=from_import_node.lineno,
                    column_offset=from_import_node.col_offset,
                )

            if from_import_node.names[0][1] is not None:
                yield from cls.error_yielder.yield_error(
                    error_id='I025',
                    line_number=from_import_node.lineno,
                    column_offset=from_import_node.col_offset,
                )
