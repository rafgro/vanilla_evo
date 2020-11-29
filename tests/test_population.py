import population


def test_population_founding():
    an_instance = population.Population()
    an_instance.found(n=10)
    assert len(an_instance.individuals) == 10


def test_population_nextgen():
    an_instance = population.Population()
    an_instance.found(n=10, ambient_fitness=2.1)
    an_instance.next_generation()
    assert len(an_instance.individuals) >= 10
