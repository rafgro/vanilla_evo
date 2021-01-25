"""
Genome Module

Main Purpose
------------
Govern technical details of genome implementation
"""

from random import randint
from codon import new_codon, generate_genome_nonrandom, copy_genome


class Genome:
    """
    Class containing a single diploid (!) genome and operations on it

    Attributes
    ----------
    sequence_A : numpy array of int16
        First copy of genome sequence
    sequence_B : numpy array of int16
        Second copy of genome sequence

    Methods
    -------
    haploid()
        Return one of the sequences
    mutate(n=1)
        Change single ints n times
    expand(n=1)
        Expand sequence by n ints
    """

    def __init__(self, seqA=None, seqB=None, cod_seqA=None, cod_seqB=None):
        if cod_seqA is not None:
            self.sequence_A = copy_genome(cod_seqA)
            self.sequence_B = copy_genome(cod_seqB)
        else:
            self.sequence_A = generate_genome_nonrandom(seqA)
            self.sequence_B = generate_genome_nonrandom(seqB)

    def __str__(self):
        return '[' + self.sequence_A + ',' \
            + self.sequence_B + ']'

    def min_length(self):
        """Return shortest length of sequuence
        """
        return min(len(self.sequence_A)-1, len(self.sequence_B)-1)

    def haploid(self):
        """Return one of the sequences for offspring
        """
        if randint(0, 1) == 0:
            return self.sequence_A
        return self.sequence_B

    def expand(self, n=1):
        """Expand the sequence by n random bits
        """
        new_part = [new_codon() for _ in range(n)]

        self.sequence_A = generate_genome_nonrandom(
            self.sequence_A.tolist() + new_part
        )
        self.sequence_B = generate_genome_nonrandom(
            self.sequence_B.tolist() + new_part
        )
