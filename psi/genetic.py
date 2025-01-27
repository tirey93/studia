import random
import math

def generate_random_binary(length):
  return ''.join(random.choice(['0', '1']) for _ in range(length))

def generate_initial_population(size, chromosome_length = 8):
    population = []
    for _ in range(size):
        chromosome = generate_random_binary(chromosome_length )
        population.append(chromosome)
    return population


def calculate_function(chromosome):
  x = int(chromosome, 2)
  return 0.2 * math.sqrt(x) + 2 * math.sin(2 * math.pi * 0.02 * x) + 5

def calculate_sum(population):
    sum = 0
    for n in population:
      sum = sum + calculate_function(n)
    return sum

def calculate_indicator(value, sum):
   return (value / sum) * 100

def select_parent(population, indicators):
    total_indicators = sum(indicators)
    random_number = random.uniform(0, total_indicators)
    
    current_sum = 0
    for i, indicator in enumerate(indicators):
      current_sum += indicator
      if current_sum > random_number:
        return population[i]
    return population[-1]

def crossover(parent1, parent2, crossover_point):
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    mutated_chromosome = list(chromosome)
    mutated_chromosome[mutation_point] = '1' if mutated_chromosome[mutation_point] == '0' else '0'
    return "".join(mutated_chromosome)

def select_best_chromosome(population):
    best_chromosome = None
    best_fitness = float('-inf')
    for chromosome in population:
        fitness = calculate_function(chromosome)
        if fitness > best_fitness:
            best_fitness = fitness
            best_chromosome = chromosome
    return best_chromosome

def binary_to_real(chromosome, lower_bound, upper_bound):
    chromosome_length = len(chromosome)
    x_prim = int(chromosome, 2)
    range_length = upper_bound - lower_bound
    return lower_bound + (range_length * x_prim) / (2**chromosome_length - 1)

def calculate_function_real(chromosome, lower_bound = -1, upper_bound = 2):
    """Calculates the fitness value of a binary chromosome."""
    x = binary_to_real(chromosome, lower_bound, upper_bound)
    if x < 0:
       return 0
    return 0.2 * math.sqrt(x) + 2 * math.sin(2 * math.pi * 0.02 * x) + 5