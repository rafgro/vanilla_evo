from population import Population
from environment import assess_population

print('Hello')
# Founding population
print('F1')
population = Population(found=True)
assess_population(population)
print(population)
# Evolution loop
for i in range(2, 13):
    # actual computation
    population.next_generation()
    assess_population(population)
    # report stats every 4 generations
    if i % 4 == 0:
        print(' ')
        print(f'F{i}')
        print(population)
