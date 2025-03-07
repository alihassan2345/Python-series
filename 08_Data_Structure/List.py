# Python mein list ek ordered collection hoti hai jo mutable (changeable) hoti hai.
# Creating a list
fruits = ["apple", "banana", "cherry", "mango"]

# Accessing elements
print(fruits[0])   # apple
print(fruits[-1])  # mango (last item)

# Modifying elements
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry', 'mango']

# Adding elements
fruits.append("orange")  # Adds at the end
fruits.insert(1, "grape")  # Inserts at index 1

# Removing elements
fruits.remove("cherry")  # Removes by value
popped = fruits.pop()  # Removes last element

print(fruits)
