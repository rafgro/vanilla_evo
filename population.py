from dataclasses import dataclass
from random import randint
from genome import Genome


@dataclass
class Individual:
    """
    Class for keeping genomes and metadata in one place
    """
    genome: Genome         # diploid genome sequences
    fitness: float = 1.5   # directly-understood fitness
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

    def __init__(self, found=False):
        self.individuals = []
        if found is True:
            self.found()

    def __str__(self):
        return f'Population of {len(self.individuals)}'

    def found(self, n=50, genome_size=10):
        """ Generate n individuals and create population
        """
        for _ in range(n):
            a_new_genome = Genome()
            a_new_genome.expand(genome_size)  # genome initilization
            self.individuals.append(Individual(genome=a_new_genome))

    def next_generation(self):
        """ Swap current population with new individuals
        """
        # matching individuals
        for i, m_individual in enumerate(self.individuals):
            if m_individual.paired_with != -1:
                continue  # skip already matched individuals
            # for now: random matching
            m_try = randint(0, len(self.individuals)-1)
            if self.individuals[m_try].paired_with == -1:
                m_individual.paired_with = m_try
                self.individuals[m_try].paired_with = i
        # mutations and crossing-overs
        # offspring
        new_individuals = []
        for i, o_individual in enumerate(self.individuals):
            if o_individual.paired_with == -1:
                continue  # skip lone individuals
            # probability of offspring dictated by fitness
            if o_individual.fitness >= 1:
                new_individuals.append(Individual(
                    genome=Genome(
                        o_individual.haploid(),
                        self.individuals[o_individual.paired_with].haploid(),
                    ),
                ))
