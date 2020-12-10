"""
Recombination Module

Main Purpose
------------
Increase variability of genomes via crossing-over events
"""

from random import randint


def crossover(agenome, events=1):
    """ Recombine two haploid parts of a genome

    Parameters
    ----------
    agenome: Genome class
        Diploid genome to modify IN PLACE
    events: integer
        Number of crossing over events
    """
    for _ in range(events):
        locus = randint(0, agenome.min_length())
        if randint(0, 1) == 0:  # from left to middle
            agenome.sequence_A[0:locus], agenome.sequence_B[0:locus] = agenome.sequence_B[0:locus], agenome.sequence_A[0:locus]
        else:  # from right to middle
            agenome.sequence_A[locus:], agenome.sequence_B[locus:] = agenome.sequence_B[locus:], agenome.sequence_A[locus:]
