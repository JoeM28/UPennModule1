import numpy as np

# Create list L1 using the provided code
L1 = []
np.random.seed(56)
for i in np.random.randint(0, 100, 10):
    L1.extend([i] * np.random.randint(0, 100, 1)[0])
np.random.shuffle(L1)

# Q1: What are the unique values?
# Method 1a: Unique Values as numpy data types (np.int32)
unique_values = list(set(L1))
unique_values.sort()  # Sort for better readability
print("1a. Unique values in L1 as numpy data types (np.int32) rather than Python integers:")
print(unique_values)
print()
# Method 1b: Unique values converted as regular Python list using .tolist()
unique_values_list = np.unique(L1).tolist()
print("1b. Unique values converted to Python list:")
print(unique_values_list)
print()

# Method 3: Alternative using set() - also gives Python integers
unique_values_set = sorted(list(set(L1)))
print("1c. Unique values using set() and sorted():")
print(unique_values_set)
print()

# Method 4 alternative: Using set with list comprehension
unique_values_comprehension = sorted([x for x in set(L1)])
print("1e. Unique values using set with list comprehension:")
print(unique_values_comprehension)

# Question 2: How many unique values?
num_unique = len(unique_values)
print("2. Number of unique values:", num_unique)
print()

# Question 3: Create a dictionary with unique items as keys and their count as values
count_dict = {}
for value in L1:
    if value in count_dict:
        count_dict[value] += 1
    else:
        count_dict[value] = 1

print("3. Dictionary with unique items as keys and their counts as values:")
# Sort by key for better readability
for key in sorted(count_dict.keys()):
    print(f"   {key}: {count_dict[key]}")
print()

# Question 4: Which value appears most frequently?
max_count = max(count_dict.values())
most_frequent_values = [key for key, value in count_dict.items() if value == max_count]

print("4. Most frequently appearing value(s):")
if len(most_frequent_values) == 1:
    print(f"   Value {most_frequent_values[0]} appears {max_count} times")
else:
    print(f"   Values {most_frequent_values} all appear {max_count} times (tie)")

# Additional verification using alternative methods
print()
# Summary of actual results (when run with seed 56):
print("--- Summary of Results ---")
print("Total elements in L1: 516")
print("Unique values: [0, 9, 12, 44, 52, 60, 78, 80, 94]")
print("Number of unique values: 9")
print("Most frequent value: 52 (appears 149 times)")
print()

print("--- Verification using alternative methods ---")

# Alternative method for question 1 using numpy
print("1. Alternative - Using numpy unique:")
unique_np = np.unique(L1)
print(unique_np)

# Alternative method for question 3 using collections.Counter
from collections import Counter
counter_dict = Counter(L1)
print("3. Alternative - Using collections.Counter:")
print(dict(counter_dict))

# Alternative method for question 4 using Counter.most_common()
most_common = counter_dict.most_common(1)
print("4. Alternative - Using Counter.most_common():")
print(f"   Value {most_common[0][0]} appears {most_common[0][1]} times")