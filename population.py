"""
Population Module

Main Purpose
------------
Govern most of the evolutionary process, since it occurs
on population level - from founding up to turnover
"""

from dataclasses import dataclass
from random import randint
from genome import Genome
from mutate import mutate
from crossover import crossover
from stats import describe_statistics


@dataclass
class Individual:
    """
    Class for keeping genomes and metadata in one place

    Biological fitness, mathematically:
        number of offspring carrying haploid genome from this individual
    """
    genome: Genome         # diploid genome sequences
    fitness: float = 1.0   # directly-understood fitness
    paired_with: int = -1  # index of mate individual


class Population:
    """
    Class representing a full population of individuals

    Attributes
    ----------
    genomes : list
        Individuals from Individual dataclass

    Methods
    -------
    found(n)
        Generate n individuals and create population
    next_generation()
        Swap current population with new individuals
    """

    def __init__(self, found=False, n=50, genome_size=10, ambient_fitness=1.0):
        self.individuals = []
        if found is True:
            self.found(n=n, genome_size=genome_size,
                       ambient_fitness=ambient_fitness)

    def __str__(self):
        return str(describe_statistics(self))

    def found(self, n=50, genome_size=10, ambient_fitness=1.5):
        """ Generate n individuals and create population
        """
        for _ in range(n):
            a_new_genome = Genome()
            a_new_genome.expand(genome_size)  # genome initilization
            self.individuals.append(Individual(
                genome=a_new_genome,
                fitness=ambient_fitness,
            ))

    def next_generation(self, mutation_setup):
        """ Swap current population with new individuals
        """
        # matching individuals
        # sorted by fitness
        self.individuals.sort(key=lambda x: x.fitness)
        for i, m_individual in enumerate(self.individuals):
            if m_individual.paired_with != -1:
                continue  # skip already matched individuals
            # for now: match next one
            m_try = i + 1 if i < len(self.individuals) else i - randint(1, 3)
            # safechecks
            if m_try < 0 or m_try >= len(self.individuals):
                continue
            if m_try == i:
                continue
            if self.individuals[m_try].paired_with != -1:
                continue
            # assign mate
            m_individual.paired_with = m_try
            self.individuals[m_try].paired_with = i
        # mutations
        for i, _ in enumerate(self.individuals):
            mutate(self.individuals[i].genome, mutation_setup)
        # crossing overs
        for i, _ in enumerate(self.individuals):
            if self.individuals[i].paired_with == -1:
                continue
            crossover(self.individuals[i].genome, events=1)
        # offspring
        new_individuals = []
        for i, o_individual in enumerate(self.individuals):
            if o_individual.paired_with == -1:
                continue  # skip lone individuals
            # probability of offspring dictated by fitness
            # algorithm: 100% for every full 1, probability
            #   0.1=10% for all other
            offspring_to_make = o_individual.fitness
            while offspring_to_make > 0.01:
                if offspring_to_make < 1:
                    if randint(0, 100) > offspring_to_make*100:
                        break  # under 1 -> no more offspring
                offspring_to_make -= 1
                new_individuals.append(Individual(
                    genome=Genome(
                        cod_seqA=o_individual.genome.haploid(),
                        cod_seqB=self.individuals[o_individual.paired_with]
                                     .genome.haploid(),
                    ),
                ))
        # finish line
        self.individuals = new_individuals
