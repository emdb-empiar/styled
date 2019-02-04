# -*- coding: utf-8 -*-
from __future__ import print_function

import re

ESC = u'\033'
# ESC = u'\xb1'
# ESC = u'\e'

STYLES = {
    u'bold': u"1",
    u'underlined': u"4",
    u'red': u'38;5;1',
    u'blink': u"5",
    u'reverse': u"7",
    u"green": u"38;5;2",
    u"yellow": u"38;5;3",
    u"blue": u"38;5;4",
    u"magenta": u"38;5;5",
    u"cyan": u"38;5;6",
    u"light_gray": u"38;5;7",
    u"dark_gray": u"38;5;8",
    u"light_red": u"38;5;9",
    u"light_green": u"38;5;10",
    u"light_yellow": u"38;5;11",
    u"light_blue": u"38;5;12",
    u"light_magenta": u"38;5;13",
    u"light_cyan": u"38;5;14",

}

END = u'{}[0m'.format(ESC)


class Styled(str):
    pattern = re.compile(r".*?(?P<pattern>[[][[].*?[|].*?[]][]]).*?")
    styled_text = re.compile(r".*?[[][[].*?'(?P<text>.*?)'[|](?P<styles>(\w+[:]?)+).*?[]][]].*")

    # todo: make plain and styled readonly attributes that are only set at construction time
    def __new__(cls, s, *args, **kwargs):
        obj = super(Styled, cls).__new__(cls, s)
        # format string using args and kwargs
        cls._plain = obj.format(*args, **kwargs)
        # extract tokens
        cls._tokens = obj._find_tokens(cls._plain)
        # transform text with tokens and styles
        cls._styled = obj._transform(cls._plain, cls._tokens)
        cls._unstyled = obj._transform(cls._plain, cls._tokens, apply=False)
        # cls.finds = cls.parse_styles(cls._plain)
        return obj

    def __init__(self, s, *args, **kwargs):
        super(Styled, self).__init__(s)

    @staticmethod
    def transform(token):
        """Static method that converts tokens into styled text"""
        start, end, text, styles = token
        s = u''
        for style in styles:
            s += u'{}[{}m'.format(ESC, STYLES[style])
        return u'{}{}{}'.format(s, text, END)

    @classmethod
    def _transform(cls, plain, tokens, apply=True):
        """Transform the whole string into a styled string"""
        i = 0
        sss = u''
        for token in tokens:
            start, end, text, styles = token
            if apply:
                sss += plain[i:start] + cls.transform(token)
            else:
                sss += plain[i:start] + text
            i = end
        sss += plain[i:]
        return sss

    @classmethod
    def _find_tokens(cls, string):
        """Find all style tokens in the string"""
        tokens = list()
        index = 0
        pos = 0
        while True:
            string = string[index:]
            result = cls.pattern.match(string)
            if not result:  # or not result2:
                break
            find = result.group(u'pattern')
            result2 = cls.styled_text.match(find)
            text = result2.group(u'text')
            styles = result2.group(u'styles').split(u':')
            t_ = (result.start() + pos + (result.end() - len(find)), result.end() + pos, text, styles)
            tokens.append(
                t_,
            )
            index = result.end()
            pos += index
        return tokens

    def __len__(self):
        return len(self._unstyled)

    # @classmethod
    # def parse_styles(cls, string):
    #     finds = list()
    #     index = 0
    #     pos = 0
    #     while True:
    #         # print('string = ', string)
    #         string = string[index:]
    #         result = cls.pattern.match(string)
    #         # result2 = cls.styled_text.match(string)
    #         if not result:  # or not result2:
    #             break
    #         find = result.group('pattern')
    #         result2 = cls.styled_text.match(find)
    #         text = result2.group('text')
    #         # text = result.group('text')
    #         styles = result2.group('styles').split(':')
    #         # styles = result.group('styles').split(':')
    #         f_ = (result.start() + pos + (result.end() - len(find)), result.end() + pos, text, styles)
    #         # print(f_)
    #         finds.append(
    #             f_,
    #         )
    #         index = result.end()
    #         pos += index
    #         # print()
    #
    #     def transform(find):
    #         _, __, text, styles = find
    #         s = ''
    #         for style in styles:
    #             s += '{}[{}m'.format(ESC, STYLES[style])
    #         return '{}{}{}'.format(s, text, END)
    #
    #     i = 0
    #     sss = ''
    #     for find in finds:
    #         a, b, c, d = find
    #         sss += cls._plain[i:a] + transform(find)
    #         print(find, transform(find))
    #         i = b
    #     sss += cls._plain[i:]
    #     print(sss)
    #
    #     return finds
