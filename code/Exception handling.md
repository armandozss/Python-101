Exception handling is a way to manage errors that occur during the execution of a program, ensuring that your program can handle problems gracefully and continue running.

## Try block
```
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a / b
```
The `try` block contains the code that might raise an exception. In this example, it includes user input and a division operation.

## Except blocks
```
except ZeroDivisionError as e:
    print("You can't divide by 0 LMFAO")
except ValueError as e:
    print("Enter only entire numbers please")
except Exception as e:
    print("Enter only numbers please")
```
These blocks handle specific types of exceptions. The first `except` block catches attempts to divide by zero, the second handles invalid input that cannot be converted to integers, and the last one catches any other exceptions that were not specifically handled.

## Else block
```
else:
    print(c)
```
The `else` block runs if no exceptions were raised in the `try` block. Here, it prints the result of the division.

## Finally block
```
finally:
    print("This will always appear")
```
The `finally` block runs no matter what, whether an exception was raised or not. It's useful for clean-up actions like closing files or releasing resources.

Exception handling helps you control how your program responds to errors, allowing you to provide user-friendly messages and ensure important code runs regardless of errors.

Made by danilo.zs
