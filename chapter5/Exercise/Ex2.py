numbers = []

for i in range(8):
    number = input(f"Enter your {i+1} number")
    numbers.append(number)

unique_number = set(numbers)

print(unique_number)