"""
Simulation module for assessing fitness
Alfa 02: random fitness assignment

Main Purpose
------------
Test and baseline only
"""

from random import randint


def evaluate(genome):
    """ Return fitness given a genome class """
    # 1.0-2.0 fit
    fit = 1.0 + 0.1 * randint(1, 10)
    # finish
    return fit
