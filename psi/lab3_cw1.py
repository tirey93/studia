
from genetic import calculate_indicator, generate_initial_population, calculate_function, calculate_sum, select_parent

# Parametry populacji
population_size = 10
chromosome_length = 8

# Generowanie populacji początkowej
initial_population = generate_initial_population(population_size, chromosome_length)

# Wyświetlenie populacji
print("Populacja początkowa:")
for i, chromosome in enumerate(initial_population):
    print(f"{i+1}. {chromosome} ({int(chromosome, 2)})")

print()
print()

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

print(parents)