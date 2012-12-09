# coding: utf-8
"""
    Smarter English pluralization
    mostly from "Dive into Python" by Mark Pilgrim
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"
__all__ = ['RandomChooser', 'ExhaustiveChooser']

import random


class RandomChooser(object):
    """Uses 'random' to make decisions."""
    def bool(self):
        return random.randint(0, 1) == 0

    def range(self, min, max):
        return random.randint(min, max)

    def choose(self, coll):
        return random.choice(coll)

    def sample(self, coll, count):
        return random.sample(coll, count)


class ExhaustiveChooser(RandomChooser):
    """Will only pick the same word once.

    Once the list is exhausted, it resets. Uses the 'set' mechanism.

    """
    def __init__(self):
        self.chosen = set()

    def choose(self, coll):
        if len(set(coll) - self.chosen) == 0:
            self.chosen = self.chosen - set(coll)
            subcoll = coll
        else:
            subcoll = list(set(coll) - self.chosen)

        choice = random.choice(subcoll)

        self.chosen = self.chosen | {choice}
        return choice
