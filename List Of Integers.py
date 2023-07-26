import random

# Function to calculate the sum, average, largest, and smallest number without using built-in functions
def calculate_stats(numbers):
    sum_num = 0
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        sum_num += num
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    average = sum_num / len(numbers)
    return sum_num, average, largest, smallest

# Function to remove duplicates from a list and count the unique numbers
def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers, len(unique_numbers)

# Create a list of 10 random integers between -100 and 100
random_numbers = [random.randint(-100, 100) for _ in range(10)]

# Print the list of numbers in a single line
print("List of numbers:", random_numbers)

# Print the list of numbers sorted in descending order
sorted_numbers = sorted(random_numbers, reverse=True)
print("Sorted numbers:", sorted_numbers)

# Calculate and print the sum of all the numbers
sum_numbers = sum(random_numbers)
print("Sum of all numbers:", sum_numbers)

# Create a list containing the first and the last numbers
first_and_last_numbers = [random_numbers[0], random_numbers[-1]]
print("First and last numbers:", first_and_last_numbers)

# Create a list of all the numbers greater than 50
numbers_greater_than_50 = [num for num in random_numbers if num > 50]
print("Numbers greater than 50:", numbers_greater_than_50)

# Create a list of all the numbers smaller than 10
numbers_smaller_than_10 = [num for num in random_numbers if num < 10]
print("Numbers smaller than 10:", numbers_smaller_than_10)

# Create a list of all the numbers squared
numbers_squared = [num ** 2 for num in random_numbers]
print("Numbers squared:", ' '.join(map(str, numbers_squared)))

# Remove duplicates from the list of numbers
unique_numbers, unique_count = remove_duplicates(random_numbers)
print("Numbers without duplicates:", unique_numbers)
print("Number of unique numbers:", unique_count)

# Calculate the average, largest, and smallest number without using built-in functions
sum_num, average, largest, smallest = calculate_stats(random_numbers)
print("Average of all numbers:", average)
print("Largest number:", largest)
print("Smallest number:", smallest)
