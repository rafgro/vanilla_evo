from genome import Genome


class Population:
    """
    Class representing a full population of individuals

    Attributes
    ----------
    genomes : list
        Individuals, equal to genomes from Genome class

    Methods
    -------
    found(n)
        Generate n individuals and create population
    """

    def __init__(self, found=False):
        self.genomes = []
        if found is True:
            self.found()

    def __str__(self):
        return f'Population of {len(self.genomes)}'

    def found(self, n=50, genome_size=10):
        """ Generate n individuals and create population
        """
        for _ in range(n):
            a_new_genome = Genome()
            a_new_genome.expand(genome_size)  # random sequence
            self.genomes.append(a_new_genome)
