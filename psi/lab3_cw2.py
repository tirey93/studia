
import random

from matplotlib import pyplot as plt
from genetic import calculate_indicator, canFunction_real, crossover, generate_initial_population, calculate_sum, mutate, select_best_chromosome, select_parent

# Parametry populacji
population_size = 200
mutation_probability = 0.5
max_generations = 200
chromosome_length = 22

def make_one_generation(population, crossover_probability, mutation_probability, chromosome_length):
    # Wyświetlenie populacji
    # print("Populacja początkowa:")
    # print(initial_population)

    sum = calculate_sum(population)
    indicators = []
    for chromosome in population:
        chromosome_value = canFunction_real(chromosome)
        indicator = calculate_indicator(chromosome_value, sum   )
        indicators.append(indicator)

    parents = []
    for _ in range(len(population)):
        parent = select_parent(population, indicators)
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
            crossover_point = random.randint(1, chromosome_length - 1) #bierzemy tylko geny w środku, nieskrajne
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

def genetic_algorithm(population_size, crossover_probability, mutation_probability):
    initial_population = generate_initial_population(population_size)
    generation_number = 1
    best_fitness_history = []
    population = initial_population
    while generation_number <= max_generations:
        new_population = make_one_generation(
            population,
            crossover_probability, 
            mutation_probability,
            chromosome_length = chromosome_length )
        population = new_population
        generation_number += 1
        best_chromosome = select_best_chromosome(population)
        best_fitness_history.append(canFunction_real(best_chromosome))

    best_chromosome = select_best_chromosome(population)
    print("Najlepszy chromosom:")
    print(best_chromosome, int(str(best_chromosome), 2))
    return best_fitness_history

crossover_probabilities = [0.5]

plt.figure(figsize=(10, 6))
for crossover_probability in crossover_probabilities:
    best_fitness_history = genetic_algorithm(
    population_size, 
    crossover_probability, 
    mutation_probability)
    plt.plot(range(1, max_generations + 1), best_fitness_history, label=f'pk={crossover_probability}')
plt.xlabel("Liczba pokoleń")
plt.ylabel("Wartość F.P.")
plt.title("Funkcja przystosowania, mutacja: "+ str(mutation_probability))
plt.legend()
plt.grid(True)
plt.show()