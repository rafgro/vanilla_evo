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
    for p in population.individuals:
        # getting diploid frequency from all individuals
        for i, L in enumerate(p.genome.sequence_A.iterdecode(dcode)):
            if i >= len(occurences_of_1s):
                continue
            if L == '1':
                occurences_of_1s[i] += 0.5
        for i, L in enumerate(p.genome.sequence_B.iterdecode(dcode)):
            if i >= len(occurences_of_1s):
                continue
            if L == '1':
                occurences_of_1s[i] += 0.5
    # calculating actual frequency stats, in place
    frequencies = [o / no_of_genomes for o in occurences_of_1s]
    # finish
    return {
        'No_of_genomes': no_of_genomes,
        'Avg_length': float(round(avg_length, 2)),
        'Frequencies': [float(round(f, 1)) for f in frequencies],
    }
