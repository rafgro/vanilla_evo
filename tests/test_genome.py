'''import genome
from codon import copy_genome


def test_genome_expansion_and_mutation():
    an_instance = genome.Genome()
    an_instance.expand(n=10)  # expansion test
    a_sequence = copy_genome(an_instance.sequence_A)
    an_instance.mutate(4)  # mutation test
    set_A = set(an_instance.sequence_A)
    set_B = set(a_sequence)
    assert len(set_A.intersection(set_B)) < len(a_sequence)  # overlap


def test_genome_haploidy():
    an_instance = genome.Genome(seqA=[1, 1, 1], seqB=[0, 0, 0])
    a_haploid = an_instance.haploid()
    assert a_haploid[0].val == 1 or a_haploid[0].val == 0'''
