# Algorithm 2 - Linda Liu

# Problem 2

# Given two strings, write an algorithm to check if the first string exists in the second.

# Ask user to input two strings
print("Please enter a string: ")
str_01 = input()
print("Please enter a second string that is >= the previous string: ")
str_02 = input()

# Functions to get the length of the strings
def length_01(a):
    return int(len(a))
def length_02(b):
    return int(len(b))

# Function to get the range of str_02
c = 0
def range_02(c):
    return str_02[c:length_01(str_01)+c]

# Looping the substring of the first string through the second string
sub_str = 0
while sub_str != str_01:
    #print(sub_str) > can use to test if loops to create sub_string are running correctly
    # Create a sub-string out of str_02 with a length that is equal to str_01
    sub_str = (range_02(c))
    c += 1
    if sub_str == str_01:
        print("Match found!")
        break
    if c == length_02(str_02):
        print("No match found.")
        break


