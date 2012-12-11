# coding: utf-8
"""
    Collection of classes which use different strategies to subset a wordhoard.
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"
__all__ = ['RandomSampler', 'PassThruSampler']

import random as r


class PassThruSampler(object):
    def __init__(self, wordhoard):
        self.wordhoard = wordhoard

    def sample(self):
        return self.wordhoard


class RandomSampler(PassThruSampler):
    def sample(self):
        return dict(
            map(
                lambda x: (x[0], r.sample(x[1], r.randrange(3, len(x[1])))),
                self.wordhoard.items()
            )
        )
