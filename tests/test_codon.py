from codon import Codon, MIN_CODON, MAX_CODON
from codon import generate_genome_random, generate_genome_nonrandom


def test_codon_initiations():
    codonA = Codon()
    assert codonA.val >= MIN_CODON and codonA.val <= MAX_CODON
    codonB = Codon(init=2)
    assert codonB.val == 2


def test_codon_generators():
    genomeA = generate_genome_random(n=5)
    assert len(genomeA) == 5 and isinstance(genomeA[0], Codon)
    genomeB = generate_genome_nonrandom([0, 1, 0, 1])
    assert str(genomeB) == "[0, 1, 0, 1]"
