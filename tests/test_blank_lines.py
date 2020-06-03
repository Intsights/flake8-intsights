import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class BlankLinesTestCase(
    unittest.TestCase,
):
    def get_linting_errors(
        self,
        source_code,
    ):
        file_tokens = list(
            tokenize.tokenize(
                readline=io.BytesIO(
                    initial_bytes=source_code.encode('utf-8'),
                ).readline,
            )
        )
        tree = ast.parse(source_code)
        filename = 'test_blank_lines'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.blank_lines.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_001,
            ),
            second=[],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_002,
            ),
            second=[
                (
                    2,
                    0,
                    'I001 at each python module, there should be a blank line at the end of the file',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I002 there should not be any blank lines at the top of a python module',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_003,
            ),
            second=[
                (
                    3,
                    0,
                    'I001 at each python module, there should be a blank line at the end of the file',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I002 there should not be any blank lines at the top of a python module',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_004,
            ),
            second=[
                (
                    1,
                    0,
                    'I001 at each python module, there should be a blank line at the end of the file',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_5(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_005,
            ),
            second=[],
        )

    def test_case_6(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_006,
            ),
            second=[
                (
                    3,
                    0,
                    'I001 at each python module, there should be a blank line at the end of the file',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_7(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_007,
            ),
            second=[
                (
                    1,
                    0,
                    'I002 there should not be any blank lines at the top of a python module',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_8(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.blank_lines.blank_lines_test_text_008,
            ),
            second=[
                (
                    1,
                    0,
                    'I002 there should not be any blank lines at the top of a python module',
                    'intsights_checker',
                ),
            ],
        )
