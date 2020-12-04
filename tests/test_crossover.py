from bitarray import bitarray
import genome
from crossover import crossover


def test_crossover_exchange():
    a, b = '11111111111', '0000000000000'
    an_instance = genome.Genome(seqA=a, seqB=b)
    crossover(an_instance, events=1)
    assert an_instance.sequence_A != bitarray(a)
