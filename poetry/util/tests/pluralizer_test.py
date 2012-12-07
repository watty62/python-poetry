__author__ = 'Doug Hurst'
__email__ = 'dalan.hurst@gmail.com'
__copyright__ = "Copyright 2012"
__license__ = "BSD"

from poetry.util.pluralizer import *

def test_pluralization_sibilant():
    assert pluralize("kiss") == "kisses"
    assert pluralize("phase") == "phases"
    assert pluralize("dish") == "dishes"
    assert pluralize("massage") == "massages"
    assert pluralize("witch") == "witches"
    assert pluralize("judge") == "judges"


def test_pluralization_voiceless_consonant():
    assert pluralize("lap") == "laps"
    assert pluralize("cat") == "cats"
    assert pluralize("clock") == "clocks"
    assert pluralize("cuff") == "cuffs"
    assert pluralize("death") == "deaths"


def test_pluralization_normal():
    assert pluralize("boy") == "boys"
    assert pluralize("girl") == "girls"
    assert pluralize("chair") == "chairs"


def test_pluralization_nouns_in_o():
    assert pluralize("hero") == "heroes"
    assert pluralize("potato") == "potatoes"
    assert pluralize("volcano") == "volcanos"


def test_pluralization_nouns_in_o_latin_origin():
    assert pluralize("canto") == "cantos"
    assert pluralize("hetero") == "heteros"
    assert pluralize("photo") == "photos"
    assert pluralize("zero") == "zeros"
    assert pluralize("piano") == "pianos"
    assert pluralize("portico") == "porticos"
    assert pluralize("pro") == "pros"
    assert pluralize("quarto") == "quartos"
    assert pluralize("kimono") == "kimonos"


def test_pluralization_nouns_in_y():
    assert pluralize("cherry") == "cherries"
    assert pluralize("lady") == "ladies"
    assert pluralize("day") == "days"
    assert pluralize("monkey") == "monkeys"


def test_pluralization_near_regular():
    assert pluralize("bath") == "baths"
    assert pluralize("mouth") == "mouths"
    assert pluralize("calf") == "calves"
    assert pluralize("leaf") == "leaves"
    assert pluralize("knife") == "knives"
    assert pluralize("life") == "lives"
    assert pluralize("house") == "houses"
    assert pluralize("moth") == "moths"
    assert pluralize("proof") == "proofs"


def test_pluralization_identities():
    assert pluralize("bison") == "bison"
    assert pluralize("buffalo") == "buffalo"
    assert pluralize("deer") == "deer"
    assert pluralize("fish") == "fish"
    assert pluralize("moose") == "moose"
    assert pluralize("pike") == "pike"
    assert pluralize("sheep") == "sheep"
    assert pluralize("salmon") == "salmon"
    assert pluralize("trout") == "trout"
    assert pluralize("swine") == "swine"
    assert pluralize("plankton") == "plankton"


def test_pluralization_ablaut():
    assert pluralize("foot") == "feet"
    assert pluralize("goose") == "geese"
    assert pluralize("louse") == "lice"
    assert pluralize("man") == "men"
    assert pluralize("mouse") == "mice"
    assert pluralize("tooth") == "teeth"
    assert pluralize("woman") == "women"