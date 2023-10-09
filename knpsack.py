import random
import Items
import matplotlib.pyplot as plt

# inputs
filname = "items"
# limatation of weight
carryLimit = 25.0  # in Kg

# GA
popsize = 10
generation = 100
mutuationrate = 0.1

# create items object
items_list = []
with open(filname, "r") as f:
    for line in f:
        new_line = line.strip()
        print(new_line)
        new_line = new_line.split(" ")
        id, weight, value = new_line[0], new_line[1], new_line[2]
        new_items = Items.Item(int(id), float(weight), float(value))
        items_list.append(new_items)


# this to create rondom solution

def create_random_solution(Item_list):
    solution = []
    for i in range(0, len(Item_list)):
        solution.append(random.randint(0, 1))
    return solution


# to Check the solution waether it is valid or not

def valid_solution(items_List, solution_list, limit):
    total_weight = 0  # check for the weight
    for i in range(0, len(solution_list)):
        if solution_list[i] == 1:
            total_weight += items_List[i].weight
        if total_weight > limit:
            return False
    return True


def calculate_value(items_list, solution_list):
    total_value = 0  # calculate for value
    for i in range(0, len(solution_list)):
        if solution_list[i] == 1:
            total_value += items_list[i].value
        return total_value


def Check_dupilicate(s1, s2):
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


def initial_population(pop_size, items_list, limitweight):
    population = []
    i = 0
    while i < pop_size:
        new_solution = create_random_solution(items_list)
        if valid_solution(items_list, new_solution, limitweight):
            if len(population) == 0:
                population.append(new_solution)
                i += 1
            else:
                skip = False
                for j in range(0, len(population)):
                    if Check_dupilicate(new_solution, population[j]):
                        skip = True
                        continue
                if not skip:
                    population.append(new_solution)
                    i += 1
    return population


def tournament_selection(pop):
    ticket1 = random.randint(0, len(pop) - 1)
    ticket2 = random.randint(0, len(pop) - 1)
    if calculate_value(items_list, pop[ticket1] > calculate_value(items_list, pop[ticket2])):
        winner = pop[ticket1]
    else:
        winner = pop[ticket2]
        return winner


# one point
def crossOver(parent1, parent2):
    breakPoint = random.randint(0, len(parent1))
    firstPart = parent1[:breakPoint]
    secondPart = parent2[breakPoint:]
    offspring = firstPart + secondPart
    if valid_solution(items_list, offspring, carryLimit):
        return offspring
    else:
        return crossOver(parent1, parent2)


def mutuation(chromosome):
    temp = chromosome
    mutuationIndex_1, mutuationIndex_2 = random.sample(range(0, len(chromosome)), 2)
    temp[mutuationIndex_1], temp[mutuationIndex_2] = temp[mutuationIndex_2], temp[mutuationIndex_1]
    if valid_solution(items_list, temp, carryLimit):
        return temp
    else:
        return mutuation(chromosome)


def Create_Generation(pop, mutation_rate):
    new_gen = []
    for i in range(0, len(pop)):
        parent1 = tournament_selection(pop)
        parent2 = tournament_selection(pop)
        offspring = crossOver(parent1, parent2)
        if random.random() < mutation_rate:
            offspring = mutuation(offspring)
            new_gen.append(offspring)
    return new_gen


def best_solution(generation, items_list):
    best = 0
    for i in range(0, len(generation)):
        temp = calculate_value(items_list, generation[i])
        if temp > best:
            best = temp
    return best


value_list = []


def Genetic_Algorithm(CarryLimit, population_size, generation_size, mutuation_rate, Item_list):
    pop = create_random_solution()
    count = 1
    for i in range(0, generation_size):
        pop = create_random_solution(pop,mutuation_rate)

        print("population", count, pop[0])
        print("value====>", calculate_value(items_list, pop[0]))
        value_list.append(best_solution(pop, items_list))
    return pop, value_list


latestPopulation, v_list = Genetic_Algorithm(carryLimit=carryLimit,
                                             population_size=popsize,
                                             generation_size=generation,
                                             mutuation_rate=mutuationrate,
                                             items_list=items_list)
plt.plot(v_list)
plt.xlabel("Generation")
plt.ylabel("Values ")
plt.title("KnapSack")
plt.show()
