from bitarray import bitarray
from random import randint


class Genome:
    """
    Class containing a single individual in population, equal to genome

    Attributes
    ----------
    sequence : bitarray
        Genome sequence in bits

    Methods
    -------
    mutate(n=1)
        Change single bits n times
    expand(n=1)
        Expand sequence by n bits
    """

    def __init__(self):
        self.sequence = bitarray()

    def mutate(self, n=1):
        """Change n times randomly single bits in the sequence
        """
        for _ in range(n):
            locus = randint(0, len(self.sequence)-1)
            self.sequence.invert(locus)

    def expand(self, n=1):
        """Expand the sequence by n random bits
        """
        for _ in range(n):
            self.sequence.append(randint(0, 1))
