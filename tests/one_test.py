__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

import unittest
from poetry.one import One


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

class OneTest(unittest.TestCase):
    def test_maybe_describe(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._maybe_describe('baseball'), 'big baseball')
        one = One(MockChooserB(), wordhoard)
        self.assertEquals(one._maybe_describe('baseball'), 'baseball')
    
    def test_determine(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._determine('baseball'), 'the baseball')
        one = One(MockChooserC(), wordhoard)
        self.assertEquals(one._determine('baseball'), 'this big baseball')
        one = One(MockChooserD(), wordhoard)
        self.assertEquals(one._determine('baseball'), 'my baseball')
    
    def test_attribute(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._attribute('baseball'), 'big baseball')
    
    def test_demonstrate(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._demonstrate('baseball'), 'this big baseball')
        one = One(MockChooserE(), wordhoard)
        self.assertEquals(one._demonstrate('baseball'), 'that small baseball')
    
    def test_possess(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._possess('baseball'), 'my baseball')
        one = One(MockChooserE(), wordhoard)
        self.assertEquals(one._possess('baseball'), 'your baseball')
        one = One(MockChooserF(), wordhoard)
        self.assertEquals(one._possess('baseball'), 'his baseball')
        one = One(MockChooserG(), wordhoard)
        self.assertEquals(one._possess('baseball'), 'her baseball')
    
    def test_definite_article(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._articulate('baseball'), 'the baseball')
    
    def test_indefinite_article(self):
        one = One(MockChooserB(), wordhoard)
        self.assertEquals(one._articulate('animal'), 'an animal')
        self.assertEquals(one._articulate('baseball'), 'a baseball')
    
    def test_make_prepositional_phrase(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._make_prepositional_phrase(['baseball']), 'on the big baseball')
    
    def test_choose_subject(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._choose_subject(['baseball'], True), 'the big baseball')
        one = One(MockChooserB(), wordhoard)
        self.assertEquals(one._choose_subject(['baseball'], True), 'a baseball')
        self.assertEquals(one._choose_subject(['baseball'], False), 'baseballs')
    
    def test_choose_object(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._choose_object(['baseball']), 'the big baseball')
        one = One(MockChooserB(), wordhoard)
        self.assertEquals(one._choose_object(['baseball']), 'baseballs')
    
    def test_choose_verb(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._choose_verb(['throw'], True), 'throws')
        self.assertEquals(one._choose_verb(['throw'], False), 'throw')
    
    def test_you(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._you(), 'You succeed')
    
    def test_subject_verb_object(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._subject_verb_object(), 'the big field swings the big field')
        one = One(MockChooserB(), wordhoard)
        self.assertEquals(one._subject_verb_object(), 'fields swing cracks on fields')
    
    def test_interlude(self):
        one = One(MockChooserA(), wordhoard)
        self.assertEquals(one._interlude(), '    --fight on the big crack and then')
        one = One(MockChooserB(), wordhoard)
        self.assertEquals(one._interlude(), '    --fight on cracks and then')
