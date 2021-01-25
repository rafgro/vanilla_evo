import population


def test_population_founding():
    an_instance = population.Population()
    an_instance.found(n=10)
    assert len(an_instance.individuals) == 10


def test_population_nextgen():
    an_instance = population.Population()
    an_instance.found(n=10, genome_size=100, ambient_fitness=3.1)
    mutation_setup = {'singles': 10.0, 'expansions': 0.0, 'deletions': 0.0}
    an_instance.next_generation(mutation_setup)
    assert len(an_instance.individuals) >= 10
