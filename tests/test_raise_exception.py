import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class RaiseExceptionTestCase(
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
        filename = 'test_raise_exception'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.raise_exception.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.raise_exception.raise_exception_test_text_001,
            ),
            second=[
                (
                    1,
                    6,
                    'I099 raising an exception should raise an object not a type',
                    'intsights_checker',
                ),
                (
                    4,
                    6,
                    'I099 raising an exception should raise an object not a type',
                    'intsights_checker',
                ),
                (
                    8,
                    10,
                    'I099 raising an exception should raise an object not a type',
                    'intsights_checker',
                ),
                (
                    11,
                    10,
                    'I099 raising an exception should raise an object not a type',
                    'intsights_checker',
                ),
                (
                    15,
                    10,
                    'I099 raising an exception should raise an object not a type',
                    'intsights_checker',
                ),
            ],
        )
