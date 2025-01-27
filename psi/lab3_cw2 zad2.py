
import pygad
import math

def rastring(x, y):
  return 20 + x**2 + y**2 - 10*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))

lower_bound = -30
upper_bound = 30

optimization_type = 'max' 
def fitness_func(ga_instance, solution, solution_idx):
    x, y = solution
    output = rastring(x, y)

    if optimization_type == 'min':
      return 1.0 / (output + 1e-6)
    elif optimization_type == 'max':
      return output

fitness_function = fitness_func
num_generations = 500
num_parents_mating = 4
sol_per_pop = 8
num_genes = 2
init_range_low = lower_bound
init_range_high = upper_bound
parent_selection_type = "sss"
keep_parents = 1
crossover_type = "uniform"
mutation_type = "random"
mutation_percent_genes = 0.01

ga_instance = pygad.GA(num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_function,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    init_range_low=init_range_low,
    init_range_high=init_range_high,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes)

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution ={solution_fitness}".format(solution_fitness=solution_fitness))
prediction = rastring(solution[0],solution[1])
print("Predicted output based on the best solution : {prediction}".format(prediction=prediction))

ga_instance.plot_fitness()

solution, solution_fitness, solution_idx = ga_instance.best_solution(ga_instance.last_generation_fitness)
print(f"Parameters of the best solution : {solution}")
print(f"Fitness value of the best solution = {solution_fitness}")
print(f"Index of the best solution : {solution_idx}")
prediction = rastring(solution[0],solution[1])
print(f"Predicted output based on the best solution : {prediction}")

if ga_instance.best_solution_generation != -1:
    print(f"Best fitness value reached after {ga_instance.best_solution_generation} generations.")

filename = 'genetic'
ga_instance.save(filename=filename)
loaded_ga_instance = pygad.load(filename=filename)
loaded_ga_instance.plot_fitness()