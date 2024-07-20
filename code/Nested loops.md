Nested loops are loops inside other loops. They are used when you need to perform repetitive tasks within repetitive tasks. A common use case for nested loops is working with two-dimensional data, such as grids or matrices.

## Basic example
```
rows = int(input("How many rows do you want to put?: "))
columns = int(input("How many columns do you want to have in this?: "))
symbol = input("What symbol do you want to put?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
```
*Now, let’s break it down:*
- `rows = int(input("How many rows do you want to put?: "))`: Prompts the user to enter the number of rows for the grid and converts it to an integer.
- `columns = int(input("How many columns do you want to have in this?: "))`: Prompts the user to enter the number of columns for the grid and converts it to an integer.
- `symbol = input("What symbol do you want to put?: ")`: Prompts the user to enter the symbol they want to use to fill the grid.

*Loop Breakdown:*
- `for i in range(rows):`: This is the outer loop. It iterates through each row.
    - `for j in range(columns):`: This is the inner loop. It iterates through each column within the current row.
        - `print(symbol, end="")`: This prints the symbol without moving to a new line. It fills out the columns in the current row.
    - `print()`: After the inner loop completes (A.K.A after filling all columns for a row), this `print()` function moves to the next line, creating a new row in the output.

## Output
If you entered 3 for rows, 5 for columns, and `*` for the symbol, the output will look like this:
```
*****
*****
*****
```

Nested loops are essential for handling multi-dimensional data. They allow you to work with structures like grids, matrices, or tables. By combining multiple loops, you can handle complex tasks efficiently.

Made by danilo.zs
