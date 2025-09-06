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
unique_values.sort()  # Sorting for readability
print("1. Method A- Unique values in L1 as numpy data types (np.int32) rather than Python integers:")
print(unique_values)
print()
# Method 1b: Unique values converted as regular Python list using .tolist()
unique_values_list = np.unique(L1).tolist()
print("1. Method B- Unique values converted to Python list:")
print(unique_values_list)
print()

# Q2: How many unique values?
num_unique = len(unique_values)  # Using the len function
print("2. Number of unique values:", num_unique)
print()

# Q3: Create a dictionary with unique items as keys and their count as values
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

# Q4: Which value appears most frequently?
max_count = max(count_dict.values())
most_frequent_values = [key for key, value in count_dict.items() if value == max_count]

print("4. Most frequently appearing value(s):")
if len(most_frequent_values) == 1:
    print(f"   Value {most_frequent_values[0]} appears {max_count} times")
else:
    print(f"   Values {most_frequent_values} all appear {max_count} times (tie)")



    def pow(x, n):
        """
        Calculates x raised to the power n (x^n).

        This function handles positive, negative, and zero exponents
        without using the built-in `**` operator.

        Args:
            x (float or int): The base number.
            n (int): The exponent.

        Returns:
            float: The result of x^n.
        """
    # Handle the case where the exponent is 0
    if n == 0:
        return 1

    # Handle the case where the exponent is negative
    if n < 0:
        x = 1 / x
        n = -n

    # Perform repeated multiplication for n times
    result = 1
    for _ in range(n):
        result *= x

    return result

# Calculate pow(2, 10)
result_2_10 = pow(2, 10)
print(f"2 raised to the power of 10 is: {result_2_10}")

# Calculate pow(3, -3)
result_3_neg_3 = pow(3, -3)
print(f"3 raised to the power of -3 is: {result_3_neg_3}")
