# Algorithm 1 - Linda Liu

# Problem 1

# Ask user to input a number
print("Please enter any number: ")
input_num = int(input())

# Defining a function
def power_func(x):
    return pow(2, x)

# While loop to find the appropriate values of x so that power_func(x) is >= input_num
x = 0
while power_func(x) < input_num:
    x += 1

# Printing the result of the findings
print("The next power of two that is equal to or greater than your input number is " + str(power_func(x)) + ".")





