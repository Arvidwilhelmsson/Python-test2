#This program prints 'x' characters based on the numbers provided in the list. Each number in the list represents the number of 'x' characters to print on that line.
numbers = [1,2,3,4,5,6,7]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'X'
    print(output)
    