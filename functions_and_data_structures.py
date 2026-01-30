# Function to calculate the area of a rectangle
def calculate_area(length, width):
    return length * width

# Ask the user to enter the length of the rectangle
length = float(input("Enter the length: "))

# Ask the user to enter the width of the rectangle
width = float(input("Enter the width: "))

# Call the function to calculate the area
area = calculate_area(length, width)

# Display the calculated area
print("The area of the rectangle is:", area)
