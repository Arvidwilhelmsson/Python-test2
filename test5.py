#This program prints 'x' characters based on the numbers provided in the list. Each number in the list represents the number of 'x' characters to print on that line.
numbers = [5,2,5,2,2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)