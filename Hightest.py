import random


def Fitness_function(x):
    return x ** 2 - 4 * x + 4


populationSize = 100
mutation_rate = 0.1
generations = 50

population = [random.uniform(0, 10) for _ in range(populationSize)]
for genaration in range(generations):  # Main loop for GA
    fitness_score = [Fitness_function(individual) for individual in population]
    num_parents = int(0.2 * populationSize)
    parents = []
    for i in range(populationSize):
        parent = random.choice(population)
        parents.append(parent)

    new_population = []
    while len(new_population) < populationSize:
        parent1 = random.choice(parents)
        parent2 = random.choice(parents)
        child = (parent1 + parent2) / 2.0
        if random.random() < mutation_rate:
            child += random.uniform(-0.1, 0.1)
        new_population.append(child)
    population = new_population
best_individual = max(population, key=Fitness_function)

print("solution", best_individual, "\t\t Fitness Value", Fitness_function((best_individual)))
