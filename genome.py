"""
Genome Module

Main Purpose
------------
Govern technical details of genome implementation
"""

from random import randint


class Genome:
    """
    Class containing a single diploid (!) genome and operations on it

    Attributes
    ----------
    sequence_A : list of ints
        First copy of genome sequence in ints
    sequence_B : list of ints
        Second copy of genome sequence in ints

    Methods
    -------
    haploid()
        Return one of the sequences
    mutate(n=1)
        Change single ints n times
    expand(n=1)
        Expand sequence by n ints
    """

    def __init__(self, seqA=None, seqB=None):
        self.sequence_A = seqA.copy()
        self.sequence_B = seqB.copy()

    def __str__(self):
        return '[' + self.sequence_A.to01() + ',' \
            + self.sequence_B.to01() + ']'

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

    def mutate(self, n=1):
        """Change n times randomly single bits in both sequences
        Disclaimer: generally should not be used
        """
        for _ in range(n):
            locus = randint(0, len(self.sequence_A)-1)
            self.sequence_A.invert(locus)
            self.sequence_B.invert(locus)

    def expand(self, n=1):
        """Expand the sequence by n random bits
        """
        for _ in range(n):
            new_part = randint(0, 1)
            self.sequence_A.append(new_part)
            self.sequence_B.append(new_part)
