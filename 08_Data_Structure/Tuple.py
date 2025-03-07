# Tuple bhi list ki tarah hoti hai, lekin immutable hoti hai (change nahi kar sakte).

numbers = (10, 20, 30, 40)

print(numbers[0])  # 10
print(numbers[-1]) # 40
print(numbers)

# Tuples are immutable
# numbers[1] = 25  ❌ This will give an error
