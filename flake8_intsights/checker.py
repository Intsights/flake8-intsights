import astroid
import flake8

from . import checkers


class Checker:
    name = 'intsights'
    version = '0.1.0'

    astroid_builder = astroid.builder.AstroidBuilder()

    def __init__(
        self,
        tree,
        filename,
        lines,
        file_tokens,
    ):
        self.source_code = ''.join(lines)
        self.filename = filename
        self.lines = self.source_code.split('\n')
        self.ast_tree = tree
        self.tokens = file_tokens
        self.start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(self.tokens, 0)
        }

        self.astroid_tree = self.astroid_builder.string_build(
            data=self.source_code,
        )
        self.all_astroid_nodes = []
        for astroid_node in checkers._checker.BaseChecker.walk(
            node=self.astroid_tree,
        ):
            astroid_node_lineno = astroid_node.lineno if astroid_node.lineno is not None else 0
            astroid_node_col_offset = astroid_node.col_offset if astroid_node.col_offset is not None else 0
            astroid_node.position_in_tree = astroid_node_lineno * 10000 + astroid_node_col_offset

            node_inside_formatted_value = False
            current_parent = astroid_node.parent
            while current_parent:
                if isinstance(current_parent, astroid.FormattedValue):
                    node_inside_formatted_value = True

                    break

                current_parent = current_parent.parent

            if not node_inside_formatted_value:
                self.all_astroid_nodes.append(astroid_node)

        self.checkers = checkers.__checkers__

    def run(
        self,
    ):
        for checker in self.checkers:
            yield from checker.check(
                filename=self.filename,
                lines=self.lines,
                tokens=self.tokens,
                start_position_to_token=self.start_position_to_token,
                ast_tree=self.ast_tree,
                astroid_tree=self.astroid_tree,
                all_astroid_nodes=self.all_astroid_nodes,
            )

    @classmethod
    def add_options(
        cls,
        parser,
    ):
        pass

    @classmethod
    def parse_options(
        cls,
        options,
    ):
        original_report = flake8.checker.Manager.report

        def patched_report(
            self,
        ):
            for checker in self.checkers:
                if checker.filename == '__init__.py' or checker.filename.endswith('/__init__.py'):
                    filtered_results = []

                    for result in checker.results:
                        if result[0] != 'F401':
                            filtered_results.append(result)

                    checker.results = filtered_results

            results = original_report(
                self=self,
            )

            return results

        flake8.checker.Manager.report = patched_report
