import textwrap
import tokenize
import ast
import io
import unittest

import flake8_intsights

from . import texts


class SpacingTestCase(
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
        filename = 'test_spacing'
        lines = io.StringIO(source_code).readlines()

        checker_obj = flake8_intsights.checker.Checker(
            tree=tree,
            filename=filename,
            lines=lines,
            file_tokens=file_tokens,
        )
        checker_obj.checkers = [flake8_intsights.checkers.spacing.Checker]
        linting_errors = list(checker_obj.run())

        return linting_errors

    def test_case_1(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_001,
            ),
            second=[],
        )

    def test_case_2(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_002,
            ),
            second=[
                (
                    3,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_3(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_003,
            ),
            second=[],
        )

    def test_case_4(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_004,
            ),
            second=[
                (
                    3,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_5(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_005,
            ),
            second=[],
        )

    def test_case_6(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_006,
            ),
            second=[
                (
                    5,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_7(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_007,
            ),
            second=[],
        )

    def test_case_8(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_008,
            ),
            second=[
                (
                    4,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_9(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_009,
            ),
            second=[],
        )

    def test_case_10(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_010,
            ),
            second=[
                (
                    4,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_11(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_011,
            ),
            second=[],
        )

    def test_case_12(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_012,
            ),
            second=[
                (
                    6,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_13(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_013,
            ),
            second=[],
        )

    def test_case_14(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_014,
            ),
            second=[
                (
                    4,
                    8,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_15(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_015,
            ),
            second=[],
        )

    def test_case_16(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_016,
            ),
            second=[
                (
                    4,
                    8,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_17(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_017,
            ),
            second=[],
        )

    def test_case_18(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_018,
            ),
            second=[
                (
                    4,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_19(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_019,
            ),
            second=[],
        )

    def test_case_20(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_020,
            ),
            second=[
                (
                    6,
                    8,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_21(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_021,
            ),
            second=[],
        )

    def test_case_22(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_022,
            ),
            second=[
                (
                    6,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_23(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_023,
            ),
            second=[],
        )

    def test_case_24(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_024,
            ),
            second=[
                (
                    4,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
                (
                    4,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_25(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_025,
            ),
            second=[],
        )

    def test_case_26(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_026,
            ),
            second=[
                (
                    5,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_27(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_027,
            ),
            second=[],
        )

    def test_case_28(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_028,
            ),
            second=[
                (
                    5,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_29(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_029,
            ),
            second=[],
        )

    def test_case_30(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_030,
            ),
            second=[
                (
                    5,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_31(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_031,
            ),
            second=[],
        )

    def test_case_32(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_032,
            ),
            second=[
                (
                    5,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_33(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_033,
            ),
            second=[],
        )

    def test_case_34(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_034,
            ),
            second=[
                (
                    5,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
                (
                    5,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_35(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_035,
            ),
            second=[],
        )

    def test_case_36(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_036,
            ),
            second=[
                (
                    3,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_37(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_037,
            ),
            second=[],
        )

    def test_case_38(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_038,
            ),
            second=[
                (
                    3,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_39(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_039,
            ),
            second=[],
        )

    def test_case_40(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_040,
            ),
            second=[
                (
                    3,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_41(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_041,
            ),
            second=[],
        )

    def test_case_42(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_042,
            ),
            second=[
                (
                    3,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_43(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_043,
            ),
            second=[],
        )

    def test_case_44(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_044,
            ),
            second=[
                (
                    4,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_45(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_045,
            ),
            second=[],
        )

    def test_case_46(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_046,
            ),
            second=[
                (
                    4,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_47(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_047,
            ),
            second=[],
        )

    def test_case_48(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_048,
            ),
            second=[
                (
                    6,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_49(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_049,
            ),
            second=[],
        )

    def test_case_50(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_050,
            ),
            second=[
                (
                    6,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_51(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_051,
            ),
            second=[],
        )

    def test_case_52(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_052,
            ),
            second=[
                (
                    6,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_53(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_053,
            ),
            second=[],
        )

    def test_case_54(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_054,
            ),
            second=[
                (
                    8,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_55(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_055,
            ),
            second=[],
        )

    def test_case_56(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_056,
            ),
            second=[
                (
                    6,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_57(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_057,
            ),
            second=[],
        )

    def test_case_58(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_058,
            ),
            second=[
                (
                    4,
                    8,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_59(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_059,
            ),
            second=[],
        )

    def test_case_60(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_060,
            ),
            second=[
                (
                    6,
                    8,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_61(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_061,
            ),
            second=[],
        )

    def test_case_62(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_062,
            ),
            second=[
                (
                    4,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_63(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_063,
            ),
            second=[],
        )

    def test_case_64(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_064,
            ),
            second=[
                (
                    6,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_65(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_065,
            ),
            second=[],
        )

    def test_case_66(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_066,
            ),
            second=[
                (
                    7,
                    8,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_67(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_067,
            ),
            second=[],
        )

    def test_case_68(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_068,
            ),
            second=[
                (
                    9,
                    8,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_69(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_069,
            ),
            second=[],
        )

    def test_case_70(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_070,
            ),
            second=[
                (
                    7,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_71(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_071,
            ),
            second=[],
        )

    def test_case_72(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_072,
            ),
            second=[
                (
                    9,
                    4,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_73(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_073,
            ),
            second=[],
        )

    def test_case_74(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_074,
            ),
            second=[
                (
                    9,
                    0,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_75(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_075,
            ),
            second=[],
        )

    def test_case_76(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_076,
            ),
            second=[
                (
                    6,
                    0,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_77(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_077,
            ),
            second=[],
        )

    def test_case_78(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_078,
            ),
            second=[
                (
                    9,
                    0,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_79(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_079,
            ),
            second=[],
        )

    def test_case_80(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_080,
            ),
            second=[
                (
                    6,
                    0,
                    'I032 control keywords must be divided by space all the time',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_81(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_081,
            ),
            second=[],
        )

    def test_case_82(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_082,
            ),
            second=[],
        )

    def test_case_83(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_083,
            ),
            second=[
                (
                    11,
                    8,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_84(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_084,
            ),
            second=[
                (
                    4,
                    0,
                    'I034 except/finally/else, must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_85(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_085,
            ),
            second=[
                (
                    4,
                    0,
                    'I034 except/finally/else, must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_86(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_086,
            ),
            second=[
                (
                    4,
                    0,
                    'I034 except/finally/else, must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_87(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_087,
            ),
            second=[],
        )

    def test_case_88(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_088,
            ),
            second=[
                (
                    3,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_89(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_089,
            ),
            second=[],
        )

    def test_case_90(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_090,
            ),
            second=[
                (
                    5,
                    4,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_91(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_091,
            ),
            second=[],
        )

    def test_case_92(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_092,
            ),
            second=[
                (
                    2,
                    0,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_93(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_093,
            ),
            second=[],
        )

    def test_case_94(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_094,
            ),
            second=[
                (
                    4,
                    0,
                    'I031 control keywords right after special control definitions must not be spaced',
                    'intsights_checker',
                ),
            ],
        )

    def test_case_95(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_095,
            ),
            second=[],
        )

    def test_case_96(
        self,
    ):
        self.assertEqual(
            first=self.get_linting_errors(
                source_code=texts.spacing.spacing_test_text_096,
            ),
            second=[],
        )
