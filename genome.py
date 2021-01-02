"""
Genome Module

Main Purpose
------------
Govern technical details of genome implementation
"""

from random import randint
from codon import Codon, generate_genome_nonrandom, copy_genome


class Genome:
    """
    Class containing a single diploid (!) genome and operations on it

    Attributes
    ----------
    sequence_A : list of codons
        First copy of genome sequence
    sequence_B : list of codons
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

    def mutate(self, n=1):
        """Change n times randomly single codons in both sequences
        Disclaimer: generally should not be used
        """
        for _ in range(n):
            locus = randint(0, len(self.sequence_A)-1)
            self.sequence_A[locus].mutate()
            self.sequence_B[locus].mutate()

    def expand(self, n=1):
        """Expand the sequence by n random bits
        """
        for _ in range(n):
            new_part = Codon()
            new_part_copy = Codon(init=new_part.val)
            self.sequence_A.append(new_part)
            self.sequence_B.append(new_part_copy)
