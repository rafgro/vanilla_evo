"""
Statistics Module

Main Purpose
------------
Characterize genomes and population, in order to allow
precise governance of the process, as well as saving objective
results of experiments
"""

from statistics import mean
from codon import MAX_CODON


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
    # getting data for frequency stats, position by position
    avg_length_corrected = int(avg_length)+1
    occurences = [[0.0 for _ in range(0, MAX_CODON+1)]
                  for _ in range(avg_length_corrected)]
    heterozygotes = [0 for _ in range(avg_length_corrected)]
    homozygotes = [0 for _ in range(avg_length_corrected)]
    for p in population.individuals:
        # getting diploid frequency from all individuals
        for i, L in enumerate(zip(
                p.genome.sequence_A,
                p.genome.sequence_B)):
            if i >= len(occurences):
                continue
            # note occurences
            occurences[i][L[0].val] += 0.5
            occurences[i][L[1].val] += 0.5
            # note zygosity
            if L[0] == L[1]:
                homozygotes[i] += 1
            else:
                heterozygotes[i] += 1
    # calculating actual frequency stats, in place
    frequencies = [sum([v*i for i, v in enumerate(o)])
                   / no_of_genomes for o in occurences]
    heterozygote_freq = [o / no_of_genomes for o in heterozygotes]
    # preparing average genome
    average_genome = [0 for _ in range(avg_length_corrected)]
    for i, what in enumerate(frequencies):
        average_genome[i] = round(what)
    # TODO: correct H-W calculation
    # calculating hardy-weinberg and fst
    expected_freq_hwe = []
    for _, f in enumerate(frequencies):
        # allele frequencies: p and q
        # then hwe is: p^2, 2pq, q^2
        p = f  # that's biological terminology
        q = MAX_CODON - f  # or q = 1.0 - f
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
        'Avg_genome': ''.join([str(o) for o in average_genome]),
        'No_of_genomes': no_of_genomes,
        'Avg_length': float(round(avg_length, 2)),
        'Frequencies': [float(round(f, 2)) for f in frequencies],
        'Heterozygotes': [float(round(f, 2)) for f in heterozygote_freq],
        # 'Fst': [float(round(f, 2)) for f in inbreeding_coeff],
    }
