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
        ("^bison$", ".*", "bison"),
        ("^buffalo$", ".*", "buffalo"),
        ("^deer$", ".*", "deer"),
        ("^fish$", ".*",  "fish"),
        ("^moose$", ".*", "moose"),
        ("^pike$", ".*", "pike"),
        ("^sheep$", ".*", "sheep"),
        ("^salmon$", ".*", "salmon"),
        ("^trout$", ".*", "trout"),
        ("^swine$", ".*", "swine"),
        ("^plankton$", ".*", "plankton"),
        ("^foot$", ".*",  "feet"),
        ("^goose$", ".*",  "geese"),
        ("^louse$", ".*",  "lice"),
        ("^man$", ".*",  "men"),
        ("^mouse$", ".*",  "mice"),
        ("^tooth$", ".*",  "teeth"),
        ("^woman$", ".*",  "women"),
        ("^proof", ".*",  "proofs"),
        ("^hero", ".*",  "heroes"),
        ("^potato", ".*",  "potatoes"),
        ("[^f]fe?$", ".e?$", "ves"),
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
