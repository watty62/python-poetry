# python-poetry - Naïve poetry generators for Python 2.6+
[![Build Status](https://secure.travis-ci.org/dalanhurst/python-poetry.png)](http://travis-ci.org/dalanhurst/python-poetry)

Currently I've only implemented a generator which uses a static dictionary,
based loosely on "Taroko Gorge" by Nick Montfort (@nickmontfort). More robust
things will come, surely.

## Running "One" (with random chooser)
    >>> import json
    >>> from jinja2 import Environment, PackageLoader
    >>> from poetry.one import *
    >>> from poetry.util.chooser import *
    >>> env = Environment(loader=PackageLoader('poetry', 'templates'))
    >>> poem = One(RandomChooser(), json.loads(open("resources/pastoral.json").read()))
    >>> print(template.render({'poem': poem.generate_stanzas(), 'title': None}))

## Running "One" (with exhaustive chooser)
    >>> poem = One(ExhaustiveChooser(), json.loads(open("resources/pastoral.json").read()))

## Sample "One" with "resources/pastoral.json"

    You halt
    Your gray harvest answers snappings toward that warm crop
    His kudzu moves hands
    This gray wet twig pulls oaks

    Fields illumine my oak
    Your bird quells my indigo grass
    My tractor quells mewlings with his wet maple

    His indigo grass gurgles barkings with crops
    This curved moon throws a curved grass
    Red seeds move that wet rabbit

    This moonrise red tractor quells maples
    Lightnings answer tractors
    Orange tractors quell his orange rumbling toward rabbits
        --quake, thirst, will toward cracklings and then

    You listen