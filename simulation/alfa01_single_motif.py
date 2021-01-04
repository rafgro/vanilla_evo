"""
Simulation module for assessing fitness
Alfa 01: simple single motif analysis

Main Purpose
------------
Test and baseline only
"""


def evaluate(genome):
    """ Return fitness given a genome class """
    # base fitness
    fit = 1.0
    # promote 1001 starting motif
    matches = 0
    if genome.sequence_A[0] == 1:
        matches += 1
    if genome.sequence_A[1] == 0:
        matches += 1
    if genome.sequence_A[2] == 0:
        matches += 1
    if genome.sequence_A[3] == 1:
        matches += 1
    fit += matches * 0.1
    # finish
    return fit
