"""
    Pastoral - A naive Python poetry generator
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

import json
import random
import re

def randbool(): return random.randint(0, 1) == 0


def uppercase_first(str): return str[0].upper() + str[1:]


class Pastoral:
    def __init__(self, wordhoard: dict):
        self.wordhoard = wordhoard

    def pluralize(self, noun):
        return noun + "s"

    def articulate(self, noun):
        return "the " + noun\
            if randbool() else "a " + noun\
                if re.search('^[^aeiou]', noun) else "an " + noun

    def choose_subject(self, nouns, is_singular):
        return uppercase_first(self.articulate(random.choice(nouns)))\
            if is_singular else uppercase_first(self.pluralize(random.choice(nouns)))

    def choose_object(self, nouns):
        return self.articulate(random.choice(nouns))\
            if randbool() else self.pluralize(random.choice(nouns)) + " " + self.make_prepositional_phrase()

    def make_prepositional_phrase(self):
        return random.choice(self.wordhoard['prepositions']) + " " + self.articulate(random.choice(self.wordhoard['sights']))

    def choose_verb(self, verbs, is_singular):
        return random.choice(verbs) + "s" if is_singular else random.choice(verbs)

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


if __name__ == "__main__":
    p = Pastoral(json.loads(open("resources/pastoral.json").read()))
    for i in range(random.randint(2, 4)):
        print(p)
