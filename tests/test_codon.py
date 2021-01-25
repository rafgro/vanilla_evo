from codon import MIN_CODON, MAX_CODON
from codon import generate_genome_random, generate_genome_nonrandom


def test_codon_initiations():
    codonA = generate_genome_random(n=1)
    assert codonA[0] >= MIN_CODON and codonA[0] <= MAX_CODON
    codonB = generate_genome_nonrandom([2])
    assert codonB[0] == 2


def test_codon_generators():
    genomeA = generate_genome_random(n=5)
    assert len(genomeA) == 5
    genomeB = generate_genome_nonrandom([0, 1, 0, 1])
    assert str(genomeB) == "[0 1 0 1]"
