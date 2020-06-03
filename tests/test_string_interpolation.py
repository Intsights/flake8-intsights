import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class StringInterpolationTestCase(
    unittest.TestCase,
):
    def get_linting_errors(
        self,
        source_code,
    ):
        source_code = textwrap.dedent(
            text=source_code.lstrip(),
        )
        file_tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        tree = ast.parse(source_code)
        filename = 'test_string_interpolation'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.string_interpolation.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.string_interpolation.string_interpolation_test_text_001,
            ),
            second=[
                (
                    2,
                    10,
                    'I098 use only fstring for string interpolation. format and % are forbidden',
                    'intsights_checker',
                ),
                (
                    3,
                    10,
                    'I098 use only fstring for string interpolation. format and % are forbidden',
                    'intsights_checker',
                ),
                (
                    4,
                    10,
                    'I098 use only fstring for string interpolation. format and % are forbidden',
                    'intsights_checker',
                ),
                (
                    9,
                    11,
                    'I098 use only fstring for string interpolation. format and % are forbidden',
                    'intsights_checker',
                ),
                (
                    14,
                    19,
                    'I098 use only fstring for string interpolation. format and % are forbidden',
                    'intsights_checker',
                ),
                (
                    15,
                    22,
                    'I098 use only fstring for string interpolation. format and % are forbidden',
                    'intsights_checker',
                ),
            ],
        )
