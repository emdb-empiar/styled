from __future__ import print_function

import re


STYLES = {
    'bold': "1",
    'underlined': "4",
    'red': '38;5;1',
    'blink': "5",
    'reverse': "7",
    "green": "38;5;2",
    "yellow": "38;5;3",
    "blue": "38;5;4",
    "magenta": "38;5;5",
    "cyan": "38;5;6",
    "light_gray": "38;5;7",
    "dark_gray": "38;5;8",
    "light_red": "38;5;9",
    "light_green": "38;5;10",
    "light_yellow": "38;5;11",
    "light_blue": "38;5;12",
    "light_magenta": "38;5;13",
    "light_cyan": "38;5;14",

}

END = '\033[0m'

class Styled(str):
    pattern = re.compile(r".*?(?P<pattern>[[][[].*?[|].*?[]][]]).*?")
    styled_text = re.compile(r".*?[[][[].*?'(?P<text>.*?)'[|](?P<styles>(\w+[:]?)+).*?[]][]].*")

    # todo: make plain and styled readonly attributes that are only set at construction time
    def __new__(cls, s, *args, **kwargs):
        obj = str.__new__(cls, s)
        # complete string by adding format args and kwargs
        cls.plain = obj.format(*args, **kwargs)
        # extract tokens

        # transform text with tokens and styles
        #
        # cls.styled = cls.parse_style(cls.plain)
        cls.finds = cls.parse_styles(cls.plain)
        return obj

    # @classmethod
    # def parse_style(cls, plain):
    #     styled_obj = plain
    #     result = cls.pattern.match(plain)
    #     print(result.groupdict())
    #     print(result.start(), result.end())
    #     try:
    #         result = cls.pattern.match(plain[result.end():])
    #         print(result.groupdict())
    #         print(result.start(), result.end())
    #         print(plain[result.end():])
    #     except AttributeError:
    #         pass
    #     return styled_obj

    @classmethod
    def _find_tokens(cls):
        tokens = list()
        index = 0
        pos = 0
        while True:
            string = string[index:]
            result = cls.pattern.match(string)
            # result2 = cls.styled_text.match(string)
            if not result:  # or not result2:
                break
            find = result.group('pattern')
            result2 = cls.styled_text.match(find)
            text = result2.group('text')
            # text = result.group('text')
            styles = result2.group('styles').split(':')
            # styles = result.group('styles').split(':')
            f_ = (result.start() + pos + (result.end() - len(find)), result.end() + pos, text, styles)
            # print(f_)
            tokens.append(
                f_,
            )
            index = result.end()
            pos += index
            # print()

    @classmethod
    def parse_styles(cls, string):
        finds = list()
        index = 0
        pos = 0
        while True:
            # print('string = ', string)
            string = string[index:]
            result = cls.pattern.match(string)
            # result2 = cls.styled_text.match(string)
            if not result: # or not result2:
                break
            find = result.group('pattern')
            result2 = cls.styled_text.match(find)
            text = result2.group('text')
            # text = result.group('text')
            styles = result2.group('styles').split(':')
            # styles = result.group('styles').split(':')
            f_ = (result.start() + pos + (result.end() - len(find)), result.end() + pos, text, styles)
            # print(f_)
            finds.append(
                f_,
            )
            index = result.end()
            pos += index
            # print()

        def transform(find):
            _, __, text, styles = find
            s = ''
            for style in styles:
                s += '\033[{}m'.format(STYLES[style])
            return '{}{}{}'.format(s, text, END)

        i = 0
        sss = ''
        for find in finds:
            a, b, c, d = find
            sss += cls.plain[i:a] + transform(find)
            print(find, transform(find))
            i = b
        sss += cls.plain[i:]
        print(sss)


        return finds
