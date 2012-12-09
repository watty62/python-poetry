# coding: utf-8
"""
    Smarter English pluralization
    mostly from "Dive into Python" by Mark Pilgrim
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"
__all__ = ['RandomChooser']

import random


class RandomChooser(object):
    def bool(self):
        return random.randint(0, 1) == 0

    def range(self, min, max):
        return random.randint(min, max)

    def choose(self, list):
        return random.choice(list)

    def sample(self, list, count):
        return random.sample(list, count)
