"""
Goals:
[v] write simplest possible evolutionary computation code
[ ] compare use of lists - numpy - numba - cuda

Results:
0.5547708s for lists
"""

import timeit
from random import randint
from statistics import mean


# coding constants
MIN_CODON, MAX_CODON = 0, 1
DICT_CODON = {0: 0.2, 1: 0.8}  # codon vs fitness


def found_population():
    # create 5 genomes of length 10
    return [
        [randint(MIN_CODON, MAX_CODON-1) for _ in range(10)] for _ in range(5)
    ]


def assess_fitness(population):
    # measure fit of each genome
    return [
        sum([DICT_CODON[f] for f in o]) for o in population
    ]


def mutate(population, howmany):
    # just substitutions
    for o in population:
        for _ in range(howmany):
            o[randint(0, len(o)-1)] = randint(MIN_CODON, MAX_CODON)


def select(population, fitness, cutout):
    # cutting out low fitness ones
    mask = [True if fitness[i] > cutout else False for i,o in enumerate(population)]
    return [o for i,o in enumerate(population) if mask[i] is True]


def grow_population(population):
    # exponentially grow population, each has two offspring
    return [
        o.copy() for _ in range(2) for o in population
    ]


def run():
    population = found_population()
    for _ in range(15):
        fitness = assess_fitness(population)
        # print(f'Mean fit: {round(mean(fitness),2)} | Size: {len(fitness)}')
        mutate(population, howmany=1)
        population = select(population, fitness, cutout=mean(fitness)*0.95)
        population = grow_population(population)


if __name__ == '__main__':
    run()
    print(timeit.timeit('run()', number=100, globals=globals()))
