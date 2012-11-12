"""
    Wordhoard - A JSON-backed word pile
"""

__author__    = 'Doug Hurst'
__email__     = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__   = "BSD"

import json

class Wordhoard:
    def __init__(self, filename):
        self.w = json.loads(open(filename).read())

    def __getattr__(self, item):
        return self.w[item]