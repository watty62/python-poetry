"""
    Smarter pluralization
    mostly from Dive into Python by Mark Pilgrim
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

import re

def pluralization_rules(language):
    with open('resources/pluralization_rules.%s.csv' % language, 'r') as file:
        for line in file:
            pattern, search, replace = line.split()
            yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)

def pluralize(noun, language = 'en'):
    for applyRule in pluralization_rules(language):
        result = applyRule(noun)
        if result: return result
