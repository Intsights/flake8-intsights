import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class BuiltinsTestCase(
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
        filename = 'test_builtins'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.builtins.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.builtins.builtins_test_text_001,
            ),
            second=[
                (
                    2,
                    0,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.builtins.builtins_test_text_002,
            ),
            second=[
                (
                    10,
                    4,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    23,
                    4,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    27,
                    0,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.builtins.builtins_test_text_003,
            ),
            second=[
                (
                    4,
                    4,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    10,
                    7,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    16,
                    4,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.builtins.builtins_test_text_004,
            ),
            second=[
                (
                    7,
                    15,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    13,
                    19,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    16,
                    42,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    22,
                    25,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_5(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.builtins.builtins_test_text_005,
            ),
            second=[
                (
                    7,
                    8,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
                (
                    15,
                    18,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_6(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.builtins.builtins_test_text_006,
            ),
            second=[
                (
                    4,
                    0,
                    'I091 never use a builtin name',
                    'intsights_checker',
                ),
            ],
        )
