import genome


def test_genome_expansion():
    an_instance = genome.Genome()
    an_instance.expand(10)  # expansion test
    assert len(an_instance.sequence_A) >= 10


def test_genome_haploidy():
    an_instance = genome.Genome(seqA=[1, 1, 1], seqB=[0, 0, 0])
    a_haploid = an_instance.haploid()
    assert a_haploid[0] == 1 or a_haploid[0] == 0
