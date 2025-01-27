
import random
from genetic import calculate_indicator, crossover, generate_initial_population, calculate_function, calculate_sum, mutate, select_best_chromosome, select_parent

# Parametry populacji
population_size = 200
chromosome_length = 8
crossover_probability = 0.5
mutation_probability = 0.06
max_generations = 200

# Generowanie populacji początkowej
initial_population = generate_initial_population(population_size, chromosome_length)

def make_one_generation(population, crossover_probability, mutation_probability):
    # Wyświetlenie populacji
    # print("Populacja początkowa:")
    # print(initial_population)

    sum = calculate_sum(initial_population)
    indicators = []
    for chromosome in initial_population:
        chromosome_value = calculate_function(chromosome)
        indicator = calculate_indicator(chromosome_value, sum   )
        indicators.append(indicator)

    parents = []
    for _ in range(len(initial_population)):
        parent = select_parent(initial_population, indicators)
        parents.append(parent)


    # print("Tworzymy pary... ")
    pairs = []
    for i in range(0, len(parents), 2):
        if i + 1 < len(parents):
            pairs.append((parents[i], parents[i+1]))
        else:
            pairs.append((parents[i], parents[i]))

    # print("Krzyżowanie...")
    childs = []
    for pair in pairs:
        if random.random() < crossover_probability:
            crossover_point = random.randint(1, chromosome_length - 1)
            child1, child2 = crossover(pair[0], pair[1], crossover_point)
            childs.append(child1)
            childs.append(child2)
        else: 
            childs.append(pair[0])
            childs.append(pair[1])

    # print("Mutacja...")
    if random.random() < mutation_probability:
        mutatated_child = random.randint(0, len(childs) - 1)
        childs[mutatated_child] = mutate(childs[mutatated_child])
    return childs

generation_number = 1
population = initial_population
while generation_number <= max_generations:
    new_population = make_one_generation(
        population,
        crossover_probability, 
        mutation_probability)
    population = new_population
    generation_number += 1

best_chromosome = select_best_chromosome(population)
print("Najlepszy chromosom:")
print(best_chromosome, int(str(best_chromosome), 2))