import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class ImportsTestCase(
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
        filename = 'test_imports'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.imports.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_001,
            ),
            second=[],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_002,
            ),
            second=[],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_003,
            ),
            second=[],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_004,
            ),
            second=[],
        )

    def test_case_5(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_005,
            ),
            second=[],
        )

    def test_case_6(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_006,
            ),
            second=[],
        )

    def test_case_7(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_007,
            ),
            second=[],
        )

    def test_case_8(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_008,
            ),
            second=[],
        )

    def test_case_9(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_009,
            ),
            second=[],
        )

    def test_case_10(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_010,
            ),
            second=[
                (
                    1,
                    0,
                    'I025 never provide a module alias',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_11(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_011,
            ),
            second=[
                (
                    1,
                    0,
                    'I025 never provide a module alias',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_12(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_012,
            ),
            second=[
                (
                    1,
                    0,
                    'I021 only one import module per line',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_13(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_013,
            ),
            second=[
                (
                    1,
                    0,
                    'I021 only one import module per line',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_14(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_014,
            ),
            second=[
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_15(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_015,
            ),
            second=[
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I025 never provide a module alias',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_16(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_016,
            ),
            second=[
                (
                    1,
                    0,
                    'I022 never import * from module',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_17(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_017,
            ),
            second=[
                (
                    1,
                    0,
                    'I021 only one import module per line',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_18(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_018,
            ),
            second=[
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I024 never relative import from a module, import the whole module instead',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_19(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_019,
            ),
            second=[
                (
                    1,
                    0,
                    'I021 only one import module per line',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I024 never relative import from a module, import the whole module instead',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_20(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_020,
            ),
            second=[
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I024 never relative import from a module, import the whole module instead',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_21(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_021,
            ),
            second=[
                (
                    1,
                    0,
                    'I021 only one import module per line',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I024 never relative import from a module, import the whole module instead',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_22(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_022,
            ),
            second=[
                (
                    1,
                    0,
                    'I025 never provide a module alias',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_23(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_023,
            ),
            second=[
                (
                    1,
                    0,
                    'I022 never import * from module',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I023 never from import a module name, just relative from imports',
                    'intsights_checker',
                ),
                (
                    1,
                    0,
                    'I024 never relative import from a module, import the whole module instead',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_24(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_024,
            ),
            second=[
                (
                    2,
                    0,
                    'I027 standard imports and relative imports should be seperated by one newline',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_25(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_025,
            ),
            second=[
                (
                    1,
                    0,
                    'I026 relative imports must be decleared after non-relative ones',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_26(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_026,
            ),
            second=[],
        )

    def test_case_27(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_027,
            ),
            second=[],
        )

    def test_case_28(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_028,
            ),
            second=[],
        )

    def test_case_29(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_029,
            ),
            second=[
                (
                    1,
                    0,
                    'I027 last import must be spaced with two lines',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_30(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.imports.imports_test_text_030,
            ),
            second=[
                (
                    1,
                    0,
                    'I027 last import must be spaced with two lines',
                    'intsights_checker',
                ),
            ],
        )
