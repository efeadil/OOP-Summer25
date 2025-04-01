"""
Python Style Guide

This guide follows PEP 8 conventions with examples of good and bad practices.
"""

# Naming Conventions
# Bad Example
VarName = 42  # wrong: Variable names should be in snake_case

# Good Example
var_name = 42  # correct: Use snake_case for variable names


# Indentation
# Bad Example
def bad_indentation():
    x = 1
        y = 2  # wrong: Inconsistent indentation
    return x + y

# Good Example
def good_indentation():
    x = 1
    y = 2  # correct: Proper indentation with 4 spaces per level
    return x + y


# Spacing
# Bad Example
x= 10+5  # wrong: Missing spaces around operators

# Good Example
x = 10 + 5  # correct: Spaces around operators for readability


# Line Length
# Bad Example
long_variable_name = "This is an example of a very long line that exceeds 79 characters which is not recommended."  # wrong

# Good Example
long_variable_name = (
    "This is an example of a long line that is split correctly."
)  # correct


# Function Definitions
# Bad Example
def badFunction( x,y ):
    return(x+y) # wrong: No spaces after commas, bad parentheses spacing

# Good Example
def good_function(x, y):
    return x + y  # correct: Proper spacing and naming


# Imports
# Bad Example
import sys, os  # wrong: Multiple imports on one line

# Good Example
import sys
import os  # correct: One import per line


# Docstrings
# Bad Example
def no_docstring():
    pass  # wrong: Function should have a docstring

# Good Example
def with_docstring():
    """This function does nothing but follows good style."""
    pass  # correct
