# python-poetry - A naive poetry generator library for Python 2.6+
[![Build Status](https://secure.travis-ci.org/dalanhurst/python-poetry.png)](http://travis-ci.org/dalanhurst/python-poetry)

Currently I've only implemented a generator which uses a static dictionary, based loosely on "Taroko Gorge" by
Nick Montfort (@nickmontfort). More robust things will come, surely.

## Running
    >>> import json
    >>> import random
    >>> from poetry.pastoral import Pastoral
    >>> p = Pastoral(json.loads(open("resources/pastoral.json").read()))
    >>> for i in range(random.randint(2, 4)): print(p)

## Sample "Pastoral"

    You listen
    The tree rakes her farmhouse
    Bales eek clickety-clackings toward stars
    Gray rabbits unveil barns
        --thirst, fight, rage over your crackling

    You jump
    Her barn rakes ladders
    The tractor answers this wet moonset nest
    The sunrise river makes this wet bubbling for maples
        --thirst, bite, scream over the gray snapping

    You halt
    The straight nest moves lightnings
    Her rabbit orders this white whirring over walnuts
    Moonrise fireflies light creakings for rivers
        --hunger, rage, strive with crunchings

    You listen
    Moonrise moons throw this young green seed
    That moonrise black oak orders twigs
    This warm wet ladder ruins thunderings under kudzus
        --will, scream, fight over thunderings