__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

import json
from poetry.one import *


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

def test_one_maybe_describe():
    one = One('', MockChooserA(), wordhoard)
    assert one._maybe_describe('baseball') == 'big baseball'
    one = One('', MockChooserB(), wordhoard)
    assert one._maybe_describe('baseball') == 'baseball'

def test_one_determine():
    one = One('', MockChooserA(), wordhoard)
    assert one._determine('baseball') == 'the baseball'
    one = One('', MockChooserC(), wordhoard)
    assert one._determine('baseball') == 'this big baseball'
    one = One('', MockChooserD(), wordhoard)
    assert one._determine('baseball') == 'my baseball'

def test_one_attribute():
    one = One('', MockChooserA(), wordhoard)
    assert one._attribute('baseball') == 'big baseball'

def test_one_demonstrate():
    one = One('', MockChooserA(), wordhoard)
    assert one._demonstrate('baseball') == 'this big baseball'
    one = One('', MockChooserE(), wordhoard)
    assert one._demonstrate('baseball') == 'that small baseball'

def test_one_possess():
    one = One('', MockChooserA(), wordhoard)
    assert one._possess('baseball') == 'my baseball'
    one = One('', MockChooserE(), wordhoard)
    assert one._possess('baseball') == 'your baseball'
    one = One('', MockChooserF(), wordhoard)
    assert one._possess('baseball') == 'his baseball'
    one = One('', MockChooserG(), wordhoard)
    assert one._possess('baseball') == 'her baseball'

def test_one_definite_article():
    one = One('', MockChooserA(), wordhoard)
    assert one._articulate('baseball') == 'the baseball'

def test_one_indefinite_article():
    one = One('', MockChooserB(), wordhoard)
    assert one._articulate('animal') == 'an animal'
    assert one._articulate('baseball') == 'a baseball'

def test_one_make_prepositional_phrase():
    one = One('', MockChooserA(), wordhoard)
    assert one._make_prepositional_phrase(['baseball']) == 'on the big baseball'

def test_one_choose_subject():
    one = One('', MockChooserA(), wordhoard)
    assert one._choose_subject(['baseball'], True) == 'The big baseball'
    one = One('', MockChooserB(), wordhoard)
    assert one._choose_subject(['baseball'], True) == 'A baseball'
    assert one._choose_subject(['baseball'], False) == 'Baseballs'

def test_one_choose_object():
    one = One('', MockChooserA(), wordhoard)
    assert one._choose_object(['baseball']) == 'the big baseball'
    one = One('', MockChooserB(), wordhoard)
    assert one._choose_object(['baseball']) == 'baseballs'

def test_one_choose_verb():
    one = One('', MockChooserA(), wordhoard)
    assert one._choose_verb(['throw'], True) == 'throws'
    assert one._choose_verb(['throw'], False) == 'throw'

def test_one_you():
    one = One('', MockChooserA(), wordhoard)
    assert one._you() == 'You succeed'

def test_one_subject_verb_object():
    one = One('', MockChooserA(), wordhoard)
    assert one._subject_verb_object() == 'The big field swings the big field'
    one = One('', MockChooserB(), wordhoard)
    assert one._subject_verb_object() == 'Fields swing cracks on fields'

def test_one_interlude():
    one = One('', MockChooserA(), wordhoard)
    assert one._interlude() == '    --fight on the big crack and then'
    one = One('', MockChooserB(), wordhoard)
    assert one._interlude() == '    --fight on cracks and then'