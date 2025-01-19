import random
import math

def generate_random_binary(length):
  """Generates a random binary string of the given length."""
  return ''.join(random.choice(['0', '1']) for _ in range(length))

def generate_initial_population(size, chromosome_length):
    """Generates an initial population of random binary chromosomes."""
    population = []
    for _ in range(size):
        chromosome = generate_random_binary(chromosome_length)
        population.append(chromosome)
    return population


def calculate_function(chromosome):
  """Calculates the fitness value of the given x using the provided function."""
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
    """Selects a parent using roulette wheel selection."""
    total_indicators = sum(indicators) #Sumowanie wskaźników
    random_number = random.uniform(0, total_indicators) #Losowa liczba z zakresu sumy wskaźników
    
    current_sum = 0
    for i, indicator in enumerate(indicators):
      current_sum += indicator
      if current_sum > random_number:
        return population[i]
    return population[-1] # In case of rounding errors return last parent

def crossover(parent1, parent2, crossover_point):
    """Performs single-point crossover on two parents."""
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2