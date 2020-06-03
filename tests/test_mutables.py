import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class MutablesTestCase(
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
        filename = 'test_mutables'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.mutables.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_001,
            ),
            second=[],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_002,
            ),
            second=[],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_003,
            ),
            second=[
                (
                    2,
                    10,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_004,
            ),
            second=[
                (
                    2,
                    10,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_5(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_005,
            ),
            second=[
                (
                    2,
                    10,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_6(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_006,
            ),
            second=[
                (
                    2,
                    10,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_7(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_007,
            ),
            second=[],
        )

    def test_case_8(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_008,
            ),
            second=[],
        )

    def test_case_9(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_009,
            ),
            second=[
                (
                    3,
                    14,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_10(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_010,
            ),
            second=[
                (
                    3,
                    14,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_11(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_011,
            ),
            second=[
                (
                    3,
                    14,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_12(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_012,
            ),
            second=[
                (
                    3,
                    14,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_13(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_013,
            ),
            second=[],
        )

    def test_case_14(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_014,
            ),
            second=[],
        )

    def test_case_15(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_015,
            ),
            second=[
                (
                    4,
                    16,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_16(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_016,
            ),
            second=[
                (
                    3,
                    14,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
                (
                    4,
                    16,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_17(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_017,
            ),
            second=[
                (
                    2,
                    14,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
                (
                    4,
                    16,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_18(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.mutables.mutables_test_text_018,
            ),
            second=[
                (
                    3,
                    14,
                    'I081 function default parameter must not be mutable',
                    'intsights_checker',
                ),
            ],
        )
