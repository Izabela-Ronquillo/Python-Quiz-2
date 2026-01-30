# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is greater than zero
if number > 0:
    print("The number is Positive.")

# Check if the number is less than zero
elif number < 0:
    print("The number is Negative.")

# If the number is neither positive nor negative, it is zero
else:
    print("The number is Zero.")
