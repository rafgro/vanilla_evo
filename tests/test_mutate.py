import mutate
import genome
import numpy as np
from codon import copy_genome


def test_mutate_substitutions():
    an_instance = genome.Genome()
    an_instance.expand(n=10)
    a_sequence = copy_genome(an_instance.sequence_A)
    mutate.mutate(an_instance, {
        'singles': 50,
        'expansions': 0,
        'deletions': 0}
    )
    assert np.array_equal(a_sequence, an_instance.sequence_A) is False


def test_mutate_expansions():
    an_instance = genome.Genome()
    an_instance.expand(n=10)
    a_sequence = copy_genome(an_instance.sequence_A)
    mutate.mutate(an_instance, {
        'singles': 0.0,
        'expansions': 50.0,
        'deletions': 0.0}
    )
    assert len(an_instance.sequence_A) > len(a_sequence)


def test_mutate_deletions():
    an_instance = genome.Genome()
    an_instance.expand(n=100)
    a_sequence = copy_genome(an_instance.sequence_A)
    mutate.mutate(an_instance, {
        'singles': 0.0,
        'expansions': 0.0,
        'deletions': 10.0}
    )
    assert len(an_instance.sequence_A) < len(a_sequence)
