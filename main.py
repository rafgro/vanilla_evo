from population import Population
from environment import assess_population

print('Hello')
# Config
mutation_setup = {'singles': 10.0, 'expansions': 0.0, 'deletions': 0.0}
# Founding population
print('F1')
population = Population(found=True)
assess_population(population)
print(population)
# Evolution loop
for i in range(2, 41):
    # actual computation
    population.next_generation(mutation_setup)
    assess_population(population)
    # report stats every 4 generations
    if i % 4 == 0:
        print(' ')
        print(f'F{i}')
        print(population)
