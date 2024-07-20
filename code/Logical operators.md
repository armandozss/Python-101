Logical operators are essential tools in programming that help us make decisions based on multiple conditions. In Python, the three primary logical operators are `and`, `or`, and `not`. They allow us to combine multiple conditions into a single `if statement`, making the code more flexible and powerful.

## And, Or
The `and` operator checks if both conditions are true, while the or operator checks if at least one condition is true.

```
Copy code
temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("It's a nice day, Go outside!!!")
elif temp <= 0 or temp >= 30:
    print("It's a really bad day, stay at home")
```
Now let's break it down:
- `temp = int(input("What is the temperature outside?: "))`: This line prompts the user to enter the temperature and converts the input to an integer.
- `if temp >= 0 and temp <= 30:`: This checks if the temperature is between 0 and 30 inclusive. If both conditions are true, the code block under this line will execute.
- `print("It's a nice day, Go outside!!!")`: This message is displayed if the temperature is within the specified range.
- `elif temp <= 0 or temp >= 30:`: This checks if the temperature is less than or equal to 0, or greater than or equal to 30. If at least one of these conditions is true, the code block under this line will execute.
- `print("It's a really bad day, stay at home")`: This message is displayed if the temperature is outside the specified range.

## Not
The `not` operator inverts the condition. If the condition is true, `not` makes it false, and vice versa.
```
temp2 = int(input("What is the temperature outside?: "))

if not (temp2 >= 0 and temp2 <= 30):
    print("It's a really bad day, stay at home")
else:
    print("It's a nice day, Go outside!!!")
```
- `temp2 = int(input("What is the temperature outside?: "))`: This line prompts the user to enter the temperature and converts the input to an integer.
- `if not (temp2 >= 0 and temp2 <= 30):`: This checks if the temperature is not between 0 and 30 inclusive. If this condition is true, the code block under this line will execute.
- `print("It's a really bad day, stay at home")`: This message is displayed if the temperature is outside the specified range.
- `else:`: If the `not` condition is false (the temperature is between 0 and 30 inclusive), the code block under this line will execute.
- `print("It's a nice day, Go outside!!!")`: This message is displayed if the temperature is within the specified range.

Logical operators are powerful tools for controlling the flow of your programs. They help you make decisions based on multiple conditions.

Made by danilo.zs
