"""
    Pastoral - A naive Python poetry generator
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

import random
import re
from poetry.util.pluralizer import pluralize

def randbool(): return random.randint(0, 1) == 0

class Pastoral:
    def __init__(self, wordhoard):
        self.wordhoard = wordhoard

    def maybe_describe(self, noun):
        return self.describe(noun) if randbool() else noun

    def maybe_define(self, noun):
        return self.define(noun) if randbool() else self.indefine(noun)

    def describe(self, noun):
        return random.choice(self.wordhoard['adjectives']) + " " + noun

    # Use definite article or possessive pronoun
    def define(self, noun):
        return random.choice(["the", "my", "your", "his", "her"]) + " " + noun

    # use indefinite article
    def indefine(self, noun):
        return "a " + noun if re.search('^[^aeiou]', noun) else "an " + noun

    def choose_subject(self, nouns, is_singular):
        return (self.maybe_define(self.maybe_describe(random.choice(nouns)))\
            if is_singular else pluralize(self.maybe_describe(random.choice(nouns)))).capitalize()

    def choose_object(self, nouns):
        return self.maybe_define(random.choice(nouns))\
            if randbool() else pluralize(random.choice(nouns)) + " " + self.make_prepositional_phrase()

    def make_prepositional_phrase(self):
        return random.choice(self.wordhoard['prepositions']) + " " + self.maybe_define(random.choice(self.wordhoard['sights']))

    def choose_verb(self, verbs, is_singular):
        return pluralize(random.choice(verbs)) if is_singular else random.choice(verbs)

    def you(self): return "You " + random.choice(self.wordhoard['intransitive'])

    def subject_verb_object(self, a, b):
        is_singular = randbool()
        return " ".join([
            self.choose_subject(self.wordhoard[a], is_singular),
            self.choose_verb(self.wordhoard['transitive'], is_singular),
            self.choose_object(self.wordhoard[b])])

    def interlude(self):
        random.shuffle(self.wordhoard['imperative'])
        return "    --" + ", ".join(self.wordhoard['imperative'][:3]) + " " +\
               self.make_prepositional_phrase()

    def __str__(self):
        return self.you() + '\n' + self.subject_verb_object('sights', 'sounds') + '\n' +\
               self.subject_verb_object('sights', 'sounds') + '\n' +\
               self.subject_verb_object('sights', 'sounds') + '\n' +\
               (self.interlude() + '\n' if random.randint(1, 3) == 1 else "")

