# ------------------------
# STRINGS
# ------------------------
print("=== STRINGS ===")
s = "Hello World"
print(s)                          # A string
print(s[0])                       # Indexing (first character)
print(s[0:5])                     # Slicing (first 5 characters)
print(s.upper())                  # Methods (convert to uppercase)
print("World" in s)               # Membership test (returns True)

# ------------------------
# LISTS
# ------------------------
print("\n=== LISTS ===")
my_list = [1, 2, 3, "apple", "banana"]
print(my_list)                    # Heterogeneous data allowed
print(my_list[2])                 # Access element by index
my_list.append("cherry")          # Add an element
print(my_list)
my_list.remove("apple")           # Remove an element
print(my_list)
print(len(my_list))               # Length of the list

# ------------------------
# TUPLES
# ------------------------
print("\n=== TUPLES ===")
my_tuple = (10, 20, 30, "dog")
print(my_tuple)
print(my_tuple[1])                # Indexing works
# my_tuple[1] = 99                # ERROR: Tuples are immutable!
print(len(my_tuple))              # Length works

# ------------------------
# SETS
# ------------------------
print("\n=== SETS ===")
my_set = {1, 2, 3, 3, 4}
print(my_set)                     # Duplicates are automatically removed
my_set.add(5)                     # Add element
print(my_set)
my_set.remove(2)                  # Remove element
print(my_set)
print(3 in my_set)                # Membership test

# ------------------------
# DICTIONARIES
# ------------------------
print("\n=== DICTIONARIES ===")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
print(my_dict["name"])            # Access value by key
my_dict["age"] = 26               # Update value
print(my_dict)
my_dict["country"] = "USA"        # Add new key-value pair
print(my_dict)
print(my_dict.keys())             # Get all keys
print(my_dict.values())           # Get all values
print(my_dict.items())            # Get key-value pairs


# ------------------------
# STRINGS
# ------------------------
print("=== STRINGS ===")
s = "Hello World"
print("Original:", s)

# Reverse string (slicing with step -1)
reversed_s = s[::-1]
print("Reversed:", reversed_s)


# ------------------------
# LISTS
# ------------------------
print("\n=== LISTS ===")
my_list = [1, 2, 3, 4, 5]
print("Original:", my_list)

# Method 1: Using slicing
print("Reversed (slice):", my_list[::-1])

# Method 2: Using reverse() (in-place)
my_list.reverse()
print("Reversed (in-place):", my_list)


# ------------------------
# TUPLES
# ------------------------
print("\n=== TUPLES ===")
my_tuple = (10, 20, 30, 40)
print("Original:", my_tuple)

# Tuples are immutable, so we create a new reversed tuple
reversed_tuple = my_tuple[::-1]
print("Reversed:", reversed_tuple)


# ------------------------
# SETS
# ------------------------
print("\n=== SETS ===")
my_set = {1, 2, 3, 4, 5}
print("Original:", my_set)

# Sets are unordered → they don’t have a "reverse" concept.
# But if you *want* to reverse the iteration order, first convert to list:
reversed_set = list(my_set)[::-1]
print("Reversed order (as list):", reversed_set)


# ------------------------
# DICTIONARIES
# ------------------------
print("\n=== DICTIONARIES ===")
my_dict = {"a": 1, "b": 2, "c": 3}
print("Original:", my_dict)

# In Python 3.7+, dicts remember insertion order.
# Reverse by converting items to a list and flipping:
reversed_dict = dict(reversed(list(my_dict.items())))
print("Reversed:", reversed_dict)


import random

# ------------------------
# RANGE with STRINGS
# ------------------------
print("=== RANGE with STRINGS ===")
s = "PYTHON"
for i in range(len(s)):          # Using range with string indices
    print(i, "->", s[i])


# ------------------------
# RANGE with LISTS
# ------------------------
print("\n=== RANGE with LISTS ===")
my_list = [10, 20, 30, 40, 50]
for i in range(len(my_list)):
    print(f"Index {i}: {my_list[i]}")


# ------------------------
# RANGE with TUPLES
# ------------------------
print("\n=== RANGE with TUPLES ===")
my_tuple = ("apple", "banana", "cherry")
for i in range(len(my_tuple)):
    print(f"Index {i}: {my_tuple[i]}")


# ------------------------
# RANGE with SETS
# ------------------------
print("\n=== RANGE with SETS ===")
my_set = {"cat", "dog", "fish"}
# sets are unordered → convert to list for indexed iteration
my_set_list = list(my_set)
for i in range(len(my_set_list)):
    print(f"Index {i}: {my_set_list[i]}")


# ------------------------
# RANGE with DICTIONARIES
# ------------------------
print("\n=== RANGE with DICTIONARIES ===")
my_dict = {"a": 100, "b": 200, "c": 300}
keys = list(my_dict.keys())
for i in range(len(keys)):
    key = keys[i]
    print(f"Index {i}: {key} -> {my_dict[key]}")


# ======================================================
# RANDOM NUMBERS with SEED in STRING, LIST, TUPLE, SET, DICT
# ======================================================

print("\n=== RANDOM with SEED ===")
random.seed(42)   # Ensures repeatable results

# STRING: choose random characters
letters = "abcdefg"
rand_chars = "".join(random.choice(letters) for _ in range(5))
print("Random string:", rand_chars)

# LIST: generate random list of numbers
rand_list = [random.randint(1, 100) for _ in range(5)]
print("Random list:", rand_list)

# TUPLE: generate random tuple of numbers
rand_tuple = tuple(random.randint(1, 50) for _ in range(4))
print("Random tuple:", rand_tuple)

# SET: generate random set (unique elements automatically)
rand_set = {random.randint(1, 20) for _ in range(5)}
print("Random set:", rand_set)

# DICT: random dict with keys a,b,c... and random values
keys = ["a", "b", "c", "d"]
rand_dict = {k: random.randint(1, 10) for k in keys}
print("Random dict:", rand_dict)

# ------------------------
# RANGE vs LEN
# ------------------------

s = "HELLO"

# len(s) just gives ONE integer (the length)
print(len(s))
# Output: 5
# You cannot loop over len(s), it's not iterable.
# Example: for x in len(s): -> ERROR

# range(len(s)) gives a sequence of numbers from 0 up to len(s)-1
for i in range(len(s)):
    print(i, "->", s[i])
# Output:
# 0 -> H
# 1 -> E
# 2 -> L
# 3 -> L
# 4 -> O


# ------------------------
# WHY USE "_" instead of "i"
# ------------------------

# Convention: use "_" when you do NOT care about the loop variable
# Example: repeat something 5 times, but index is irrelevant
for _ in range(5):
    print("Hello")

# Here we don't use the value of "_" inside the loop body.
# "_" signals to other programmers: "I don’t need this variable"
# If we used "i", it would look like we intend to use the index.
s = "HELLO"

# ------------------------
# 1. Using len(s)
# ------------------------
print("len(s):", len(s))
# Just returns the length (5 here).
# It’s not iterable, so you cannot do "for x in len(s)".
# Example: for x in len(s): -> ERROR


# ------------------------
# 2. Using range(len(s))
# ------------------------
print("\nUsing range(len(s)):")
for i in range(len(s)):
    print(i, "->", s[i])
# This gives indices 0..4, useful if you need the index AND the character.


# ------------------------
# 3. Direct iteration (no range, no index)
# ------------------------
print("\nDirect iteration over the string:")
for ch in s:
    print(ch)
# This is cleaner if you only need the characters, not their positions.


# ------------------------
# WHY USE "_"
# ------------------------
print("\nUsing '_' when index is not needed:")
for _ in range(3):
    print("Repeat something")
# "_" is a throwaway variable → signals "we don’t use this value"
# If we wrote "for i in range(3):", it would look like we planned to use i.


import random

random.seed(42)  # reproducibility

# ------------------------
# LIST (5 random numbers)
# ------------------------
rand_list = random.sample(range(1, 100), 5)   # unique numbers
print("Random list:", rand_list)


# ------------------------
# TUPLE (5 random numbers)
# ------------------------
rand_tuple = tuple(random.sample(range(1, 100), 5))
print("Random tuple:", rand_tuple)


# ------------------------
# SET (5 random numbers)
# ------------------------
rand_set = set(random.sample(range(1, 100), 5))
print("Random set:", rand_set)


# ------------------------
# STRING (random characters)
# ------------------------
# Here we pick 5 random lowercase letters
import string
rand_string = ''.join(random.choices(string.ascii_lowercase, k=5))
print("Random string:", rand_string)


import random

# ------------------------
# 1. Explicit way
# ------------------------
my_list = list([1, 2, 3])    # using list() constructor
print("Explicit list:", my_list)


# ------------------------
# 2. Using square brackets []   ✅ most common
# ------------------------
my_list2 = [1, 2, 3]
print("List with []:", my_list2)
# Square brackets [] are Python's literal syntax for creating a list.


# ------------------------
# 3. Using list comprehension
# ------------------------
my_list3 = [x**2 for x in range(5)]   # squares of numbers 0–4
print("List comprehension:", my_list3)
# Even though 'list' keyword is not written,
# the [] itself creates a list object.


# ------------------------
# 4. Functions that directly return a list
# ------------------------
rand_list = random.sample(range(1, 100), 5)
print("Random list:", rand_list)
# Here random.sample() already RETURNS a list.
# We didn't write 'list(...)', but result is a list object.


# ------------------------
# 5. From range without list keyword
# ------------------------
r = range(5)              # this is a range object, not a list
print("Range object:", r)

r_list = list(r)          # explicitly convert to list
print("Converted to list:", r_list)
print(type([1,2,3]))          # <class 'list'>
print(type(random.sample(range(10), 3)))  # <class 'list'>
print(type(range(5)))         # <class 'range'>
import sys

print("=" * 50)
print("UNDERSTANDING RANGE OBJECTS")
print("=" * 50)

# 1. BASIC DIFFERENCE: Range vs List
print("\n1. BASIC DIFFERENCE:")
print("-" * 20)

# Creating a range object (lazy evaluation)
r = range(10)
print(f"range(10) creates: {r}")
print(f"Type: {type(r)}")

# Converting range to list (eager evaluation - creates all values immediately)
lst = list(range(10))
print(f"list(range(10)) creates: {lst}")
print(f"Type: {type(lst)}")

# 2. MEMORY EFFICIENCY DEMONSTRATION
print("\n2. MEMORY USAGE COMPARISON:")
print("-" * 30)

# Range object - stores only start, stop, step (very small memory)
big_range = range(1000000)  # 1 million numbers
print(f"Memory used by range(1000000): {sys.getsizeof(big_range)} bytes")

# List object - stores all 1 million integers (much larger memory)
big_list = list(range(1000000))
print(f"Memory used by list(range(1000000)): {sys.getsizeof(big_list)} bytes")
print(f"Memory difference: {sys.getsizeof(big_list) - sys.getsizeof(big_range)} bytes")

# 3. LAZY EVALUATION IN ACTION
print("\n3. LAZY EVALUATION DEMONSTRATION:")
print("-" * 35)

# Range doesn't generate values until you ask for them
print("Creating range(5)...")
my_range = range(5)
print("Range created! No values generated yet.")

print("\nNow iterating through range (values generated on-demand):")
for i, value in enumerate(my_range):
    print(f"  Iteration {i}: Generated value {value}")

# 4. ACCESSING ELEMENTS
print("\n4. ACCESSING ELEMENTS:")
print("-" * 25)

r = range(0, 20, 2)  # Even numbers from 0 to 18
print(f"Range: {r}")
print(f"First element r[0]: {r[0]}")
print(f"Third element r[2]: {r[2]}")
print(f"Length: {len(r)}")
print("Range supports indexing but doesn't store all values!")

# 5. ITERATION COMPARISON
print("\n5. ITERATION BEHAVIOR:")
print("-" * 25)

print("Iterating with range(5):")
for num in range(5):  # Generates values one by one
    print(f"  {num}")

print("Iterating with list(range(5)):")
for num in list(range(5)):  # All values already in memory
    print(f"  {num}")

# 6. PRACTICAL EXAMPLES
print("\n6. WHEN TO USE EACH:")
print("-" * 22)

# Use range() for simple loops (memory efficient)
print("Good use of range() - just looping:")
total = 0
for i in range(100):  # No need to create a list
    total += i
print(f"Sum of 0-99: {total}")

# Use list(range()) when you need list operations
print("\nWhen you need a list (for list methods):")
numbers = list(range(1, 11))
print(f"Original list: {numbers}")
numbers.append(11)  # List method
numbers.remove(5)   # List method
print(f"After modifications: {numbers}")

# 7. MEMORY EFFICIENCY WITH LARGE RANGES
print("\n7. EFFICIENCY WITH LARGE NUMBERS:")
print("-" * 35)

# This is efficient - no memory used for storing values
print("Checking if 500000 is in range(1000000)...")
result = 500000 in range(1000000)  # Very fast, no list created
print(f"Result: {result}")

# This would be inefficient - creates entire list first
print("DON'T do: 500000 in list(range(1000000)) - wastes memory!")

# 8. RANGE PARAMETERS
print("\n8. RANGE PARAMETERS:")
print("-" * 20)

# range(start, stop, step)
examples = [
    (range(5), "range(5) - start=0, stop=5, step=1"),
    (range(2, 8), "range(2, 8) - start=2, stop=8, step=1"),
    (range(0, 10, 2), "range(0, 10, 2) - start=0, stop=10, step=2"),
    (range(10, 0, -1), "range(10, 0, -1) - countdown")
]

for r, description in examples:
    print(f"{description}: {list(r)}")

print("\n" + "=" * 50)
print("KEY TAKEAWAY:")
print("Range objects are LAZY - they generate values on-demand")
print("Lists are EAGER - they store all values immediately")
print("Use range() for loops, list(range()) when you need list operations")
print("=" * 50)


print("=" * 60)
print("UNDERSTANDING ENUMERATE() AND LOOP ALTERNATIVES")
print("=" * 60)

my_range = range(5)  # Creates range(0, 1, 2, 3, 4)

# 1. ORIGINAL CODE EXPLANATION
print("\n1. ORIGINAL CODE WITH ENUMERATE:")
print("-" * 40)
print("enumerate() gives us both index AND value:")

for i, value in enumerate(my_range):
    print(f"  Iteration {i}: Generated value {value}")
    # i = index (0, 1, 2, 3, 4)
    # value = actual value from range (0, 1, 2, 3, 4)
    # In this case they're the same, but that's coincidental!

# 2. WHAT ENUMERATE ACTUALLY RETURNS
print("\n2. WHAT ENUMERATE() PRODUCES:")
print("-" * 35)
print("enumerate(range(5)) produces these pairs:")
for pair in enumerate(range(5)):
    print(f"  {pair}")  # Shows (index, value) tuples

# 3. ALTERNATIVE WAYS TO WRITE THE SAME LOOP
print("\n3. ALTERNATIVE METHODS:")
print("-" * 25)

print("Method 1 - Simple for loop (no index):")
for value in my_range:
    print(f"  Generated value {value}")

print("\nMethod 2 - Manual counter:")
counter = 0
for value in my_range:
    print(f"  Iteration {counter}: Generated value {value}")
    counter += 1

print("\nMethod 3 - Using range with len():")
my_list = list(my_range)  # Convert to list to use len()
for i in range(len(my_list)):
    print(f"  Iteration {i}: Generated value {my_list[i]}")

print("\nMethod 4 - Using zip() with range:")
for i, value in zip(range(len(my_range)), my_range):
    print(f"  Iteration {i}: Generated value {value}")

print("\nMethod 5 - List comprehension with enumerate (for display):")
result = [(i, value) for i, value in enumerate(my_range)]
for i, value in result:
    print(f"  Iteration {i}: Generated value {value}")

# 4. ENUMERATE WITH DIFFERENT START VALUES
print("\n4. ENUMERATE WITH CUSTOM START:")
print("-" * 35)
print("enumerate() can start counting from any number:")

for i, value in enumerate(my_range, start=1):  # Start counting from 1
    print(f"  Iteration {i}: Generated value {value}")

for i, value in enumerate(my_range, start=10):  # Start counting from 10
    print(f"  Iteration {i}: Generated value {value}")

# 5. PRACTICAL EXAMPLES WHERE ENUMERATE SHINES
print("\n5. WHEN ENUMERATE() IS MOST USEFUL:")
print("-" * 40)

# Example 1: Processing a list with index information
fruits = ['apple', 'banana', 'orange']
print("Numbering items in a list:")
for i, fruit in enumerate(fruits, start=1):
    print(f"  {i}. {fruit}")

# Example 2: Finding positions of specific items
numbers = [10, 25, 30, 25, 40]
print(f"\nFinding positions of 25 in {numbers}:")
for i, num in enumerate(numbers):
    if num == 25:
        print(f"  Found 25 at index {i}")

# Example 3: Creating index-value pairs
text = "Hello"
print(f"\nCharacter positions in '{text}':")
for i, char in enumerate(text):
    print(f"  Position {i}: '{char}'")

# 6. COMPARISON: WHEN ENUMERATE IS BETTER
print("\n6. WHY USE ENUMERATE() VS ALTERNATIVES:")
print("-" * 45)

data = ['a', 'b', 'c', 'd']

print("❌ Less Pythonic (manual counter):")
counter = 0
for item in data:
    print(f"  {counter}: {item}")
    counter += 1

print("\n❌ Less Pythonic (range + len):")
for i in range(len(data)):
    print(f"  {i}: {data[i]}")

print("\n✅ Pythonic with enumerate:")
for i, item in enumerate(data):
    print(f"  {i}: {item}")

print("\n" + "=" * 60)
print("KEY POINTS ABOUT ENUMERATE:")
print("• enumerate(iterable) returns (index, value) pairs")
print("• Default start is 0, but you can change it: enumerate(data, start=1)")
print("• More readable than manual counters or range(len())")
print("• Works with any iterable: lists, ranges, strings, etc.")
print("• The 'Pythonic' way to get both index and value")
print("=" * 60)


import numpy as np
print("COMPARISON: np.int16 vs int")
print("=" * 30)
# Output: COMPARISON: np.int16 vs int
#         ==============================

# Create arrays with different dtypes
array_int16 = np.ones(5, dtype=np.int16)
array_int = np.ones(5, dtype=int)

print(f"np.int16 array: {array_int16}")
# Output: np.int16 array: [1 1 1 1 1]

print(f"dtype=int array: {array_int}")
# Output: dtype=int array: [1 1 1 1 1]

print(f"\nnp.int16 actual type: {array_int16.dtype}")
# Output: np.int16 actual type: int16

print(f"dtype=int actual type: {array_int.dtype}")
# Output: dtype=int actual type: int64

# Key differences:
print(f"\nMemory per number:")
# Output: Memory per number:

print(f"np.int16: {array_int16.itemsize} bytes per number")
# Output: np.int16: 2 bytes per number

print(f"dtype=int: {array_int.itemsize} bytes per number")
# Output: dtype=int: 8 bytes per number

print(f"\nValue range:")
# Output: Value range:

print(f"np.int16: {np.iinfo(np.int16).min} to {np.iinfo(np.int16).max}")
# Output: np.int16: -32768 to 32767

print(f"dtype=int: {np.iinfo(array_int.dtype).min} to {np.iinfo(array_int.dtype).max}")
# Output: dtype=int: -9223372036854775808 to 9223372036854775807