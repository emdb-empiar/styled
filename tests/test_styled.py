# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from unittest import TestCase

from styled import Styled, StyleError, ESC, END


class NonStringType(object):
    def __init__(self, s):
        self.s = s


class Py23Fix(object):
    def __init__(self, *args, **kwargs):
        if sys.version_info[0] > 2:
            pass
        else:
            # new names for assert methods
            self.assertCountEqual = self.assertItemsEqual
        super(Py23Fix, self).__init__(*args, **kwargs)


class BaseTestStyled(Py23Fix, TestCase):
    pass


class TestStyled(BaseTestStyled):
    def test_default(self):
        string = 'this is a string'
        S = Styled(string)
        self.assertEqual(S, string)
        self.assertIsInstance(S, Styled)

    def test_empty(self):
        s = Styled()
        self.assertEqual(len(s), 0)

    def test_type(self):
        s = NonStringType(27)
        with self.assertRaises(ValueError):
            Styled(s)

    def test_find_tokens(self):
        s = """[[ 'a word'|fg-red ]]"""
        s = Styled(s)
        self.assertCountEqual(s._tokens, [(0, 21, u'a word', [u'fg-red'])])
        s = Styled("""[[ 'your {} is open'|fg-blue ]]""", 'bank')
        self.assertCountEqual(s._tokens, [(0, 33, u'your bank is open', [u'fg-blue'])])

    def test_length(self):
        u = 'I am the most handsome guy in the room.'
        u_list = u.split(' ')
        s = Styled(" ".join(u_list[:4] + ["[[ '{}'|bold ]]".format(u_list[4])] + u_list[5:]))
        self.assertEqual(len(u), len(s))

    def test_format(self):
        u = "This is a very {} affair in which {count} people were involved."
        s = Styled(u, 'noble', count=38)
        self.assertEqual(s, u.format('noble', count=38))

    def test_quotes(self):
        sq = Styled("I have a [[ 'bold \"hair\"'|fg-red ]] face.")
        dq = Styled('I have a [[ "bold \'hair\'"|fg-red ]] face.')
        tq = Styled("""I have a [[ "bold 'hair'"|fg-red ]] face.""")
        self.assertCountEqual(sq._tokens, [(9, 35, u'bold "hair"', [u'fg-red'])])
        self.assertCountEqual(dq._tokens, [(9, 35, u"bold 'hair'", [u'fg-red'])])
        self.assertCountEqual(tq._tokens, [(9, 35, u"bold 'hair'", [u'fg-red'])])

    def test_style_error(self):
        with self.assertRaises(StyleError):
            Styled('I have a [[ "bold\'hair|fg-red ]] face')

    def test_invalid_style(self):
        with self.assertRaises(StyleError):
            Styled("I have a [[ 'good'|fg-sldjdlj ]]")

    def test_contatenate_styled(self):
        s1 = Styled("This is the [[ 'end'|bold ]]!")
        s2 = Styled(" when this [[ 'ends'|bold ]]!")
        s3 = s1 + s2
        self.assertIsInstance(s3, Styled)
        self.assertEqual(s3, s1 + s2)
        self.assertEqual(len(s3), len(s1) + len(s2))

    def test_concatenate_with_other(self):
        s1 = Styled("This is the [[ 'end'|bold ]]!")
        u1 = " And I will be finished."
        c1 = s1 + u1
        self.assertEqual(c1, s1 + u1)
        self.assertIsInstance(c1, Styled)
        u2 = "I will be finished..."
        s2 = Styled(" when this [[ 'ends'|bold ]]!")
        c2 = u2 + s2
        self.assertEqual(c2, u2 + s2)
        self.assertIsInstance(c2, Styled)

    def test_fg_colour(self):
        s = Styled("I have never seen a [[ 'white'|fg-white:bold ]] stallion.")
        self.assertIsInstance(s, Styled)

    def test_bg_colour(self):
        s = Styled("[[ 'White bold text on a black background.'|fg-black:bg-white:bold ]]")
        self.assertIsInstance(s, Styled)

    def test_catch_multiple_fgs(self):
        with self.assertRaises(StyleError):
            s = Styled("[[ 'useless'|fg-red:fg-orange ]]")

    def test_catch_multiple_bgs(self):
        with self.assertRaises(StyleError):
            s = Styled("[[ 'useless'|bg-red:bg-orange ]]")

    def test_catch_multiple_no_ends(self):
        with self.assertRaises(StyleError):
            s = Styled("[[ 'useless'|bg-red:no-end:no-end ]]")

    def test_clean_tokens(self):
        s = Styled("[[ 'some text'|bold:bold ]]")
        # self.assertItemsEqual(s._cleaned_tokens, [(0, 27, u"some text", [u'bold'])])
        self.assertCountEqual(s._cleaned_tokens, [(0, 27, u"some text", [u'bold'])])

    def test_iteration(self):
        s = Styled("There are some folks who [[ 'gasp'|fg-black:bg-deep_sky_blue_2:underlined:blink ]] at the thought "
                   "of the military. ")
        s += 'Woe unto them!'
        self.assertIsInstance(s, Styled)

    def test_unicode(self):
        s = Styled("We wish we had [[ 'red'|fg-red ]] faces")
        if sys.version_info[0] > 2:
            u_s = str(s)
        else:
            u_s = unicode(s)
        s_s = str(s)
        u_ = u"Thërę are some folkß who [[ 'gæsp'|fg-black:bg-deep_sky_blue_2:underlined:blink ]] at the " \
             u"thœught of the military. "
        e = Styled(u_)
        if sys.version_info[0] > 2:
            self.assertIsInstance(u_s, str)
        else:
            self.assertIsInstance(u_s, unicode)
        self.assertIsInstance(s_s, str)
        self.assertIsInstance(s, Styled)
        self.assertIsInstance(e, Styled)

    def test_concat_unicode(self):
        u_s = u"A unicode string"
        s = Styled("A [[ 'styled'|blink ]] string")
        c1 = u_s + s
        c2 = s + u_s
        if sys.version_info[0] > 2:
            self.assertIsInstance(u_s, str)
        else:
            self.assertIsInstance(u_s, unicode)
        self.assertIsInstance(c1, Styled)
        self.assertIsInstance(c2, Styled)

    def test_no_end(self):
        # lacks end
        u_ = u"[[ 'gæsp'|fg-black:bg-deep_sky_blue_2:underlined:blink:no-end ]]"
        e = Styled(u_)
        self.assertNotEqual(e[-3:], u'[0m'.format(ESC, END))
        # has end
        u_ = u"[[ 'gæsp'|fg-black:bg-deep_sky_blue_2:underlined:blink ]]"
        e = Styled(u_)
        self.assertEqual(e[-3:], u'[0m'.format(ESC, END))

    def test_yes_end(self):
        u_ = u"[[ 'wonder-woman'|fg-red:no-end ]] and this text will also be red [[ 'super-man'|fg-blue:yes-end ]]" \
             u"and this text will be normal"
        e = Styled(u_)
        # test that there is not styling at the end
        self.assertTrue(e[-1], u_[-1])
