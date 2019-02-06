# -*- coding: utf-8 -*-
from __future__ import print_function

import re
from .assets import COLOURS, STYLE_NAMES, FG_COLOURS, BG_COLOURS, ESC, END


class StyleError(Exception):
    def __init__(self, *args, **kwargs):
        super(StyleError, self).__init__(*args)


class Styled(str):
    pattern = re.compile(r".*?(?P<pattern>[[][[].*?[|].*?[]][]]).*?", re.UNICODE|re.DOTALL)
    styled_text = re.compile(r".*?[[][[].*?[\"'](?P<text>.*?)[\"'][|](?P<styles>(\w+[:-]?)+).*?[]][]].*", re.UNICODE|re.DOTALL)

    # todo: make plain and styled readonly attributes that are only set at construction time
    def __new__(cls, s=None, *args, **kwargs):
        if s is None:
            obj = super(Styled, cls).__new__(cls, u'')
        else:
            if isinstance(s, basestring):
                if isinstance(s, str):
                    obj = super(Styled, cls).__new__(cls, s.decode('utf-8'))
                elif isinstance(s, unicode):
                    obj = super(Styled, cls).__new__(cls, s)
            else:
                raise ValueError("Invalid input object of type {}".format(type(s)))
        # format string using args and kwargs
        cls._plain = obj.format(*args, **kwargs).decode('utf-8')
        # extract tokens
        cls._tokens = obj._find_tokens(cls._plain)
        # validate
        cls._validate(cls._tokens)
        # remove duplicates
        cls._cleaned_tokens = cls._clean(cls._tokens)
        # transform text with tokens and styles
        cls._styled = obj._transform(cls._plain, cls._cleaned_tokens)
        # unstyled version for length inference
        cls._unstyled = obj._transform(cls._plain, cls._cleaned_tokens, apply=False)
        return obj

    def __init__(self, s=None, *args, **kwargs):
        super(Styled, self).__init__(s)

    @staticmethod
    def transform(token):
        """Static method that converts tokens into styled text"""
        start, end, text, styles = token
        s = u''
        for style in styles:
            pos = None
            try:
                pos, style_ = style.split('-')
            except ValueError:
                style_ = style
            try:
                if pos == u'fg':
                    s += u'{}[{}m'.format(ESC, FG_COLOURS(style_))
                elif pos == u'bg':
                    s += u'{}[{}m'.format(ESC, BG_COLOURS(style_))
                else:
                    s += u'{}[{}m'.format(ESC, STYLE_NAMES[style_])
            except KeyError:
                raise StyleError(u"Unknown style '{}'".format(style_))
        return u'{}{}{}'.format(s, text, END)

    @classmethod
    def _transform(cls, plain, tokens, apply=True):
        """Transform the whole string into a styled string"""
        i = 0
        styled = u''
        for token in tokens:
            start, end, text, styles = token
            if apply:
                styled += plain[i:start] + cls.transform(token)
            else:
                styled += plain[i:start] + text
            i = end
        styled += plain[i:]
        return styled

    @classmethod
    def _find_tokens(cls, string):
        """Find all style tokens in the string"""
        tokens = list()
        index = 0
        pos = 0
        while True:
            string = string[index:]
            pattern = cls.pattern.match(string)
            if not pattern:  # or not styled_text:
                break
            found_pattern = pattern.group(u'pattern')
            styled_text = cls.styled_text.match(found_pattern)
            if not styled_text:
                raise StyleError(u"Invalid tokens in pattern {}".format(found_pattern))
            text = styled_text.group(u'text')
            styles = styled_text.group(u'styles').split(u':')
            t_ = (pattern.start() + pos + (pattern.end() - len(found_pattern)), pattern.end() + pos, text, styles)
            tokens.append(
                t_,
            )
            index = pattern.end()
            pos += index
        return tokens

    @classmethod
    def _validate(cls, tokens):
        """Validate styling

        * no multiple fgs or bgs
        """
        for start, end, text, styles in tokens:
            fgs = list()
            bgs = list()
            other = list()
            for style in styles:
                pos = None
                try:
                    pos, style_ = style.split('-')
                except ValueError:
                    style_ = style
                if pos == u'fg':
                    fgs.append(style)
                elif pos == u'bg':
                    bgs.append(style)
                else:
                    other.append(style)
            if len(fgs) > 1:
                raise StyleError(u"Multiple foreground styles for text '{}': {}".format(text, ', '.join(styles)))
            if len(bgs) > 1:
                raise StyleError(u"Multiple background styles for text '{}': {}".format(text, ', '.join(styles)))

    @classmethod
    def _clean(cls, tokens):
        """Remove duplicates and sundry things"""
        cleaned_tokens = list()
        for start, end, text, styles in tokens:
            cleaned_tokens.append((start, end, text, list(set(styles))))
        return cleaned_tokens

    def __len__(self):
        return len(self._unstyled)

    def __str__(self):
        return self._styled.encode('utf-8')

    def __unicode__(self):
        return self._styled

    def __eq__(self, other):
        return self._unstyled.encode('utf-8') == other

    def __add__(self, other):
        """styled + other"""
        if isinstance(other, Styled):
            return Styled(self._plain + other._plain)
        else:
            return Styled(self._plain + other)

    def __radd__(self, other):
        """other + styled"""
        if isinstance(other, Styled):
            return Styled(other._plain + self._plain)
        else:
            return Styled(other + self._plain)
