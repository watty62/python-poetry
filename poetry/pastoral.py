"""
    Pastoral - A naive Python poetry generator
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"
__all__ = ['Pastoral']

import random
import re
from poetry.util.pluralizer import pluralize


def randbool(): return random.randint(0, 1) == 0


class Pastoral:
    def __init__(self, wordhoard):
        self.wordhoard = wordhoard
        self.themes = {}

    def maybe_describe(self, noun):
        return self.attribute(noun) if randbool() else noun

    def determine(self, noun):
        return [
                self.articulate,
                self.demonstrate,
                self.possess
               ][random.randint(0, 2)](noun)

    # Use attributive adjective
    def attribute(self, noun):
        adjective = random.choice(self.wordhoard['adjectives'])
        if adjective in self.themes: self.themes[adjective] += 1
        else: self.themes[adjective] = 0
        return adjective + " " + noun

    # Use demonstrative
    def demonstrate(self, noun):
        return random.choice(["this", "that"]) + " " + self.attribute(noun)

    # Use possessive pronoun
    def possess(self, noun):
        return random.choice(["my", "your", "his", "her"]) + " " + noun

    # Use definite or indefinite article
    def articulate(self, noun):
        return (("the"
                 if randbool()
                 else ("a"
                       if re.search('^[^aeiou]', noun)
                       else "an"))
                + " "
                + noun)

    def choose_subject(self, nouns, is_singular):
        return (self.determine(self.maybe_describe(random.choice(nouns)))
                if is_singular
                else pluralize(self.maybe_describe(random.choice(nouns)))).capitalize()

    def choose_object(self, nouns):
        return (self.determine(self.maybe_describe(random.choice(nouns)))
                if randbool()
                else pluralize(random.choice(nouns)))

    def choose_verb(self, verbs, is_singular):
        verb = random.choice(verbs)

        if verb in self.themes: self.themes[verb] += 1
        else: self.themes[verb] = 0

        return pluralize(verb) if is_singular else verb

    def make_prepositional_phrase(self, objects):
        return (random.choice(self.wordhoard['prepositions'])
                + " "
                + self.choose_object(self.wordhoard[objects]))

    def you(self):
        return "You " + random.choice(self.wordhoard['intransitives'])

    def subject_verb_object(self):
        is_singular = randbool()
        return " ".join([
            self.choose_subject(self.wordhoard['sights'], is_singular),
            self.choose_verb(self.wordhoard['transitives'], is_singular),
            self.choose_object(self.wordhoard['sights'])
            if randbool()
            else (self.choose_object(self.wordhoard['sounds'])
                  + " "
                  + self.make_prepositional_phrase('sights'))
        ])

    def interlude(self):
        return ("    --" + ", ".join(random.sample(self.wordhoard['imperatives'], 3))
                + " " + self.make_prepositional_phrase('sounds')
                + " and then \n\n" + self.you())

    def get_stanzas(self):
        while 3 not in self.themes.values():
            if len(self.themes): stanza = []
            else: stanza = [self.you()]

            stanza.extend(map(lambda i: self.subject_verb_object(), range(3)))

            if 3 in self.themes.values(): stanza.append(self.interlude())
            else: stanza.append('')

            yield '\n'.join(stanza)


