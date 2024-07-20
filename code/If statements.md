If statements are a fundamental part of programming. They allow you to execute code based on certain conditions, making your programs dynamic and interactive. 

First, let's see a basic example. 
```
age = int(input("How old are you?: "))

if age >= 18:
    print("Nice, you can enter here")
else:
    print("You can't enter")

```
Now let's break it down:
- `age = int(input("How old are you?: "))`: This line prompts the user to enter their age and converts the input to an integer.
- `if age >= 18:`: This checks if the age is 18 or greater. If this condition is true, the code block under this line will execute.
- `print("Nice, you can enter here")`: This message is displayed if the condition is met.
- `else:`: If the first condition is not met (i.e., age is less than 18), the code block under this line will execute.
- `print("You can't enter")`: This message is displayed if the age is less than 18.

## The Purpose of the Colon (:)
The colon `(:)` is used to indicate the start of an indented block of code. It is a key part of the syntax for defining control flow statements like `if`, `elif`, `else`, `for`, `while`, and function definitions.

If statements, along with elif and else, are powerful tools for controlling the flow of your programs. They help you make decisions based on different conditions.

Made by danilo.zs
