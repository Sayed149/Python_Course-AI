# Question:
# Solve a Map Coloring problem using three colors:
# ['blue', 'red', 'green'].
#
# There are 6 territories (0, 1, 2, 3, 4, 5).
# Find all possible combinations of colors such that
# no neighboring territories have the same color.
#
# Neighboring territories:
# (0,1), (0,5), (0,4), (5,4),
# (1,4), (1,3), (4,2), (2,3)
#
# Display all valid solutions and the total number of solutions.


from itertools import product

colors = ["blue", "red", "green"]

neighbors = [
    (0, 1),
    (0, 5),
    (0, 4),
    (5, 4),
    (1, 4),
    (1, 3),
    (4, 2),
    (2, 3)
]

solutions = []

for combination in product(colors, repeat=6):

    valid = True

    for a, b in neighbors:
        if combination[a] == combination[b]:
            valid = False
            break

    if valid:
        solutions.append(combination)

for i, solution in enumerate(solutions, 1):
    print(i, solution)

print("Total solutions:", len(solutions))