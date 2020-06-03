import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class IndentsTestCase(
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
        filename = 'test_indents'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.indents.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_001,
            ),
            second=[],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_002,
            ),
            second=[
                (
                    2,
                    0,
                    'I004 only 4 spaces indentation',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_003,
            ),
            second=[
                (
                    2,
                    0,
                    'I003 no tabs indentation, only spaces',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_004,
            ),
            second=[],
        )

    def test_case_5(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_005,
            ),
            second=[
                (
                    2,
                    0,
                    'I006 indentation should be gradually added',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_6(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_006,
            ),
            second=[
                (
                    2,
                    0,
                    'I006 indentation should be gradually added',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_7(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_007,
            ),
            second=[
                (
                    4,
                    0,
                    'I006 indentation should be gradually added',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_8(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_008,
            ),
            second=[
                (
                    3,
                    0,
                    'I006 indentation should be gradually added',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_9(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_009,
            ),
            second=[],
        )

    def test_case_10(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_010,
            ),
            second=[],
        )

    def test_case_11(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_011,
            ),
            second=[
                (
                    3,
                    0,
                    'I006 indentation should be gradually added',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_12(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_012,
            ),
            second=[],
        )

    def test_case_13(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_013,
            ),
            second=[],
        )

    def test_case_14(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_014,
            ),
            second=[],
        )

    def test_case_15(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.indents.indents_test_text_015,
            ),
            second=[],
        )
