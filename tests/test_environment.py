'''import environment
import population


def test_population_nextgen():
    an_instance = population.Population()
    an_instance.found(n=10, ambient_fitness=3.1245)
    environment.assess_population(an_instance)
    assert an_instance.individuals[5].fitness != 3.1245'''
