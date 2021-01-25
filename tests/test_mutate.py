'''import mutate
import genome
from codon import copy_genome


def test_mutate_substitutions():
    an_instance = genome.Genome()
    an_instance.expand(n=10)
    a_sequence = copy_genome(an_instance.sequence_A)
    mutate.mutate(an_instance, {'singles': 50, 'expansions': 0, 'deletions': 0})
    set_A = set(an_instance.sequence_A)
    set_B = set(a_sequence)
    assert len(set_A.intersection(set_B)) < len(a_sequence)  # overlap


def test_mutate_expansions():
    an_instance = genome.Genome()
    an_instance.expand(n=10)
    a_sequence = copy_genome(an_instance.sequence_A)
    mutate.mutate(an_instance, {
        'singles': 0.0,
        'expansions': 50.0,
        'deletions': 0.0}
    )
    assert len(an_instance.sequence_A) > len(a_sequence)'''
