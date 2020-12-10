"""
Statistics Module

Main Purpose
------------
Characterize genomes and population, in order to allow
precise governance of the process, as well as saving objective
results of experiments
"""

from bitarray import bitarray
from statistics import mean


def describe_statistics(population):
    """ Return genetic statistics about population

    Parameters
    ----------
    population: class Population
        Whole class, read-only

    Mechanism
    ---------
    Expects class with list of individuals with genomes inside
    """
    # basic stats
    no_of_genomes = len(population.individuals)
    avg_length = mean([len(p.genome.sequence_A)+len(p.genome.sequence_B)
                       for p in population.individuals]) / 2  # 2*mean hence /2
    # decoding dict for bitarray
    dcode = {'0': bitarray('0'), '1': bitarray('1')}
    # getting data for frequency stats, position by position
    occurences_of_1s = [0.0 for _ in range(int(avg_length)+1)]
    heterozygotes_of_1s = [0 for _ in range(int(avg_length)+1)]
    homozygotes_of_1s = [0 for _ in range(int(avg_length)+1)]
    homozygotes_of_0s = [0 for _ in range(int(avg_length)+1)]
    for p in population.individuals:
        # getting diploid frequency from all individuals
        for i, L in enumerate(zip(
                p.genome.sequence_A.iterdecode(dcode),
                p.genome.sequence_B.iterdecode(dcode))):
            if i >= len(occurences_of_1s):
                continue
            if L[0] == '1' and L[1] == '1':
                homozygotes_of_1s[i] += 1
                occurences_of_1s[i] += 1.0
            elif L[0] == '0' and L[1] == '0':
                homozygotes_of_0s[i] += 1
            else:
                heterozygotes_of_1s[i] += 1
                occurences_of_1s[i] += 0.5
    # calculating actual frequency stats, in place
    frequencies = [o / no_of_genomes for o in occurences_of_1s]
    heterozygote_freq = [o / no_of_genomes for o in heterozygotes_of_1s]
    # homozygote1_freq = [o / no_of_genomes for o in homozygotes_of_1s]
    # homozygote0_freq = [o / no_of_genomes for o in homozygotes_of_0s]
    # calculating hardy-weinberg and fst
    expected_freq_hwe = []
    for _, f in enumerate(frequencies):
        # allele frequencies: p and q
        # then hwe is: p^2, 2pq, q^2
        p = f  # that's biological terminology
        q = 1.0 - f
        expected_freq_hwe.append(
            {'homo1': p**2, 'hetero': 2*p*q, 'homo0': q**2}
        )
    inbreeding_coeff = []
    for i, e in enumerate(expected_freq_hwe):
        # fst: (hetero expected / observed) / expected
        if heterozygote_freq[i] == 0 or e['hetero'] == 0:
            inbreeding_coeff.append(0)  # avoiding division by zero
            continue
        inbreeding_coeff.append(
            (e['hetero'] - heterozygote_freq[i]) / e['hetero']
        )
    # finish
    return {
        'No_of_genomes': no_of_genomes,
        'Avg_length': float(round(avg_length, 2)),
        'Frequencies': [float(round(f, 2)) for f in frequencies],
        'Heterozygotes': [float(round(f, 2)) for f in heterozygote_freq],
        'Fst': [float(round(f, 2)) for f in inbreeding_coeff],
    }
