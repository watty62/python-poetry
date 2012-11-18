# python-poetry - A naive poetry generator library for Python 2.6+
[![Build Status](https://secure.travis-ci.org/dalanhurst/python-poetry.png)](http://travis-ci.org/dalanhurst/python-poetry)

Currently I've only implemented a generator which uses a static dictionary, based loosely on "Taroko Gorge" by
Nick Montfort (@nickmontfort). More robust things will come, surely.

## Running
    >>> import json
    >>> import random
    >>> from poetry.pastoral import Pastoral
    >>> p = Pastoral(json.loads(open("resources/pastoral.json").read()))
    >>> for stanza in p.get_stanzas(): print(stanza)

## Sample "Pastoral"

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