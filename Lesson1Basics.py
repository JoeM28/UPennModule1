
"""
Created on Thu Mar 15 11:08:33 2018

@author: Leo
"""

# Variables and argument passing
a = 0                    # assign 0 to variable a
a = b = c = 0            # assign 0 to variable a, b, c at same time
a, b, c = 1, 2, 3        # assign 1, 2, 3 to a, b, c
a, b = b, a              # swap the value for a and b
print(a, b)

# Numbers
int1 = 123456789
print(int1**5)
print(type(int1))

float1 = 3.1415
float2 = 5.69e-6         # use scientific notation
print(type(float1))
print(type(float2))

# Strings
s1 = 'Hello, world'           # Single quotations
s2 = "Hello, world"           # Double quotations
print(type(s1))
print(s1 == s2)

c = """This is a longer string that
spans multiple lines"""
print(c)

a = "The first string "
b = "and the second string"
print(a + b)

# Booleans
x = True
y = False
print(x and y)
print(x or y)

# None
x = None
y = 3
print(x is None)
print(y is not None)

print(type(x))
print(type(y))

# print statement
letter = 'c'
print(letter)                              # print letter
number = 42
print("the number is:", number)            # prints "the number is: 42"

# List
print([1, 2, 3])                  # List with three items with the same type
print([4, 5.67, "Python"])        # List with three items but they are different types
print([45])                       # List with one item
print([])                         # Empty list

# indexing and slicing a list
L = [12, 90, 4, 5.67, "Python"]
print(L[0])                       # Select the first element
print(L[2])                       # Select the third element
print(L[1:4])                     # Select from the second to the fourth elements
print(L[:3])                      # Select from the first element to the third element
print(L[2:])                      # Select from the third element to the end
print(L[::-1])                    # reverse the list

# List practice
L = [3, 7, 2, 56, 23, 21]
L.append(21)               # Append 21 at the end of L
print(L)
L.extend([3, 8])           # Append 3 and 8 at the end of L
print(L)
L.insert(4, 100)           # Insert 100 as the fifth element
print(L)
L.remove(56)               # Remove 56 from L
print(L)
L.pop()                    # Remove the last element
print(L)
L.pop(3)                   # Remove the fourth element
print(L)
print(L.index(23))         # Return the index of 23
print(L.count(3))          # Count how many 3 in L
L.reverse()                # Reverse L
print(L)
L.sort()                   # Sort L in ascending order
print(L)

# Tuple
tup1 = (1, 2, 3)              # Create a tuple variable called tup1
print(tup1)
tup2 = 1, 2, 3                # Equivalent to tup1 = (1, 2, 3)
print(tup2)
print(type(tup1))
print(type(tup2))

# nested tuple
nested_tup = (4, 5, 6), (7, 8)   # Create a tuple variable called nested_tup
print(nested_tup)

print(tuple('hello'))
print(tuple([2, 3, 4, 5]))
print(tup1)
print(tup1[1])
a = (1, 2, 2, 2, 3, 4, 2)
print(a.count(2))                # Count how many 2 in a
print(a.index(2))                # Return the index of the first 2 in a

# set
print(set([2, 2, 2, 1, 3, 3]))
print({2, 2, 2, 1, 3, 3})

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a & b)

# dictionary
# Dictionary with three string keys and items
print({'x':34, 'y':12, 'z':7})   # or dict(x = 34, y = 12, z = 7)
# Dictionary with two integer keys and items
print({1:2, 2:3})                # or dict([(1, 2), (2, 3)])
print({})                        # or use dict() to create an empty dictionary

# Modify a dict
d = {'x':34, 'y':12, 'z':7}
print(d['x'])                   # Return the value for the key 'x'
d['y'] = 0                      # Change the value for the key 'y'
print(d)
d['a'] = 78                     # Insert 'a': 78 into d
print(d)

# examples of how to use dict methods
print(d)
print(0 in d)
print(d.items())
print(d.keys())
print(d.values())
print(d.get('a'))
print(d.pop('a'))
print(d)
print(d.popitem())
print(d)

# 1. LIST
fruits = ["apple", "banana", "cherry", "apple"]
print("LIST Example:", fruits)
print("➡ LIST is Ordered, Mutable, Allows Duplicates")
print("➡ Example Syntax: list1 = ['a', 'hello', 20]")

fruits[1] = "blueberry"   # change value
print("Updated LIST:", fruits, "\n")


# 2. TUPLE
colors = ("red", "green", "blue", "red")
print("TUPLE Example:", colors)
print("➡ TUPLE is Ordered, Immutable, Allows Duplicates")
print("➡ Example Syntax: tuple1 = ('a', 'hello', 20)")

# colors[1] = "yellow"  # ❌ Uncomment to see error
print("Tuples cannot be changed once created\n")


# 3. SET
numbers = {1, 2, 3, 2, 1}
print("SET Example:", numbers)
print("➡ SET is Unordered, Mutable, No Duplicates")
print("➡ Example Syntax: set1 = {1, 2, 3}")

numbers.add(4)  # add a new item
print("Updated SET:", numbers, "\n")


# 4. DICTIONARY
student = {"name": "Alice", "age": 21, "city": "New York"}
print("DICTIONARY Example:", student)
print("➡ DICTIONARY stores Key-Value pairs, Mutable, Keys Unique")
print("➡ Example Syntax: dict1 = {'name':'Bob', 'age':25}")

student["age"] = 22         # update value
student["grade"] = "A"      # add new key-value
print("Updated DICTIONARY:", student)



# if else statement
x = 4
if x < 0:
    print('The input is negative')
elif x == 0:
    print('The input is equal to zero')
else:
    print('The input is positive')

# for loop
L1 = [3, 6, 2, 8, 78]
total = 0
for val in L1:
    total += val                       # calculate the sum of L1
print(total)
print(sum(L1))

total = 0
for i in range(len(L1)):               # Iterate a list by index:
    total += L1[i]
print(total)

d = {'a': 3, 'b': 1, 'c': None, 'd': 6, None: '3'}

for key, value in d.items():
    if key is None or value is None:   # If key or value is None
        print(key, value)              # Print out key - value pairs

# while statement
L = [3, 6, 2, 8, 78]
n = len(L)
i = 0
while i < n:
    print(L[i])
    i += 1

# break statement
# get the sum of the list, if the value is none, stop the loop
L2 = [11, 3, 135, None, 9]
result = 0
for i in range(len(L2)):
    if L2[i] is None:
        print('L2[', i, '] is not a valid number')
        break
    result += L2[i]
print(result)

# Continue statement
result = 0
for value in L2:
    if value is None:
        continue
    result += value
print(result)

# pass statement
result = 0
# We can also skip the none value and continue to loop
for value in L2:
    if value is None:
        pass
    else:
        result += value
print(result)

# Define function
def my_add(x, y):
    return x + y  # this function now returns the sum

print(my_add(1, 5))

def multiply(x, y):
    return x * y

print(multiply(4, 8))