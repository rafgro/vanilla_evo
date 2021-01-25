"""
Codon Module

Main Purpose
------------
Define and restrict codon content
Provide few util funcs around codons
"""

import numpy as np
import numba
from random import randint


MIN_CODON = 0  # minimum value of a codon
MAX_CODON = 5  # maximum value of a codon, not inclusive


@numba.jit(nopython=True)
def generate_genome_random(n):
    """ Return list of random codons with length=n """
    return np.random.randint(low=MIN_CODON, high=MAX_CODON, size=n)


# @numba.jit(nopython=True)  # numba postponed re: reflected lists
def generate_genome_nonrandom(thelist):
    """ Return list of codons following provided list """
    if thelist is None:
        return np.array([], dtype=np.int16)
    else:
        return np.array(thelist, dtype=np.int16)


def new_codon():
    """ Return int inside min-max constants """
    return randint(MIN_CODON, MAX_CODON)


def copy_genome(thelist):
    """ Return new list based on a list of codons """
    return np.array(thelist, dtype=np.int16, copy=True)
