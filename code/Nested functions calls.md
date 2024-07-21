Nested function calls involve using the result of one function as the input for another function. This can make your code more concise by eliminating intermediate variables.

## Basic example without nested functions
```
num = input("Enter a whole positive number: ")
num = float(num)
num = abs(num)
num = round(num)

print(num)
```
Here, `num` is processed through multiple steps, with each step modifying the value before the final output.

## Basic example with nested functions
```
print(round(abs(float(input("Put a whole positive number: ")))))
```
In this version, `input()` is immediately converted to a float, then `abs()` is applied, and the result is rounded, all in one line. This reduces the need for temporary variables and makes your code shorter and often easier to read.

Made by danilo.zs
