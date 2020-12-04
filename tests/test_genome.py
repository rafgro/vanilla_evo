from bitarray import bitarray
import genome


def test_genome_expansion_and_mutation():
    an_instance = genome.Genome()
    an_instance.expand(n=10)  # expansion test
    a_sequence_bit = an_instance.sequence_A.copy()
    an_instance.mutate(4)  # mutation test
    assert an_instance.sequence_A != bitarray(a_sequence_bit)


def test_genome_haploidy():
    an_instance = genome.Genome(seqA='111', seqB='000')
    a_haploid = an_instance.haploid()
    assert a_haploid == bitarray('111') or a_haploid == bitarray('000')
