# Algorithm 2 - Linda Liu

# Problem 4

import itertools

print("Please enter the number of stairs: ")
stairs = int(input())

# Creating an empty list to allow user to input a list of steps skipped
skip = []
steps = int(input("Please enter the total number of steps you wish to skip, followed by their corresponding values: "))

# Creation of the skip list base on previous user inputs
for i in range(0, steps):
    steps = int(input())
    skip.append(steps)

def findCombos(n):

    combos = []
    num_combos = 0

    for x in range(n+1, 1, -1):
        candidates = list(itertools.product(skip, repeat=x))

        for c in candidates:
            if sum(c) == n:
                combos.append(c)
    num_combos = len(combos)
    print("The number of possibilities are " + str(num_combos) + " and they are:")
    return combos

print(findCombos(stairs))

