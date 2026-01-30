numbers = []

for i in range(5):
    num = int(input(f"Input a number {i + 1}: "))
    numbers.append(num)

numbers.sort(reverse=True)

print("Numbers from highest to lowest:", numbers)
