Functions in Python allow you to organize code into reusable blocks. You define a function using the `def` keyword, followed by the function name and parentheses. Inside the parentheses, you can specify parameters, which are variables that the function can accept.

## Basic syntax
```
def data(first_name, last_name, age):
    print("Hello " + first_name)
    print("Your last name is " + last_name)
    print("You are " + str(age) + " years old")
```
In this function, `data` takes three parameters: `first_name`, `last_name`, and `age`. When you call the function with specific arguments, it prints a greeting and details based on those arguments.

## Call the function
To call the function, you pass the required arguments:
```
first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
age = int(input("What is your age?: "))

greet_user(first_name, last_name, age)
```
This code collects user input and then calls the `greet_user` function with those inputs. The function then prints a personalized message.

Functions help you avoid repetition, make your code more readable, and allow you to manage complex tasks by breaking them into smaller, manageable pieces.

Made by danilo.zs
