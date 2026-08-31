#This code snippet creates a list of unique numbers from the given list `numbers`, sorts them in ascending order, and then prints the sorted list of unique numbers.
numbers = [1, 7, 4, 9, 2, 7, 1, 4, 7, 8]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
uniques.sort()
print(uniques)