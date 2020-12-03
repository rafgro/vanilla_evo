import mutate
import genome


def test_mutate_substitutions():
    an_instance = genome.Genome()
    an_instance.expand(n=10)
    a_sequence_bit = an_instance.sequence_A.copy()
    mutate.mutate(an_instance, {'singles': 50, 'expansions': 0})
    assert an_instance.sequence_A != a_sequence_bit


def test_mutate_expansions():
    an_instance = genome.Genome()
    an_instance.expand(n=10)
    a_sequence_bit = an_instance.sequence_A.copy()
    mutate.mutate(an_instance, {'singles': 0, 'expansions': 50})
    assert len(an_instance.sequence_A) > len(a_sequence_bit)
