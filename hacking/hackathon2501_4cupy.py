"""
Goals:
[v] write simplest possible evolutionary computation code
[ ] compare use of lists - numpy - numba - cuda

Results:
2.6306323s with cupy
"""

import timeit
import cupy as cp


# coding constants
MIN_CODON, MAX_CODON = 0, 1


def found_population():
    # create 5 genomes of length 10
    return cp.random.randint(low=MIN_CODON, high=MAX_CODON, size=(5, 10))


def assess_fitness(population):
    # measure fit of each genome
    return (population * 0.8).sum(axis=1)


def mutate(population, howmany, rand1, rand2, seed):
    # just substitutions
    for a,o in enumerate(population):
        for b in range(howmany):
            o[rand1[seed+a+b]] = rand2[seed+a+b]


def select(population, fitness, cutout):
    # cutting out low fitness ones
    mask = cp.ones((len(population),), dtype=cp.bool_)
    for i,o in enumerate(population):
        if fitness[i] < cutout:
            mask[i] = False
    return population[mask]


def grow_population(population):
    # exponentially grow population, each has two offspring
    return cp.concatenate((population, population), axis=0)


# pseudorandom array indexes
rand1 = cp.random.randint(low=0, high=10, size=(1000,))
# pseudorandom substitution mutations
rand2 = cp.random.randint(low=MIN_CODON, high=MAX_CODON+1, size=(1000,))


def run(rand1, rand2):
    population = found_population()
    for seed in range(15):
        fitness = assess_fitness(population)
        # print(f'Mean fit: {round(mean(fitness),2)} | Size: {len(fitness)}')
        mutate(population, 1, rand1, rand2, seed*10)
        population = select(population, fitness, cutout=cp.mean(fitness)*0.95)
        population = grow_population(population)


if __name__ == '__main__':
    run(rand1, rand2)
    print(timeit.timeit('run(rand1, rand2)', number=100, globals=globals()))
