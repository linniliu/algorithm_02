mystring = "Hello Oraask"

# Getting length of string
lengthOfmystring = len(mystring)

# Iterating through the string using while loop
for i in mystring[0:lengthOfmystring:2] :
# Print all characters iterated
    print("Element of string:" , i)


# Looping the substring of the first string through the second string
sub_str = 0
while sub_str != str_01:
    print(sub_str) #> can use to test if loops to create sub_string are running correctly
    # Create a sub-string out of str_02 with a length that is equal to str_01
    sub_str = (range_02(c))
    c += 1
    if sub_str == str_01:
        print("Match found.")
        break
    elif c == length_02(str_02):
        print("No match found.")
        break
    else:
        print("No match found!")


sub_str = str_01
for sub_str in range_02(c):
    c += 1
    if c == length_02(str_02):
        print("No match found.")
        continue
    elif sub_str == str_01:
        print("Match found.")
        continue
    else:
        print("No match found!")


#Get Max example (Class 5, timestamp 150)

def get_max(n1, n2, n3):
  if n1 > n2 and n1 > n3:
    return n1
  if n2 > n3:
    return n2
  return n3
