import math

# Fixed values of C and H
C = 50
H = 30

# Ask the user for a comma-separated string of numbers
user_input = input("Enter a comma-separated string of numbers: ")

# Split the user input into a list of numbers
numbers = user_input.split(',')

# Calculate and print the values using the formula for each number in the list
results = []
for num in numbers:
    D = int(num)
    Q = int(math.sqrt((2 * C * D) / H))
    results.append(Q)

# Convert the results list to a comma-separated string and print the output
output = ','.join(str(q) for q in results)
print(output)
