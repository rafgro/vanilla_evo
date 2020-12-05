from population import Population

print('Hello')
# Founding population
print('F1')
population = Population(found=True)
print(population)
# Second generation
print('F2')
population.next_generation()
print(population)
# Third generation
print('F3')
population.next_generation()
print(population)
