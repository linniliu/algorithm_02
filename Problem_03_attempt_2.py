# Algorithm 2 - Linda Liu

# Problem 3  Attempt 2 - using itertools

import itertools

print("Please enter the number of stairs ")
stairs = int(input())

def findCombos(n):

    combos = []
    num_combos = 0

    for x in range(n+1, 1, -1):
        candidates = list(itertools.product([1,2], repeat=x))

        for c in candidates:
            if sum(c) == n:
                combos.append(c)
    num_combos = len(combos)
    print("The number of possibilities are " + str(num_combos) + " and they are:")
    return combos

print(findCombos(stairs))