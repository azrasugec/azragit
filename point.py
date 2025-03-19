# This script calculates min, max, and average of a list from 1 to 10

# Define a list from 1 to 10
numbers = list(range(1, 11))

# Calculate min, max, and average
min_value = min(numbers)
max_value = max(numbers)
average_value = sum(numbers) / len(numbers)

# Print the results
print(f'Min: {min_value}')
print(f'Max: {max_value}')
print(f'Average: {average_value:.2f}')
