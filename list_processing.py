# Create an empty list to store the numbers
numbers = []

# Ask the user to input 5 numbers
for i in range(5):
    num = int(input(f"Input a number {i + 1}: "))
    numbers.append(num)  # Add the number to the list

# Sort the numbers from highest to lowest
numbers.sort(reverse=True)

# Display the sorted numbers
print("Numbers from highest to lowest:", numbers)
