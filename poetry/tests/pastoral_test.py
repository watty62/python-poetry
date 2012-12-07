__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

import json
from poetry.pastoral import *


class MockChooserA(object):
    def bool(self):
        return True

    def range(self, min, max):
        return min

    def choose(self, list):
        return list[0]

    def sample(self, list, count):
        return list[:count]


class MockChooserB(MockChooserA):
    def bool(self):
        return False


class MockChooserC(MockChooserA):
    def range(self, min, max):
        return min + 1


class MockChooserD(MockChooserA):
    def range(self, min, max):
        return min + 2


class MockChooserE(MockChooserA):
    def choose(self, list):
        return list[1]


class MockChooserF(MockChooserA):
    def choose(self, list):
        return list[2]


class MockChooserG(MockChooserA):
    def choose(self, list):
        return list[3]


wordhoard = {
    "adjectives": ["big", "small"],
    "imperatives": ["fight"],
    "intransitives": ["succeed"],
    "prepositions": ["on"],
    "sights": ["field"],
    "sounds": ["crack"],
    "transitives": ["swing"]
}

def test_pastoral_maybe_describe():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._maybe_describe('baseball') == 'big baseball'
    pastoral = Pastoral(MockChooserB(), wordhoard)
    assert pastoral._maybe_describe('baseball') == 'baseball'

def test_pastoral_determine():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._determine('baseball') == 'the baseball'
    pastoral = Pastoral(MockChooserC(), wordhoard)
    assert pastoral._determine('baseball') == 'this big baseball'
    pastoral = Pastoral(MockChooserD(), wordhoard)
    assert pastoral._determine('baseball') == 'my baseball'

def test_pastoral_attribute():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._attribute('baseball') == 'big baseball'

def test_pastoral_demonstrate():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._demonstrate('baseball') == 'this big baseball'
    pastoral = Pastoral(MockChooserE(), wordhoard)
    assert pastoral._demonstrate('baseball') == 'that small baseball'

def test_pastoral_possess():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._possess('baseball') == 'my baseball'
    pastoral = Pastoral(MockChooserE(), wordhoard)
    assert pastoral._possess('baseball') == 'your baseball'
    pastoral = Pastoral(MockChooserF(), wordhoard)
    assert pastoral._possess('baseball') == 'his baseball'
    pastoral = Pastoral(MockChooserG(), wordhoard)
    assert pastoral._possess('baseball') == 'her baseball'

def test_pastoral_definite_article():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._articulate('baseball') == 'the baseball'

def test_pastoral_indefinite_article():
    pastoral = Pastoral(MockChooserB(), wordhoard)
    assert pastoral._articulate('animal') == 'an animal'
    assert pastoral._articulate('baseball') == 'a baseball'

def test_pastoral_make_prepositional_phrase():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._make_prepositional_phrase(['baseball']) == 'on the big baseball'

def test_pastoral_choose_subject():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._choose_subject(['baseball'], True) == 'The big baseball'
    pastoral = Pastoral(MockChooserB(), wordhoard)
    assert pastoral._choose_subject(['baseball'], True) == 'A baseball'
    assert pastoral._choose_subject(['baseball'], False) == 'Baseballs'

def test_pastoral_choose_object():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._choose_object(['baseball']) == 'the big baseball'
    pastoral = Pastoral(MockChooserB(), wordhoard)
    assert pastoral._choose_object(['baseball']) == 'baseballs'

def test_pastoral_choose_verb():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._choose_verb(['throw'], True) == 'throws'
    assert pastoral._choose_verb(['throw'], False) == 'throw'

def test_pastoral_you():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._you() == 'You succeed'

def test_pastoral_subject_verb_object():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._subject_verb_object() == 'The big field swings the big field'
    pastoral = Pastoral(MockChooserB(), wordhoard)
    assert pastoral._subject_verb_object() == 'Fields swing cracks on fields'

def test_pastoral_interlude():
    pastoral = Pastoral(MockChooserA(), wordhoard)
    assert pastoral._interlude() == '    --fight on the big crack and then\n\nYou succeed'
    pastoral = Pastoral(MockChooserB(), wordhoard)
    assert pastoral._interlude() == '    --fight on cracks and then\n\nYou succeed'