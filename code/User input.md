User input is the way that you, as a programmer can allow the user to send information. This can be through typing on a keyboard, clicking a mouse, and so on. In Python, we commonly use the keyboard to input data while the program is running.

To get user input in Python, you use the `input()` function. This function displays a prompt (a message to the user) and waits for the user to type something. Once the user presses Enter, the input captures what they typed as a string.

For example:
```
animal  =  input("What is your favorite animal? ")
print("My favorite animal is, " + animal + "!")
```
Now let's break it down:
- `animal` is the variable where the user's input will be saved.
- `input()` is the function that captures the user's response.
- `What is your favorite animal? "` is the prompt that the user will see before entering anything.
- `print("My favorite animal is, " + animal + "!")` is how we display the user's response.

To take a numerical input, A.K.A an integer, you need to call the `int()` function.

For example:
```
age  =  int(input("How old are you? "))
print("I'm " + age + " years old!")
```
Now let's break it down.
- `age` is the variable where the user's input will be saved.
- `int()` is the function that will converts the user's response into an integer.
- `input()` is the function that captures the user's response.
- `"How old are you? "` is the prompt that the user will see before entering anything.
- `print("I'm " + str(age) + " years old!")`  is how we display the user's response. Notice how the `age` variable is converted back into a string using the `str()` function. This lets us print the number as a string. If we don't convert it back to a string, the code will likely result in an error, so keep that in mind.

Note: You can use the `float()` function if you want to convert the input to a float number. Just type float() instead of int()

Furthermore, if you want to perform a mathematical operation using the user's input and you forget to convert their input to an integer, you can always do it in the `print()` function. Let's watch this closer:

```
print("Do you want to know how old are you going to be in 56589 years from now?")
age  =   input("How old are you? ")
print(int(age) + 56589)
```
Notice how I didn't use the `int()` function in the input. You can always use it afterward, but remember that this is not a good practice and your code won't look neat and clean. Also, remember that the `input()` function converts everything into a string.

Made by danilo.zs
