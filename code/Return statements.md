The `return` statement is used in functions to send back a result to the caller. It allows a function to produce a value that can be used elsewhere in your code.

## Basic example
```
def multiply(number1, number2):
    results = number1 * number2
    return results
```
In this function, `multiply` takes two parameters and computes their product. The `return` statement sends this computed value back to where the function was called.

To use the function:
```
number1 = int(input("Introduce a number: "))
number2 = int(input("Introduce another number: "))

x = multiply(number1, number2)

print(x)
```
Here, `multiply(number1, number2)` computes the product and returns it. The result is stored in the variable `x`, which is then printed.

Using `return` is important because it allows functions to send results back, making your code more modular and easier to manage. Without `return`, a function would only execute its statements without giving any output to the rest of the program.

Made by danilo.zs
