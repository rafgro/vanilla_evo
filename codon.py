"""
Codon Module

Main Purpose
------------
Define and restrict codon content
Plus provide few util funcs around codons
"""

from random import randint


MIN_CODON = 0  # minimum value of a codon
MAX_CODON = 5  # maximum value of a codon, not inclusive


class Codon:
    """
    Class containing a single codon, restricted int number
    Abstracts away all direct modifications and reading (!) of codons

    Attributes
    ----------
    val : int
        Actual codon content

    Methods
    -------
    mutate()
        Random change of value in the bounded value
    """

    def __init__(self, init=None):
        if init is not None and init >= MIN_CODON and init <= MAX_CODON:
            self.val = init
        else:
            self.val = randint(MIN_CODON, MAX_CODON)

    def mutate(self):
        self.val = randint(MIN_CODON, MAX_CODON)

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other

    def __hash__(self):
        return hash(self.val)


def generate_genome_random(n):
    """ Return list of random codons with length=n """
    return [Codon() for _ in range(0, n)]


def generate_genome_nonrandom(thelist):
    """ Return list of codons following provided list """
    if thelist is not None:
        return [Codon(init=n) for n in thelist]
    else:
        return []


def copy_genome(thelist):
    """ Return new list based on a list of codons """
    return [Codon(init=n.val) for n in thelist]
