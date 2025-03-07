# Set ek unordered collection hai jo duplicate values allow nahi karta.
my_set = {1, 2, 3, 4, 4, 5}

print(my_set)  # {1, 2, 3, 4, 5}  (duplicates removed automatically)

# Adding elements
my_set.add(6)

# Removing elements
my_set.remove(3)

print(my_set)
