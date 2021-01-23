"""
Codon Module

Main Purpose
------------
Define and restrict codon content
Plus provide few util funcs around codons
"""

import numpy as np
import numba


MIN_CODON = 0  # minimum value of a codon
MAX_CODON = 5  # maximum value of a codon, not inclusive


@numba.jit(nopython=True)
def generate_genome_random(n):
    """ Return list of random codons with length=n """
    return np.random.randint(low=MIN_CODON, high=MAX_CODON, size=n)


@numba.jit(nopython=True)
def generate_genome_nonrandom(thelist):
    """ Return list of codons following provided list """
    return np.array(thelist, dtype=np.int16)


@numba.jit(nopython=True)
def copy_genome(thelist):
    """ Return new list based on a list of codons """
    return np.array(thelist, dtype=np.int16)
