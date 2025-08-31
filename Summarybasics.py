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
