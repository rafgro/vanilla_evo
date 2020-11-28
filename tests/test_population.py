import population


def test_population_founding():
    an_instance = population.Population()
    an_instance.found(10)
    assert len(an_instance.genomes) == 10
