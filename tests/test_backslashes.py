import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class BackslashesTestCase(
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
        filename = 'test_backslashes'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.backslashes.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.backslashes.backslashes_test_text_001,
            ),
            second=[],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.backslashes.backslashes_test_text_002,
            ),
            second=[
                (
                    1,
                    24,
                    'I093 do not break a line with backslashes',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.backslashes.backslashes_test_text_003,
            ),
            second=[
                (
                    1,
                    24,
                    'I093 do not break a line with backslashes',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.backslashes.backslashes_test_text_004,
            ),
            second=[],
        )
