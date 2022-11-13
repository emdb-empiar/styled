[![PyPI version](https://badge.fury.io/py/styled.svg)](https://badge.fury.io/py/styled) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/styled.svg) [![Coverage Status](https://coveralls.io/repos/github/emdb-empiar/styled/badge.svg?branch=master)](https://coveralls.io/github/emdb-empiar/styled?branch=master) [![Build Status](https://travis-ci.org/emdb-empiar/styled.svg?branch=master)](https://travis-ci.org/emdb-empiar/styled)

# Introduction

Welcome to `styled`, a simple Python package that makes a breeze of writing beautiful text to the terminal. 
The main innovation behind `styled` is the dead-simple user interface which does away with the user's need to know 
anything other than the style names. Behind the scenes `styled` handles everything to keep 
your styles consistent and redundant and informing you when you have made formatting errors.

`styled` was borne out of the frustration encountered in using other packages which muddle the boundary between
_user-space_ and _design-space_. The user should be free to be a _user_, and it is the _designer's_ job to hide the 
implementation behind a simple user interface that facilitates the user's task. This is what I've tried to do. If I have 
failed to live up to this please let me know. I'm sure together we can come up with something better.

## Getting Started

To get it from `PyPI` use

```bash
pip install styled
```

It's best to do this in a virtual environment.

```bash
# anaconda/miniconda
conda create -n styled python
source activate styled
pip install styled

# virtualenv
virtualenv /path/to/env/styled -p /path/to/python
source /path/to/envs/styled/bin/activate
pip install styled

```

Using `styled` is easy. Try this out in your Python console.

```shell
>>> from styled import Styled
>>> s = Styled("We are [[ 'bold'|bold ]] men!")
>>> print(s)
We are bold men!
```

You can perform string formatting _directly_ in the constructor.

```shell
>>> s = Styled("There were up to [[ '{}'|bold:fg-red ]] people who handed over themselves to the \
[[ '{police}'|fg-black:bg-red:bold ]].", 24, police='policia')
>>> print(s)
There were up to 24 people who handed over themselves to the policia.
```

You have to delimit the text you want to style with `[[ ... ]]` then make sure that the following _three (3)_ conditions hold:

* separate the text from the styles with a pipe (`|`),
* quote the text part with either a pair of single (`'...'`) or double (`"..."`) quotes, then 
* separate each style with a colon (`:`)

There are _three (3)_ types of styles:

* _text styling_ such as `bold`, `blink`, `underlined` etc.
* *foreground colours*, such as `fg-red`,
* *background colours*, such as `bg-blue`.

If you want to style an extended piece of text you can use a special additional style marker (`no-end`) indicating to 
continue the styling for as long as possible. This can be useful if you want to style a long stretch of text.

```shell
>>> s = Styled("There were up to [[ '{}'|bold:fg-red:no-end ]] people who handed over themselves to the \
[[ '{police}'|fg-black:bg-red:bold ]].", 24, police='policia')
>>> print(s)
There were up to 24 people who handed over themselves to the policia.
``` 

The above example will have all the text until the next marker affected by the red foreground styling. You can also 
manually enforce an end marker by using `yes-end` as a style. By default, all style markers will terminate on the 
text to be styled. So, for example

```shell
>>> # an example of a terminating end marker
>>> s = Styled("There were up to [[ '{}'|bold:fg-red:no-end ]] people who handed over themselves [[ ''|yes-end ]] to the \
[[ '{police}'|fg-black:bg-red:bold ]].", 24, police='policia')
>>> print(s)
There were up to 24 people who handed over themselves to the policia.
``` 

will suspend red foreground at the end of the word 'themselves'.

You can only have one foreground and one background colour. Ignoring this produces a `StyleError`

```shell
>>> from styled import Styled
>>> s = Styled("There were up to [[ '{}'|bold:fg-red:fg-blue ]] people who handed over themselves to the [[ '{police}'|fg-black:bg-red:bold ]].", 24, police='policia')
Traceback (most recent call last):
  File "/Users/pkorir/miniconda2/envs/styled/lib/python2.7/site-packages/IPython/core/interactiveshell.py", line 2878, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-3-0993b680f88b>", line 1, in <module>
    s = Styled("There were up to [[ '{}'|bold:fg-red:fg-blue ]] people who handed over themselves to the [[ '{police}'|fg-black:bg-red:bold ]].", 24, police='policia')
  File "/Users/pkorir/PycharmProjects/styled/styled/styled.py", line 55, in __init__
    self._validate(self._tokens)
  File "/Users/pkorir/PycharmProjects/styled/styled/styled.py", line 156, in _validate
    raise StyleError(u"Multiple foreground styles for text '{}': {}".format(text, ', '.join(styles)))
StyleError: Multiple foreground styles for text '24': bold, fg-red, fg-blue
```

Inputting an invalid `style` also raises a `StyleError`

```shell
>>> s = Styled("This just can't just [[ 'go'|underline ]] on forever! ")
Traceback (most recent call last):
  File "/Users/pkorir/miniconda2/envs/styled/lib/python2.7/site-packages/IPython/core/interactiveshell.py", line 2878, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-4-528d6d2ac4f4>", line 1, in <module>
    s = Styled("This just can't just [[ 'go'|underline ]] on forever! ")
  File "/Users/pkorir/PycharmProjects/styled/styled/styled.py", line 59, in __init__
    self._styled = self._transform(self._plain, self._cleaned_tokens)
  File "/Users/pkorir/PycharmProjects/styled/styled/styled.py", line 99, in _transform
    styled += plain[i:start] + self.transform(token)
  File "/Users/pkorir/PycharmProjects/styled/styled/styled.py", line 87, in transform
    raise StyleError(u"Unknown style '{}'".format(style_))
StyleError: Unknown style 'underline'
```

(In case you're wondering, it should have been `underlined` not `underline`.)

![Viewing the colour palette](colours.png) "Colour Palette"

![Viewing the formatting options](formats.png) "Formatting Options"

![Trying your hand out of a string of formatted text](try.png) "Trying out a formatted string"

## Concatenation

Concatenating a normal string and a `Styled` string produces a `Styled` string, which is a subclass of string. 
Internally, though, everything is a Unicode string.

```shell
>>> s = Styled("This just can't just [[ 'go'|underlined ]] on forever! ")
>>> u = "She shouted back!"
>>> print(type(s + u))
<class 'styled.styled.Styled'>
>>> print(type(u + s))
<class 'styled.styled.Styled'>
>>> s += "Gloria!"
>>> print(type(s))
<class 'styled.styled.Styled'>
```

## Validation

The process of generating the output involves some validation - to check that styles are sane. At present,
only multiple fore- and background colours are checked. This will be expanded as needed.

## Cleaning Styles

In addition to validation, styles are cleaned. Cleaning ensures that the final set of styles is non-redundant.

```shell
>>> s = Styled("It takes enormous [[ 'courage'|bold:bold:bold ]] to admit that you're wrong.")
>>> s._tokens
[(19, 49, u'courage', [u'bold', u'bold', u'bold'])]
>>> s._cleaned_tokens
[(19, 49, u'courage', [u'bold'])]
```

## Aspirations?

When I grow up I want to have my own Python string declaration like so:

```shell
# hey! I'm a styled string
s = s"You have to [[ 'believe'|fg-red ]] it to [[ 'see'|fg-green ]] it!"
```

## Special Thanks

To the following people

* Dimitris Zlatanidis (for the inspiration and resources in his package `colored` available at <https://gitlab.com/dslackw/colored>)
* Cesare Catavitello (for being the _first_ user)