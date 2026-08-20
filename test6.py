#This program finds the largest number in a list of numbers. It initializes the maximum value to the first number in the list and then iterates through the list, updating the maximum value whenever it encounters a larger number. Finally, it prints the largest number found.
numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f"The largest number is: {max}")
