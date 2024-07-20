A `while` loop is a control flow statement that repeatedly executes a block of code as long as a specified condition is true. It's useful when you want to repeat an action multiple times but don't know in advance how many times you'll need to run the loop.

## Basic example
```
name = ""
while len(name) == 0:
    name = input("What is your name?: ")

print("Hello, nice to meet you " + name)
```
Now, let's break it down:
- `name = ""`: We start by initializing the `name` variable with an empty string.
- `while len(name) == 0:`: This line sets up a `while` loop that will keep running as long as the length of the `name` variable is 0. In other words, it continues running while `name` is an empty string.
- `name = input("What is your name?: ")`: Inside the loop, we ask the user to input their name. This will replace the empty `name` with the user's input. Once the user provides a name (the length of `name` is no longer 0), the loop stops running, and the code proceeds to the next line.
- `print("Hello, nice to meet you " + name)`: Finally, after the loop ends, we greet the user with their name.

The `while` loop is perfect for situations where you need to repeat an action until a certain condition is met. It keeps checking the condition and continues to execute the code inside the loop until the condition becomes false.

Made by danilo.zs
