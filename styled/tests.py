from __future__ import print_function
from unittest import TestCase

import core


class TestStyled(TestCase):
    # def test_default(self):
    #     string = 'this is a string'
    #     S = core.Styled(string)
    #     self.assertEqual(S, string)
    #     self.assertIsInstance(S, core.Styled)
    #
    # def test_format(self):
    #     string = 'I have {} {thing}s.'
    #     pos = 5
    #     thing = 'orange'
    #     S = core.Styled(string, pos, thing=thing)
    #     print(S)
    #     self.assertEqual(S, string.format(pos, thing=thing))
    #
    # def test_length(self):
    #     string = 'I have {} {thing}s.'
    #     pos = 11
    #     thing = 'pencil'
    #     S = core.Styled(string, pos, thing=thing)
    #     self.assertEqual(len(S), len(string.format(pos, thing=thing)))

    def test_style(self):
        ss1 = """[[ 'Red'|red:blink ]]"""
        ss2 = """ roses are usually [[ 'red'|red:bold ]]. boogey oogey"""
        # S1 = core.Styled(ss1)
        # print(S1)
        # print(S1.finds)
        # print()
        # S2 = core.Styled(ss2)
        # print(S2)
        # print(S2.finds)
        # print()
        S3 = core.Styled(ss1 + ss2 + ss2 + ss1 + ss1 + ss2)
        # print(S3)
        # print(S3.finds)
        # print()
        ss3 = "Note that [[ 'm.start(group)'|bold:green ]] will equal [[ 'm.end(group)'|bold:yellow ]] if [[ 'group'|underlined ]] " \
              "matched a null string. For example, after [[ 'm = re.search('b(c?)', 'cba')'|bold:blue ]], " \
              "[[ 'm.start(0)'|bold ]] is 1, [[ 'm.end(0)'|bold ]] is 2, [[ 'm.start(1)'|bold ]] and " \
              "[[ 'm.end(1)'|bold ]] are both 2, and [[ 'm.start(2)'|bold ]] raises an [[ 'IndexError'|underlined ]] " \
              "exception."
        S4 = core.Styled(ss3)
        # print(S4)
        # print(S4.finds)
        # print()
        ss4 = "This text [[ 'blinks'|reverse:magenta ]]!"
        S5 = core.Styled(ss4)
