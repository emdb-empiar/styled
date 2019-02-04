# Introduction

Welcome to `styled`, a simple Python package to make writing beautiful text to the terminal effortless. 
The main innovation behind `styled` is the dead-simple user interface keeping the user in user space without ever 
having to know anything more than the names of the colours. Behind the scenes `styled` handles everything to keep 
your styles consistent and redundant informing you when you have made formatting errors.

`styled` was borne out of the frustration encountered in using other packages which muddle the boundary between
_user-space_ and _design-space_. The user should be a _user_ and the _designer_ is there to hide the implementation
behind a clean UI that respects the user's time. This is what I've tried to do. If I have failed to live up to this 
do let me know. I'm sure together we can come up with something better

## Getting Started

Using `styled` is easy. Watch this:

```python
from styled import Styled
s = Styled("We are [[ 'bold'|bold ]] men!")
print(s)
```

Use format parameters _directly_ in the constructor.

```python
s = Styled("There were up to [[ '{}'|bold:fg-red ]] people who handed over themselves to the [[ '{police}'|fg-black:bg-red:bold ]].", 24, police='policia')
print(s)
```

## Concatenation
## Validation
## Cleaning Styles

# Aspirations?

When I grow up I want to have my own Python string declaration like so:

```python
# hey! I'm a styled string
s = s"You have to [[ 'believe'|fg-red ]] it to [[ 'see'|fg-green ]] it!"
```