import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class DeclerationsTestCase(
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
        filename = 'test_declerations'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.declerations.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_001,
            ),
            second=[],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_002,
            ),
            second=[],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_003,
            ),
            second=[],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_004,
            ),
            second=[],
        )

    def test_case_5(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_005,
            ),
            second=[],
        )

    def test_case_6(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_006,
            ),
            second=[],
        )

    def test_case_7(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_007,
            ),
            second=[],
        )

    def test_case_8(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_008,
            ),
            second=[],
        )

    def test_case_9(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_009,
            ),
            second=[],
        )

    def test_case_10(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_010,
            ),
            second=[],
        )

    def test_case_11(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_011,
            ),
            second=[],
        )

    def test_case_12(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_012,
            ),
            second=[],
        )

    def test_case_13(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_013,
            ),
            second=[],
        )

    def test_case_14(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_014,
            ),
            second=[],
        )

    def test_case_15(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_015,
            ),
            second=[],
        )

    def test_case_16(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_016,
            ),
            second=[],
        )

    def test_case_17(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_017,
            ),
            second=[],
        )

    def test_case_18(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_018,
            ),
            second=[],
        )

    def test_case_19(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_019,
            ),
            second=[],
        )

    def test_case_20(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_020,
            ),
            second=[],
        )

    def test_case_21(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_021,
            ),
            second=[],
        )

    def test_case_22(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_022,
            ),
            second=[],
        )

    def test_case_23(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_023,
            ),
            second=[],
        )

    def test_case_24(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_024,
            ),
            second=[],
        )

    def test_case_25(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_025,
            ),
            second=[],
        )

    def test_case_26(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_026,
            ),
            second=[],
        )

    def test_case_27(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_027,
            ),
            second=[],
        )

    def test_case_28(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_028,
            ),
            second=[],
        )

    def test_case_29(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_029,
            ),
            second=[],
        )

    def test_case_30(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_030,
            ),
            second=[],
        )

    def test_case_31(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_031,
            ),
            second=[],
        )

    def test_case_32(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_032,
            ),
            second=[],
        )

    def test_case_33(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_033,
            ),
            second=[],
        )

    def test_case_34(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_034,
            ),
            second=[],
        )

    def test_case_35(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_035,
            ),
            second=[],
        )

    def test_case_36(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_036,
            ),
            second=[],
        )

    def test_case_37(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_037,
            ),
            second=[],
        )

    def test_case_38(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_038,
            ),
            second=[],
        )

    def test_case_39(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_039,
            ),
            second=[],
        )

    def test_case_40(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_040,
            ),
            second=[],
        )

    def test_case_41(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_041,
            ),
            second=[],
        )

    def test_case_42(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_042,
            ),
            second=[],
        )

    def test_case_43(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_043,
            ),
            second=[],
        )

    def test_case_44(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_044,
            ),
            second=[],
        )

    def test_case_45(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_045,
            ),
            second=[],
        )

    def test_case_46(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_046,
            ),
            second=[],
        )

    def test_case_47(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_047,
            ),
            second=[],
        )

    def test_case_48(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_048,
            ),
            second=[],
        )

    def test_case_49(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_049,
            ),
            second=[],
        )

    def test_case_50(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_050,
            ),
            second=[],
        )

    def test_case_51(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_051,
            ),
            second=[],
        )

    def test_case_52(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_052,
            ),
            second=[],
        )

    def test_case_53(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_053,
            ),
            second=[],
        )

    def test_case_54(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_054,
            ),
            second=[],
        )

    def test_case_55(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_055,
            ),
            second=[],
        )

    def test_case_56(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_056,
            ),
            second=[],
        )

    def test_case_57(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_057,
            ),
            second=[],
        )

    def test_case_58(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_058,
            ),
            second=[],
        )

    def test_case_59(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_059,
            ),
            second=[],
        )

    def test_case_60(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_060,
            ),
            second=[],
        )

    def test_case_61(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_061,
            ),
            second=[],
        )

    def test_case_62(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_062,
            ),
            second=[],
        )

    def test_case_63(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_063,
            ),
            second=[],
        )

    def test_case_64(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_064,
            ),
            second=[],
        )

    def test_case_65(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_065,
            ),
            second=[],
        )

    def test_case_66(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_066,
            ),
            second=[
                (
                    1,
                    0,
                    'I051 class definition without inheritance should be declared only by "class Name:"',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_67(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_067,
            ),
            second=[
                (
                    1,
                    16,
                    'I053 each base class should be seperated by a new-line',
                    'intsights_checker',
                ),
                (
                    1,
                    16,
                    'I054 each base class should be one indentation level above the main class',
                    'intsights_checker',
                ),
                (
                    1,
                    16,
                    'I055 each base class definition should be ended with a comma',
                    'intsights_checker',
                ),
                (
                    1,
                    24,
                    'I053 each base class should be seperated by a new-line',
                    'intsights_checker',
                ),
                (
                    1,
                    24,
                    'I054 each base class should be one indentation level above the main class',
                    'intsights_checker',
                ),
                (
                    1,
                    24,
                    'I055 each base class definition should be ended with a comma',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_68(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_068,
            ),
            second=[
                (
                    3,
                    4,
                    'I055 each base class definition should be ended with a comma',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_69(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_069,
            ),
            second=[],
        )

    def test_case_70(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_070,
            ),
            second=[
                (
                    1,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_71(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_071,
            ),
            second=[
                (
                    1,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_72(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_072,
            ),
            second=[
                (
                    1,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_73(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_073,
            ),
            second=[],
        )

    def test_case_74(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_074,
            ),
            second=[
                (
                    3,
                    4,
                    'I065 each function argument should be ended with a comma',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_75(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_075,
            ),
            second=[
                (
                    1,
                    18,
                    'I063 each function argument should be in a new line',
                    'intsights_checker',
                ),
                (
                    1,
                    18,
                    'I064 each function argument should be in the same indentation level, 1 level above the function definition line',
                    'intsights_checker',
                ),
                (
                    1,
                    18,
                    'I065 each function argument should be ended with a comma',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_76(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_076,
            ),
            second=[
                (
                    2,
                    10,
                    'I063 each function argument should be in a new line',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_77(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_077,
            ),
            second=[
                (
                    2,
                    16,
                    'I064 each function argument should be in the same indentation level, 1 level above the function definition line',
                    'intsights_checker',
                ),
                (
                    3,
                    16,
                    'I064 each function argument should be in the same indentation level, 1 level above the function definition line',
                    'intsights_checker',
                ),

            ],
        )

    def test_case_78(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_078,
            ),
            second=[],
        )

    def test_case_79(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_079,
            ),
            second=[],
        )

    def test_case_80(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_080,
            ),
            second=[],
        )

    def test_case_81(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_081,
            ),
            second=[],
        )

    def test_case_82(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_082,
            ),
            second=[],
        )

    def test_case_83(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_083,
            ),
            second=[],
        )

    def test_case_84(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_084,
            ),
            second=[],
        )

    def test_case_85(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_085,
            ),
            second=[],
        )

    def test_case_86(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_086,
            ),
            second=[],
        )

    def test_case_87(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_087,
            ),
            second=[
                (
                    2,
                    4,
                    'I056 classes should never inherit from object',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_88(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_088,
            ),
            second=[],
        )

    def test_case_89(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_089,
            ),
            second=[],
        )

    def test_case_90(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_090,
            ),
            second=[],
        )

    def test_case_91(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_091,
            ),
            second=[],
        )

    def test_case_92(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_092,
            ),
            second=[],
        )

    def test_case_93(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_093,
            ),
            second=[],
        )

    def test_case_94(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_094,
            ),
            second=[],
        )

    def test_case_95(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_095,
            ),
            second=[],
        )

    def test_case_96(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_096,
            ),
            second=[],
        )

    def test_case_97(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_097,
            ),
            second=[
                (
                    3,
                    0,
                    'I071 exception handler parameter name should be "exception"',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_98(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_098,
            ),
            second=[
                (
                    3,
                    0,
                    'I071 exception handler parameter name should be "exception"',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_99(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_099,
            ),
            second=[
                (
                    2,
                    18,
                    'I047 dict keys must not be on the same line',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_100(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_100,
            ),
            second=[
                (
                    3,
                    8,
                    'I048 dict keys must be identically indented',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_101(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_101,
            ),
            second=[
                (
                    3,
                    4,
                    'I048 dict keys must be identically indented',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_102(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_102,
            ),
            second=[
                (
                    3,
                    8,
                    'I046 dict key and value must be on the same line',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_103(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_103,
            ),
            second=[],
        )

    def test_case_104(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_104,
            ),
            second=[
                (
                    14,
                    4,
                    'I049 dict key type must be on of the following: a const, a name, of a dict unpack',
                    'intsights_checker',
                ),
                (
                    17,
                    4,
                    'I049 dict key type must be on of the following: a const, a name, of a dict unpack',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_105(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_105,
            ),
            second=[
                (
                    3,
                    0,
                    'I066 there must not be any empty lines in the function definition',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_106(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_106,
            ),
            second=[
                (
                    3,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
                (
                    5,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
                (
                    7,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
                (
                    9,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
                (
                    14,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
                (
                    16,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
                (
                    18,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
                (
                    20,
                    0,
                    'I061 function definition with no arguments should be defined as: "def function_name():"',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_107(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_107,
            ),
            second=[],
        )

    def test_case_108(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_108,
            ),
            second=[],
        )

    def test_case_109(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.declerations.declerations_test_text_109,
            ),
            second=[],
        )
