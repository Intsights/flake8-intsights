import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class NamingTestCase(
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
        filename = 'test_naming'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.naming.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertCountEqual(
            first=self.get_linting_errors(
                source_code=texts.naming.naming_test_text_001,
            ),
            second=[
                (
                    65,
                    18,
                    'I097 function arguments should be lower case',
                    'intsights_checker',
                ),
                (
                    14,
                    4,
                    'I094 functions first arguments should be either self/cls whether it is a standard method or a classmethod correspondingly',
                    'intsights_checker',
                ),
                (
                    17,
                    17,
                    'I094 functions first arguments should be either self/cls whether it is a standard method or a classmethod correspondingly',
                    'intsights_checker',
                ),
                (
                    23,
                    17,
                    'I094 functions first arguments should be either self/cls whether it is a standard method or a classmethod correspondingly',
                    'intsights_checker',
                ),
                (
                    27,
                    4,
                    'I094 functions first arguments should be either self/cls whether it is a standard method or a classmethod correspondingly',
                    'intsights_checker',
                ),
                (
                    31,
                    17,
                    'I094 functions first arguments should be either self/cls whether it is a standard method or a classmethod correspondingly',
                    'intsights_checker',
                ),
                (
                    39,
                    17,
                    'I094 functions first arguments should be either self/cls whether it is a standard method or a classmethod correspondingly',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.naming.naming_test_text_002,
            ),
            second=[
                (
                    4,
                    0,
                    'I095 class name should start with upper case char and must not include underscore',
                    'intsights_checker',
                ),
                (
                    7,
                    0,
                    'I095 class name should start with upper case char and must not include underscore',
                    'intsights_checker',
                ),
                (
                    15,
                    0,
                    'I096 unittest TestCase class name should start with the tested module name and end with TestCase',
                    'intsights_checker',
                ),
                (
                    20,
                    0,
                    'I096 unittest TestCase class name should start with the tested module name and end with TestCase',
                    'intsights_checker',
                ),
            ],
        )
