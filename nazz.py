b6 # Empty list
prospective_students = []
print("empty list:", prospective_students)

# List of random numbers
numbers = [1, 7, 65, 2, 43, 13]
print("Random numbers:", numbers)

# Ascending order
numbers.sort()
print("Ascending order:", numbers)

# Descending order
numbers.sort(reverse=True)
print("Descending order:", numbers)

# Add 25 to each element and create a new list
updated_numbers = [number + 25 for number in numbers]
print(updated_numbers)
# Or
updated_number = []
for number in numbers:
    number += 25
    updated_number.append(number)
print("Updated numbers (each +25):", updated_number)

# Total number of elements
print("Total number of elements:", len(numbers))

# Print the sum of the elements
print("Sum of elements:", sum(numbers))

# Print the lowest and the biggest element
print("Lowest element:", min(numbers))
print("Biggest element:", max(numbers))