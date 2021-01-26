"""
Goals:
[v] write simplest possible evolutionary computation code
[ ] compare use of lists - numpy - numba - cuda

Results:
0.4238421s with numpy
"""

import timeit
import numpy as np
from statistics import mean


# coding constants
MIN_CODON, MAX_CODON = 0, 1
DICT_CODON = {0: 0.2, 1: 0.8}  # codon vs fitness


def found_population():
    # create 5 genomes of length 10
    return np.random.randint(low=MIN_CODON, high=MAX_CODON, size=(5, 10))


# numpy 5x longer than lists
def assess_fitness(population, fit_dict):
    # measure fit of each genome
    return (population * 0.8).sum(axis=1)


def mutate(population, howmany, rand1, rand2, seed):
    # just substitutions
    for a,o in enumerate(population):
        for b in range(howmany):
            o[rand1[seed+a+b]] = rand2[seed+a+b]


def select(population, fitness, cutout):
    # cutting out low fitness ones
    mask = np.ones(len(population), dtype=bool)
    mask[[i for i,o in enumerate(population) if fitness[i] < cutout]] = False
    return population[mask]


def grow_population(population):
    # exponentially grow population, each has two offspring
    return np.array([
        o.copy() for _ in range(2) for o in population
    ])


# pseudorandom array indexes
rand1 = np.random.randint(low=0, high=10, size=(1000,))
# pseudorandom substitution mutations
rand2 = np.random.randint(low=MIN_CODON, high=MAX_CODON+1, size=(1000,))


def run():
    global rand1, rand2
    population = found_population()
    for seed in range(15):
        fitness = assess_fitness(population, DICT_CODON)
        # print(f'Mean fit: {round(mean(fitness),2)} | Size: {len(fitness)}')
        mutate(population, 1, rand1, rand2, seed*10)
        population = select(population, fitness, cutout=mean(fitness)*0.95)
        population = grow_population(population)


if __name__ == '__main__':
    run()
    print(timeit.timeit('run()', number=100, globals=globals()))
