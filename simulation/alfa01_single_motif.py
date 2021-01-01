"""
Simulation module for assessing fitness
Alfa 01: simple single motif analysis

Main Purpose
------------
Test and baseline only
"""
from bitarray import bitarray


def evaluate(genome):
    """ Return fitness given a genome class """
    # base fitness
    fit = 1.1
    # promote 1001 motif
    matches = genome.sequence_A.search(bitarray('1001'))
    fit += len(matches) * 1.0
    if fit > 2.2: fit = 2.2
    # finish
    return fit
