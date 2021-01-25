'''import genome
from crossover import crossover


def test_crossover_exchange():
    a = [1, 1, 1, 1, 1, 1, 1, 1]
    b = [0, 0, 0, 0, 0, 0, 0, 0]
    an_instance = genome.Genome(seqA=a, seqB=b)
    crossover(an_instance, events=1)
    assert str(an_instance.sequence_A) != str(an_instance.sequence_B)'''
