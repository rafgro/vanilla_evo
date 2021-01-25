"""
Mutation Module

Main Purpose
------------
Introduce primary source of variability within genomes
"""

import numba
import numpy as np
from random import randint
from codon import new_codon
from numba.core import types
from numba.typed import Dict


def pydict_to_numbadict(adict):
    d = Dict.empty(
        key_type=types.unicode_type,
        value_type=types.float64,
    )
    for k, v in adict.items():
        d[k] = v
    return d


@numba.jit(nopython=True)
def mutate(agenome, frequency_table):
    """ Change sequence of codons in a random way

    Parameters
    ----------
    agenome: Genome class
        Diploid genome to modify IN PLACE
    frequency_table: dictionary
        Should have frequencies in percentage of
            singles - single substitutions anywhere
            expansions - expansion at any side of the genome
            deletions - single deletions anywhere
    """
    # correcting frequency table
    for k, v in frequency_table.items():
        frequency_table[k] *= 1000
    # calculations of local frequencies and actual events
    no_of_substitutions = 0
    no_of_expansions = 0
    no_of_deletions = 0
    for _ in range(len(agenome.sequence_A)):
        dice_roll = randint(1, 100000)
        if dice_roll < frequency_table['singles']:
            no_of_substitutions += 1
        if dice_roll < frequency_table['expansions']:
            no_of_expansions += 1
        if dice_roll < frequency_table['deletions']:
            no_of_deletions += 1

    # single substitutions
    for _ in range(no_of_substitutions):
        locus = randint(0, agenome.min_length())
        if randint(0, 1) == 0:  # diploid substitution
            agenome.sequence_A[locus] = new_codon()
            agenome.sequence_B[locus] = new_codon()
        else:  # haploid substituion
            if randint(0, 1) == 0:
                agenome.sequence_A[locus] = new_codon()
            else:
                agenome.sequence_B[locus] = new_codon()

    # single deletions
    mask_A = np.ones((len(agenome.sequence_A),), dtype=np.bool_)
    mask_B = np.ones((len(agenome.sequence_B),), dtype=np.bool_)
    for _ in range(no_of_deletions):
        locus = randint(0, agenome.min_length())
        if randint(0, 1) == 0:  # diploid deletion
            mask_A[locus] = False
            mask_B[locus] = False
        else:  # haploid deletion
            if randint(0, 1) == 0:
                mask_A[locus] = False
            else:
                mask_B[locus] = False
    agenome.sequence_A = agenome.sequence_A[mask_A]
    agenome.sequence_B = agenome.sequence_B[mask_B]

    # expansions
    agenome.expand(no_of_expansions)
    # finish
