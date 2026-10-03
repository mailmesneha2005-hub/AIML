numbers = [10, 20, 30, 40, 50]

# Loop + conditional
for number in numbers:
    if number > 25:
        print(number, "is greater than 25")
    else:
        print(number, "is 25 or less")


# Function
def calculate_sum(numbers):
    return sum(numbers)


total = calculate_sum(numbers)
print("Total:", total)