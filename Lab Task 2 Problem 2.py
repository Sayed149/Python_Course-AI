<<<<<<< HEAD
# ============================================================
# Question 2:
# Write a Python program to detect whether any queens are
# attacking each other in a given arrangement.
# ============================================================


queens = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 5)
]


attack = False


# Check every pair of queens
for i in range(len(queens)):
    for j in range(i + 1, len(queens)):

        r1, c1 = queens[i]
        r2, c2 = queens[j]


        # Row attack
        if r1 == r2:
            print(queens[i], "and", queens[j], "are attacking")
            attack = True


        elif c1 == c2:
            print(queens[i], "and", queens[j], "are attacking")
            attack = True


        # Diagonal attack
        elif abs(r1 - r2) == abs(c1 - c2):
            print(queens[i], "and", queens[j], "are attacking")
            attack = True


# Final Answer
if not attack:
    print("No queens are attacking each other.")
else:
    print("Queens are attacking each other.")
=======
# ============================================================
# Question 2:
# Write a Python program to detect whether any queens are
# attacking each other in a given arrangement.
# ============================================================


queens = [
    (1, 2),
    (2, 4),
    (3, 6),
    (4, 5)
]


attack = False


# Check every pair of queens
for i in range(len(queens)):
    for j in range(i + 1, len(queens)):

        r1, c1 = queens[i]
        r2, c2 = queens[j]


        # Row attack
        if r1 == r2:
            print(queens[i], "and", queens[j], "are attacking")
            attack = True


        # Column attack
        elif c1 == c2:
            print(queens[i], "and", queens[j], "are attacking")
            attack = True


        # Diagonal attack
        elif abs(r1 - r2) == abs(c1 - c2):
            print(queens[i], "and", queens[j], "are attacking")
            attack = True


# Final Answer
if not attack:
    print("No queens are attacking each other.")
else:
    print("Queens are attacking each other.")
>>>>>>> d521cf8 (Deleted\.py)
