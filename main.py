from population import Population
from environment import assess_population

print('Hello')
# Founding population
print('F1')
population = Population(found=True)
assess_population(population)
print(population)
# Second generation
print('F2')
population.next_generation()
assess_population(population)
print(population)
# Third generation
print('F3')
population.next_generation()
assess_population(population)
print(population)
