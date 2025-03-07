# Dictionary key-value pair format mein data store karta hai.
 # Creating a dictionary
student = {
    "name": "Ali",
    "age": 20,
    "course": "Python"
}

# Accessing values
print(student["name"])  # Ali

# Modifying values
student["age"] = 21

# Adding new key-value pair
student["city"] = "Karachi"

# Removing key-value pair
del student["course"]

print(student)
