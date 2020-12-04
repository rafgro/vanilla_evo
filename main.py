from population import Population

print('Hello')
# Founding population
population = Population(found=True)
print(population)
# Second generation
population.next_generation()
# Third generation
population.next_generation()
