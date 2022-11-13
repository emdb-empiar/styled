# -*- coding: utf-8 -*-

__version__ = u'0.3.0'

try:
    from styled import Styled, StyleError
    from assets import STYLE_NAMES, FG_COLOURS, BG_COLOURS, ESC, END, COLOURS
except ImportError:
    from .styled import Styled, StyleError
    from .assets import STYLE_NAMES, FG_COLOURS, BG_COLOURS, ESC, END, COLOURS

__all__ = [
    u'Styled', u'StyleError', u'STYLE_NAMES',
    u'FG_COLOURS', u'BG_COLOURS', u'END', u'ESC', u'COLOURS'
]
