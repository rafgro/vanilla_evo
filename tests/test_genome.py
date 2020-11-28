import genome


def test_genome_expansion_and_mutation():
    an_instance = genome.Genome()
    an_instance.expand(n=10)  # expansion test
    a_sequence_bit = an_instance.sequence.copy()
    an_instance.mutate(4)  # mutation test
    assert an_instance.sequence != a_sequence_bit
