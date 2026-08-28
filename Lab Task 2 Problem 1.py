# ============================================================
# Question 1:
# Write a Python program to check whether an N-Puzzle is
# solvable or not using the number of inversions and the
# position of the blank tile.
# ============================================================


initial = [
    [6, 1, 10, 2],
    [7, 11, 4, 14],
    [5, 9, 15, 0],
    [8, 12, 13, 3]
]

goal = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0]
]


# Print Initial State
print("Initial State:")
for row in initial:
    print(row)


# Print Goal State
print("\nGoal State:")
for row in goal:
    print(row)


# Find all tiles except blank tile (0)
tiles = []

for row in initial:
    for value in row:
        if value != 0:
            tiles.append(value)


# Count inversions
inversions = 0

for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        if tiles[i] > tiles[j]:
            inversions += 1


print("\nNumber of Inversions:", inversions)


# Find blank tile row
n = len(initial)

for i in range(n):
    for j in range(n):
        if initial[i][j] == 0:
            blank_row = i


# Calculate blank row from bottom
blank_row_from_bottom = n - blank_row

print("Blank Row from Bottom:", blank_row_from_bottom)


# Check solvability
if n % 2 == 1:

    # Odd dimension
    if inversions % 2 == 0:
        solvable = True
    else:
        solvable = False

else:

    # Even dimension
    if blank_row_from_bottom % 2 == 1:

        # Blank is in odd row from bottom
        if inversions % 2 == 0:
            solvable = True
        else:
            solvable = False

    else:

        # Blank is in even row from bottom
        if inversions % 2 == 1:
            solvable = True
        else:
            solvable = False


# Final Answer
if solvable:
    print("Puzzle is Solvable.")
else:
    print("Puzzle is Not Solvable.")