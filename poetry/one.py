# coding: utf-8
"""
    One - A naïve Python poetry generator

    Losely based on "Taroko Gorge" by Nick Montfort
    http://nickm.com/poems/taroko_gorge.html
"""

__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"
__all__ = ['One']

import re
from poetry.util.pluralizer import pluralize


class One(object):
    def __init__(self, chooser, wordhoard):
        self.chooser = chooser
        self.themes = {}
        self.wordhoard = wordhoard

    def _maybe_describe(self, noun):
        """Does a coin-flip, uses an (attributive) adjective if true.

        Keyword arguments:
            noun -- a string representing a noun or nominal phrase

        """
        return self._attribute(noun) if self.chooser.bool() else noun

    def _determine(self, noun):
        """Randomly chooses a determiner for the noun.

        Currently uses one of:
            an article,
            a demonstrative pronoun, or
            a possessive pronoun

        Keyword arguments:
            noun -- a string representing a noun or nominal phrase

        """
        return [
                self._articulate,
                self._demonstrate,
                self._possess
               ][self.chooser.range(0, 2)](noun)

    def _attribute(self, noun):
        """Prefixes an (attributive) adjective to the noun.

        Keyword arguments:
            noun -- a string representing a noun or nominal phrase

        """
        adjective = self.chooser.choose(self.wordhoard['adjectives'])
        if adjective in self.themes: self.themes[adjective] += 1
        else: self.themes[adjective] = 0
        return adjective + " " + noun

    def _demonstrate(self, noun):
        """Prefixes a demonstrative pronoun to the noun.

        Keyword arguments:
            noun -- a string representing a noun or nominal phrase

        """
        return self.chooser.choose(["this", "that"]) + " " + self._attribute(noun)

    def _possess(self, noun):
        """Prefixes a possessive pronoun to the noun.

        Keyword arguments:
            noun -- a string representing a noun or nominal phrase

        """
        return self.chooser.choose(["my", "your", "his", "her"]) + " " + noun

    def _articulate(self, noun):
        """Prefixes an article (definite or indefinite) to the noun.

        Keyword arguments:
            noun -- a string representing a noun or nominal phrase

        """
        return (("the"
                 if self.chooser.bool()
                 else ("a"
                       if re.search('^[^aeiou]', noun)
                       else "an"))
                + " "
                + noun)

    def _make_prepositional_phrase(self, objects):
        """Creates a prepositional phrase.

        Keyword arguments:
            objects -- a set of nouns from which to choose the phrase object

        """
        return (self.chooser.choose(self.wordhoard['prepositions'])
                + " "
                + self._choose_object(objects))

    def _choose_subject(self, nouns, is_singular):
        """Chooses a single noun from a list and optionally describes it.

        Keyword arguments:
            nouns -- a set of nouns from which to choose
            is_singular -- a boolean telling if the subject should be pluralized or not

        """
        return (self._determine(self._maybe_describe(self.chooser.choose(nouns)))
                if is_singular
                else pluralize(self._maybe_describe(self.chooser.choose(nouns)))).capitalize()

    def _choose_object(self, nouns):
        """Chooses a single noun from a list and optionally describes it.

        Keyword arguments:
            nouns -- a set of nouns from which to choose

        """
        return (self._determine(self._maybe_describe(self.chooser.choose(nouns)))
                if self.chooser.bool()
                else pluralize(self.chooser.choose(nouns)))

    def _choose_verb(self, verbs, is_singular):
        """Chooses a single verb from a list.

        Keyword arguments:
            verbs -- a set of verbs from which to choose
            is_singular -- a boolean telling if the verb should be pluralized or not

        """
        verb = self.chooser.choose(verbs)

        if verb in self.themes: self.themes[verb] += 1
        else: self.themes[verb] = 0

        return pluralize(verb) if is_singular else verb

    def _you(self):
        """Creates a simple 'You' + intransitive verb sentence."""
        return "You " + self.chooser.choose(self.wordhoard['intransitives'])

    def _subject_verb_object(self):
        """Creates a standard SVO sentence."""
        is_singular = self.chooser.bool()
        return " ".join([
            self._choose_subject(self.wordhoard['sights'], is_singular),
            self._choose_verb(self.wordhoard['transitives'], is_singular),
            self._choose_object(self.wordhoard['sights'])
            if self.chooser.bool()
            else (self._choose_object(self.wordhoard['sounds'])
                  + " "
                  + self._make_prepositional_phrase(self.wordhoard['sights']))
        ])

    def _interlude(self):
        """
        Creates an interlude which could join two sets of stanzas more-or-
        less seamlessly.
        """
        return ("    --" + ", ".join(self.chooser.sample(self.wordhoard['imperatives'], 3))
                + " " + self._make_prepositional_phrase(self.wordhoard['sounds'])
                + " and then")

    def _get_stanzas(self):
        """
        Yields stanzas until a 'theme' occurs. Currently a theme is defined as
        the repetition of a verb or noun phrase three times.
        """
        while 3 not in self.themes.values():
            if len(self.themes) == 0: stanza = [self._you()]
            else: stanza = []

            stanza.extend(map(lambda i: self._subject_verb_object(), range(3)))

            if 3 in self.themes.values(): stanza.extend([self._interlude(), '', self._you()])

            yield stanza

    def render(self, template):
        return template.render(title = None, poem = self._get_stanzas())

    def __str__(self):
        return reduce(lambda i,x: i + '\n'.join(x) + '\n\n', self._get_stanzas(), "")

