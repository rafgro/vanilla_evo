"""
Recombination Module

Main Purpose
------------
Increase variability of genomes via crossing-over events
"""

import numpy as np
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
        locus = randint(1, agenome.min_length()-1)
        if randint(0, 1) == 0:  # from left to middle
            new_seq_A = np.concatenate((agenome.sequence_B[0:locus], agenome.sequence_A[locus:]), axis=0)
            new_seq_B = np.concatenate((agenome.sequence_A[0:locus], agenome.sequence_B[locus:]), axis=0)
        else:  # from right to middle
            new_seq_A = np.concatenate((agenome.sequence_A[0:locus], agenome.sequence_B[locus:]), axis=0)
            new_seq_B = np.concatenate((agenome.sequence_B[0:locus], agenome.sequence_A[locus:]), axis=0)
        agenome.sequence_A = new_seq_A
        agenome.sequence_B = new_seq_B
