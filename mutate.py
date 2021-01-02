"""
Mutation Module

Main Purpose
------------
Introduce primary source of variability within genomes
"""

from random import randint
from codon import Codon


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
            agenome.sequence_A[locus].mutate()
            agenome.sequence_B[locus].mutate()
        else:  # haploid substituion
            if randint(0, 1) == 0:
                agenome.sequence_A[locus].mutate()
            else:
                agenome.sequence_B[locus].mutate()
    # single deletions
    for _ in range(no_of_deletions):
        locus = randint(0, agenome.min_length())
        if randint(0, 1) == 0:  # diploid deletion
            del agenome.sequence_A[locus]
            del agenome.sequence_B[locus]
        else:  # haploid deletion
            if randint(0, 1) == 0:
                del agenome.sequence_A[locus]
            else:
                del agenome.sequence_B[locus]
    # expansions
    for _ in range(no_of_expansions):
        expansion = Codon()
        expansion_copy = Codon(init=expansion.val)
        agenome.sequence_A.append(expansion)
        agenome.sequence_B.append(expansion_copy)
    # finish
