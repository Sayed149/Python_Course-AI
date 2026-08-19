# Problem 2:
# Consider the problem of maximizing the function f(x) = 27x - x^2,
# where x can vary between integer values 0 and 31.
# Encode x as a binary string of length 5.
# Start with an initial population of four chromosomes at random
# and apply Genetic Algorithm Operators (Selection, Crossover,
# and Mutation) to illustrate how genetic algorithm evolves
# toward fitter candidate solution.

import random


# Fitness function
def fitness(x):
    return 27 * x - x * x


# Convert binary string to decimal
def binary_to_decimal(binary):
    return int(binary, 2)


# Create initial population of 4 chromosomes
population = []

for i in range(4):
    chromosome = format(random.randint(0, 31), "05b")
    population.append(chromosome)


# Run Genetic Algorithm for 5 generations
for generation in range(1, 6):

    print("\nGeneration", generation)
    print("--------------------")

    fitness_values = []

    # Calculate fitness
    for chromosome in population:

        x = binary_to_decimal(chromosome)
        f = fitness(x)

        fitness_values.append(f)

        print("Chromosome:", chromosome,
              "x =", x,
              "Fitness =", f)

    # Find best chromosome
    best_index = fitness_values.index(max(fitness_values))

    print("\nBest chromosome:", population[best_index])
    print("Best x:", binary_to_decimal(population[best_index]))
    print("Best fitness:", fitness_values[best_index])

    # Selection
    selected = random.choices(
        population,
        weights=fitness_values,
        k=4
    )

    print("\nSelected chromosomes:", selected)

    # Crossover
    new_population = []

    for i in range(0, 4, 2):

        parent1 = selected[i]
        parent2 = selected[i + 1]

        # Random crossover point from 1 to 4
        point = random.randint(1, 4)

        print("\nParents:", parent1, parent2)
        print("Crossover point:", point)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        print("Children:", child1, child2)

        new_population.append(child1)
        new_population.append(child2)

    # Mutation
    mutation_rate = 0.1

    for i in range(len(new_population)):

        chromosome = list(new_population[i])

        for j in range(len(chromosome)):

            if random.random() < mutation_rate:

                if chromosome[j] == "0":
                    chromosome[j] = "1"
                else:
                    chromosome[j] = "0"

        new_population[i] = "".join(chromosome)

    # New generation
    population = new_population


print("\nGenetic Algorithm Finished")