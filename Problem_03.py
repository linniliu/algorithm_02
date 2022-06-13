# Algorithm 2 - Linda Liu

# Problem 3  Attempt 1 (unfinished)

# PLAN
# Step 1. Generate a matrix of size n
    #ie. Use n = 4 as an example
# Step 2. Replace all values inside the list with 0
# Step 3. Replace all in the list with 1 (will add up to n) > this is the first possibility
    #ie. [1, 1, 1, 1]
# Step 4. Replace 0 index with 0 and add 1 to n^th index
    #ie. [0, 1, 1, 2]
# Step 5. Replace 0 index with 0 and add 1 to (n-1)^th index
    #ie. [0, 1, 2, 1]
# Step 6. Replace 0 index with 0 and add 1 to (n-2)^th index
    #ie. [0, 2, 1, 1]
# Step 6. Replace 0 and 1 index with 0 and add 1 to n and n-1 index
    #ie. [0, 0, 2, 2]


print("Please a random number of steps: ")
n = int(input())

#Store the step increments as a dictionary
step = (1, 2)

# Create the correct size of the matrix based on the input number of stairs
#stair = list(range(1, n+1))
#print(stair)

# Create a function for the staircase increments
def stair(n):
    return list(range(1, n+1))
print(stair(n))

#Replace all the values of stair with 0
i = 0
for i in stair:
    print(i)



