# -*- coding: utf-8 -*-
"""Module defining :py:class:`styled.Styled` class

`Styled` objects are intended to operate just like strings
(some methods are yet to be defined e.g. `format()`.

"""
from __future__ import print_function

import re

from .assets import STYLE_NAMES, FG_COLOURS, BG_COLOURS, ESC, END


# todo: add other string interfaces e.g. format, etc.
#  to make a Styled object behave like a string

class StyleError(Exception):
    """Exception indicating a style error has occured"""
    pass


class Styled:
    """Main class that handles styled text and replaces markup with styles"""
    # matches styled text delimiter: ".*[[.*|.*]].*"
    pattern = re.compile(
        r".*?(?P<pattern>[\[][\[].*?[|].*?[\]][\]]).*?",
        re.UNICODE | re.DOTALL
    )
    # matches styled text and text styles: "[[ '<text>'|<styles> ]]"
    styled_text = re.compile(
        r".*?[\[][\[].*?[\"'](?P<text>.*?)[\"'][|]"
        r"(?P<styles>(\w+[:-]?)+).*?[\]][\]].*",
        re.UNICODE | re.DOTALL
    )

    def __init__(self, styled_string=None, *args, **kwargs):
        if isinstance(styled_string, str):
            self._s = styled_string
        elif isinstance(styled_string, bytes):
            self._s = styled_string.decode('utf-8')
        elif styled_string is None:
            self._s = ''
        else:
            raise ValueError(
                "Invalid input object of type {}".format(
                    type(styled_string)
                )
            )
        # bugfix: escape curly braces
        if re.search(r'.*?[{].*?[-].*?[}].*?', self._s):
            self._s = self._s.replace("{", "{{").replace("}", "}}")
        # format string using args and kwargs
        self._plain = self._s.format(*args, **kwargs)
        # extract tokens
        self._tokens = self._find_tokens(self.plain)
        # validate
        self._validate(self._tokens)
        # remove duplicates
        self._cleaned_tokens = self._clean(self._tokens)
        # transform text with tokens and styles
        self._styled = self._transform(self.plain, self._cleaned_tokens)
        # unstyled version for length inference
        self._unstyled = self._transform(
            self.plain, self._cleaned_tokens, invoke=False
        )

    @property
    def plain(self):
        """Unprocessed text with format params filled"""
        return self._plain

    @staticmethod
    def transform(token):
        """Static method that converts tokens into styled text"""
        _, __, text, styles = token
        styled_string = ''
        terminate = True
        for style in styles:
            pos = None
            try:
                pos, style_ = style.split('-')
            except ValueError:
                style_ = style
            try:
                if pos == 'fg':
                    styled_string += '{}[{}m'.format(ESC, FG_COLOURS(style_))
                elif pos == 'bg':
                    styled_string += '{}[{}m'.format(ESC, BG_COLOURS(style_))
                elif pos == 'no' and style_ == 'end':
                    terminate = False
                elif pos == 'yes' and style_ == 'end':
                    terminate = True
                else:
                    styled_string += '{}[{}m'.format(ESC, STYLE_NAMES[style_])
            except KeyError:
                raise StyleError("Unknown style '{}'".format(style_))
        if terminate:
            return '{}{}{}'.format(styled_string, text, END)
        return '{}{}'.format(styled_string, text)

    def _transform(self, plain, tokens, invoke=True):
        """Static method to transform the whole string into a styled string"""
        i = 0
        styled = ''
        for token in tokens:
            start, end, text, _ = token
            if invoke:
                styled += plain[i:start] + self.transform(token)
            else:
                styled += plain[i:start] + text
            i = end
        styled += plain[i:]
        return styled

    def _find_tokens(self, string):
        """Find all style tokens in the string"""
        tokens = list()
        index = 0
        pos = 0
        while True:
            string = string[index:]
            pattern = self.pattern.match(string)
            if not pattern:  # or not styled_text:
                break
            found_pattern = pattern.group('pattern')
            styled_text = self.styled_text.match(found_pattern)
            if not styled_text:
                raise StyleError(
                    "Invalid tokens in pattern {}".format(
                        found_pattern)
                )
            text = styled_text.group('text')
            styles = styled_text.group('styles').split(':')
            token = (
                pattern.start() + pos + (pattern.end() - len(found_pattern)),
                pattern.end() + pos, text, styles
            )
            tokens.append(
                token,
            )
            index = pattern.end()
            pos += index
        return tokens

    @staticmethod
    def _validate(tokens):
        """Validate styling

        * no multiple fgs or bgs
        """
        for _, __, text, styles in tokens:
            fgs = list()
            bgs = list()
            no_ends = list()
            other = list()
            for style in styles:
                pos = None
                try:
                    pos, style_ = style.split('-')
                except ValueError:
                    style_ = style
                if pos == 'fg':
                    fgs.append(style)
                elif pos == 'bg':
                    bgs.append(style)
                elif pos == 'no' and style_ == 'end':
                    no_ends.append(style_)
                else:
                    other.append(style)
            if len(fgs) > 1:
                raise StyleError(
                    "Multiple foreground styles for text '{}': {}".format(
                        text, ', '.join(styles)
                    )
                )
            if len(bgs) > 1:
                raise StyleError(
                    "Multiple background styles for text '{}': {}".format(
                        text, ', '.join(styles)
                    )
                )
            if len(no_ends) > 1:
                raise StyleError(
                    "Multiple no-ends for text '{}': {}".format(
                        text, ', '.join(styles)
                    )
                )

    @staticmethod
    def _clean(tokens):
        """Remove duplicates and sundry things"""
        cleaned_tokens = list()
        for start, end, text, styles in tokens:
            cleaned_tokens.append((start, end, text, list(set(styles))))
        return cleaned_tokens

    def __len__(self):
        return len(self._unstyled)

    # string handling
    def __bytes__(self):
        return self._styled.encode('utf-8')

    def __str__(self):
        return self._styled

    def __eq__(self, other):
        return self._unstyled == other

    def __add__(self, other):
        """styled + other"""
        if isinstance(other, Styled):
            return Styled(self.plain + other.plain)
        return Styled(self.plain + other)

    def __radd__(self, other):
        """other + styled"""
        return Styled(other + self.plain)

    def __getitem__(self, item):
        return self._styled[item]
