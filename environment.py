def assess_population(population):
    """ Modify fitness metadata of individuals

    Parameters
    ----------
    population: Population class
        Population of individuals, modified IN PLACE
    """
    # simple test fitness run
    # in future: move outside to a func/class
    for ind in population.individuals:
        ind.fitness = 2.1
