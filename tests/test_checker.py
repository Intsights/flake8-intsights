import tokenize
import astroid
import io
import unittest

import flake8_intsights


class CheckerTestCase(
    unittest.TestCase,
):
    @classmethod
    def setUp(
        cls,
    ):
        cls.checker = flake8_intsights.checkers._checker.BaseChecker()

    def test_number_of_blank_lines_above(
        self,
    ):
        source_code = (
            'line_1 = 1\n'
            'line_2 = 2\n'
            'line_3 = 3\n'
        )

        parsed_source = astroid.parse(source_code)
        lines = source_code.split('\n')

        self.assertEqual(
            first=self.checker.number_of_blank_lines_above(lines, parsed_source.body[0]),
            second=0,
        )
        self.assertEqual(
            first=self.checker.number_of_blank_lines_above(lines, parsed_source.body[1]),
            second=0,
        )
        self.assertEqual(
            first=self.checker.number_of_blank_lines_above(lines, parsed_source.body[2]),
            second=0,
        )

        source_code = (
            'line_1 = 1\n\n'
            'line_2 = 2\n\n\n'
            'line_3 = 3\n'
        )

        parsed_source = astroid.parse(source_code)
        lines = source_code.split('\n')

        self.assertEqual(
            first=self.checker.number_of_blank_lines_above(lines, parsed_source.body[0]),
            second=0,
        )
        self.assertEqual(
            first=self.checker.number_of_blank_lines_above(lines, parsed_source.body[1]),
            second=1,
        )
        self.assertEqual(
            first=self.checker.number_of_blank_lines_above(lines, parsed_source.body[2]),
            second=2,
        )

    def test_get_previous_token_from_position(
        self,
    ):
        source_code = (
            'tuple_1 = (\n'
            '   1,\n'
            '   2,\n'
            ')\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        previous_token = self.checker.get_previous_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string='(',
        )

        self.assertEqual(
            first=previous_token['token'].start,
            second=(
                1,
                10,
            ),
        )

        source_code = (
            'list_1 = [\n'
            '   1,\n'
            '   2,\n'
            ']\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        previous_token = self.checker.get_previous_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string='[',
        )

        self.assertEqual(
            first=previous_token['token'].start,
            second=(
                1,
                9,
            ),
        )

        source_code = (
            'set_1 = {\n'
            '   1,\n'
            '   2,\n'
            '}\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        previous_token = self.checker.get_previous_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string='{',
        )

        self.assertEqual(
            first=previous_token['token'].start,
            second=(
                1,
                8,
            ),
        )

        source_code = (
            'dict_1 = {\n'
            '   1: 1,\n'
            '   2: 2,\n'
            '}\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        previous_token = self.checker.get_previous_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string='{',
        )

        self.assertEqual(
            first=previous_token['token'].start,
            second=(
                1,
                9,
            ),
        )

    def test_get_next_token_from_position(
        self,
    ):
        source_code = (
            'tuple_1 = (\n'
            '   1,\n'
            '   2,\n'
            ')\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        next_token = self.checker.get_next_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string=')',
        )

        self.assertEqual(
            first=next_token['token'].start,
            second=(
                4,
                0,
            ),
        )

        source_code = (
            'list_1 = [\n'
            '   1,\n'
            '   2,\n'
            ']\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        next_token = self.checker.get_next_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string=']',
        )

        self.assertEqual(
            first=next_token['token'].start,
            second=(
                4,
                0,
            ),
        )

        source_code = (
            'set_1 = {\n'
            '   1,\n'
            '   2,\n'
            '}\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        next_token = self.checker.get_next_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string='}',
        )

        self.assertEqual(
            first=next_token['token'].start,
            second=(
                4,
                0,
            ),
        )

        source_code = (
            'dict_1 = {\n'
            '   1: 1,\n'
            '   2: 2,\n'
            '}\n'
        )

        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        next_token = self.checker.get_next_token_from_position(
            lineno=2,
            col_offset=3,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
            token_type=tokenize.OP,
            token_string='}',
        )

        self.assertEqual(
            first=next_token['token'].start,
            second=(
                4,
                0,
            ),
        )

    def test_get_node_opener_token(
        self,
    ):
        source_code = (
            'tuple_1 = (\n'
            '   1,\n'
            '   2,\n'
            ')\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_opener_token = self.checker.get_node_opener_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_opener_token['token'].start,
            second=(
                1,
                10,
            ),
        )

        source_code = (
            'list_1 = [\n'
            '   1,\n'
            '   2,\n'
            ']\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_opener_token = self.checker.get_node_opener_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_opener_token['token'].start,
            second=(
                1,
                9,
            ),
        )

        source_code = (
            'set_1 = {\n'
            '   1,\n'
            '   2,\n'
            '}\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_opener_token = self.checker.get_node_opener_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_opener_token['token'].start,
            second=(
                1,
                8,
            ),
        )

        source_code = (
            'dict_1 = {\n'
            '   1: 1,\n'
            '   2: 2,\n'
            '}\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_opener_token = self.checker.get_node_opener_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_opener_token['token'].start,
            second=(
                1,
                9,
            ),
        )

        source_code = (
            'call(\n'
            '   1,\n'
            '   b=2,\n'
            ')\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_opener_token = self.checker.get_node_opener_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_opener_token['token'].start,
            second=(
                1,
                4,
            ),
        )

    def test_get_node_closer_token(
        self,
    ):
        source_code = (
            'tuple_1 = (\n'
            '   1,\n'
            '   2,\n'
            ')\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_closer_token = self.checker.get_node_closer_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_closer_token.start,
            second=(
                4,
                0,
            ),
        )

        source_code = (
            'list_1 = [\n'
            '   1,\n'
            '   2,\n'
            ']\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_closer_token = self.checker.get_node_closer_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_closer_token.start,
            second=(
                4,
                0,
            ),
        )

        source_code = (
            'set_1 = {\n'
            '   1,\n'
            '   2,\n'
            '}\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_closer_token = self.checker.get_node_closer_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_closer_token.start,
            second=(
                4,
                0,
            ),
        )

        source_code = (
            'dict_1 = {\n'
            '   1: 1,\n'
            '   2: 2,\n'
            '}\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_closer_token = self.checker.get_node_closer_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_closer_token.start,
            second=(
                4,
                0,
            ),
        )

        source_code = (
            'call(\n'
            '   1,\n'
            '   b=2,\n'
            ')\n'
        )

        parsed_source = astroid.parse(source_code)
        tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        start_position_to_token = {
            token.start: {
                'token': token,
                'index': index,
            }
            for index, token in enumerate(tokens, 0)
        }

        node_closer_token = self.checker.get_node_closer_token(
            node=parsed_source.body[0].value,
            tokens=tokens,
            start_position_to_token=start_position_to_token,
        )

        self.assertEqual(
            first=node_closer_token.start,
            second=(
                4,
                0,
            ),
        )
