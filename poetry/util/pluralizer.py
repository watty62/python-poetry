"""
    Smarter English pluralization
    mostly from "Dive into Python" by Mark Pilgrim
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

import re

def pluralization_rules():
    rules = (
        ("[sxz]$", "$", "es"),
        ("[^aeioudgkprt]h$", "$", "es"),
        ("[^aeiou]y$", "y$", "ies"),
        ("$", "$", "s"))
    for pattern, search, replace in rules:
        yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)

def pluralize(noun):
    for applyRule in pluralization_rules():
        result = applyRule(noun)
        if result: return result
