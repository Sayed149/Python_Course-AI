# Problem 1:
# In Genetic Algorithm, Single Point Crossover is a form of crossover
# in which two parent chromosomes are selected and a random/given point
# is selected. The genes/data are interchanged between them after the
# selected point.
#
# Example:
# P1: 000011110011
# P2: 101010101010
# Point: 4
#
# After Crossover:
# C1: 000010101010
# C2: 101011110011
#
# The problem is to select a random point for the crossover of two given
# parents and generate at least five generations of children from the
# given pair of chromosomes.
#
# parent1 = "000011110011"
# parent2 = "101010101010"


import random

parent1 = "000011110011"
parent2 = "101010101010"

print("Parent 1:", parent1)
print("Parent 2:", parent2)

for generation in range(1, 6):

    # Select a random crossover point
    point = random.randint(1, len(parent1) - 1)

    # Perform single point crossover
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    print("\nGeneration", generation)
    print("Crossover Point:", point)
    print("Child 1:", child1)
    print("Child 2:", child2)

    # Children become parents for the next generation
    parent1 = child1
    parent2 = child2