#This program iterates through a 2D list (matrix) and prints each item. It uses nested loops to access each row and then each item within that row, printing them one by one.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)